import io
p=r'D:\user\Documents\GitHub\fengshuo_v1\sitemap.xml'
s=io.open(p,encoding='utf-8').read()
new=['https://fengshuo.cc/exhibitions/2008-tales.html','https://fengshuo.cc/exhibitions/2012-carnival.html']
add=''.join('  <url><loc>%s</loc><changefreq>yearly</changefreq><priority>0.7</priority></url>\n'%u
            for u in new if u not in s)
anchor='</urlset>'
i=s.rfind(anchor)
s=s[:i]+add+s[i:]
io.open(p,'w',encoding='utf-8',newline='\n').write(s)
import re
locs=re.findall(r'<loc>([^<]+)</loc>',s)
print('sitemap urls:', len(locs))
print('exhibition urls:', [u for u in locs if 'exhibition' in u])