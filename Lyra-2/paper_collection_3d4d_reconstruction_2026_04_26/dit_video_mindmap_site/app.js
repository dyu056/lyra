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
  for (const [key, value] of Object.entries(attrs)) node.setAttribute(key, value);
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

function citationCount(item) {
  return Number.parseInt(item?.citation_count || 0, 10) || 0;
}

function sortCardsByCitation(cards) {
  return [...cards].sort((a, b) => {
    const byCitation = citationCount(b) - citationCount(a);
    if (byCitation) return byCitation;
    const byDate = (b.published || "").localeCompare(a.published || "");
    if (byDate) return byDate;
    return (a.title || "").localeCompare(b.title || "");
  });
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
    if (node.children?.length && nodeVisibleByFilter(node)) state.expanded.add(node.key);
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
  let cursorY = 0;
  const depthGap = 310;

  function visit(node, depth) {
    const children = visibleChildren(node);
    if (!children.length) {
      const y = cursorY;
      cursorY += node.kind === "paper" ? 82 : 58;
      rows.push(node);
      positioned.push({ node, depth, x: depth * depthGap, y });
      return y;
    }
    const ys = children.map((child) => visit(child, depth + 1));
    const y = (Math.min(...ys) + Math.max(...ys)) / 2;
    positioned.push({ node, depth, x: depth * depthGap, y });
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

function focusNode(item) {
  const bounds = svg.getBoundingClientRect();
  state.transform.x = 42 - item.x * state.transform.k;
  state.transform.y = Math.min(150, bounds.height * 0.5 - item.y * state.transform.k);
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
    g.appendChild(el("circle", { r: radius, fill: KIND_COLOR[node.kind] || "#334155" }));
    const isPaper = node.kind === "paper";
    const label = el("text", { x: radius + 8, y: isPaper ? -20 : -4 });
    label.textContent = isPaper
      ? `${citationCount(node)} cites · ${truncate(node.title || node.name, 58)}`
      : truncate(node.name, 46);
    const count = el("text", { class: "count", x: radius + 8, y: isPaper ? 34 : 13 });
    const childHint = node.children?.length ? (state.expanded.has(node.key) ? "−" : "+") : "";
    count.textContent = isPaper
      ? `${node.arxiv_id || ""} · ${node.year || ""}`
      : `${node.count || 0} papers ${childHint}`;
    g.appendChild(label);
    if (isPaper) {
      const method = el("text", { class: "method", x: radius + 8, y: -2 });
      method.textContent = `Method: ${truncate(node.method, 62)}`;
      const description = el("text", { class: "description", x: radius + 8, y: 16 });
      description.textContent = `Desc: ${truncate(node.description, 82)}`;
      g.appendChild(method);
      g.appendChild(description);
    }
    g.appendChild(count);
    g.addEventListener("click", (event) => {
      event.stopPropagation();
      selectNode(node);
      if (node.children?.length) {
        state.expanded.add(node.key);
        focusNode(item);
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
  return sortCardsByCitation(filtered.map((id) => state.cardsById.get(id)).filter(Boolean));
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
    fragment.querySelector(".paper-meta").textContent = `${card.arxiv_id} · ${card.year} · ${citationCount(card)} cites · ${card.source_group}`;
    fragment.querySelector("h3").textContent = card.title;
    fragment.querySelector(".one-liner").textContent = card.one_liner;
    fragment.querySelector("dd.motivation").textContent = card.motivation;
    fragment.querySelector("dd.angle").textContent = card.angle;
    fragment.querySelector("dd.subproblem").textContent = card.subproblem;
    fragment.querySelector("dd.solution").textContent = card.solution_family;
    fragment.querySelector("a.paper").href = card.abs_url;
    fragment.querySelector("a.pdf").href = card.pdf_path || card.abs_url;
    fragment.querySelector("a.figure").href = card.method_figure;
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
  const source = new Map(state.data.stats.source_group.map((x) => [x.name, x.count]));
  const rows = [
    ["Total papers", state.data.stats.total],
    ["2026 arXiv", source.get("2026-arxiv") || 0],
    ["Classic pre-2026", source.get("curated-pre2026") || 0],
    ["Method diagrams", state.data.cards.filter((c) => c.method_figure).length],
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
  document.getElementById("expandAll").addEventListener("click", () => expandToDepth(4));
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
  const response = await fetch("./data/mindmap.json");
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
