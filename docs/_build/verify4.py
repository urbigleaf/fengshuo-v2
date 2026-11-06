import io,os,re
R=r'D:\user\Documents\GitHub\fengshuo_v1'
p=os.path.join(R,'exhibitions','2008-tales.html')
s=io.open(p,encoding='utf-8').read()
figs=re.findall(r'<figure class="exhfig">(.*?)</figure>', s, re.S)
print('total figures:', len(figs))
for i,f in enumerate(figs):
    img=re.search(r'src="([^"]+)"',f).group(1).split('/')[-1]
    cap=re.search(r'<figcaption class="exhfig__cap">(.*?)</figcaption>',f,re.S)
    if cap:
        z=re.search(r'data-lang="zh">(.*?)</span>',cap.group(1),re.S).group(1)
        e=re.search(r'data-lang="en" lang="en">(.*?)</span>',cap.group(1),re.S).group(1)
        print('  %-22s CAP zh=%r en=%r' % (img, z, e))
    else:
        print('  %-22s (no caption)' % img)
print()
zh=re.search(r'<div data-lang="zh">(.*?)</div>\s*<div data-lang="en"', s, re.S).group(1)
print('body zh paras:', len(re.findall(r'<p>',zh)), '| chars', len(re.sub(r'<[^>]+>','',zh).strip()))
print('captions total:', s.count('exhfig__cap'))
print('page size:', len(s.encode('utf-8')))