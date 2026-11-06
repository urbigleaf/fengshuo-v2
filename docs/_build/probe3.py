import os,re
D=r'D:\user\Documents\GitHub\fengshuo\docs'
raw=open(os.path.join(D,'2008-寓言冯硕个人作品展','index.html'),'rb').read()
i=raw.find(b'\xe5\xb1\x95\xe8\xa7\x88\xe5\x89\x8d\xe8\xa8\x80')   # "展览前言" in utf8
j=raw.find('展览前言'.encode('utf-8'))
print('utf8 hit for 展览前言:', i, j)
# show raw bytes around first <p> of the preface
k=raw.find(b'\x3c\x70\x3e')  
for probe in [b'\xe5\xb1\x95', b'\xe5\xb1\xb1', b'\xe6\x99\x9d']:
    print(probe, 'count', raw.count(probe))
print('total bytes', len(raw))
# check whether file is gbk-encoded
try:
    raw.decode('gbk'); print('gbk decodable: True')
except Exception as e: print('gbk decodable: False', str(e)[:80])
try:
    s=raw.decode('gbk')
    m=re.search(r'<main[^>]*>(.*?)</main>', s, re.S)
    ps=re.findall(r'<p[^>]*>(.*?)</p>', m.group(1), re.S)
    t=[re.sub(r'<[^>]+>','',x).strip() for x in ps if len(re.sub(r'<[^>]+>','',x).strip())>1]
    print('GBK decode p4:', t[4][:70])
    print('GBK decode p7:', t[7][:40])
except Exception as e:
    print('gbk main parse fail', e)