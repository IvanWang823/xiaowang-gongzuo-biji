# -*- coding: utf-8 -*-
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.chart import PieChart, BarChart, Reference
from collections import defaultdict
import os

# ============ 路径配置（跨设备 · v2.0）============
# 默认 Windows 路径；云端/macOS/Linux 用环境变量覆盖：FINANCE_PATH=/your/path
BASE_PATH = os.getenv("FINANCE_PATH", "F:/理财分析")
OUT_FILE = os.path.join(BASE_PATH, "04_成果", "四平台理财持仓分析.xlsx")

# ============ 汇率（2026-08-27）============
rate_now = 6.7225       # 在岸/实时即期
rate_mid = 6.7840       # 央行中间价
rate_year_ago = 7.1560  # 一年前

# ============ 中国银行 · 美元理财（币种：美元 USD）============
# 字段：序号, 产品名称, 发行方, 币种, 参考市值(美元), 最新收益(美元), 持仓收益(美元), 到期日, 类型
rows = [
    (1, "和鼎美元封闭165号(QDII)-汇",                   "招银理财",   "美元/汇", 7031.90,  4.90,  32.90, "2027-02-01",        "封闭式"),
    (2, "贝远稳航美元封闭第29期",                       "贝莱德建信", "美元/汇", 7050.32,  4.79,  51.32, "2027-06-02",        "封闭式"),
    (3, "全球配置高评级美元封闭2649",                   "中银理财",   "美元/汇", 7064.95,  4.66,  65.94, "2026-10-13",        "封闭式"),
    (4, "（尊享）全球配置高评级美元1个月最短持有期-汇", "中银理财",   "美元/汇", 16000.00, 1.60,  91.24, "未显示",            "开放式"),
    (5, "QDII日计划（美元版）-汇",                      "中银理财",   "美元/汇", 16000.00, 1.44, 443.85, "未显示(活期类)",    "开放式"),
]
total_mv_usd = round(sum(r[4] for r in rows), 2)          # 53147.17 USD
total_profit_usd = round(sum(r[6] for r in rows), 2)      # 685.25 USD
total_mv_cny = round(total_mv_usd * rate_now, 2)          # ≈ 357282 元
total_profit_cny = round(total_profit_usd * rate_now, 2)  # ≈ 4606 元

# ============ 招商银行（币种：人民币 CNY）============
funds = [
    (1, "周周享",                          2233.60,   0.00,     8.91,    "+0.40%",  "货币/短债"),
    (2, "富国亚洲收益债券(QDII)人民币A",    1733.58,  -0.16,   -25.32,   "-1.44%",  "QDII债券"),
    (3, "景顺长城景颐裕利债券C(定投)",      1637.87,   1.44,    12.87,   "+0.79%",  "纯债"),
    (4, "富国中证港股通互联网ETF发起式联接C",1189.25,   9.06,  -540.75,  "-31.26%", "指数联接"),
    (5, "摩根日本精选股票(QDII)A",          824.29,   2.19,    53.63,   "+6.96%",  "QDII股票"),
    (6, "富国恒生港股通高股息低波动ETF联接A",520.07,  -0.33,    -9.20,   "-1.74%",  "指数联接"),
]
total_fund_mv = round(sum(f[2] for f in funds), 2)
total_fund_profit = round(sum(f[4] for f in funds), 2)

licai = [
    (1, "月月宝（多宝理财）",                        4721.53,   22.53,  "可申赎(今日)",        "1.95%(近1年)"),
    (2, "半年宝（多宝理财）",                       10101.01,  101.01,  "可申赎(今日)",        "1.79%(近1年)"),
    (3, "多月宝（多宝理财）",                       50065.00,   65.00,  "2027-02-17到期",      "2.00%-2.30%(近1年)"),
    (4, "光大理财阳光金创利稳健乐享日开14天D",       10015.04,   87.27,  "可申赎(每日)",        "2.36%(成立以来)"),
    (5, "交银理财灵动聚利日开6号180天持有期(JY04)", 30080.91,   81.91,  "最近可赎日2027-01-28", "6.24%(成立以来)"),
]
total_lc_mv = round(sum(l[2] for l in licai), 2)
total_lc_profit = round(sum(l[3] for l in licai), 2)

cmb_total_mv = round(total_fund_mv + total_lc_mv, 2)
cmb_total_profit = round(total_fund_profit + total_lc_profit, 2)

# ============ 建设银行（币种：人民币 CNY）============
ccb_funds = [
    (1, "华夏纯债债券C",          "000016",   2456.11, -0.41,   43.65,  "+1.78%", "纯债"),
    (2, "建信现金添益A",           "003022",   2740.80,  0.09,   44.90,  "+1.64%", "货币"),
    (3, "华夏聚嘉优选三个月持有",  "018915",   2198.02,  0.39,   -1.98,  "-0.09%", "持有期固收"),
    (4, "南方亚洲美元债C",         "002401",   3695.13,  8.83, -102.76,  "-2.78%", "QDII美元债"),
    (5, "建信沪深300A",           "165310",    102.23,  0.73,    2.23,  "+2.18%", "指数基金"),
]
ccb_total_fund_mv = round(sum(f[3] for f in ccb_funds), 2)
ccb_total_fund_profit = round(sum(f[5] for f in ccb_funds), 2)

ccb_licai = [
    (1, "浦银理财多季鑫封闭式113号（元旦专享）", 10145.12, 145.12, "2026-09-28到期", "未提供"),
]
ccb_total_lc_mv = round(sum(l[2] for l in ccb_licai), 2)
ccb_total_lc_profit = round(sum(l[3] for l in ccb_licai), 2)

ccb_total_mv = round(ccb_total_fund_mv + ccb_total_lc_mv, 2)
ccb_total_profit = round(ccb_total_fund_profit + ccb_total_lc_profit, 2)

grand_total_mv = round(total_mv_cny + cmb_total_mv + ccb_total_mv, 2)
grand_total_profit = round(total_profit_cny + cmb_total_profit + ccb_total_profit, 2)

# ============ 支付宝（币种：人民币 CNY）============
# --- 帮你投策略组合 ---
alipay_strategy = [
    (1, "7日理财+",           1764.43,   0.03,   13.97),
    (2, "全球精选50",         2456.82,   7.27,   68.76),
    (3, "全球精选20",         1017.79,   1.22,   17.76),
    (4, "定活理财|360天",     1003.43,   0.28,    3.44),
    (5, "全球精选100",        2300.57,   9.33,  117.21),
    (6, "股票基金选70",       2642.30,   8.45,    2.95),
]
alipay_strat_mv = round(sum(s[2] for s in alipay_strategy), 2)
alipay_strat_profit = round(sum(s[4] for s in alipay_strategy), 2)

# --- 基金持仓 ---
alipay_funds = [
    (1, "华宝核心优势灵活配置混合A",              2004.38,  20.74,  250.78, "+14.30%", "混合/定投"),
    (2, "中欧数字经济混合A",                       761.58,   3.95,   29.68, "+4.05%",  "混合"),
    (3, "嘉实美国成长股票(QDII)",                 1752.16,  11.77,   92.72, "+5.59%",  "QDII美股"),
    (4, "广发纳斯达克100ETF联接(QDII)A",          560.60,   3.51,   60.64, "+12.13%", "QDII指数"),
    (5, "招商信用添利债券(LOF)A",                3863.65,   1.81,   47.97, "+1.26%",  "债券/定投"),
    (6, "华宝纳斯达克精选股票(QDII)A",           1113.83,  20.37,   26.34, "+2.42%",  "QDII美股"),
    (7, "长城收益宝货币A",                         2431.91,   0.08,   12.30, "+0.51%",  "货币/定投"),
    (8, "长城短债债券A",                          1914.91,   0.00,   19.03, "+1.00%",  "短债/定投"),
    (9, "长城稳健增利债券C",                      2084.75,  -0.28,   21.46, "+1.04%",  "债券/定投"),
    (10, "长城中证港通高股息投资指数(QDII)C",     1098.57,  28.55,   28.55, "+2.67%",  "QDII港股"),
    (11, "长城中证A500指数C",                     1252.11,   9.12,   36.63, "+3.01%",  "指数/定投"),
    (12, "天弘中证全指证券公司ETF联接C",          2863.64,  72.96, -251.32, "-8.07%",  "指数/目标投"),
    (13, "中银美元债债券(QDII)A",                6382.08,  14.85, -117.92, "-1.81%",  "QDII美元债/定投"),
    (14, "中银国有企业债券C",                     2351.99,   0.75,   20.99, "+0.90%",  "债券/定投"),
    (15, "富国亚洲收益债券(QDII)A",               3377.76,   2.88,  -41.42, "-1.21%",  "QDII亚债"),
]
alipay_fund_mv = round(sum(f[2] for f in alipay_funds), 2)
alipay_fund_profit = round(sum(f[4] for f in alipay_funds), 2)

alipay_total_mv = round(alipay_strat_mv + alipay_fund_mv, 2)
alipay_total_profit = round(alipay_strat_profit + alipay_fund_profit, 2)

