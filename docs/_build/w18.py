import os,re,json
D=r'D:\user\Documents\GitHub\fengshuo\docs'
p=os.path.join(D,'2008-寓言冯硕个人作品展','index.html')
raw=open(p,'rb').read()
a=raw.find(b'<main'); b=raw.find(b'</main>')
seg=raw[a:b]
print('1) raw bytes in main contain UTF-8 of 展览前言:', seg.find('展览前言'.encode('utf-8')) >= 0)
s=seg.decode('utf-8')
print('2) decoded str contains 展览前言:', '展览前言' in s)
ps=re.findall(r'<p[^>]*>(.*?)</p>', s, re.S|re.I)
t=re.sub(r'<[^>]+>','',ps[4])
print('3) p4 text contains 展览前言:', '展览前言' in t, '| head:', t.strip()[:14])
# now the JSON round-trip test
js=json.dumps({'x':t[:20]}, ensure_ascii=False)
back=json.loads(js)['x']
print('4) json roundtrip identical:', back==t[:20], '| head:', back[:10])
# and file roundtrip
open(r'D:\user\Documents\GitHub\fengshuo_v1\_build\_t.json','wb').write(js.encode('utf-8'))
rt=json.load(open(r'D:\user\Documents\GitHub\fengshuo_v1\_build\_t.json',encoding='utf-8'))['x']
print('5) file roundtrip identical:', rt==t[:20], '| head:', rt[:10])