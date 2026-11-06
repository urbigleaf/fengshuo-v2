import io,os,json
R=r'D:\user\Documents\GitHub\fengshuo_v1'
# check the JSON that the generator reads
j=json.load(io.open(os.path.join(R,'_build','exh_clean.json'),encoding='utf-8'))
t2008=j['2008']['paras'][4]
print('JSON 2008 p4 head:', repr(t2008[:24]))
# detect: is it proper chinese?
ok=all(('\u4e00'<=ch<='\u9fff') or ch.isascii() or ch in '：，。、；！？（）《》—…「」' for ch in t2008)
print('json looks proper chinese:', ok)
# check gen_lib w() write encoding
g=io.open(os.path.join(R,'_build','gen_lib.py'),encoding='utf-8').read()
import re
for m in re.finditer(r'def w\(.*?\n(?:.*\n){0,8}', g):
    print('w() def:\n', m.group(0))