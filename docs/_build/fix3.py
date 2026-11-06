import io
B=r'D:\user\Documents\GitHub\fengshuo_v1\_build'
# 1) generator: mark each year section
p=B+r'\gen_p2.py'
g=io.open(p,encoding='utf-8').read()
old="'<section class=\"sect sect--tight\"><div class=\"wrap\">'"
new="'<section class=\"sect sect--tight\" data-year-group=\"%s\"><div class=\"wrap\">'"
print('gen marker found:', old in g)
g=g.replace(old,new)
g=g.replace("% (y, len(items), grid(items, \"../\")))","% (y, y, len(items), grid(items, \"../\")))")
io.open(p,'w',encoding='utf-8',newline='\n').write(g)

# 2) JS: also hide the whole year group
p2=r'D:\user\Documents\GitHub\fengshuo_v1\assets\js\site.js'
j=io.open(p2,encoding='utf-8').read()
oldj="""      var counter = doc.querySelector('[data-count]');"""
newj="""      doc.querySelectorAll('[data-year-group]').forEach(function (grp) {
        var showGrp = (y === 'all') || (grp.getAttribute('data-year-group') === y);
        grp.style.display = showGrp ? '' : 'none';
      });
      var counter = doc.querySelector('[data-count]');"""
print('js anchor found:', oldj in j)
j=j.replace(oldj,newj)
io.open(p2,'w',encoding='utf-8',newline='\n').write(j)
print('js', len(j), '| gen', len(g))