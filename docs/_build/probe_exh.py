import io,re,os
from html.parser import HTMLParser
D=r'D:\user\Documents\GitHub\fengshuo\docs'
for name in ['2008-寓言冯硕个人作品展','2012-狂欢冯硕个人作品展']:
    p=os.path.join(D,name,'index.html')
    s=io.open(p,encoding='utf-8',errors='replace').read()
    m=re.search(r'<main[^>]*>(.*?)</main>', s, re.S) or re.search(r'<div class="entry-content[^"]*">(.*?)</article>', s, re.S)
    body=m.group(1) if m else ''
    imgs=re.findall(r'<img[^>]+src="([^"]+)"', body)
    ps=re.findall(r'<p[^>]*>(.*?)</p>', body, re.S)
    txt=[re.sub(r'<[^>]+>','',x).strip() for x in ps]
    txt=[t for t in txt if t]
    print('='*60)
    print(name)
    print(' body chars:', len(body), '| imgs:', len(imgs), '| <p>:', len(ps))
    print(' text chars:', sum(len(t) for t in txt))
    for i,t in enumerate(txt[:6]): print('  p%d: %s' % (i, t[:110].replace('\n',' ')))
    for u in imgs[:8]: print('  img:', u.split('/')[-1])