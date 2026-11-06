import json
p=r'D:\user\Documents\GitHub\fengshuo_v1\_build\exh_en.json'
d=json.load(open(p,encoding='utf-8'))
REP={'\u9225\u6a9a':"'"+"s", '\u9225\u6a9b':"'"+"t", '\u9225\u6a9c':"'"+"re",
     '\u9225\u6a99':"'"+"ll", '\u9225\u6a93':"'"+"ve", '\u9225\u672f':"'s",
     '\u9225':"'", '\u9226\u00b0':'"', '\u9225\u2013':'-', '\u9225\u2014':'--'}
def fix(t):
    for a,b in sorted(REP.items(), key=lambda x:-len(x[0])): t=t.replace(a,b)
    return t
for k in d: d[k]['paras']=[fix(t) for t in d[k]['paras']]
bad=[(k,i) for k in d for i,t in enumerate(d[k]['paras']) if '\u9225' in t]
print('remaining mojibake paras:', bad)
print('sample:', d['2012']['paras'][1][:85])
open(p,'wb').write(json.dumps(d,ensure_ascii=False,indent=1).encode('utf-8'))
print('ok')