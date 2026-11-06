import io,os,re
R=r'D:\user\Documents\GitHub\fengshuo_v1'
a=io.open(R+r'\about\index.html',encoding='utf-8').read()
print('about refs:', re.findall(r'href="([^"]*(?:2008-tales|2012-carnival)[^"]*)"', a))
s=io.open(R+r'\sitemap.xml',encoding='utf-8').read()
print('sitemap exhibitions:', [u for u in re.findall(r'<loc>([^<]+)</loc>',s) if 'exhibition' in u])
print('sitemap total:', len(re.findall(r'<loc>',s)))
e=io.open(R+r'\_build\exh_en.json',encoding='utf-8'); import json
d=json.load(e)
print('en paras available 2008/2012:', len(d['2008']['paras']), len(d['2012']['paras']))
print('from-src google fonts refs:', sum(io.open(p,encoding='utf-8').read().count('fonts.googleapis') for p in [os.path.join(R,'exhibitions','2008-tales.html'),os.path.join(R,'exhibitions','2012-carnival.html')]))