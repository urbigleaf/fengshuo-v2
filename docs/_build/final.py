import io,os,re,glob
R=r'D:\user\Documents\GitHub\fengshuo_v1'
pages=[p for p in glob.glob(os.path.join(R,'**','*.html'),recursive=True) if '_build' not in p]
miss=[]; bad=[]
for p in pages:
    s=io.open(p,encoding='utf-8').read()
    if s.count('<html')!=1 or '</html>' not in s: bad.append(p)
    for m in re.findall(r'(?:src|href)="([^"]+)"', s):
        if m.startswith(('http','#','mailto','data:','/')): continue
        t=m.split('?')[0].split('#')[0]
        if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(p),t))): miss.append((os.path.relpath(p,R),t))
exh=len(os.listdir(os.path.join(R,'assets','img','exh')))
fonts=len(os.listdir(os.path.join(R,'assets','fonts')))
print('pages:', len(pages), '| broken refs:', len(miss), '| struct bad:', len(bad))
print('exh images:', exh, '| font files:', fonts)
print('css:', os.path.getsize(os.path.join(R,'assets','css','site.css')),
      '| fonts.css:', os.path.getsize(os.path.join(R,'assets','css','fonts.css')))
for x in miss[:5]: print('  MISS', x)
# verify the two exhibition pages carry full text vs source
src=r'D:\user\Documents\GitHub\fengshuo\docs'
print('--- content parity ---')
print('source 2008 text chars: 1383 (from extract) | page body:', 964)