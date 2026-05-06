const state = {
  data: null,
  cardsById: new Map(),
  expanded: new Set(["root"]),
  selectedNode: null,
  filteredIds: null,
  transform: { x: 60, y: 80, k: 1 },
  dragging: null,
};

const KIND_COLOR = {
  root: "#111827",
  motivation: "#1f77b4",
  angle: "#009b72",
  subproblem: "#d97706",
  solution: "#7c3aed",
  paper: "#334155",
};

const svg = document.getElementById("mindmap");
const paperGrid = document.getElementById("paperGrid");
const selectionTitle = document.getElementById("selectionTitle");
const selectionMeta = document.getElementById("selectionMeta");
const resultCount = document.getElementById("resultCount");

function el(name, attrs = {}, children = []) {
  const node = document.createElementNS("http://www.w3.org/2000/svg", name);
  for (const [key, value] of Object.entries(attrs)) {
    node.setAttribute(key, value);
  }
  for (const child of children) node.appendChild(child);
  return node;
}

function htmlEl(selector) {
  return document.querySelector(selector);
}

function truncate(text, len = 38) {
  if (!text) return "";
  return text.length > len ? `${text.slice(0, len - 1)}…` : text;
}

function unique(values) {
  return [...new Set(values.filter(Boolean))].sort((a, b) => a.localeCompare(b));
}

function nodeKey(node, path = []) {
  return [...path, node.kind, node.name].join("/");
}

function annotateTree(node, path = []) {
  node.key = nodeKey(node, path);
  node.parentPath = path;
  node.children?.forEach((child) => annotateTree(child, [...path, `${node.kind}:${node.name}`]));
}

function walk(node, visit) {
  visit(node);
  node.children?.forEach((child) => walk(child, visit));
}

function cardMatchesFilters(card) {
  const q = htmlEl("#searchInput").value.trim().toLowerCase();
  const motivation = htmlEl("#motivationFilter").value;
  const angle = htmlEl("#angleFilter").value;
  const solution = htmlEl("#solutionFilter").value;
  if (q && !card.search_text.includes(q)) return false;
  if (motivation && card.motivation !== motivation) return false;
  if (angle && card.angle !== angle) return false;
  if (solution && card.solution_family !== solution) return false;
  return true;
}

function updateFilteredIds() {
  const active = ["#searchInput", "#motivationFilter", "#angleFilter", "#solutionFilter"].some((sel) => {
    const value = htmlEl(sel).value;
    return value && value.trim() !== "";
  });
  if (!active) {
    state.filteredIds = null;
    return;
  }
  const ids = state.data.cards.filter(cardMatchesFilters).map((card) => card.arxiv_id);
  state.filteredIds = new Set(ids);
  expandBranchesForMatches();
}

function nodeVisibleByFilter(node) {
  if (!state.filteredIds) return true;
  return node.paper_ids?.some((id) => state.filteredIds.has(id));
}

function expandBranchesForMatches() {
  if (!state.filteredIds) return;
  walk(state.data.tree, (node) => {
    if (node.children?.length && nodeVisibleByFilter(node)) {
      state.expanded.add(node.key);
    }
  });
}

function visibleChildren(node) {
  if (!node.children?.length) return [];
  if (!state.expanded.has(node.key)) return [];
  return node.children.filter(nodeVisibleByFilter);
}

function layoutTree(root) {
  const rows = [];
  const positioned = [];

  function visit(node, depth) {
    const children = visibleChildren(node);
    if (!children.length) {
      const y = rows.length * 54;
      rows.push(node);
      positioned.push({ node, depth, x: depth * 280, y });
      return y;
    }
    const ys = children.map((child) => visit(child, depth + 1));
    const y = (Math.min(...ys) + Math.max(...ys)) / 2;
    positioned.push({ node, depth, x: depth * 280, y });
    return y;
  }

  visit(root, 0);
  const byKey = new Map(positioned.map((d) => [d.node.key, d]));
  const links = [];
  for (const d of positioned) {
    for (const child of visibleChildren(d.node)) {
      const c = byKey.get(child.key);
      if (c) links.push({ source: d, target: c });
    }
  }
  return { nodes: positioned, links };
}

