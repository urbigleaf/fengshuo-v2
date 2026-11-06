import io
p=r'D:\user\Documents\GitHub\fengshuo_v1\assets\css\site.css'
c=io.open(p,encoding='utf-8').read()
add='''
/* ---- exhibition pages ---- */
.exh-meta dl{
  display:grid;grid-template-columns:max-content 1fr;
  gap:.55em clamp(14px,2vw,28px);margin:0;max-width:62ch;
  border-top:1px solid var(--line);padding-top:clamp(14px,2vw,22px)}
.exh-meta dt{
  font-size:.72rem;letter-spacing:.16em;text-transform:uppercase;
  color:var(--ink-dim);padding-top:.18em}
.exh-meta dd{margin:0;font-size:.95rem;line-height:1.6}
.sect--text p{
  max-width:64ch;margin:0 0 1.15em;line-height:1.95;
  font-size:clamp(.95rem,.6vw + .8rem,1.06rem);text-indent:2em}
.sect--text p:last-child{margin-bottom:0}
.exhgal{
  column-width:clamp(190px,26vw,340px);
  column-gap:clamp(12px,1.8vw,26px);column-fill:balance;
  margin-top:clamp(16px,2.4vw,30px)}
@media (max-width:560px){.exhgal{column-width:auto;column-count:2;column-gap:10px}}
.exhfig{
  margin:0 0 clamp(12px,1.8vw,24px);break-inside:avoid;page-break-inside:avoid;
  line-height:0;background:var(--surface);overflow:hidden;position:relative}
.exhfig img{
  width:100%;height:auto;display:block;
  transition:filter .6s var(--ease);filter:saturate(.96)}
.exhfig:hover img{filter:saturate(1.06)}
.credit{
  font-size:.8rem;letter-spacing:.04em;color:var(--ink-dim);
  border-top:1px solid var(--line);padding-top:1.1em;max-width:64ch}
'''
marker='/* ---- works grid(?) ---- */'
if '/* ---- exhibition pages ---- */' not in c:
    c=c.rstrip()+'\n'+add
io.open(p,'w',encoding='utf-8',newline='\n').write(c)
print('site.css', len(c))