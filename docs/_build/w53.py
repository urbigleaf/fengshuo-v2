import json,io
R=r'D:\user\Documents\GitHub\fengshuo_v1'
ZH=json.load(open(R+r'\_build\exh_clean.json',encoding='utf-8'))
EN=json.load(open(R+r'\_build\exh_en.json',encoding='utf-8'))
print('ZH 2008 p1 (codepoints):', ' '.join('%04X'%ord(c) for c in ZH['2008']['paras'][1][:8]))
print('ZH 2008 p1 len', len(ZH['2008']['paras'][1]))
print('ZH 2008 p2 len', len(ZH['2008']['paras'][2]))
print('EN 2008 p1:', repr(EN['2008']['paras'][1]))
print('EN 2008 p2:', repr(EN['2008']['paras'][2]))