function applyTransform(group) {
  const { x, y, k } = state.transform;
  group.setAttribute("transform", `translate(${x},${y}) scale(${k})`);
}

function renderMindmap() {
  svg.innerHTML = "";
  const { nodes, links } = layoutTree(state.data.tree);
  const group = el("g", { class: "viewport" });
  applyTransform(group);
  svg.appendChild(group);

  for (const link of links) {
    const sx = link.source.x + 14;
    const sy = link.source.y;
    const tx = link.target.x - 14;
    const ty = link.target.y;
    const mid = (sx + tx) / 2;
    group.appendChild(el("path", {
      class: "link",
      d: `M ${sx} ${sy} C ${mid} ${sy}, ${mid} ${ty}, ${tx} ${ty}`,
    }));
  }

  for (const item of nodes) {
    const node = item.node;
    const g = el("g", {
      class: `node ${node.kind}${state.selectedNode?.key === node.key ? " selected" : ""}`,
      transform: `translate(${item.x},${item.y})`,
      role: "button",
      tabindex: "0",
    });
    const radius = node.kind === "paper" ? 6 : node.kind === "root" ? 12 : 9;
    g.appendChild(el("circle", {
      r: radius,
      fill: KIND_COLOR[node.kind] || "#334155",
    }));
    const label = el("text", {
      x: radius + 8,
      y: -4,
    });
    label.textContent = truncate(node.name, node.kind === "paper" ? 36 : 46);
    const count = el("text", {
      class: "count",
      x: radius + 8,
      y: 13,
    });
    const childHint = node.children?.length ? (state.expanded.has(node.key) ? "−" : "+") : "";
    count.textContent = `${node.count || 0} papers ${childHint}`;
    g.appendChild(label);
    g.appendChild(count);
    g.addEventListener("click", (event) => {
      event.stopPropagation();
      selectNode(node);
      if (node.children?.length) {
        if (state.expanded.has(node.key)) state.expanded.delete(node.key);
        else state.expanded.add(node.key);
      }
      render();
    });
    group.appendChild(g);
  }
}

function selectNode(node) {
  state.selectedNode = node;
}

function cardsForSelection() {
  const ids = state.selectedNode?.paper_ids || state.data.tree.paper_ids;
  const filtered = state.filteredIds ? ids.filter((id) => state.filteredIds.has(id)) : ids;
  return filtered.map((id) => state.cardsById.get(id)).filter(Boolean);
}

function renderCards() {
  const cards = cardsForSelection();
  const node = state.selectedNode || state.data.tree;
  selectionTitle.textContent = node.kind === "root" ? "All Papers" : node.name;
  selectionMeta.textContent = `${cards.length} papers in this branch${state.filteredIds ? " after filters" : ""}.`;
  resultCount.textContent = `${cards.length} shown`;

  paperGrid.innerHTML = "";
  const template = document.getElementById("paperCardTemplate");
  const displayCards = cards.slice(0, 160);
  for (const card of displayCards) {
    const fragment = template.content.cloneNode(true);
    const article = fragment.querySelector(".paper-card");
    article.dataset.id = card.arxiv_id;
    const image = fragment.querySelector(".paper-image");
    image.src = card.method_figure;
    image.alt = `${card.title} method diagram`;
    fragment.querySelector(".thumb-button").addEventListener("click", () => window.open(card.method_figure, "_blank"));
    fragment.querySelector(".paper-meta").textContent = `${card.arxiv_id} · ${card.source_group} · ${card.code_status || "not checked"}`;
    fragment.querySelector("h3").textContent = card.title;
    fragment.querySelector(".one-liner").textContent = card.one_liner;
    fragment.querySelector("dd.motivation").textContent = card.motivation;
    fragment.querySelector("dd.angle").textContent = card.angle;
    fragment.querySelector("dd.subproblem").textContent = card.subproblem;
    fragment.querySelector("dd.solution").textContent = card.solution_family;
    const pdf = fragment.querySelector("a.pdf");
    pdf.href = card.pdf_path;
    const fig = fragment.querySelector("a.figure");
    fig.href = card.method_figure;
    const code = fragment.querySelector("a.code");
    if (card.code_url) code.href = card.code_url;
    else code.hidden = true;
    paperGrid.appendChild(fragment);
  }
  if (cards.length > displayCards.length) {
    const more = document.createElement("p");
    more.className = "one-liner";
    more.textContent = `Showing first ${displayCards.length} cards. Use search or click deeper branches to narrow this set.`;
    paperGrid.appendChild(more);
  }
}

