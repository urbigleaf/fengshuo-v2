import io,re
p=r'D:\user\Documents\GitHub\fengshuo_v1\assets\css\site.css'
c=io.open(p,encoding='utf-8').read()

old_grid='''.grid{
  display:grid;gap:clamp(14px,2.4vw,36px) clamp(12px,1.9vw,28px);
  grid-template-columns:repeat(auto-fill,minmax(clamp(150px,20vw,300px),1fr))}'''
new_grid='''.grid{
  column-width:clamp(170px,21vw,290px);
  column-gap:clamp(12px,1.9vw,28px);
  column-fill:balance}
@media (max-width:520px){.grid{column-width:auto;column-count:2;column-gap:10px}}'''
assert old_grid in c, 'grid block not found'
c=c.replace(old_grid,new_grid)

# card must not split across columns, and frame must hug the image
c=c.replace('''.card{
  position:relative;display:flex;flex-direction:column;gap:.7em;''','''.card{
  position:relative;display:flex;flex-direction:column;gap:.7em;
  break-inside:avoid;page-break-inside:avoid;
  margin:0 0 clamp(14px,2.4vw,34px);''')

c=c.replace('''.card__frame{
  position:relative;overflow:hidden;background:var(--surface);
  aspect-ratio:var(--ar,1);display:grid;place-items:center}''','''.card__frame{
  position:relative;overflow:hidden;background:var(--surface);
  display:block;line-height:0}
.card__frame picture{display:block}''')

c=c.replace('''.card__frame img{
  width:100%;height:100%;object-fit:contain;''','''.card__frame img{
  width:100%;height:auto;display:block;''')

c=c.replace('''.card:hover .card__frame img,.card:focus-visible .card__frame img{
  transform:scale(1.045);filter:saturate(1.06)}''','''.card:hover .card__frame img,.card:focus-visible .card__frame img{
  filter:saturate(1.06)}''')

io.open(p,'w',encoding='utf-8',newline='\n').write(c)
print('site.css', len(c), 'bytes')