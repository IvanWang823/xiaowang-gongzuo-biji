import re, json
s=open("辽宁省上网侧电价2026年7月热力图.html",encoding="utf-8",errors="ignore").read()

def grab(name):
    # 找 const/let/var name = [[...]] 形式
    m=re.search(r'(?:const|let|var)\s+'+name+r'\s*=\s*(\[\[.*?\]\])\s*;', s, re.S)
    if not m:
        # 退而求其次：name = [ 开头
        m=re.search(name+r'\s*=\s*(\[\[.*?\]\])', s, re.S)
    if not m:
        return None
    txt=m.group(1)
    # 解析二维数组
    try:
        arr=json.loads(txt)
    except Exception as e:
        # 数字里可能有 负数/小数，json 能处理；若失败打印片段
        print(f"  {name} JSON解析失败: {e}; 片段={txt[:80]}")
        return None
    return arr

for n in ["before","realTime"]:
    arr=grab(n)
    if arr is None:
        print(f"{n}: 未提取到"); continue
    rows=len(arr); cols=len(arr[0]) if arr else 0
    flat=[v for r in arr for v in r]
    print(f"{n}: {rows} 行 × {cols} 列 | 样本行1前5={arr[0][:5]} | 样本行2前3={arr[1][:3]} | 全表min={min(flat):.1f} max={max(flat):.1f}")
    json.dump(arr, open(f"_heat_{n}.json","w"))
    print(f"  已存 _heat_{n}.json")
