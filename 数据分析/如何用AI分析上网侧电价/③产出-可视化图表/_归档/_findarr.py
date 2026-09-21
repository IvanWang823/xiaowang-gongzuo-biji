import re
s=open("辽宁省上网侧电价2026年7月热力图.html",encoding="utf-8",errors="ignore").read()
# 找所有带数字的中括号数组，按命中长度排序
cands=re.findall(r'\[\[[-0-9.,\s]{50,}\]\]', s)
cands+=re.findall(r'\[[-0-9.,\s]{50,}\]', s)
cands.sort(key=len, reverse=True)
print("候选数组数:", len(cands))
for i,c in enumerate(cands[:4]):
    print(f"\n--- 候选#{i} 长度={len(c)} ---")
    print(c[:200])
# 也找变量赋值（含 before/realTime/heat/data 等关键词附近）
print("\n===== before/realTime/heat/data 关键词上下文 =====")
for kw in ["before","realTime","real","data","heat","matrix","arr","rows"]:
    idx=s.find(kw)
    if idx>=0:
        print(f"  '{kw}' @ {idx}: ...{s[idx-30:idx+80].replace(chr(10),' ')}...")
