import re
def show(f, names, n=160):
    s=open(f,encoding="utf-8",errors="ignore").read()
    print(f"\n========== {f} ==========")
    for nm in names:
        # 找 const/let/var nm = 或 nm=[ 或 nm={
        m=re.search(r'(?:const|let|var)\s+'+nm+r'\s*=\s*([\[{][\s\S]{0,400}?)\s*[;\]\)]', s)
        if not m:
            m=re.search(nm+r'\s*=\s*([\[{][\s\S]{0,400}?)[\];]', s)
        if m:
            print(f"\n-- {nm} -- {m.group(1)[:n]}")
        else:
            print(f"\n-- {nm} -- (未找到)")
# 典型日：找 DATA / PRESETS
show("辽宁省上网侧电价2026年7月典型日曲线图.html", ["DATA","PRESETS","W"])
# 辐照
show("辽宁省上网侧电价2026年7月_辐照深挖.html", ["Y","Yp","Yr","X","D"])
# 偏差套利
show("辽宁省上网侧电价2026年7月_偏差与套利.html", ["vals","D","mn"])
# 电源分布
show("辽宁省电源分布示意图.html", ["listData","TYPES","POINTS","markers"])
