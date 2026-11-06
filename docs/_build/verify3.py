import io,os,re
R=r'D:\user\Documents\GitHub\fengshuo_v1'
p=os.path.join(R,'exhibitions','2008-tales.html')
s=io.open(p,encoding='utf-8').read()
zh=re.search(r'<div data-lang="zh">(.*?)</div>\s*<div data-lang="en"', s, re.S).group(1)
en=re.search(r'<div data-lang="en" lang="en">(.*?)</div>', s, re.S).group(1)
print('body zh paras:', len(re.findall(r'<p>',zh)), '| chars', len(re.sub(r'<[^>]+>','',zh).strip()))
print('body en paras:', len(re.findall(r'<p>',en)), '| chars', len(re.sub(r'<[^>]+>','',en).strip()))
print('caption present:', s.count('exhfig__cap'))
caps=re.findall(r'<figcaption class="exhfig__cap">(.*?)</figcaption>', s, re.S)
for c in caps:
    z=re.search(r'data-lang="zh">(.*?)</span>', c, re.S).group(1)
    e=re.search(r'data-lang="en" lang="en">(.*?)</span>', c, re.S).group(1)
    print('  caption zh:', repr(z), '| en:', repr(e))
# confirm caption sits inside the figure whose img is exh-2008-05
figs=re.findall(r'<figure class="exhfig">(.*?)</figure>', s, re.S)
for i,f in enumerate(figs):
    img=re.search(r'src="([^"]+)"',f).group(1)
    has='figcaption' in f
    print('  fig%d %-34s caption=%s' % (i+1, img.split('/')[-1], has))
print()
print('broken refs check:', sum(1 for m in re.findall(r'(?:src|href)="([^"]+)"',s)
      if not m.startswith(('http','#','/')) and not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(p),m.split('?')[0])))))