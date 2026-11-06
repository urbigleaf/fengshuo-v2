import os,re,json
D=r'D:\user\Documents\GitHub\fengshuo\docs'
def extract(path):
    raw=open(path,'rb').read()
    a=raw.find(b'<main'); b=raw.find(b'</main>')
    seg=raw[a:b].decode('utf-8')
    seg=re.sub(r'<(script|style)\b.*?</\1>','',seg,flags=re.S|re.I)
    ps=re.findall(r'<p[^>]*>(.*?)</p>', seg, re.S|re.I)
    out=[]
    for x in ps:
        t=re.sub(r'<br\s*/?>','\n',x)
        t=re.sub(r'<[^>]+>','',t)
        t=re.sub(r'[ \t\u3000]+',' ',t)
        t=re.sub(r'\n{3,}','\n\n',t).strip()
        if t: out.append(t)
    imgs=[u for u in re.findall(r'<img[^>]+src="([^"]+)"', seg)]
    return out, imgs
res={}
for key,name in [('2008','2008-寓言冯硕个人作品展'),('2012','2012-狂欢冯硕个人作品展')]:
    p,i=extract(os.path.join(D,name,'index.html'))
    res[key]={'paras':p,'imgs':i}
    print(key,'paras',len(p),'imgs',len(i),'chars',sum(len(t) for t in p))
# write with explicit utf-8, and dump a human-readable txt for verification
open(r'D:\user\Documents\GitHub\fengshuo_v1\_build\exh_full.json','wb').write(json.dumps(res,ensure_ascii=False,indent=1).encode('utf-8'))
with open(r'D:\user\Documents\GitHub\fengshuo_v1\_build\exh_full.txt','wb') as f:
    for k,v in res.items():
        f.write(('===== %s =====\n'%k).encode('utf-8'))
        for i,t in enumerate(v['paras']): f.write(('--- p%d ---\n%s\n'%(i,t)).encode('utf-8'))
        for u in v['imgs']: f.write(('IMG %s\n'%u).encode('utf-8'))
print('written json+txt OK')