import io,re,os,json
D=r'D:\user\Documents\GitHub\fengshuo\docs'
out={}
for key,name in [('2008','2008-寓言冯硕个人作品展'),('2012','2012-狂欢冯硕个人作品展')]:
    p=os.path.join(D,name,'index.html')
    s=io.open(p,encoding='utf-8',errors='replace').read()
    m=re.search(r'<main[^>]*>(.*?)</main>', s, re.S)
    body=m.group(1) if m else ''
    # strip share/nav noise
    body=re.sub(r'<(script|style|nav|footer)\b.*?</\1>','',body,flags=re.S)
    imgs=re.findall(r'<img[^>]+src="([^"]+)"', body)
    ps=re.findall(r'<p[^>]*>(.*?)</p>', body, re.S)
    txt=[re.sub(r'\s+',' ',re.sub(r'<[^>]+>','',x)).strip() for x in ps]
    txt=[t for t in txt if len(t)>1]
    out[key]={'paras':txt,'imgs':imgs}
    print('==',key,'| paras',len(txt),'| imgs',len(imgs))
json.dump(out, io.open(r'D:\user\Documents\GitHub\fengshuo_v1\_build\exh_raw.json','w',encoding='utf-8'), ensure_ascii=False, indent=1)
# verify image files exist
miss=[]
for k,v in out.items():
    for u in v['imgs']:
        rp=os.path.join(D, u.lstrip('/').replace('/','\\'))
        if not os.path.exists(rp): miss.append((k,u))
print('missing imgs:', len(miss))
for x in miss[:20]: print('  MISS', x)