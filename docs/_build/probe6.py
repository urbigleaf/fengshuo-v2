import os,re,json
D=r'D:\user\Documents\GitHub\fengshuo\docs'
raw=open(os.path.join(D,'2008-寓言冯硕个人作品展','index.html'),'rb').read()
a=raw.find(b'<main'); b=raw.find(b'</main>')
seg=raw[a:b].decode('utf-8')
ps=re.findall(r'<p[^>]*>(.*?)</p>', seg, re.S|re.I)
print('p count', len(ps))
for i,x in enumerate(ps):
    t=re.sub(r'<br\s*/?>','\n',x)
    t=re.sub(r'<[^>]+>','',t).strip()
    print('--- p%d len=%d'%(i,len(t)))
    print(t[:120].replace('\n','\\n'))