import re
f="辽宁省上网侧电价2026年7月热力图.html"
s=open(f,encoding="utf-8",errors="ignore").read()
print("文件总长:",len(s))
# 找 echarts.init / option 变量名
for kw in ["echarts.init","setOption","heatmap","xAxis","yAxis","categories","data:","var ","let ","const ","visualMap","min:","max:"]:
    print(f"  {kw:14} 出现 {s.count(kw)} 次")
print("\n===== 前 2500 字符（看结构） =====")
print(s[:2500])
