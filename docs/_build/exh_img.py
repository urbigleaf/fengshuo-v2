import os,re,json,subprocess
D=r'D:\user\Documents\GitHub\fengshuo\docs'
R=r'D:\user\Documents\GitHub\fengshuo_v1'
MAGICK=r'C:\Program Files\ImageMagick-7.1.2-Q16-HDRI\magick.exe'
data=json.load(open(os.path.join(R,'_build','exh_full.json'),encoding='utf-8'))
os.makedirs(os.path.join(R,'assets','img','exh'),exist_ok=True)
report=[]
for k,v in data.items():
    newimgs=[]
    for n,u in enumerate(v['imgs']):
        # u like /wp-content/uploads/2023/.../name.jpg
        rel=u.lstrip('/').replace('/','\\')
        src=os.path.join(D,rel)
        if not os.path.exists(src):
            report.append((k,'MISSING',u)); continue
        ext=os.path.splitext(u)[1].lower()
        base='exh-%s-%02d'%(k,n+1)
        info=subprocess.run([MAGICK,'identify','-format','%w %h',src],capture_output=True,text=True)
        try: W,H=[int(x) for x in info.stdout.split()]
        except Exception: W,H=0,0
        outs=[]
        for wid in (700,1100,1600):
            if W<=wid and wid!=700: continue
            if W<=wid and wid==700 and W<700: pass
            out=os.path.join(R,'assets','img','exh','%s-%d.webp'%(base,min(wid,max(W,400))))
            pass
        made=[]
        for wid in (400,700,1100,1600):
            if W<=wid and made: continue
            tgt=os.path.join(R,'assets','img','exh','%s-%d.jpg'%(base,wid))
            subprocess.run([MAGICK,src,'-resize','%dx>'%wid,'-strip','-quality','80','-interlace','Plane',tgt],check=True)
            made.append(wid)
        newimgs.append({'base':base,'w':W,'h':H,'widths':made})
        report.append((k,'ok',base,W,H))
    v['processed']=newimgs
json.dump(data, open(os.path.join(R,'_build','exh_full.json'),'w',encoding='utf-8'), ensure_ascii=False, indent=1)
n=len(os.listdir(os.path.join(R,'assets','img','exh')))
print('exh img files:', n)
print('errors:', [r for r in report if r[1]!='ok'])
print('first:', report[0], report[-1])