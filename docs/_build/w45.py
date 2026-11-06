import io
p=r'D:\user\Documents\GitHub\fengshuo_v1\assets\css\site.css'
c=io.open(p,encoding='utf-8').read()
add='''
/* linked exhibition entries with thumbnails */
.exh--linked{position:relative}
.exh__thumb{
  width:clamp(56px,7vw,84px);height:72px;object-fit:cover;object-position:center 22%;
  flex:0 0 auto;margin-right:clamp(10px,1.6vw,20px);
  background:var(--surface);filter:saturate(.95);transition:filter .5s var(--ease)}
.exh--linked:hover .exh__thumb{filter:saturate(1.05)}
/* exhibition body: dual-language blocks */
.exhbody>div[data-lang]{display:none}
html[data-lang="zh"] .exhbody>div[data-lang="zh"],
html[data-lang="en"] .exhbody>div[data-lang="en"]{display:block}
.exhbody div[data-lang="en"] p{text-indent:0;line-height:1.8}
.exhposter{margin:0 auto;max-width:min(340px,62vw);line-height:0}
.exhposter img{width:100%;height:auto;display:block;box-shadow:0 18px 44px rgba(0,0,0,.34)}
.sect-back{margin-top:1.4em}
'''
if '.exh--linked' not in c:
    c=c.rstrip()+'\n'+add
io.open(p,'w',encoding='utf-8',newline='\n').write(c)
print('site.css', len(c))