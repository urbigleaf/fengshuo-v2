import io
p=r'D:\user\Documents\GitHub\fengshuo_v1\assets\css\site.css'
c=io.open(p,encoding='utf-8').read()
add='''
/* installation-photo captions */
.exhfig{position:relative}
.exhfig__cap{
  display:block;line-height:1.55;font-size:.74rem;letter-spacing:.02em;
  color:var(--ink-dim);padding:.55em .2em 0;text-align:left}
.exhfig__cap span{display:block}
'''
if '.exhfig__cap' not in c:
    c=c.rstrip()+'\n'+add
io.open(p,'w',encoding='utf-8',newline='\n').write(c)
print('site.css', len(c))