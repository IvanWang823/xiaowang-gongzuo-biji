# xiaowang-gongzuo-biji

🌐 English version: [README_EN.md](README_EN.md)

> AI 数据分析案例集 · 电力新能源 / 煤炭 / 海运 / 理财 + AI 入门教程 + AI 编程教程 + AIGC 创作实战
> 作者：抖音「小王工作笔记」（ID: 163277992）

## 简介

本仓库是 AI 辅助数据分析与编程的**方法 / 思路沉淀**，不含原始数据与最终产出图表，便于复用与分享。

## 目录结构

```
xiaowang-gongzuo-biji/
├── README.md / README_EN.md
├── assets/                    # 公共素材
│   └── donate/                # 打赏码（支付宝）
├── ai-data-analysis/          # 数据分析案例（思路 / 方法）
│   ├── 光伏风电出力预测
│   ├── 如何用AI分析上网侧电价
│   ├── 弃风弃光率
│   ├── 海运价格分析
│   ├── 煤炭价格分析
│   └── 理财分析
├── ai-getting-started/        # AI 入门内容
│   ├── 01_教程文档/          # 如何用AI做数据分析
│   └── AI写小说思路文字稿.md
├── ai-programming-tutorials/  # AI 编程教程
│   └── 01~06 课件（Markdown喂AI / 工作流 / SQL / 前端 / 后端 / 测试审查）
└── aigc-getting-started/      # AIGC 创作实战
    └── 汽车视频/            # 汽车短视频分镜与素材
        ├── 汽车视频制作总表.xlsx   # 分镜总表（镜头编号 / 分镜图 / AI 提示词 / 时长 / 状态）
        └── 分镜图/                # 9 张分镜素材图
```

## 内容说明

### ai-data-analysis（数据分析案例）

| 案例 | 内容 |
| --- | --- |
| 光伏风电出力预测 | 风光电出力预测的分析思路 |
| 如何用AI分析上网侧电价 | 上网侧（发电侧）电价数据分析思路 |
| 弃风弃光率 | 弃风弃光率分析流程 |
| 海运价格分析 | 海运价格分析思路 |
| 煤炭价格分析 | 煤炭价格分析框架与手册 |
| 理财分析 | 理财分析工作流文档 |

### ai-getting-started（AI 入门）

- `01_教程文档/`：如何用 AI 做数据分析（教程文档）
- `AI写小说思路文字稿.md`：用 AI 写小说的方法论文字稿

### ai-programming-tutorials（AI 编程教程）

AI 辅助编程系列课件（详见模块内 README）：

| 课时 | 内容 |
| --- | --- |
| 01 | 为何用 Markdown 喂 AI |
| 02 | 为何要创建 AI 工作流 |
| 03 | AI 生成 SQL 脚本 |
| 04 | AI 生成前端网页实战 |
| 05 | AI 生成后端代码 |
| 06 | 测试与审查 |

### aigc-getting-started（AIGC 创作实战）

- `汽车视频/`：汽车短视频创作素材
  - `汽车视频制作总表.xlsx`：分镜总表（Sheet「分镜表」），字段含「镜头编号、内容描述、分镜图、分镜视频、AI 提示词、时长、状态」，用于规划汽车短视频的分镜与 AI 生成提示词
  - `分镜图/`：9 张分镜素材图（`车身` `车尾` `汽车logo` `前轮毂` `后轮毂` `左大灯` `右大灯` `车方向盘` `车内饰`）

## 打赏支持

如果这个仓库对你有帮助，可以扫码请我喝杯咖啡 ☕ 打赏完全自愿，不影响任何内容的免费使用。

<img src="assets/donate/alipay.jpg" alt="支付宝打赏码" width="240">

---

## 说明

- `ai-data-analysis/` 与 `ai-getting-started/` 仅保留分析思路 / 方法类内容，不含原始数据与最终产出图表。
- `ai-programming-tutorials/` 为 AI 编程教程栏目，收纳「用 AI 做编程」系列课件（Markdown 喂 AI / AI 工作流 / SQL / 前端 / 后端 / 测试审查）。
- `aigc-getting-started/` 为 AIGC 创作实战栏目，收纳创作素材（如汽车短视频分镜图与分镜总表），便于直接复用。
- 库名 `xiaowang-gongzuo-biji` 对应作者的抖音账号「小王工作笔记」。

## 更新日志

> 按更新日期倒序记录每次变动，便于追溯。

### 2026-09-22
- `ai-programming-tutorials/` 新增补充资料 `如何基于ima创建AI智能客服系统.html`
- 新增「打赏支持」区块与支付宝打赏码 `assets/donate/alipay.jpg`
- `ai-programming-tutorials/` 新增补充资料 `向量数据库.html`

### 2026-09-21
- 新增 `ai-programming-tutorials/` 模块（与 `ai-data-analysis` 平级），纳入 AI 编程第一~六课课件：
  - 01 为何用 Markdown 喂 AI
  - 02 为何要创建 AI 工作流
  - 03 AI 生成 SQL 脚本
  - 04 AI 生成前端网页实战
  - 05 AI 生成后端代码
  - 06 测试与审查
