# Boardmix 脑图构建摘要

## Motivation
- 动态场景与 4D 重建: 210
- 实时/大规模/高效 3D 表示: 155
- 多视角几何/表面/场景重建: 148
- 生成式 3D/4D 内容与仿真: 104
- SLAM/机器人/自动驾驶世界模型: 96
- 稀疏/单目/少视角 3D 重建: 88
- 人体/头像/可动画资产: 29
- 领域/传感器特化重建: 9

## 切入点
- 表示/几何角度: 255
- 时空/动态角度: 210
- 训练/监督角度: 200
- 计算角度: 68
- 生成/世界模型角度: 67
- 内存/存储角度: 22
- 系统/在线部署角度: 14
- 数据/传感角度: 3

## 子问题
- 建模运动/形变/时间一致性: 194
- 解决稀疏视角几何不稳定: 169
- 提升几何一致性/表面质量: 146
- 提升可控生成/世界演化预测: 143
- 降低显存/存储/模型体积: 86
- 减少优化/采样/渲染步骤: 42
- 接入 SLAM/机器人闭环系统: 34
- 提升泛化/跨场景/开放世界能力: 17
- 适配特殊传感器/行业场景: 8

## 解法族
- SLAM / pose graph / online mapping pipeline: 252
- Gaussian Splatting 表示与正则化: 189
- Motion decomposition / canonical space / deformation: 103
- Diffusion/生成先验/视频模型: 93
- SDF/隐式表面/网格/点云: 51
- NeRF/辐射场/体渲染: 47
- Feed-forward / Transformer / Foundation Model: 47
- Pruning / compression / progressive coding: 36
- Sensor/domain-specific pipeline: 14
- 组合式/混合 pipeline: 7

## 代码状态
- code_link_found_not_audited: 485
- no_code_link_found: 354
