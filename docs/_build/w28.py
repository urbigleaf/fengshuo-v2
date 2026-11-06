import json
p=r'D:\user\Documents\GitHub\fengshuo_v1\_build\exh_en.json'
d=json.load(open(p,encoding='utf-8'))
t=d['2012']['paras'][1]
i=t.find('Feng Shuo')
seg=t[i:i+22]
print('segment:', seg)
print('codepoints:', ' '.join('U+%04X'%ord(c) for c in seg))
print('repr:', repr(seg))