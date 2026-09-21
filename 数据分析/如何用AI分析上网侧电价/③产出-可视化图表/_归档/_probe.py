import re, os
files=[
 "辽宁省上网侧电价2026年7月典型日曲线图.html",
 "辽宁省上网侧电价2026年7月负价时段指纹图.html",
 "辽宁省上网侧电价2026年7月_气象代理vs负价.html",
 "辽宁省上网侧电价2026年7月_辐照深挖.html",
 "辽宁省上网侧电价2026年7月_偏差与套利.html",
 "辽宁省电价市场机制机理图.html",
 "辽宁省电源分布示意图.html",
]
for f in files:
    s=open(f,encoding="utf-8",errors="ignore").read()
    has_svg = "<svg" in s
    has_data = len(re.findall(r'data-v="', s))
    has_canvas = "<canvas" in s
    # 最长数字数组
    cands=re.findall(r'\[[-0-9.,\s]{20,}\]', s)
    cands.sort(key=len,reverse=True)
    longest = cands[0][:120] if cands else "(无)"
    # 变量名线索
    vars_=sorted(set(re.findall(r'(?:const|let|var)\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*=', s)))
    print(f"\n### {f} ({len(s)}B) svg={has_svg} canvas={has_canvas} data-v点数={has_data}")
    print(f"  变量:{vars_[:12]}")
    print(f"  最长数组片段: {longest}")
