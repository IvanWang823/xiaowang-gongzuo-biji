# GEFCom 数据集与基准参考（光伏 / 风电直接对口）

> 来源说明：原始素材来自公众号「优化算法侠」2024-01-08 的转载文（内容本质为 GEFCom 维基 + 一堆优化算法广告，文章本身质量低、非同行评审）。但其披露的 **GEFCom 数据集结构与三篇奠基论文均为真实可查证**（IEEE WGEF 主办、*International Journal of Forecasting* 出版），故提纯落库，作为本项目的**学术基准数据源**与**文献库补强**。
> 边界：本文件为数据集/基准索引，不进入"工程实践素材"分类；其引用的 3 篇论文为同行评审，已补入 `../02_论文文献/文献清单.md` #14–#16。

---

## 一、GEFCom 是什么（与项目关系）

Global Energy Forecasting Competition（全球能源预测竞赛），由 IEEE 电力系统能源预测工作组（WGEF）组织，旨在建立能源预测的**公开基准数据集**，让不同研究组的结果可复现、可横向比较。

**与本项目直接对口**：GEFCom 系列中 **GEFCom2014 同时设有风电（W）与光伏（S）两条赛道**，是学界光伏/风电功率预测最权威的标准基准；GEFCom2012 也含风电赛道。项目论文辅助反复引用"GEFCom 基准"，但此前文献清单里**缺这三篇最权威的奠基论文**——本文与文献清单 #14–#16 一并补齐。

---

## 二、各届数据集结构与对口性

### GEFCom2012（双赛道：层级负荷 + 风电）
- **风电赛道数据**：7 个风电场逐时功率
  - `train`：2009-07-01 ～ 2010-12-31（训练，无缺口，除非数据质量问题）
  - `test`：2011-01-01 ～ 2012-06-28（测试）
  - `windforecasts_wf1–wf7`：同期风电预报，每 12 h 发布一次、预报范围 48 h、时间分辨率 1 h
  - `benchmark`：7 个风电场逐时功率基准预测
- **对口性**：风电功率预测基准（点对点 / 序列预测）。

### GEFCom2014（四赛道：负荷 / 电价 / 风电 / 光伏）
解压后含 `Instructions.txt` + 15 个子文件夹（Task n：Ln-train.csv + Ln-benchmark.csv）。
- **风电赛道 GEFCom2014-W**：澳大利亚 10 个风电场、24 h 预测；特征含**风矢量东西/南北分量 u、v**（即经纬向风分量投影）。
- **光伏赛道 GEFCom2014-S**：澳大利亚某区域 3 座光伏电站、未来 24 h 预测；特征含 **ECMWF 提供的 12 个气象变量**。
- **对口性**：⭐⭐⭐ 项目两大主题（光伏 + 风电）的**标准学术基准**，方法论文（如文献清单 #8–#13）多数以 GEFCom2014-W/S 做验证集。

### GEFCom2017（层级概率负荷预测）
- 数据：ISONE 区域（8 个负荷区 + 州级 + 系统级）共 10 条时间序列；持续更新至 2023 年（ISO-NE 官网开放下载）。
- **对口性**：偏负荷预测，与本项目关联弱；仅作"概率预测竞赛方法论"背景（与文献 #7 Pinson&Girard、#11 Bazionis 概率预测呼应）。

---

## 三、三篇奠基论文（已核实 DOI，可直引）

| 论文 | 期刊 | DOI | 覆盖赛事 |
| :--- | :--- | :--- | :--- |
| Hong, Pinson, Fan (2014). *Global Energy Forecasting Competition 2012* | *Int. J. Forecasting* 30(2):357–363 | 10.1016/j.ijforecast.2013.07.001 | GEFCom2012（含风电赛道） |
| Hong, Pinson, Fan, Zareipour, Troccoli, Hyndman (2016). *Probabilistic energy forecasting: GEFCom2014 and beyond* | *Int. J. Forecasting* 32(3):896–913 | 10.1016/j.ijforecast.2016.02.001 | GEFCom2014（四赛道：负荷/电价/风电/光伏，581 队 61 国） |
| Hong, Xie, Black (2019). *Global energy forecasting competition 2017: Hierarchical probabilistic load forecasting* | *Int. J. Forecasting* 35(4):1389–1399 | 10.1016/j.ijforecast.2019.02.006 | GEFCom2017 |

> 以上三篇均为主办方权威综述，数据集随论文一并公开（benchmark data pool），是引用"本项目以 GEFCom 为基准"时**最该引的原始出处**。

---

## 四、本项目落点建议

1. **方法验证**：本项目光伏/风电模型若需对标学界，优先用 GEFCom2014-S / GEFCom2014-W 作外部验证集（已有公开 benchmark 与冠军方案可对照）。
2. **文献引用**：汇报"基准来源"时引 #14–#16（本清单），而非只写"GEFCom"——把抽象基准落成可查证的同行评审出处。
3. **数据治理呼应**：GEFCom2012 原文即把"数据清洗（data cleansing）"列为竞赛核心挑战之一，与申威睿思"数据质量治理"、清徕美"标签污染三概念解耦"形成跨来源呼应。

---

## 五、获取途径（公开）
- GEFCom2012/2014 数据集与说明随上述 IJF 论文公开；检索 DOI 即可定位出版社页面与补充材料。
- GEFCom2017 持续更新数据：ISO-NE 官网 `iso-ne.com` → Load and Demand → Zone Info（2011–2023）。
