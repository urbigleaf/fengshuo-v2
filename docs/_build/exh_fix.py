import io,re,os,json
D=r'D:\user\Documents\GitHub\fengshuo\docs'
def fixpath(s):
    try: return s
    except: return s
out={}
for key,name in [('2008','2008-寓言冯硕个人作品展'),('2012','2012-狂欢冯硕个人作品展')]:
    raw=open(os.path.join(D,name,'index.html'),'rb').read()
    s=raw.decode('utf-8')
    m=re.search(r'<main[^>]*>(.*?)</main>', s, re.S)
    body=m.group(1) if m else ''
    body=re.sub(r'<(script|style|nav|footer)\b.*?</\1>','',body,flags=re.S)
    imgs=re.findall(r'<img[^>]+src="([^"]+)"', body)
    ps=re.findall(r'<p[^>]*>(.*?)</p>', body, re.S)
    txt=[re.sub(r'\s+',' ',re.sub(r'<[^>]+>','',x)).strip() for x in ps]
    txt=[t for t in txt if len(t)>1]
    # repair the mojibake: text that decodes as utf8-from-gbk
    fixed=[]
    for t in txt:
        try:
            cand=t.encode('gbk','ignore').decode('utf-8')
            if cand and sum('\u4e00'<=ch<='\u9fff' for ch in cand) >= sum('\u4e00'<=ch<='\u9fff' for ch in t):
                t=cand
        except Exception:
            pass
        fixed.append(t)
    out[key]={'paras':fixed,'imgs':imgs}
raw=json.dumps(out, ensure_ascii=False, indent=1)
io.open(r'D:\user\Documents\GitHub\fengshuo_v1\_build\exh_raw.json','w',encoding='utf-8').write(raw)
rep=[]
for k in ('2008','2012'):
    for i,t in enumerate(out[k]['paras']):
        bad=sum(1 for ch in t if '\u4e00'<=ch<='\u9fff')>0
        moj=('锛' in t or '鏄' in t or '涓' in t or '鑻' in t)
        rep.append((k,i,len(t),moj))
print('paras:', len(rep))
print('still mojibake:', [ (k,i) for k,i,l,m in rep if m ])
print('p8 2012:', out['2012']['paras'][8][:50])
print('p9 2012:', out['2012']['paras'][9][:50])
print('p10 2012:', out['2012']['paras'][10])
print('img sample:', out['2012']['imgs'][0].split('/')[-1])