grand_total_mv_all = round(total_mv_cny + cmb_total_mv + ccb_total_mv + alipay_total_mv, 2)
grand_total_profit_all = round(total_profit_cny + cmb_total_profit + ccb_total_profit + alipay_total_profit, 2)

wb = openpyxl.Workbook()

# ============ Sheet1: 中行美元理财 ============
ws = wb.active
ws.title = "中行美元理财"
ws["A1"] = "中国银行 · 美元理财持仓明细"
ws["A1"].font = Font(size=14, bold=True, color="1F4E79")
ws["A2"] = f"数据来源：中国银行APP持仓截图 IMG_1412.PNG ｜ 统计日 2026-08-27 ｜ 币种：美元(USD) ｜ 按即期{rate_now}折算人民币≈{total_mv_cny:,.0f}元"
ws["A2"].font = Font(size=9, color="808080")

headers = ["序号", "产品名称", "发行方", "币种", "参考市值(美元)", "最新收益(美元)",
           "持仓收益(美元)", "到期日", "类型"]
hrow = 4
for c, h in enumerate(headers, 1):
    cell = ws.cell(row=hrow, column=c, value=h)
    cell.font = Font(bold=True, color="FFFFFF")
    cell.fill = PatternFill("solid", fgColor="1F4E79")
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

r_start = hrow + 1
for i, r in enumerate(rows):
    rr = r_start + i
    for c, v in enumerate(r, 1):
        cell = ws.cell(row=rr, column=c, value=v)
        cell.alignment = Alignment(horizontal="center" if c in (1, 4, 5, 6, 7, 8, 9) else "left", vertical="center")
        if c in (6, 7):
            cell.font = Font(color="C00000")
        if c == 5:
            cell.number_format = '#,##0.00'
        if c in (6, 7):
            cell.number_format = '#,##0.00'

rr_total = r_start + len(rows)
ws.cell(row=rr_total, column=1, value="合计").font = Font(bold=True)
ws.cell(row=rr_total, column=2, value=f"共{len(rows)}只产品").font = Font(bold=True)
tc1 = ws.cell(row=rr_total, column=5, value=total_mv_usd)
tc1.number_format = '#,##0.00'; tc1.font = Font(bold=True)
tc2 = ws.cell(row=rr_total, column=7, value=total_profit_usd)
tc2.number_format = '#,##0.00'; tc2.font = Font(bold=True, color="C00000")

thin = Side(style="thin", color="BFBFBF")
border = Border(left=thin, right=thin, top=thin, bottom=thin)
for rr in range(hrow, rr_total + 1):
    for c in range(1, len(headers) + 1):
        ws.cell(row=rr, column=c).border = border

for c, w in enumerate([6, 38, 12, 9, 16, 16, 16, 18, 10], 1):
    ws.column_dimensions[openpyxl.utils.get_column_letter(c)].width = w

pie = PieChart()
pie.title = "各产品参考市值占比(美元)"
data = Reference(ws, min_col=5, min_row=hrow, max_row=r_start + len(rows) - 1)
cats = Reference(ws, min_col=2, min_row=r_start, max_row=r_start + len(rows) - 1)
pie.add_data(data, titles_from_data=True)
pie.set_categories(cats)
pie.height = 8; pie.width = 13
ws.add_chart(pie, "A12")

bar = BarChart()
bar.title = "各产品持仓收益(美元)"
bdata = Reference(ws, min_col=7, min_row=hrow, max_row=r_start + len(rows) - 1)
bar.add_data(bdata, titles_from_data=True)
bar.set_categories(cats)
bar.height = 8; bar.width = 13
bar.y_axis.title = "美元"
ws.add_chart(bar, "H12")

# ============ Sheet2: 汇总分析 ============
ws2 = wb.create_sheet("汇总分析")
ws2["A1"] = "汇总分析"; ws2["A1"].font = Font(size=14, bold=True, color="1F4E79")

ws2["A3"] = "「待补充字段清单」（交付前请核对，v2.5）"; ws2["A3"].font = Font(bold=True, size=12, color="B8860B")
pending = [
    "1. 建设银行 · 浦银理财多季鑫封闭式113号（元旦专享）：参考年化未提供（建行APP截图未显示），已标 年化N/A。",
]
for i, t in enumerate(pending):
    ws2.cell(row=4 + i, column=1, value=t)

row_boc = 4 + len(pending) + 2
ws2.cell(row=row_boc, column=1, value="一、中国银行美元理财").font = Font(bold=True, size=12)
boc = [
    ("产品数量", f"{len(rows)} 只"),
    ("总参考市值(美元)", f"{total_mv_usd:,.2f} USD"),
    ("总参考市值(人民币)", f"≈{total_mv_cny:,.0f} 元 (按即期{rate_now})"),
    ("总持仓收益(美元)", f"+{total_profit_usd:,.2f} USD"),
    ("总持仓收益(人民币)", f"≈+{total_profit_cny:,.0f} 元"),
    ("币种结构", "100% 美元/汇"),
    ("最近到期", "全球配置高评级美元封闭2649（2026-10-13）"),
]
for i, (k, v) in enumerate(boc):
    ws2.cell(row=row_boc + 1 + i, column=1, value=k).font = Font(bold=True)
    ws2.cell(row=row_boc + 1 + i, column=2, value=v)

row0 = row_boc + 1 + len(boc) + 2
ws2.cell(row=row0, column=1, value="按发行方汇总(美元)").font = Font(bold=True, size=12)
issuer = defaultdict(lambda: [0, 0.0, 0.0])
for r in rows:
    issuer[r[2]][0] += 1; issuer[r[2]][1] += r[4]; issuer[r[2]][2] += r[6]
for ci, h in enumerate(["发行方", "只数", "市值(USD)", "持仓收益(USD)"], 1):
    ws2.cell(row=row0 + 1, column=ci, value=h).font = Font(bold=True)
for i, (k, v) in enumerate(issuer.items()):
    ws2.cell(row=row0 + 2 + i, column=1, value=k)
    ws2.cell(row=row0 + 2 + i, column=2, value=v[0])
    ws2.cell(row=row0 + 2 + i, column=3, value=round(v[1], 2)).number_format = '#,##0.00'
    ws2.cell(row=row0 + 2 + i, column=4, value=round(v[2], 2)).number_format = '#,##0.00'

typ = defaultdict(lambda: [0, 0.0, 0.0])
for r in rows:
    typ[r[8]][0] += 1; typ[r[8]][1] += r[4]; typ[r[8]][2] += r[6]
row1 = row0 + 2 + len(issuer) + 2
ws2.cell(row=row1, column=1, value="按类型汇总(美元)").font = Font(bold=True, size=12)
for ci, h in enumerate(["类型", "只数", "市值(USD)", "持仓收益(USD)"], 1):
    ws2.cell(row=row1 + 1, column=ci, value=h).font = Font(bold=True)
for i, (k, v) in enumerate(typ.items()):
    ws2.cell(row=row1 + 2 + i, column=1, value=k)
    ws2.cell(row=row1 + 2 + i, column=2, value=v[0])
    ws2.cell(row=row1 + 2 + i, column=3, value=round(v[1], 2)).number_format = '#,##0.00'
    ws2.cell(row=row1 + 2 + i, column=4, value=round(v[2], 2)).number_format = '#,##0.00'

obs_row = row1 + 2 + len(typ) + 2
ws2.cell(row=obs_row, column=1, value="客观观察（不含投资建议）").font = Font(bold=True, size=12)
obs = [
    "1. 全部为美元/汇产品，合计市值约 %s 美元（≈%s 元人民币），累计持仓收益 +%s 美元（≈+%s 元）。" % (f"{total_mv_usd:,.2f}", f"{total_mv_cny:,.0f}", f"{total_profit_usd:,.2f}", f"{total_profit_cny:,.0f}"),
    "2. 封闭式 3 只单日收益 +4.66~+4.90 美元，明显高于开放式 2 只（+1.44~+1.60 美元）。",
    "3. QDII日计划(美元版)累计持仓收益最高（+443.85），推测持有最久、滚动收益累积。",
    "4. 中银理财占 3 只、市值约 %.1f%%，为单一最大发行方，集中度偏高。" % (issuer["中银理财"][1] / total_mv_usd * 100),
    "5. 最近到期：全球配置高评级美元封闭2649，2026-10-13。",
    "6. 注：市值/收益均为美元计价，折算人民币按 2026-08-27 即期 6.7225，汇率波动会改变人民币折算额。",
]
for i, t in enumerate(obs):
    ws2.cell(row=obs_row + 1 + i, column=1, value=t)

conf_row = obs_row + 1 + len(obs) + 2
ws2.cell(row=conf_row, column=1, value="置信度评级（v2.5 · 数据缺项如实下调）").font = Font(bold=True, size=12)
conf = [
    ("数据完整度", "高 — 17 张截图覆盖全部四平台；仅建行 1 只缺参考年化（见待补充字段清单）"),
    ("OCR可信度", "中高 — 金额/收益来自截图提取，请以 APP 原始数据为最终准绳"),
    ("币种确认", "高 — 中行 5 只已确认美元/汇，其余平台人民币，无标黄待核项"),
    ("资产分类", "中 — 帮你投策略组合内部股债构成按产品名推断，非官方披露"),
    ("财务诊断", "中 — 缺个人风险偏好/期限/目标/回撤参数，为中性口径诊断"),
    ("整体评级", "B+（补齐建行参考年化与个人参数后可上调）"),
]
for i, (k, v) in enumerate(conf):
    ws2.cell(row=conf_row + 1 + i, column=1, value=k).font = Font(bold=True)
    ws2.cell(row=conf_row + 1 + i, column=2, value=v)

