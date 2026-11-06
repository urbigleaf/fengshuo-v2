import io
p=r'D:\user\Documents\GitHub\fengshuo_v1\_build\gen_p5.py'
g=io.open(p,encoding='utf-8').read()
old="return page(content, 0, '../',"
new="return page(content, 1, '../',"
print('found depth arg:', old in g)
g=g.replace(old,new)
io.open(p,'w',encoding='utf-8',newline='\n').write(g)
print('patched depth -> 1')