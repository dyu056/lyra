# 3D/4D 重建与世界模型论文问题-切入点脑图

> Boardmix 导入建议：用 Boardmix 的文本/Markdown 生成思维导图，或先导入 XMind/Markdown。每个 paper 叶子节点附一句话方案、代码状态、PDF 和 method figure 路径。

## Motivation：SLAM/机器人/自动驾驶世界模型（96）
### 切入点：时空/动态角度（15）
#### 子问题：建模运动/形变/时间一致性（1）
##### 解法族：Motion decomposition / canonical space / deformation（1）
###### MotionScape ｜ 2604.07991
- Paper：MotionScape: A Large-Scale Real-World Highly Dynamic UAV Video Dataset for World Models
- 一句话：MotionScape 针对「建模运动/形变/时间一致性」，从「时空/动态角度」切入，主要采用「Motion decomposition / canonical space / deformation」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2604.07991](method_figures/2604.07991_MotionScape.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_MotionScape_A_Large_Scale_Real_World_Highly_Dynamic_UAV_Video_Dataset_for_World_Models_2604.07991.pdf
- Code：https://github.com/Thelegendzz/MotionScape（code_link_found_not_audited）

#### 子问题：接入 SLAM/机器人闭环系统（1）
##### 解法族：NeRF/辐射场/体渲染（1）
###### Tiny-DroNeRF ｜ 2603.01850
- Paper：Tiny-DroNeRF: Tiny Neural Radiance Fields aboard Federated Learning-enabled Nano-drones
- 一句话：Tiny-DroNeRF 针对「接入 SLAM/机器人闭环系统」，从「时空/动态角度」切入，主要采用「NeRF/辐射场/体渲染」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2603.01850](method_figures/2603.01850_Tiny-DroNeRF.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Tiny_DroNeRF_Tiny_Neural_Radiance_Fields_aboard_Federated_Learning_enabled_Nano_drones_2603.01850.pdf

#### 子问题：提升可控生成/世界演化预测（12）
##### 解法族：Diffusion/生成先验/视频模型（10；另有 7 篇见 full/csv）
###### Bridging Scene Generation and Planning ｜ 2603.14948
- Paper：Bridging Scene Generation and Planning: Driving with World Model via Unifying Vision and Motion Representation
- 一句话：Bridging Scene Generation and Planning 针对「提升可控生成/世界演化预测」，从「时空/动态角度」切入，主要采用「Diffusion/生成先验/视频模型」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2603.14948](method_figures/2603.14948_Bridging_Scene_Generation_and_Planning.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Bridging_Scene_Generation_and_Planning_Driving_with_World_Model_via_Unifying_Vision_and_Mo_2603.14948.pdf
- Code：https://github.com/TabGuigui/WorldDrive（code_link_found_not_audited）
###### ConsisDrive ｜ 2602.03213
- Paper：ConsisDrive: Identity-Preserving Driving World Models for Video Generation by Instance Mask
- 一句话：ConsisDrive 针对「提升可控生成/世界演化预测」，从「时空/动态角度」切入，主要采用「Diffusion/生成先验/视频模型」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2602.03213](method_figures/2602.03213_ConsisDrive.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_ConsisDrive_Identity_Preserving_Driving_World_Models_for_Video_Generation_by_Instance_Mask_2602.03213.pdf
###### Human-Robot ｜ 2601.01705
- Paper：Explicit World Models for Reliable Human-Robot Collaboration
- 一句话：Human-Robot 针对「提升可控生成/世界演化预测」，从「时空/动态角度」切入，主要采用「Diffusion/生成先验/视频模型」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2601.01705](method_figures/2601.01705_Human-Robot.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Explicit_World_Models_for_Reliable_Human_Robot_Collaboration_2601.01705.pdf

##### 解法族：Motion decomposition / canonical space / deformation（1）
###### RoboStereo ｜ 2603.12639
- Paper：RoboStereo: Dual-Tower 4D Embodied World Models for Unified Policy Optimization
- 一句话：RoboStereo 针对「提升可控生成/世界演化预测」，从「时空/动态角度」切入，主要采用「Motion decomposition / canonical space / deformation」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2603.12639](method_figures/2603.12639_RoboStereo.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_RoboStereo_Dual_Tower_4D_Embodied_World_Models_for_Unified_Policy_Optimization_2603.12639.pdf
- Code：https://github.com/LAION-AI/aesthetic-predictor（code_link_found_not_audited）

##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### 本文方法 ｜ 2604.20151
- Paper：Toward Safe Autonomous Robotic Endovascular Interventions using World Models
- 一句话：本文方法 针对「提升可控生成/世界演化预测」，从「时空/动态角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2604.20151](method_figures/2604.20151_paper.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Toward_Safe_Autonomous_Robotic_Endovascular_Interventions_using_World_Models_2604.20151.pdf

#### 子问题：提升泛化/跨场景/开放世界能力（1）
##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### Learning to unfold cloth ｜ 2602.16675
- Paper：Learning to unfold cloth: Scaling up world models to deformable object manipulation
- 一句话：Learning to unfold cloth 针对「提升泛化/跨场景/开放世界能力」，从「时空/动态角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2602.16675](method_figures/2602.16675_Learning_to_unfold_cloth.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Learning_to_unfold_cloth_Scaling_up_world_models_to_deformable_object_manipulation_2602.16675.pdf

### 切入点：生成/世界模型角度（35）
#### 子问题：提升可控生成/世界演化预测（35）
##### 解法族：Diffusion/生成先验/视频模型（15；另有 12 篇见 full/csv）
###### World-Model-Based ｜ 2604.11302
- Paper：3D-Anchored Lookahead Planning for Persistent Robotic Scene Memory via World-Model-Based MCTS
- 一句话：World-Model-Based 针对「提升可控生成/世界演化预测」，从「生成/世界模型角度」切入，主要采用「Diffusion/生成先验/视频模型」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2604.11302](method_figures/2604.11302_World-Model-Based.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_3D_Anchored_Lookahead_Planning_for_Persistent_Robotic_Scene_Memory_via_World_Model_Based_M_2604.11302.pdf
###### ABot-PhysWorld ｜ 2603.23376
- Paper：ABot-PhysWorld: Interactive World Foundation Model for Robotic Manipulation with Physics Alignment
- 一句话：ABot-PhysWorld 针对「提升可控生成/世界演化预测」，从「生成/世界模型角度」切入，主要采用「Diffusion/生成先验/视频模型」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2603.23376](method_figures/2603.23376_ABot-PhysWorld.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_ABot_PhysWorld_Interactive_World_Foundation_Model_for_Robotic_Manipulation_with_Physics_Al_2603.23376.pdf
- Code：https://github.com/amap-cvlab/ABot-PhysWorld（code_link_found_not_audited）
###### BridgeV2W ｜ 2602.03793
- Paper：BridgeV2W: Bridging Video Generation Models to Embodied World Models via Embodiment Masks
- 一句话：BridgeV2W 针对「提升可控生成/世界演化预测」，从「生成/世界模型角度」切入，主要采用「Diffusion/生成先验/视频模型」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2602.03793](method_figures/2602.03793_BridgeV2W.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_BridgeV2W_Bridging_Video_Generation_Models_to_Embodied_World_Models_via_Embodiment_Masks_2602.03793.pdf

##### 解法族：Feed-forward / Transformer / Foundation Model（3）
###### Causal World Modeling for Robot Control ｜ 2601.21998
- Paper：Causal World Modeling for Robot Control
- 一句话：Causal World Modeling for Robot Control 针对「提升可控生成/世界演化预测」，从「生成/世界模型角度」切入，主要采用「Feed-forward / Transformer / Foundation Model」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2601.21998](method_figures/2601.21998_Causal_World_Modeling_for_Robot_Control.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Causal_World_Modeling_for_Robot_Control_2601.21998.pdf
- Code：https://github.com/UT-HCRL/LEGATO（code_link_found_not_audited）
###### LLMs ｜ 2604.10690
- Paper：Do LLMs Build Spatial World Models? Evidence from Grid-World Maze Tasks
- 一句话：LLMs 针对「提升可控生成/世界演化预测」，从「生成/世界模型角度」切入，主要采用「Feed-forward / Transformer / Foundation Model」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2604.10690](method_figures/2604.10690_LLMs.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Do_LLMs_Build_Spatial_World_Models_Evidence_from_Grid_World_Maze_Tasks_2604.10690.pdf
- Code：https://github.com/likenneth/othello_world/（code_link_found_not_audited）
###### UniDWM ｜ 2602.01536
- Paper：UniDWM: Towards a Unified Driving World Model via Multifaceted Representation Learning
- 一句话：UniDWM 针对「提升可控生成/世界演化预测」，从「生成/世界模型角度」切入，主要采用「Feed-forward / Transformer / Foundation Model」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2602.01536](method_figures/2602.01536_UniDWM.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_UniDWM_Towards_a_Unified_Driving_World_Model_via_Multifaceted_Representation_Learning_2602.01536.pdf
- Code：https://github.com/Say2L/UniDWM（code_link_found_not_audited）

##### 解法族：Gaussian Splatting 表示与正则化（2）
###### NavGSim ｜ 2603.15186
- Paper：NavGSim: High-Fidelity Gaussian Splatting Simulator for Large-Scale Navigation
- 一句话：NavGSim 针对「提升可控生成/世界演化预测」，从「生成/世界模型角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2603.15186](method_figures/2603.15186_NavGSim.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_NavGSim_High_Fidelity_Gaussian_Splatting_Simulator_for_Large_Scale_Navigation_2603.15186.pdf
###### Policy-Guided ｜ 2603.25981
- Paper：Policy-Guided World Model Planning for Language-Conditioned Visual Navigation
- 一句话：Policy-Guided 针对「提升可控生成/世界演化预测」，从「生成/世界模型角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2603.25981](method_figures/2603.25981_Policy-Guided.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Policy_Guided_World_Model_Planning_for_Language_Conditioned_Visual_Navigation_2603.25981.pdf
- Code：https://github.com/AmirhoseinCh/PiJEPA.git（code_link_found_not_audited）

##### 解法族：Pruning / compression / progressive coding（1）
###### Where Bits Matter in World Model Planning ｜ 2602.11882
- Paper：Where Bits Matter in World Model Planning: A Paired Mixed-Bit Study for Efficient Spatial Reasoning
- 一句话：Where Bits Matter in World Model Planning 针对「提升可控生成/世界演化预测」，从「生成/世界模型角度」切入，主要采用「Pruning / compression / progressive coding」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2602.11882](method_figures/2602.11882_Where_Bits_Matter_in_World_Model_Planning.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Where_Bits_Matter_in_World_Model_Planning_A_Paired_Mixed_Bit_Study_for_Efficient_Spatial_R_2602.11882.pdf
- Code：https://github.com/suraj-ranganath/DINO-MBQuant（code_link_found_not_audited）

##### 解法族：SLAM / pose graph / online mapping pipeline（14；另有 11 篇见 full/csv）
###### Multi-Modal ｜ 2601.12277
- Paper：An Efficient and Multi-Modal Navigation System with One-Step World Model
- 一句话：Multi-Modal 针对「提升可控生成/世界演化预测」，从「生成/世界模型角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2601.12277](method_figures/2601.12277_Multi-Modal.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_An_Efficient_and_Multi_Modal_Navigation_System_with_One_Step_World_Model_2601.12277.pdf
- Code：https://github.com/robotnav-bot/NOW（code_link_found_not_audited）
###### AtomVLA ｜ 2603.08519
- Paper：AtomVLA: Scalable Post-Training for Robotic Manipulation via Predictive Latent World Models
- 一句话：AtomVLA 针对「提升可控生成/世界演化预测」，从「生成/世界模型角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2603.08519](method_figures/2603.08519_AtomVLA.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_AtomVLA_Scalable_Post_Training_for_Robotic_Manipulation_via_Predictive_Latent_World_Models_2603.08519.pdf
###### Zero-Shot ｜ 2603.13825
- Paper：Building Explicit World Model for Zero-Shot Open-World Object Manipulation
- 一句话：Zero-Shot 针对「提升可控生成/世界演化预测」，从「生成/世界模型角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2603.13825](method_figures/2603.13825_Zero-Shot.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Building_Explicit_World_Model_for_Zero_Shot_Open_World_Object_Manipulation_2603.13825.pdf

### 切入点：系统/在线部署角度（7）
#### 子问题：接入 SLAM/机器人闭环系统（4）
##### 解法族：SLAM / pose graph / online mapping pipeline（3）
###### CAVERS ｜ 2604.15052
- Paper：CAVERS: Multimodal SLAM Data from a Natural Karstic Cave with Ground Truth Motion Capture
- 一句话：CAVERS 针对「接入 SLAM/机器人闭环系统」，从「系统/在线部署角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2604.15052](method_figures/2604.15052_CAVERS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_CAVERS_Multimodal_SLAM_Data_from_a_Natural_Karstic_Cave_with_Ground_Truth_Motion_Capture_2604.15052.pdf
- Code：https://github.com/spaceuma/cavers（code_link_found_not_audited）
###### SLAM ｜ 2603.17229
- Paper：Visual SLAM with DEM Anchoring for Lunar Surface Navigation
- 一句话：SLAM 针对「接入 SLAM/机器人闭环系统」，从「系统/在线部署角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2603.17229](method_figures/2603.17229_SLAM.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Visual_SLAM_with_DEM_Anchoring_for_Lunar_Surface_Navigation_2603.17229.pdf
- Code：https://github.com/MichaelGrupp/evo（code_link_found_not_audited）
###### pySpatial ｜ 2603.00905
- Paper：pySpatial: Generating 3D Visual Programs for Zero-Shot Spatial Reasoning
- 一句话：pySpatial 针对「接入 SLAM/机器人闭环系统」，从「系统/在线部署角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2603.00905](method_figures/2603.00905_pySpatial.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_pySpatial_Generating_3D_Visual_Programs_for_Zero_Shot_Spatial_Reasoning_2603.00905.pdf
- Code：https://github.com/Zhanpeng1202/pySpatial（code_link_found_not_audited）

##### 解法族：组合式/混合 pipeline（1）
###### 本文方法 ｜ 2603.05876
- Paper：Systematic Evaluation of Novel View Synthesis for Video Place Recognition
- 一句话：本文方法 针对「接入 SLAM/机器人闭环系统」，从「系统/在线部署角度」切入，主要采用「组合式/混合 pipeline」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2603.05876](method_figures/2603.05876_paper.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Systematic_Evaluation_of_Novel_View_Synthesis_for_Video_Place_Recognition_2603.05876.pdf

#### 子问题：提升可控生成/世界演化预测（1）
##### 解法族：Feed-forward / Transformer / Foundation Model（1）
###### From Perception to Action ｜ 2602.01644
- Paper：From Perception to Action: Spatial AI Agents and World Models
- 一句话：From Perception to Action 针对「提升可控生成/世界演化预测」，从「系统/在线部署角度」切入，主要采用「Feed-forward / Transformer / Foundation Model」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2602.01644](method_figures/2602.01644_From_Perception_to_Action.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_From_Perception_to_Action_Spatial_AI_Agents_and_World_Models_2602.01644.pdf
- Code：https://github.com/Significant-Gravitas/Auto-GPT（code_link_found_not_audited）

#### 子问题：解决稀疏视角几何不稳定（2）
##### 解法族：SLAM / pose graph / online mapping pipeline（2）
###### SCE-SLAM ｜ 2601.09665
- Paper：SCE-SLAM: Scale-Consistent Monocular SLAM via Scene Coordinate Embeddings
- 一句话：SCE-SLAM 针对「解决稀疏视角几何不稳定」，从「系统/在线部署角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2601.09665](method_figures/2601.09665_SCE-SLAM.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_SCE_SLAM_Scale_Consistent_Monocular_SLAM_via_Scene_Coordinate_Embeddings_2601.09665.pdf
###### SpatialAnt ｜ 2603.26837
- Paper：SpatialAnt: Autonomous Zero-Shot Robot Navigation via Active Scene Reconstruction and Visual Anticipation
- 一句话：SpatialAnt 针对「解决稀疏视角几何不稳定」，从「系统/在线部署角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2603.26837](method_figures/2603.26837_SpatialAnt.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_SpatialAnt_Autonomous_Zero_Shot_Robot_Navigation_via_Active_Scene_Reconstruction_and_Visua_2603.26837.pdf
- Code：https://github.com/IMNearth/Spatial-X（code_link_found_not_audited）

### 切入点：表示/几何角度（16）
#### 子问题：接入 SLAM/机器人闭环系统（2）
##### 解法族：Gaussian Splatting 表示与正则化（1）
###### 3DGSNav ｜ 2602.12159
- Paper：3DGSNav: Enhancing Vision-Language Model Reasoning for Object Navigation via Active 3D Gaussian Splatting
- 一句话：3DGSNav 针对「接入 SLAM/机器人闭环系统」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2602.12159](method_figures/2602.12159_3DGSNav.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_3DGSNav_Enhancing_Vision_Language_Model_Reasoning_for_Object_Navigation_via_Active_3D_Gaus_2602.12159.pdf
- Code：https://github.com/eliahuhorwitz/Academic-project-page-template（code_link_found_not_audited）

##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### 本文方法 ｜ 2602.13909
- Paper：High-fidelity 3D reconstruction for planetary exploration
- 一句话：本文方法 针对「接入 SLAM/机器人闭环系统」，从「表示/几何角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2602.13909](method_figures/2602.13909_paper.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_High_fidelity_3D_reconstruction_for_planetary_exploration_2602.13909.pdf

#### 子问题：提升几何一致性/表面质量（6）
##### 解法族：Gaussian Splatting 表示与正则化（2）
###### NeRF ｜ 2604.18205
- Paper：A Comparative Evaluation of Geometric Accuracy in NeRF and Gaussian Splatting
- 一句话：NeRF 针对「提升几何一致性/表面质量」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2604.18205](method_figures/2604.18205_NeRF.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_A_Comparative_Evaluation_of_Geometric_Accuracy_in_NeRF_and_Gaussian_Splatting_2604.18205.pdf
###### SplatBus ｜ 2601.15431
- Paper：SplatBus: A Gaussian Splatting Viewer Framework via GPU Interprocess Communication
- 一句话：SplatBus 针对「提升几何一致性/表面质量」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2601.15431](method_figures/2601.15431_SplatBus.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_SplatBus_A_Gaussian_Splatting_Viewer_Framework_via_GPU_Interprocess_Communication_2601.15431.pdf
- Code：https://github.com/RockyXu66/splatbus（code_link_found_not_audited）

##### 解法族：Pruning / compression / progressive coding（1）
###### Multi-Traversal ｜ 2604.05908
- Paper：Appearance Decomposition Gaussian Splatting for Multi-Traversal Reconstruction
- 一句话：Multi-Traversal 针对「提升几何一致性/表面质量」，从「表示/几何角度」切入，主要采用「Pruning / compression / progressive coding」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2604.05908](method_figures/2604.05908_Multi-Traversal.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Appearance_Decomposition_Gaussian_Splatting_for_Multi_Traversal_Reconstruction_2604.05908.pdf
- Code：https://github.com/IRMVLab/ADM-GS（code_link_found_not_audited）

##### 解法族：SLAM / pose graph / online mapping pipeline（2）
###### ParkGaussian ｜ 2601.01386
- Paper：ParkGaussian: Surround-view 3D Gaussian Splatting for Autonomous Parking
- 一句话：ParkGaussian 针对「提升几何一致性/表面质量」，从「表示/几何角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2601.01386](method_figures/2601.01386_ParkGaussian.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_ParkGaussian_Surround_view_3D_Gaussian_Splatting_for_Autonomous_Parking_2601.01386.pdf
- Code：https://github.com/wm-research/ParkGaussian（code_link_found_not_audited）
###### to-3D ｜ 2603.27797
- Paper：Which Reconstruction Model Should a Robot Use? Routing Image-to-3D Models for Cost-Aware Robotic Manipulation
- 一句话：to-3D 针对「提升几何一致性/表面质量」，从「表示/几何角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2603.27797](method_figures/2603.27797_to-3D.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Which_Reconstruction_Model_Should_a_Robot_Use_Routing_Image_to_3D_Models_for_Cost_Aware_Ro_2603.27797.pdf
- Code：https://github.com/scout-model-routing/scout（code_link_found_not_audited）

##### 解法族：Sensor/domain-specific pipeline（1）
###### FlowTouch ｜ 2603.08255
- Paper：FlowTouch: View-Invariant Visuo-Tactile Prediction
- 一句话：FlowTouch 针对「提升几何一致性/表面质量」，从「表示/几何角度」切入，主要采用「Sensor/domain-specific pipeline」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2603.08255](method_figures/2603.08255_FlowTouch.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_FlowTouch_View_Invariant_Visuo_Tactile_Prediction_2603.08255.pdf
- Code：https://github.com/flowtouch/flowtouch（code_link_found_not_audited）

#### 子问题：提升可控生成/世界演化预测（3）
##### 解法族：Gaussian Splatting 表示与正则化（3）
###### AstroSplat ｜ 2603.11969
- Paper：AstroSplat: Physics-Based Gaussian Splatting for Rendering and Reconstruction of Small Celestial Bodies
- 一句话：AstroSplat 针对「提升可控生成/世界演化预测」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2603.11969](method_figures/2603.11969_AstroSplat.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_AstroSplat_Physics_Based_Gaussian_Splatting_for_Rendering_and_Reconstruction_of_Small_Cele_2603.11969.pdf
###### 本文方法 ｜ 2602.08266
- Paper：Informative Object-centric Next Best View for Object-aware 3D Gaussian Splatting in Cluttered Scenes
- 一句话：本文方法 针对「提升可控生成/世界演化预测」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2602.08266](method_figures/2602.08266_paper.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Informative_Object_centric_Next_Best_View_for_Object_aware_3D_Gaussian_Splatting_in_Clutte_2602.08266.pdf
###### PhotoAgent ｜ 2603.22796
- Paper：PhotoAgent: A Robotic Photographer with Spatial and Aesthetic Understanding
- 一句话：PhotoAgent 针对「提升可控生成/世界演化预测」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2603.22796](method_figures/2603.22796_PhotoAgent.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_PhotoAgent_A_Robotic_Photographer_with_Spatial_and_Aesthetic_Understanding_2603.22796.pdf

#### 子问题：解决稀疏视角几何不稳定（2）
##### 解法族：Gaussian Splatting 表示与正则化（1）
###### 本文方法 ｜ 2602.17124
- Paper：3D Scene Rendering with Multimodal Gaussian Splatting
- 一句话：本文方法 针对「解决稀疏视角几何不稳定」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2602.17124](method_figures/2602.17124_paper.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_3D_Scene_Rendering_with_Multimodal_Gaussian_Splatting_2602.17124.pdf

##### 解法族：NeRF/辐射场/体渲染（1）
###### 本文方法 ｜ 2601.03869
- Paper：Bayesian Monocular Depth Refinement via Neural Radiance Fields
- 一句话：本文方法 针对「解决稀疏视角几何不稳定」，从「表示/几何角度」切入，主要采用「NeRF/辐射场/体渲染」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2601.03869](method_figures/2601.03869_paper.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Bayesian_Monocular_Depth_Refinement_via_Neural_Radiance_Fields_2601.03869.pdf

#### 子问题：降低显存/存储/模型体积（3）
##### 解法族：Gaussian Splatting 表示与正则化（2）
###### 本文方法 ｜ 2601.07540
- Paper：Enhancing Novel View Synthesis via Geometry Grounded Set Diffusion
- 一句话：本文方法 针对「降低显存/存储/模型体积」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2601.07540](method_figures/2601.07540_paper.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Enhancing_Novel_View_Synthesis_via_Geometry_Grounded_Set_Diffusion_2601.07540.pdf
- Code：https://github.com/eliahuhorwitz/Academic-project-page-template（code_link_found_not_audited）
###### GSMem ｜ 2603.19137
- Paper：GSMem: 3D Gaussian Splatting as Persistent Spatial Memory for Zero-Shot Embodied Exploration and Reasoning
- 一句话：GSMem 针对「降低显存/存储/模型体积」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2603.19137](method_figures/2603.19137_GSMem.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_GSMem_3D_Gaussian_Splatting_as_Persistent_Spatial_Memory_for_Zero_Shot_Embodied_Exploratio_2603.19137.pdf

##### 解法族：NeRF/辐射场/体渲染（1）
###### Physically-Based ｜ 2602.13549
- Paper：Nighttime Autonomous Driving Scene Reconstruction with Physically-Based Gaussian Splatting
- 一句话：Physically-Based 针对「降低显存/存储/模型体积」，从「表示/几何角度」切入，主要采用「NeRF/辐射场/体渲染」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2602.13549](method_figures/2602.13549_Physically-Based.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Nighttime_Autonomous_Driving_Scene_Reconstruction_with_Physically_Based_Gaussian_Splatting_2602.13549.pdf

### 切入点：计算角度（3）
#### 子问题：建模运动/形变/时间一致性（1）
##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### RobotPan ｜ 2604.13476
- Paper：RobotPan: A 360$^\circ$ Surround-View Robotic Vision System for Embodied Perception
- 一句话：RobotPan 针对「建模运动/形变/时间一致性」，从「计算角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2604.13476](method_figures/2604.13476_RobotPan.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_RobotPan_A_360_circ_Surround_View_Robotic_Vision_System_for_Embodied_Perception_2604.13476.pdf

#### 子问题：接入 SLAM/机器人闭环系统（1）
##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### VGGT-SLAM 2.0 ｜ 2601.19887
- Paper：VGGT-SLAM 2.0: Real-time Dense Feed-forward Scene Reconstruction
- 一句话：VGGT-SLAM 2.0 针对「接入 SLAM/机器人闭环系统」，从「计算角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2601.19887](method_figures/2601.19887_VGGT-SLAM_2.0.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_VGGT_SLAM_2_0_Real_time_Dense_Feed_forward_Scene_Reconstruction_2601.19887.pdf
- Code：https://github.com/MIT-SPARK/VGGT-SLAM（code_link_found_not_audited）

#### 子问题：解决稀疏视角几何不稳定（1）
##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### 本文方法 ｜ 2603.17236
- Paper：Neural Radiance Maps for Extraterrestrial Navigation and Path Planning
- 一句话：本文方法 针对「解决稀疏视角几何不稳定」，从「计算角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2603.17236](method_figures/2603.17236_paper.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Neural_Radiance_Maps_for_Extraterrestrial_Navigation_and_Path_Planning_2603.17236.pdf
- Code：https://github.com/adamdai/rover_nerf_planning（code_link_found_not_audited）

### 切入点：训练/监督角度（20）
#### 子问题：提升几何一致性/表面质量（3）
##### 解法族：NeRF/辐射场/体渲染（1）
###### To View Transform or Not to View Transform ｜ 2603.28090
- Paper：To View Transform or Not to View Transform: NeRF-based Pre-training Perspective
- 一句话：To View Transform or Not to View Transform 针对「提升几何一致性/表面质量」，从「训练/监督角度」切入，主要采用「NeRF/辐射场/体渲染」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2603.28090](method_figures/2603.28090_To_View_Transform_or_Not_to_View_Transform.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_To_View_Transform_or_Not_to_View_Transform_NeRF_based_Pre_training_Perspective_2603.28090.pdf
- Code：https://github.com/open-mmlab/mmdetection3d（code_link_found_not_audited）

##### 解法族：Sensor/domain-specific pipeline（1）
###### TouchAnything ｜ 2604.08945
- Paper：TouchAnything: Diffusion-Guided 3D Reconstruction from Sparse Robot Touches
- 一句话：TouchAnything 针对「提升几何一致性/表面质量」，从「训练/监督角度」切入，主要采用「Sensor/domain-specific pipeline」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2604.08945](method_figures/2604.08945_TouchAnything.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_TouchAnything_Diffusion_Guided_3D_Reconstruction_from_Sparse_Robot_Touches_2604.08945.pdf
- Code：https://github.com/nerfies/nerfies.github.io（code_link_found_not_audited）

##### 解法族：组合式/混合 pipeline（1）
###### 4DRC-OCC ｜ 2603.07794
- Paper：4DRC-OCC: Robust Semantic Occupancy Prediction Through Fusion of 4D Radar and Camera
- 一句话：4DRC-OCC 针对「提升几何一致性/表面质量」，从「训练/监督角度」切入，主要采用「组合式/混合 pipeline」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2603.07794](method_figures/2603.07794_4DRC-OCC.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_4DRC_OCC_Robust_Semantic_Occupancy_Prediction_Through_Fusion_of_4D_Radar_and_Camera_2603.07794.pdf

#### 子问题：提升可控生成/世界演化预测（12）
##### 解法族：Diffusion/生成先验/视频模型（2）
###### Persistent Robot World Models ｜ 2603.25685
- Paper：Persistent Robot World Models: Stabilizing Multi-Step Rollouts via Reinforcement Learning
- 一句话：Persistent Robot World Models 针对「提升可控生成/世界演化预测」，从「训练/监督角度」切入，主要采用「Diffusion/生成先验/视频模型」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2603.25685](method_figures/2603.25685_Persistent_Robot_World_Models.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Persistent_Robot_World_Models_Stabilizing_Multi_Step_Rollouts_via_Reinforcement_Learning_2603.25685.pdf
- Code：https://github.com/KellerJordan/Muon（code_link_found_not_audited）
###### Risk-Aware ｜ 2602.23259
- Paper：Risk-Aware World Model Predictive Control for Generalizable End-to-End Autonomous Driving
- 一句话：Risk-Aware 针对「提升可控生成/世界演化预测」，从「训练/监督角度」切入，主要采用「Diffusion/生成先验/视频模型」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2602.23259](method_figures/2602.23259_Risk-Aware.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Risk_Aware_World_Model_Predictive_Control_for_Generalizable_End_to_End_Autonomous_Driving_2602.23259.pdf
- Code：https://github.com/Thinklab-SJTU/Bench2Drive/tree/main（code_link_found_not_audited）

##### 解法族：Feed-forward / Transformer / Foundation Model（2）
###### 3D-Mix for VLA ｜ 2603.24393
- Paper：3D-Mix for VLA: A Plug-and-Play Module for Integrating VGGT-based 3D Information into Vision-Language-Action Models
- 一句话：3D-Mix for VLA 针对「提升可控生成/世界演化预测」，从「训练/监督角度」切入，主要采用「Feed-forward / Transformer / Foundation Model」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2603.24393](method_figures/2603.24393_3D-Mix_for_VLA.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_3D_Mix_for_VLA_A_Plug_and_Play_Module_for_Integrating_VGGT_based_3D_Information_into_Visio_2603.24393.pdf
- Code：https://github.com/ZGC-EmbodyAI/3DMix-for-VLA（code_link_found_not_audited）
###### DriveTok ｜ 2603.19219
- Paper：DriveTok: 3D Driving Scene Tokenization for Unified Multi-View Reconstruction and Understanding
- 一句话：DriveTok 针对「提升可控生成/世界演化预测」，从「训练/监督角度」切入，主要采用「Feed-forward / Transformer / Foundation Model」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2603.19219](method_figures/2603.19219_DriveTok.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_DriveTok_3D_Driving_Scene_Tokenization_for_Unified_Multi_View_Reconstruction_and_Understan_2603.19219.pdf
- Code：https://github.com/paryi555/DriveTok（code_link_found_not_audited）

##### 解法族：Motion decomposition / canonical space / deformation（1）
###### DLWM ｜ 2604.00969
- Paper：DLWM: Dual Latent World Models enable Holistic Gaussian-centric Pre-training in Autonomous Driving
- 一句话：DLWM 针对「提升可控生成/世界演化预测」，从「训练/监督角度」切入，主要采用「Motion decomposition / canonical space / deformation」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2604.00969](method_figures/2604.00969_DLWM.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_DLWM_Dual_Latent_World_Models_enable_Holistic_Gaussian_centric_Pre_training_in_Autonomous_2604.00969.pdf

##### 解法族：SLAM / pose graph / online mapping pipeline（7；另有 4 篇见 full/csv）
###### Drive-JEPA ｜ 2601.22032
- Paper：Drive-JEPA: Video JEPA Meets Multimodal Trajectory Distillation for End-to-End Driving
- 一句话：Drive-JEPA 针对「提升可控生成/世界演化预测」，从「训练/监督角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2601.22032](method_figures/2601.22032_Drive-JEPA.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Drive_JEPA_Video_JEPA_Meets_Multimodal_Trajectory_Distillation_for_End_to_End_Driving_2601.22032.pdf
- Code：https://github.com/linhanwang/Drive-JEPA（code_link_found_not_audited）
###### Hi-WM ｜ 2604.21741
- Paper：Hi-WM: Human-in-the-World-Model for Scalable Robot Post-Training
- 一句话：Hi-WM 针对「提升可控生成/世界演化预测」，从「训练/监督角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2604.21741](method_figures/2604.21741_Hi-WM.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Hi_WM_Human_in_the_World_Model_for_Scalable_Robot_Post_Training_2604.21741.pdf
###### LaST-VLA ｜ 2603.01928
- Paper：LaST-VLA: Thinking in Latent Spatio-Temporal Space for Vision-Language-Action in Autonomous Driving
- 一句话：LaST-VLA 针对「提升可控生成/世界演化预测」，从「训练/监督角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2603.01928](method_figures/2603.01928_LaST-VLA.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_LaST_VLA_Thinking_in_Latent_Spatio_Temporal_Space_for_Vision_Language_Action_in_Autonomous_2603.01928.pdf
- Code：https://github.com/luo-yc17/LaST-VLA（code_link_found_not_audited）

#### 子问题：提升泛化/跨场景/开放世界能力（3）
##### 解法族：Feed-forward / Transformer / Foundation Model（1）
###### WorldFlow3D ｜ 2603.29089
- Paper：WorldFlow3D: Flowing Through 3D Distributions for Unbounded World Generation
- 一句话：WorldFlow3D 针对「提升泛化/跨场景/开放世界能力」，从「训练/监督角度」切入，主要采用「Feed-forward / Transformer / Foundation Model」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2603.29089](method_figures/2603.29089_WorldFlow3D.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_WorldFlow3D_Flowing_Through_3D_Distributions_for_Unbounded_World_Generation_2603.29089.pdf

##### 解法族：NeRF/辐射场/体渲染（1）
###### 本文方法 ｜ 2602.10943
- Paper：Towards Learning a Generalizable 3D Scene Representation from 2D Observations
- 一句话：本文方法 针对「提升泛化/跨场景/开放世界能力」，从「训练/监督角度」切入，主要采用「NeRF/辐射场/体渲染」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2602.10943](method_figures/2602.10943_paper.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Towards_Learning_a_Generalizable_3D_Scene_Representation_from_2D_Observations_2602.10943.pdf

##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### to-Geometry ｜ 2604.12908
- Paper：Robotic Manipulation is Vision-to-Geometry Mapping ($f(v) \rightarrow G$): Vision-Geometry Backbones over Language and Video Models
- 一句话：to-Geometry 针对「提升泛化/跨场景/开放世界能力」，从「训练/监督角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2604.12908](method_figures/2604.12908_to-Geometry.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Robotic_Manipulation_is_Vision_to_Geometry_Mapping_f_v_rightarrow_G_Vision_Geometry_Backbo_2604.12908.pdf

#### 子问题：解决稀疏视角几何不稳定（2）
##### 解法族：Gaussian Splatting 表示与正则化（1）
###### VG3S ｜ 2603.06210
- Paper：VG3S: Visual Geometry Grounded Gaussian Splatting for Semantic Occupancy Prediction
- 一句话：VG3S 针对「解决稀疏视角几何不稳定」，从「训练/监督角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2603.06210](method_figures/2603.06210_VG3S.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_VG3S_Visual_Geometry_Grounded_Gaussian_Splatting_for_Semantic_Occupancy_Prediction_2603.06210.pdf

##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### Asset Harvester ｜ 2604.18468
- Paper：Asset Harvester: Extracting 3D Assets from Autonomous Driving Logs for Simulation
- 一句话：Asset Harvester 针对「解决稀疏视角几何不稳定」，从「训练/监督角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「SLAM/机器人/自动驾驶世界模型」。
- Method diagram：![2604.18468](method_figures/2604.18468_Asset_Harvester.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Asset_Harvester_Extracting_3D_Assets_from_Autonomous_Driving_Logs_for_Simulation_2604.18468.pdf
- Code：https://github.com/NVIDIA/asset-harvester（code_link_found_not_audited）

## Motivation：人体/头像/可动画资产（29）
### 切入点：时空/动态角度（9）
#### 子问题：建模运动/形变/时间一致性（5）
##### 解法族：Motion decomposition / canonical space / deformation（3）
###### ESGaussianFace ｜ 2601.01847
- Paper：ESGaussianFace: Emotional and Stylized Audio-Driven Facial Animation via 3D Gaussian Splatting
- 一句话：ESGaussianFace 针对「建模运动/形变/时间一致性」，从「时空/动态角度」切入，主要采用「Motion decomposition / canonical space / deformation」来服务「人体/头像/可动画资产」。
- Method diagram：![2601.01847](method_figures/2601.01847_ESGaussianFace.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_ESGaussianFace_Emotional_and_Stylized_Audio_Driven_Facial_Animation_via_3D_Gaussian_Splatt_2601.01847.pdf
###### JOintGS ｜ 2602.04317
- Paper：JOintGS: Joint Optimization of Cameras, Bodies and 3D Gaussians for In-the-Wild Monocular Reconstruction
- 一句话：JOintGS 针对「建模运动/形变/时间一致性」，从「时空/动态角度」切入，主要采用「Motion decomposition / canonical space / deformation」来服务「人体/头像/可动画资产」。
- Method diagram：![2602.04317](method_figures/2602.04317_JOintGS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_JOintGS_Joint_Optimization_of_Cameras_Bodies_and_3D_Gaussians_for_In_the_Wild_Monocular_Re_2602.04317.pdf
- Code：https://github.com/MiliLab/JOintGS（code_link_found_not_audited）
###### Structure-Aware ｜ 2604.09324
- Paper：Structure-Aware Fine-Grained Gaussian Splatting for Expressive Avatar Reconstruction
- 一句话：Structure-Aware 针对「建模运动/形变/时间一致性」，从「时空/动态角度」切入，主要采用「Motion decomposition / canonical space / deformation」来服务「人体/头像/可动画资产」。
- Method diagram：![2604.09324](method_figures/2604.09324_Structure-Aware.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Structure_Aware_Fine_Grained_Gaussian_Splatting_for_Expressive_Avatar_Reconstruction_2604.09324.pdf
- Code：https://github.com/Su245811YZ/SFGS（code_link_found_not_audited）

##### 解法族：SDF/隐式表面/网格/点云（1）
###### MV-Fashion ｜ 2603.08147
- Paper：MV-Fashion: Towards Enabling Virtual Try-On and Size Estimation with Multi-View Paired Data
- 一句话：MV-Fashion 针对「建模运动/形变/时间一致性」，从「时空/动态角度」切入，主要采用「SDF/隐式表面/网格/点云」来服务「人体/头像/可动画资产」。
- Method diagram：![2603.08147](method_figures/2603.08147_MV-Fashion.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_MV_Fashion_Towards_Enabling_Virtual_Try_On_and_Size_Estimation_with_Multi_View_Paired_Data_2603.08147.pdf
- Code：https://github.com/HunorLaczko/MV-Fashion（code_link_found_not_audited）

##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### Gaussian Wardrobe ｜ 2603.04290
- Paper：Gaussian Wardrobe: Compositional 3D Gaussian Avatars for Free-Form Virtual Try-On
- 一句话：Gaussian Wardrobe 针对「建模运动/形变/时间一致性」，从「时空/动态角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「人体/头像/可动画资产」。
- Method diagram：![2603.04290](method_figures/2603.04290_Gaussian_Wardrobe.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Gaussian_Wardrobe_Compositional_3D_Gaussian_Avatars_for_Free_Form_Virtual_Try_On_2603.04290.pdf

#### 子问题：提升几何一致性/表面质量（1）
##### 解法族：Motion decomposition / canonical space / deformation（1）
###### CLOTH-HUGS ｜ 2604.15875
- Paper：CLOTH-HUGS: Cloth Aware Human Gaussian Splatting
- 一句话：CLOTH-HUGS 针对「提升几何一致性/表面质量」，从「时空/动态角度」切入，主要采用「Motion decomposition / canonical space / deformation」来服务「人体/头像/可动画资产」。
- Method diagram：![2604.15875](method_figures/2604.15875_CLOTH-HUGS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_CLOTH_HUGS_Cloth_Aware_Human_Gaussian_Splatting_2604.15875.pdf

#### 子问题：提升可控生成/世界演化预测（1）
##### 解法族：Motion decomposition / canonical space / deformation（1）
###### LOME ｜ 2603.27449
- Paper：LOME: Learning Human-Object Manipulation with Action-Conditioned Egocentric World Model
- 一句话：LOME 针对「提升可控生成/世界演化预测」，从「时空/动态角度」切入，主要采用「Motion decomposition / canonical space / deformation」来服务「人体/头像/可动画资产」。
- Method diagram：![2603.27449](method_figures/2603.27449_LOME.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_LOME_Learning_Human_Object_Manipulation_with_Action_Conditioned_Egocentric_World_Model_2603.27449.pdf

#### 子问题：解决稀疏视角几何不稳定（1）
##### 解法族：Gaussian Splatting 表示与正则化（1）
###### VRGaussianAvatar ｜ 2602.01674
- Paper：VRGaussianAvatar: Integrating 3D Gaussian Avatars into VR
- 一句话：VRGaussianAvatar 针对「解决稀疏视角几何不稳定」，从「时空/动态角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「人体/头像/可动画资产」。
- Method diagram：![2602.01674](method_figures/2602.01674_VRGaussianAvatar.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_VRGaussianAvatar_Integrating_3D_Gaussian_Avatars_into_VR_2602.01674.pdf
- Code：https://github.com/hailsong/VRGaussianAvatar（code_link_found_not_audited）

#### 子问题：降低显存/存储/模型体积（1）
##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### OFERA ｜ 2602.01748
- Paper：OFERA: Blendshape-driven 3D Gaussian Control for Occluded Facial Expression to Realistic Avatars in VR
- 一句话：OFERA 针对「降低显存/存储/模型体积」，从「时空/动态角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「人体/头像/可动画资产」。
- Method diagram：![2602.01748](method_figures/2602.01748_OFERA.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_OFERA_Blendshape_driven_3D_Gaussian_Control_for_Occluded_Facial_Expression_to_Realistic_Av_2602.01748.pdf

### 切入点：表示/几何角度（9）
#### 子问题：建模运动/形变/时间一致性（2）
##### 解法族：Gaussian Splatting 表示与正则化（1）
###### UniMGS ｜ 2601.19233
- Paper：UniMGS: Unifying Mesh and 3D Gaussian Splatting with Single-Pass Rasterization and Proxy-Based Deformation
- 一句话：UniMGS 针对「建模运动/形变/时间一致性」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「人体/头像/可动画资产」。
- Method diagram：![2601.19233](method_figures/2601.19233_UniMGS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_UniMGS_Unifying_Mesh_and_3D_Gaussian_Splatting_with_Single_Pass_Rasterization_and_Proxy_Ba_2601.19233.pdf

##### 解法族：Motion decomposition / canonical space / deformation（1）
###### PartNerFace ｜ 2604.13918
- Paper：PartNerFace: Part-based Neural Radiance Fields for Animatable Facial Avatar Reconstruction
- 一句话：PartNerFace 针对「建模运动/形变/时间一致性」，从「表示/几何角度」切入，主要采用「Motion decomposition / canonical space / deformation」来服务「人体/头像/可动画资产」。
- Method diagram：![2604.13918](method_figures/2604.13918_PartNerFace.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_PartNerFace_Part_based_Neural_Radiance_Fields_for_Animatable_Facial_Avatar_Reconstruction_2604.13918.pdf

#### 子问题：接入 SLAM/机器人闭环系统（1）
##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### SurgCalib ｜ 2603.08983
- Paper：SurgCalib: Gaussian Splatting-Based Hand-Eye Calibration for Robot-Assisted Minimally Invasive Surgery
- 一句话：SurgCalib 针对「接入 SLAM/机器人闭环系统」，从「表示/几何角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「人体/头像/可动画资产」。
- Method diagram：![2603.08983](method_figures/2603.08983_SurgCalib.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_SurgCalib_Gaussian_Splatting_Based_Hand_Eye_Calibration_for_Robot_Assisted_Minimally_Invas_2603.08983.pdf

#### 子问题：提升几何一致性/表面质量（4）
##### 解法族：Diffusion/生成先验/视频模型（1）
###### GeoDiff4D ｜ 2602.24161
- Paper：GeoDiff4D: Geometry-Aware Diffusion for 4D Head Avatar Reconstruction
- 一句话：GeoDiff4D 针对「提升几何一致性/表面质量」，从「表示/几何角度」切入，主要采用「Diffusion/生成先验/视频模型」来服务「人体/头像/可动画资产」。
- Method diagram：![2602.24161](method_figures/2602.24161_GeoDiff4D.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_GeoDiff4D_Geometry_Aware_Diffusion_for_4D_Head_Avatar_Reconstruction_2602.24161.pdf

##### 解法族：Gaussian Splatting 表示与正则化（2）
###### Real-Time ｜ 2604.10259
- Paper：Real-Time Human Reconstruction and Animation using Feed-Forward Gaussian Splatting
- 一句话：Real-Time 针对「提升几何一致性/表面质量」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「人体/头像/可动画资产」。
- Method diagram：![2604.10259](method_figures/2604.10259_Real-Time.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Real_Time_Human_Reconstruction_and_Animation_using_Feed_Forward_Gaussian_Splatting_2604.10259.pdf
- Code：https://github.com/Devdoot57/HumanGS（code_link_found_not_audited）
###### TIDI-GS ｜ 2601.09291
- Paper：TIDI-GS: Floater Suppression in 3D Gaussian Splatting for Enhanced Indoor Scene Fidelity
- 一句话：TIDI-GS 针对「提升几何一致性/表面质量」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「人体/头像/可动画资产」。
- Method diagram：![2601.09291](method_figures/2601.09291_TIDI-GS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_TIDI_GS_Floater_Suppression_in_3D_Gaussian_Splatting_for_Enhanced_Indoor_Scene_Fidelity_2601.09291.pdf

##### 解法族：SDF/隐式表面/网格/点云（1）
###### SARS ｜ 2602.09918
- Paper：SARS: A Novel Face and Body Shape and Appearance Aware 3D Reconstruction System extends Morphable Models
- 一句话：SARS 针对「提升几何一致性/表面质量」，从「表示/几何角度」切入，主要采用「SDF/隐式表面/网格/点云」来服务「人体/头像/可动画资产」。
- Method diagram：![2602.09918](method_figures/2602.09918_SARS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_SARS_A_Novel_Face_and_Body_Shape_and_Appearance_Aware_3D_Reconstruction_System_extends_Mor_2602.09918.pdf

#### 子问题：解决稀疏视角几何不稳定（1）
##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### OAHuman ｜ 2603.14249
- Paper：OAHuman: Occlusion-Aware 3D Human Reconstruction from Monocular Images
- 一句话：OAHuman 针对「解决稀疏视角几何不稳定」，从「表示/几何角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「人体/头像/可动画资产」。
- Method diagram：![2603.14249](method_figures/2603.14249_OAHuman.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_OAHuman_Occlusion_Aware_3D_Human_Reconstruction_from_Monocular_Images_2603.14249.pdf
- Code：https://github.com/black-forest-labs/flux（code_link_found_not_audited）

#### 子问题：降低显存/存储/模型体积（1）
##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### ProgressiveAvatars ｜ 2603.16447
- Paper：ProgressiveAvatars: Progressive Animatable 3D Gaussian Avatars
- 一句话：ProgressiveAvatars 针对「降低显存/存储/模型体积」，从「表示/几何角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「人体/头像/可动画资产」。
- Method diagram：![2603.16447](method_figures/2603.16447_ProgressiveAvatars.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_ProgressiveAvatars_Progressive_Animatable_3D_Gaussian_Avatars_2603.16447.pdf

### 切入点：计算角度（4）
#### 子问题：减少优化/采样/渲染步骤（1）
##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### Any3DAvatar ｜ 2604.13856
- Paper：Any3DAvatar: Fast and High-Quality Full-Head 3D Avatar Reconstruction from Single Portrait Image
- 一句话：Any3DAvatar 针对「减少优化/采样/渲染步骤」，从「计算角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「人体/头像/可动画资产」。
- Method diagram：![2604.13856](method_figures/2604.13856_Any3DAvatar.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Any3DAvatar_Fast_and_High_Quality_Full_Head_3D_Avatar_Reconstruction_from_Single_Portrait_2604.13856.pdf

#### 子问题：提升几何一致性/表面质量（2）
##### 解法族：Feed-forward / Transformer / Foundation Model（2）
###### GRAFT ｜ 2604.19624
- Paper：GRAFT: Geometric Refinement and Fitting Transformer for Human Scene Reconstruction
- 一句话：GRAFT 针对「提升几何一致性/表面质量」，从「计算角度」切入，主要采用「Feed-forward / Transformer / Foundation Model」来服务「人体/头像/可动画资产」。
- Method diagram：![2604.19624](method_figures/2604.19624_GRAFT.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_GRAFT_Geometric_Refinement_and_Fitting_Transformer_for_Human_Scene_Reconstruction_2604.19624.pdf
- Code：https://github.com/pradyumnaym/graft（code_link_found_not_audited）
###### HD-VGGT ｜ 2603.27222
- Paper：HD-VGGT: High-Resolution Visual Geometry Transformer
- 一句话：HD-VGGT 针对「提升几何一致性/表面质量」，从「计算角度」切入，主要采用「Feed-forward / Transformer / Foundation Model」来服务「人体/头像/可动画资产」。
- Method diagram：![2603.27222](method_figures/2603.27222_HD-VGGT.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_HD_VGGT_High_Resolution_Visual_Geometry_Transformer_2603.27222.pdf

#### 子问题：解决稀疏视角几何不稳定（1）
##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### Full-Head ｜ 2601.12770
- Paper：Generalizable and Animatable 3D Full-Head Gaussian Avatar from a Single Image
- 一句话：Full-Head 针对「解决稀疏视角几何不稳定」，从「计算角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「人体/头像/可动画资产」。
- Method diagram：![2601.12770](method_figures/2601.12770_Full-Head.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Generalizable_and_Animatable_3D_Full_Head_Gaussian_Avatar_from_a_Single_Image_2601.12770.pdf
- Code：https://github.com/ShaelynZ/fhavatar（code_link_found_not_audited）

### 切入点：训练/监督角度（7）
#### 子问题：建模运动/形变/时间一致性（1）
##### 解法族：Gaussian Splatting 表示与正则化（1）
###### Splat-Portrait ｜ 2601.18633
- Paper：Splat-Portrait: Generalizing Talking Heads with Gaussian Splatting
- 一句话：Splat-Portrait 针对「建模运动/形变/时间一致性」，从「训练/监督角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「人体/头像/可动画资产」。
- Method diagram：![2601.18633](method_figures/2601.18633_Splat-Portrait.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Splat_Portrait_Generalizing_Talking_Heads_with_Gaussian_Splatting_2601.18633.pdf
- Code：https://github.com/stonewalking/Splat-portrait（code_link_found_not_audited）

#### 子问题：接入 SLAM/机器人闭环系统（1）
##### 解法族：Gaussian Splatting 表示与正则化（1）
###### ReaDy-Go ｜ 2602.11575
- Paper：ReaDy-Go: Real-to-Sim Dynamic 3D Gaussian Splatting Simulation for Environment-Specific Visual Navigation with Moving Obstacles
- 一句话：ReaDy-Go 针对「接入 SLAM/机器人闭环系统」，从「训练/监督角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「人体/头像/可动画资产」。
- Method diagram：![2602.11575](method_figures/2602.11575_ReaDy-Go.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_ReaDy_Go_Real_to_Sim_Dynamic_3D_Gaussian_Splatting_Simulation_for_Environment_Specific_Vis_2602.11575.pdf
- Code：https://github.com/google/nerfies/releases/tag/0.1（code_link_found_not_audited）

#### 子问题：提升几何一致性/表面质量（1）
##### 解法族：组合式/混合 pipeline（1）
###### NeuralFur ｜ 2601.12481
- Paper：NeuralFur: Animal Fur Reconstruction From Multi-View Images
- 一句话：NeuralFur 针对「提升几何一致性/表面质量」，从「训练/监督角度」切入，主要采用「组合式/混合 pipeline」来服务「人体/头像/可动画资产」。
- Method diagram：![2601.12481](method_figures/2601.12481_NeuralFur.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_NeuralFur_Animal_Fur_Reconstruction_From_Multi_View_Images_2601.12481.pdf
- Code：https://github.com/avaxman/Directional（code_link_found_not_audited）

#### 子问题：解决稀疏视角几何不稳定（3）
##### 解法族：Gaussian Splatting 表示与正则化（2）
###### AHOY ｜ 2603.17975
- Paper：AHOY! Animatable Humans under Occlusion from YouTube Videos with Gaussian Splatting and Video Diffusion Priors
- 一句话：AHOY 针对「解决稀疏视角几何不稳定」，从「训练/监督角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「人体/头像/可动画资产」。
- Method diagram：![2603.17975](method_figures/2603.17975_AHOY.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_AHOY_Animatable_Humans_under_Occlusion_from_YouTube_Videos_with_Gaussian_Splatting_and_Vid_2603.17975.pdf
###### LiftAvatar ｜ 2603.02129
- Paper：LiftAvatar: Kinematic-Space Completion for Expression-Controlled 3D Gaussian Avatar Animation
- 一句话：LiftAvatar 针对「解决稀疏视角几何不稳定」，从「训练/监督角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「人体/头像/可动画资产」。
- Method diagram：![2603.02129](method_figures/2603.02129_LiftAvatar.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_LiftAvatar_Kinematic_Space_Completion_for_Expression_Controlled_3D_Gaussian_Avatar_Animati_2603.02129.pdf

##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### MultiGO++ ｜ 2603.04993
- Paper：MultiGO++: Monocular 3D Clothed Human Reconstruction via Geometry-Texture Collaboration
- 一句话：MultiGO++ 针对「解决稀疏视角几何不稳定」，从「训练/监督角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「人体/头像/可动画资产」。
- Method diagram：![2603.04993](method_figures/2603.04993_MultiGO.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_MultiGO_Monocular_3D_Clothed_Human_Reconstruction_via_Geometry_Texture_Collaboration_2603.04993.pdf

#### 子问题：降低显存/存储/模型体积（1）
##### 解法族：Gaussian Splatting 表示与正则化（1）
###### LayerGS ｜ 2601.05853
- Paper：LayerGS: Decomposition and Inpainting of Layered 3D Human Avatars via 2D Gaussian Splatting
- 一句话：LayerGS 针对「降低显存/存储/模型体积」，从「训练/监督角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「人体/头像/可动画资产」。
- Method diagram：![2601.05853](method_figures/2601.05853_LayerGS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_LayerGS_Decomposition_and_Inpainting_of_Layered_3D_Human_Avatars_via_2D_Gaussian_Splatting_2601.05853.pdf
- Code：https://github.com/RockyXu66/LayerGS（code_link_found_not_audited）

## Motivation：动态场景与 4D 重建（210）
### 切入点：内存/存储角度（3）
#### 子问题：降低显存/存储/模型体积（3）
##### 解法族：Pruning / compression / progressive coding（2）
###### 本文方法 ｜ 2201.05989
- Paper：Instant Neural Graphics Primitives with a Multiresolution Hash Encoding
- 一句话：本文方法 针对「降低显存/存储/模型体积」，从「内存/存储角度」切入，主要采用「Pruning / compression / progressive coding」来服务「动态场景与 4D 重建」。
- Method diagram：![2201.05989](method_figures/2201.05989_paper.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2022_Instant_Neural_Graphics_Primitives_with_a_Multiresolution_Hash_Encoding_2201.05989.pdf
- Code：https://github.com/NVlabs/instant-ngp（code_link_found_not_audited）
###### Gaussians on a Diet ｜ 2604.20046
- Paper：Gaussians on a Diet: High-Quality Memory-Bounded 3D Gaussian Splatting Training
- 一句话：Gaussians on a Diet 针对「降低显存/存储/模型体积」，从「内存/存储角度」切入，主要采用「Pruning / compression / progressive coding」来服务「动态场景与 4D 重建」。
- Method diagram：![2604.20046](method_figures/2604.20046_Gaussians_on_a_Diet.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Gaussians_on_a_Diet_High_Quality_Memory_Bounded_3D_Gaussian_Splatting_Training_2604.20046.pdf

##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### StegoNGP ｜ 2603.00949
- Paper：StegoNGP: 3D Cryptographic Steganography using Instant-NGP
- 一句话：StegoNGP 针对「降低显存/存储/模型体积」，从「内存/存储角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「动态场景与 4D 重建」。
- Method diagram：![2603.00949](method_figures/2603.00949_StegoNGP.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_StegoNGP_3D_Cryptographic_Steganography_using_Instant_NGP_2603.00949.pdf
- Code：https://github.com/jiang-wenxiang/StegoNGP（code_link_found_not_audited）

### 切入点：时空/动态角度（133）
#### 子问题：建模运动/形变/时间一致性（108）
##### 解法族：Diffusion/生成先验/视频模型（5；另有 2 篇见 full/csv）
###### Fine-Tuning ｜ 2603.02619
- Paper：Direct Reward Fine-Tuning on Poses for Single Image to 3D Human in the Wild
- 一句话：Fine-Tuning 针对「建模运动/形变/时间一致性」，从「时空/动态角度」切入，主要采用「Diffusion/生成先验/视频模型」来服务「动态场景与 4D 重建」。
- Method diagram：![2603.02619](method_figures/2603.02619_Fine-Tuning.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Direct_Reward_Fine_Tuning_on_Poses_for_Single_Image_to_3D_Human_in_the_Wild_2603.02619.pdf
- Code：https://github.com/nerfies/nerfies.github.io（code_link_found_not_audited）
###### LiveWorld ｜ 2603.07145
- Paper：LiveWorld: Simulating Out-of-Sight Dynamics in Generative Video World Models
- 一句话：LiveWorld 针对「建模运动/形变/时间一致性」，从「时空/动态角度」切入，主要采用「Diffusion/生成先验/视频模型」来服务「动态场景与 4D 重建」。
- Method diagram：![2603.07145](method_figures/2603.07145_LiveWorld.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_LiveWorld_Simulating_Out_of_Sight_Dynamics_in_Generative_Video_World_Models_2603.07145.pdf
###### Phys4D ｜ 2603.03485
- Paper：Phys4D: Fine-Grained Physics-Consistent 4D Modeling from Video Diffusion
- 一句话：Phys4D 针对「建模运动/形变/时间一致性」，从「时空/动态角度」切入，主要采用「Diffusion/生成先验/视频模型」来服务「动态场景与 4D 重建」。
- Method diagram：![2603.03485](method_figures/2603.03485_Phys4D.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Phys4D_Fine_Grained_Physics_Consistent_4D_Modeling_from_Video_Diffusion_2603.03485.pdf

##### 解法族：Feed-forward / Transformer / Foundation Model（3）
###### MoRe ｜ 2603.05078
- Paper：MoRe: Motion-aware Feed-forward 4D Reconstruction Transformer
- 一句话：MoRe 针对「建模运动/形变/时间一致性」，从「时空/动态角度」切入，主要采用「Feed-forward / Transformer / Foundation Model」来服务「动态场景与 4D 重建」。
- Method diagram：![2603.05078](method_figures/2603.05078_MoRe.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_MoRe_Motion_aware_Feed_forward_4D_Reconstruction_Transformer_2603.05078.pdf
- Code：https://github.com/HellexF/MoRe（code_link_found_not_audited）
###### ReconDrive ｜ 2603.07552
- Paper：ReconDrive: Fast Feed-Forward 4D Gaussian Splatting for Autonomous Driving Scene Reconstruction
- 一句话：ReconDrive 针对「建模运动/形变/时间一致性」，从「时空/动态角度」切入，主要采用「Feed-forward / Transformer / Foundation Model」来服务「动态场景与 4D 重建」。
- Method diagram：![2603.07552](method_figures/2603.07552_ReconDrive.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_ReconDrive_Fast_Feed_Forward_4D_Gaussian_Splatting_for_Autonomous_Driving_Scene_Reconstruc_2603.07552.pdf
- Code：https://github.com/TuojingAI/ReconDrive（code_link_found_not_audited）
###### V-DPM ｜ 2601.09499
- Paper：V-DPM: 4D Video Reconstruction with Dynamic Point Maps
- 一句话：V-DPM 针对「建模运动/形变/时间一致性」，从「时空/动态角度」切入，主要采用「Feed-forward / Transformer / Foundation Model」来服务「动态场景与 4D 重建」。
- Method diagram：![2601.09499](method_figures/2601.09499_V-DPM.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_V_DPM_4D_Video_Reconstruction_with_Dynamic_Point_Maps_2601.09499.pdf

##### 解法族：Gaussian Splatting 表示与正则化（3）
###### GA-GS ｜ 2604.04331
- Paper：GA-GS: Generation-Assisted Gaussian Splatting for Static Scene Reconstruction
- 一句话：GA-GS 针对「建模运动/形变/时间一致性」，从「时空/动态角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「动态场景与 4D 重建」。
- Method diagram：![2604.04331](method_figures/2604.04331_GA-GS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_GA_GS_Generation_Assisted_Gaussian_Splatting_for_Static_Scene_Reconstruction_2604.04331.pdf
###### KGS-GCN ｜ 2603.16943
- Paper：KGS-GCN: Enhancing Sparse Skeleton Sensing via Kinematics-Driven Gaussian Splatting and Probabilistic Topology for Action Recognition
- 一句话：KGS-GCN 针对「建模运动/形变/时间一致性」，从「时空/动态角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「动态场景与 4D 重建」。
- Method diagram：![2603.16943](method_figures/2603.16943_KGS-GCN.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_KGS_GCN_Enhancing_Sparse_Skeleton_Sensing_via_Kinematics_Driven_Gaussian_Splatting_and_Pro_2603.16943.pdf
###### PanopticQuery ｜ 2604.05638
- Paper：PanopticQuery: Unified Query-Time Reasoning for 4D Scenes
- 一句话：PanopticQuery 针对「建模运动/形变/时间一致性」，从「时空/动态角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「动态场景与 4D 重建」。
- Method diagram：![2604.05638](method_figures/2604.05638_PanopticQuery.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_PanopticQuery_Unified_Query_Time_Reasoning_for_4D_Scenes_2604.05638.pdf

##### 解法族：Motion decomposition / canonical space / deformation（68；另有 65 篇见 full/csv）
###### Real-Time ｜ 2310.08528
- Paper：4D Gaussian Splatting for Real-Time Dynamic Scene Rendering
- 一句话：Real-Time 针对「建模运动/形变/时间一致性」，从「时空/动态角度」切入，主要采用「Motion decomposition / canonical space / deformation」来服务「动态场景与 4D 重建」。
- Method diagram：![2310.08528](method_figures/2310.08528_Real-Time.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2024_4D_Gaussian_Splatting_for_Real_Time_Dynamic_Scene_Rendering_2310.08528.pdf
- Code：https://github.com/hustvl/4DGaussians（code_link_found_not_audited）
###### D-NeRF ｜ 2011.13961
- Paper：D-NeRF: Neural Radiance Fields for Dynamic Scenes
- 一句话：D-NeRF 针对「建模运动/形变/时间一致性」，从「时空/动态角度」切入，主要采用「Motion decomposition / canonical space / deformation」来服务「动态场景与 4D 重建」。
- Method diagram：![2011.13961](method_figures/2011.13961_D-NeRF.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2020_D_NeRF_Neural_Radiance_Fields_for_Dynamic_Scenes_2011.13961.pdf
###### High-Fidelity ｜ 2309.13101
- Paper：Deformable 3D Gaussians for High-Fidelity Monocular Dynamic Scene Reconstruction
- 一句话：High-Fidelity 针对「建模运动/形变/时间一致性」，从「时空/动态角度」切入，主要采用「Motion decomposition / canonical space / deformation」来服务「动态场景与 4D 重建」。
- Method diagram：![2309.13101](method_figures/2309.13101_High-Fidelity.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2023_Deformable_3D_Gaussians_for_High_Fidelity_Monocular_Dynamic_Scene_Reconstruction_2309.13101.pdf
- Code：https://github.com/ingra14m/Deformable-3D-Gaussians（code_link_found_not_audited）

##### 解法族：NeRF/辐射场/体渲染（2）
###### HyperNeRF ｜ 2106.13228
- Paper：HyperNeRF: A Higher-Dimensional Representation for Topologically Varying Neural Radiance Fields
- 一句话：HyperNeRF 针对「建模运动/形变/时间一致性」，从「时空/动态角度」切入，主要采用「NeRF/辐射场/体渲染」来服务「动态场景与 4D 重建」。
- Method diagram：![2106.13228](method_figures/2106.13228_HyperNeRF.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2021_HyperNeRF_A_Higher_Dimensional_Representation_for_Topologically_Varying_Neural_Radiance_Fi_2106.13228.pdf
- Code：https://github.com/google/hypernerf（code_link_found_not_audited）
###### NeRFscopy ｜ 2602.15775
- Paper：NeRFscopy: Neural Radiance Fields for in-vivo Time-Varying Tissues from Endoscopy
- 一句话：NeRFscopy 针对「建模运动/形变/时间一致性」，从「时空/动态角度」切入，主要采用「NeRF/辐射场/体渲染」来服务「动态场景与 4D 重建」。
- Method diagram：![2602.15775](method_figures/2602.15775_NeRFscopy.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_NeRFscopy_Neural_Radiance_Fields_for_in_vivo_Time_Varying_Tissues_from_Endoscopy_2602.15775.pdf

##### 解法族：Pruning / compression / progressive coding（2）
###### Neural 3D Video Synthesis from Multi-view Video ｜ 2103.02597
- Paper：Neural 3D Video Synthesis from Multi-view Video
- 一句话：Neural 3D Video Synthesis from Multi-view Video 针对「建模运动/形变/时间一致性」，从「时空/动态角度」切入，主要采用「Pruning / compression / progressive coding」来服务「动态场景与 4D 重建」。
- Method diagram：![2103.02597](method_figures/2103.02597_Neural_3D_Video_Synthesis_from_Multi-view_Video.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2022_Neural_3D_Video_Synthesis_from_Multi_view_Video_2103.02597.pdf
- Code：https://github.com/facebookresearch/Neural_3D_Video（code_link_found_not_audited）
###### LivingWorld ｜ 2604.01641
- Paper：LivingWorld: Interactive 4D World Generation with Environmental Dynamics
- 一句话：LivingWorld 针对「建模运动/形变/时间一致性」，从「时空/动态角度」切入，主要采用「Pruning / compression / progressive coding」来服务「动态场景与 4D 重建」。
- Method diagram：![2604.01641](method_figures/2604.01641_LivingWorld.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_LivingWorld_Interactive_4D_World_Generation_with_Environmental_Dynamics_2604.01641.pdf

##### 解法族：SLAM / pose graph / online mapping pipeline（25；另有 22 篇见 full/csv）
###### K-Planes ｜ 2301.10241
- Paper：K-Planes: Explicit Radiance Fields in Space, Time, and Appearance
- 一句话：K-Planes 针对「建模运动/形变/时间一致性」，从「时空/动态角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「动态场景与 4D 重建」。
- Method diagram：![2301.10241](method_figures/2301.10241_K-Planes.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2023_K_Planes_Explicit_Radiance_Fields_in_Space_Time_and_Appearance_2301.10241.pdf
- Code：https://github.com/sarafridov/K-Planes（code_link_found_not_audited）
###### ACCURATE ｜ 2603.07533
- Paper：ACCURATE: Arbitrary-shaped Continuum Reconstruction Under Robust Adaptive Two-view Estimation
- 一句话：ACCURATE 针对「建模运动/形变/时间一致性」，从「时空/动态角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「动态场景与 4D 重建」。
- Method diagram：![2603.07533](method_figures/2603.07533_ACCURATE.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_ACCURATE_Arbitrary_shaped_Continuum_Reconstruction_Under_Robust_Adaptive_Two_view_Estimati_2603.07533.pdf
###### From Sparse Sensors to Continuous Fields ｜ 2602.04201
- Paper：From Sparse Sensors to Continuous Fields: STRIDE for Spatiotemporal Reconstruction
- 一句话：From Sparse Sensors to Continuous Fields 针对「建模运动/形变/时间一致性」，从「时空/动态角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「动态场景与 4D 重建」。
- Method diagram：![2602.04201](method_figures/2602.04201_From_Sparse_Sensors_to_Continuous_Fields.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_From_Sparse_Sensors_to_Continuous_Fields_STRIDE_for_Spatiotemporal_Reconstruction_2602.04201.pdf

#### 子问题：接入 SLAM/机器人闭环系统（2）
##### 解法族：SLAM / pose graph / online mapping pipeline（2）
###### GaussTwin ｜ 2603.05108
- Paper：GaussTwin: Unified Simulation and Correction with Gaussian Splatting for Robotic Digital Twins
- 一句话：GaussTwin 针对「接入 SLAM/机器人闭环系统」，从「时空/动态角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「动态场景与 4D 重建」。
- Method diagram：![2603.05108](method_figures/2603.05108_GaussTwin.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_GaussTwin_Unified_Simulation_and_Correction_with_Gaussian_Splatting_for_Robotic_Digital_Tw_2603.05108.pdf
- Code：https://github.com/6cyc6/gausstwin（code_link_found_not_audited）
###### SLAM Adversarial Lab ｜ 2603.17165
- Paper：SLAM Adversarial Lab: An Extensible Framework for Visual SLAM Robustness Evaluation under Adverse Conditions
- 一句话：SLAM Adversarial Lab 针对「接入 SLAM/机器人闭环系统」，从「时空/动态角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「动态场景与 4D 重建」。
- Method diagram：![2603.17165](method_figures/2603.17165_SLAM_Adversarial_Lab.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_SLAM_Adversarial_Lab_An_Extensible_Framework_for_Visual_SLAM_Robustness_Evaluation_under_A_2603.17165.pdf
- Code：https://github.com/sfu-rsl/SLAMAdversarialLab（code_link_found_not_audited）

#### 子问题：提升几何一致性/表面质量（2）
##### 解法族：Motion decomposition / canonical space / deformation（1）
###### Director ｜ 2604.01678
- Paper：Director: Instance-aware Gaussian Splatting for Dynamic Scene Modeling and Understanding
- 一句话：Director 针对「提升几何一致性/表面质量」，从「时空/动态角度」切入，主要采用「Motion decomposition / canonical space / deformation」来服务「动态场景与 4D 重建」。
- Method diagram：![2604.01678](method_figures/2604.01678_Director.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Director_Instance_aware_Gaussian_Splatting_for_Dynamic_Scene_Modeling_and_Understanding_2604.01678.pdf

##### 解法族：SDF/隐式表面/网格/点云（1）
###### MeshMimic ｜ 2602.15733
- Paper：MeshMimic: Geometry-Aware Humanoid Motion Learning through 3D Scene Reconstruction
- 一句话：MeshMimic 针对「提升几何一致性/表面质量」，从「时空/动态角度」切入，主要采用「SDF/隐式表面/网格/点云」来服务「动态场景与 4D 重建」。
- Method diagram：![2602.15733](method_figures/2602.15733_MeshMimic.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_MeshMimic_Geometry_Aware_Humanoid_Motion_Learning_through_3D_Scene_Reconstruction_2602.15733.pdf

#### 子问题：提升可控生成/世界演化预测（16）
##### 解法族：Diffusion/生成先验/视频模型（6；另有 3 篇见 full/csv）
###### DreamPlan ｜ 2603.16860
- Paper：DreamPlan: Efficient Reinforcement Fine-Tuning of Vision-Language Planners via Video World Models
- 一句话：DreamPlan 针对「提升可控生成/世界演化预测」，从「时空/动态角度」切入，主要采用「Diffusion/生成先验/视频模型」来服务「动态场景与 4D 重建」。
- Method diagram：![2603.16860](method_figures/2603.16860_DreamPlan.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_DreamPlan_Efficient_Reinforcement_Fine_Tuning_of_Vision_Language_Planners_via_Video_World_2603.16860.pdf
- Code：https://github.com/physical-superintelligence-lab/DreamPlan/tree/main（code_link_found_not_audited）
###### DreamWorld ｜ 2603.00466
- Paper：DreamWorld: Unified World Modeling in Video Generation
- 一句话：DreamWorld 针对「提升可控生成/世界演化预测」，从「时空/动态角度」切入，主要采用「Diffusion/生成先验/视频模型」来服务「动态场景与 4D 重建」。
- Method diagram：![2603.00466](method_figures/2603.00466_DreamWorld.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_DreamWorld_Unified_World_Modeling_in_Video_Generation_2603.00466.pdf
- Code：https://github.com/ABU121111/DreamWorld（code_link_found_not_audited）
###### DriveVA ｜ 2604.04198
- Paper：DriveVA: Video Action Models are Zero-Shot Drivers
- 一句话：DriveVA 针对「提升可控生成/世界演化预测」，从「时空/动态角度」切入，主要采用「Diffusion/生成先验/视频模型」来服务「动态场景与 4D 重建」。
- Method diagram：![2604.04198](method_figures/2604.04198_DriveVA.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_DriveVA_Video_Action_Models_are_Zero_Shot_Drivers_2604.04198.pdf
- Code：https://github.com/autonomousvision/navsim（code_link_found_not_audited）

##### 解法族：Motion decomposition / canonical space / deformation（4；另有 1 篇见 full/csv）
###### Beyond Dense Futures ｜ 2603.12553
- Paper：Beyond Dense Futures: World Models as Structured Planners for Robotic Manipulation
- 一句话：Beyond Dense Futures 针对「提升可控生成/世界演化预测」，从「时空/动态角度」切入，主要采用「Motion decomposition / canonical space / deformation」来服务「动态场景与 4D 重建」。
- Method diagram：![2603.12553](method_figures/2603.12553_Beyond_Dense_Futures.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Beyond_Dense_Futures_World_Models_as_Structured_Planners_for_Robotic_Manipulation_2603.12553.pdf
- Code：https://github.com/wm-planner/structvla（code_link_found_not_audited）
###### MAD ｜ 2601.09452
- Paper：MAD: Motion Appearance Decoupling for efficient Driving World Models
- 一句话：MAD 针对「提升可控生成/世界演化预测」，从「时空/动态角度」切入，主要采用「Motion decomposition / canonical space / deformation」来服务「动态场景与 4D 重建」。
- Method diagram：![2601.09452](method_figures/2601.09452_MAD.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_MAD_Motion_Appearance_Decoupling_for_efficient_Driving_World_Models_2601.09452.pdf
- Code：https://github.com/vita-epfl/MAD-World-Model-Code/（code_link_found_not_audited）
###### ResWorld ｜ 2602.10884
- Paper：ResWorld: Temporal Residual World Model for End-to-End Autonomous Driving
- 一句话：ResWorld 针对「提升可控生成/世界演化预测」，从「时空/动态角度」切入，主要采用「Motion decomposition / canonical space / deformation」来服务「动态场景与 4D 重建」。
- Method diagram：![2602.10884](method_figures/2602.10884_ResWorld.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_ResWorld_Temporal_Residual_World_Model_for_End_to_End_Autonomous_Driving_2602.10884.pdf
- Code：https://github.com/mengtan00/ResWorld.git（code_link_found_not_audited）

##### 解法族：Pruning / compression / progressive coding（1）
###### Beyond Pixel Histories ｜ 2603.03482
- Paper：Beyond Pixel Histories: World Models with Persistent 3D State
- 一句话：Beyond Pixel Histories 针对「提升可控生成/世界演化预测」，从「时空/动态角度」切入，主要采用「Pruning / compression / progressive coding」来服务「动态场景与 4D 重建」。
- Method diagram：![2603.03482](method_figures/2603.03482_Beyond_Pixel_Histories.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Beyond_Pixel_Histories_World_Models_with_Persistent_3D_State_2603.03482.pdf
- Code：https://github.com/francelico/PERSIST（code_link_found_not_audited）

##### 解法族：SLAM / pose graph / online mapping pipeline（5；另有 2 篇见 full/csv）
###### AutoWorld ｜ 2603.28963
- Paper：AutoWorld: Scaling Multi-Agent Traffic Simulation with Self-Supervised World Models
- 一句话：AutoWorld 针对「提升可控生成/世界演化预测」，从「时空/动态角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「动态场景与 4D 重建」。
- Method diagram：![2603.28963](method_figures/2603.28963_AutoWorld.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_AutoWorld_Scaling_Multi_Agent_Traffic_Simulation_with_Self_Supervised_World_Models_2603.28963.pdf
###### CUA-Suite ｜ 2603.24440
- Paper：CUA-Suite: Massive Human-annotated Video Demonstrations for Computer-Use Agents
- 一句话：CUA-Suite 针对「提升可控生成/世界演化预测」，从「时空/动态角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「动态场景与 4D 重建」。
- Method diagram：![2603.24440](method_figures/2603.24440_CUA-Suite.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_CUA_Suite_Massive_Human_annotated_Video_Demonstrations_for_Computer_Use_Agents_2603.24440.pdf
- Code：https://github.com/ServiceNow/GroundCUA/tree/main/VideoCUA（code_link_found_not_audited）
###### From Gradients to Riccati Geometry ｜ 2603.13423
- Paper：From Gradients to Riccati Geometry: Kalman World Models for Single-Pass Learning
- 一句话：From Gradients to Riccati Geometry 针对「提升可控生成/世界演化预测」，从「时空/动态角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「动态场景与 4D 重建」。
- Method diagram：![2603.13423](method_figures/2603.13423_From_Gradients_to_Riccati_Geometry.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_From_Gradients_to_Riccati_Geometry_Kalman_World_Models_for_Single_Pass_Learning_2603.13423.pdf

#### 子问题：解决稀疏视角几何不稳定（4）
##### 解法族：Gaussian Splatting 表示与正则化（1）
###### 4C4D ｜ 2604.04063
- Paper：4C4D: 4 Camera 4D Gaussian Splatting
- 一句话：4C4D 针对「解决稀疏视角几何不稳定」，从「时空/动态角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「动态场景与 4D 重建」。
- Method diagram：![2604.04063](method_figures/2604.04063_4C4D.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_4C4D_4_Camera_4D_Gaussian_Splatting_2604.04063.pdf
- Code：https://github.com/yangzf-1023/4C4D（code_link_found_not_audited）

##### 解法族：NeRF/辐射场/体渲染（1）
###### GAT-NeRF ｜ 2601.14875
- Paper：GAT-NeRF: Geometry-Aware-Transformer Enhanced Neural Radiance Fields for High-Fidelity 4D Facial Avatars
- 一句话：GAT-NeRF 针对「解决稀疏视角几何不稳定」，从「时空/动态角度」切入，主要采用「NeRF/辐射场/体渲染」来服务「动态场景与 4D 重建」。
- Method diagram：![2601.14875](method_figures/2601.14875_GAT-NeRF.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_GAT_NeRF_Geometry_Aware_Transformer_Enhanced_Neural_Radiance_Fields_for_High_Fidelity_4D_F_2601.14875.pdf

##### 解法族：SLAM / pose graph / online mapping pipeline（2）
###### Point2Pose ｜ 2604.10415
- Paper：Point2Pose: Occlusion-Recovering 6D Pose Tracking and 3D Reconstruction for Multiple Unknown Objects Via 2D Point Trackers
- 一句话：Point2Pose 针对「解决稀疏视角几何不稳定」，从「时空/动态角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「动态场景与 4D 重建」。
- Method diagram：![2604.10415](method_figures/2604.10415_Point2Pose.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Point2Pose_Occlusion_Recovering_6D_Pose_Tracking_and_3D_Reconstruction_for_Multiple_Unknow_2604.10415.pdf
- Code：https://github.com/borglab/gtsam\（code_link_found_not_audited）
###### SF3D-RGB ｜ 2602.21699
- Paper：SF3D-RGB: Scene Flow Estimation from Monocular Camera and Sparse LiDAR
- 一句话：SF3D-RGB 针对「解决稀疏视角几何不稳定」，从「时空/动态角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「动态场景与 4D 重建」。
- Method diagram：![2602.21699](method_figures/2602.21699_SF3D-RGB.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_SF3D_RGB_Scene_Flow_Estimation_from_Monocular_Camera_and_Sparse_LiDAR_2602.21699.pdf
- Code：https://github.com/dfki-av/DeepLiDARFlow（code_link_found_not_audited）

#### 子问题：降低显存/存储/模型体积（1）
##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### Geometry-Aware ｜ 2602.07854
- Paper：Geometry-Aware Rotary Position Embedding for Consistent Video World Model
- 一句话：Geometry-Aware 针对「降低显存/存储/模型体积」，从「时空/动态角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「动态场景与 4D 重建」。
- Method diagram：![2602.07854](method_figures/2602.07854_Geometry-Aware.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Geometry_Aware_Rotary_Position_Embedding_for_Consistent_Video_World_Model_2602.07854.pdf

### 切入点：生成/世界模型角度（3）
#### 子问题：提升可控生成/世界演化预测（3）
##### 解法族：Diffusion/生成先验/视频模型（1）
###### RL ｜ 2603.21546
- Paper：What Do World Models Learn in RL? Probing Latent Representations in Learned Environment Simulators
- 一句话：RL 针对「提升可控生成/世界演化预测」，从「生成/世界模型角度」切入，主要采用「Diffusion/生成先验/视频模型」来服务「动态场景与 4D 重建」。
- Method diagram：![2603.21546](method_figures/2603.21546_RL.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_What_Do_World_Models_Learn_in_RL_Probing_Latent_Representations_in_Learned_Environment_Sim_2603.21546.pdf

##### 解法族：SLAM / pose graph / online mapping pipeline（2）
###### PIRATR ｜ 2602.05557
- Paper：PIRATR: Parametric Object Inference for Robotic Applications with Transformers in 3D Point Clouds
- 一句话：PIRATR 针对「提升可控生成/世界演化预测」，从「生成/世界模型角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「动态场景与 4D 重建」。
- Method diagram：![2602.05557](method_figures/2602.05557_PIRATR.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_PIRATR_Parametric_Object_Inference_for_Robotic_Applications_with_Transformers_in_3D_Point_2602.05557.pdf
- Code：https://github.com/swingaxe/piratr（code_link_found_not_audited）
###### Picasso ｜ 2602.08058
- Paper：Picasso: Holistic Scene Reconstruction with Physics-Constrained Sampling
- 一句话：Picasso 针对「提升可控生成/世界演化预测」，从「生成/世界模型角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「动态场景与 4D 重建」。
- Method diagram：![2602.08058](method_figures/2602.08058_Picasso.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Picasso_Holistic_Scene_Reconstruction_with_Physics_Constrained_Sampling_2602.08058.pdf
- Code：https://github.com/shanice-l/gdrnpp_bop2022（code_link_found_not_audited）

### 切入点：系统/在线部署角度（3）
#### 子问题：建模运动/形变/时间一致性（2）
##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### NRGS-SLAM ｜ 2602.17182
- Paper：NRGS-SLAM: Monocular Non-Rigid SLAM for Endoscopy via Deformation-Aware 3D Gaussian Splatting
- 一句话：NRGS-SLAM 针对「建模运动/形变/时间一致性」，从「系统/在线部署角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「动态场景与 4D 重建」。
- Method diagram：![2602.17182](method_figures/2602.17182_NRGS-SLAM.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_NRGS_SLAM_Monocular_Non_Rigid_SLAM_for_Endoscopy_via_Deformation_Aware_3D_Gaussian_Splatti_2602.17182.pdf

##### 解法族：Sensor/domain-specific pipeline（1）
###### from-Motion ｜ 2602.14311
- Paper：Exploiting Structure-from-Motion for Robust Vision-Based Map Matching for Aircraft Surface Movement
- 一句话：from-Motion 针对「建模运动/形变/时间一致性」，从「系统/在线部署角度」切入，主要采用「Sensor/domain-specific pipeline」来服务「动态场景与 4D 重建」。
- Method diagram：![2602.14311](method_figures/2602.14311_from-Motion.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Exploiting_Structure_from_Motion_for_Robust_Vision_Based_Map_Matching_for_Aircraft_Surface_2602.14311.pdf

#### 子问题：接入 SLAM/机器人闭环系统（1）
##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### OGScene3D ｜ 2603.16301
- Paper：OGScene3D: Incremental Open-Vocabulary 3D Gaussian Scene Graph Mapping for Scene Understanding
- 一句话：OGScene3D 针对「接入 SLAM/机器人闭环系统」，从「系统/在线部署角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「动态场景与 4D 重建」。
- Method diagram：![2603.16301](method_figures/2603.16301_OGScene3D.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_OGScene3D_Incremental_Open_Vocabulary_3D_Gaussian_Scene_Graph_Mapping_for_Scene_Understand_2603.16301.pdf
- Code：https://github.com/IRMVLab/OGScene3D（code_link_found_not_audited）

### 切入点：表示/几何角度（43）
#### 子问题：建模运动/形变/时间一致性（15）
##### 解法族：Gaussian Splatting 表示与正则化（6；另有 3 篇见 full/csv）
###### Object-Centered ｜ 2604.19216
- Paper：An Object-Centered Data Acquisition Method for 3D Gaussian Splatting using Mobile Phones
- 一句话：Object-Centered 针对「建模运动/形变/时间一致性」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「动态场景与 4D 重建」。
- Method diagram：![2604.19216](method_figures/2604.19216_Object-Centered.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_An_Object_Centered_Data_Acquisition_Method_for_3D_Gaussian_Splatting_using_Mobile_Phones_2604.19216.pdf
###### GaussExplorer ｜ 2601.13132
- Paper：GaussExplorer: 3D Gaussian Splatting for Embodied Exploration and Reasoning
- 一句话：GaussExplorer 针对「建模运动/形变/时间一致性」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「动态场景与 4D 重建」。
- Method diagram：![2601.13132](method_figures/2601.13132_GaussExplorer.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_GaussExplorer_3D_Gaussian_Splatting_for_Embodied_Exploration_and_Reasoning_2601.13132.pdf
###### Incoherent Deformation, Not Capacity ｜ 2604.16747
- Paper：Incoherent Deformation, Not Capacity: Diagnosing and Mitigating Overfitting in Dynamic Gaussian Splatting
- 一句话：Incoherent Deformation, Not Capacity 针对「建模运动/形变/时间一致性」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「动态场景与 4D 重建」。
- Method diagram：![2604.16747](method_figures/2604.16747_Incoherent_Deformation_Not_Capacity.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Incoherent_Deformation_Not_Capacity_Diagnosing_and_Mitigating_Overfitting_in_Dynamic_Gauss_2604.16747.pdf

##### 解法族：Motion decomposition / canonical space / deformation（2）
###### DynamicVGGT ｜ 2603.08254
- Paper：DynamicVGGT: Learning Dynamic Point Maps for 4D Scene Reconstruction in Autonomous Driving
- 一句话：DynamicVGGT 针对「建模运动/形变/时间一致性」，从「表示/几何角度」切入，主要采用「Motion decomposition / canonical space / deformation」来服务「动态场景与 4D 重建」。
- Method diagram：![2603.08254](method_figures/2603.08254_DynamicVGGT.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_DynamicVGGT_Learning_Dynamic_Point_Maps_for_4D_Scene_Reconstruction_in_Autonomous_Driving_2603.08254.pdf
###### E2EGS ｜ 2603.14684
- Paper：E2EGS: Event-to-Edge Gaussian Splatting for Pose-Free 3D Reconstruction
- 一句话：E2EGS 针对「建模运动/形变/时间一致性」，从「表示/几何角度」切入，主要采用「Motion decomposition / canonical space / deformation」来服务「动态场景与 4D 重建」。
- Method diagram：![2603.14684](method_figures/2603.14684_E2EGS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_E2EGS_Event_to_Edge_Gaussian_Splatting_for_Pose_Free_3D_Reconstruction_2603.14684.pdf
- Code：https://github.com/MichaelGrupp/evo（code_link_found_not_audited）

##### 解法族：NeRF/辐射场/体渲染（1）
###### EmoTaG ｜ 2603.21332
- Paper：EmoTaG: Emotion-Aware Talking Head Synthesis on Gaussian Splatting with Few-Shot Personalization
- 一句话：EmoTaG 针对「建模运动/形变/时间一致性」，从「表示/几何角度」切入，主要采用「NeRF/辐射场/体渲染」来服务「动态场景与 4D 重建」。
- Method diagram：![2603.21332](method_figures/2603.21332_EmoTaG.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_EmoTaG_Emotion_Aware_Talking_Head_Synthesis_on_Gaussian_Splatting_with_Few_Shot_Personaliz_2603.21332.pdf
- Code：https://github.com/jamesdemon923/EmoTaG（code_link_found_not_audited）

##### 解法族：SLAM / pose graph / online mapping pipeline（6；另有 3 篇见 full/csv）
###### 4D Synchronized Fields ｜ 2603.14301
- Paper：4D Synchronized Fields: Motion-Language Gaussian Splatting for Temporal Scene Understanding
- 一句话：4D Synchronized Fields 针对「建模运动/形变/时间一致性」，从「表示/几何角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「动态场景与 4D 重建」。
- Method diagram：![2603.14301](method_figures/2603.14301_4D_Synchronized_Fields.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_4D_Synchronized_Fields_Motion_Language_Gaussian_Splatting_for_Temporal_Scene_Understanding_2603.14301.pdf
###### Drive-Through ｜ 2603.26638
- Paper：Drive-Through 3D Vehicle Exterior Reconstruction via Dynamic-Scene SfM and Distortion-Aware Gaussian Splatting
- 一句话：Drive-Through 针对「建模运动/形变/时间一致性」，从「表示/几何角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「动态场景与 4D 重建」。
- Method diagram：![2603.26638](method_figures/2603.26638_Drive-Through.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Drive_Through_3D_Vehicle_Exterior_Reconstruction_via_Dynamic_Scene_SfM_and_Distortion_Awar_2603.26638.pdf
###### GGD-SLAM ｜ 2604.12837
- Paper：GGD-SLAM: Monocular 3DGS SLAM Powered by Generalizable Motion Model for Dynamic Environments
- 一句话：GGD-SLAM 针对「建模运动/形变/时间一致性」，从「表示/几何角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「动态场景与 4D 重建」。
- Method diagram：![2604.12837](method_figures/2604.12837_GGD-SLAM.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_GGD_SLAM_Monocular_3DGS_SLAM_Powered_by_Generalizable_Motion_Model_for_Dynamic_Environment_2604.12837.pdf

#### 子问题：接入 SLAM/机器人闭环系统（3）
##### 解法族：SLAM / pose graph / online mapping pipeline（3）
###### RadarSplat-RIO ｜ 2604.13492
- Paper：RadarSplat-RIO: Indoor Radar-Inertial Odometry with Gaussian Splatting-Based Radar Bundle Adjustment
- 一句话：RadarSplat-RIO 针对「接入 SLAM/机器人闭环系统」，从「表示/几何角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「动态场景与 4D 重建」。
- Method diagram：![2604.13492](method_figures/2604.13492_RadarSplat-RIO.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_RadarSplat_RIO_Indoor_Radar_Inertial_Odometry_with_Gaussian_Splatting_Based_Radar_Bundle_A_2604.13492.pdf
###### SGAD-SLAM ｜ 2603.21055
- Paper：SGAD-SLAM: Splatting Gaussians at Adjusted Depth for Better Radiance Fields in RGBD SLAM
- 一句话：SGAD-SLAM 针对「接入 SLAM/机器人闭环系统」，从「表示/几何角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「动态场景与 4D 重建」。
- Method diagram：![2603.21055](method_figures/2603.21055_SGAD-SLAM.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_SGAD_SLAM_Splatting_Gaussians_at_Adjusted_Depth_for_Better_Radiance_Fields_in_RGBD_SLAM_2603.21055.pdf
- Code：https://github.com/MachinePerceptionLab/SGAD-SLAM（code_link_found_not_audited）
###### 本文方法 ｜ 2602.07493
- Paper：Thermal odometry and dense mapping using learned odometry and Gaussian splatting
- 一句话：本文方法 针对「接入 SLAM/机器人闭环系统」，从「表示/几何角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「动态场景与 4D 重建」。
- Method diagram：![2602.07493](method_figures/2602.07493_paper.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Thermal_odometry_and_dense_mapping_using_learned_odometry_and_Gaussian_splatting_2602.07493.pdf

#### 子问题：提升几何一致性/表面质量（9）
##### 解法族：Gaussian Splatting 表示与正则化（4；另有 1 篇见 full/csv）
###### GTLR-GS ｜ 2603.23192
- Paper：GTLR-GS: Geometry-Texture Aware LiDAR-Regularized 3D Gaussian Splatting for Realistic Scene Reconstruction
- 一句话：GTLR-GS 针对「提升几何一致性/表面质量」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「动态场景与 4D 重建」。
- Method diagram：![2603.23192](method_figures/2603.23192_GTLR-GS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_GTLR_GS_Geometry_Texture_Aware_LiDAR_Regularized_3D_Gaussian_Splatting_for_Realistic_Scene_2603.23192.pdf
###### HDR ｜ 2603.28020
- Paper：Physically Inspired Gaussian Splatting for HDR Novel View Synthesis
- 一句话：HDR 针对「提升几何一致性/表面质量」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「动态场景与 4D 重建」。
- Method diagram：![2603.28020](method_figures/2603.28020_HDR.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Physically_Inspired_Gaussian_Splatting_for_HDR_Novel_View_Synthesis_2603.28020.pdf
- Code：https://github.com/ZeldaM1/PhysHDR-GS（code_link_found_not_audited）
###### ProDiG ｜ 2604.02003
- Paper：ProDiG: Progressive Diffusion-Guided Gaussian Splatting for Aerial to Ground Reconstruction
- 一句话：ProDiG 针对「提升几何一致性/表面质量」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「动态场景与 4D 重建」。
- Method diagram：![2604.02003](method_figures/2604.02003_ProDiG.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_ProDiG_Progressive_Diffusion_Guided_Gaussian_Splatting_for_Aerial_to_Ground_Reconstruction_2604.02003.pdf
- Code：https://github.com/sirsh07/ProDiG（code_link_found_not_audited）

##### 解法族：Motion decomposition / canonical space / deformation（1）
###### Thinking Like Van Gogh ｜ 2601.10075
- Paper：Thinking Like Van Gogh: Structure-Aware Style Transfer via Flow-Guided 3D Gaussian Splatting
- 一句话：Thinking Like Van Gogh 针对「提升几何一致性/表面质量」，从「表示/几何角度」切入，主要采用「Motion decomposition / canonical space / deformation」来服务「动态场景与 4D 重建」。
- Method diagram：![2601.10075](method_figures/2601.10075_Thinking_Like_Van_Gogh.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Thinking_Like_Van_Gogh_Structure_Aware_Style_Transfer_via_Flow_Guided_3D_Gaussian_Splattin_2601.10075.pdf

##### 解法族：NeRF/辐射场/体渲染（3）
###### Nerfies ｜ 2011.12948
- Paper：Nerfies: Deformable Neural Radiance Fields
- 一句话：Nerfies 针对「提升几何一致性/表面质量」，从「表示/几何角度」切入，主要采用「NeRF/辐射场/体渲染」来服务「动态场景与 4D 重建」。
- Method diagram：![2011.12948](method_figures/2011.12948_Nerfies.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2021_Nerfies_Deformable_Neural_Radiance_Fields_2011.12948.pdf
- Code：https://github.com/google/nerfies（code_link_found_not_audited）
###### PCM-NeRF ｜ 2604.17831
- Paper：PCM-NeRF: Probabilistic Camera Modeling for Neural Radiance Fields under Pose Uncertainty
- 一句话：PCM-NeRF 针对「提升几何一致性/表面质量」，从「表示/几何角度」切入，主要采用「NeRF/辐射场/体渲染」来服务「动态场景与 4D 重建」。
- Method diagram：![2604.17831](method_figures/2604.17831_PCM-NeRF.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_PCM_NeRF_Probabilistic_Camera_Modeling_for_Neural_Radiance_Fields_under_Pose_Uncertainty_2604.17831.pdf
- Code：https://github.com/shravan-18/PCM-NeRF（code_link_found_not_audited）
###### PhysConvex ｜ 2602.18886
- Paper：PhysConvex: Physics-Informed 3D Dynamic Convex Radiance Fields for Reconstruction and Simulation
- 一句话：PhysConvex 针对「提升几何一致性/表面质量」，从「表示/几何角度」切入，主要采用「NeRF/辐射场/体渲染」来服务「动态场景与 4D 重建」。
- Method diagram：![2602.18886](method_figures/2602.18886_PhysConvex.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_PhysConvex_Physics_Informed_3D_Dynamic_Convex_Radiance_Fields_for_Reconstruction_and_Simul_2602.18886.pdf

##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### EndoVGGT ｜ 2603.24577
- Paper：EndoVGGT: GNN-Enhanced Depth Estimation for Surgical 3D Reconstruction
- 一句话：EndoVGGT 针对「提升几何一致性/表面质量」，从「表示/几何角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「动态场景与 4D 重建」。
- Method diagram：![2603.24577](method_figures/2603.24577_EndoVGGT.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_EndoVGGT_GNN_Enhanced_Depth_Estimation_for_Surgical_3D_Reconstruction_2603.24577.pdf

#### 子问题：提升可控生成/世界演化预测（2）
##### 解法族：Gaussian Splatting 表示与正则化（2）
###### AvatarPointillist ｜ 2604.04787
- Paper：AvatarPointillist: AutoRegressive 4D Gaussian Avatarization
- 一句话：AvatarPointillist 针对「提升可控生成/世界演化预测」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「动态场景与 4D 重建」。
- Method diagram：![2604.04787](method_figures/2604.04787_AvatarPointillist.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_AvatarPointillist_AutoRegressive_4D_Gaussian_Avatarization_2604.04787.pdf
- Code：https://github.com/KumapowerLIU/AvatarPointillist（code_link_found_not_audited）
###### 本文方法 ｜ 2603.23637
- Paper：Stochastic Ray Tracing for the Reconstruction of 3D Gaussian Splatting
- 一句话：本文方法 针对「提升可控生成/世界演化预测」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「动态场景与 4D 重建」。
- Method diagram：![2603.23637](method_figures/2603.23637_paper.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Stochastic_Ray_Tracing_for_the_Reconstruction_of_3D_Gaussian_Splatting_2603.23637.pdf

#### 子问题：提升泛化/跨场景/开放世界能力（1）
##### 解法族：Gaussian Splatting 表示与正则化（1）
###### BLaDA ｜ 2604.08410
- Paper：BLaDA: Bridging Language to Functional Dexterous Actions within 3DGS Fields
- 一句话：BLaDA 针对「提升泛化/跨场景/开放世界能力」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「动态场景与 4D 重建」。
- Method diagram：![2604.08410](method_figures/2604.08410_BLaDA.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_BLaDA_Bridging_Language_to_Functional_Dexterous_Actions_within_3DGS_Fields_2604.08410.pdf
- Code：https://github.com/PopeyePxx/BLaDA（code_link_found_not_audited）

#### 子问题：解决稀疏视角几何不稳定（9）
##### 解法族：Gaussian Splatting 表示与正则化（3）
###### BALTIC ｜ 2604.19133
- Paper：BALTIC: A Benchmark and Cross-Domain Strategy for 3D Reconstruction Across Air and Underwater Domains Under Varying Illumination
- 一句话：BALTIC 针对「解决稀疏视角几何不稳定」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「动态场景与 4D 重建」。
- Method diagram：![2604.19133](method_figures/2604.19133_BALTIC.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_BALTIC_A_Benchmark_and_Cross_Domain_Strategy_for_3D_Reconstruction_Across_Air_and_Underwat_2604.19133.pdf
###### Matryoshka Gaussian Splatting ｜ 2603.19234
- Paper：Matryoshka Gaussian Splatting
- 一句话：Matryoshka Gaussian Splatting 针对「解决稀疏视角几何不稳定」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「动态场景与 4D 重建」。
- Method diagram：![2603.19234](method_figures/2603.19234_Matryoshka_Gaussian_Splatting.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Matryoshka_Gaussian_Splatting_2603.19234.pdf
- Code：https://github.com/ZhilinGuo/matryoshka-gaussian-splatting（code_link_found_not_audited）
###### Multi-Human ｜ 2604.02996
- Paper：Rendering Multi-Human and Multi-Object with 3D Gaussian Splatting
- 一句话：Multi-Human 针对「解决稀疏视角几何不稳定」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「动态场景与 4D 重建」。
- Method diagram：![2604.02996](method_figures/2604.02996_Multi-Human.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Rendering_Multi_Human_and_Multi_Object_with_3D_Gaussian_Splatting_2604.02996.pdf

##### 解法族：Motion decomposition / canonical space / deformation（1）
###### 本文方法 ｜ 2602.17473
- Paper：4D Monocular Surgical Reconstruction under Arbitrary Camera Motions
- 一句话：本文方法 针对「解决稀疏视角几何不稳定」，从「表示/几何角度」切入，主要采用「Motion decomposition / canonical space / deformation」来服务「动态场景与 4D 重建」。
- Method diagram：![2602.17473](method_figures/2602.17473_paper.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_4D_Monocular_Surgical_Reconstruction_under_Arbitrary_Camera_Motions_2602.17473.pdf
- Code：https://github.com/IRMVLab/Local-EndoGS（code_link_found_not_audited）

##### 解法族：NeRF/辐射场/体渲染（2）
###### NeRF ｜ 2003.08934
- Paper：NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis
- 一句话：NeRF 针对「解决稀疏视角几何不稳定」，从「表示/几何角度」切入，主要采用「NeRF/辐射场/体渲染」来服务「动态场景与 4D 重建」。
- Method diagram：![2003.08934](method_figures/2003.08934_NeRF.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2020_NeRF_Representing_Scenes_as_Neural_Radiance_Fields_for_View_Synthesis_2003.08934.pdf
- Code：https://github.com/facebookresearch/neuralvolumes（code_link_found_not_audited）
###### MU-GeNeRF ｜ 2604.17965
- Paper：MU-GeNeRF: Multi-view Uncertainty-guided Generalizable Neural Radiance Fields for Distractor-aware Scene
- 一句话：MU-GeNeRF 针对「解决稀疏视角几何不稳定」，从「表示/几何角度」切入，主要采用「NeRF/辐射场/体渲染」来服务「动态场景与 4D 重建」。
- Method diagram：![2604.17965](method_figures/2604.17965_MU-GeNeRF.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_MU_GeNeRF_Multi_view_Uncertainty_guided_Generalizable_Neural_Radiance_Fields_for_Distracto_2604.17965.pdf
- Code：https://github.com/Yanyilucas/MU-GeNeRF（code_link_found_not_audited）

##### 解法族：SLAM / pose graph / online mapping pipeline（3）
###### PoInit-of-View ｜ 2604.16540
- Paper：PoInit-of-View: Poisoning Initialization of Views Transfers Across Multiple 3D Reconstruction Systems
- 一句话：PoInit-of-View 针对「解决稀疏视角几何不稳定」，从「表示/几何角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「动态场景与 4D 重建」。
- Method diagram：![2604.16540](method_figures/2604.16540_PoInit-of-View.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_PoInit_of_View_Poisoning_Initialization_of_Views_Transfers_Across_Multiple_3D_Reconstructi_2604.16540.pdf
- Code：https://github.com/nerfbaselines/nerfbaselines（code_link_found_not_audited）
###### Block-Structured ｜ 2602.09415
- Paper：Stability and Concentration in Nonlinear Inverse Problems with Block-Structured Parameters: Lipschitz Geometry, Identifiability, and an Application to Gaussian Splatting
- 一句话：Block-Structured 针对「解决稀疏视角几何不稳定」，从「表示/几何角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「动态场景与 4D 重建」。
- Method diagram：![2602.09415](method_figures/2602.09415_Block-Structured.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Stability_and_Concentration_in_Nonlinear_Inverse_Problems_with_Block_Structured_Parameters_2602.09415.pdf
###### VBGS-SLAM ｜ 2604.02696
- Paper：VBGS-SLAM: Variational Bayesian Gaussian Splatting Simultaneous Localization and Mapping
- 一句话：VBGS-SLAM 针对「解决稀疏视角几何不稳定」，从「表示/几何角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「动态场景与 4D 重建」。
- Method diagram：![2604.02696](method_figures/2604.02696_VBGS-SLAM.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_VBGS_SLAM_Variational_Bayesian_Gaussian_Splatting_Simultaneous_Localization_and_Mapping_2604.02696.pdf

#### 子问题：降低显存/存储/模型体积（4）
##### 解法族：Gaussian Splatting 表示与正则化（2）
###### GSTurb ｜ 2602.22800
- Paper：GSTurb: Gaussian Splatting for Atmospheric Turbulence Mitigation
- 一句话：GSTurb 针对「降低显存/存储/模型体积」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「动态场景与 4D 重建」。
- Method diagram：![2602.22800](method_figures/2602.22800_GSTurb.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_GSTurb_Gaussian_Splatting_for_Atmospheric_Turbulence_Mitigation_2602.22800.pdf
- Code：https://github.com/DuhlLiamz/3DGS_turbulence/tree/main（code_link_found_not_audited）
###### Semantic-Guided ｜ 2602.15516
- Paper：Semantic-Guided 3D Gaussian Splatting for Transient Object Removal
- 一句话：Semantic-Guided 针对「降低显存/存储/模型体积」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「动态场景与 4D 重建」。
- Method diagram：![2602.15516](method_figures/2602.15516_Semantic-Guided.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Semantic_Guided_3D_Gaussian_Splatting_for_Transient_Object_Removal_2602.15516.pdf

##### 解法族：NeRF/辐射场/体渲染（2）
###### From Implicit Ambiguity to Explicit Solidity ｜ 2601.21421
- Paper：From Implicit Ambiguity to Explicit Solidity: Diagnosing Interior Geometric Degradation in Neural Radiance Fields for Dense 3D Scene Understanding
- 一句话：From Implicit Ambiguity to Explicit Solidity 针对「降低显存/存储/模型体积」，从「表示/几何角度」切入，主要采用「NeRF/辐射场/体渲染」来服务「动态场景与 4D 重建」。
- Method diagram：![2601.21421](method_figures/2601.21421_From_Implicit_Ambiguity_to_Explicit_Solidity.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_From_Implicit_Ambiguity_to_Explicit_Solidity_Diagnosing_Interior_Geometric_Degradation_in_2601.21421.pdf
- Code：https://github.com/ZJiangsan/3D_DenseFruitCounting（code_link_found_not_audited）
###### 本文方法 ｜ 2603.09277
- Paper：Speeding Up the Learning of 3D Gaussians with Much Shorter Gaussian Lists
- 一句话：本文方法 针对「降低显存/存储/模型体积」，从「表示/几何角度」切入，主要采用「NeRF/辐射场/体渲染」来服务「动态场景与 4D 重建」。
- Method diagram：![2603.09277](method_figures/2603.09277_paper.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Speeding_Up_the_Learning_of_3D_Gaussians_with_Much_Shorter_Gaussian_Lists_2603.09277.pdf
- Code：https://github.com/MachinePerceptionLab/ShorterSplatting（code_link_found_not_audited）

### 切入点：计算角度（2）
#### 子问题：建模运动/形变/时间一致性（1）
##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### M^3 ｜ 2603.16844
- Paper：M^3: Dense Matching Meets Multi-View Foundation Models for Monocular Gaussian Splatting SLAM
- 一句话：M^3 针对「建模运动/形变/时间一致性」，从「计算角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「动态场景与 4D 重建」。
- Method diagram：![2603.16844](method_figures/2603.16844_M_3.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_M_3_Dense_Matching_Meets_Multi_View_Foundation_Models_for_Monocular_Gaussian_Splatting_SLA_2603.16844.pdf
- Code：https://github.com/InternRobotics/M3（code_link_found_not_audited）

#### 子问题：接入 SLAM/机器人闭环系统（1）
##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### SceneVGGT ｜ 2602.15899
- Paper：SceneVGGT: VGGT-based online 3D semantic SLAM for indoor scene understanding and navigation
- 一句话：SceneVGGT 针对「接入 SLAM/机器人闭环系统」，从「计算角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「动态场景与 4D 重建」。
- Method diagram：![2602.15899](method_figures/2602.15899_SceneVGGT.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_SceneVGGT_VGGT_based_online_3D_semantic_SLAM_for_indoor_scene_understanding_and_navigation_2602.15899.pdf
- Code：https://github.com/HBVC-AI/SceneVGGT/（code_link_found_not_audited）

### 切入点：训练/监督角度（23）
#### 子问题：建模运动/形变/时间一致性（12）
##### 解法族：Diffusion/生成先验/视频模型（1）
###### Belief-State ｜ 2601.03517
- Paper：Semantic Belief-State World Model for 3D Human Motion Prediction
- 一句话：Belief-State 针对「建模运动/形变/时间一致性」，从「训练/监督角度」切入，主要采用「Diffusion/生成先验/视频模型」来服务「动态场景与 4D 重建」。
- Method diagram：![2601.03517](method_figures/2601.03517_Belief-State.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Semantic_Belief_State_World_Model_for_3D_Human_Motion_Prediction_2601.03517.pdf
- Code：https://github.com/DavidBoja/SMPL-Anthropometry（code_link_found_not_audited）

##### 解法族：Gaussian Splatting 表示与正则化（2）
###### TokenGS ｜ 2604.15239
- Paper：TokenGS: Decoupling 3D Gaussian Prediction from Pixels with Learnable Tokens
- 一句话：TokenGS 针对「建模运动/形变/时间一致性」，从「训练/监督角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「动态场景与 4D 重建」。
- Method diagram：![2604.15239](method_figures/2604.15239_TokenGS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_TokenGS_Decoupling_3D_Gaussian_Prediction_from_Pixels_with_Learnable_Tokens_2604.15239.pdf
###### UFO-4D ｜ 2602.24290
- Paper：UFO-4D: Unposed Feedforward 4D Reconstruction from Two Images
- 一句话：UFO-4D 针对「建模运动/形变/时间一致性」，从「训练/监督角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「动态场景与 4D 重建」。
- Method diagram：![2602.24290](method_figures/2602.24290_UFO-4D.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_UFO_4D_Unposed_Feedforward_4D_Reconstruction_from_Two_Images_2602.24290.pdf
- Code：https://github.com/ufo-4d/ufo-4d（code_link_found_not_audited）

##### 解法族：Motion decomposition / canonical space / deformation（1）
###### MotionCrafter ｜ 2602.08961
- Paper：MotionCrafter: Dense Geometry and Motion Reconstruction with a 4D VAE
- 一句话：MotionCrafter 针对「建模运动/形变/时间一致性」，从「训练/监督角度」切入，主要采用「Motion decomposition / canonical space / deformation」来服务「动态场景与 4D 重建」。
- Method diagram：![2602.08961](method_figures/2602.08961_MotionCrafter.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_MotionCrafter_Dense_Geometry_and_Motion_Reconstruction_with_a_4D_VAE_2602.08961.pdf
- Code：https://github.com/TencentARC/MotionCrafter（code_link_found_not_audited）

##### 解法族：NeRF/辐射场/体渲染（2）
###### Event-Aided ｜ 2602.21101
- Paper：Event-Aided Sharp Radiance Field Reconstruction for Fast-Flying Drones
- 一句话：Event-Aided 针对「建模运动/形变/时间一致性」，从「训练/监督角度」切入，主要采用「NeRF/辐射场/体渲染」来服务「动态场景与 4D 重建」。
- Method diagram：![2602.21101](method_figures/2602.21101_Event-Aided.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Event_Aided_Sharp_Radiance_Field_Reconstruction_for_Fast_Flying_Drones_2602.21101.pdf
- Code：https://github.com/uzh-rpg/event-sharp-nerf-drones（code_link_found_not_audited）
###### NeRF-MIR ｜ 2601.17350
- Paper：NeRF-MIR: Towards High-Quality Restoration of Masked Images with Neural Radiance Fields
- 一句话：NeRF-MIR 针对「建模运动/形变/时间一致性」，从「训练/监督角度」切入，主要采用「NeRF/辐射场/体渲染」来服务「动态场景与 4D 重建」。
- Method diagram：![2601.17350](method_figures/2601.17350_NeRF-MIR.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_NeRF_MIR_Towards_High_Quality_Restoration_of_Masked_Images_with_Neural_Radiance_Fields_2601.17350.pdf

##### 解法族：Pruning / compression / progressive coding（1）
###### 本文方法 ｜ 2603.08133
- Paper：Fast Low-light Enhancement and Deblurring for 3D Dark Scenes
- 一句话：本文方法 针对「建模运动/形变/时间一致性」，从「训练/监督角度」切入，主要采用「Pruning / compression / progressive coding」来服务「动态场景与 4D 重建」。
- Method diagram：![2603.08133](method_figures/2603.08133_paper.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Fast_Low_light_Enhancement_and_Deblurring_for_3D_Dark_Scenes_2603.08133.pdf

##### 解法族：SLAM / pose graph / online mapping pipeline（5；另有 2 篇见 full/csv）
###### Dark3R ｜ 2603.05330
- Paper：Dark3R: Learning Structure from Motion in the Dark
- 一句话：Dark3R 针对「建模运动/形变/时间一致性」，从「训练/监督角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「动态场景与 4D 重建」。
- Method diagram：![2603.05330](method_figures/2603.05330_Dark3R.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Dark3R_Learning_Structure_from_Motion_in_the_Dark_2603.05330.pdf
###### Multi-Scale ｜ 2602.13806
- Paper：Gaussian Sequences with Multi-Scale Dynamics for 4D Reconstruction from Monocular Casual Videos
- 一句话：Multi-Scale 针对「建模运动/形变/时间一致性」，从「训练/监督角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「动态场景与 4D 重建」。
- Method diagram：![2602.13806](method_figures/2602.13806_Multi-Scale.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Gaussian_Sequences_with_Multi_Scale_Dynamics_for_4D_Reconstruction_from_Monocular_Casual_V_2602.13806.pdf
###### Gaussian-Constrained ｜ 2602.07016
- Paper：Gaussian-Constrained LeJEPA Representations for Unsupervised Scene Discovery and Pose Consistency
- 一句话：Gaussian-Constrained 针对「建模运动/形变/时间一致性」，从「训练/监督角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「动态场景与 4D 重建」。
- Method diagram：![2602.07016](method_figures/2602.07016_Gaussian-Constrained.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Gaussian_Constrained_LeJEPA_Representations_for_Unsupervised_Scene_Discovery_and_Pose_Cons_2602.07016.pdf

#### 子问题：提升几何一致性/表面质量（3）
##### 解法族：Gaussian Splatting 表示与正则化（1）
###### GEAR ｜ 2604.07728
- Paper：GEAR: GEometry-motion Alternating Refinement for Articulated Object Modeling with Gaussian Splatting
- 一句话：GEAR 针对「提升几何一致性/表面质量」，从「训练/监督角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「动态场景与 4D 重建」。
- Method diagram：![2604.07728](method_figures/2604.07728_GEAR.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_GEAR_GEometry_motion_Alternating_Refinement_for_Articulated_Object_Modeling_with_Gaussian_2604.07728.pdf
- Code：https://github.com/VIPL-VSU/GEAR（code_link_found_not_audited）

##### 解法族：Motion decomposition / canonical space / deformation（1）
###### GeoSurDepth ｜ 2601.05839
- Paper：GeoSurDepth: Harnessing Foundation Model for Spatial Geometry Consistency-Oriented Self-Supervised Surround-View Depth Estimation
- 一句话：GeoSurDepth 针对「提升几何一致性/表面质量」，从「训练/监督角度」切入，主要采用「Motion decomposition / canonical space / deformation」来服务「动态场景与 4D 重建」。
- Method diagram：![2601.05839](method_figures/2601.05839_GeoSurDepth.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_GeoSurDepth_Harnessing_Foundation_Model_for_Spatial_Geometry_Consistency_Oriented_Self_Sup_2601.05839.pdf

##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### Hand3R ｜ 2602.03200
- Paper：Hand3R: Online 4D Hand-Scene Reconstruction in the Wild
- 一句话：Hand3R 针对「提升几何一致性/表面质量」，从「训练/监督角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「动态场景与 4D 重建」。
- Method diagram：![2602.03200](method_figures/2602.03200_Hand3R.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Hand3R_Online_4D_Hand_Scene_Reconstruction_in_the_Wild_2602.03200.pdf

#### 子问题：提升可控生成/世界演化预测（4）
##### 解法族：Diffusion/生成先验/视频模型（1）
###### Dynamic Worlds, Dynamic Humans ｜ 2601.19484
- Paper：Dynamic Worlds, Dynamic Humans: Generating Virtual Human-Scene Interaction Motion in Dynamic Scenes
- 一句话：Dynamic Worlds, Dynamic Humans 针对「提升可控生成/世界演化预测」，从「训练/监督角度」切入，主要采用「Diffusion/生成先验/视频模型」来服务「动态场景与 4D 重建」。
- Method diagram：![2601.19484](method_figures/2601.19484_Dynamic_Worlds_Dynamic_Humans.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Dynamic_Worlds_Dynamic_Humans_Generating_Virtual_Human_Scene_Interaction_Motion_in_Dynamic_2601.19484.pdf

##### 解法族：Feed-forward / Transformer / Foundation Model（1）
###### 本文方法 ｜ 2602.21467
- Paper：Geometric Priors for Generalizable World Models via Vector Symbolic Architecture
- 一句话：本文方法 针对「提升可控生成/世界演化预测」，从「训练/监督角度」切入，主要采用「Feed-forward / Transformer / Foundation Model」来服务「动态场景与 4D 重建」。
- Method diagram：![2602.21467](method_figures/2602.21467_paper.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Geometric_Priors_for_Generalizable_World_Models_via_Vector_Symbolic_Architecture_2602.21467.pdf

##### 解法族：Pruning / compression / progressive coding（1）
###### Latent-WAM ｜ 2603.24581
- Paper：Latent-WAM: Latent World Action Modeling for End-to-End Autonomous Driving
- 一句话：Latent-WAM 针对「提升可控生成/世界演化预测」，从「训练/监督角度」切入，主要采用「Pruning / compression / progressive coding」来服务「动态场景与 4D 重建」。
- Method diagram：![2603.24581](method_figures/2603.24581_Latent-WAM.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Latent_WAM_Latent_World_Action_Modeling_for_End_to_End_Autonomous_Driving_2603.24581.pdf
- Code：https://github.com/OpenDriveLab/OpenScene（code_link_found_not_audited）

##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### WestWorld ｜ 2603.14392
- Paper：WestWorld: A Knowledge-Encoded Scalable Trajectory World Model for Diverse Robotic Systems
- 一句话：WestWorld 针对「提升可控生成/世界演化预测」，从「训练/监督角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「动态场景与 4D 重建」。
- Method diagram：![2603.14392](method_figures/2603.14392_WestWorld.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_WestWorld_A_Knowledge_Encoded_Scalable_Trajectory_World_Model_for_Diverse_Robotic_Systems_2603.14392.pdf

#### 子问题：提升泛化/跨场景/开放世界能力（1）
##### 解法族：Motion decomposition / canonical space / deformation（1）
###### SynFlow ｜ 2604.09411
- Paper：SynFlow: Scaling Up LiDAR Scene Flow Estimation with Synthetic Data
- 一句话：SynFlow 针对「提升泛化/跨场景/开放世界能力」，从「训练/监督角度」切入，主要采用「Motion decomposition / canonical space / deformation」来服务「动态场景与 4D 重建」。
- Method diagram：![2604.09411](method_figures/2604.09411_SynFlow.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_SynFlow_Scaling_Up_LiDAR_Scene_Flow_Estimation_with_Synthetic_Data_2604.09411.pdf
- Code：https://github.com/Kin-Zhang/SynFlow（code_link_found_not_audited）

#### 子问题：解决稀疏视角几何不稳定（2）
##### 解法族：Gaussian Splatting 表示与正则化（2）
###### DSA-SRGS ｜ 2603.04770
- Paper：DSA-SRGS: Super-Resolution Gaussian Splatting for Dynamic Sparse-View DSA Reconstruction
- 一句话：DSA-SRGS 针对「解决稀疏视角几何不稳定」，从「训练/监督角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「动态场景与 4D 重建」。
- Method diagram：![2603.04770](method_figures/2603.04770_DSA-SRGS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_DSA_SRGS_Super_Resolution_Gaussian_Splatting_for_Dynamic_Sparse_View_DSA_Reconstruction_2603.04770.pdf
###### Zero-Shot ｜ 2602.07101
- Paper：Zero-Shot UAV Navigation in Forests via Relightable 3D Gaussian Splatting
- 一句话：Zero-Shot 针对「解决稀疏视角几何不稳定」，从「训练/监督角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「动态场景与 4D 重建」。
- Method diagram：![2602.07101](method_figures/2602.07101_Zero-Shot.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Zero_Shot_UAV_Navigation_in_Forests_via_Relightable_3D_Gaussian_Splatting_2602.07101.pdf

#### 子问题：降低显存/存储/模型体积（1）
##### 解法族：Pruning / compression / progressive coding（1）
###### SSD-GS ｜ 2604.13333
- Paper：SSD-GS: Scattering and Shadow Decomposition for Relightable 3D Gaussian Splatting
- 一句话：SSD-GS 针对「降低显存/存储/模型体积」，从「训练/监督角度」切入，主要采用「Pruning / compression / progressive coding」来服务「动态场景与 4D 重建」。
- Method diagram：![2604.13333](method_figures/2604.13333_SSD-GS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_SSD_GS_Scattering_and_Shadow_Decomposition_for_Relightable_3D_Gaussian_Splatting_2604.13333.pdf
- Code：https://github.com/irisfreesiri/SSD-GS（code_link_found_not_audited）

## Motivation：多视角几何/表面/场景重建（148）
### 切入点：数据/传感角度（2）
#### 子问题：提升几何一致性/表面质量（1）
##### 解法族：Motion decomposition / canonical space / deformation（1）
###### LiDAR ｜ 2603.03765
- Paper：LiDAR Prompted Spatio-Temporal Multi-View Stereo for Autonomous Driving
- 一句话：LiDAR 针对「提升几何一致性/表面质量」，从「数据/传感角度」切入，主要采用「Motion decomposition / canonical space / deformation」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2603.03765](method_figures/2603.03765_LiDAR.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_LiDAR_Prompted_Spatio_Temporal_Multi_View_Stereo_for_Autonomous_Driving_2603.03765.pdf
- Code：https://github.com/Akina2001/DriveMVS.git（code_link_found_not_audited）

#### 子问题：解决稀疏视角几何不稳定（1）
##### 解法族：Feed-forward / Transformer / Foundation Model（1）
###### DUSt3R ｜ 2312.14132
- Paper：DUSt3R: Geometric 3D Vision Made Easy
- 一句话：DUSt3R 针对「解决稀疏视角几何不稳定」，从「数据/传感角度」切入，主要采用「Feed-forward / Transformer / Foundation Model」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2312.14132](method_figures/2312.14132_DUSt3R.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2024_DUSt3R_Geometric_3D_Vision_Made_Easy_2312.14132.pdf
- Code：https://github.com/cdcseacave/openMVS（code_link_found_not_audited）

### 切入点：时空/动态角度（13）
#### 子问题：建模运动/形变/时间一致性（6）
##### 解法族：Gaussian Splatting 表示与正则化（1）
###### Rig-Aware ｜ 2601.14208
- Paper：Rig-Aware 3D Reconstruction of Vehicle Undercarriages using Gaussian Splatting
- 一句话：Rig-Aware 针对「建模运动/形变/时间一致性」，从「时空/动态角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2601.14208](method_figures/2601.14208_Rig-Aware.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Rig_Aware_3D_Reconstruction_of_Vehicle_Undercarriages_using_Gaussian_Splatting_2601.14208.pdf

##### 解法族：Motion decomposition / canonical space / deformation（2）
###### Non-Rigid ｜ 2603.02985
- Paper：The Dresden Dataset for 4D Reconstruction of Non-Rigid Abdominal Surgical Scenes
- 一句话：Non-Rigid 针对「建模运动/形变/时间一致性」，从「时空/动态角度」切入，主要采用「Motion decomposition / canonical space / deformation」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2603.02985](method_figures/2603.02985_Non-Rigid.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_The_Dresden_Dataset_for_4D_Reconstruction_of_Non_Rigid_Abdominal_Surgical_Scenes_2603.02985.pdf
- Code：https://github.com/reubendocea/d4d（code_link_found_not_audited）
###### WildDepth ｜ 2603.16816
- Paper：WildDepth: A Multimodal Dataset for 3D Wildlife Perception and Depth Estimation
- 一句话：WildDepth 针对「建模运动/形变/时间一致性」，从「时空/动态角度」切入，主要采用「Motion decomposition / canonical space / deformation」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2603.16816](method_figures/2603.16816_WildDepth.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_WildDepth_A_Multimodal_Dataset_for_3D_Wildlife_Perception_and_Depth_Estimation_2603.16816.pdf

##### 解法族：SDF/隐式表面/网格/点云（1）
###### Neu-PiG ｜ 2602.22212
- Paper：Neu-PiG: Neural Preconditioned Grids for Fast Dynamic Surface Reconstruction on Long Sequences
- 一句话：Neu-PiG 针对「建模运动/形变/时间一致性」，从「时空/动态角度」切入，主要采用「SDF/隐式表面/网格/点云」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2602.22212](method_figures/2602.22212_Neu-PiG.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Neu_PiG_Neural_Preconditioned_Grids_for_Fast_Dynamic_Surface_Reconstruction_on_Long_Sequen_2602.22212.pdf
- Code：https://github.com/vc-bonn/neu-pig（code_link_found_not_audited）

##### 解法族：SLAM / pose graph / online mapping pipeline（2）
###### Think, Act, Build ｜ 2604.00528
- Paper：Think, Act, Build: An Agentic Framework with Vision Language Models for Zero-Shot 3D Visual Grounding
- 一句话：Think, Act, Build 针对「建模运动/形变/时间一致性」，从「时空/动态角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2604.00528](method_figures/2604.00528_Think_Act_Build.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Think_Act_Build_An_Agentic_Framework_with_Vision_Language_Models_for_Zero_Shot_3D_Visual_G_2604.00528.pdf
- Code：https://github.com/WHB139426/TAB-Agent（code_link_found_not_audited）
###### Unblur-SLAM ｜ 2603.26810
- Paper：Unblur-SLAM: Dense Neural SLAM for Blurry Inputs
- 一句话：Unblur-SLAM 针对「建模运动/形变/时间一致性」，从「时空/动态角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2603.26810](method_figures/2603.26810_Unblur-SLAM.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Unblur_SLAM_Dense_Neural_SLAM_for_Blurry_Inputs_2603.26810.pdf
- Code：https://github.com/SlamMate/Unblur-SLAM.git（code_link_found_not_audited）

#### 子问题：提升几何一致性/表面质量（3）
##### 解法族：SDF/隐式表面/网格/点云（2）
###### GelSphere ｜ 2603.14104
- Paper：GelSphere: An Omnidirectional Rolling Vision-Based Tactile Sensor for Online 3D Reconstruction and Normal Force Estimation
- 一句话：GelSphere 针对「提升几何一致性/表面质量」，从「时空/动态角度」切入，主要采用「SDF/隐式表面/网格/点云」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2603.14104](method_figures/2603.14104_GelSphere.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_GelSphere_An_Omnidirectional_Rolling_Vision_Based_Tactile_Sensor_for_Online_3D_Reconstruct_2603.14104.pdf
- Code：https://github.com/nerfies/nerfies.github.io（code_link_found_not_audited）
###### Vista4D ｜ 2604.21915
- Paper：Vista4D: Video Reshooting with 4D Point Clouds
- 一句话：Vista4D 针对「提升几何一致性/表面质量」，从「时空/动态角度」切入，主要采用「SDF/隐式表面/网格/点云」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2604.21915](method_figures/2604.21915_Vista4D.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Vista4D_Video_Reshooting_with_4D_Point_Clouds_2604.21915.pdf
- Code：https://github.com/Eyeline-Labs/Vista4D（code_link_found_not_audited）

##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### SPARK ｜ 2601.08414
- Paper：SPARK: Scalable Real-Time Point Cloud Aggregation with Multi-View Self-Calibration
- 一句话：SPARK 针对「提升几何一致性/表面质量」，从「时空/动态角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2601.08414](method_figures/2601.08414_SPARK.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_SPARK_Scalable_Real_Time_Point_Cloud_Aggregation_with_Multi_View_Self_Calibration_2601.08414.pdf

#### 子问题：解决稀疏视角几何不稳定（4）
##### 解法族：Diffusion/生成先验/视频模型（1）
###### CAT3D ｜ 2405.10314
- Paper：CAT3D: Create Anything in 3D with Multi-View Diffusion Models
- 一句话：CAT3D 针对「解决稀疏视角几何不稳定」，从「时空/动态角度」切入，主要采用「Diffusion/生成先验/视频模型」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2405.10314](method_figures/2405.10314_CAT3D.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2024_CAT3D_Create_Anything_in_3D_with_Multi_View_Diffusion_Models_2405.10314.pdf

##### 解法族：SLAM / pose graph / online mapping pipeline（3）
###### MorphGS ｜ 2601.02716
- Paper：MorphGS: Morphology-Adaptive Articulated 3D Motion Transfer from Videos
- 一句话：MorphGS 针对「解决稀疏视角几何不稳定」，从「时空/动态角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2601.02716](method_figures/2601.02716_MorphGS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_MorphGS_Morphology_Adaptive_Articulated_3D_Motion_Transfer_from_Videos_2601.02716.pdf
###### NTIRE ｜ 2604.04135
- Paper：NTIRE 2026 3D Restoration and Reconstruction in Real-world Adverse Conditions: RealX3D Challenge Results
- 一句话：NTIRE 针对「解决稀疏视角几何不稳定」，从「时空/动态角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2604.04135](method_figures/2604.04135_NTIRE.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_NTIRE_2026_3D_Restoration_and_Reconstruction_in_Real_world_Adverse_Conditions_RealX3D_Chal_2604.04135.pdf
###### Low-Pass ｜ 2601.17900
- Paper：Revisiting 3D Reconstruction Kernels as Low-Pass Filters
- 一句话：Low-Pass 针对「解决稀疏视角几何不稳定」，从「时空/动态角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2601.17900](method_figures/2601.17900_Low-Pass.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Revisiting_3D_Reconstruction_Kernels_as_Low_Pass_Filters_2601.17900.pdf

### 切入点：系统/在线部署角度（1）
#### 子问题：接入 SLAM/机器人闭环系统（1）
##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### Memory Over Maps ｜ 2603.20530
- Paper：Memory Over Maps: 3D Object Localization Without Reconstruction
- 一句话：Memory Over Maps 针对「接入 SLAM/机器人闭环系统」，从「系统/在线部署角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2603.20530](method_figures/2603.20530_Memory_Over_Maps.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Memory_Over_Maps_3D_Object_Localization_Without_Reconstruction_2603.20530.pdf

### 切入点：表示/几何角度（88）
#### 子问题：减少优化/采样/渲染步骤（1）
##### 解法族：SDF/隐式表面/网格/点云（1）
###### Dirichlet-Regularized ｜ 2602.13801
- Paper：Joint Orientation and Weight Optimization for Robust Watertight Surface Reconstruction via Dirichlet-Regularized Winding Fields
- 一句话：Dirichlet-Regularized 针对「减少优化/采样/渲染步骤」，从「表示/几何角度」切入，主要采用「SDF/隐式表面/网格/点云」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2602.13801](method_figures/2602.13801_Dirichlet-Regularized.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Joint_Orientation_and_Weight_Optimization_for_Robust_Watertight_Surface_Reconstruction_via_2602.13801.pdf

#### 子问题：建模运动/形变/时间一致性（3）
##### 解法族：Gaussian Splatting 表示与正则化（3）
###### PatchPoison ｜ 2604.13153
- Paper：PatchPoison: Poisoning Multi-View Datasets to Degrade 3D Reconstruction
- 一句话：PatchPoison 针对「建模运动/形变/时间一致性」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2604.13153](method_figures/2604.13153_PatchPoison.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_PatchPoison_Poisoning_Multi_View_Datasets_to_Degrade_3D_Reconstruction_2604.13153.pdf
###### Reconstruction Matters ｜ 2603.19193
- Paper：Reconstruction Matters: Learning Geometry-Aligned BEV Representation through 3D Gaussian Splatting
- 一句话：Reconstruction Matters 针对「建模运动/形变/时间一致性」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2603.19193](method_figures/2603.19193_Reconstruction_Matters.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Reconstruction_Matters_Learning_Geometry_Aligned_BEV_Representation_through_3D_Gaussian_Sp_2603.19193.pdf
###### XSPLAIN ｜ 2602.10239
- Paper：XSPLAIN: XAI-enabling Splat-based Prototype Learning for Attribute-aware INterpretability
- 一句话：XSPLAIN 针对「建模运动/形变/时间一致性」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2602.10239](method_figures/2602.10239_XSPLAIN.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_XSPLAIN_XAI_enabling_Splat_based_Prototype_Learning_for_Attribute_aware_INterpretability_2602.10239.pdf
- Code：https://github.com/Solvro/ml-splat-xai（code_link_found_not_audited）

#### 子问题：提升几何一致性/表面质量（59）
##### 解法族：Feed-forward / Transformer / Foundation Model（3）
###### VGGT ｜ 2503.11651
- Paper：VGGT: Visual Geometry Grounded Transformer
- 一句话：VGGT 针对「提升几何一致性/表面质量」，从「表示/几何角度」切入，主要采用「Feed-forward / Transformer / Foundation Model」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2503.11651](method_figures/2503.11651_VGGT.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2025_VGGT_Visual_Geometry_Grounded_Transformer_2503.11651.pdf
- Code：https://github.com/facebookresearch/vggt（code_link_found_not_audited）
###### HGGT ｜ 2603.23997
- Paper：HGGT: Robust and Flexible 3D Hand Mesh Reconstruction from Uncalibrated Images
- 一句话：HGGT 针对「提升几何一致性/表面质量」，从「表示/几何角度」切入，主要采用「Feed-forward / Transformer / Foundation Model」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2603.23997](method_figures/2603.23997_HGGT.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_HGGT_Robust_and_Flexible_3D_Hand_Mesh_Reconstruction_from_Uncalibrated_Images_2603.23997.pdf
- Code：https://github.com/lym29/HGGT（code_link_found_not_audited）
###### Splat and Distill ｜ 2602.06032
- Paper：Splat and Distill: Augmenting Teachers with Feed-Forward 3D Reconstruction For 3D-Aware Distillation
- 一句话：Splat and Distill 针对「提升几何一致性/表面质量」，从「表示/几何角度」切入，主要采用「Feed-forward / Transformer / Foundation Model」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2602.06032](method_figures/2602.06032_Splat_and_Distill.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Splat_and_Distill_Augmenting_Teachers_with_Feed_Forward_3D_Reconstruction_For_3D_Aware_Dis_2602.06032.pdf
- Code：https://github.com/xapharius/pytorch-nyuv2（code_link_found_not_audited）

##### 解法族：Gaussian Splatting 表示与正则化（11；另有 8 篇见 full/csv）
###### Sparse-Voxel ｜ 2601.17720
- Paper：Advancing Structured Priors for Sparse-Voxel Surface Reconstruction
- 一句话：Sparse-Voxel 针对「提升几何一致性/表面质量」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2601.17720](method_figures/2601.17720_Sparse-Voxel.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Advancing_Structured_Priors_for_Sparse_Voxel_Surface_Reconstruction_2601.17720.pdf
###### Cross-Instance ｜ 2603.21936
- Paper：Cross-Instance Gaussian Splatting Registration via Geometry-Aware Feature-Guided Alignment
- 一句话：Cross-Instance 针对「提升几何一致性/表面质量」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2603.21936](method_figures/2603.21936_Cross-Instance.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Cross_Instance_Gaussian_Splatting_Registration_via_Geometry_Aware_Feature_Guided_Alignment_2603.21936.pdf
###### Dehaze-then-Splat ｜ 2604.13589
- Paper：Dehaze-then-Splat: Generative Dehazing with Physics-Informed 3D Gaussian Splatting for Smoke-Free Novel View Synthesis
- 一句话：Dehaze-then-Splat 针对「提升几何一致性/表面质量」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2604.13589](method_figures/2604.13589_Dehaze-then-Splat.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Dehaze_then_Splat_Generative_Dehazing_with_Physics_Informed_3D_Gaussian_Splatting_for_Smok_2604.13589.pdf
- Code：https://github.com/chen-yu-chao/3DRR_codebase（code_link_found_not_audited）

##### 解法族：Motion decomposition / canonical space / deformation（1）
###### Robo3R ｜ 2602.10101
- Paper：Robo3R: Enhancing Robotic Manipulation with Accurate Feed-Forward 3D Reconstruction
- 一句话：Robo3R 针对「提升几何一致性/表面质量」，从「表示/几何角度」切入，主要采用「Motion decomposition / canonical space / deformation」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2602.10101](method_figures/2602.10101_Robo3R.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Robo3R_Enhancing_Robotic_Manipulation_with_Accurate_Feed_Forward_3D_Reconstruction_2602.10101.pdf
- Code：https://github.com/InternRobotics/Robo3R（code_link_found_not_audited）

##### 解法族：NeRF/辐射场/体渲染（5；另有 2 篇见 full/csv）
###### Mip-NeRF 360 ｜ 2111.12077
- Paper：Mip-NeRF 360: Unbounded Anti-Aliased Neural Radiance Fields
- 一句话：Mip-NeRF 360 针对「提升几何一致性/表面质量」，从「表示/几何角度」切入，主要采用「NeRF/辐射场/体渲染」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2111.12077](method_figures/2111.12077_Mip-NeRF_360.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2022_Mip_NeRF_360_Unbounded_Anti_Aliased_Neural_Radiance_Fields_2111.12077.pdf
- Code：http://github.com/google-research/google-research/tree/master/jaxnerf（code_link_found_not_audited）
###### RegNeRF ｜ 2112.00724
- Paper：RegNeRF: Regularizing Neural Radiance Fields for View Synthesis from Sparse Inputs
- 一句话：RegNeRF 针对「提升几何一致性/表面质量」，从「表示/几何角度」切入，主要采用「NeRF/辐射场/体渲染」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2112.00724](method_figures/2112.00724_RegNeRF.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2021_RegNeRF_Regularizing_Neural_Radiance_Fields_for_View_Synthesis_from_Sparse_Inputs_2112.00724.pdf
- Code：https://github.com/google/mipnerf（code_link_found_not_audited）
###### EdgeNeRF ｜ 2601.01431
- Paper：EdgeNeRF: Edge-Guided Regularization for Neural Radiance Fields from Sparse Views
- 一句话：EdgeNeRF 针对「提升几何一致性/表面质量」，从「表示/几何角度」切入，主要采用「NeRF/辐射场/体渲染」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2601.01431](method_figures/2601.01431_EdgeNeRF.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_EdgeNeRF_Edge_Guided_Regularization_for_Neural_Radiance_Fields_from_Sparse_Views_2601.01431.pdf
- Code：https://github.com/skyhigh404/edgenerf（code_link_found_not_audited）

##### 解法族：SDF/隐式表面/网格/点云（26；另有 23 篇见 full/csv）
###### MonoSDF ｜ 2206.00665
- Paper：MonoSDF: Exploring Monocular Geometric Cues for Neural Implicit Surface Reconstruction
- 一句话：MonoSDF 针对「提升几何一致性/表面质量」，从「表示/几何角度」切入，主要采用「SDF/隐式表面/网格/点云」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2206.00665](method_figures/2206.00665_MonoSDF.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2022_MonoSDF_Exploring_Monocular_Geometric_Cues_for_Neural_Implicit_Surface_Reconstruction_2206.00665.pdf
- Code：https://github.com/autonomousvision/monosdf（code_link_found_not_audited）
###### 本文方法 ｜ 2003.09852
- Paper：Multiview Neural Surface Reconstruction by Disentangling Geometry and Appearance
- 一句话：本文方法 针对「提升几何一致性/表面质量」，从「表示/几何角度」切入，主要采用「SDF/隐式表面/网格/点云」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2003.09852](method_figures/2003.09852_paper.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2020_Multiview_Neural_Surface_Reconstruction_by_Disentangling_Geometry_and_Appearance_2003.09852.pdf
- Code：https://github.com/readthedocs/sphinx_rtd_theme（code_link_found_not_audited）
###### NeuS ｜ 2106.10689
- Paper：NeuS: Learning Neural Implicit Surfaces by Volume Rendering for Multi-view Reconstruction
- 一句话：NeuS 针对「提升几何一致性/表面质量」，从「表示/几何角度」切入，主要采用「SDF/隐式表面/网格/点云」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2106.10689](method_figures/2106.10689_NeuS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2023_NeuS_Learning_Neural_Implicit_Surfaces_by_Volume_Rendering_for_Multi_view_Reconstruction_2106.10689.pdf

##### 解法族：SLAM / pose graph / online mapping pipeline（11；另有 8 篇见 full/csv）
###### A 3D Reconstruction Benchmark for Asset Inspection ｜ 2603.17358
- Paper：A 3D Reconstruction Benchmark for Asset Inspection
- 一句话：A 3D Reconstruction Benchmark for Asset Inspection 针对「提升几何一致性/表面质量」，从「表示/几何角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2603.17358](method_figures/2603.17358_A_3D_Reconstruction_Benchmark_for_Asset_Inspection.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_A_3D_Reconstruction_Benchmark_for_Asset_Inspection_2603.17358.pdf
- Code：https://github.com/MichaelGrupp/evo（code_link_found_not_audited）
###### BayesFusion-SDF ｜ 2602.19697
- Paper：BayesFusion-SDF: Probabilistic Signed Distance Fusion with View Planning on CPU
- 一句话：BayesFusion-SDF 针对「提升几何一致性/表面质量」，从「表示/几何角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2602.19697](method_figures/2602.19697_BayesFusion-SDF.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_BayesFusion_SDF_Probabilistic_Signed_Distance_Fusion_with_View_Planning_on_CPU_2602.19697.pdf
- Code：https://github.com/mazumdarsoumya/BayesFusionSDF/edit/main/README.md（code_link_found_not_audited）
###### CEI-3D ｜ 2603.11810
- Paper：CEI-3D: Collaborative Explicit-Implicit 3D Reconstruction for Realistic and Fine-Grained Object Editing
- 一句话：CEI-3D 针对「提升几何一致性/表面质量」，从「表示/几何角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2603.11810](method_figures/2603.11810_CEI-3D.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_CEI_3D_Collaborative_Explicit_Implicit_3D_Reconstruction_for_Realistic_and_Fine_Grained_Ob_2603.11810.pdf
- Code：https://github.com/shiyue001/CEI-3D（code_link_found_not_audited）

##### 解法族：Sensor/domain-specific pipeline（2）
###### SatGeo-NeRF ｜ 2603.21931
- Paper：SatGeo-NeRF: Geometrically Regularized NeRF for Satellite Imagery
- 一句话：SatGeo-NeRF 针对「提升几何一致性/表面质量」，从「表示/几何角度」切入，主要采用「Sensor/domain-specific pipeline」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2603.21931](method_figures/2603.21931_SatGeo-NeRF.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_SatGeo_NeRF_Geometrically_Regularized_NeRF_for_Satellite_Imagery_2603.21931.pdf
###### UD-SfPNet ｜ 2603.00908
- Paper：UD-SfPNet: An Underwater Descattering Shape-from-Polarization Network for 3D Normal Reconstruction
- 一句话：UD-SfPNet 针对「提升几何一致性/表面质量」，从「表示/几何角度」切入，主要采用「Sensor/domain-specific pipeline」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2603.00908](method_figures/2603.00908_UD-SfPNet.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_UD_SfPNet_An_Underwater_Descattering_Shape_from_Polarization_Network_for_3D_Normal_Reconst_2603.00908.pdf
- Code：https://github.com/WangPuyun/UD-SfPNet（code_link_found_not_audited）

#### 子问题：提升可控生成/世界演化预测（1）
##### 解法族：Gaussian Splatting 表示与正则化（1）
###### F3DGS ｜ 2604.01605
- Paper：F3DGS: Federated 3D Gaussian Splatting for Decentralized Multi-Agent World Modeling
- 一句话：F3DGS 针对「提升可控生成/世界演化预测」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2604.01605](method_figures/2604.01605_F3DGS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_F3DGS_Federated_3D_Gaussian_Splatting_for_Decentralized_Multi_Agent_World_Modeling_2604.01605.pdf

#### 子问题：提升泛化/跨场景/开放世界能力（1）
##### 解法族：Feed-forward / Transformer / Foundation Model（1）
###### FF3R ｜ 2604.09862
- Paper：FF3R: Feedforward Feature 3D Reconstruction from Unconstrained views
- 一句话：FF3R 针对「提升泛化/跨场景/开放世界能力」，从「表示/几何角度」切入，主要采用「Feed-forward / Transformer / Foundation Model」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2604.09862](method_figures/2604.09862_FF3R.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_FF3R_Feedforward_Feature_3D_Reconstruction_from_Unconstrained_views_2604.09862.pdf
- Code：https://github.com/ChaoyiZh/ff3r（code_link_found_not_audited）

#### 子问题：解决稀疏视角几何不稳定（15）
##### 解法族：Feed-forward / Transformer / Foundation Model（1）
###### NOVA3R ｜ 2603.04179
- Paper：NOVA3R: Non-pixel-aligned Visual Transformer for Amodal 3D Reconstruction
- 一句话：NOVA3R 针对「解决稀疏视角几何不稳定」，从「表示/几何角度」切入，主要采用「Feed-forward / Transformer / Foundation Model」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2603.04179](method_figures/2603.04179_NOVA3R.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_NOVA3R_Non_pixel_aligned_Visual_Transformer_for_Amodal_3D_Reconstruction_2603.04179.pdf
- Code：https://github.com/wrchen530/nova3r（code_link_found_not_audited）

##### 解法族：Gaussian Splatting 表示与正则化（6；另有 3 篇见 full/csv）
###### BrepGaussian ｜ 2602.21105
- Paper：BrepGaussian: CAD reconstruction from Multi-View Images with Gaussian Splatting
- 一句话：BrepGaussian 针对「解决稀疏视角几何不稳定」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2602.21105](method_figures/2602.21105_BrepGaussian.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_BrepGaussian_CAD_reconstruction_from_Multi_View_Images_with_Gaussian_Splatting_2602.21105.pdf
###### COSMOS ｜ 2602.06044
- Paper：COSMOS: Coherent Supergaussian Modeling with Spatial Priors for Sparse-View 3D Splatting
- 一句话：COSMOS 针对「解决稀疏视角几何不稳定」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2602.06044](method_figures/2602.06044_COSMOS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2025_COSMOS_Coherent_Supergaussian_Modeling_with_Spatial_Priors_for_Sparse_View_3D_Splatting_2602.06044.pdf
###### ELoG-GS ｜ 2604.12592
- Paper：ELoG-GS: Dual-Branch Gaussian Splatting with Luminance-Guided Enhancement for Extreme Low-light 3D Reconstruction
- 一句话：ELoG-GS 针对「解决稀疏视角几何不稳定」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2604.12592](method_figures/2604.12592_ELoG-GS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_ELoG_GS_Dual_Branch_Gaussian_Splatting_with_Luminance_Guided_Enhancement_for_Extreme_Low_l_2604.12592.pdf
- Code：https://github.com/lyh120/FSGS_EAPGS（code_link_found_not_audited）

##### 解法族：NeRF/辐射场/体渲染（1）
###### TreeDGS ｜ 2601.12823
- Paper：TreeDGS: Aerial Gaussian Splatting for Distant DBH Measurement
- 一句话：TreeDGS 针对「解决稀疏视角几何不稳定」，从「表示/几何角度」切入，主要采用「NeRF/辐射场/体渲染」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2601.12823](method_figures/2601.12823_TreeDGS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_TreeDGS_Aerial_Gaussian_Splatting_for_Distant_DBH_Measurement_2601.12823.pdf
- Code：https://github.com/cdcseacave/openMVS（code_link_found_not_audited）

##### 解法族：SDF/隐式表面/网格/点云（1）
###### Pi-GS ｜ 2602.03327
- Paper：Pi-GS: Sparse-View Gaussian Splatting with Dense π^3 Initialization
- 一句话：Pi-GS 针对「解决稀疏视角几何不稳定」，从「表示/几何角度」切入，主要采用「SDF/隐式表面/网格/点云」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2602.03327](method_figures/2602.03327_Pi-GS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Pi_GS_Sparse_View_Gaussian_Splatting_with_Dense_3_Initialization_2602.03327.pdf
- Code：https://github.com/Mango0000/Pi-GS（code_link_found_not_audited）

##### 解法族：SLAM / pose graph / online mapping pipeline（6；另有 3 篇见 full/csv）
###### Affostruction ｜ 2601.09211
- Paper：Affostruction: 3D Affordance Grounding with Generative Reconstruction
- 一句话：Affostruction 针对「解决稀疏视角几何不稳定」，从「表示/几何角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2601.09211](method_figures/2601.09211_Affostruction.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Affostruction_3D_Affordance_Grounding_with_Generative_Reconstruction_2601.09211.pdf
- Code：https://github.com/chrockey/Affostruction（code_link_found_not_audited）
###### Dehallu3D ｜ 2603.01601
- Paper：Dehallu3D: Hallucination-Mitigated 3D Generation from Single Image via Cyclic View Consistency Refinement
- 一句话：Dehallu3D 针对「解决稀疏视角几何不稳定」，从「表示/几何角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2603.01601](method_figures/2603.01601_Dehallu3D.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Dehallu3D_Hallucination_Mitigated_3D_Generation_from_Single_Image_via_Cyclic_View_Consiste_2603.01601.pdf
###### FullCircle ｜ 2603.22572
- Paper：FullCircle: Effortless 3D Reconstruction from Casual 360$^\circ$ Captures
- 一句话：FullCircle 针对「解决稀疏视角几何不稳定」，从「表示/几何角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2603.22572](method_figures/2603.22572_FullCircle.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_FullCircle_Effortless_3D_Reconstruction_from_Casual_360_circ_Captures_2603.22572.pdf
- Code：https://github.com/theialab/fullcircle（code_link_found_not_audited）

#### 子问题：适配特殊传感器/行业场景（1）
##### 解法族：Sensor/domain-specific pipeline（1）
###### Agreement-Driven ｜ 2601.17791
- Paper：Agreement-Driven Multi-View 3D Reconstruction for Live Cattle Weight Estimation
- 一句话：Agreement-Driven 针对「适配特殊传感器/行业场景」，从「表示/几何角度」切入，主要采用「Sensor/domain-specific pipeline」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2601.17791](method_figures/2601.17791_Agreement-Driven.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Agreement_Driven_Multi_View_3D_Reconstruction_for_Live_Cattle_Weight_Estimation_2601.17791.pdf
- Code：https://github.com/devinli123/MV-SAM3D（code_link_found_not_audited）

#### 子问题：降低显存/存储/模型体积（7）
##### 解法族：Gaussian Splatting 表示与正则化（3）
###### 本文方法 ｜ 2602.08909
- Paper：Analysis of Converged 3D Gaussian Splatting Solutions: Density Effects and Prediction Limit
- 一句话：本文方法 针对「降低显存/存储/模型体积」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2602.08909](method_figures/2602.08909_paper.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Analysis_of_Converged_3D_Gaussian_Splatting_Solutions_Density_Effects_and_Prediction_Limit_2602.08909.pdf
###### 本文方法 ｜ 2602.14199
- Paper：Learnable Multi-level Discrete Wavelet Transforms for 3D Gaussian Splatting Frequency Modulation
- 一句话：本文方法 针对「降低显存/存储/模型体积」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2602.14199](method_figures/2602.14199_paper.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Learnable_Multi_level_Discrete_Wavelet_Transforms_for_3D_Gaussian_Splatting_Frequency_Modu_2602.14199.pdf
###### R3GW ｜ 2603.02801
- Paper：R3GW: Relightable 3D Gaussians for Outdoor Scenes in the Wild
- 一句话：R3GW 针对「降低显存/存储/模型体积」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2603.02801](method_figures/2603.02801_R3GW.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_R3GW_Relightable_3D_Gaussians_for_Outdoor_Scenes_in_the_Wild_2603.02801.pdf

##### 解法族：Pruning / compression / progressive coding（1）
###### Naka-GS ｜ 2604.11142
- Paper：Naka-GS: A Bionics-inspired Dual-Branch Naka Correction and Progressive Point Pruning for Low-Light 3DGS
- 一句话：Naka-GS 针对「降低显存/存储/模型体积」，从「表示/几何角度」切入，主要采用「Pruning / compression / progressive coding」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2604.11142](method_figures/2604.11142_Naka-GS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Naka_GS_A_Bionics_inspired_Dual_Branch_Naka_Correction_and_Progressive_Point_Pruning_for_L_2604.11142.pdf
- Code：https://github.com/RunyuZhu/Naka-GS（code_link_found_not_audited）

##### 解法族：SDF/隐式表面/网格/点云（3）
###### DualPrim ｜ 2603.16133
- Paper：DualPrim: Compact 3D Reconstruction with Positive and Negative Primitives
- 一句话：DualPrim 针对「降低显存/存储/模型体积」，从「表示/几何角度」切入，主要采用「SDF/隐式表面/网格/点云」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2603.16133](method_figures/2603.16133_DualPrim.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_DualPrim_Compact_3D_Reconstruction_with_Positive_and_Negative_Primitives_2603.16133.pdf
###### EvalMVX ｜ 2602.24065
- Paper：EvalMVX: A Unified Benchmarking for Neural 3D Reconstruction under Diverse Multiview Setups
- 一句话：EvalMVX 针对「降低显存/存储/模型体积」，从「表示/几何角度」切入，主要采用「SDF/隐式表面/网格/点云」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2602.24065](method_figures/2602.24065_EvalMVX.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_EvalMVX_A_Unified_Benchmarking_for_Neural_3D_Reconstruction_under_Diverse_Multiview_Setups_2602.24065.pdf
###### 本文方法 ｜ 2602.19182
- Paper：Thin Plate Spline Surface Reconstruction via the Method of Matched Sections
- 一句话：本文方法 针对「降低显存/存储/模型体积」，从「表示/几何角度」切入，主要采用「SDF/隐式表面/网格/点云」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2602.19182](method_figures/2602.19182_paper.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2025_Thin_Plate_Spline_Surface_Reconstruction_via_the_Method_of_Matched_Sections_2602.19182.pdf

### 切入点：计算角度（5）
#### 子问题：减少优化/采样/渲染步骤（1）
##### 解法族：Feed-forward / Transformer / Foundation Model（1）
###### Multi-View ｜ 2604.10246
- Paper：A Comparison of Multi-View Stereo Methods for Photogrammetric 3D Reconstruction: From Traditional to Learning-Based Approaches
- 一句话：Multi-View 针对「减少优化/采样/渲染步骤」，从「计算角度」切入，主要采用「Feed-forward / Transformer / Foundation Model」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2604.10246](method_figures/2604.10246_Multi-View.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_A_Comparison_of_Multi_View_Stereo_Methods_for_Photogrammetric_3D_Reconstruction_From_Tradi_2604.10246.pdf

#### 子问题：建模运动/形变/时间一致性（3）
##### 解法族：SLAM / pose graph / online mapping pipeline（3）
###### GMAC ｜ 2602.01033
- Paper：GMAC: Global Multi-View Constraint for Automatic Multi-Camera Extrinsic Calibration
- 一句话：GMAC 针对「建模运动/形变/时间一致性」，从「计算角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2602.01033](method_figures/2602.01033_GMAC.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_GMAC_Global_Multi_View_Constraint_for_Automatic_Multi_Camera_Extrinsic_Calibration_2602.01033.pdf
###### MoE3D ｜ 2601.05208
- Paper：MoE3D: A Mixture-of-Experts Module for 3D Reconstruction
- 一句话：MoE3D 针对「建模运动/形变/时间一致性」，从「计算角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2601.05208](method_figures/2601.05208_MoE3D.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_MoE3D_A_Mixture_of_Experts_Module_for_3D_Reconstruction_2601.05208.pdf
###### PAS3R ｜ 2603.21436
- Paper：PAS3R: Pose-Adaptive Streaming 3D Reconstruction for Long Video Sequences
- 一句话：PAS3R 针对「建模运动/形变/时间一致性」，从「计算角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2603.21436](method_figures/2603.21436_PAS3R.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_PAS3R_Pose_Adaptive_Streaming_3D_Reconstruction_for_Long_Video_Sequences_2603.21436.pdf
- Code：https://github.com/xlbjyxqc/PAS3R（code_link_found_not_audited）

#### 子问题：降低显存/存储/模型体积（1）
##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### FrameVGGT ｜ 2603.07690
- Paper：FrameVGGT: Geometry-Aligned Frame-Level Memory for Bounded Streaming VGGT
- 一句话：FrameVGGT 针对「降低显存/存储/模型体积」，从「计算角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2603.07690](method_figures/2603.07690_FrameVGGT.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_FrameVGGT_Geometry_Aligned_Frame_Level_Memory_for_Bounded_Streaming_VGGT_2603.07690.pdf

### 切入点：训练/监督角度（39）
#### 子问题：建模运动/形变/时间一致性（2）
##### 解法族：Sensor/domain-specific pipeline（1）
###### TransDex ｜ 2603.13869
- Paper：TransDex: Pre-training Visuo-Tactile Policy with Point Cloud Reconstruction for Dexterous Manipulation of Transparent Objects
- 一句话：TransDex 针对「建模运动/形变/时间一致性」，从「训练/监督角度」切入，主要采用「Sensor/domain-specific pipeline」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2603.13869](method_figures/2603.13869_TransDex.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_TransDex_Pre_training_Visuo_Tactile_Policy_with_Point_Cloud_Reconstruction_for_Dexterous_M_2603.13869.pdf
- Code：https://github.com/LFGfg/TransDex（code_link_found_not_audited）

##### 解法族：组合式/混合 pipeline（1）
###### SimpleProc ｜ 2604.04925
- Paper：SimpleProc: Fully Procedural Synthetic Data from Simple Rules for Multi-View Stereo
- 一句话：SimpleProc 针对「建模运动/形变/时间一致性」，从「训练/监督角度」切入，主要采用「组合式/混合 pipeline」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2604.04925](method_figures/2604.04925_SimpleProc.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_SimpleProc_Fully_Procedural_Synthetic_Data_from_Simple_Rules_for_Multi_View_Stereo_2604.04925.pdf
- Code：https://github.com/princeton-vl/SimpleProc（code_link_found_not_audited）

#### 子问题：接入 SLAM/机器人闭环系统（2）
##### 解法族：SLAM / pose graph / online mapping pipeline（2）
###### SurfSLAM ｜ 2601.10814
- Paper：SurfSLAM: Sim-to-Real Underwater Stereo Reconstruction For Real-Time SLAM
- 一句话：SurfSLAM 针对「接入 SLAM/机器人闭环系统」，从「训练/监督角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2601.10814](method_figures/2601.10814_SurfSLAM.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_SurfSLAM_Sim_to_Real_Underwater_Stereo_Reconstruction_For_Real_Time_SLAM_2601.10814.pdf
- Code：https://github.com/MichaelGrupp/evo（code_link_found_not_audited）
###### UniScale ｜ 2602.23224
- Paper：UniScale: Unified Scale-Aware 3D Reconstruction for Multi-View Understanding via Prior Injection for Robotic Perception
- 一句话：UniScale 针对「接入 SLAM/机器人闭环系统」，从「训练/监督角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2602.23224](method_figures/2602.23224_UniScale.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_UniScale_Unified_Scale_Aware_3D_Reconstruction_for_Multi_View_Understanding_via_Prior_Inje_2602.23224.pdf

#### 子问题：提升几何一致性/表面质量（12）
##### 解法族：Feed-forward / Transformer / Foundation Model（3）
###### GPA-VGGT ｜ 2601.16885
- Paper：GPA-VGGT:Adapting VGGT to Large Scale Localization by Self-Supervised Learning with Geometry and Physics Aware Loss
- 一句话：GPA-VGGT 针对「提升几何一致性/表面质量」，从「训练/监督角度」切入，主要采用「Feed-forward / Transformer / Foundation Model」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2601.16885](method_figures/2601.16885_GPA-VGGT.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_GPA_VGGT_Adapting_VGGT_to_Large_Scale_Localization_by_Self_Supervised_Learning_with_Geomet_2601.16885.pdf
- Code：https://github.com/X-yangfan/GPA-VGGT（code_link_found_not_audited）
###### to-3D ｜ 2603.05787
- Paper：Spectral Probing of Feature Upsamplers in 2D-to-3D Scene Reconstruction
- 一句话：to-3D 针对「提升几何一致性/表面质量」，从「训练/监督角度」切入，主要采用「Feed-forward / Transformer / Foundation Model」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2603.05787](method_figures/2603.05787_to-3D.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Spectral_Probing_of_Feature_Upsamplers_in_2D_to_3D_Scene_Reconstruction_2603.05787.pdf
###### VGGT-360 ｜ 2603.18943
- Paper：VGGT-360: Geometry-Consistent Zero-Shot Panoramic Depth Estimation
- 一句话：VGGT-360 针对「提升几何一致性/表面质量」，从「训练/监督角度」切入，主要采用「Feed-forward / Transformer / Foundation Model」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2603.18943](method_figures/2603.18943_VGGT-360.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_VGGT_360_Geometry_Consistent_Zero_Shot_Panoramic_Depth_Estimation_2603.18943.pdf

##### 解法族：Gaussian Splatting 表示与正则化（2）
###### OceanSplat ｜ 2601.04984
- Paper：OceanSplat: Object-aware Gaussian Splatting with Trinocular View Consistency for Underwater Scene Reconstruction
- 一句话：OceanSplat 针对「提升几何一致性/表面质量」，从「训练/监督角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2601.04984](method_figures/2601.04984_OceanSplat.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_OceanSplat_Object_aware_Gaussian_Splatting_with_Trinocular_View_Consistency_for_Underwater_2601.04984.pdf
###### SmokeGS-R ｜ 2604.05301
- Paper：SmokeGS-R: Physics-Guided Pseudo-Clean 3DGS for Real-World Multi-View Smoke Restoration
- 一句话：SmokeGS-R 针对「提升几何一致性/表面质量」，从「训练/监督角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2604.05301](method_figures/2604.05301_SmokeGS-R.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_SmokeGS_R_Physics_Guided_Pseudo_Clean_3DGS_for_Real_World_Multi_View_Smoke_Restoration_2604.05301.pdf
- Code：https://github.com/windrise/3drr_Track2_SmokeGS-R（code_link_found_not_audited）

##### 解法族：SDF/隐式表面/网格/点云（3）
###### Interaction-Aware ｜ 2604.05436
- Paper：Human Interaction-Aware 3D Reconstruction from a Single Image
- 一句话：Interaction-Aware 针对「提升几何一致性/表面质量」，从「训练/监督角度」切入，主要采用「SDF/隐式表面/网格/点云」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2604.05436](method_figures/2604.05436_Interaction-Aware.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Human_Interaction_Aware_3D_Reconstruction_from_a_Single_Image_2604.05436.pdf
- Code：https://github.com/ytrock/THuman2.0-Dataset/blob/main/THUman2.1_Agreement.pdf（code_link_found_not_audited）
###### High-Fidelity ｜ 2602.23926
- Paper：Leveraging Geometric Prior Uncertainty and Complementary Constraints for High-Fidelity Neural Indoor Surface Reconstruction
- 一句话：High-Fidelity 针对「提升几何一致性/表面质量」，从「训练/监督角度」切入，主要采用「SDF/隐式表面/网格/点云」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2602.23926](method_figures/2602.23926_High-Fidelity.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Leveraging_Geometric_Prior_Uncertainty_and_Complementary_Constraints_for_High_Fidelity_Neu_2602.23926.pdf
- Code：https://github.com/IRMVLab/GPU-SDF（code_link_found_not_audited）
###### UniSH ｜ 2601.01222
- Paper：UniSH: Unifying Scene and Human Reconstruction in a Feed-Forward Pass
- 一句话：UniSH 针对「提升几何一致性/表面质量」，从「训练/监督角度」切入，主要采用「SDF/隐式表面/网格/点云」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2601.01222](method_figures/2601.01222_UniSH.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_UniSH_Unifying_Scene_and_Human_Reconstruction_in_a_Feed_Forward_Pass_2601.01222.pdf
- Code：https://github.com/murphylmf/UniSH（code_link_found_not_audited）

##### 解法族：SLAM / pose graph / online mapping pipeline（3）
###### Language-Colored ｜ 2604.02546
- Paper：Contrastive Language-Colored Pointmap Pretraining for Unified 3D Scene Understanding
- 一句话：Language-Colored 针对「提升几何一致性/表面质量」，从「训练/监督角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2604.02546](method_figures/2604.02546_Language-Colored.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Contrastive_Language_Colored_Pointmap_Pretraining_for_Unified_3D_Scene_Understanding_2604.02546.pdf
- Code：https://github.com/Yebulabula/UniScene3D（code_link_found_not_audited）
###### 本文方法 ｜ 2604.18336
- Paper：Enhancing Glass Surface Reconstruction via Depth Prior for Robot Navigation
- 一句话：本文方法 针对「提升几何一致性/表面质量」，从「训练/监督角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2604.18336](method_figures/2604.18336_paper.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Enhancing_Glass_Surface_Reconstruction_via_Depth_Prior_for_Robot_Navigation_2604.18336.pdf
- Code：https://github.com/jarvisyjw/GlassRecon（code_link_found_not_audited）
###### FILT3R ｜ 2603.18493
- Paper：FILT3R: Latent State Adaptive Kalman Filter for Streaming 3D Reconstruction
- 一句话：FILT3R 针对「提升几何一致性/表面质量」，从「训练/监督角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2603.18493](method_figures/2603.18493_FILT3R.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_FILT3R_Latent_State_Adaptive_Kalman_Filter_for_Streaming_3D_Reconstruction_2603.18493.pdf
- Code：https://github.com/jinotter3/FILT3R（code_link_found_not_audited）

##### 解法族：Sensor/domain-specific pipeline（1）
###### SwiftGS ｜ 2603.18634
- Paper：SwiftGS: Episodic Priors for Immediate Satellite Surface Recovery
- 一句话：SwiftGS 针对「提升几何一致性/表面质量」，从「训练/监督角度」切入，主要采用「Sensor/domain-specific pipeline」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2603.18634](method_figures/2603.18634_SwiftGS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_SwiftGS_Episodic_Priors_for_Immediate_Satellite_Surface_Recovery_2603.18634.pdf

#### 子问题：提升可控生成/世界演化预测（2）
##### 解法族：SDF/隐式表面/网格/点云（1）
###### Pi-HOC ｜ 2604.12923
- Paper：Pi-HOC: Pairwise 3D Human-Object Contact Estimation
- 一句话：Pi-HOC 针对「提升可控生成/世界演化预测」，从「训练/监督角度」切入，主要采用「SDF/隐式表面/网格/点云」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2604.12923](method_figures/2604.12923_Pi-HOC.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Pi_HOC_Pairwise_3D_Human_Object_Contact_Estimation_2604.12923.pdf
- Code：https://github.com/SravanChittupalli/Pi-HOC（code_link_found_not_audited）

##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### Feed-Forward 3D Scene Modeling ｜ 2604.14025
- Paper：Feed-Forward 3D Scene Modeling: A Problem-Driven Perspective
- 一句话：Feed-Forward 3D Scene Modeling 针对「提升可控生成/世界演化预测」，从「训练/监督角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2604.14025](method_figures/2604.14025_Feed-Forward_3D_Scene_Modeling.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Feed_Forward_3D_Scene_Modeling_A_Problem_Driven_Perspective_2604.14025.pdf
- Code：https://github.com/ziplab/Awesome-Feed-Forward-3D（code_link_found_not_audited）

#### 子问题：提升泛化/跨场景/开放世界能力（4）
##### 解法族：Feed-forward / Transformer / Foundation Model（1）
###### Geo$^\textbf{2}$ ｜ 2603.25819
- Paper：Geo$^\textbf{2}$: Geometry-Guided Cross-view Geo-Localization and Image Synthesis
- 一句话：Geo$^\textbf{2}$ 针对「提升泛化/跨场景/开放世界能力」，从「训练/监督角度」切入，主要采用「Feed-forward / Transformer / Foundation Model」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2603.25819](method_figures/2603.25819_Geo_textbf_2.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Geo_textbf_2_Geometry_Guided_Cross_view_Geo_Localization_and_Image_Synthesis_2603.25819.pdf
- Code：https://github.com/google/nerfies/releases/tag/0.1（code_link_found_not_audited）

##### 解法族：SLAM / pose graph / online mapping pipeline（2）
###### ReplicateAnyScene ｜ 2604.10789
- Paper：ReplicateAnyScene: Zero-Shot Video-to-3D Composition via Textual-Visual-Spatial Alignment
- 一句话：ReplicateAnyScene 针对「提升泛化/跨场景/开放世界能力」，从「训练/监督角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2604.10789](method_figures/2604.10789_ReplicateAnyScene.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_ReplicateAnyScene_Zero_Shot_Video_to_3D_Composition_via_Textual_Visual_Spatial_Alignment_2604.10789.pdf
- Code：https://github.com/xiac20/ReplicateAnyScene（code_link_found_not_audited）
###### 本文方法 ｜ 2602.07891
- Paper：Scalable Adaptation of 3D Geometric Foundation Models via Weak Supervision from Internet Video
- 一句话：本文方法 针对「提升泛化/跨场景/开放世界能力」，从「训练/监督角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2602.07891](method_figures/2602.07891_paper.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Scalable_Adaptation_of_3D_Geometric_Foundation_Models_via_Weak_Supervision_from_Internet_V_2602.07891.pdf

##### 解法族：Sensor/domain-specific pipeline（1）
###### Single-Slice-to-3D ｜ 2602.09407
- Paper：Single-Slice-to-3D Reconstruction in Medical Imaging and Natural Objects: A Comparative Benchmark with SAM 3D
- 一句话：Single-Slice-to-3D 针对「提升泛化/跨场景/开放世界能力」，从「训练/监督角度」切入，主要采用「Sensor/domain-specific pipeline」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2602.09407](method_figures/2602.09407_Single-Slice-to-3D.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Single_Slice_to_3D_Reconstruction_in_Medical_Imaging_and_Natural_Objects_A_Comparative_Ben_2602.09407.pdf
- Code：https://github.com/luoyan407/Benchmark_3D_Generative_Models（code_link_found_not_audited）

#### 子问题：解决稀疏视角几何不稳定（14）
##### 解法族：Feed-forward / Transformer / Foundation Model（5；另有 2 篇见 full/csv）
###### Fisheye3R ｜ 2603.28896
- Paper：Fisheye3R: Adapting Unified 3D Feed-Forward Foundation Models to Fisheye Lenses
- 一句话：Fisheye3R 针对「解决稀疏视角几何不稳定」，从「训练/监督角度」切入，主要采用「Feed-forward / Transformer / Foundation Model」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2603.28896](method_figures/2603.28896_Fisheye3R.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Fisheye3R_Adapting_Unified_3D_Feed_Forward_Foundation_Models_to_Fisheye_Lenses_2603.28896.pdf
###### 本文方法 ｜ 2604.03878
- Paper：Learning 3D Reconstruction with Priors in Test Time
- 一句话：本文方法 针对「解决稀疏视角几何不稳定」，从「训练/监督角度」切入，主要采用「Feed-forward / Transformer / Foundation Model」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2604.03878](method_figures/2604.03878_paper.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Learning_3D_Reconstruction_with_Priors_in_Test_Time_2604.03878.pdf
- Code：https://github.com/cvlab-stonybrook/TCO（code_link_found_not_audited）
###### PanoVGGT ｜ 2603.17571
- Paper：PanoVGGT: Feed-Forward 3D Reconstruction from Panoramic Imagery
- 一句话：PanoVGGT 针对「解决稀疏视角几何不稳定」，从「训练/监督角度」切入，主要采用「Feed-forward / Transformer / Foundation Model」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2603.17571](method_figures/2603.17571_PanoVGGT.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_PanoVGGT_Feed_Forward_3D_Reconstruction_from_Panoramic_Imagery_2603.17571.pdf

##### 解法族：Gaussian Splatting 表示与正则化（2）
###### Satellite-Free ｜ 2604.01581
- Paper：Satellite-Free Training for Drone-View Geo-Localization
- 一句话：Satellite-Free 针对「解决稀疏视角几何不稳定」，从「训练/监督角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2604.01581](method_figures/2604.01581_Satellite-Free.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Satellite_Free_Training_for_Drone_View_Geo_Localization_2604.01581.pdf
###### Scene-Agnostic ｜ 2604.09045
- Paper：Scene-Agnostic Object-Centric Representation Learning for 3D Gaussian Splatting
- 一句话：Scene-Agnostic 针对「解决稀疏视角几何不稳定」，从「训练/监督角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2604.09045](method_figures/2604.09045_Scene-Agnostic.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Scene_Agnostic_Object_Centric_Representation_Learning_for_3D_Gaussian_Splatting_2604.09045.pdf

##### 解法族：SDF/隐式表面/网格/点云（2）
###### ArtHOI ｜ 2603.25791
- Paper：ArtHOI: Taming Foundation Models for Monocular 4D Reconstruction of Hand-Articulated-Object Interactions
- 一句话：ArtHOI 针对「解决稀疏视角几何不稳定」，从「训练/监督角度」切入，主要采用「SDF/隐式表面/网格/点云」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2603.25791](method_figures/2603.25791_ArtHOI.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_ArtHOI_Taming_Foundation_Models_for_Monocular_4D_Reconstruction_of_Hand_Articulated_Object_2603.25791.pdf
- Code：https://github.com/hitcs-zikaiwang/ArtHOI-4D-Reconstruction（code_link_found_not_audited）
###### Human-Scene ｜ 2603.12789
- Paper：Coherent Human-Scene Reconstruction from Multi-Person Multi-View Video in a Single Pass
- 一句话：Human-Scene 针对「解决稀疏视角几何不稳定」，从「训练/监督角度」切入，主要采用「SDF/隐式表面/网格/点云」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2603.12789](method_figures/2603.12789_Human-Scene.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Coherent_Human_Scene_Reconstruction_from_Multi_Person_Multi_View_Video_in_a_Single_Pass_2603.12789.pdf

##### 解法族：SLAM / pose graph / online mapping pipeline（5；另有 2 篇见 full/csv）
###### CMHANet ｜ 2603.12721
- Paper：CMHANet: A Cross-Modal Hybrid Attention Network for Point Cloud Registration
- 一句话：CMHANet 针对「解决稀疏视角几何不稳定」，从「训练/监督角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2603.12721](method_figures/2603.12721_CMHANet.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_CMHANet_A_Cross_Modal_Hybrid_Attention_Network_for_Point_Cloud_Registration_2603.12721.pdf
- Code：https://github.com/DongXu-Zhang/CMHANet（code_link_found_not_audited）
###### MLLM ｜ 2604.06725
- Paper：Enhancing MLLM Spatial Understanding via Active 3D Scene Exploration for Multi-Perspective Reasoning
- 一句话：MLLM 针对「解决稀疏视角几何不稳定」，从「训练/监督角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2604.06725](method_figures/2604.06725_MLLM.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Enhancing_MLLM_Spatial_Understanding_via_Active_3D_Scene_Exploration_for_Multi_Perspective_2604.06725.pdf
###### Reliev3R ｜ 2604.00548
- Paper：Reliev3R: Relieving Feed-forward Reconstruction from Multi-View Geometric Annotations
- 一句话：Reliev3R 针对「解决稀疏视角几何不稳定」，从「训练/监督角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2604.00548](method_figures/2604.00548_Reliev3R.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Reliev3R_Relieving_Feed_forward_Reconstruction_from_Multi_View_Geometric_Annotations_2604.00548.pdf

#### 子问题：适配特殊传感器/行业场景（1）
##### 解法族：NeRF/辐射场/体渲染（1）
###### NeRF ｜ 2603.18306
- Paper：Fast and Generalizable NeRF Architecture Selection for Satellite Scene Reconstruction
- 一句话：NeRF 针对「适配特殊传感器/行业场景」，从「训练/监督角度」切入，主要采用「NeRF/辐射场/体渲染」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2603.18306](method_figures/2603.18306_NeRF.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Fast_and_Generalizable_NeRF_Architecture_Selection_for_Satellite_Scene_Reconstruction_2603.18306.pdf

#### 子问题：降低显存/存储/模型体积（2）
##### 解法族：SDF/隐式表面/网格/点云（1）
###### EventNeuS ｜ 2602.03847
- Paper：EventNeuS: 3D Mesh Reconstruction from a Single Event Camera
- 一句话：EventNeuS 针对「降低显存/存储/模型体积」，从「训练/监督角度」切入，主要采用「SDF/隐式表面/网格/点云」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2602.03847](method_figures/2602.03847_EventNeuS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_EventNeuS_3D_Mesh_Reconstruction_from_a_Single_Event_Camera_2602.03847.pdf
- Code：https://github.com/NVlabs/tiny-cuda-nn（code_link_found_not_audited）

##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### GAP-MLLM ｜ 2603.16461
- Paper：GAP-MLLM: Geometry-Aligned Pre-training for Activating 3D Spatial Perception in Multimodal Large Language Models
- 一句话：GAP-MLLM 针对「降低显存/存储/模型体积」，从「训练/监督角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「多视角几何/表面/场景重建」。
- Method diagram：![2603.16461](method_figures/2603.16461_GAP-MLLM.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_GAP_MLLM_Geometry_Aligned_Pre_training_for_Activating_3D_Spatial_Perception_in_Multimodal_2603.16461.pdf

## Motivation：实时/大规模/高效 3D 表示（155）
### 切入点：内存/存储角度（18）
#### 子问题：解决稀疏视角几何不稳定（1）
##### 解法族：Gaussian Splatting 表示与正则化（1）
###### 本文方法 ｜ 2602.20933
- Paper：Dropping Anchor and Spherical Harmonics for Sparse-view Gaussian Splatting
- 一句话：本文方法 针对「解决稀疏视角几何不稳定」，从「内存/存储角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2602.20933](method_figures/2602.20933_paper.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Dropping_Anchor_and_Spherical_Harmonics_for_Sparse_view_Gaussian_Splatting_2602.20933.pdf

#### 子问题：降低显存/存储/模型体积（17）
##### 解法族：Feed-forward / Transformer / Foundation Model（1）
###### HeSS ｜ 2603.25336
- Paper：HeSS: Head Sensitivity Score for Sparsity Redistribution in VGGT
- 一句话：HeSS 针对「降低显存/存储/模型体积」，从「内存/存储角度」切入，主要采用「Feed-forward / Transformer / Foundation Model」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2603.25336](method_figures/2603.25336_HeSS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_HeSS_Head_Sensitivity_Score_for_Sparsity_Redistribution_in_VGGT_2603.25336.pdf
- Code：https://github.com/libary753/HeSS（code_link_found_not_audited）

##### 解法族：NeRF/辐射场/体渲染（1）
###### Multi-Resolution ｜ 2604.02836
- Paper：Factorized Multi-Resolution HashGrid for Efficient Neural Radiance Fields: Execution on Edge-Devices
- 一句话：Multi-Resolution 针对「降低显存/存储/模型体积」，从「内存/存储角度」切入，主要采用「NeRF/辐射场/体渲染」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2604.02836](method_figures/2604.02836_Multi-Resolution.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Factorized_Multi_Resolution_HashGrid_for_Efficient_Neural_Radiance_Fields_Execution_on_Edg_2604.02836.pdf
- Code：https://github.com/postech-ami/Fact-Hash（code_link_found_not_audited）

##### 解法族：Pruning / compression / progressive coding（14；另有 11 篇见 full/csv）
###### 3DTurboQuant ｜ 2604.05366
- Paper：3DTurboQuant: Training-Free Near-Optimal Quantization for 3D Reconstruction Models
- 一句话：3DTurboQuant 针对「降低显存/存储/模型体积」，从「内存/存储角度」切入，主要采用「Pruning / compression / progressive coding」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2604.05366](method_figures/2604.05366_3DTurboQuant.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_3DTurboQuant_Training_Free_Near_Optimal_Quantization_for_3D_Reconstruction_Models_2604.05366.pdf
- Code：https://github.com/JaeLee18/3DTurboQuant（code_link_found_not_audited）
###### Clean-GS ｜ 2601.00913
- Paper：Clean-GS: Semantic Mask-Guided Pruning for 3D Gaussian Splatting
- 一句话：Clean-GS 针对「降低显存/存储/模型体积」，从「内存/存储角度」切入，主要采用「Pruning / compression / progressive coding」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2601.00913](method_figures/2601.00913_Clean-GS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Clean_GS_Semantic_Mask_Guided_Pruning_for_3D_Gaussian_Splatting_2601.00913.pdf
- Code：https://github.com/smlab-niser/clean-gs（code_link_found_not_audited）
###### GS^2 ｜ 2604.01884
- Paper：GS^2: Graph-based Spatial Distribution Optimization for Compact 3D Gaussian Splatting
- 一句话：GS^2 针对「降低显存/存储/模型体积」，从「内存/存储角度」切入，主要采用「Pruning / compression / progressive coding」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2604.01884](method_figures/2604.01884_GS_2.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_GS_2_Graph_based_Spatial_Distribution_Optimization_for_Compact_3D_Gaussian_Splatting_2604.01884.pdf
- Code：https://github.com/BJTU-KD3D/GS-2（code_link_found_not_audited）

##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### VGGT-SLAM++ ｜ 2604.06830
- Paper：VGGT-SLAM++
- 一句话：VGGT-SLAM++ 针对「降低显存/存储/模型体积」，从「内存/存储角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2604.06830](method_figures/2604.06830_VGGT-SLAM.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_VGGT_SLAM_2604.06830.pdf

### 切入点：时空/动态角度（12）
#### 子问题：减少优化/采样/渲染步骤（2）
##### 解法族：Gaussian Splatting 表示与正则化（1）
###### FastPhysGS ｜ 2602.01723
- Paper：FastPhysGS: Accelerating Physics-based Dynamic 3DGS Simulation via Interior Completion and Adaptive Optimization
- 一句话：FastPhysGS 针对「减少优化/采样/渲染步骤」，从「时空/动态角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2602.01723](method_figures/2602.01723_FastPhysGS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_FastPhysGS_Accelerating_Physics_based_Dynamic_3DGS_Simulation_via_Interior_Completion_and_2602.01723.pdf

##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### Real-Time ｜ 2602.00466
- Paper：Stealthy Coverage Control for Human-enabled Real-Time 3D Reconstruction
- 一句话：Real-Time 针对「减少优化/采样/渲染步骤」，从「时空/动态角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2602.00466](method_figures/2602.00466_Real-Time.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Stealthy_Coverage_Control_for_Human_enabled_Real_Time_3D_Reconstruction_2602.00466.pdf

#### 子问题：建模运动/形变/时间一致性（5）
##### 解法族：Gaussian Splatting 表示与正则化（1）
###### GHOST ｜ 2603.18912
- Paper：GHOST: Fast Category-agnostic Hand-Object Interaction Reconstruction from RGB Videos using Gaussian Splatting
- 一句话：GHOST 针对「建模运动/形变/时间一致性」，从「时空/动态角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2603.18912](method_figures/2603.18912_GHOST.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_GHOST_Fast_Category_agnostic_Hand_Object_Interaction_Reconstruction_from_RGB_Videos_using_2603.18912.pdf
- Code：https://github.com/ATAboukhadra/GHOST（code_link_found_not_audited）

##### 解法族：Motion decomposition / canonical space / deformation（1）
###### 本文方法 ｜ 2603.19543
- Paper：Zero Shot Deformation Reconstruction for Soft Robots Using a Flexible Sensor Array and Cage Based 3D Gaussian Modeling
- 一句话：本文方法 针对「建模运动/形变/时间一致性」，从「时空/动态角度」切入，主要采用「Motion decomposition / canonical space / deformation」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2603.19543](method_figures/2603.19543_paper.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Zero_Shot_Deformation_Reconstruction_for_Soft_Robots_Using_a_Flexible_Sensor_Array_and_Cag_2603.19543.pdf

##### 解法族：SLAM / pose graph / online mapping pipeline（3）
###### 4K4D ｜ 2310.11448
- Paper：4K4D: Real-Time 4D View Synthesis at 4K Resolution
- 一句话：4K4D 针对「建模运动/形变/时间一致性」，从「时空/动态角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2310.11448](method_figures/2310.11448_4K4D.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2023_4K4D_Real_Time_4D_View_Synthesis_at_4K_Resolution_2310.11448.pdf
- Code：https://github.com/zju3dv/4K4D（code_link_found_not_audited）
###### Mem3R ｜ 2604.07279
- Paper：Mem3R: Streaming 3D Reconstruction with Hybrid Memory via Test-Time Training
- 一句话：Mem3R 针对「建模运动/形变/时间一致性」，从「时空/动态角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2604.07279](method_figures/2604.07279_Mem3R.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Mem3R_Streaming_3D_Reconstruction_with_Hybrid_Memory_via_Test_Time_Training_2604.07279.pdf
- Code：https://github.com/lck666666/Mem3R（code_link_found_not_audited）
###### Splats in Splats++ ｜ 2604.15862
- Paper：Splats in Splats++: Robust and Generalizable 3D Gaussian Splatting Steganography
- 一句话：Splats in Splats++ 针对「建模运动/形变/时间一致性」，从「时空/动态角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2604.15862](method_figures/2604.15862_Splats_in_Splats.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Splats_in_Splats_Robust_and_Generalizable_3D_Gaussian_Splatting_Steganography_2604.15862.pdf

#### 子问题：接入 SLAM/机器人闭环系统（1）
##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### FUSE-Flow ｜ 2602.01035
- Paper：FUSE-Flow: Scalable Real-Time Multi-View Point Cloud Reconstruction Using Confidence
- 一句话：FUSE-Flow 针对「接入 SLAM/机器人闭环系统」，从「时空/动态角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2602.01035](method_figures/2602.01035_FUSE-Flow.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_FUSE_Flow_Scalable_Real_Time_Multi_View_Point_Cloud_Reconstruction_Using_Confidence_2602.01035.pdf

#### 子问题：提升可控生成/世界演化预测（2）
##### 解法族：Gaussian Splatting 表示与正则化（1）
###### GSStream ｜ 2603.09718
- Paper：GSStream: 3D Gaussian Splatting based Volumetric Scene Streaming System
- 一句话：GSStream 针对「提升可控生成/世界演化预测」，从「时空/动态角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2603.09718](method_figures/2603.09718_GSStream.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_GSStream_3D_Gaussian_Splatting_based_Volumetric_Scene_Streaming_System_2603.09718.pdf

##### 解法族：Motion decomposition / canonical space / deformation（1）
###### PointWorld ｜ 2601.03782
- Paper：PointWorld: Scaling 3D World Models for In-The-Wild Robotic Manipulation
- 一句话：PointWorld 针对「提升可控生成/世界演化预测」，从「时空/动态角度」切入，主要采用「Motion decomposition / canonical space / deformation」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2601.03782](method_figures/2601.03782_PointWorld.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_PointWorld_Scaling_3D_World_Models_for_In_The_Wild_Robotic_Manipulation_2601.03782.pdf
- Code：https://github.com/NVlabs/PointWorld（code_link_found_not_audited）

#### 子问题：解决稀疏视角几何不稳定（1）
##### 解法族：Gaussian Splatting 表示与正则化（1）
###### LoD-Structured ｜ 2601.18475
- Paper：LoD-Structured 3D Gaussian Splatting for Streaming Video Reconstruction
- 一句话：LoD-Structured 针对「解决稀疏视角几何不稳定」，从「时空/动态角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2601.18475](method_figures/2601.18475_LoD-Structured.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_LoD_Structured_3D_Gaussian_Splatting_for_Streaming_Video_Reconstruction_2601.18475.pdf

#### 子问题：降低显存/存储/模型体积（1）
##### 解法族：Pruning / compression / progressive coding（1）
###### Interpreting Physics in Video World Models ｜ 2602.07050
- Paper：Interpreting Physics in Video World Models
- 一句话：Interpreting Physics in Video World Models 针对「降低显存/存储/模型体积」，从「时空/动态角度」切入，主要采用「Pruning / compression / progressive coding」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2602.07050](method_figures/2602.07050_Interpreting_Physics_in_Video_World_Models.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Interpreting_Physics_in_Video_World_Models_2602.07050.pdf

### 切入点：生成/世界模型角度（1）
#### 子问题：提升可控生成/世界演化预测（1）
##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### Kinematics-Aware ｜ 2603.07264
- Paper：Kinematics-Aware Latent World Models for Data-Efficient Autonomous Driving
- 一句话：Kinematics-Aware 针对「提升可控生成/世界演化预测」，从「生成/世界模型角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2603.07264](method_figures/2603.07264_Kinematics-Aware.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Kinematics_Aware_Latent_World_Models_for_Data_Efficient_Autonomous_Driving_2603.07264.pdf

### 切入点：系统/在线部署角度（2）
#### 子问题：接入 SLAM/机器人闭环系统（2）
##### 解法族：Gaussian Splatting 表示与正则化（1）
###### High-Fidelity ｜ 2601.03200
- Paper：A High-Fidelity Digital Twin for Robotic Manipulation Based on 3D Gaussian Splatting
- 一句话：High-Fidelity 针对「接入 SLAM/机器人闭环系统」，从「系统/在线部署角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2601.03200](method_figures/2601.03200_High-Fidelity.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_A_High_Fidelity_Digital_Twin_for_Robotic_Manipulation_Based_on_3D_Gaussian_Splatting_2601.03200.pdf
- Code：https://github.com/aras-p/UnityGaussianSplatting（code_link_found_not_audited）

##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### Model-Based ｜ 2602.02430
- Paper：3D Foundation Model-Based Loop Closing for Decentralized Collaborative SLAM
- 一句话：Model-Based 针对「接入 SLAM/机器人闭环系统」，从「系统/在线部署角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2602.02430](method_figures/2602.02430_Model-Based.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_3D_Foundation_Model_Based_Loop_Closing_for_Decentralized_Collaborative_SLAM_2602.02430.pdf

### 切入点：表示/几何角度（44）
#### 子问题：减少优化/采样/渲染步骤（6）
##### 解法族：Gaussian Splatting 表示与正则化（4；另有 1 篇见 full/csv）
###### LAGS ｜ 2604.16910
- Paper：LAGS: Low-Altitude Gaussian Splatting with Groupwise Heterogeneous Graph Learning
- 一句话：LAGS 针对「减少优化/采样/渲染步骤」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2604.16910](method_figures/2604.16910_LAGS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_LAGS_Low_Altitude_Gaussian_Splatting_with_Groupwise_Heterogeneous_Graph_Learning_2604.16910.pdf
###### Neural Gabor Splatting ｜ 2604.15941
- Paper：Neural Gabor Splatting: Enhanced Gaussian Splatting with Neural Gabor for High-frequency Surface Reconstruction
- 一句话：Neural Gabor Splatting 针对「减少优化/采样/渲染步骤」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2604.15941](method_figures/2604.15941_Neural_Gabor_Splatting.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Neural_Gabor_Splatting_Enhanced_Gaussian_Splatting_with_Neural_Gabor_for_High_frequency_Su_2604.15941.pdf
- Code：https://github.com/haato-w/neural-gabor-splatting（code_link_found_not_audited）
###### RefracGS ｜ 2603.21695
- Paper：RefracGS: Novel View Synthesis Through Refractive Water Surfaces with 3D Gaussian Ray Tracing
- 一句话：RefracGS 针对「减少优化/采样/渲染步骤」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2603.21695](method_figures/2603.21695_RefracGS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_RefracGS_Novel_View_Synthesis_Through_Refractive_Water_Surfaces_with_3D_Gaussian_Ray_Traci_2603.21695.pdf
- Code：https://github.com/eliahuhorwitz/Academic-project-page-template（code_link_found_not_audited）

##### 解法族：NeRF/辐射场/体渲染（1）
###### GEMM-GS ｜ 2604.02120
- Paper：GEMM-GS: Accelerating 3D Gaussian Splatting on Tensor Cores with GEMM-Compatible Blending
- 一句话：GEMM-GS 针对「减少优化/采样/渲染步骤」，从「表示/几何角度」切入，主要采用「NeRF/辐射场/体渲染」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2604.02120](method_figures/2604.02120_GEMM-GS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_GEMM_GS_Accelerating_3D_Gaussian_Splatting_on_Tensor_Cores_with_GEMM_Compatible_Blending_2604.02120.pdf
- Code：https://github.com/shieldforever/GEMM-GS（code_link_found_not_audited）

##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### R3-RECON ｜ 2601.07484
- Paper：R3-RECON: Radiance-Field-Free Active Reconstruction via Renderability
- 一句话：R3-RECON 针对「减少优化/采样/渲染步骤」，从「表示/几何角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2601.07484](method_figures/2601.07484_R3-RECON.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_R3_RECON_Radiance_Field_Free_Active_Reconstruction_via_Renderability_2601.07484.pdf
- Code：https://github.com/jkff00/r3recon（code_link_found_not_audited）

#### 子问题：建模运动/形变/时间一致性（7）
##### 解法族：Gaussian Splatting 表示与正则化（5；另有 2 篇见 full/csv）
###### 本文方法 ｜ 2601.01660
- Paper：Animated 3DGS Avatars in Diverse Scenes with Consistent Lighting and Shadows
- 一句话：本文方法 针对「建模运动/形变/时间一致性」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2601.01660](method_figures/2601.01660_paper.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Animated_3DGS_Avatars_in_Diverse_Scenes_with_Consistent_Lighting_and_Shadows_2601.01660.pdf
###### Generalized non-exponential Gaussian splatting ｜ 2603.02887
- Paper：Generalized non-exponential Gaussian splatting
- 一句话：Generalized non-exponential Gaussian splatting 针对「建模运动/形变/时间一致性」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2603.02887](method_figures/2603.02887_Generalized_non-exponential_Gaussian_splatting.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Generalized_non_exponential_Gaussian_splatting_2603.02887.pdf
###### Habitat-GS ｜ 2604.12626
- Paper：Habitat-GS: A High-Fidelity Navigation Simulator with Dynamic Gaussian Splatting
- 一句话：Habitat-GS 针对「建模运动/形变/时间一致性」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2604.12626](method_figures/2604.12626_Habitat-GS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Habitat_GS_A_High_Fidelity_Navigation_Simulator_with_Dynamic_Gaussian_Splatting_2604.12626.pdf
- Code：https://github.com/zju3dv/habitat-gs（code_link_found_not_audited）

##### 解法族：Motion decomposition / canonical space / deformation（1）
###### RGB-LiDAR ｜ 2603.06061
- Paper：Transforming Omnidirectional RGB-LiDAR data into 3D Gaussian Splatting
- 一句话：RGB-LiDAR 针对「建模运动/形变/时间一致性」，从「表示/几何角度」切入，主要采用「Motion decomposition / canonical space / deformation」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2603.06061](method_figures/2603.06061_RGB-LiDAR.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Transforming_Omnidirectional_RGB_LiDAR_data_into_3D_Gaussian_Splatting_2603.06061.pdf

##### 解法族：NeRF/辐射场/体渲染（1）
###### NERFIFY ｜ 2603.00805
- Paper：NERFIFY: A Multi-Agent Framework for Turning NeRF Papers into Code
- 一句话：NERFIFY 针对「建模运动/形变/时间一致性」，从「表示/几何角度」切入，主要采用「NeRF/辐射场/体渲染」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2603.00805](method_figures/2603.00805_NERFIFY.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_NERFIFY_A_Multi_Agent_Framework_for_Turning_NeRF_Papers_into_Code_2603.00805.pdf
- Code：https://github.com/wangqiannudt/nerf-arxiv-daily（code_link_found_not_audited）

#### 子问题：接入 SLAM/机器人闭环系统（4）
##### 解法族：SLAM / pose graph / online mapping pipeline（4；另有 1 篇见 full/csv）
###### FeatureSLAM ｜ 2601.05738
- Paper：FeatureSLAM: Feature-enriched 3D gaussian splatting SLAM in real time
- 一句话：FeatureSLAM 针对「接入 SLAM/机器人闭环系统」，从「表示/几何角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2601.05738](method_figures/2601.05738_FeatureSLAM.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_FeatureSLAM_Feature_enriched_3D_gaussian_splatting_SLAM_in_real_time_2601.05738.pdf
###### PointSLAM++ ｜ 2601.11617
- Paper：PointSLAM++: Robust Dense Neural Gaussian Point Cloud-based SLAM
- 一句话：PointSLAM++ 针对「接入 SLAM/机器人闭环系统」，从「表示/几何角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2601.11617](method_figures/2601.11617_PointSLAM.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_PointSLAM_Robust_Dense_Neural_Gaussian_Point_Cloud_based_SLAM_2601.11617.pdf
###### RGS-SLAM ｜ 2601.00705
- Paper：RGS-SLAM: Robust Gaussian Splatting SLAM with One-Shot Dense Initialization
- 一句话：RGS-SLAM 针对「接入 SLAM/机器人闭环系统」，从「表示/几何角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2601.00705](method_figures/2601.00705_RGS-SLAM.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_RGS_SLAM_Robust_Gaussian_Splatting_SLAM_with_One_Shot_Dense_Initialization_2601.00705.pdf
- Code：https://github.com/Breeze1124/RGS-SLAM（code_link_found_not_audited）

#### 子问题：提升几何一致性/表面质量（10）
##### 解法族：Gaussian Splatting 表示与正则化（6；另有 3 篇见 full/csv）
###### CaricatureGS ｜ 2601.03319
- Paper：CaricatureGS: Exaggerating 3D Gaussian Splatting Faces With Gaussian Curvature
- 一句话：CaricatureGS 针对「提升几何一致性/表面质量」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2601.03319](method_figures/2601.03319_CaricatureGS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_CaricatureGS_Exaggerating_3D_Gaussian_Splatting_Faces_With_Gaussian_Curvature_2601.03319.pdf
- Code：https://github.com/eldad929/caricatureGS（code_link_found_not_audited）
###### Instant Colorization of Gaussian Splats ｜ 2604.17155
- Paper：Instant Colorization of Gaussian Splats
- 一句话：Instant Colorization of Gaussian Splats 针对「提升几何一致性/表面质量」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2604.17155](method_figures/2604.17155_Instant_Colorization_of_Gaussian_Splats.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Instant_Colorization_of_Gaussian_Splats_2604.17155.pdf
- Code：https://github.com/dlieber01/Instant-Colorization-of-Gaussian-Splats（code_link_found_not_audited）
###### ProFuse ｜ 2601.04754
- Paper：ProFuse: Efficient Cross-View Context Fusion for Open-Vocabulary 3D Gaussian Splatting
- 一句话：ProFuse 针对「提升几何一致性/表面质量」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2601.04754](method_figures/2601.04754_ProFuse.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_ProFuse_Efficient_Cross_View_Context_Fusion_for_Open_Vocabulary_3D_Gaussian_Splatting_2601.04754.pdf
- Code：https://github.com/chiou1203/ProFuse（code_link_found_not_audited）

##### 解法族：SDF/隐式表面/网格/点云（2）
###### 本文方法 ｜ 2602.14493
- Paper：Gaussian Mesh Renderer for Lightweight Differentiable Rendering
- 一句话：本文方法 针对「提升几何一致性/表面质量」，从「表示/几何角度」切入，主要采用「SDF/隐式表面/网格/点云」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2602.14493](method_figures/2602.14493_paper.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Gaussian_Mesh_Renderer_for_Lightweight_Differentiable_Rendering_2602.14493.pdf
- Code：https://github.com/huntorochi/Gaussian-Mesh-Renderer（code_link_found_not_audited）
###### PolGS++ ｜ 2603.10801
- Paper：PolGS++: Physically-Guided Polarimetric Gaussian Splatting for Fast Reflective Surface Reconstruction
- 一句话：PolGS++ 针对「提升几何一致性/表面质量」，从「表示/几何角度」切入，主要采用「SDF/隐式表面/网格/点云」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2603.10801](method_figures/2603.10801_PolGS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_PolGS_Physically_Guided_Polarimetric_Gaussian_Splatting_for_Fast_Reflective_Surface_Recons_2603.10801.pdf
- Code：https://github.com/PRIS-CV/PolGS_plus（code_link_found_not_audited）

##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### Real-Time ｜ 2601.13574
- Paper：Highly Deformable Proprioceptive Membrane for Real-Time 3D Shape Reconstruction
- 一句话：Real-Time 针对「提升几何一致性/表面质量」，从「表示/几何角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2601.13574](method_figures/2601.13574_Real-Time.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Highly_Deformable_Proprioceptive_Membrane_for_Real_Time_3D_Shape_Reconstruction_2601.13574.pdf

##### 解法族：Sensor/domain-specific pipeline（1）
###### NLiPsCalib ｜ 2603.09319
- Paper：NLiPsCalib: An Efficient Calibration Framework for High-Fidelity 3D Reconstruction of Curved Visuotactile Sensors
- 一句话：NLiPsCalib 针对「提升几何一致性/表面质量」，从「表示/几何角度」切入，主要采用「Sensor/domain-specific pipeline」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2603.09319](method_figures/2603.09319_NLiPsCalib.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_NLiPsCalib_An_Efficient_Calibration_Framework_for_High_Fidelity_3D_Reconstruction_of_Curve_2603.09319.pdf
- Code：https://github.com/FerryRain/NLiPs（code_link_found_not_audited）

#### 子问题：提升可控生成/世界演化预测（1）
##### 解法族：Motion decomposition / canonical space / deformation（1）
###### GS-Surrogate ｜ 2604.06358
- Paper：GS-Surrogate: Deformable Gaussian Splatting for Parameter Space Exploration of Ensemble Simulations
- 一句话：GS-Surrogate 针对「提升可控生成/世界演化预测」，从「表示/几何角度」切入，主要采用「Motion decomposition / canonical space / deformation」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2604.06358](method_figures/2604.06358_GS-Surrogate.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_GS_Surrogate_Deformable_Gaussian_Splatting_for_Parameter_Space_Exploration_of_Ensemble_Sim_2604.06358.pdf

#### 子问题：解决稀疏视角几何不稳定（6）
##### 解法族：Gaussian Splatting 表示与正则化（3）
###### AdaGScale ｜ 2604.18980
- Paper：AdaGScale: Viewpoint-Adaptive Gaussian Scaling in 3D Gaussian Splatting to Reduce Gaussian-Tile Pairs
- 一句话：AdaGScale 针对「解决稀疏视角几何不稳定」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2604.18980](method_figures/2604.18980_AdaGScale.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_AdaGScale_Viewpoint_Adaptive_Gaussian_Scaling_in_3D_Gaussian_Splatting_to_Reduce_Gaussian_2604.18980.pdf
###### GloSplat ｜ 2603.04847
- Paper：GloSplat: Joint Pose-Appearance Optimization for Faster and More Accurate 3D Reconstruction
- 一句话：GloSplat 针对「解决稀疏视角几何不稳定」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2603.04847](method_figures/2603.04847_GloSplat.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_GloSplat_Joint_Pose_Appearance_Optimization_for_Faster_and_More_Accurate_3D_Reconstruction_2603.04847.pdf
###### 本文方法 ｜ 2603.29185
- Paper：Hierarchical Visual Relocalization with Nearest View Synthesis from Feature Gaussian Splatting
- 一句话：本文方法 针对「解决稀疏视角几何不稳定」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2603.29185](method_figures/2603.29185_paper.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Hierarchical_Visual_Relocalization_with_Nearest_View_Synthesis_from_Feature_Gaussian_Splat_2603.29185.pdf
- Code：https://github.com/HqiTao/SplatHLoc（code_link_found_not_audited）

##### 解法族：NeRF/辐射场/体渲染（1）
###### Augmented Radiance Field ｜ 2602.19916
- Paper：Augmented Radiance Field: A General Framework for Enhanced Gaussian Splatting
- 一句话：Augmented Radiance Field 针对「解决稀疏视角几何不稳定」，从「表示/几何角度」切入，主要采用「NeRF/辐射场/体渲染」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2602.19916](method_figures/2602.19916_Augmented_Radiance_Field.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Augmented_Radiance_Field_A_General_Framework_for_Enhanced_Gaussian_Splatting_2602.19916.pdf

##### 解法族：SLAM / pose graph / online mapping pipeline（2）
###### GSO-SLAM ｜ 2602.11714
- Paper：GSO-SLAM: Bidirectionally Coupled Gaussian Splatting and Direct Visual Odometry
- 一句话：GSO-SLAM 针对「解决稀疏视角几何不稳定」，从「表示/几何角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2602.11714](method_figures/2602.11714_GSO-SLAM.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_GSO_SLAM_Bidirectionally_Coupled_Gaussian_Splatting_and_Direct_Visual_Odometry_2602.11714.pdf
- Code：https://github.com/Lab-of-AI-and-Robotics/GSO-SLAM（code_link_found_not_audited）
###### GeGS-PCR ｜ 2604.17721
- Paper：GeGS-PCR: Effective and Robust 3D Point Cloud Registration with Two-Stage Color-Enhanced Geometric-3DGS Fusion
- 一句话：GeGS-PCR 针对「解决稀疏视角几何不稳定」，从「表示/几何角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2604.17721](method_figures/2604.17721_GeGS-PCR.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_GeGS_PCR_Effective_and_Robust_3D_Point_Cloud_Registration_with_Two_Stage_Color_Enhanced_Ge_2604.17721.pdf

#### 子问题：降低显存/存储/模型体积（10）
##### 解法族：Feed-forward / Transformer / Foundation Model（1）
###### UniQueR ｜ 2603.22851
- Paper：UniQueR: Unified Query-based Feedforward 3D Reconstruction
- 一句话：UniQueR 针对「降低显存/存储/模型体积」，从「表示/几何角度」切入，主要采用「Feed-forward / Transformer / Foundation Model」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2603.22851](method_figures/2603.22851_UniQueR.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_UniQueR_Unified_Query_based_Feedforward_3D_Reconstruction_2603.22851.pdf

##### 解法族：Gaussian Splatting 表示与正则化（4；另有 1 篇见 full/csv）
###### Drop-In ｜ 2603.23297
- Paper：Drop-In Perceptual Optimization for 3D Gaussian Splatting
- 一句话：Drop-In 针对「降低显存/存储/模型体积」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2603.23297](method_figures/2603.23297_Drop-In.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Drop_In_Perceptual_Optimization_for_3D_Gaussian_Splatting_2603.23297.pdf
- Code：https://github.com/apple/ml-perceptual-3dgs（code_link_found_not_audited）
###### MSGS ｜ 2604.13340
- Paper：MSGS: Multispectral 3D Gaussian Splatting
- 一句话：MSGS 针对「降低显存/存储/模型体积」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2604.13340](method_figures/2604.13340_MSGS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_MSGS_Multispectral_3D_Gaussian_Splatting_2604.13340.pdf
###### PointSplat ｜ 2604.09903
- Paper：PointSplat: Efficient Geometry-Driven Pruning and Transformer Refinement for 3D Gaussian Splatting
- 一句话：PointSplat 针对「降低显存/存储/模型体积」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2604.09903](method_figures/2604.09903_PointSplat.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_PointSplat_Efficient_Geometry_Driven_Pruning_and_Transformer_Refinement_for_3D_Gaussian_Sp_2604.09903.pdf
- Code：https://github.com/anhthuan1999/pointsplat（code_link_found_not_audited）

##### 解法族：Pruning / compression / progressive coding（3）
###### EntON ｜ 2603.06216
- Paper：EntON: Eigenentropy-Optimized Neighborhood Densification in 3D Gaussian Splatting
- 一句话：EntON 针对「降低显存/存储/模型体积」，从「表示/几何角度」切入，主要采用「Pruning / compression / progressive coding」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2603.06216](method_figures/2603.06216_EntON.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_EntON_Eigenentropy_Optimized_Neighborhood_Densification_in_3D_Gaussian_Splatting_2603.06216.pdf
- Code：https://github.com/hbb1/2d-gaussian-splatting（code_link_found_not_audited）
###### GS4City ｜ 2604.11401
- Paper：GS4City: Hierarchical Semantic Gaussian Splatting via City-Model Priors
- 一句话：GS4City 针对「降低显存/存储/模型体积」，从「表示/几何角度」切入，主要采用「Pruning / compression / progressive coding」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2604.11401](method_figures/2604.11401_GS4City.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_GS4City_Hierarchical_Semantic_Gaussian_Splatting_via_City_Model_Priors_2604.11401.pdf
- Code：https://github.com/Jinyzzz/GS4City（code_link_found_not_audited）
###### QuantumGS ｜ 2602.05047
- Paper：QuantumGS: Quantum Encoding Framework for Gaussian Splatting
- 一句话：QuantumGS 针对「降低显存/存储/模型体积」，从「表示/几何角度」切入，主要采用「Pruning / compression / progressive coding」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2602.05047](method_figures/2602.05047_QuantumGS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_QuantumGS_Quantum_Encoding_Framework_for_Gaussian_Splatting_2602.05047.pdf
- Code：https://github.com/gwilczynski95/QuantumGS（code_link_found_not_audited）

##### 解法族：SLAM / pose graph / online mapping pipeline（2）
###### 本文方法 ｜ 2601.02339
- Paper：Joint Semantic and Rendering Enhancements in 3D Gaussian Modeling with Anisotropic Local Encoding
- 一句话：本文方法 针对「降低显存/存储/模型体积」，从「表示/几何角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2601.02339](method_figures/2601.02339_paper.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Joint_Semantic_and_Rendering_Enhancements_in_3D_Gaussian_Modeling_with_Anisotropic_Local_E_2601.02339.pdf
###### OT-UVGS ｜ 2604.19127
- Paper：OT-UVGS: Revisiting UV Mapping for Gaussian Splatting as a Capacity Allocation Problem
- 一句话：OT-UVGS 针对「降低显存/存储/模型体积」，从「表示/几何角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2604.19127](method_figures/2604.19127_OT-UVGS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_OT_UVGS_Revisiting_UV_Mapping_for_Gaussian_Splatting_as_a_Capacity_Allocation_Problem_2604.19127.pdf

### 切入点：计算角度（45）
#### 子问题：减少优化/采样/渲染步骤（23）
##### 解法族：Feed-forward / Transformer / Foundation Model（4；另有 1 篇见 full/csv）
###### Grounding Image Matching in 3D with MASt3R ｜ 2406.09756
- Paper：Grounding Image Matching in 3D with MASt3R
- 一句话：Grounding Image Matching in 3D with MASt3R 针对「减少优化/采样/渲染步骤」，从「计算角度」切入，主要采用「Feed-forward / Transformer / Foundation Model」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2406.09756](method_figures/2406.09756_Grounding_Image_Matching_in_3D_with_MASt3R.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2024_Grounding_Image_Matching_in_3D_with_MASt3R_2406.09756.pdf
- Code：https://github.com/naver/mast3r（code_link_found_not_audited）
###### Efficient-LVSM ｜ 2602.06478
- Paper：Efficient-LVSM: Faster, Cheaper, and Better Large View Synthesis Model via Decoupled Co-Refinement Attention
- 一句话：Efficient-LVSM 针对「减少优化/采样/渲染步骤」，从「计算角度」切入，主要采用「Feed-forward / Transformer / Foundation Model」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2602.06478](method_figures/2602.06478_Efficient-LVSM.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Efficient_LVSM_Faster_Cheaper_and_Better_Large_View_Synthesis_Model_via_Decoupled_Co_Refin_2602.06478.pdf
- Code：https://github.com/Ayakaee/Efficient-LVSM（code_link_found_not_audited）
###### S-VGGT ｜ 2603.17625
- Paper：S-VGGT: Structure-Aware Subscene Decomposition for Scalable 3D Foundation Models
- 一句话：S-VGGT 针对「减少优化/采样/渲染步骤」，从「计算角度」切入，主要采用「Feed-forward / Transformer / Foundation Model」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2603.17625](method_figures/2603.17625_S-VGGT.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_S_VGGT_Structure_Aware_Subscene_Decomposition_for_Scalable_3D_Foundation_Models_2603.17625.pdf
- Code：https://github.com/Powertony102/S-VGGT（code_link_found_not_audited）

##### 解法族：Gaussian Splatting 表示与正则化（8；另有 5 篇见 full/csv）
###### Real-Time ｜ 2308.04079
- Paper：3D Gaussian Splatting for Real-Time Radiance Field Rendering
- 一句话：Real-Time 针对「减少优化/采样/渲染步骤」，从「计算角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2308.04079](method_figures/2308.04079_Real-Time.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2023_3D_Gaussian_Splatting_for_Real_Time_Radiance_Field_Rendering_2308.04079.pdf
###### 本文方法 ｜ 2603.17227
- Paper：Adaptive Anchor Policies for Efficient 4D Gaussian Streaming
- 一句话：本文方法 针对「减少优化/采样/渲染步骤」，从「计算角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2603.17227](method_figures/2603.17227_paper.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Adaptive_Anchor_Policies_for_Efficient_4D_Gaussian_Streaming_2603.17227.pdf
###### AdvSplat ｜ 2603.23686
- Paper：AdvSplat: Adversarial Attacks on Feed-Forward Gaussian Splatting Models
- 一句话：AdvSplat 针对「减少优化/采样/渲染步骤」，从「计算角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2603.23686](method_figures/2603.23686_AdvSplat.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_AdvSplat_Adversarial_Attacks_on_Feed_Forward_Gaussian_Splatting_Models_2603.23686.pdf

##### 解法族：Motion decomposition / canonical space / deformation（1）
###### Fast and Robust Deformable 3D Gaussian Splatting ｜ 2603.20857
- Paper：Fast and Robust Deformable 3D Gaussian Splatting
- 一句话：Fast and Robust Deformable 3D Gaussian Splatting 针对「减少优化/采样/渲染步骤」，从「计算角度」切入，主要采用「Motion decomposition / canonical space / deformation」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2603.20857](method_figures/2603.20857_Fast_and_Robust_Deformable_3D_Gaussian_Splatting.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Fast_and_Robust_Deformable_3D_Gaussian_Splatting_2603.20857.pdf

##### 解法族：NeRF/辐射场/体渲染（1）
###### Few TensoRF ｜ 2603.25008
- Paper：Few TensoRF: Enhance the Few-shot on Tensorial Radiance Fields
- 一句话：Few TensoRF 针对「减少优化/采样/渲染步骤」，从「计算角度」切入，主要采用「NeRF/辐射场/体渲染」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2603.25008](method_figures/2603.25008_Few_TensoRF.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Few_TensoRF_Enhance_the_Few_shot_on_Tensorial_Radiance_Fields_2603.25008.pdf
- Code：https://github.com/ytrock/THuman2.0-Dataset（code_link_found_not_audited）

##### 解法族：SDF/隐式表面/网格/点云（2）
###### Fast-HaMeR ｜ 2603.16444
- Paper：Fast-HaMeR: Boosting Hand Mesh Reconstruction using Knowledge Distillation
- 一句话：Fast-HaMeR 针对「减少优化/采样/渲染步骤」，从「计算角度」切入，主要采用「SDF/隐式表面/网格/点云」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2603.16444](method_figures/2603.16444_Fast-HaMeR.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Fast_HaMeR_Boosting_Hand_Mesh_Reconstruction_using_Knowledge_Distillation_2603.16444.pdf
- Code：https://github.com/hunainahmedj/Fast-HaMeR（code_link_found_not_audited）
###### Non-Invasive ｜ 2601.19014
- Paper：Non-Invasive 3D Wound Measurement with RGB-D Imaging
- 一句话：Non-Invasive 针对「减少优化/采样/渲染步骤」，从「计算角度」切入，主要采用「SDF/隐式表面/网格/点云」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2601.19014](method_figures/2601.19014_Non-Invasive.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Non_Invasive_3D_Wound_Measurement_with_RGB_D_Imaging_2601.19014.pdf

##### 解法族：SLAM / pose graph / online mapping pipeline（6；另有 3 篇见 full/csv）
###### MVSNet ｜ 1804.02505
- Paper：MVSNet: Depth Inference for Unstructured Multi-view Stereo
- 一句话：MVSNet 针对「减少优化/采样/渲染步骤」，从「计算角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![1804.02505](method_figures/1804.02505_MVSNet.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2018_MVSNet_Depth_Inference_for_Unstructured_Multi_view_Stereo_1804.02505.pdf
- Code：https://github.com/openMVG/openMVG（code_link_found_not_audited）
###### Flash-Mono ｜ 2604.03092
- Paper：Flash-Mono: Feed-Forward Accelerated Gaussian Splatting Monocular SLAM
- 一句话：Flash-Mono 针对「减少优化/采样/渲染步骤」，从「计算角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2604.03092](method_figures/2604.03092_Flash-Mono.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Flash_Mono_Feed_Forward_Accelerated_Gaussian_Splatting_Monocular_SLAM_2604.03092.pdf
- Code：https://github.com/eliahuhorwitz/Academic-project-page-template（code_link_found_not_audited）
###### GaussianCaR ｜ 2602.08784
- Paper：GaussianCaR: Gaussian Splatting for Efficient Camera-Radar Fusion
- 一句话：GaussianCaR 针对「减少优化/采样/渲染步骤」，从「计算角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2602.08784](method_figures/2602.08784_GaussianCaR.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_GaussianCaR_Gaussian_Splatting_for_Efficient_Camera_Radar_Fusion_2602.08784.pdf
- Code：https://www.github.com/santimontiel/gaussiancar（code_link_found_not_audited）

##### 解法族：Sensor/domain-specific pipeline（1）
###### Grasp, Slide, Roll ｜ 2602.23206
- Paper：Grasp, Slide, Roll: Comparative Analysis of Contact Modes for Tactile-Based Shape Reconstruction
- 一句话：Grasp, Slide, Roll 针对「减少优化/采样/渲染步骤」，从「计算角度」切入，主要采用「Sensor/domain-specific pipeline」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2602.23206](method_figures/2602.23206_Grasp_Slide_Roll.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Grasp_Slide_Roll_Comparative_Analysis_of_Contact_Modes_for_Tactile_Based_Shape_Reconstruct_2602.23206.pdf

#### 子问题：建模运动/形变/时间一致性（5）
##### 解法族：Feed-forward / Transformer / Foundation Model（2）
###### FastGHA ｜ 2601.13837
- Paper：FastGHA: Generalized Few-Shot 3D Gaussian Head Avatars with Real-Time Animation
- 一句话：FastGHA 针对「建模运动/形变/时间一致性」，从「计算角度」切入，主要采用「Feed-forward / Transformer / Foundation Model」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2601.13837](method_figures/2601.13837_FastGHA.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_FastGHA_Generalized_Few_Shot_3D_Gaussian_Head_Avatars_with_Real_Time_Animation_2601.13837.pdf
###### LiveStre4m ｜ 2604.06740
- Paper：LiveStre4m: Feed-Forward Live Streaming of Novel Views from Unposed Multi-View Video
- 一句话：LiveStre4m 针对「建模运动/形变/时间一致性」，从「计算角度」切入，主要采用「Feed-forward / Transformer / Foundation Model」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2604.06740](method_figures/2604.06740_LiveStre4m.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_LiveStre4m_Feed_Forward_Live_Streaming_of_Novel_Views_from_Unposed_Multi_View_Video_2604.06740.pdf
- Code：https://github.com/pedro-quesado/LiveStre4m（code_link_found_not_audited）

##### 解法族：SLAM / pose graph / online mapping pipeline（3）
###### FastLoop ｜ 2603.17201
- Paper：FastLoop: Parallel Loop Closing with GPU-Acceleration in Visual SLAM
- 一句话：FastLoop 针对「建模运动/形变/时间一致性」，从「计算角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2603.17201](method_figures/2603.17201_FastLoop.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_FastLoop_Parallel_Loop_Closing_with_GPU_Acceleration_in_Visual_SLAM_2603.17201.pdf
- Code：https://github.com/sfu-rsl/FastLoop（code_link_found_not_audited）
###### MoRGS ｜ 2603.25042
- Paper：MoRGS: Efficient Per-Gaussian Motion Reasoning for Streamable Dynamic 3D Scenes
- 一句话：MoRGS 针对「建模运动/形变/时间一致性」，从「计算角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2603.25042](method_figures/2603.25042_MoRGS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_MoRGS_Efficient_Per_Gaussian_Motion_Reasoning_for_Streamable_Dynamic_3D_Scenes_2603.25042.pdf
###### Ultra-Fast ｜ 2602.07860
- Paper：Recovering 3D Shapes from Ultra-Fast Motion-Blurred Images
- 一句话：Ultra-Fast 针对「建模运动/形变/时间一致性」，从「计算角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2602.07860](method_figures/2602.07860_Ultra-Fast.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Recovering_3D_Shapes_from_Ultra_Fast_Motion_Blurred_Images_2602.07860.pdf
- Code：https://github.com/Maxmilite/rec-from-ultrafast-blur（code_link_found_not_audited）

#### 子问题：接入 SLAM/机器人闭环系统（5）
##### 解法族：SLAM / pose graph / online mapping pipeline（5；另有 2 篇见 full/csv）
###### 本文方法 ｜ 2603.20077
- Paper：A Unified Platform and Quality Assurance Framework for 3D Ultrasound Reconstruction with Robotic, Optical, and Electromagnetic Tracking
- 一句话：本文方法 针对「接入 SLAM/机器人闭环系统」，从「计算角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2603.20077](method_figures/2603.20077_paper.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_A_Unified_Platform_and_Quality_Assurance_Framework_for_3D_Ultrasound_Reconstruction_with_R_2603.20077.pdf
###### 本文方法 ｜ 2601.12122
- Paper：Active Semantic Mapping of Horticultural Environments Using Gaussian Splatting
- 一句话：本文方法 针对「接入 SLAM/机器人闭环系统」，从「计算角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2601.12122](method_figures/2601.12122_paper.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Active_Semantic_Mapping_of_Horticultural_Environments_Using_Gaussian_Splatting_2601.12122.pdf
###### Keyframe-Optimized ｜ 2604.00804
- Paper：Compact Keyframe-Optimized Multi-Agent Gaussian Splatting SLAM
- 一句话：Keyframe-Optimized 针对「接入 SLAM/机器人闭环系统」，从「计算角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2604.00804](method_figures/2604.00804_Keyframe-Optimized.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Compact_Keyframe_Optimized_Multi_Agent_Gaussian_Splatting_SLAM_2604.00804.pdf
- Code：https://github.com/lemonci/coko-slam（code_link_found_not_audited）

#### 子问题：提升几何一致性/表面质量（1）
##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### RayMap3R ｜ 2603.20588
- Paper：RayMap3R: Inference-Time RayMap for Dynamic 3D Reconstruction
- 一句话：RayMap3R 针对「提升几何一致性/表面质量」，从「计算角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2603.20588](method_figures/2603.20588_RayMap3R.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_RayMap3R_Inference_Time_RayMap_for_Dynamic_3D_Reconstruction_2603.20588.pdf
- Code：https://github.com/Brack-Wang/raymap3r（code_link_found_not_audited）

#### 子问题：提升可控生成/世界演化预测（1）
##### 解法族：Feed-forward / Transformer / Foundation Model（1）
###### UrbanVGGT ｜ 2603.22531
- Paper：UrbanVGGT: Scalable Sidewalk Width Estimation from Street View Images
- 一句话：UrbanVGGT 针对「提升可控生成/世界演化预测」，从「计算角度」切入，主要采用「Feed-forward / Transformer / Foundation Model」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2603.22531](method_figures/2603.22531_UrbanVGGT.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_UrbanVGGT_Scalable_Sidewalk_Width_Estimation_from_Street_View_Images_2603.22531.pdf

#### 子问题：解决稀疏视角几何不稳定（4）
##### 解法族：Feed-forward / Transformer / Foundation Model（1）
###### RnG ｜ 2603.01194
- Paper：RnG: A Unified Transformer for Complete 3D Modeling from Partial Observations
- 一句话：RnG 针对「解决稀疏视角几何不稳定」，从「计算角度」切入，主要采用「Feed-forward / Transformer / Foundation Model」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2603.01194](method_figures/2603.01194_RnG.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_RnG_A_Unified_Transformer_for_Complete_3D_Modeling_from_Partial_Observations_2603.01194.pdf
- Code：https://github.com/XiangMochu/RnG（code_link_found_not_audited）

##### 解法族：Gaussian Splatting 表示与正则化（2）
###### Graphical X Splatting (GraphiXS) ｜ 2601.19843
- Paper：Graphical X Splatting (GraphiXS): A Graphical Model for 4D Gaussian Splatting under Uncertainty
- 一句话：Graphical X Splatting (GraphiXS) 针对「解决稀疏视角几何不稳定」，从「计算角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2601.19843](method_figures/2601.19843_Graphical_X_Splatting_GraphiXS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Graphical_X_Splatting_GraphiXS_A_Graphical_Model_for_4D_Gaussian_Splatting_under_Uncertain_2601.19843.pdf
- Code：https://github.com/dendenxu/fast-gaussian-rasterization（code_link_found_not_audited）
###### PLANING ｜ 2601.22046
- Paper：PLANING: A Loosely Coupled Triangle-Gaussian Framework for Streaming 3D Reconstruction
- 一句话：PLANING 针对「解决稀疏视角几何不稳定」，从「计算角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2601.22046](method_figures/2601.22046_PLANING.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_PLANING_A_Loosely_Coupled_Triangle_Gaussian_Framework_for_Streaming_3D_Reconstruction_2601.22046.pdf
- Code：https://github.com/InternRobotics/PLANING（code_link_found_not_audited）

##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### 3DGS$^2$-TR ｜ 2602.00395
- Paper：3DGS$^2$-TR: Scalable Second-Order Trust-Region Method for 3D Gaussian Splatting
- 一句话：3DGS$^2$-TR 针对「解决稀疏视角几何不稳定」，从「计算角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2602.00395](method_figures/2602.00395_3DGS_2_-TR.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_3DGS_2_TR_Scalable_Second_Order_Trust_Region_Method_for_3D_Gaussian_Splatting_2602.00395.pdf

#### 子问题：降低显存/存储/模型体积（6）
##### 解法族：Feed-forward / Transformer / Foundation Model（1）
###### Speed3R ｜ 2603.08055
- Paper：Speed3R: Sparse Feed-forward 3D Reconstruction Models
- 一句话：Speed3R 针对「降低显存/存储/模型体积」，从「计算角度」切入，主要采用「Feed-forward / Transformer / Foundation Model」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2603.08055](method_figures/2603.08055_Speed3R.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Speed3R_Sparse_Feed_forward_3D_Reconstruction_Models_2603.08055.pdf
- Code：https://github.com/Visual-AI/speed3r（code_link_found_not_audited）

##### 解法族：Pruning / compression / progressive coding（1）
###### GlobalSplat ｜ 2604.15284
- Paper：GlobalSplat: Efficient Feed-Forward 3D Gaussian Splatting via Global Scene Tokens
- 一句话：GlobalSplat 针对「降低显存/存储/模型体积」，从「计算角度」切入，主要采用「Pruning / compression / progressive coding」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2604.15284](method_figures/2604.15284_GlobalSplat.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_GlobalSplat_Efficient_Feed_Forward_3D_Gaussian_Splatting_via_Global_Scene_Tokens_2604.15284.pdf

##### 解法族：SLAM / pose graph / online mapping pipeline（4；另有 1 篇见 full/csv）
###### EmbodiedSplat ｜ 2603.04254
- Paper：EmbodiedSplat: Online Feed-Forward Semantic 3DGS for Open-Vocabulary 3D Scene Understanding
- 一句话：EmbodiedSplat 针对「降低显存/存储/模型体积」，从「计算角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2603.04254](method_figures/2603.04254_EmbodiedSplat.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_EmbodiedSplat_Online_Feed_Forward_Semantic_3DGS_for_Open_Vocabulary_3D_Scene_Understanding_2603.04254.pdf
- Code：https://github.com/0nandon/EmbodiedSplat（code_link_found_not_audited）
###### 本文方法 ｜ 2604.14141
- Paper：Geometric Context Transformer for Streaming 3D Reconstruction
- 一句话：本文方法 针对「降低显存/存储/模型体积」，从「计算角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2604.14141](method_figures/2604.14141_paper.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Geometric_Context_Transformer_for_Streaming_3D_Reconstruction_2604.14141.pdf
- Code：https://github.com/robbyant/lingbot-map（code_link_found_not_audited）
###### MeMix ｜ 2603.15330
- Paper：MeMix: Writing Less, Remembering More for Streaming 3D Reconstruction
- 一句话：MeMix 针对「降低显存/存储/模型体积」，从「计算角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2603.15330](method_figures/2603.15330_MeMix.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_MeMix_Writing_Less_Remembering_More_for_Streaming_3D_Reconstruction_2603.15330.pdf
- Code：https://github.com/Hopding/pdf-lib（code_link_found_not_audited）

### 切入点：训练/监督角度（33）
#### 子问题：减少优化/采样/渲染步骤（2）
##### 解法族：Gaussian Splatting 表示与正则化（2）
###### DirectFisheye-GS ｜ 2604.00648
- Paper：DirectFisheye-GS: Enabling Native Fisheye Input in Gaussian Splatting with Cross-View Joint Optimization
- 一句话：DirectFisheye-GS 针对「减少优化/采样/渲染步骤」，从「训练/监督角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2604.00648](method_figures/2604.00648_DirectFisheye-GS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_DirectFisheye_GS_Enabling_Native_Fisheye_Input_in_Gaussian_Splatting_with_Cross_View_Joint_2604.00648.pdf
###### Faster-GS ｜ 2602.09999
- Paper：Faster-GS: Analyzing and Improving Gaussian Splatting Optimization
- 一句话：Faster-GS 针对「减少优化/采样/渲染步骤」，从「训练/监督角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2602.09999](method_figures/2602.09999_Faster-GS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Faster_GS_Analyzing_and_Improving_Gaussian_Splatting_Optimization_2602.09999.pdf
- Code：https://github.com/nerficg-project/faster-gaussian-splatting（code_link_found_not_audited）

#### 子问题：建模运动/形变/时间一致性（4）
##### 解法族：Motion decomposition / canonical space / deformation（1）
###### GHOST ｜ 2603.20583
- Paper：GHOST: Ground-projected Hypotheses from Observed Structure-from-Motion Trajectories
- 一句话：GHOST 针对「建模运动/形变/时间一致性」，从「训练/监督角度」切入，主要采用「Motion decomposition / canonical space / deformation」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2603.20583](method_figures/2603.20583_GHOST.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_GHOST_Ground_projected_Hypotheses_from_Observed_Structure_from_Motion_Trajectories_2603.20583.pdf
- Code：https://github.com/ceres-solver/ceres-solver（code_link_found_not_audited）

##### 解法族：NeRF/辐射场/体渲染（2）
###### HexPlane ｜ 2301.09632
- Paper：HexPlane: A Fast Representation for Dynamic Scenes
- 一句话：HexPlane 针对「建模运动/形变/时间一致性」，从「训练/监督角度」切入，主要采用「NeRF/辐射场/体渲染」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2301.09632](method_figures/2301.09632_HexPlane.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2023_HexPlane_A_Fast_Representation_for_Dynamic_Scenes_2301.09632.pdf
- Code：https://github.com/Caoang327/HexPlane（code_link_found_not_audited）
###### IDDR-NGP ｜ 2601.11030
- Paper：IDDR-NGP: Incorporating Detectors for Distractor Removal with Instant Neural Radiance Field
- 一句话：IDDR-NGP 针对「建模运动/形变/时间一致性」，从「训练/监督角度」切入，主要采用「NeRF/辐射场/体渲染」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2601.11030](method_figures/2601.11030_IDDR-NGP.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_IDDR_NGP_Incorporating_Detectors_for_Distractor_Removal_with_Instant_Neural_Radiance_Field_2601.11030.pdf

##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### InHabit ｜ 2604.19673
- Paper：InHabit: Leveraging Image Foundation Models for Scalable 3D Human Placement
- 一句话：InHabit 针对「建模运动/形变/时间一致性」，从「训练/监督角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2604.19673](method_figures/2604.19673_InHabit.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_InHabit_Leveraging_Image_Foundation_Models_for_Scalable_3D_Human_Placement_2604.19673.pdf
- Code：https://github.com/pradyumnaym/graft（code_link_found_not_audited）

#### 子问题：接入 SLAM/机器人闭环系统（1）
##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### NICE-SLAM ｜ 2112.12130
- Paper：NICE-SLAM: Neural Implicit Scalable Encoding for SLAM
- 一句话：NICE-SLAM 针对「接入 SLAM/机器人闭环系统」，从「训练/监督角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2112.12130](method_figures/2112.12130_NICE-SLAM.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2022_NICE_SLAM_Neural_Implicit_Scalable_Encoding_for_SLAM_2112.12130.pdf
- Code：https://github.com/cvg/nice-slam（code_link_found_not_audited）

#### 子问题：提升几何一致性/表面质量（4）
##### 解法族：Feed-forward / Transformer / Foundation Model（1）
###### Free Geometry ｜ 2604.14048
- Paper：Free Geometry: Refining 3D Reconstruction from Longer Versions of Itself
- 一句话：Free Geometry 针对「提升几何一致性/表面质量」，从「训练/监督角度」切入，主要采用「Feed-forward / Transformer / Foundation Model」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2604.14048](method_figures/2604.14048_Free_Geometry.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Free_Geometry_Refining_3D_Reconstruction_from_Longer_Versions_of_Itself_2604.14048.pdf
- Code：https://github.com/hiteacherIamhumble/Free-Geometry（code_link_found_not_audited）

##### 解法族：Gaussian Splatting 表示与正则化（1）
###### DualSplat ｜ 2604.21631
- Paper：DualSplat: Robust 3D Gaussian Splatting via Pseudo-Mask Bootstrapping from Reconstruction Failures
- 一句话：DualSplat 针对「提升几何一致性/表面质量」，从「训练/监督角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2604.21631](method_figures/2604.21631_DualSplat.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_DualSplat_Robust_3D_Gaussian_Splatting_via_Pseudo_Mask_Bootstrapping_from_Reconstruction_F_2604.21631.pdf
- Code：https://github.com/Lans1ot/DualSplat（code_link_found_not_audited）

##### 解法族：SLAM / pose graph / online mapping pipeline（2）
###### Dual-Domain Representation Alignment ｜ 2603.19563
- Paper：Dual-Domain Representation Alignment: Bridging 2D and 3D Vision via Geometry-Aware Architecture Search
- 一句话：Dual-Domain Representation Alignment 针对「提升几何一致性/表面质量」，从「训练/监督角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2603.19563](method_figures/2603.19563_Dual-Domain_Representation_Alignment.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Dual_Domain_Representation_Alignment_Bridging_2D_and_3D_Vision_via_Geometry_Aware_Architec_2603.19563.pdf
- Code：https://github.com/EMI-Group/evonas（code_link_found_not_audited）
###### Scal3R ｜ 2604.08542
- Paper：Scal3R: Scalable Test-Time Training for Large-Scale 3D Reconstruction
- 一句话：Scal3R 针对「提升几何一致性/表面质量」，从「训练/监督角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2604.08542](method_figures/2604.08542_Scal3R.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Scal3R_Scalable_Test_Time_Training_for_Large_Scale_3D_Reconstruction_2604.08542.pdf

#### 子问题：提升可控生成/世界演化预测（3）
##### 解法族：Diffusion/生成先验/视频模型（1）
###### DreamDojo ｜ 2602.06949
- Paper：DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos
- 一句话：DreamDojo 针对「提升可控生成/世界演化预测」，从「训练/监督角度」切入，主要采用「Diffusion/生成先验/视频模型」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2602.06949](method_figures/2602.06949_DreamDojo.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_DreamDojo_A_Generalist_Robot_World_Model_from_Large_Scale_Human_Videos_2602.06949.pdf
- Code：https://github.com/NVIDIA/DreamDojo（code_link_found_not_audited）

##### 解法族：Motion decomposition / canonical space / deformation（1）
###### Olaf-World ｜ 2602.10104
- Paper：Olaf-World: Orienting Latent Actions for Video World Modeling
- 一句话：Olaf-World 针对「提升可控生成/世界演化预测」，从「训练/监督角度」切入，主要采用「Motion decomposition / canonical space / deformation」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2602.10104](method_figures/2602.10104_Olaf-World.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Olaf_World_Orienting_Latent_Actions_for_Video_World_Modeling_2602.10104.pdf
- Code：https://github.com/showlab/Olaf-World（code_link_found_not_audited）

##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### ModTrans ｜ 2604.01607
- Paper：ModTrans: Translating Real-world Models for Distributed Training Simulator
- 一句话：ModTrans 针对「提升可控生成/世界演化预测」，从「训练/监督角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2604.01607](method_figures/2604.01607_ModTrans.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_ModTrans_Translating_Real_world_Models_for_Distributed_Training_Simulator_2604.01607.pdf
- Code：https://github.com/microsoft/onnxconverter-common/blob/master/onnxconverter_common/onnx2py.py（code_link_found_not_audited）

#### 子问题：提升泛化/跨场景/开放世界能力（2）
##### 解法族：Pruning / compression / progressive coding（1）
###### Self-Supervised ｜ 2603.07039
- Paper：Self-Supervised Multi-Modal World Model with 4D Space-Time Embedding
- 一句话：Self-Supervised 针对「提升泛化/跨场景/开放世界能力」，从「训练/监督角度」切入，主要采用「Pruning / compression / progressive coding」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2603.07039](method_figures/2603.07039_Self-Supervised.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Self_Supervised_Multi_Modal_World_Model_with_4D_Space_Time_Embedding_2603.07039.pdf
- Code：https://github.com/legel/deepearth（code_link_found_not_audited）

##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### 本文方法 ｜ 2602.05029
- Paper：Differentiable Inverse Graphics for Zero-shot Scene Reconstruction and Robot Grasping
- 一句话：本文方法 针对「提升泛化/跨场景/开放世界能力」，从「训练/监督角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2602.05029](method_figures/2602.05029_paper.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Differentiable_Inverse_Graphics_for_Zero_shot_Scene_Reconstruction_and_Robot_Grasping_2602.05029.pdf

#### 子问题：解决稀疏视角几何不稳定（9）
##### 解法族：Gaussian Splatting 表示与正则化（4；另有 1 篇见 full/csv）
###### ColorGradedGaussians ｜ 2604.01551
- Paper：ColorGradedGaussians: Palette-Based Color Grading for 3D Gaussian Splatting via View-Space Sparse Decomposition
- 一句话：ColorGradedGaussians 针对「解决稀疏视角几何不稳定」，从「训练/监督角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2604.01551](method_figures/2604.01551_ColorGradedGaussians.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_ColorGradedGaussians_Palette_Based_Color_Grading_for_3D_Gaussian_Splatting_via_View_Space_2604.01551.pdf
###### 本文方法 ｜ 2604.11098
- Paper：Efficient Transceiver Design for Aerial Image Transmission and Large-scale Scene Reconstruction
- 一句话：本文方法 针对「解决稀疏视角几何不稳定」，从「训练/监督角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2604.11098](method_figures/2604.11098_paper.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Efficient_Transceiver_Design_for_Aerial_Image_Transmission_and_Large_scale_Scene_Reconstru_2604.11098.pdf
###### FreeScale ｜ 2604.10512
- Paper：FreeScale: Scaling 3D Scenes via Certainty-Aware Free-View Generation
- 一句话：FreeScale 针对「解决稀疏视角几何不稳定」，从「训练/监督角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2604.10512](method_figures/2604.10512_FreeScale.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_FreeScale_Scaling_3D_Scenes_via_Certainty_Aware_Free_View_Generation_2604.10512.pdf
- Code：https://github.com/mvp-ai-lab/FreeScale（code_link_found_not_audited）

##### 解法族：SLAM / pose graph / online mapping pipeline（5；另有 2 篇见 full/csv）
###### S-MUSt3R ｜ 2602.04517
- Paper：S-MUSt3R: Sliding Multi-view 3D Reconstruction
- 一句话：S-MUSt3R 针对「解决稀疏视角几何不稳定」，从「训练/监督角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2602.04517](method_figures/2602.04517_S-MUSt3R.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_S_MUSt3R_Sliding_Multi_view_3D_Reconstruction_2602.04517.pdf
###### SR3R ｜ 2602.24020
- Paper：SR3R: Rethinking Super-Resolution 3D Reconstruction With Feed-Forward Gaussian Splatting
- 一句话：SR3R 针对「解决稀疏视角几何不稳定」，从「训练/监督角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2602.24020](method_figures/2602.24020_SR3R.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_SR3R_Rethinking_Super_Resolution_3D_Reconstruction_With_Feed_Forward_Gaussian_Splatting_2602.24020.pdf
- Code：https://github.com/eliahuhorwitz/Academic-project-page-template（code_link_found_not_audited）
###### SurgCUT3R ｜ 2603.06971
- Paper：SurgCUT3R: Surgical Scene-Aware Continuous Understanding of Temporal 3D Representation
- 一句话：SurgCUT3R 针对「解决稀疏视角几何不稳定」，从「训练/监督角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2603.06971](method_figures/2603.06971_SurgCUT3R.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_SurgCUT3R_Surgical_Scene_Aware_Continuous_Understanding_of_Temporal_3D_Representation_2603.06971.pdf
- Code：https://github.com/eliahuhorwitz/Academic-project-page-template（code_link_found_not_audited）

#### 子问题：降低显存/存储/模型体积（8）
##### 解法族：Gaussian Splatting 表示与正则化（7；另有 4 篇见 full/csv）
###### DefenseSplat ｜ 2602.19323
- Paper：DefenseSplat: Enhancing the Robustness of 3D Gaussian Splatting via Frequency-Aware Filtering
- 一句话：DefenseSplat 针对「降低显存/存储/模型体积」，从「训练/监督角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2602.19323](method_figures/2602.19323_DefenseSplat.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_DefenseSplat_Enhancing_the_Robustness_of_3D_Gaussian_Splatting_via_Frequency_Aware_Filteri_2602.19323.pdf
###### F4Splat ｜ 2603.21304
- Paper：F4Splat: Feed-Forward Predictive Densification for Feed-Forward 3D Gaussian Splatting
- 一句话：F4Splat 针对「降低显存/存储/模型体积」，从「训练/监督角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2603.21304](method_figures/2603.21304_F4Splat.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_F4Splat_Feed_Forward_Predictive_Densification_for_Feed_Forward_3D_Gaussian_Splatting_2603.21304.pdf
###### LL-GaussianImage ｜ 2601.15772
- Paper：LL-GaussianImage: Efficient Image Representation for Zero-shot Low-Light Enhancement with 2D Gaussian Splatting
- 一句话：LL-GaussianImage 针对「降低显存/存储/模型体积」，从「训练/监督角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2601.15772](method_figures/2601.15772_LL-GaussianImage.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_LL_GaussianImage_Efficient_Image_Representation_for_Zero_shot_Low_Light_Enhancement_with_2_2601.15772.pdf
- Code：https://github.com/YuhanChen2024/LL-GaussianImage（code_link_found_not_audited）

##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### CT ｜ 2602.05884
- Paper：Neural Implicit 3D Cardiac Shape Reconstruction from Sparse CT Angiography Slices Mimicking 2D Transthoracic Echocardiography Views
- 一句话：CT 针对「降低显存/存储/模型体积」，从「训练/监督角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「实时/大规模/高效 3D 表示」。
- Method diagram：![2602.05884](method_figures/2602.05884_CT.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Neural_Implicit_3D_Cardiac_Shape_Reconstruction_from_Sparse_CT_Angiography_Slices_Mimickin_2602.05884.pdf

## Motivation：生成式 3D/4D 内容与仿真（104）
### 切入点：内存/存储角度（1）
#### 子问题：降低显存/存储/模型体积（1）
##### 解法族：Diffusion/生成先验/视频模型（1）
###### AnyRecon ｜ 2604.19747
- Paper：AnyRecon: Arbitrary-View 3D Reconstruction with Video Diffusion Model
- 一句话：AnyRecon 针对「降低显存/存储/模型体积」，从「内存/存储角度」切入，主要采用「Diffusion/生成先验/视频模型」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2604.19747](method_figures/2604.19747_AnyRecon.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_AnyRecon_Arbitrary_View_3D_Reconstruction_with_Video_Diffusion_Model_2604.19747.pdf
- Code：https://github.com/OpenImagingLab/AnyRecon（code_link_found_not_audited）

### 切入点：时空/动态角度（22）
#### 子问题：建模运动/形变/时间一致性（3）
##### 解法族：Diffusion/生成先验/视频模型（1）
###### AnyView ｜ 2601.16982
- Paper：AnyView: Synthesizing Any Novel View in Dynamic Scenes
- 一句话：AnyView 针对「建模运动/形变/时间一致性」，从「时空/动态角度」切入，主要采用「Diffusion/生成先验/视频模型」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2601.16982](method_figures/2601.16982_AnyView.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_AnyView_Synthesizing_Any_Novel_View_in_Dynamic_Scenes_2601.16982.pdf
- Code：https://github.com/TRI-ML/DDAD（code_link_found_not_audited）

##### 解法族：Motion decomposition / canonical space / deformation（1）
###### ActionMesh ｜ 2601.16148
- Paper：ActionMesh: Animated 3D Mesh Generation with Temporal 3D Diffusion
- 一句话：ActionMesh 针对「建模运动/形变/时间一致性」，从「时空/动态角度」切入，主要采用「Motion decomposition / canonical space / deformation」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2601.16148](method_figures/2601.16148_ActionMesh.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_ActionMesh_Animated_3D_Mesh_Generation_with_Temporal_3D_Diffusion_2601.16148.pdf
- Code：https://github.com/facebookresearch/actionmesh（code_link_found_not_audited）

##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### Code2Worlds ｜ 2602.11757
- Paper：Code2Worlds: Empowering Coding LLMs for 4D World Generation
- 一句话：Code2Worlds 针对「建模运动/形变/时间一致性」，从「时空/动态角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2602.11757](method_figures/2602.11757_Code2Worlds.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Code2Worlds_Empowering_Coding_LLMs_for_4D_World_Generation_2602.11757.pdf
- Code：https://github.com/AIGeeksGroup/Code2Worlds（code_link_found_not_audited）

#### 子问题：提升几何一致性/表面质量（2）
##### 解法族：Diffusion/生成先验/视频模型（2）
###### DuoMo ｜ 2603.03265
- Paper：DuoMo: Dual Motion Diffusion for World-Space Human Reconstruction
- 一句话：DuoMo 针对「提升几何一致性/表面质量」，从「时空/动态角度」切入，主要采用「Diffusion/生成先验/视频模型」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2603.03265](method_figures/2603.03265_DuoMo.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_DuoMo_Dual_Motion_Diffusion_for_World_Space_Human_Reconstruction_2603.03265.pdf
- Code：https://github.com/nerfies/nerfies.github.io（code_link_found_not_audited）
###### Geometry-Guided ｜ 2603.27016
- Paper：Generative Shape Reconstruction with Geometry-Guided Langevin Dynamics
- 一句话：Geometry-Guided 针对「提升几何一致性/表面质量」，从「时空/动态角度」切入，主要采用「Diffusion/生成先验/视频模型」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2603.27016](method_figures/2603.27016_Geometry-Guided.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Generative_Shape_Reconstruction_with_Geometry_Guided_Langevin_Dynamics_2603.27016.pdf
- Code：https://github.com/linusnie/gg-langevin（code_link_found_not_audited）

#### 子问题：提升可控生成/世界演化预测（12）
##### 解法族：Diffusion/生成先验/视频模型（10；另有 7 篇见 full/csv）
###### 本文方法 ｜ 2601.17067
- Paper：A Mechanistic View on Video Generation as World Models: State and Dynamics
- 一句话：本文方法 针对「提升可控生成/世界演化预测」，从「时空/动态角度」切入，主要采用「Diffusion/生成先验/视频模型」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2601.17067](method_figures/2601.17067_paper.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_A_Mechanistic_View_on_Video_Generation_as_World_Models_State_and_Dynamics_2601.17067.pdf
- Code：https://github.com/genmoai/mochi（code_link_found_not_audited）
###### EVA ｜ 2603.17808
- Paper：EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards
- 一句话：EVA 针对「提升可控生成/世界演化预测」，从「时空/动态角度」切入，主要采用「Diffusion/生成先验/视频模型」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2603.17808](method_figures/2603.17808_EVA.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_EVA_Aligning_Video_World_Models_with_Executable_Robot_Actions_via_Inverse_Dynamics_Rewards_2603.17808.pdf
- Code：https://github.com/RobbinW/EVA（code_link_found_not_audited）
###### Real-World ｜ 2603.15583
- Paper：Grounding World Simulation Models in a Real-World Metropolis
- 一句话：Real-World 针对「提升可控生成/世界演化预测」，从「时空/动态角度」切入，主要采用「Diffusion/生成先验/视频模型」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2603.15583](method_figures/2603.15583_Real-World.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Grounding_World_Simulation_Models_in_a_Real_World_Metropolis_2603.15583.pdf
- Code：https://github.com/naver-ai/seoul-world-model（code_link_found_not_audited）

##### 解法族：Feed-forward / Transformer / Foundation Model（1）
###### VGGT-World ｜ 2603.12655
- Paper：VGGT-World: Transforming VGGT into an Autoregressive Geometry World Model
- 一句话：VGGT-World 针对「提升可控生成/世界演化预测」，从「时空/动态角度」切入，主要采用「Feed-forward / Transformer / Foundation Model」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2603.12655](method_figures/2603.12655_VGGT-World.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_VGGT_World_Transforming_VGGT_into_an_Autoregressive_Geometry_World_Model_2603.12655.pdf

##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### WorldAgents ｜ 2603.19708
- Paper：WorldAgents: Can Foundation Image Models be Agents for 3D World Models?
- 一句话：WorldAgents 针对「提升可控生成/世界演化预测」，从「时空/动态角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2603.19708](method_figures/2603.19708_WorldAgents.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_WorldAgents_Can_Foundation_Image_Models_be_Agents_for_3D_World_Models_2603.19708.pdf
- Code：https://github.com/black-forest-labs/flux2（code_link_found_not_audited）

#### 子问题：解决稀疏视角几何不稳定（5）
##### 解法族：Diffusion/生成先验/视频模型（1）
###### ArtifactWorld ｜ 2604.12251
- Paper：ArtifactWorld: Scaling 3D Gaussian Splatting Artifact Restoration via Video Generation Models
- 一句话：ArtifactWorld 针对「解决稀疏视角几何不稳定」，从「时空/动态角度」切入，主要采用「Diffusion/生成先验/视频模型」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2604.12251](method_figures/2604.12251_ArtifactWorld.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_ArtifactWorld_Scaling_3D_Gaussian_Splatting_Artifact_Restoration_via_Video_Generation_Mode_2604.12251.pdf

##### 解法族：SLAM / pose graph / online mapping pipeline（4；另有 1 篇见 full/csv）
###### 3DTCR ｜ 2603.13049
- Paper：3DTCR: A Physics-Based Generative Framework for Vortex-Following 3D Reconstruction to Improve Tropical Cyclone Intensity Forecasting
- 一句话：3DTCR 针对「解决稀疏视角几何不稳定」，从「时空/动态角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2603.13049](method_figures/2603.13049_3DTCR.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_3DTCR_A_Physics_Based_Generative_Framework_for_Vortex_Following_3D_Reconstruction_to_Impro_2603.13049.pdf
- Code：https://github.com/JunLiu88/3DTCR（code_link_found_not_audited）
###### HumanOrbit ｜ 2602.24148
- Paper：HumanOrbit: 3D Human Reconstruction as 360° Orbit Generation
- 一句话：HumanOrbit 针对「解决稀疏视角几何不稳定」，从「时空/动态角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2602.24148](method_figures/2602.24148_HumanOrbit.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_HumanOrbit_3D_Human_Reconstruction_as_360_Orbit_Generation_2602.24148.pdf
###### LD-SLRO ｜ 2602.05434
- Paper：LD-SLRO: Latent Diffusion Structured Light for 3-D Reconstruction of Highly Reflective Objects
- 一句话：LD-SLRO 针对「解决稀疏视角几何不稳定」，从「时空/动态角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2602.05434](method_figures/2602.05434_LD-SLRO.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_LD_SLRO_Latent_Diffusion_Structured_Light_for_3_D_Reconstruction_of_Highly_Reflective_Obje_2602.05434.pdf

### 切入点：生成/世界模型角度（26）
#### 子问题：提升可控生成/世界演化预测（22）
##### 解法族：Diffusion/生成先验/视频模型（15；另有 12 篇见 full/csv）
###### Aether ｜ 2503.18945
- Paper：Aether: Geometric-Aware Unified World Modeling
- 一句话：Aether 针对「提升可控生成/世界演化预测」，从「生成/世界模型角度」切入，主要采用「Diffusion/生成先验/视频模型」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2503.18945](method_figures/2503.18945_Aether.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2025_Aether_Geometric_Aware_Unified_World_Modeling_2503.18945.pdf
- Code：https://github.com/OpenRobotLab/Aether（code_link_found_not_audited）
###### Action Images ｜ 2604.06168
- Paper：Action Images: End-to-End Policy Learning via Multiview Video Generation
- 一句话：Action Images 针对「提升可控生成/世界演化预测」，从「生成/世界模型角度」切入，主要采用「Diffusion/生成先验/视频模型」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2604.06168](method_figures/2604.06168_Action_Images.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Action_Images_End_to_End_Policy_Learning_via_Multiview_Video_Generation_2604.06168.pdf
- Code：https://github.com/UMass-Embodied-AGI/ActionImages（code_link_found_not_audited）
###### ActionParty ｜ 2604.02330
- Paper：ActionParty: Multi-Subject Action Binding in Generative Video Games
- 一句话：ActionParty 针对「提升可控生成/世界演化预测」，从「生成/世界模型角度」切入，主要采用「Diffusion/生成先验/视频模型」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2604.02330](method_figures/2604.02330_ActionParty.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_ActionParty_Multi_Subject_Action_Binding_in_Generative_Video_Games_2604.02330.pdf
- Code：https://github.com/action-party/action-party（code_link_found_not_audited）

##### 解法族：Gaussian Splatting 表示与正则化（1）
###### Physics-Grounded ｜ 2602.00148
- Paper：Learning Physics-Grounded 4D Dynamics with Neural Gaussian Force Fields
- 一句话：Physics-Grounded 针对「提升可控生成/世界演化预测」，从「生成/世界模型角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2602.00148](method_figures/2602.00148_Physics-Grounded.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Learning_Physics_Grounded_4D_Dynamics_with_Neural_Gaussian_Force_Fields_2602.00148.pdf
- Code：https://github.com/lishiqianhugh/NeuralGaussianForceField（code_link_found_not_audited）

##### 解法族：Pruning / compression / progressive coding（1）
###### 本文方法 ｜ 2603.08546
- Paper：Interactive World Simulator for Robot Policy Training and Evaluation
- 一句话：本文方法 针对「提升可控生成/世界演化预测」，从「生成/世界模型角度」切入，主要采用「Pruning / compression / progressive coding」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2603.08546](method_figures/2603.08546_paper.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Interactive_World_Simulator_for_Robot_Policy_Training_and_Evaluation_2603.08546.pdf

##### 解法族：SLAM / pose graph / online mapping pipeline（5；另有 2 篇见 full/csv）
###### Enactor ｜ 2603.18266
- Paper：Enactor: From Traffic Simulators to Surrogate World Models
- 一句话：Enactor 针对「提升可控生成/世界演化预测」，从「生成/世界模型角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2603.18266](method_figures/2603.18266_Enactor.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Enactor_From_Traffic_Simulators_to_Surrogate_World_Models_2603.18266.pdf
###### Latent World Models for Automated Driving ｜ 2603.09086
- Paper：Latent World Models for Automated Driving: A Unified Taxonomy, Evaluation Framework, and Open Challenges
- 一句话：Latent World Models for Automated Driving 针对「提升可控生成/世界演化预测」，从「生成/世界模型角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2603.09086](method_figures/2603.09086_Latent_World_Models_for_Automated_Driving.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Latent_World_Models_for_Automated_Driving_A_Unified_Taxonomy_Evaluation_Framework_and_Open_2603.09086.pdf
###### NeoVerse ｜ 2601.00393
- Paper：NeoVerse: Enhancing 4D World Model with in-the-wild Monocular Videos
- 一句话：NeoVerse 针对「提升可控生成/世界演化预测」，从「生成/世界模型角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2601.00393](method_figures/2601.00393_NeoVerse.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_NeoVerse_Enhancing_4D_World_Model_with_in_the_wild_Monocular_Videos_2601.00393.pdf
- Code：https://github.com/IamCreateAI/NeoVerse（code_link_found_not_audited）

#### 子问题：解决稀疏视角几何不稳定（3）
##### 解法族：Diffusion/生成先验/视频模型（2）
###### GO-Renderer ｜ 2603.23246
- Paper：GO-Renderer: Generative Object Rendering with 3D-aware Controllable Video Diffusion Models
- 一句话：GO-Renderer 针对「解决稀疏视角几何不稳定」，从「生成/世界模型角度」切入，主要采用「Diffusion/生成先验/视频模型」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2603.23246](method_figures/2603.23246_GO-Renderer.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_GO_Renderer_Generative_Object_Rendering_with_3D_aware_Controllable_Video_Diffusion_Models_2603.23246.pdf
- Code：https://github.com/IGL-HKUST/GO-Renderer（code_link_found_not_audited）
###### Rotate Your Character ｜ 2601.05722
- Paper：Rotate Your Character: Revisiting Video Diffusion Models for High-Quality 3D Character Generation
- 一句话：Rotate Your Character 针对「解决稀疏视角几何不稳定」，从「生成/世界模型角度」切入，主要采用「Diffusion/生成先验/视频模型」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2601.05722](method_figures/2601.05722_Rotate_Your_Character.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Rotate_Your_Character_Revisiting_Video_Diffusion_Models_for_High_Quality_3D_Character_Gene_2601.05722.pdf

##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### GlassesGB ｜ 2601.17088
- Paper：GlassesGB: Controllable 2D GAN-Based Eyewear Personalization for 3D Gaussian Blendshapes Head Avatars
- 一句话：GlassesGB 针对「解决稀疏视角几何不稳定」，从「生成/世界模型角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2601.17088](method_figures/2601.17088_GlassesGB.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_GlassesGB_Controllable_2D_GAN_Based_Eyewear_Personalization_for_3D_Gaussian_Blendshapes_He_2601.17088.pdf
- Code：https://github.com/nerfies/nerfies.github.io（code_link_found_not_audited）

#### 子问题：降低显存/存储/模型体积（1）
##### 解法族：Pruning / compression / progressive coding（1）
###### GaussianGPT ｜ 2603.26661
- Paper：GaussianGPT: Towards Autoregressive 3D Gaussian Scene Generation
- 一句话：GaussianGPT 针对「降低显存/存储/模型体积」，从「生成/世界模型角度」切入，主要采用「Pruning / compression / progressive coding」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2603.26661](method_figures/2603.26661_GaussianGPT.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_GaussianGPT_Towards_Autoregressive_3D_Gaussian_Scene_Generation_2603.26661.pdf
- Code：https://github.com/KellerJordan/Muon（code_link_found_not_audited）

### 切入点：系统/在线部署角度（1）
#### 子问题：建模运动/形变/时间一致性（1）
##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### R-PGA ｜ 2603.26067
- Paper：R-PGA: Robust Physical Adversarial Camouflage Generation via Relightable 3D Gaussian Splatting
- 一句话：R-PGA 针对「建模运动/形变/时间一致性」，从「系统/在线部署角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2603.26067](method_figures/2603.26067_R-PGA.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_R_PGA_Robust_Physical_Adversarial_Camouflage_Generation_via_Relightable_3D_Gaussian_Splatt_2603.26067.pdf

### 切入点：表示/几何角度（13）
#### 子问题：减少优化/采样/渲染步骤（1）
##### 解法族：Gaussian Splatting 表示与正则化（1）
###### S2D ｜ 2603.10893
- Paper：S2D: Sparse to Dense Lifting for 3D Reconstruction with Minimal Inputs
- 一句话：S2D 针对「减少优化/采样/渲染步骤」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2603.10893](method_figures/2603.10893_S2D.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_S2D_Sparse_to_Dense_Lifting_for_3D_Reconstruction_with_Minimal_Inputs_2603.10893.pdf
- Code：https://github.com/George-Attano/S2D_Base/tree/main（code_link_found_not_audited）

#### 子问题：提升几何一致性/表面质量（4）
##### 解法族：Gaussian Splatting 表示与正则化（3）
###### LightHarmony3D ｜ 2603.29209
- Paper：LightHarmony3D: Harmonizing Illumination and Shadows for Object Insertion in 3D Gaussian Splatting
- 一句话：LightHarmony3D 针对「提升几何一致性/表面质量」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2603.29209](method_figures/2603.29209_LightHarmony3D.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_LightHarmony3D_Harmonizing_Illumination_and_Shadows_for_Object_Insertion_in_3D_Gaussian_Sp_2603.29209.pdf
###### M2StyleGS ｜ 2604.03773
- Paper：M2StyleGS: Multi-Modality 3D Style Transfer with Gaussian Splatting
- 一句话：M2StyleGS 针对「提升几何一致性/表面质量」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2604.03773](method_figures/2604.03773_M2StyleGS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_M2StyleGS_Multi_Modality_3D_Style_Transfer_with_Gaussian_Splatting_2604.03773.pdf
###### SpectralSplat ｜ 2604.03462
- Paper：SpectralSplat: Appearance-Disentangled Feed-Forward Gaussian Splatting for Driving Scenes
- 一句话：SpectralSplat 针对「提升几何一致性/表面质量」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2604.03462](method_figures/2604.03462_SpectralSplat.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_SpectralSplat_Appearance_Disentangled_Feed_Forward_Gaussian_Splatting_for_Driving_Scenes_2604.03462.pdf

##### 解法族：NeRF/辐射场/体渲染（1）
###### EAG-PT ｜ 2601.23065
- Paper：EAG-PT: Emission-Aware Gaussians and Path Tracing for Indoor Scene Reconstruction and Editing
- 一句话：EAG-PT 针对「提升几何一致性/表面质量」，从「表示/几何角度」切入，主要采用「NeRF/辐射场/体渲染」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2601.23065](method_figures/2601.23065_EAG-PT.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_EAG_PT_Emission_Aware_Gaussians_and_Path_Tracing_for_Indoor_Scene_Reconstruction_and_Editi_2601.23065.pdf
- Code：https://github.com/eliphatfs/torchoptix（code_link_found_not_audited）

#### 子问题：提升可控生成/世界演化预测（1）
##### 解法族：Gaussian Splatting 表示与正则化（1）
###### Mirage2Matter ｜ 2602.00096
- Paper：Mirage2Matter: A Physically Grounded Gaussian World Model from Video
- 一句话：Mirage2Matter 针对「提升可控生成/世界演化预测」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2602.00096](method_figures/2602.00096_Mirage2Matter.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Mirage2Matter_A_Physically_Grounded_Gaussian_World_Model_from_Video_2602.00096.pdf
- Code：https://github.com/VAST-AI-Research/TripoSR（code_link_found_not_audited）

#### 子问题：提升泛化/跨场景/开放世界能力（1）
##### 解法族：NeRF/辐射场/体渲染（1）
###### Bridging Visual and Wireless Sensing ｜ 2601.19216
- Paper：Bridging Visual and Wireless Sensing: A Unified Radiation Field for 3D Radio Map Construction
- 一句话：Bridging Visual and Wireless Sensing 针对「提升泛化/跨场景/开放世界能力」，从「表示/几何角度」切入，主要采用「NeRF/辐射场/体渲染」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2601.19216](method_figures/2601.19216_Bridging_Visual_and_Wireless_Sensing.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Bridging_Visual_and_Wireless_Sensing_A_Unified_Radiation_Field_for_3D_Radio_Map_Constructi_2601.19216.pdf
- Code：https://github.com/wenchaozheng/URF-GS（code_link_found_not_audited）

#### 子问题：解决稀疏视角几何不稳定（4）
##### 解法族：Diffusion/生成先验/视频模型（1）
###### 本文方法 ｜ 2602.17909
- Paper：A Single Image and Multimodality Is All You Need for Novel View Synthesis
- 一句话：本文方法 针对「解决稀疏视角几何不稳定」，从「表示/几何角度」切入，主要采用「Diffusion/生成先验/视频模型」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2602.17909](method_figures/2602.17909_paper.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_A_Single_Image_and_Multimodality_Is_All_You_Need_for_Novel_View_Synthesis_2602.17909.pdf
- Code：https://github.com/importAmir/MultiModalNVS（code_link_found_not_audited）

##### 解法族：Gaussian Splatting 表示与正则化（1）
###### FreeFix ｜ 2601.20857
- Paper：FreeFix: Boosting 3D Gaussian Splatting via Fine-Tuning-Free Diffusion Models
- 一句话：FreeFix 针对「解决稀疏视角几何不稳定」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2601.20857](method_figures/2601.20857_FreeFix.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_FreeFix_Boosting_3D_Gaussian_Splatting_via_Fine_Tuning_Free_Diffusion_Models_2601.20857.pdf
- Code：https://github.com/hyzhou404/FreeFix（code_link_found_not_audited）

##### 解法族：NeRF/辐射场/体渲染（1）
###### NeRF ｜ 2604.11983
- Paper：A Geometric Algebra-informed NeRF Framework for Generalizable Wireless Channel Prediction
- 一句话：NeRF 针对「解决稀疏视角几何不稳定」，从「表示/几何角度」切入，主要采用「NeRF/辐射场/体渲染」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2604.11983](method_figures/2604.11983_NeRF.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_A_Geometric_Algebra_informed_NeRF_Framework_for_Generalizable_Wireless_Channel_Prediction_2604.11983.pdf

##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### Intrinsic Tolerance in C-Arm Imaging ｜ 2603.14031
- Paper：Intrinsic Tolerance in C-Arm Imaging: How Extrinsic Re-optimization Preserves 3D Reconstruction Accuracy
- 一句话：Intrinsic Tolerance in C-Arm Imaging 针对「解决稀疏视角几何不稳定」，从「表示/几何角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2603.14031](method_figures/2603.14031_Intrinsic_Tolerance_in_C-Arm_Imaging.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Intrinsic_Tolerance_in_C_Arm_Imaging_How_Extrinsic_Re_optimization_Preserves_3D_Reconstruc_2603.14031.pdf

#### 子问题：降低显存/存储/模型体积（2）
##### 解法族：Gaussian Splatting 表示与正则化（1）
###### ARGS ｜ 2604.00494
- Paper：ARGS: Auto-Regressive Gaussian Splatting via Parallel Progressive Next-Scale Prediction
- 一句话：ARGS 针对「降低显存/存储/模型体积」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2604.00494](method_figures/2604.00494_ARGS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_ARGS_Auto_Regressive_Gaussian_Splatting_via_Parallel_Progressive_Next_Scale_Prediction_2604.00494.pdf

##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### Brain3D ｜ 2604.08068
- Paper：Brain3D: EEG-to-3D Decoding of Visual Representations via Multimodal Reasoning
- 一句话：Brain3D 针对「降低显存/存储/模型体积」，从「表示/几何角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2604.08068](method_figures/2604.08068_Brain3D.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Brain3D_EEG_to_3D_Decoding_of_Visual_Representations_via_Multimodal_Reasoning_2604.08068.pdf

### 切入点：计算角度（2）
#### 子问题：减少优化/采样/渲染步骤（1）
##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### LGM ｜ 2402.05054
- Paper：LGM: Large Multi-View Gaussian Model for High-Resolution 3D Content Creation
- 一句话：LGM 针对「减少优化/采样/渲染步骤」，从「计算角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2402.05054](method_figures/2402.05054_LGM.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2024_LGM_Large_Multi_View_Gaussian_Model_for_High_Resolution_3D_Content_Creation_2402.05054.pdf

#### 子问题：接入 SLAM/机器人闭环系统（1）
##### 解法族：组合式/混合 pipeline（1）
###### SLAT-Phys ｜ 2603.23973
- Paper：SLAT-Phys: Fast Material Property Field Prediction from Structured 3D Latents
- 一句话：SLAT-Phys 针对「接入 SLAM/机器人闭环系统」，从「计算角度」切入，主要采用「组合式/混合 pipeline」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2603.23973](method_figures/2603.23973_SLAT-Phys.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_SLAT_Phys_Fast_Material_Property_Field_Prediction_from_Structured_3D_Latents_2603.23973.pdf
- Code：https://github.com/nerfies/nerfies.github.io（code_link_found_not_audited）

### 切入点：训练/监督角度（39）
#### 子问题：减少优化/采样/渲染步骤（1）
##### 解法族：Gaussian Splatting 表示与正则化（1）
###### DAV-GSWT ｜ 2602.15355
- Paper：DAV-GSWT: Diffusion-Active-View Sampling for Data-Efficient Gaussian Splatting Wang Tiles
- 一句话：DAV-GSWT 针对「减少优化/采样/渲染步骤」，从「训练/监督角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2602.15355](method_figures/2602.15355_DAV-GSWT.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_DAV_GSWT_Diffusion_Active_View_Sampling_for_Data_Efficient_Gaussian_Splatting_Wang_Tiles_2602.15355.pdf

#### 子问题：建模运动/形变/时间一致性（5）
##### 解法族：Diffusion/生成先验/视频模型（2）
###### SemanticNVS ｜ 2602.20079
- Paper：SemanticNVS: Improving Semantic Scene Understanding in Generative Novel View Synthesis
- 一句话：SemanticNVS 针对「建模运动/形变/时间一致性」，从「训练/监督角度」切入，主要采用「Diffusion/生成先验/视频模型」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2602.20079](method_figures/2602.20079_SemanticNVS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_SemanticNVS_Improving_Semantic_Scene_Understanding_in_Generative_Novel_View_Synthesis_2602.20079.pdf
- Code：https://github.com/XinyaChen21/SemanticNVS（code_link_found_not_audited）
###### VGGRPO ｜ 2603.26599
- Paper：VGGRPO: Towards World-Consistent Video Generation with 4D Latent Reward
- 一句话：VGGRPO 针对「建模运动/形变/时间一致性」，从「训练/监督角度」切入，主要采用「Diffusion/生成先验/视频模型」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2603.26599](method_figures/2603.26599_VGGRPO.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_VGGRPO_Towards_World_Consistent_Video_Generation_with_4D_Latent_Reward_2603.26599.pdf
- Code：https://github.com/JD-P/simulacra-aesthetic-captions（code_link_found_not_audited）

##### 解法族：Gaussian Splatting 表示与正则化（1）
###### UltraG-Ray ｜ 2603.29022
- Paper：UltraG-Ray: Physics-Based Gaussian Ray Casting for Novel Ultrasound View Synthesis
- 一句话：UltraG-Ray 针对「建模运动/形变/时间一致性」，从「训练/监督角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2603.29022](method_figures/2603.29022_UltraG-Ray.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_UltraG_Ray_Physics_Based_Gaussian_Ray_Casting_for_Novel_Ultrasound_View_Synthesis_2603.29022.pdf

##### 解法族：NeRF/辐射场/体渲染（1）
###### DreamFusion ｜ 2209.14988
- Paper：DreamFusion: Text-to-3D using 2D Diffusion
- 一句话：DreamFusion 针对「建模运动/形变/时间一致性」，从「训练/监督角度」切入，主要采用「NeRF/辐射场/体渲染」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2209.14988](method_figures/2209.14988_DreamFusion.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2022_DreamFusion_Text_to_3D_using_2D_Diffusion_2209.14988.pdf
- Code：https://github.com/google-research/multinerf（code_link_found_not_audited）

##### 解法族：SDF/隐式表面/网格/点云（1）
###### 本文方法 ｜ 2603.09925
- Paper：On the Structural Failure of Chamfer Distance in 3D Shape Optimization
- 一句话：本文方法 针对「建模运动/形变/时间一致性」，从「训练/监督角度」切入，主要采用「SDF/隐式表面/网格/点云」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2603.09925](method_figures/2603.09925_paper.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_On_the_Structural_Failure_of_Chamfer_Distance_in_3D_Shape_Optimization_2603.09925.pdf

#### 子问题：提升几何一致性/表面质量（11）
##### 解法族：Diffusion/生成先验/视频模型（2）
###### GeodesicNVS ｜ 2603.01010
- Paper：GeodesicNVS: Probability Density Geodesic Flow Matching for Novel View Synthesis
- 一句话：GeodesicNVS 针对「提升几何一致性/表面质量」，从「训练/监督角度」切入，主要采用「Diffusion/生成先验/视频模型」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2603.01010](method_figures/2603.01010_GeodesicNVS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_GeodesicNVS_Probability_Density_Geodesic_Flow_Matching_for_Novel_View_Synthesis_2603.01010.pdf
###### OrbitNVS ｜ 2603.19613
- Paper：OrbitNVS: Harnessing Video Diffusion Priors for Novel View Synthesis
- 一句话：OrbitNVS 针对「提升几何一致性/表面质量」，从「训练/监督角度」切入，主要采用「Diffusion/生成先验/视频模型」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2603.19613](method_figures/2603.19613_OrbitNVS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_OrbitNVS_Harnessing_Video_Diffusion_Priors_for_Novel_View_Synthesis_2603.19613.pdf

##### 解法族：Gaussian Splatting 表示与正则化（3）
###### Leveling3D ｜ 2603.16211
- Paper：Leveling3D: Leveling Up 3D Reconstruction with Feed-Forward 3D Gaussian Splatting and Geometry-Aware Generation
- 一句话：Leveling3D 针对「提升几何一致性/表面质量」，从「训练/监督角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2603.16211](method_figures/2603.16211_Leveling3D.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Leveling3D_Leveling_Up_3D_Reconstruction_with_Feed_Forward_3D_Gaussian_Splatting_and_Geome_2603.16211.pdf
###### LiDAR-EVS ｜ 2603.14763
- Paper：LiDAR-EVS: Enhance Extrapolated View Synthesis for 3D Gaussian Splatting with Pseudo-LiDAR Supervision
- 一句话：LiDAR-EVS 针对「提升几何一致性/表面质量」，从「训练/监督角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2603.14763](method_figures/2603.14763_LiDAR-EVS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_LiDAR_EVS_Enhance_Extrapolated_View_Synthesis_for_3D_Gaussian_Splatting_with_Pseudo_LiDAR_2603.14763.pdf
###### SIC3D ｜ 2604.08760
- Paper：SIC3D: Style Image Conditioned Text-to-3D Gaussian Splatting Generation
- 一句话：SIC3D 针对「提升几何一致性/表面质量」，从「训练/监督角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2604.08760](method_figures/2604.08760_SIC3D.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_SIC3D_Style_Image_Conditioned_Text_to_3D_Gaussian_Splatting_Generation_2604.08760.pdf

##### 解法族：SLAM / pose graph / online mapping pipeline（6；另有 3 篇见 full/csv）
###### SyncDreamer ｜ 2309.03453
- Paper：SyncDreamer: Generating Multiview-consistent Images from a Single-view Image
- 一句话：SyncDreamer 针对「提升几何一致性/表面质量」，从「训练/监督角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2309.03453](method_figures/2309.03453_SyncDreamer.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2024_SyncDreamer_Generating_Multiview_consistent_Images_from_a_Single_view_Image_2309.03453.pdf
- Code：https://github.com/liuyuan-pal/SyncDreamer（code_link_found_not_audited）
###### DiffStyle3D ｜ 2601.19717
- Paper：DiffStyle3D: Consistent 3D Gaussian Stylization via Attention Optimization
- 一句话：DiffStyle3D 针对「提升几何一致性/表面质量」，从「训练/监督角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2601.19717](method_figures/2601.19717_DiffStyle3D.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_DiffStyle3D_Consistent_3D_Gaussian_Stylization_via_Attention_Optimization_2601.19717.pdf
###### GeoDiff3D ｜ 2601.19785
- Paper：GeoDiff3D: Self-Supervised 3D Scene Generation with Geometry-Constrained 2D Diffusion Guidance
- 一句话：GeoDiff3D 针对「提升几何一致性/表面质量」，从「训练/监督角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2601.19785](method_figures/2601.19785_GeoDiff3D.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_GeoDiff3D_Self_Supervised_3D_Scene_Generation_with_Geometry_Constrained_2D_Diffusion_Guida_2601.19785.pdf
- Code：https://github.com/XLabs-AI/x-flux（code_link_found_not_audited）

#### 子问题：提升可控生成/世界演化预测（6）
##### 解法族：Diffusion/生成先验/视频模型（5；另有 2 篇见 full/csv）
###### GR3EN ｜ 2601.16272
- Paper：GR3EN: Generative Relighting for 3D Environments
- 一句话：GR3EN 针对「提升可控生成/世界演化预测」，从「训练/监督角度」切入，主要采用「Diffusion/生成先验/视频模型」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2601.16272](method_figures/2601.16272_GR3EN.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_GR3EN_Generative_Relighting_for_3D_Environments_2601.16272.pdf
###### 本文方法 ｜ 2601.10553
- Paper：Inference-time Physics Alignment of Video Generative Models with Latent World Models
- 一句话：本文方法 针对「提升可控生成/世界演化预测」，从「训练/监督角度」切入，主要采用「Diffusion/生成先验/视频模型」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2601.10553](method_figures/2601.10553_paper.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Inference_time_Physics_Alignment_of_Video_Generative_Models_with_Latent_World_Models_2601.10553.pdf
- Code：https://github.com/facebookresearch/WMReward（code_link_found_not_audited）
###### LIVE ｜ 2602.03747
- Paper：LIVE: Long-horizon Interactive Video World Modeling
- 一句话：LIVE 针对「提升可控生成/世界演化预测」，从「训练/监督角度」切入，主要采用「Diffusion/生成先验/视频模型」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2602.03747](method_figures/2602.03747_LIVE.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_LIVE_Long_horizon_Interactive_Video_World_Modeling_2602.03747.pdf
- Code：https://github.com/Junchao-cs/LIVE（code_link_found_not_audited）

##### 解法族：Feed-forward / Transformer / Foundation Model（1）
###### Omni123 ｜ 2604.02289
- Paper：Omni123: Exploring 3D Native Foundation Models with Limited 3D Data by Unifying Text to 2D and 3D Generation
- 一句话：Omni123 针对「提升可控生成/世界演化预测」，从「训练/监督角度」切入，主要采用「Feed-forward / Transformer / Foundation Model」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2604.02289](method_figures/2604.02289_Omni123.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Omni123_Exploring_3D_Native_Foundation_Models_with_Limited_3D_Data_by_Unifying_Text_to_2D_2604.02289.pdf
- Code：https://github.com/black-forest-labs/flux2（code_link_found_not_audited）

#### 子问题：解决稀疏视角几何不稳定（12）
##### 解法族：Diffusion/生成先验/视频模型（4；另有 1 篇见 full/csv）
###### LaVR ｜ 2601.14674
- Paper：LaVR: Scene Latent Conditioned Generative Video Trajectory Re-Rendering using Large 4D Reconstruction Models
- 一句话：LaVR 针对「解决稀疏视角几何不稳定」，从「训练/监督角度」切入，主要采用「Diffusion/生成先验/视频模型」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2601.14674](method_figures/2601.14674_LaVR.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_LaVR_Scene_Latent_Conditioned_Generative_Video_Trajectory_Re_Rendering_using_Large_4D_Reco_2601.14674.pdf
###### 本文方法 ｜ 2603.22275
- Paper：Repurposing Geometric Foundation Models for Multi-view Diffusion
- 一句话：本文方法 针对「解决稀疏视角几何不稳定」，从「训练/监督角度」切入，主要采用「Diffusion/生成先验/视频模型」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2603.22275](method_figures/2603.22275_paper.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Repurposing_Geometric_Foundation_Models_for_Multi_view_Diffusion_2603.22275.pdf
- Code：https://github.com/cvlab-kaist/GLD/（code_link_found_not_audited）
###### Training-Free ｜ 2603.21166
- Paper：Training-Free Instance-Aware 3D Scene Reconstruction and Diffusion-Based View Synthesis from Sparse Images
- 一句话：Training-Free 针对「解决稀疏视角几何不稳定」，从「训练/监督角度」切入，主要采用「Diffusion/生成先验/视频模型」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2603.21166](method_figures/2603.21166_Training-Free.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Training_Free_Instance_Aware_3D_Scene_Reconstruction_and_Diffusion_Based_View_Synthesis_fr_2603.21166.pdf
- Code：https://github.com/nerfies/nerfies.github.io（code_link_found_not_audited）

##### 解法族：Gaussian Splatting 表示与正则化（4；另有 1 篇见 full/csv）
###### ArtiFixer ｜ 2603.00492
- Paper：ArtiFixer: Enhancing and Extending 3D Reconstruction with Auto-Regressive Diffusion Models
- 一句话：ArtiFixer 针对「解决稀疏视角几何不稳定」，从「训练/监督角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2603.00492](method_figures/2603.00492_ArtiFixer.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_ArtiFixer_Enhancing_and_Extending_3D_Reconstruction_with_Auto_Regressive_Diffusion_Models_2603.00492.pdf
- Code：https://github.com/Hopding/pdf-lib（code_link_found_not_audited）
###### Instrument-Splatting++ ｜ 2603.22792
- Paper：Instrument-Splatting++: Towards Controllable Surgical Instrument Digital Twin Using Gaussian Splatting
- 一句话：Instrument-Splatting++ 针对「解决稀疏视角几何不稳定」，从「训练/监督角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2603.22792](method_figures/2603.22792_Instrument-Splatting.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Instrument_Splatting_Towards_Controllable_Surgical_Instrument_Digital_Twin_Using_Gaussian_2603.22792.pdf
###### LL-GaussianMap ｜ 2601.15766
- Paper：LL-GaussianMap: Zero-shot Low-Light Image Enhancement via 2D Gaussian Splatting Guided Gain Maps
- 一句话：LL-GaussianMap 针对「解决稀疏视角几何不稳定」，从「训练/监督角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2601.15766](method_figures/2601.15766_LL-GaussianMap.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_LL_GaussianMap_Zero_shot_Low_Light_Image_Enhancement_via_2D_Gaussian_Splatting_Guided_Gain_2601.15766.pdf

##### 解法族：SLAM / pose graph / online mapping pipeline（4；另有 1 篇见 full/csv）
###### Free-Range Gaussians ｜ 2604.04874
- Paper：Free-Range Gaussians: Non-Grid-Aligned Generative 3D Gaussian Reconstruction
- 一句话：Free-Range Gaussians 针对「解决稀疏视角几何不稳定」，从「训练/监督角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2604.04874](method_figures/2604.04874_Free-Range_Gaussians.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Free_Range_Gaussians_Non_Grid_Aligned_Generative_3D_Gaussian_Reconstruction_2604.04874.pdf
###### Fine-Tuning ｜ 2604.09688
- Paper：Immunizing 3D Gaussian Generative Models Against Unauthorized Fine-Tuning via Attribute-Space Traps
- 一句话：Fine-Tuning 针对「解决稀疏视角几何不稳定」，从「训练/监督角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2604.09688](method_figures/2604.09688_Fine-Tuning.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Immunizing_3D_Gaussian_Generative_Models_Against_Unauthorized_Fine_Tuning_via_Attribute_Sp_2604.09688.pdf
###### Soft Shadow Diffusion (SSD) ｜ 2601.12257
- Paper：Soft Shadow Diffusion (SSD): Physics-inspired Learning for 3D Computational Periscopy
- 一句话：Soft Shadow Diffusion (SSD) 针对「解决稀疏视角几何不稳定」，从「训练/监督角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2601.12257](method_figures/2601.12257_Soft_Shadow_Diffusion_SSD.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Soft_Shadow_Diffusion_SSD_Physics_inspired_Learning_for_3D_Computational_Periscopy_2601.12257.pdf

#### 子问题：降低显存/存储/模型体积（4）
##### 解法族：Diffusion/生成先验/视频模型（1）
###### From Part to Whole ｜ 2603.21557
- Paper：From Part to Whole: 3D Generative World Model with an Adaptive Structural Hierarchy
- 一句话：From Part to Whole 针对「降低显存/存储/模型体积」，从「训练/监督角度」切入，主要采用「Diffusion/生成先验/视频模型」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2603.21557](method_figures/2603.21557_From_Part_to_Whole.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_From_Part_to_Whole_3D_Generative_World_Model_with_an_Adaptive_Structural_Hierarchy_2603.21557.pdf

##### 解法族：Gaussian Splatting 表示与正则化（1）
###### HeadLighter ｜ 2601.02103
- Paper：HeadLighter: Disentangling Illumination in Generative 3D Gaussian Heads via Lightstage Captures
- 一句话：HeadLighter 针对「降低显存/存储/模型体积」，从「训练/监督角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2601.02103](method_figures/2601.02103_HeadLighter.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_HeadLighter_Disentangling_Illumination_in_Generative_3D_Gaussian_Heads_via_Lightstage_Capt_2601.02103.pdf
- Code：https://github.com/yakhyo/face-parsing（code_link_found_not_audited）

##### 解法族：Pruning / compression / progressive coding（1）
###### Geometry-Appearance ｜ 2601.00328
- Paper：Joint Geometry-Appearance Human Reconstruction in a Unified Latent Space via Bridge Diffusion
- 一句话：Geometry-Appearance 针对「降低显存/存储/模型体积」，从「训练/监督角度」切入，主要采用「Pruning / compression / progressive coding」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2601.00328](method_figures/2601.00328_Geometry-Appearance.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Joint_Geometry_Appearance_Human_Reconstruction_in_a_Unified_Latent_Space_via_Bridge_Diffus_2601.00328.pdf
- Code：https://github.com/haiantyz/JGA-LBD（code_link_found_not_audited）

##### 解法族：组合式/混合 pipeline（1）
###### Sampling-Aware ｜ 2604.07890
- Paper：Sampling-Aware 3D Spatial Analysis in Multiplexed Imaging
- 一句话：Sampling-Aware 针对「降低显存/存储/模型体积」，从「训练/监督角度」切入，主要采用「组合式/混合 pipeline」来服务「生成式 3D/4D 内容与仿真」。
- Method diagram：![2604.07890](method_figures/2604.07890_Sampling-Aware.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Sampling_Aware_3D_Spatial_Analysis_in_Multiplexed_Imaging_2604.07890.pdf

## Motivation：稀疏/单目/少视角 3D 重建（88）
### 切入点：时空/动态角度（5）
#### 子问题：解决稀疏视角几何不稳定（5）
##### 解法族：Diffusion/生成先验/视频模型（1）
###### Novel View Synthesis as Video Completion ｜ 2604.08500
- Paper：Novel View Synthesis as Video Completion
- 一句话：Novel View Synthesis as Video Completion 针对「解决稀疏视角几何不稳定」，从「时空/动态角度」切入，主要采用「Diffusion/生成先验/视频模型」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2604.08500](method_figures/2604.08500_Novel_View_Synthesis_as_Video_Completion.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Novel_View_Synthesis_as_Video_Completion_2604.08500.pdf
- Code：https://github.com/szqwu/FrameCrafter（code_link_found_not_audited）

##### 解法族：Motion decomposition / canonical space / deformation（1）
###### MonoArt ｜ 2603.19231
- Paper：MonoArt: Progressive Structural Reasoning for Monocular Articulated 3D Reconstruction
- 一句话：MonoArt 针对「解决稀疏视角几何不稳定」，从「时空/动态角度」切入，主要采用「Motion decomposition / canonical space / deformation」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2603.19231](method_figures/2603.19231_MonoArt.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_MonoArt_Progressive_Structural_Reasoning_for_Monocular_Articulated_3D_Reconstruction_2603.19231.pdf

##### 解法族：NeRF/辐射场/体渲染（1）
###### pixelNeRF ｜ 2012.02190
- Paper：pixelNeRF: Neural Radiance Fields from One or Few Images
- 一句话：pixelNeRF 针对「解决稀疏视角几何不稳定」，从「时空/动态角度」切入，主要采用「NeRF/辐射场/体渲染」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2012.02190](method_figures/2012.02190_pixelNeRF.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2021_pixelNeRF_Neural_Radiance_Fields_from_One_or_Few_Images_2012.02190.pdf

##### 解法族：SLAM / pose graph / online mapping pipeline（2）
###### IBRNet ｜ 2102.13090
- Paper：IBRNet: Learning Multi-View Image-Based Rendering
- 一句话：IBRNet 针对「解决稀疏视角几何不稳定」，从「时空/动态角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2102.13090](method_figures/2102.13090_IBRNet.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2021_IBRNet_Learning_Multi_View_Image_Based_Rendering_2102.13090.pdf
- Code：https://github.com/googleinterns/IBRNet（code_link_found_not_audited）
###### UniCon3R ｜ 2604.19923
- Paper：UniCon3R: Contact-aware 3D Human-Scene Reconstruction from Monocular Video
- 一句话：UniCon3R 针对「解决稀疏视角几何不稳定」，从「时空/动态角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2604.19923](method_figures/2604.19923_UniCon3R.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_UniCon3R_Contact_aware_3D_Human_Scene_Reconstruction_from_Monocular_Video_2604.19923.pdf
- Code：https://github.com/surtantheta/UniCon3R（code_link_found_not_audited）

### 切入点：生成/世界模型角度（2）
#### 子问题：提升可控生成/世界演化预测（1）
##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### A3R ｜ 2604.01882
- Paper：A3R: Agentic Affordance Reasoning via Cross-Dimensional Evidence in 3D Gaussian Scenes
- 一句话：A3R 针对「提升可控生成/世界演化预测」，从「生成/世界模型角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2604.01882](method_figures/2604.01882_A3R.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_A3R_Agentic_Affordance_Reasoning_via_Cross_Dimensional_Evidence_in_3D_Gaussian_Scenes_2604.01882.pdf

#### 子问题：降低显存/存储/模型体积（1）
##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### GenSmoke-GS ｜ 2604.03039
- Paper：GenSmoke-GS: A Multi-Stage Method for Novel View Synthesis from Smoke-Degraded Images Using a Generative Model
- 一句话：GenSmoke-GS 针对「降低显存/存储/模型体积」，从「生成/世界模型角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2604.03039](method_figures/2604.03039_GenSmoke-GS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_GenSmoke_GS_A_Multi_Stage_Method_for_Novel_View_Synthesis_from_Smoke_Degraded_Images_Using_2604.03039.pdf
- Code：https://github.com/plbbl/GenSmoke-GS（code_link_found_not_audited）

### 切入点：表示/几何角度（38）
#### 子问题：减少优化/采样/渲染步骤（3）
##### 解法族：Gaussian Splatting 表示与正则化（1）
###### VIRGi ｜ 2603.02986
- Paper：VIRGi: View-dependent Instant Recoloring of 3D Gaussians Splats
- 一句话：VIRGi 针对「减少优化/采样/渲染步骤」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2603.02986](method_figures/2603.02986_VIRGi.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_VIRGi_View_dependent_Instant_Recoloring_of_3D_Gaussians_Splats_2603.02986.pdf

##### 解法族：NeRF/辐射场/体渲染（2）
###### Generalizable NGP-SR ｜ 2603.20128
- Paper：Generalizable NGP-SR: Generalizable Neural Radiance Fields Super-Resolution via Neural Graph Primitives
- 一句话：Generalizable NGP-SR 针对「减少优化/采样/渲染步骤」，从「表示/几何角度」切入，主要采用「NeRF/辐射场/体渲染」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2603.20128](method_figures/2603.20128_Generalizable_NGP-SR.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Generalizable_NGP_SR_Generalizable_Neural_Radiance_Fields_Super_Resolution_via_Neural_Grap_2603.20128.pdf
- Code：https://github.com/WanqiYuan/NGP-SR（code_link_found_not_audited）
###### SAC-NeRF ｜ 2603.15622
- Paper：SAC-NeRF: Adaptive Ray Sampling for Neural Radiance Fields via Soft Actor-Critic Reinforcement Learning
- 一句话：SAC-NeRF 针对「减少优化/采样/渲染步骤」，从「表示/几何角度」切入，主要采用「NeRF/辐射场/体渲染」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2603.15622](method_figures/2603.15622_SAC-NeRF.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2025_SAC_NeRF_Adaptive_Ray_Sampling_for_Neural_Radiance_Fields_via_Soft_Actor_Critic_Reinforcem_2603.15622.pdf

#### 子问题：建模运动/形变/时间一致性（2）
##### 解法族：Gaussian Splatting 表示与正则化（1）
###### DF3DV-1K ｜ 2604.13416
- Paper：DF3DV-1K: A Large-Scale Dataset and Benchmark for Distractor-Free Novel View Synthesis
- 一句话：DF3DV-1K 针对「建模运动/形变/时间一致性」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2604.13416](method_figures/2604.13416_DF3DV-1K.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_DF3DV_1K_A_Large_Scale_Dataset_and_Benchmark_for_Distractor_Free_Novel_View_Synthesis_2604.13416.pdf

##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### InstantHDR ｜ 2603.11298
- Paper：InstantHDR: Single-forward Gaussian Splatting for High Dynamic Range 3D Reconstruction
- 一句话：InstantHDR 针对「建模运动/形变/时间一致性」，从「表示/几何角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2603.11298](method_figures/2603.11298_InstantHDR.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_InstantHDR_Single_forward_Gaussian_Splatting_for_High_Dynamic_Range_3D_Reconstruction_2603.11298.pdf

#### 子问题：提升几何一致性/表面质量（2）
##### 解法族：NeRF/辐射场/体渲染（1）
###### Spectral-Geometric ｜ 2603.12903
- Paper：Spectral-Geometric Neural Fields for Pose-Free LiDAR View Synthesis
- 一句话：Spectral-Geometric 针对「提升几何一致性/表面质量」，从「表示/几何角度」切入，主要采用「NeRF/辐射场/体渲染」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2603.12903](method_figures/2603.12903_Spectral-Geometric.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Spectral_Geometric_Neural_Fields_for_Pose_Free_LiDAR_View_Synthesis_2603.12903.pdf

##### 解法族：SDF/隐式表面/网格/点云（1）
###### Geo-NVS-w ｜ 2601.08371
- Paper：Geo-NVS-w: Geometry-Aware Novel View Synthesis In-the-Wild with an SDF Renderer
- 一句话：Geo-NVS-w 针对「提升几何一致性/表面质量」，从「表示/几何角度」切入，主要采用「SDF/隐式表面/网格/点云」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2601.08371](method_figures/2601.08371_Geo-NVS-w.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Geo_NVS_w_Geometry_Aware_Novel_View_Synthesis_In_the_Wild_with_an_SDF_Renderer_2601.08371.pdf

#### 子问题：解决稀疏视角几何不稳定（26）
##### 解法族：Gaussian Splatting 表示与正则化（19；另有 16 篇见 full/csv）
###### A Step to Decouple Optimization in 3DGS ｜ 2601.16736
- Paper：A Step to Decouple Optimization in 3DGS
- 一句话：A Step to Decouple Optimization in 3DGS 针对「解决稀疏视角几何不稳定」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2601.16736](method_figures/2601.16736_A_Step_to_Decouple_Optimization_in_3DGS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_A_Step_to_Decouple_Optimization_in_3DGS_2601.16736.pdf
- Code：https://github.com/EliottDJay/3DGS_AdamWGS（code_link_found_not_audited）
###### AA-Splat ｜ 2603.29394
- Paper：AA-Splat: Anti-Aliased Feed-forward Gaussian Splatting
- 一句话：AA-Splat 针对「解决稀疏视角几何不稳定」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2603.29394](method_figures/2603.29394_AA-Splat.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_AA_Splat_Anti_Aliased_Feed_forward_Gaussian_Splatting_2603.29394.pdf
###### AnchorSplat ｜ 2604.07053
- Paper：AnchorSplat: Feed-Forward 3D Gaussian Splatting with 3D Geometric Priors
- 一句话：AnchorSplat 针对「解决稀疏视角几何不稳定」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2604.07053](method_figures/2604.07053_AnchorSplat.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_AnchorSplat_Feed_Forward_3D_Gaussian_Splatting_with_3D_Geometric_Priors_2604.07053.pdf

##### 解法族：NeRF/辐射场/体渲染（1）
###### View-Adaptive ｜ 2602.18322
- Paper：Unifying Color and Lightness Correction with View-Adaptive Curve Adjustment for Robust 3D Novel View Synthesis
- 一句话：View-Adaptive 针对「解决稀疏视角几何不稳定」，从「表示/几何角度」切入，主要采用「NeRF/辐射场/体渲染」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2602.18322](method_figures/2602.18322_View-Adaptive.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Unifying_Color_and_Lightness_Correction_with_View_Adaptive_Curve_Adjustment_for_Robust_3D_2602.18322.pdf

##### 解法族：SDF/隐式表面/网格/点云（1）
###### Real-Time ｜ 2603.15433
- Paper：Real-Time Human Frontal View Synthesis from a Single Image
- 一句话：Real-Time 针对「解决稀疏视角几何不稳定」，从「表示/几何角度」切入，主要采用「SDF/隐式表面/网格/点云」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2603.15433](method_figures/2603.15433_Real-Time.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Real_Time_Human_Frontal_View_Synthesis_from_a_Single_Image_2603.15433.pdf
- Code：https://github.com/rslinfy/PrismMirror（code_link_found_not_audited）

##### 解法族：SLAM / pose graph / online mapping pipeline（5；另有 2 篇见 full/csv）
###### Implicit-Scale ｜ 2602.13041
- Paper：Implicit-Scale 3D Reconstruction for Multi-Food Volume Estimation from Monocular Images
- 一句话：Implicit-Scale 针对「解决稀疏视角几何不稳定」，从「表示/几何角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2602.13041](method_figures/2602.13041_Implicit-Scale.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Implicit_Scale_3D_Reconstruction_for_Multi_Food_Volume_Estimation_from_Monocular_Images_2602.13041.pdf
###### MipSLAM ｜ 2603.06989
- Paper：MipSLAM: Alias-Free Gaussian Splatting SLAM
- 一句话：MipSLAM 针对「解决稀疏视角几何不稳定」，从「表示/几何角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2603.06989](method_figures/2603.06989_MipSLAM.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_MipSLAM_Alias_Free_Gaussian_Splatting_SLAM_2603.06989.pdf
- Code：https://github.com/yzli1998/MipSLAM（code_link_found_not_audited）
###### MonoEM-GS ｜ 2604.10593
- Paper：MonoEM-GS: Monocular Expectation-Maximization Gaussian Splatting SLAM
- 一句话：MonoEM-GS 针对「解决稀疏视角几何不稳定」，从「表示/几何角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2604.10593](method_figures/2604.10593_MonoEM-GS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_MonoEM_GS_Monocular_Expectation_Maximization_Gaussian_Splatting_SLAM_2604.10593.pdf

#### 子问题：降低显存/存储/模型体积（5）
##### 解法族：Gaussian Splatting 表示与正则化（2）
###### IDESplat ｜ 2601.03824
- Paper：IDESplat: Iterative Depth Probability Estimation for Generalizable 3D Gaussian Splatting
- 一句话：IDESplat 针对「降低显存/存储/模型体积」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2601.03824](method_figures/2601.03824_IDESplat.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_IDESplat_Iterative_Depth_Probability_Estimation_for_Generalizable_3D_Gaussian_Splatting_2601.03824.pdf
- Code：https://github.com/CVL-UESTC/IDESplat（code_link_found_not_audited）
###### NG-GS ｜ 2604.14706
- Paper：NG-GS: NeRF-Guided 3D Gaussian Splatting Segmentation
- 一句话：NG-GS 针对「降低显存/存储/模型体积」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2604.14706](method_figures/2604.14706_NG-GS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_NG_GS_NeRF_Guided_3D_Gaussian_Splatting_Segmentation_2604.14706.pdf
- Code：https://github.com/BJTU-KD3D/NG-GS（code_link_found_not_audited）

##### 解法族：NeRF/辐射场/体渲染（1）
###### Evidential Neural Radiance Fields ｜ 2602.23574
- Paper：Evidential Neural Radiance Fields
- 一句话：Evidential Neural Radiance Fields 针对「降低显存/存储/模型体积」，从「表示/几何角度」切入，主要采用「NeRF/辐射场/体渲染」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2602.23574](method_figures/2602.23574_Evidential_Neural_Radiance_Fields.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Evidential_Neural_Radiance_Fields_2602.23574.pdf
- Code：https://github.com/KerryDRX/EvidentialNeRF（code_link_found_not_audited）

##### 解法族：Pruning / compression / progressive coding（1）
###### Camera-Agnostic ｜ 2603.21933
- Paper：Camera-Agnostic Pruning of 3D Gaussian Splats via Descriptor-Based Beta Evidence
- 一句话：Camera-Agnostic 针对「降低显存/存储/模型体积」，从「表示/几何角度」切入，主要采用「Pruning / compression / progressive coding」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2603.21933](method_figures/2603.21933_Camera-Agnostic.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Camera_Agnostic_Pruning_of_3D_Gaussian_Splats_via_Descriptor_Based_Beta_Evidence_2603.21933.pdf

##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### ReCoSplat ｜ 2603.09968
- Paper：ReCoSplat: Autoregressive Feed-Forward Gaussian Splatting Using Render-and-Compare
- 一句话：ReCoSplat 针对「降低显存/存储/模型体积」，从「表示/几何角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2603.09968](method_figures/2603.09968_ReCoSplat.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_ReCoSplat_Autoregressive_Feed_Forward_Gaussian_Splatting_Using_Render_and_Compare_2603.09968.pdf

### 切入点：计算角度（6）
#### 子问题：提升泛化/跨场景/开放世界能力（1）
##### 解法族：Diffusion/生成先验/视频模型（1）
###### LagerNVS ｜ 2603.20176
- Paper：LagerNVS: Latent Geometry for Fully Neural Real-time Novel View Synthesis
- 一句话：LagerNVS 针对「提升泛化/跨场景/开放世界能力」，从「计算角度」切入，主要采用「Diffusion/生成先验/视频模型」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2603.20176](method_figures/2603.20176_LagerNVS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_LagerNVS_Latent_Geometry_for_Fully_Neural_Real_time_Novel_View_Synthesis_2603.20176.pdf
- Code：https://github.com/facebookresearch/lagernvs（code_link_found_not_audited）

#### 子问题：解决稀疏视角几何不稳定（4）
##### 解法族：Gaussian Splatting 表示与正则化（2）
###### 本文方法 ｜ 2604.05687
- Paper：3D Smoke Scene Reconstruction Guided by Vision Priors from Multimodal Large Language Models
- 一句话：本文方法 针对「解决稀疏视角几何不稳定」，从「计算角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2604.05687](method_figures/2604.05687_paper.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_3D_Smoke_Scene_Reconstruction_Guided_by_Vision_Priors_from_Multimodal_Large_Language_Model_2604.05687.pdf
###### WildSplatter ｜ 2604.21182
- Paper：WildSplatter: Feed-forward 3D Gaussian Splatting with Appearance Control from Unconstrained Images
- 一句话：WildSplatter 针对「解决稀疏视角几何不稳定」，从「计算角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2604.21182](method_figures/2604.21182_WildSplatter.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_WildSplatter_Feed_forward_3D_Gaussian_Splatting_with_Appearance_Control_from_Unconstrained_2604.21182.pdf
- Code：https://github.com/yfujimura/WildSplatter（code_link_found_not_audited）

##### 解法族：SLAM / pose graph / online mapping pipeline（2）
###### 本文方法 ｜ 2603.20428
- Paper：Benchmarking Efficient & Effective Camera Pose Estimation Strategies for Novel View Synthesis
- 一句话：本文方法 针对「解决稀疏视角几何不稳定」，从「计算角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2603.20428](method_figures/2603.20428_paper.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Benchmarking_Efficient_Effective_Camera_Pose_Estimation_Strategies_for_Novel_View_Synthesi_2603.20428.pdf
- Code：https://github.com/ubc-vision/image-matching-benchmark（code_link_found_not_audited）
###### 本文方法 ｜ 2601.19489
- Paper：Fast Converging 3D Gaussian Splatting for 1-Minute Reconstruction
- 一句话：本文方法 针对「解决稀疏视角几何不稳定」，从「计算角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2601.19489](method_figures/2601.19489_paper.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Fast_Converging_3D_Gaussian_Splatting_for_1_Minute_Reconstruction_2601.19489.pdf
- Code：https://github.com/j-alex-hanson/speedy-splat（code_link_found_not_audited）

#### 子问题：降低显存/存储/模型体积（1）
##### 解法族：Gaussian Splatting 表示与正则化（1）
###### OnlineX ｜ 2603.02134
- Paper：OnlineX: Unified Online 3D Reconstruction and Understanding with Active-to-Stable State Evolution
- 一句话：OnlineX 针对「降低显存/存储/模型体积」，从「计算角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2603.02134](method_figures/2603.02134_OnlineX.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_OnlineX_Unified_Online_3D_Reconstruction_and_Understanding_with_Active_to_Stable_State_Evo_2603.02134.pdf
- Code：https://github.com/xiac20/ScenePainter（code_link_found_not_audited）

### 切入点：训练/监督角度（37）
#### 子问题：提升几何一致性/表面质量（5）
##### 解法族：Feed-forward / Transformer / Foundation Model（2）
###### From None to All ｜ 2603.27455
- Paper：From None to All: Self-Supervised 3D Reconstruction via Novel View Synthesis
- 一句话：From None to All 针对「提升几何一致性/表面质量」，从「训练/监督角度」切入，主要采用「Feed-forward / Transformer / Foundation Model」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2603.27455](method_figures/2603.27455_From_None_to_All.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_From_None_to_All_Self_Supervised_3D_Reconstruction_via_Novel_View_Synthesis_2603.27455.pdf
- Code：https://github.com/ranrhuang/NAS3R（code_link_found_not_audited）
###### SEAR ｜ 2603.18774
- Paper：SEAR: Simple and Efficient Adaptation of Visual Geometric Transformers for RGB+Thermal 3D Reconstruction
- 一句话：SEAR 针对「提升几何一致性/表面质量」，从「训练/监督角度」切入，主要采用「Feed-forward / Transformer / Foundation Model」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2603.18774](method_figures/2603.18774_SEAR.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_SEAR_Simple_and_Efficient_Adaptation_of_Visual_Geometric_Transformers_for_RGB_Thermal_3D_R_2603.18774.pdf
- Code：https://www.github.com/Schindler-EPFL-Lab/SEAR（code_link_found_not_audited）

##### 解法族：Gaussian Splatting 表示与正则化（3）
###### BetterScene ｜ 2602.22596
- Paper：BetterScene: 3D Scene Synthesis with Representation-Aligned Generative Model
- 一句话：BetterScene 针对「提升几何一致性/表面质量」，从「训练/监督角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2602.22596](method_figures/2602.22596_BetterScene.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_BetterScene_3D_Scene_Synthesis_with_Representation_Aligned_Generative_Model_2602.22596.pdf
###### DOC-GS ｜ 2604.06739
- Paper：DOC-GS: Dual-Domain Observation and Calibration for Reliable Sparse-View Gaussian Splatting
- 一句话：DOC-GS 针对「提升几何一致性/表面质量」，从「训练/监督角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2604.06739](method_figures/2604.06739_DOC-GS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_DOC_GS_Dual_Domain_Observation_and_Calibration_for_Reliable_Sparse_View_Gaussian_Splatting_2604.06739.pdf
###### GeoNVS ｜ 2603.14965
- Paper：GeoNVS: Geometry Grounded Video Diffusion for Novel View Synthesis
- 一句话：GeoNVS 针对「提升几何一致性/表面质量」，从「训练/监督角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2603.14965](method_figures/2603.14965_GeoNVS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_GeoNVS_Geometry_Grounded_Video_Diffusion_for_Novel_View_Synthesis_2603.14965.pdf

#### 子问题：提升可控生成/世界演化预测（1）
##### 解法族：Gaussian Splatting 表示与正则化（1）
###### HY-World 2.0 ｜ 2604.14268
- Paper：HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds
- 一句话：HY-World 2.0 针对「提升可控生成/世界演化预测」，从「训练/监督角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2604.14268](method_figures/2604.14268_HY-World_2.0.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_HY_World_2_0_A_Multi_Modal_World_Model_for_Reconstructing_Generating_and_Simulating_3D_Wor_2604.14268.pdf
- Code：https://github.com/Tencent-Hunyuan/HY-World-2.0（code_link_found_not_audited）

#### 子问题：提升泛化/跨场景/开放世界能力（2）
##### 解法族：Feed-forward / Transformer / Foundation Model（1）
###### Scaling View Synthesis Transformers ｜ 2602.21341
- Paper：Scaling View Synthesis Transformers
- 一句话：Scaling View Synthesis Transformers 针对「提升泛化/跨场景/开放世界能力」，从「训练/监督角度」切入，主要采用「Feed-forward / Transformer / Foundation Model」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2602.21341](method_figures/2602.21341_Scaling_View_Synthesis_Transformers.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Scaling_View_Synthesis_Transformers_2602.21341.pdf

##### 解法族：Gaussian Splatting 表示与正则化（1）
###### Geometrically-Grounded ｜ 2601.22988
- Paper：Learning Geometrically-Grounded 3D Visual Representations for View-Generalizable Robotic Manipulation
- 一句话：Geometrically-Grounded 针对「提升泛化/跨场景/开放世界能力」，从「训练/监督角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2601.22988](method_figures/2601.22988_Geometrically-Grounded.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Learning_Geometrically_Grounded_3D_Visual_Representations_for_View_Generalizable_Robotic_M_2601.22988.pdf
- Code：https://github.com/RichardDuan-shandong/GEM3D（code_link_found_not_audited）

#### 子问题：解决稀疏视角几何不稳定（25）
##### 解法族：Feed-forward / Transformer / Foundation Model（1）
###### CAM3R ｜ 2603.22631
- Paper：CAM3R: Camera-Agnostic Model for 3D Reconstruction
- 一句话：CAM3R 针对「解决稀疏视角几何不稳定」，从「训练/监督角度」切入，主要采用「Feed-forward / Transformer / Foundation Model」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2603.22631](method_figures/2603.22631_CAM3R.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_CAM3R_Camera_Agnostic_Model_for_3D_Reconstruction_2603.22631.pdf
- Code：https://github.com/nam1410/cam3r（code_link_found_not_audited）

##### 解法族：Gaussian Splatting 表示与正则化（8；另有 5 篇见 full/csv）
###### AnyStyle ｜ 2602.04043
- Paper：AnyStyle: Single-Pass Multimodal Stylization for 3D Gaussian Splatting
- 一句话：AnyStyle 针对「解决稀疏视角几何不稳定」，从「训练/监督角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2602.04043](method_figures/2602.04043_AnyStyle.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_AnyStyle_Single_Pass_Multimodal_Stylization_for_3D_Gaussian_Splatting_2602.04043.pdf
- Code：https://github.com/joaxkal/AnyStyle（code_link_found_not_audited）
###### GSCompleter ｜ 2604.20155
- Paper：GSCompleter: A Distillation-Free Plugin for Metric-Aware 3D Gaussian Splatting Completion in Seconds
- 一句话：GSCompleter 针对「解决稀疏视角几何不稳定」，从「训练/监督角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2604.20155](method_figures/2604.20155_GSCompleter.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_GSCompleter_A_Distillation_Free_Plugin_for_Metric_Aware_3D_Gaussian_Splatting_Completion_i_2604.20155.pdf
###### GaussFly ｜ 2604.05062
- Paper：GaussFly: Contrastive Reinforcement Learning for Visuomotor Policies in 3D Gaussian Fields
- 一句话：GaussFly 针对「解决稀疏视角几何不稳定」，从「训练/监督角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2604.05062](method_figures/2604.05062_GaussFly.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_GaussFly_Contrastive_Reinforcement_Learning_for_Visuomotor_Policies_in_3D_Gaussian_Fields_2604.05062.pdf

##### 解法族：Motion decomposition / canonical space / deformation（1）
###### VGGT-HPE ｜ 2604.10106
- Paper：VGGT-HPE: Reframing Head Pose Estimation as Relative Pose Prediction
- 一句话：VGGT-HPE 针对「解决稀疏视角几何不稳定」，从「训练/监督角度」切入，主要采用「Motion decomposition / canonical space / deformation」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2604.10106](method_figures/2604.10106_VGGT-HPE.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_VGGT_HPE_Reframing_Head_Pose_Estimation_as_Relative_Pose_Prediction_2604.10106.pdf
- Code：https://github.com/VasilikiVas/vggt-hpe（code_link_found_not_audited）

##### 解法族：NeRF/辐射场/体渲染（1）
###### 本文方法 ｜ 2602.06488
- Paper：Rebenchmarking Unsupervised Monocular 3D Occupancy Prediction
- 一句话：本文方法 针对「解决稀疏视角几何不稳定」，从「训练/监督角度」切入，主要采用「NeRF/辐射场/体渲染」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2602.06488](method_figures/2602.06488_paper.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Rebenchmarking_Unsupervised_Monocular_3D_Occupancy_Prediction_2602.06488.pdf

##### 解法族：Pruning / compression / progressive coding（1）
###### Zero-1-to-3 ｜ 2303.11328
- Paper：Zero-1-to-3: Zero-shot One Image to 3D Object
- 一句话：Zero-1-to-3 针对「解决稀疏视角几何不稳定」，从「训练/监督角度」切入，主要采用「Pruning / compression / progressive coding」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2303.11328](method_figures/2303.11328_Zero-1-to-3.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2023_Zero_1_to_3_Zero_shot_One_Image_to_3D_Object_2303.11328.pdf
- Code：https://github.com/allenai/objaverse-rendering（code_link_found_not_audited）

##### 解法族：SLAM / pose graph / online mapping pipeline（12；另有 9 篇见 full/csv）
###### DROID-SLAM ｜ 2108.10869
- Paper：DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras
- 一句话：DROID-SLAM 针对「解决稀疏视角几何不稳定」，从「训练/监督角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2108.10869](method_figures/2108.10869_DROID-SLAM.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2022_DROID_SLAM_Deep_Visual_SLAM_for_Monocular_Stereo_and_RGB_D_Cameras_2108.10869.pdf
- Code：https://github.com/princeton-vl/DROID-SLAM（code_link_found_not_audited）
###### AirSplat ｜ 2603.25129
- Paper：AirSplat: Alignment and Rating for Robust Feed-Forward 3D Gaussian Splatting
- 一句话：AirSplat 针对「解决稀疏视角几何不稳定」，从「训练/监督角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2603.25129](method_figures/2603.25129_AirSplat.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_AirSplat_Alignment_and_Rating_for_Robust_Feed_Forward_3D_Gaussian_Splatting_2603.25129.pdf
- Code：https://github.com/nerfies/nerfies.github.io（code_link_found_not_audited）
###### Diff3R ｜ 2604.01030
- Paper：Diff3R: Feed-forward 3D Gaussian Splatting with Uncertainty-aware Differentiable Optimization
- 一句话：Diff3R 针对「解决稀疏视角几何不稳定」，从「训练/监督角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2604.01030](method_figures/2604.01030_Diff3R.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Diff3R_Feed_forward_3D_Gaussian_Splatting_with_Uncertainty_aware_Differentiable_Optimizati_2604.01030.pdf
- Code：https://github.com/nerfies/nerfies.github.io（code_link_found_not_audited）

##### 解法族：组合式/混合 pipeline（1）
###### Sim2Radar ｜ 2602.13314
- Paper：Sim2Radar: Toward Bridging the Radar Sim-to-Real Gap with VLM-Guided Scene Reconstruction
- 一句话：Sim2Radar 针对「解决稀疏视角几何不稳定」，从「训练/监督角度」切入，主要采用「组合式/混合 pipeline」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2602.13314](method_figures/2602.13314_Sim2Radar.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Sim2Radar_Toward_Bridging_the_Radar_Sim_to_Real_Gap_with_VLM_Guided_Scene_Reconstruction_2602.13314.pdf

#### 子问题：降低显存/存储/模型体积（4）
##### 解法族：Gaussian Splatting 表示与正则化（2）
###### GIFSplat ｜ 2602.22571
- Paper：GIFSplat: Generative Prior-Guided Iterative Feed-Forward 3D Gaussian Splatting from Sparse Views
- 一句话：GIFSplat 针对「降低显存/存储/模型体积」，从「训练/监督角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2602.22571](method_figures/2602.22571_GIFSplat.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_GIFSplat_Generative_Prior_Guided_Iterative_Feed_Forward_3D_Gaussian_Splatting_from_Sparse_2602.22571.pdf
###### One-Shot Refiner ｜ 2601.14161
- Paper：One-Shot Refiner: Boosting Feed-forward Novel View Synthesis via One-Step Diffusion
- 一句话：One-Shot Refiner 针对「降低显存/存储/模型体积」，从「训练/监督角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2601.14161](method_figures/2601.14161_One-Shot_Refiner.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_One_Shot_Refiner_Boosting_Feed_forward_Novel_View_Synthesis_via_One_Step_Diffusion_2601.14161.pdf

##### 解法族：SLAM / pose graph / online mapping pipeline（2）
###### From Rays to Projections ｜ 2601.05116
- Paper：From Rays to Projections: Better Inputs for Feed-Forward View Synthesis
- 一句话：From Rays to Projections 针对「降低显存/存储/模型体积」，从「训练/监督角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2601.05116](method_figures/2601.05116_From_Rays_to_Projections.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_From_Rays_to_Projections_Better_Inputs_for_Feed_Forward_View_Synthesis_2601.05116.pdf
###### VGG-T$^3$ ｜ 2602.23361
- Paper：VGG-T$^3$: Offline Feed-Forward 3D Reconstruction at Scale
- 一句话：VGG-T$^3$ 针对「降低显存/存储/模型体积」，从「训练/监督角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「稀疏/单目/少视角 3D 重建」。
- Method diagram：![2602.23361](method_figures/2602.23361_VGG-T_3.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_VGG_T_3_Offline_Feed_Forward_3D_Reconstruction_at_Scale_2602.23361.pdf

## Motivation：领域/传感器特化重建（9）
### 切入点：数据/传感角度（1）
#### 子问题：适配特殊传感器/行业场景（1）
##### 解法族：Sensor/domain-specific pipeline（1）
###### NAS-GS ｜ 2601.06285
- Paper：NAS-GS: Noise-Aware Sonar Gaussian Splatting
- 一句话：NAS-GS 针对「适配特殊传感器/行业场景」，从「数据/传感角度」切入，主要采用「Sensor/domain-specific pipeline」来服务「领域/传感器特化重建」。
- Method diagram：![2601.06285](method_figures/2601.06285_NAS-GS.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_NAS_GS_Noise_Aware_Sonar_Gaussian_Splatting_2601.06285.pdf
- Code：https://github.com/SenseRoboticsLab/NAS-GS（code_link_found_not_audited）

### 切入点：时空/动态角度（1）
#### 子问题：适配特殊传感器/行业场景（1）
##### 解法族：Sensor/domain-specific pipeline（1）
###### Sonar-MASt3R ｜ 2603.13585
- Paper：Sonar-MASt3R: Real-Time Opti-Acoustic Fusion in Turbid, Unstructured Environments
- 一句话：Sonar-MASt3R 针对「适配特殊传感器/行业场景」，从「时空/动态角度」切入，主要采用「Sensor/domain-specific pipeline」来服务「领域/传感器特化重建」。
- Method diagram：![2603.13585](method_figures/2603.13585_Sonar-MASt3R.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Sonar_MASt3R_Real_Time_Opti_Acoustic_Fusion_in_Turbid_Unstructured_Environments_2603.13585.pdf

### 切入点：表示/几何角度（4）
#### 子问题：解决稀疏视角几何不稳定（1）
##### 解法族：NeRF/辐射场/体渲染（1）
###### 本文方法 ｜ 2602.16713
- Paper：Three-dimensional Damage Visualization of Civil Structures via Gaussian Splatting-enabled Digital Twins
- 一句话：本文方法 针对「解决稀疏视角几何不稳定」，从「表示/几何角度」切入，主要采用「NeRF/辐射场/体渲染」来服务「领域/传感器特化重建」。
- Method diagram：![2602.16713](method_figures/2602.16713_paper.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Three_dimensional_Damage_Visualization_of_Civil_Structures_via_Gaussian_Splatting_enabled_2602.16713.pdf
- Code：https://github.com/readthedocs/sphinx_rtd_theme（code_link_found_not_audited）

#### 子问题：适配特殊传感器/行业场景（3）
##### 解法族：Gaussian Splatting 表示与正则化（1）
###### Arbitrary-Scale ｜ 2604.17727
- Paper：Voronoi-guided Bilateral 2D Gaussian Splatting for Arbitrary-Scale Hyperspectral Image Super-Resolution
- 一句话：Arbitrary-Scale 针对「适配特殊传感器/行业场景」，从「表示/几何角度」切入，主要采用「Gaussian Splatting 表示与正则化」来服务「领域/传感器特化重建」。
- Method diagram：![2604.17727](method_figures/2604.17727_Arbitrary-Scale.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Voronoi_guided_Bilateral_2D_Gaussian_Splatting_for_Arbitrary_Scale_Hyperspectral_Image_Sup_2604.17727.pdf

##### 解法族：NeRF/辐射场/体渲染（2）
###### CropNeRF ｜ 2601.00207
- Paper：CropNeRF: A Neural Radiance Field-Based Framework for Crop Counting
- 一句话：CropNeRF 针对「适配特殊传感器/行业场景」，从「表示/几何角度」切入，主要采用「NeRF/辐射场/体渲染」来服务「领域/传感器特化重建」。
- Method diagram：![2601.00207](method_figures/2601.00207_CropNeRF.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_CropNeRF_A_Neural_Radiance_Field_Based_Framework_for_Crop_Counting_2601.00207.pdf
- Code：https://github.com/robotic-vision-lab/CropNeRF-A-Neural-Radiance-Field-Based-Framework（code_link_found_not_audited）
###### Neural Brain Fields ｜ 2601.00012
- Paper：Neural Brain Fields: A NeRF-Inspired Approach for Generating Nonexistent EEG Electrodes
- 一句话：Neural Brain Fields 针对「适配特殊传感器/行业场景」，从「表示/几何角度」切入，主要采用「NeRF/辐射场/体渲染」来服务「领域/传感器特化重建」。
- Method diagram：![2601.00012](method_figures/2601.00012_Neural_Brain_Fields.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2025_Neural_Brain_Fields_A_NeRF_Inspired_Approach_for_Generating_Nonexistent_EEG_Electrodes_2601.00012.pdf
- Code：https://github.com/Shaharak88/neural-brain-fields（code_link_found_not_audited）

### 切入点：计算角度（1）
#### 子问题：适配特殊传感器/行业场景（1）
##### 解法族：SLAM / pose graph / online mapping pipeline（1）
###### VISO ｜ 2601.01144
- Paper：VISO: Robust Underwater Visual-Inertial-Sonar SLAM with Photometric Rendering for Dense 3D Reconstruction
- 一句话：VISO 针对「适配特殊传感器/行业场景」，从「计算角度」切入，主要采用「SLAM / pose graph / online mapping pipeline」来服务「领域/传感器特化重建」。
- Method diagram：![2601.01144](method_figures/2601.01144_VISO.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_VISO_Robust_Underwater_Visual_Inertial_Sonar_SLAM_with_Photometric_Rendering_for_Dense_3D_2601.01144.pdf

### 切入点：训练/监督角度（2）
#### 子问题：提升几何一致性/表面质量（1）
##### 解法族：Sensor/domain-specific pipeline（1）
###### Inter-Slice ｜ 2602.04162
- Paper：Improving 2D Diffusion Models for 3D Medical Imaging with Inter-Slice Consistent Stochasticity
- 一句话：Inter-Slice 针对「提升几何一致性/表面质量」，从「训练/监督角度」切入，主要采用「Sensor/domain-specific pipeline」来服务「领域/传感器特化重建」。
- Method diagram：![2602.04162](method_figures/2602.04162_Inter-Slice.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Improving_2D_Diffusion_Models_for_3D_Medical_Imaging_with_Inter_Slice_Consistent_Stochasti_2602.04162.pdf
- Code：https://github.com/duchenhe/ISCS（code_link_found_not_audited）

#### 子问题：解决稀疏视角几何不稳定（1）
##### 解法族：NeRF/辐射场/体渲染（1）
###### LWIR ｜ 2603.05473
- Paper：Towards 3D Scene Understanding of Gas Plumes in LWIR Hyperspectral Images Using Neural Radiance Fields
- 一句话：LWIR 针对「解决稀疏视角几何不稳定」，从「训练/监督角度」切入，主要采用「NeRF/辐射场/体渲染」来服务「领域/传感器特化重建」。
- Method diagram：![2603.05473](method_figures/2603.05473_LWIR.png)
- PDF：/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26/pdfs/2026_Towards_3D_Scene_Understanding_of_Gas_Plumes_in_LWIR_Hyperspectral_Images_Using_Neural_Rad_2603.05473.pdf
- Code：https://github.com/lanl/HSI-Nerfstudio（code_link_found_not_audited）