for c, w in enumerate([24, 14, 16, 16], 1):
    ws2.column_dimensions[openpyxl.utils.get_column_letter(c)].width = w

# ============ Sheet3: 汇率形势分析 ============
ws3 = wb.create_sheet("汇率形势分析")
usd_equiv = total_mv_usd
ws3["A1"] = "美元汇率形势分析（客观）"
ws3["A1"].font = Font(size=14, bold=True, color="1F4E79")
ws3["A2"] = "统计日 2026-08-27 ｜ 数据来源：中国货币市场 / 实时汇率网 ｜ 本表仅做客观数据整理，不含任何投资建议"
ws3["A2"].font = Font(size=9, color="808080")

ws3["A4"] = "一、当前汇率快照"; ws3["A4"].font = Font(bold=True, size=12)
snap = [
    ("指标", "数值", "说明"),
    ("USD/CNY 央行中间价", rate_mid, "2026-08-27，较前贬值11bp"),
    ("USD/CNY 在岸即期", rate_now, "2026-08-27 约值"),
    ("美元指数 USDX", 99.11, "2026-08-27 约值，近10日-0.86%"),
    ("一年前 USD/CNY", rate_year_ago, "2025-08-27 约值"),
    ("美元年内变动(%)", round((rate_now - rate_year_ago) / rate_year_ago * 100, 2), "美元对人民币较一年前贬值"),
]
for i, row in enumerate(snap):
    for c, v in enumerate(row, 1):
        cell = ws3.cell(row=5 + i, column=c, value=v)
        if i == 0:
            cell.font = Font(bold=True, color="FFFFFF")
            cell.fill = PatternFill("solid", fgColor="1F4E79")
        if c == 2 and isinstance(v, (int, float)):
            cell.number_format = '#,##0.0000' if 'USD/CNY' in snap[i][0] else '#,##0.00'

row_bg = 5 + len(snap) + 2
ws3.cell(row=row_bg, column=1, value="二、美元走势背景（客观事实）").font = Font(bold=True, size=12)
bg = [
    "1. 美联储利率区间维持 3.5%-3.75%（2026-01 暂停）。",
    "2. 美国CPI降温，市场普遍押注 2026年9月美联储降息；机构看空美元。",
    "3. 美元指数现约 99.1，近10日 -0.86%，短期偏弱。",
    "4. 机构观点：去美元化长期趋势、人民币有升值空间。",
    "5. 风险：若通胀反弹（地缘冲突推升油价），降息放缓，美元或阶段性反弹。",
]
for i, t in enumerate(bg):
    ws3.cell(row=row_bg + 1 + i, column=1, value=t)

row_ex = row_bg + 1 + len(bg) + 2
ws3.cell(row=row_ex, column=1, value="三、本持仓的汇率敞口（客观）").font = Font(bold=True, size=12)
ex = [
    "1. 5只产品均为「美元/汇」，本金与收益以美元计，参考市值即美元金额。",
    "2. 折算人民币 = 美元金额 × 到期时实时汇率，汇率变动直接影响人民币落袋额。",
    "3. 美元走弱 → 同额美元折算人民币减少；美元走强 → 折算人民币增加。",
    "4. 封闭式3只到期日 2026-10 至 2027-06，跨越降息窗口，到期汇率不确定。",
    "5. 开放式2只可灵活赎回，汇率风险更实时。",
]
for i, t in enumerate(ex):
    ws3.cell(row=row_ex + 1 + i, column=1, value=t)

row_sc = row_ex + 1 + len(ex) + 2
ws3.cell(row=row_sc, column=1, value="四、汇率情景测算（数学推演，非投资建议）").font = Font(bold=True, size=12)
ws3.cell(row=row_sc + 1, column=1,
         value=f"本持仓美元本金 ≈ {usd_equiv:,.2f} USD（产品本身以美元计价）").font = Font(italic=True)
sc_header = ["情景", "假设 USD/CNY", "折算人民币(元)", "较当前变动(元)"]
for c, h in enumerate(sc_header, 1):
    cell = ws3.cell(row=row_sc + 2, column=c, value=h)
    cell.font = Font(bold=True, color="FFFFFF")
    cell.fill = PatternFill("solid", fgColor="1F4E79")
scenarios = [
    ("美元大幅走强(参考一年前)", rate_year_ago),
    ("美元走强情景", 6.85),
    ("当前基准", rate_now),
    ("美元走弱情景(降息预期)", 6.55),
    ("美元大幅走弱", 6.40),
]
base_cny = usd_equiv * rate_now
for i, (name, r) in enumerate(scenarios):
    cny = usd_equiv * r
    ws3.cell(row=row_sc + 3 + i, column=1, value=name)
    ws3.cell(row=row_sc + 3 + i, column=2, value=r).number_format = '0.0000'
    ws3.cell(row=row_sc + 3 + i, column=3, value=round(cny, 2)).number_format = '#,##0.00'
    delta = round(cny - base_cny, 2)
    dc = ws3.cell(row=row_sc + 3 + i, column=4, value=delta)
    dc.number_format = '#,##0.00'
    dc.font = Font(color="C00000" if delta >= 0 else "006100")

for c, w in enumerate([34, 18, 20, 18], 1):
    ws3.column_dimensions[openpyxl.utils.get_column_letter(c)].width = w

# ============ Sheet4: 招商银行持仓 ============
ws4 = wb.create_sheet("招商银行持仓")
ws4["A1"] = "招商银行 · 全部持仓明细"
ws4["A1"].font = Font(size=14, bold=True, color="1F4E79")
ws4["A2"] = "数据来源：招商银行APP截图 IMG_1415/1414/1413.PNG ｜ 统计日 2026-08-27 ｜ 单位：人民币元"
ws4["A2"].font = Font(size=9, color="808080")

ws4["A4"] = "一、基金持仓（6只）"; ws4["A4"].font = Font(bold=True, size=12)
fund_headers = ["序号", "产品名称", "金额(元)", "日收益(元)", "持仓收益(元)", "收益率", "类型"]
fh_row = 5
for c, h in enumerate(fund_headers, 1):
    cell = ws4.cell(row=fh_row, column=c, value=h)
    cell.font = Font(bold=True, color="FFFFFF")
    cell.fill = PatternFill("solid", fgColor="1F4E79")

fr_start = fh_row + 1
for i, f in enumerate(funds):
    rr = fr_start + i
    for c, v in enumerate(f, 1):
        cell = ws4.cell(row=rr, column=c, value=v)
        cell.alignment = Alignment(horizontal="center" if c != 2 else "left", vertical="center")
        if c == 3:
            cell.number_format = '#,##0.00'
        if c in (4, 5):
            cell.number_format = '#,##0.00'
            if isinstance(v, (int, float)):
                cell.font = Font(color="C00000" if v >= 0 else "006100")

fr_total = fr_start + len(funds)
ws4.cell(row=fr_total, column=1, value="合计").font = Font(bold=True)
ws4.cell(row=fr_total, column=2, value=f"共{len(funds)}只").font = Font(bold=True)
tc_fmv = ws4.cell(row=fr_total, column=3, value=total_fund_mv)
tc_fmv.number_format = '#,##0.00'; tc_fmv.font = Font(bold=True)
tc_fp = ws4.cell(row=fr_total, column=5, value=total_fund_profit)
tc_fp.number_format = '#,##0.00'; tc_fp.font = Font(bold=True, color="C00000" if total_fund_profit >= 0 else "006100")

for rr in range(fh_row, fr_total + 1):
    for c in range(1, len(fund_headers) + 1):
        ws4.cell(row=rr, column=c).border = border

lr_start = fr_total + 3
ws4.cell(row=lr_start, column=1, value="二、理财持仓（5只）").font = Font(bold=True, size=12)
lc_headers = ["序号", "产品名称", "持仓金额(元)", "持仓收益(元)", "到期/状态", "参考年化(参考值·口径见单元格)", "实际累计收益率"]
for c, h in enumerate(lc_headers, 1):
    cell = ws4.cell(row=lr_start + 1, column=c, value=h)
    cell.font = Font(bold=True, color="FFFFFF")
    cell.fill = PatternFill("solid", fgColor="1F4E79")

lcr_start = lr_start + 2
for i, l in enumerate(licai):
    rr = lcr_start + i
    for c, v in enumerate(l, 1):
        cell = ws4.cell(row=rr, column=c, value=v)
        cell.alignment = Alignment(horizontal="center" if c != 2 else "left", vertical="center")
        if c == 3:
            cell.number_format = '#,##0.00'
        if c == 4:
            cell.number_format = '#,##0.00'
            cell.font = Font(color="C00000")
    rate_pct = l[3] / l[2] * 100
    rcell = ws4.cell(row=rr, column=7, value=f"{rate_pct:+.2f}%")
    rcell.alignment = Alignment(horizontal="center", vertical="center")
    rcell.font = Font(color="C00000" if l[3] >= 0 else "006100")