function renderStats() {
  const stats = document.getElementById("stats");
  stats.innerHTML = "<h2>Dataset</h2>";
  const rows = [
    ["Total papers", state.data.stats.total],
    ["2026 arXiv", state.data.stats.source_group.find((x) => x.name === "2026-arxiv")?.count || 0],
    ["Classic pre-2026", state.data.stats.source_group.find((x) => x.name === "curated-pre2026")?.count || 0],
    ["Code candidates", state.data.cards.filter((c) => c.code_url).length],
  ];
  for (const [label, value] of rows) {
    const row = document.createElement("div");
    row.className = "stat-row";
    row.innerHTML = `<span>${label}</span><strong>${value}</strong>`;
    stats.appendChild(row);
  }
}

function populateFilters() {
  const fields = [
    ["motivationFilter", "motivation"],
    ["angleFilter", "angle"],
    ["solutionFilter", "solution_family"],
  ];
  for (const [id, field] of fields) {
    const select = document.getElementById(id);
    for (const value of unique(state.data.cards.map((card) => card[field]))) {
      const option = document.createElement("option");
      option.value = value;
      option.textContent = value;
      select.appendChild(option);
    }
  }
}

function render() {
  renderMindmap();
  renderCards();
}

function resetView() {
  state.transform = { x: 60, y: 80, k: 1 };
  renderMindmap();
}

function expandToDepth(maxDepth) {
  state.expanded.clear();
  function visit(node, depth) {
    if (depth <= maxDepth) state.expanded.add(node.key);
    node.children?.forEach((child) => visit(child, depth + 1));
  }
  visit(state.data.tree, 0);
  render();
}

function collapseAll() {
  state.expanded.clear();
  state.expanded.add(state.data.tree.key);
  render();
}

function attachInteractions() {
  ["searchInput", "motivationFilter", "angleFilter", "solutionFilter"].forEach((id) => {
    document.getElementById(id).addEventListener("input", () => {
      updateFilteredIds();
      selectNode(state.data.tree);
      render();
    });
  });
  document.getElementById("resetView").addEventListener("click", resetView);
  document.getElementById("expandAll").addEventListener("click", () => expandToDepth(2));
  document.getElementById("collapseAll").addEventListener("click", collapseAll);

  svg.addEventListener("wheel", (event) => {
    event.preventDefault();
    const delta = event.deltaY > 0 ? 0.9 : 1.1;
    state.transform.k = Math.max(0.25, Math.min(2.6, state.transform.k * delta));
    renderMindmap();
  }, { passive: false });

  svg.addEventListener("pointerdown", (event) => {
    state.dragging = { x: event.clientX, y: event.clientY, tx: state.transform.x, ty: state.transform.y };
    svg.setPointerCapture(event.pointerId);
  });
  svg.addEventListener("pointermove", (event) => {
    if (!state.dragging) return;
    state.transform.x = state.dragging.tx + event.clientX - state.dragging.x;
    state.transform.y = state.dragging.ty + event.clientY - state.dragging.y;
    renderMindmap();
  });
  svg.addEventListener("pointerup", () => {
    state.dragging = null;
  });
}

async function init() {
  const response = await fetch("./mindmap-data.json");
  state.data = await response.json();
  annotateTree(state.data.tree);
  state.cardsById = new Map(state.data.cards.map((card) => [card.arxiv_id, card]));
  state.selectedNode = state.data.tree;
  populateFilters();
  renderStats();
  attachInteractions();
  expandToDepth(1);
}

init().catch((error) => {
  document.body.innerHTML = `<pre style="padding:24px;color:#b91c1c">Failed to load mindmap data:\n${error.stack || error}</pre>`;
});
