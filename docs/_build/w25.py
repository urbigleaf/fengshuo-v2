import os,re,json,html
D=r'D:\user\Documents\GitHub\fengshuo\docs'
def ext(p):
    raw=open(p,'rb').read()
    a=raw.find(b'<main'); b=raw.find(b'</main>')
    s=raw[a:b].decode('utf-8')
    s=re.sub(r'<(script|style)\b.*?</\1>','',s,flags=re.S|re.I)
    ps=re.findall(r'<p[^>]*>(.*?)</p>', s, re.S|re.I)
    out=[]
    for x in ps:
        t=re.sub(r'<br\s*/?>','\n',x)
        t=re.sub(r'<[^>]+>','',t)
        t=html.unescape(t)
        t=re.sub(r'[ \t\u3000]+',' ',t)
        t=re.sub(r'\n{3,}','\n\n',t).strip()
        if t: out.append(t)
    imgs=re.findall(r'<img[^>]+src="([^"]+)"', s)
    return out,imgs
res={}
for key,name in [('2008','en\\2008-feng-shuo-tales-at-marlborough-chelsea'),
                 ('2012','en\\2012-feng-shuo-the-carnivalesque-at-m-art-center')]:
    p,i=ext(os.path.join(D,name,'index.html'))
    res[key]={'paras':p,'imgs':i}
    print('==',key,'paras',len(p),'imgs',len(i),'chars',sum(len(t) for t in p))
    for n,t in enumerate(p): print('   p%d (%d): %s'%(n,len(t),t[:80]))
open(r'D:\user\Documents\GitHub\fengshuo_v1\_build\exh_en.json','wb').write(json.dumps(res,ensure_ascii=False,indent=1).encode('utf-8'))
print('saved exh_en.json')