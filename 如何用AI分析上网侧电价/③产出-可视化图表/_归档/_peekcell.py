import re
s=open("辽宁省上网侧电价2026年7月热力图.html",encoding="utf-8",errors="ignore").read()
# 找第一个完整 cell 标签（含所有属性）
cells=re.findall(r'<div class="cell"[^>]*>', s)
print("cell 标签总数:", len(cells))
print("\n前 3 个 cell 完整结构:")
for c in cells[:3]:
    print("  ", c)
print("\n含 data- 属性名统计（属性键值）:")
attrs=re.findall(r'data-[a-z]+=', s)
from collections import Counter
print("  ", Counter(attrs))
# 看一个带 data 值的样本
m=re.search(r'<div class="cells"[^>]*>(.*?)</div>\s*</div>', s, re.S)
if m:
    print("\n第一个 cells 容器前 400 字符:")
    print(m.group(1)[:400])