lr_total = lcr_start + len(licai)
ws4.cell(row=lr_total, column=1, value="合计").font = Font(bold=True)
ws4.cell(row=lr_total, column=2, value=f"共{len(licai)}只").font = Font(bold=True)
tc_lmv = ws4.cell(row=lr_total, column=3, value=total_lc_mv)
tc_lmv.number_format = '#,##0.00'; tc_lmv.font = Font(bold=True)
tc_lp = ws4.cell(row=lr_total, column=4, value=total_lc_profit)
tc_lp.number_format = '#,##0.00'; tc_lp.font = Font(bold=True, color="C00000")

for rr in range(lr_start + 1, lr_total + 1):
    for c in range(1, len(lc_headers) + 1):
        ws4.cell(row=rr, column=c).border = border

for c, w in enumerate([6, 38, 14, 14, 24, 16, 14], 1):
    ws4.column_dimensions[openpyxl.utils.get_column_letter(c)].width = w

ov_start = lr_total + 3
ws4.cell(row=ov_start, column=1, value="三、招商银行总览").font = Font(bold=True, size=12)
overview_data = [
    ("基金总金额", f"{total_fund_mv:,.2f} 元"),
    ("基金总收益", f"{total_fund_profit:+,.2f} 元"),
    ("理财总金额", f"{total_lc_mv:,.2f} 元"),
    ("理财总收益", f"{total_lc_profit:+,.2f} 元"),
    ("招行合计金额", f"{cmb_total_mv:,.2f} 元"),
    ("招行合计收益", f"{cmb_total_profit:+,.2f} 元"),
]
for i, (k, v) in enumerate(overview_data):
    ws4.cell(row=ov_start + 1 + i, column=1, value=k).font = Font(bold=True)
    ws4.cell(row=ov_start + 1 + i, column=2, value=v)

obs_start = ov_start + 1 + len(overview_data) + 2
ws4.cell(row=obs_start, column=1, value="客观观察（不含投资建议）").font = Font(bold=True, size=12)
observations = [
    "1. 招行合计持仓约 %.2f 元，累计收益 %+.2f 元。" % (cmb_total_mv, cmb_total_profit),
    "2. 理财端全部盈利（+357.72），其中半年宝单只贡献 +101.01。",
    "3. 基金端整体亏损（-%.2f），主因富国中证港股通互联网ETF联接C亏 -540.75（-31.26%%）。" % abs(total_fund_profit),
    "4. 港股互联网基金亏损严重（-31.26%%），同期港股高股息低波ETF也亏（-1.74%%）。",
    "5. QDII分化：日本精选股票QDII赚 +6.96%%，亚洲收益债券QDII亏 -1.44%%。",
    "6. 多月宝金额最大（50,065元），占招行理财约 %d%%，收益仅 +65.00（年化偏低）。" % int(50065 / total_lc_mv * 100),
    "7. 交银理财180天持有期最近可赎日2027-01-28，流动性锁定约5个月。",
    "8. 参考年化口径不同、不可直接横向比：多宝系列(月月宝/半年宝/多月宝)为近1年参考年化(参考值)；光大=2.36%、交银=6.24%为成立以来年化。你各产品实际持有累计(月月宝0.48%/半年宝1.00%/多月宝0.13%/光大0.87%/交银0.27%)均低于对应参考年化，主因持有期短于参考口径周期(近1年或成立以来)。",
]
for i, t in enumerate(observations):
    ws4.cell(row=obs_start + 1 + i, column=1, value=t)

# ============ Sheet5: 建设银行持仓 ============
ws5_ccb = wb.create_sheet("建设银行持仓")
ws5_ccb["A1"] = "建设银行 · 全部持仓明细"
ws5_ccb["A1"].font = Font(size=14, bold=True, color="1F4E79")
ws5_ccb["A2"] = "数据来源：建设银行APP截图 IMG_1419/1418/1417/1416.PNG ｜ 统计日 2026-08-27 ｜ 单位：人民币元"
ws5_ccb["A2"].font = Font(size=9, color="808080")

# --- 基金区 ---
ws5_ccb.cell(row=4, column=1, value="一、基金持仓（5只）").font = Font(bold=True, size=12)
ccb_fund_headers = ["序号", "产品名称", "代码", "参考市值(元)", "日收益(元)", "持仓收益(元)", "收益率", "类型"]
for c, h in enumerate(ccb_fund_headers, 1):
    cell = ws5_ccb.cell(row=5, column=c, value=h)
    cell.font = Font(bold=True, color="FFFFFF")
    cell.fill = PatternFill("solid", fgColor="1F4E79")

ccb_fr_start = 6
for i, f in enumerate(ccb_funds):
    rr = ccb_fr_start + i
    for c, v in enumerate(f, 1):
        cell = ws5_ccb.cell(row=rr, column=c, value=v)
        cell.alignment = Alignment(horizontal="center" if c != 2 else "left", vertical="center")
        if c == 3:
            cell.number_format = '000000'
        if c == 4:
            cell.number_format = '#,##0.00'
        if c in (5, 6):
            cell.number_format = '#,##0.00'
            if isinstance(v, (int, float)):
                cell.font = Font(color="C00000" if v >= 0 else "006100")

ccb_fr_total = ccb_fr_start + len(ccb_funds)
ws5_ccb.cell(row=ccb_fr_total, column=1, value="合计").font = Font(bold=True)
ws5_ccb.cell(row=ccb_fr_total, column=2, value=f"共{len(ccb_funds)}只").font = Font(bold=True)
tc_cfmv = ws5_ccb.cell(row=ccb_fr_total, column=4, value=ccb_total_fund_mv)
tc_cfmv.number_format = '#,##0.00'; tc_cfmv.font = Font(bold=True)
tc_cfp = ws5_ccb.cell(row=ccb_fr_total, column=6, value=ccb_total_fund_profit)
tc_cfp.number_format = '#,##0.00'; tc_cfp.font = Font(bold=True, color="C00000" if ccb_total_fund_profit >= 0 else "006100")

for rr in range(5, ccb_fr_total + 1):
    for c in range(1, len(ccb_fund_headers) + 1):
        ws5_ccb.cell(row=rr, column=c).border = border

# --- 理财区 ---
ccb_lr_start = ccb_fr_total + 3
ws5_ccb.cell(row=ccb_lr_start, column=1, value="二、理财持仓（1只）").font = Font(bold=True, size=12)
ccb_lc_headers = ["序号", "产品名称", "持仓金额(元)", "持仓收益(元)", "到期/状态", "参考年化(参考值·口径见单元格)"]
for c, h in enumerate(ccb_lc_headers, 1):
    cell = ws5_ccb.cell(row=ccb_lr_start + 1, column=c, value=h)
    cell.font = Font(bold=True, color="FFFFFF")
    cell.fill = PatternFill("solid", fgColor="1F4E79")

ccb_lcr_start = ccb_lr_start + 2
for i, l in enumerate(ccb_licai):
    rr = ccb_lcr_start + i
    for c, v in enumerate(l, 1):
        cell = ws5_ccb.cell(row=rr, column=c, value=v)
        cell.alignment = Alignment(horizontal="center" if c != 2 else "left", vertical="center")
        if c == 3:
            cell.number_format = '#,##0.00'
        if c == 4:
            cell.number_format = '#,##0.00'
            cell.font = Font(color="C00000")
    rate_pct = l[3] / l[2] * 100
    rcell = ws5_ccb.cell(row=rr, column=7, value=f"{rate_pct:+.2f}%")
    rcell.alignment = Alignment(horizontal="center", vertical="center")
    rcell.font = Font(color="C00000" if l[3] >= 0 else "006100")

ccb_lr_total = ccb_lcr_start + len(ccb_licai)
ws5_ccb.cell(row=ccb_lr_total, column=1, value="合计").font = Font(bold=True)
ws5_ccb.cell(row=ccb_lr_total, column=2, value=f"共{len(ccb_licai)}只").font = Font(bold=True)
tc_clmv = ws5_ccb.cell(row=ccb_lr_total, column=3, value=ccb_total_lc_mv)
tc_clmv.number_format = '#,##0.00'; tc_clmv.font = Font(bold=True)
tc_clp = ws5_ccb.cell(row=ccb_lr_total, column=4, value=ccb_total_lc_profit)
tc_clp.number_format = '#,##0.00'; tc_clp.font = Font(bold=True, color="C00000")

for rr in range(ccb_lr_start + 1, ccb_lr_total + 1):
    for c in range(1, len(ccb_lc_headers) + 2):  # +1 for 实际累计收益率
        ws5_ccb.cell(row=rr, column=c).border = border

# 理财表头补第7列
ws5_ccb.cell(row=ccb_lr_start + 1, column=7, value="实际累计收益率").font = Font(bold=True, color="FFFFFF")
ws5_ccb.cell(row=ccb_lr_start + 1, column=7).fill = PatternFill("solid", fgColor="1F4E79")

