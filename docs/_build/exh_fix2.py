import io,re,os,json
D=r'D:\user\Documents\GitHub\fengshuo\docs'

def looks_mojibake(t):
    # mojibake: many chars in the "garbage" CJK ranges produced by gbk->utf8 confusion
    junk=set('锛銆鑻鍥涘鏄涓€簰鐨勪簡鍜屽湪涓婃槸')
    n=sum(1 for ch in t if ch in '锛銆鑻鍥涘鏄簰鐨勪簡鍜屽湪閫犳€')
    return n >= 2

def repair(t):
    for _ in range(2):
        try:
            b=t.encode('gbk')
        except Exception:
            return t
        try:
            c=b.decode('utf-8')
        except Exception:
            return t
        if c and c!=t: t=c
        else: return t
    return t

def is_ok(t): return not looks_mojibake(t) and '\ufffd' not in t

out={}
for key,name in [('2008','2008-寓言冯硕个人作品展'),('2012','2012-狂欢冯硕个人作品展')]:
    raw=open(os.path.join(D,name,'index.html'),'rb').read()
    s=raw.decode('utf-8','replace')
    m=re.search(r'<main[^>]*>(.*?)</main>', s, re.S)
    body=m.group(1) if m else ''
    body=re.sub(r'<(script|style|nav|footer)\b.*?</\1>','',body,flags=re.S)
    imgs=re.findall(r'<img[^>]+src="([^"]+)"', body)
    ps=re.findall(r'<p[^>]*>(.*?)</p>', body, re.S)
    txt=[re.sub(r'\s+',' ',re.sub(r'<[^>]+>','',x)).strip() for x in ps]
    txt=[t for t in txt if len(t)>1]
    fixed=[t if is_ok(t) else repair(t) for t in txt]
    out[key]={'paras':fixed,'imgs':imgs}
    print('==',key,'paras',len(fixed))
    for i,(a,b) in enumerate(zip(txt,fixed)):
        if a!=b: print('   repaired p%d: %s'%(i, b[:45]))
io.open(r'D:\user\Documents\GitHub\fengshuo_v1\_build\exh_raw.json','w',encoding='utf-8').write(json.dumps(out,ensure_ascii=False,indent=1))
bad=[(k,i) for k in out for i,t in enumerate(out[k]['paras']) if not is_ok(t)]
print('remaining bad:', bad)
print('p10 2012:', out['2012']['paras'][10])
print('2008 p4:', out['2008']['paras'][4][:60])