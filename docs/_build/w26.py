import os,json,io,re
p=r'D:\user\Documents\GitHub\fengshuo_v1\_build\exh_en.json'
d=json.load(open(p,encoding='utf-8'))
def fix(t):
    # 鈥? / 鈥檚 pattern = UTF-8 apostrophe bytes misread; repair via cp1252->utf8
    out=[]
    for ch in t: out.append(ch)
    s=''.join(out)
    try:
        cand=s.encode('gbk','ignore').decode('utf-8','ignore')
        if cand.count('\u2019')>s.count('\u2019') or '鈥' in s:
            s2=s.replace('鈥檚',"'s").replace('鈥檛',"'t").replace('鈥',"'")
            s=s2
    except Exception: pass
    return s
for k in d:
    d[k]['paras']=[fix(t) for t in d[k]['paras']]
bad=[(k,i) for k in d for i,t in enumerate(d[k]['paras']) if '鈥' in t or '\ufffd' in t]
print('remaining bad:', bad)
print('sample:', d['2012']['paras'][1][:70])
print('sample2:', d['2008']['paras'][6][:70])
open(p,'wb').write(json.dumps(d,ensure_ascii=False,indent=1).encode('utf-8'))
print('saved')