for c, w in enumerate([6, 34, 10, 14, 14, 14, 12, 16], 1):
    ws5_ccb.column_dimensions[openpyxl.utils.get_column_letter(c)].width = w

# --- 总览 ---
ccb_ov_start = ccb_lr_total + 3
ws5_ccb.cell(row=ccb_ov_start, column=1, value="三、建设银行总览").font = Font(bold=True, size=12)
ccb_overview = [
    ("基金总金额", f"{ccb_total_fund_mv:,.2f} 元"),
    ("基金总收益", f"{ccb_total_fund_profit:+,.2f} 元"),
    ("理财总金额", f"{ccb_total_lc_mv:,.2f} 元"),
    ("理财总收益", f"{ccb_total_lc_profit:+,.2f} 元"),
    ("理财累计收益（含历史已赎回）", "+6,475.73 元"),
    ("建行合计金额", f"{ccb_total_mv:,.2f} 元"),
    ("建行合计收益", f"{ccb_total_profit:+,.2f} 元"),
]
for i, (k, v) in enumerate(ccb_overview):
    ws5_ccb.cell(row=ccb_ov_start + 1 + i, column=1, value=k).font = Font(bold=True)
    ws5_ccb.cell(row=ccb_ov_start + 1 + i, column=2, value=v)

ccb_obs_start = ccb_ov_start + 1 + len(ccb_overview) + 2
ws5_ccb.cell(row=ccb_obs_start, column=1, value="客观观察（不含投资建议）").font = Font(bold=True, size=12)
ccb_obs = [
    "1. 建行合计持仓约 %.2f 元，累计收益 %+.2f 元。" % (ccb_total_mv, ccb_total_profit),
    "2. 理财端仅1只（浦银多季鑫封闭式113号），金额10,145.12，持仓收益+145.12；但APP显示累计收益+6,475.73（说明该产品历史上多次复投/滚动持有，当前份额只是最新一期）。",
    "3. 基金端5只中3只盈利（华夏纯债+43.65/建信现金添益+44.90/建信沪深300+2.23），2只亏损。",
    "4. 南方亚洲美元债C亏损最大（-102.76，-2.78%%），美元债受汇率和利率双重影响。",
    "5. 华夏聚嘉优选三个月持有即将于2026-08-28开放赎回（明天），目前微亏-1.98。",
    "6. 建信沪深300A金额极小（102.23元），疑似试水或定投初期。",
    "7. 浦银理财多季鑫113号将于2026-09-28到期，还有约1个月。",
]
for i, t in enumerate(ccb_obs):
    ws5_ccb.cell(row=ccb_obs_start + 1 + i, column=1, value=t)

# ============ Sheet6: 支付宝持仓 ============
ws6_alipay = wb.create_sheet("支付宝持仓")
ws6_alipay["A1"] = "支付宝 · 全部持仓明细"
ws6_alipay["A1"].font = Font(size=14, bold=True, color="1F4E79")
ws6_alipay["A2"] = "数据来源：支付宝APP截图 IMG_1428~IMG_1420.PNG（共9张）｜ 统计日 2026-08-27 ｜ 单位：人民币元"
ws6_alipay["A2"].font = Font(size=9, color="808080")

# --- 帮你投策略组合 ---
ws6_alipay.cell(row=4, column=1, value="一、帮你投策略组合（6只）").font = Font(bold=True, size=12)
strat_headers = ["序号", "产品名称", "金额(元)", "昨日收益(元)", "持有收益(元)"]
for c, h in enumerate(strat_headers, 1):
    cell = ws6_alipay.cell(row=5, column=c, value=h)
    cell.font = Font(bold=True, color="FFFFFF")
    cell.fill = PatternFill("solid", fgColor="1F4E79")

strat_start = 6
for i, s in enumerate(alipay_strategy):
    rr = strat_start + i
    for c, v in enumerate(s, 1):
        cell = ws6_alipay.cell(row=rr, column=c, value=v)
        cell.alignment = Alignment(horizontal="center" if c != 2 else "left", vertical="center")
        if c == 3:
            cell.number_format = '#,##0.00'
        if c in (4, 5):
            cell.number_format = '#,##0.00'
            if isinstance(v, (int, float)):
                cell.font = Font(color="C00000" if v >= 0 else "006100")

strat_total = strat_start + len(alipay_strategy)
ws6_alipay.cell(row=strat_total, column=1, value="合计").font = Font(bold=True)
ws6_alipay.cell(row=strat_total, column=2, value=f"共{len(alipay_strategy)}只").font = Font(bold=True)
tc_smv = ws6_alipay.cell(row=strat_total, column=3, value=alipay_strat_mv)
tc_smv.number_format = '#,##0.00'; tc_smv.font = Font(bold=True)
tc_sp = ws6_alipay.cell(row=strat_total, column=5, value=alipay_strat_profit)
tc_sp.number_format = '#,##0.00'; tc_sp.font = Font(bold=True, color="C00000")

for rr in range(5, strat_total + 1):
    for c in range(1, len(strat_headers) + 1):
        ws6_alipay.cell(row=rr, column=c).border = border

# --- 基金区 ---
fund_start = strat_total + 3
ws6_alipay.cell(row=fund_start, column=1, value="二、基金持仓（15只）").font = Font(bold=True, size=12)
alipay_fund_headers = ["序号", "产品名称", "金额(元)", "日收益(元)", "持有收益(元)", "收益率", "类型/备注"]
for c, h in enumerate(alipay_fund_headers, 1):
    cell = ws6_alipay.cell(row=fund_start + 1, column=c, value=h)
    cell.font = Font(bold=True, color="FFFFFF")
    cell.fill = PatternFill("solid", fgColor="1F4E79")

af_start = fund_start + 2
for i, f in enumerate(alipay_funds):
    rr = af_start + i
    for c, v in enumerate(f, 1):
        cell = ws6_alipay.cell(row=rr, column=c, value=v)
        cell.alignment = Alignment(horizontal="center" if c != 2 else "left", vertical="center")
        if c == 3:
            cell.number_format = '#,##0.00'
        if c in (4, 5):
            cell.number_format = '#,##0.00'
            if isinstance(v, (int, float)):
                cell.font = Font(color="C00000" if v >= 0 else "006100")

af_total = af_start + len(alipay_funds)
ws6_alipay.cell(row=af_total, column=1, value="合计").font = Font(bold=True)
ws6_alipay.cell(row=af_total, column=2, value=f"共{len(alipay_funds)}只").font = Font(bold=True)
tc_afmv = ws6_alipay.cell(row=af_total, column=3, value=alipay_fund_mv)
tc_afmv.number_format = '#,##0.00'; tc_afmv.font = Font(bold=True)
tc_afp = ws6_alipay.cell(row=af_total, column=5, value=alipay_fund_profit)
tc_afp.number_format = '#,##0.00'; tc_afp.font = Font(bold=True, color="C00000" if alipay_fund_profit >= 0 else "006100")

for rr in range(fund_start + 1, af_total + 1):
    for c in range(1, len(alipay_fund_headers) + 1):
        ws6_alipay.cell(row=rr, column=c).border = border

# --- 总览 ---
alipay_ov = af_total + 3
ws6_alipay.cell(row=alipay_ov, column=1, value="三、支付宝总览").font = Font(bold=True, size=12)
alipay_overview = [
    ("帮你投策略金额", f"{alipay_strat_mv:,.2f} 元"),
    ("帮你投策略收益", f"{alipay_strat_profit:+,.2f} 元"),
    ("基金总金额", f"{alipay_fund_mv:,.2f} 元"),
    ("基金总收益", f"{alipay_fund_profit:+,.2f} 元"),
    ("支付宝合计金额", f"{alipay_total_mv:,.2f} 元"),
    ("支付宝合计收益", f"{alipay_total_profit:+,.2f} 元"),
]
for i, (k, v) in enumerate(alipay_overview):
    ws6_alipay.cell(row=alipay_ov + 1 + i, column=1, value=k).font = Font(bold=True)
    ws6_alipay.cell(row=alipay_ov + 1 + i, column=2, value=v)

alipay_obs = alipay_ov + 1 + len(alipay_overview) + 2
ws6_alipay.cell(row=alipay_obs, column=1, value="客观观察（不含投资建议）").font = Font(bold=True, size=12)
alipay_observations = [
    "1. 支付宝合计持仓约 %.2f 元，累计收益 %+.2f 元。" % (alipay_total_mv, alipay_total_profit),
    "2. 帮你投策略全部盈利（+224.09），其中全球精选100单只贡献 +117.21，表现最突出。",
    "3. 基金端15只中12只盈利、3只亏损，整体盈利 %+.2f 元。" % alipay_fund_profit,
    "4. 最大亏损源：天弘中证全指证券公司ETF联接C亏 -251.32（-8.07%%），证券板块近期承压。",
    "5. 第二亏损源：中银美元债债券(QDII)A亏 -117.92（-1.81%%），美元债受汇率和利率双重影响。",
    "6. 第三亏损源：富国亚洲收益债券(QDII)A亏 -41.42（-1.21%%）。",
    "7. 盈利冠军：华宝核心优势灵活配置混合A赚 +250.78（+14.30%%），定投效果显著。",
    "8. QDII类分化明显：美股方向（嘉实美国成长+92.72/广发纳指100+60.64/华宝纳指精选+26.34）全线盈利；美元债/亚债方向（中银美元债-117.92/富国亚收债-41.42）均亏。",
    "9. 中银美元债金额最大（6,382.08元），占支付宝基金总额约 %.0f%%，但也是最大单只亏损源。" % int(6382.08 / alipay_fund_mv * 100),
    "10. 定投产品共9只（华宝核心优势/招商信用添利/长城系列3只/长城A500/中银美元债/中银国企债），说明你在支付宝以定投为主。",
]
for i, t in enumerate(alipay_observations):
    ws6_alipay.cell(row=alipay_obs + 1 + i, column=1, value=t)

