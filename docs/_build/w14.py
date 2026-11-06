import io
p=r'D:\user\Documents\GitHub\fengshuo_v1\_build\gen_p5.py'
s=io.open(p,encoding='utf-8').read()
old="os.path.join(BUILD,'exh_clean.json')"
new=r"r'D:\user\Documents\GitHub\fengshuo_v1\_build\exh_clean.json'"
print('found:', old in s)
s=s.replace(old,new)
io.open(p,'w',encoding='utf-8',newline='\n').write(s)
print('patched')