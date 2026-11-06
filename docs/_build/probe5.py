import os,re
D=r'D:\user\Documents\GitHub\fengshuo\docs'
raw=open(os.path.join(D,'2008-寓言冯硕个人作品展','index.html'),'rb').read()
# locate the <main> region in bytes
a=raw.find(b'<main'); b=raw.find(b'</main>')
seg=raw[a:b]
print('main bytes', len(seg))
# find a <p> containing bytes for the mojibake of 展览前言
i=seg.find('展览前言'.encode('utf-8'))
print('mojibake-utf8 hit in main:', i)
cand=seg[i:i+200] if i>=0 else seg[:200]
print('bytes repr:', repr(cand[:60]))
tests={}
for enc in ('utf-8','gbk','gb18030','big5','cp936-safe'): pass
# direction A: bytes are utf-8 of mojibake text -> encode back to gbk? test both
for name,fn in [
  ('utf8->gbk->utf8', lambda s: s.encode('gbk','ignore').decode('utf-8','replace')),
  ('utf8->latin1->gbk', lambda s: s.encode('latin1','ignore').decode('gbk','replace')),
]:
    try:
        s=cand.decode('utf-8','replace')
        print(name, '=>', fn(s)[:50])
    except Exception as e:
        print(name,'fail',e)
# maybe main is GBK bytes that decode correctly with gb18030
try:
    print('gb18030 main p:', seg[i:i+120].decode('gb18030','replace')[:50])
except Exception as e:
    print('gb18030 fail', e)