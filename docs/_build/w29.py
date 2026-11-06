import json,os,re,html
D=r'D:\user\Documents\GitHub\fengshuo\docs'
# re-extract cleanly (no mangling) and store
def ext(p):
    raw=open(p,'rb').read()
    a=raw.find(b'<main'); b=raw.find(b'</main>')
    s=raw[a:b].decode('utf-8')
    s=re.sub(r'<(script|style)\b.*?</\1>','',s,flags=re.S|re.I)
    ps=re.findall(r'<p[^>]*>(.*?)</p>', s, re.S|re.I)
    out=[]
    for x in ps:
        t=re.sub(r'<br\s*/?>','\n',x)
        t=re.sub(r'<[^>]+>','',t)
        t=html.unescape(t)
        t=re.sub(r'[ \t\u3000]+',' ',t)
        t=re.sub(r'\n{3,}','\n\n',t).strip()
        if t: out.append(t)
    return out, re.findall(r'<img[^>]+src="([^"]+)"', s)
res={}
for key,name in [('2008','en\\2008-feng-shuo-tales-at-marlborough-chelsea'),
                 ('2012','en\\2012-feng-shuo-the-carnivalesque-at-m-art-center')]:
    p,i=ext(os.path.join(D,name,'index.html'))
    res[key]={'paras':p,'imgs':i}
open(r'D:\user\Documents\GitHub\fengshuo_v1\_build\exh_en.json','wb').write(json.dumps(res,ensure_ascii=False,indent=1).encode('utf-8'))
t=res['2012']['paras'][1]
i=t.find('Feng Shuo'); seg=t[i:i+22]
print('re-extracted. apostrophe codepoints:', ' '.join('U+%04X'%ord(c) for c in seg[9:13]))
print('paras 2008/2012:', len(res['2008']['paras']), len(res['2012']['paras']))
print('2008 img count:', len(res['2008']['imgs']), '| 2012:', len(res['2012']['imgs']))