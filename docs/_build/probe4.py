import os,re,json
D=r'D:\user\Documents\GitHub\fengshuo\docs'
raw=open(os.path.join(D,'2008-寓言冯硕个人作品展','index.html'),'rb').read()
s=raw.decode('utf-8')
m=re.search(r'<main[^>]*>(.*?)</main>', s, re.S)
body=m.group(1)
ps=re.findall(r'<p[^>]*>(.*?)</p>', body, re.S)
out=[]
for i,x in enumerate(ps):
    t=re.sub(r'\s+',' ',re.sub(r'<[^>]+>','',x)).strip()
    out.append(t)
res={'paras':out,'n':len(ps)}
open(r'D:\user\Documents\GitHub\fengshuo_v1\_build\p2008.json','wb').write(json.dumps(res,ensure_ascii=False,indent=1).encode('utf-8'))
print('wrote p2008.json, paras', len(out))