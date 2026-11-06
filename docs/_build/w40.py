import io
p=r'D:\user\Documents\GitHub\fengshuo_v1\_build\gen_p3.py'
g=io.open(p,encoding='utf-8').read()
# add thumbnails to the two linked entries
g=g.replace('<a class="exh" href="2012-carnival.html"><span class="exh__year">2012</span>',
 '<a class="exh exh--linked" href="2012-carnival.html">'
 '<img class="exh__thumb" src="../assets/img/exh/poster-2012-512.jpg" width="512" height="1024" loading="lazy" alt="">'
 '<span class="exh__year">2012</span>')
g=g.replace('<a class="exh" href="2008-tales.html"><span class="exh__year">2008</span>',
 '<a class="exh exh--linked" href="2008-tales.html">'
 '<img class="exh__thumb" src="../assets/img/exh/exh-2008-03-400.jpg" width="400" height="300" loading="lazy" alt="">'
 '<span class="exh__year">2008</span>')
io.open(p,'w',encoding='utf-8',newline='\n').write(g)
print('thumbs added:', g.count('exh__thumb'))