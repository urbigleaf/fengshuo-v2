import io,os,re
R=r'D:\user\Documents\GitHub\fengshuo_v1'
pages=[]
for dp,_,fs in os.walk(R):
    if '_build' in dp: continue
    for f in fs:
        if f.endswith('.html'): pages.append(os.path.join(dp,f))
miss=[]
for p in pages:
    s=io.open(p,encoding='utf-8').read()
    for m in re.findall(r'(?:src|href)=\"([^\"]+)\"', s):
        if m.startswith(('http','#','mailto','data:','/')): continue
        if m=='favicon.ico': continue
        t=m.split('?')[0].split('#')[0]
        ap=os.path.normpath(os.path.join(os.path.dirname(p), t))
        if not os.path.exists(ap): miss.append((os.path.relpath(p,R), t))
print('real broken refs:', len(miss))
for x in miss[:8]: print(' ', x)
# image counts
img=os.path.join(R,'assets','img')
print('img files:', len(os.listdir(img)))
print('total MB: %.1f' % (sum(os.path.getsize(os.path.join(img,f)) for f in os.listdir(img))/1048576))
print('css:', os.path.getsize(os.path.join(R,'assets','css','site.css')))
print('js :', os.path.getsize(os.path.join(R,'assets','js','site.js')))