for c, w in enumerate([6, 38, 12, 12, 14, 10, 16], 1):
    ws6_alipay.column_dimensions[openpyxl.utils.get_column_letter(c)].width = w

# ============ Sheet: 宏观速览（v2.0 推荐模块 · 仅解释波动来源，不预测）============
ws7 = wb.create_sheet("宏观速览")
ws7["A1"] = "宏观速览（客观 · 仅解释收益波动来源，不预测、不归因买卖）"
ws7["A1"].font = Font(size=14, bold=True, color="1F4E79")
ws7["A2"] = "统计日 2026-08-27 ｜ 数据来源：WebSearch 实时抓取（Wind/中国货币网/港交所/新浪财经），非训练数据 ｜ 本表用途：对照你的持仓亏损源（港股ETF/美元债/债基）做客观归因，不含任何投资建议"
ws7["A2"].font = Font(size=9, color="808080")

ws7["A4"] = "一、A股主要指数（2026-08-27 收盘）"
ws7["A4"].font = Font(size=11, bold=True, color="1F4E79")
a_shares = [
    ("指数", "最新点位", "涨跌幅", "与你持仓的关联（客观归因）"),
    ("上证指数", 3956.57, "+1.13%", "建信沪深300A(+2.18%累计)属A股宽基，今日普涨但仅影响当日净值，不改变长期累计"),
    ("沪深300", 4630.28, "+0.86%", "同上；A股当日风险偏好回升、科技成长领涨"),
    ("深证成指", 14048.88, "+1.50%", "—"),
    ("创业板指", 3473.35, "+1.71%", "—"),
    ("科创50", 1693.48, "+3.77%", "科技成长方向当日最强（PCB/CPO/半导体），与你的科技类基金正相关"),
]
ar = 5
for i, row in enumerate(a_shares):
    for c, v in enumerate(row, 1):
        cell = ws7.cell(row=ar + i, column=c, value=v)
        cell.alignment = Alignment(vertical="center", wrap_text=(c == 4), horizontal="left" if c == 4 else "center")
        if i == 0:
            cell.font = Font(bold=True)
            cell.fill = PatternFill("solid", fgColor="D9E1F2")
        if c == 3:
            cell.font = Font(color="C00000") if v.startswith("+") else Font(color="008000")

ws7["A12"] = "二、港股主要指数（2026-08-27）"
ws7["A12"].font = Font(size=11, bold=True, color="1F4E79")
h_shares = [
    ("指数", "最新点位", "涨跌幅", "与你持仓的关联（客观归因）"),
    ("恒生指数", "≈25,546", "-0.34%", "港股当日偏弱；近一月(8/3-8/27)区间 -4.33%，整体承压"),
    ("恒生科技指数", 4620.29, "-0.13%", "富国中证港股通互联网ETF联接C(-31.26%)主投港股科技，近一月区间 -4.33% 部分解释其深度回撤"),
    ("恒生中国企业指数", "≈8,471", "+0.21%", "中概相关，当日微涨"),
]
hr = 13
for i, row in enumerate(h_shares):
    for c, v in enumerate(row, 1):
        cell = ws7.cell(row=hr + i, column=c, value=v)
        cell.alignment = Alignment(vertical="center", wrap_text=(c == 4), horizontal="left" if c == 4 else "center")
        if i == 0:
            cell.font = Font(bold=True)
            cell.fill = PatternFill("solid", fgColor="D9E1F2")
        if c == 3:
            cell.font = Font(color="C00000") if v.startswith("+") else Font(color="008000")

ws7["A18"] = "三、债券市场（2026-08-27）"
ws7["A18"].font = Font(size=11, bold=True, color="1F4E79")
bond = [
    ("指标", "最新值", "变动", "与你持仓的关联（客观归因）"),
    ("中国10年期国债收益率", "≈1.69%", "+0.06bp(微上)", "债基（华夏纯债+43.65/建信现金添益+44.90）处平稳债市，净值微涨；利率微上行对长债价小幅压力"),
    ("美国10年期国债收益率", "4.649%", "+0.22%", "南方亚洲美元债C(-102.76)主投美债，美债收益率上行→存量债价下跌，部分解释其亏损"),
    ("中债综合指数(财富)", 262.50, "-0.02%", "债市当日小幅波动，整体平稳"),
]
br = 19
for i, row in enumerate(bond):
    for c, v in enumerate(row, 1):
        cell = ws7.cell(row=br + i, column=c, value=v)
        cell.alignment = Alignment(vertical="center", wrap_text=(c == 4), horizontal="left" if c == 4 else "center")
        if i == 0:
            cell.font = Font(bold=True)
            cell.fill = PatternFill("solid", fgColor="D9E1F2")

ws7["A24"] = "四、汇率与美元（2026-08-27）"
ws7["A24"].font = Font(size=11, bold=True, color="1F4E79")
fx = [
    ("指标", "最新值", "变动", "与你持仓的关联（客观归因）"),
    ("美元指数", 99.1360, "+0.22%", "当日美元微走强，与你中行美元理财(占全行67%)的人民币折算额正相关"),
    ("USD/CNY 离岸", 6.7194, "人民币升值", "美元贬值→你美元资产折人民币被动缩水（详见「汇率形势分析」）"),
    ("在岸即期(基准)", 6.7225, "—", "中行折算口径"),
]
fr = 25
for i, row in enumerate(fx):
    for c, v in enumerate(row, 1):
        cell = ws7.cell(row=fr + i, column=c, value=v)
        cell.alignment = Alignment(vertical="center", wrap_text=(c == 4), horizontal="left" if c == 4 else "center")
        if i == 0:
            cell.font = Font(bold=True)
            cell.fill = PatternFill("solid", fgColor="D9E1F2")

ws7["A31"] = "客观归因小结：你的主要亏损源中，富国港股通互联网ETF(-31.26%)对应近一月港股科技区间-4.33%、当日恒生科技仍-0.13%；南方亚洲美元债C(-102.76)对应美债10年收益率上行至4.649%；债基微赚对应中债10年约1.69%的平稳环境。以上为事后波动来源解释，不构成任何未来走势判断或买卖建议。"
ws7["A31"].font = Font(size=9, italic=True, color="808080")
ws7["A31"].alignment = Alignment(wrap_text=True, vertical="top")
ws7.merge_cells("A31:D34")

for c, w in enumerate([22, 14, 14, 60], 1):
    ws7.column_dimensions[openpyxl.utils.get_column_letter(c)].width = w

# ============ Sheet: 全行合并总览 ============
ws5 = wb.create_sheet("全行合并总览")
ws5["A1"] = "全行合并总览（客观）"
ws5["A1"].font = Font(size=14, bold=True, color="1F4E79")
ws5["A2"] = "统计日 2026-08-27 ｜ 中行美元理财按即期6.7225折算人民币 ｜ 单位：人民币元（中行为折算值）"
ws5["A2"].font = Font(size=9, color="808080")

merge = [
    ("项目", "中行(折算人民币)", "招商银行", "建设银行", "支付宝", "全行合计"),
    ("持仓市值", f"≈{total_mv_cny:,.0f}", f"{cmb_total_mv:,.0f}", f"{ccb_total_mv:,.0f}", f"{alipay_total_mv:,.0f}", f"≈{grand_total_mv_all:,.0f}"),
    ("持仓收益", f"≈{total_profit_cny:+,.0f}", f"{cmb_total_profit:+,.0f}", f"{ccb_total_profit:+,.0f}", f"{alipay_total_profit:+,.0f}", f"≈{grand_total_profit_all:+,.0f}"),
    ("原币种口径", "53,147.17 USD", "113,122.15 元", "21,337.41 元", "44,999.26 元", "美元+人民币混合"),
]
for i, row in enumerate(merge):
    for c, v in enumerate(row, 1):
        cell = ws5.cell(row=4 + i, column=c, value=v)
        if i == 0:
            cell.font = Font(bold=True, color="FFFFFF")
            cell.fill = PatternFill("solid", fgColor="1F4E79")
        cell.alignment = Alignment(horizontal="left" if c == 1 else "center", vertical="center")

note_row = 4 + len(merge) + 2
ws5.cell(row=note_row, column=1,
         value="说明：中行美元理财以美元计价，折算人民币含汇率假设；汇率波动将改变中行部分人民币折算额（详见「汇率形势分析」）。").font = Font(italic=True, size=9, color="808080")

