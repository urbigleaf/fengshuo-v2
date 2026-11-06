import os,re
D=r'D:\user\Documents\GitHub\fengshuo\docs'
for name in ['en\\2008-feng-shuo-tales-at-marlborough-chelsea','en\\2012-feng-shuo-the-carnivalesque-at-m-art-center']:
    p=os.path.join(D,name,'index.html')
    raw=open(p,'rb').read()
    print('==',name,'bytes',len(raw))
    a=raw.find(b'<main'); b=raw.find(b'</main>')
    print('   has <main>:', a>=0)
    seg=raw[a:b] if a>=0 else raw
    s=seg.decode('utf-8','replace')
    ps=re.findall(r'<p[^>]*>(.*?)</p>', s, re.S|re.I)
    txt=[re.sub(r'\s+',' ',re.sub(r'<[^>]+>','',x)).strip() for x in ps]
    txt=[t for t in txt if len(t)>1]
    imgs=re.findall(r'<img[^>]+src="([^"]+)"', s)
    print('   paras',len(txt),'imgs',len(imgs),'chars',sum(len(t) for t in txt))
    for i,t in enumerate(txt[:4]): print('    p%d: %s'%(i,t[:90]))