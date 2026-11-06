import os,subprocess,json
R=r'D:\user\Documents\GitHub\fengshuo_v1'
MAGICK=r'C:\Program Files\ImageMagick-7.1.2-Q16-HDRI\magick.exe'
d=json.load(open(os.path.join(R,'_build','exh_clean.json'),encoding='utf-8'))
for k in ('2008','2012'):
    print('==',k)
    for n,im in enumerate(d[k]['processed']):
        src=d[k]['imgs'][n].split('/')[-1]
        print('  %2d %-12s %sx%s  src=%s' % (n+1, im['base'], im['w'], im['h'], src[:40]))