for c, w in enumerate([14, 18, 12, 12, 12, 16], 1):
    ws5.column_dimensions[openpyxl.utils.get_column_letter(c)].width = w

# ============ Sheet8: 理财师诊断分析（分析师版） ============
ws8 = wb.create_sheet("理财师诊断分析")
ws8["A1"] = "理财师诊断分析（分析师版 · 含诊断结论与优化思路）"
ws8["A1"].font = Font(size=14, bold=True, color="1F4E79")
ws8["A2"] = "统计日 2026-08-27 ｜ 数据来源：中行/招行/建行/支付宝APP持仓截图经WorkBuddy读图提取 ｜ 单位：人民币元（中行美元按即期6.7225折算）"
ws8["A2"].font = Font(size=9, color="808080")
ws8["A3"] = "⚠️ 本分析仅供参考，不构成具体投资建议。优化思路仅提供逻辑与方向，不指令买入/卖出具体产品。"
ws8["A3"].font = Font(size=9, italic=True, color="C00000")

ws8["A5"] = "【前置说明】模板要求的个人参数（风险偏好 / 投资期限 / 理财目标 / 可接受最大回撤）本次未提供，以下基于持仓结构做中性诊断；补齐参数后可进一步校准匹配度。"
ws8["A5"].font = Font(size=10, color="C00000")
ws8.merge_cells("A5:H5")

dr = 7
ws8.cell(row=dr, column=1, value="一、整体诊断结论").font = Font(size=12, bold=True, color="1F4E79")
dr += 1
_diag_conc = ("你的持仓是一篮子『极度稳健、类固收主导』的组合：固收/类固收（美元理财 + 银行理财 + 债基 + 货币）合计约占总资产 95.3%，"
              "权益（股票类）仅约 2.6%。最突出特征是『单一美元资产（中行）占全行约 2/3』，造成币种与平台双重集中。"
              "截至统计日全行累计收益约 +5,056 元（总回报约 +0.94%），其中约 +4,607 元来自中行美元理财，其余三平台合计仅 +449 元、招行基金端仍小幅亏损。"
              "组合安全性高、波动小，但收益天花板偏低，且美元汇率敞口是核心风险点。")
ws8.cell(row=dr, column=1, value=_diag_conc).alignment = Alignment(wrap_text=True, vertical="top")
ws8.merge_cells(start_row=dr, start_column=1, end_row=dr+3, end_column=8)
for rr in range(dr, dr+4):
    ws8.row_dimensions[rr].height = 20
dr += 5

ws8.cell(row=dr, column=1, value="二、大类资产配置比例").font = Font(size=12, bold=True, color="1F4E79")
dr += 1
for c, h in enumerate(["大类资产", "市值(元)", "占比", "说明"], 1):
    cell = ws8.cell(row=dr, column=c, value=h)
    cell.font = Font(bold=True, color="FFFFFF"); cell.fill = PatternFill("solid", fgColor="1F4E79")
    cell.alignment = Alignment(horizontal="center")
dr += 1
_diag_alloc = [
    ("境外美元固收（中行5只）", 357281.85, "66.55%", "美元/汇，QDII+美元封闭+美元日计划，收益与汇率双挂钩"),
    ("银行固收理财（招行5+建行1）", 115128.61, "21.45%", "多宝系列+日开/封闭固收理财，人民币计价"),
    ("债券及持有期固收（债基）", 31695.85, "5.91%", "纯债/短债/美元债/持有期固收基金"),
    ("股票及权益（股基/指数/QDII股票）", 14042.71, "2.62%", "港股/美股/券商/沪深300等指数与主动股基"),
    ("策略组合（帮你投6只）", 11185.34, "2.08%", "支付宝帮你投智能股债混合组合"),
    ("现金及货币", 7406.31, "1.38%", "货币基金、货币型"),
    ("合计", 536740.67, "100.00%", "全行总资产（人民币折算）"),
]
for row in _diag_alloc:
    for c, v in enumerate(row, 1):
        cell = ws8.cell(row=dr, column=c, value=v)
        cell.alignment = Alignment(horizontal="left" if c in (1, 4) else "center", vertical="center")
        if row[0] == "合计":
            cell.font = Font(bold=True)
    dr += 1
dr += 1

ws8.cell(row=dr, column=1, value="三、集中度风险").font = Font(size=12, bold=True, color="1F4E79")
dr += 1
_diag_conc3 = [
    "1. 币种集中度（最高风险）：美元敞口 ≈ 中行357,282 + 各美元债（南方亚洲美元债3,695 + 中银美元债6,382 + 富国亚收债QDII 1,734+3,378）≈ 372,471 元，占总资产约 69.4%。美元走弱将直接侵蚀人民币折算额。",
    "2. 平台集中度：中行（折人民币）357,282 元占全行 66.5%，单一平台占比过高；招行113,122(21.1%)、支付宝44,999(8.4%)、建行21,337(4.0%)。",
    "3. 发行方集中度：中银系（中行中银理财3只 + 支付宝中银美元债 + 中银国企债）合计超 27 万元，为最大单一发行方关联；招银系（招行代销招银理财 + 招行自身）次之。",
    "4. 单只占比：中行QDII日计划（16,000 USD折107,560元）为单只最大；招行多月宝50,065元占全行约9.3%。单只/单平台过大，流动性与信用风险难分散。",
    "5. 板块集中度：港股方向（富国港股互联网、富国恒生高股息、长城港通高股息）与美元债方向（南方亚洲美元债、中银美元债、富国亚收债）是主要亏损来源，呈明显方向性集中。",
]
for t in _diag_conc3:
    ws8.cell(row=dr, column=1, value=t).alignment = Alignment(wrap_text=True, vertical="top")
    ws8.merge_cells(start_row=dr, start_column=1, end_row=dr+1, end_column=8)
    ws8.row_dimensions[dr].height = 30
    dr += 2
dr += 1

ws8.cell(row=dr, column=1, value="四、收益与风险特征").font = Font(size=12, bold=True, color="1F4E79")
dr += 1
_diag_conc4 = [
    "1. 全行累计收益 +5,056 元（总回报约 +0.94%）；中行贡献约 +4,607 元（91%），其余三平台合计 +449 元，招行基金端仍亏 -499.86 元。",
    "2. 盈利源：中行美元理财（确定性较高）、QDII美股（嘉实美国成长+92.72、广发纳指+60.64、华宝纳指+26.34）、华宝核心优势混合（+250.78，定投效果显著）、帮你投策略（+224.09）。",
    "3. 亏损源（集中且方向性）：港股基金（富国中证港股通互联网ETF -540.75 / -31.26% 为全组合最大单只亏损）、证券ETF（天弘证券公司 -251.32 / -8.07%）、美元债（南方亚洲美元债 -102.76、中银美元债 -117.92、富国亚收债 -25.32 / -41.42）。",
    "4. 风险特征：整体低波动、低回撤，近似『货币+短债增强』画像；但隐性风险来自美元汇率与港股/美元债方向性暴露，而非传统股债波动。",
    "5. 定投痕迹明显（支付宝9只、招行/建行亦有定投），长期摊薄成本逻辑成立，但部分定投标的（港股、美元债）当前处于浮亏。",
]
for t in _diag_conc4:
    ws8.cell(row=dr, column=1, value=t).alignment = Alignment(wrap_text=True, vertical="top")
    ws8.merge_cells(start_row=dr, start_column=1, end_row=dr+1, end_column=8)
    ws8.row_dimensions[dr].height = 30
    dr += 2
dr += 1

ws8.cell(row=dr, column=1, value="五、费用情况").font = Font(size=12, bold=True, color="1F4E79")
dr += 1
ws8.cell(row=dr, column=1, value="当前数据未包含管理费、托管费、申购/赎回费、销售服务费等信息（截图未提供）。建议后续补充各产品费率，以评估『净值收益 - 费率』后的真实净回报；对小收益、短持有期产品，费率侵蚀效应尤为显著。").alignment = Alignment(wrap_text=True, vertical="top")
ws8.merge_cells(start_row=dr, start_column=1, end_row=dr+1, end_column=8)
ws8.row_dimensions[dr].height = 30
dr += 3

ws8.cell(row=dr, column=1, value="六、与风险偏好/期限/目标的匹配度").font = Font(size=12, bold=True, color="1F4E79")
dr += 1
ws8.cell(row=dr, column=1, value="用户未提供风险偏好/投资期限/理财目标/最大回撤参数，无法做定量匹配。仅从结构推断：组合呈现『高度稳健、近似保本』取向，适合『短期要用钱 / 极低回撤容忍』场景；若实际目标是『中长期保值增值』且能承受 -10%~-20% 波动，则当前权益暴露（2.6%）明显偏低，存在通胀侵蚀购买力的隐忧。请补齐参数以校准。").alignment = Alignment(wrap_text=True, vertical="top")
ws8.merge_cells(start_row=dr, start_column=1, end_row=dr+2, end_column=8)
ws8.row_dimensions[dr].height = 45
dr += 4

