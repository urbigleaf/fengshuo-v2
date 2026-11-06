import io,os,re,glob
R=r'D:\user\Documents\GitHub\fengshuo_v1'
pages=[p for p in glob.glob(os.path.join(R,'**','*.html'),recursive=True) if '_build' not in p]
miss=[]
for p in pages:
    s=io.open(p,encoding='utf-8').read()
    for m in re.findall(r'(?:src|href)="([^"]+)"', s):
        if m.startswith(('http','#','mailto','data:','/')): continue
        t=m.split('?')[0].split('#')[0]
        if t and not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(p),t))): miss.append((os.path.relpath(p,R),t))
print('pages:',len(pages),'| broken refs:',len(miss))
for x in miss[:6]: print('  MISS',x)
print()
for f in ['exhibitions\\2008-tales.html','exhibitions\\2012-carnival.html']:
    p=os.path.join(R,f); s=io.open(p,encoding='utf-8').read()
    zh=re.search(r'<div data-lang="zh">(.*?)</div>\s*<div data-lang="en"', s, re.S)
    en=re.search(r'<div data-lang="en" lang="en">(.*?)</div>', s, re.S)
    zt=re.sub(r'<[^>]+>','',zh.group(1)) if zh else ''
    et=re.sub(r'<[^>]+>','',en.group(1)) if en else ''
    zhp=len(re.findall(r'<p>',zh.group(1))) if zh else 0
    enp=len(re.findall(r'<p>',en.group(1))) if en else 0
    imgs=len(re.findall(r'<img',s))
    print('%-30s zh:%d chars/%d p | en:%d chars/%d p | imgs %d' % (f, len(zt.strip()), zhp, len(et.strip()), enp, imgs))
    print('   en head:', repr(et.strip()[:52]))
print()
s=io.open(os.path.join(R,'exhibitions','index.html'),encoding='utf-8').read()
print('list links 2008/2012:', '2008-tales.html' in s, '2012-carnival.html' in s)
print('thumb count:', s.count('exh__thumb'))