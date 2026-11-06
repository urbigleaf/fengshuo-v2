import io,json
R=r'D:\user\Documents\GitHub\fengshuo_v1'
ZH=json.load(open(R+r'\_build\exh_clean.json',encoding='utf-8'))
EN=json.load(open(R+r'\_build\exh_en.json',encoding='utf-8'))
print('zh 2008 paras:')
for i,t in enumerate(ZH['2008']['paras']): print('  p%d (%d): %r'%(i,len(t),t[:60]))
print()
print('en 2008 paras:')
for i,t in enumerate(EN['2008']['paras']): print('  p%d (%d): %r'%(i,len(t),t[:70]))
print()
print('zh 2012 last paras:')
for i,t in enumerate(ZH['2012']['paras'][-2:], start=len(ZH['2012']['paras'])-2): print('  p%d (%d): %r'%(i,len(t),t[:60]))