ws8.cell(row=dr, column=1, value="七、优化思路与再平衡方向（仅逻辑，无具体买卖指令）").font = Font(size=12, bold=True, color="1F4E79")
dr += 1
_diag_conc7 = [
    "1. 权益暴露偏低：若投资期限≥3年且能承受波动，可思考在组合中适度提升混合/权益比例，以对冲通胀与单一固收收益天花板；方向而非具体标的。",
    "2. 币种分散：美元敞口近七成，在机构对美元走弱的共识下，可思考分批锁定部分美元收益、或分散至非美资产，降低单一币种汇率风险。",
    "3. 平台/发行方分散：中行单平台占2/3，可思考跨平台、跨发行方分散，降低单一机构信用与流动性风险。",
    "4. 亏损方向审视：港股、美元债、证券ETF 是主要拖累，思考这些方向的持有逻辑是否成立、是否超配，而非简单止损或加仓。",
    "5. 流动性管理：多只产品锁定至 2026-09 至 2027-06（建行浦银09-28、中行2649号10-13、交银01-28、多月宝02-17），需提前规划到期现金流与再配置节奏。",
    "6. 成本意识：补齐费率后，对『收益≈费率』的产品思考保留必要性，避免费力不赚钱。",
]
for t in _diag_conc7:
    ws8.cell(row=dr, column=1, value=t).alignment = Alignment(wrap_text=True, vertical="top")
    ws8.merge_cells(start_row=dr, start_column=1, end_row=dr+1, end_column=8)
    ws8.row_dimensions[dr].height = 30
    dr += 2
dr += 1

ws8.cell(row=dr, column=1, value="八、优先关注事项清单（按重要性排序）").font = Font(size=12, bold=True, color="1F4E79")
dr += 1
for c, h in enumerate(["优先级", "事项", "原因"], 1):
    cell = ws8.cell(row=dr, column=c, value=h)
    cell.font = Font(bold=True, color="FFFFFF"); cell.fill = PatternFill("solid", fgColor="C00000")
    cell.alignment = Alignment(horizontal="center")
dr += 1
_diag_prio = [
    ("P1", "美元汇率敞口（66%仓位暴露在美元）", "当前最大单一风险点；美元走弱将直接减少人民币落袋额，需持续跟踪汇率与降息节奏"),
    ("P2", "近期到期现金流安排", "建行浦银09-28、中行2649号10-13、交银01-28、多月宝02-17 陆续到期，需规划再配置"),
    ("P3", "港股/美元债/证券ETF 亏损集中", "三大方向性亏损源合计拖累明显，审视持有逻辑与是否超配"),
    ("P4", "权益配置过低", "若期限长，2.6%权益难抗通胀；思考提升方向而非立即行动"),
    ("P5", "补齐费率数据", "评估真实净收益，识别『收益≈费率』的无效持仓"),
    ("P6", "补齐个人风险参数", "风险偏好/期限/目标/最大回撤，用于校准上述诊断匹配度"),
]
for row in _diag_prio:
    for c, v in enumerate(row, 1):
        cell = ws8.cell(row=dr, column=c, value=v)
        cell.alignment = Alignment(horizontal="center" if c == 1 else "left", vertical="top", wrap_text=True)
    ws8.row_dimensions[dr].height = 30
    dr += 1
dr += 1

ws8.cell(row=dr, column=1, value="※ 本分析由 WorkBuddy 基于用户提供的持仓截图客观整理与推演，仅供参考，不构成任何具体的买入/卖出投资建议。投资有风险，决策需结合自身情况。").font = Font(size=9, italic=True, color="808080")
ws8.merge_cells(start_row=dr, start_column=1, end_row=dr, end_column=8)

for c, w in enumerate([16, 30, 14, 40, 14, 14, 14, 14], 1):
    ws8.column_dimensions[openpyxl.utils.get_column_letter(c)].width = w

# ============ Sheet9: 美元敞口压力测试 ============
ws9 = wb.create_sheet("美元敞口压力测试")
ws9["A1"] = "美元敞口压力测试（纯数学推演 · 非投资建议）"
ws9["A1"].font = Font(size=14, bold=True, color="1F4E79")
ws9["A2"] = "统计日 2026-08-27 ｜ 中行5只美元理财本金 53,147.17 USD（≈%.0f 元@即期%.4f）｜ 全行总资产≈%.0f 元" % (total_mv_cny, rate_now, grand_total_mv_all)
ws9["A2"].font = Font(size=9, color="808080")

scen = [
    ("美元大幅走强（回到一年前 7.156）", 7.1560),
    ("美元走强（6.8500）", 6.8500),
    ("当前基准（%.4f）" % rate_now, rate_now),
    ("美元走弱（降息预期 6.5500）", 6.5500),
    ("美元大幅走弱（6.4000）", 6.4000),
]

# 表1：中行美元敞口情景价值
r = 4
ws9.cell(row=r, column=1, value="表1 ｜ 中行美元敞口（53,147.17 USD）情景价值").font = Font(bold=True, size=11, color="1F4E79")
r += 1
for c, h in enumerate(["情景", "假设汇率", "折人民币(元)", "较当前(元)"], 1):
    cell = ws9.cell(row=r, column=c, value=h)
    cell.font = Font(bold=True, color="FFFFFF")
    cell.fill = PatternFill("solid", fgColor="1F4E79")
    cell.alignment = Alignment(horizontal="center")
r += 1
for name, rate in scen:
    cny = total_mv_usd * rate
    delta = cny - total_mv_cny
    for c, v in enumerate([name, rate, round(cny, 2), round(delta, 2)], 1):
        cell = ws9.cell(row=r, column=c, value=v)
        cell.alignment = Alignment(horizontal="left" if c == 1 else "center")
        if c == 4:
            cell.font = Font(color="C00000" if delta >= 0 else "008000")
    r += 1

# 表2：降敞口风险对冲效果
r += 2
ws9.cell(row=r, column=1, value="表2 ｜ 若将美元敞口降至 50%/40%（等值美元赎回转人民币资产）的风险对冲效果").font = Font(bold=True, size=11, color="1F4E79")
r += 1
for c, h in enumerate(["降敞口目标", "转出美元敞口(人民币等值)", "弱到6.55 少亏", "弱到6.40 少亏", "强到6.85 少赚", "强到7.156 少赚"], 1):
    cell = ws9.cell(row=r, column=c, value=h)
    cell.font = Font(bold=True, color="FFFFFF")
    cell.fill = PatternFill("solid", fgColor="1F4E79")
    cell.alignment = Alignment(horizontal="center", wrap_text=True)
r += 1
for target in [0.50, 0.40]:
    target_cny = grand_total_mv_all * target
    transfer = total_mv_cny - target_cny
    loss_655 = transfer * (rate_now - 6.5500) / rate_now
    loss_640 = transfer * (rate_now - 6.4000) / rate_now
    gain_685 = transfer * (6.8500 - rate_now) / rate_now
    gain_7156 = transfer * (7.1560 - rate_now) / rate_now
    for c, v in enumerate(["降到 %.0f%%" % (target * 100), round(transfer, 2), round(loss_655, 2), round(loss_640, 2), round(-gain_685, 2), round(-gain_7156, 2)], 1):
        cell = ws9.cell(row=r, column=c, value=v)
        cell.alignment = Alignment(horizontal="center")
        if c in (3, 4):
            cell.font = Font(color="008000")
        elif c in (5, 6):
            cell.font = Font(color="808080")
    r += 1

r += 2
for i, t in enumerate([
    "说明1：纯数学推演，不含任何买卖建议。降敞口=将等值美元资产赎回并转为人民币资产（假设无损转换，未计赎回费/在途时间/再投资收益率）。",
    "说明2：『少亏』=美元走弱时你避免的人民币损失（风险降低额，绿色为正向保护）；『少赚』=美元走强时你放弃的潜在收益（对称代价，灰色）。",
    "说明3：当前美元敞口占全行约 %.0f%%，降敞口在减少下行风险的同时，也对称放弃了美元走强的上行收益，需结合自身判断。" % (total_mv_cny / grand_total_mv_all * 100),
    "说明4：汇率为示意情景非预测；实际中行产品另有自身收益（累计+685 USD），本表仅测汇率端敞口，未叠加产品收益波动。",
]):
    ws9.cell(row=r + i, column=1, value=t).font = Font(italic=True, size=9, color="808080")

for c, w in enumerate([34, 22, 16, 16, 16, 16], 1):
    ws9.column_dimensions[openpyxl.utils.get_column_letter(c)].width = w

# 确保输出目录存在（04_成果/ 可能因手动清理被删，openpyxl 不会自动建目录）
os.makedirs(os.path.dirname(OUT_FILE), exist_ok=True)
wb.save(OUT_FILE)
print("OK | 中行USD=%.2f->CNY≈%.0f | 招行=%.2f | 建行=%.2f | 支付宝=%.2f | 全行≈%.0f | 全行收益≈%+.0f" %
      (total_mv_usd, total_mv_cny, cmb_total_mv, ccb_total_mv, alipay_total_mv, grand_total_mv_all, grand_total_profit_all))
