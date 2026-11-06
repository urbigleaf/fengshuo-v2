import io
p=r'D:\user\Documents\GitHub\fengshuo_v1\_build\gen_p3.py'
g=io.open(p,encoding='utf-8').read()
# this block lives in the ABOUT page -> paths must climb one level
g=g.replace('\'<a class="exh" href="#tales"><span class="exh__year">2008</span>',
  '\'<a class="exh exh--linked" href="../exhibitions/2008-tales.html">'
  '<img class="exh__thumb" src="../assets/img/exh/exh-2008-03-400.jpg" width="400" height="300" loading="lazy" alt="">'
  '<span class="exh__year">2008</span>')
g=g.replace('\'<a class="exh" href="#carnival"><span class="exh__year">2012</span>',
  '\'<a class="exh exh--linked" href="../exhibitions/2012-carnival.html">'
  '<img class="exh__thumb" src="../assets/img/exh/poster-2012-512.jpg" width="512" height="1024" loading="lazy" alt="">'
  '<span class="exh__year">2012</span>')
io.open(p,'w',encoding='utf-8',newline='\n').write(g)
print('#tales left:', g.count('href="#tales"'), '| #carnival left:', g.count('href="#carnival"'))
print('linked:', g.count('exh--linked'), '| thumbs:', g.count('exh__thumb'))