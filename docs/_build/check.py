import io,os,re,json
R=r'D:\user\Documents\GitHub\fengshuo_v1'
pages=[]
for dp,_,fs in os.walk(R):
    if '_build' in dp: continue
    for f in fs:
        if f.endswith('.html'): pages.append(os.path.join(dp,f))
print('html pages:', len(pages))
missing=[]; badref=[]
for p in pages:
    s=io.open(p,encoding='utf-8').read()
    if s.count('<html')!=1 or s.count('</html>')!=1: badref.append(('struct',p))
    if 'data-lang=\"zh\"' not in s: badref.append(('nolang',p))
    for m in re.findall(r'(?:src|href)=\"([^\"]+)\"', s):
        if m.startswith(('http','#','mailto','data:')): continue
        t=m.split('?')[0].split('#')[0]
        if not t: continue
        ap=os.path.normpath(os.path.join(os.path.dirname(p), t))
        if not os.path.exists(ap): missing.append((os.path.relpath(p,R), t))
print('struct/lang issues:', len(badref))
print('broken local refs:', len(missing))
for x in missing[:10]: print('  ', x)