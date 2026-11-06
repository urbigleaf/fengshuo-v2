import io,re,os
D=r'D:\user\Documents\GitHub\fengshuo\docs'
p=os.path.join(D,'2012-狂欢冯硕个人作品展','index.html')
raw=open(p,'rb').read()
print('bytes:', len(raw))
print('meta charset:', re.findall(rb'charset=["\']?([\w-]+)', raw[:2000]))
for enc in ('utf-8','gb18030'):
    try:
        s=raw.decode(enc)
        m=re.search(r'<main[^>]*>(.*?)</main>', s, re.S)
        body=m.group(1) if m else ''
        ps=re.findall(r'<p[^>]*>(.*?)</p>', body, re.S)
        t8=re.sub(r'\s+',' ',re.sub(r'<[^>]+>','',ps[8])) if len(ps)>8 else ''
        print('---', enc, 'p8 head:', t8[:60])
    except Exception as e:
        print('---', enc, 'FAIL', e)