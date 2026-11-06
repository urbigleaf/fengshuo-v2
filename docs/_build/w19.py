import io,os,re,json
R=r'D:\user\Documents\GitHub\fengshuo_v1'
out=[]
for f in ['exhibitions\\2008-tales.html','exhibitions\\2012-carnival.html']:
    p=os.path.join(R,f)
    s=io.open(p,encoding='utf-8').read()
    ps=re.findall(r'<p>(.*?)</p>', s, re.S)
    txt=''.join(re.sub(r'<[^>]+>','',x) for x in ps)
    first=ps[0][:6] if ps else ''
    cps=' '.join('U+%04X'%ord(c) for c in first)
    han=sum(1 for c in txt if '\u4e00'<=c<='\u9fff')
    ascii_=sum(1 for c in txt if c.isascii())
    print('%s chars=%d han=%d ascii=%d' % (f, len(txt), han, ascii_))
    print('   first6 codepoints:', cps)