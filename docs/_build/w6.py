import io,os
P=r'D:\user\Documents\GitHub\fengshuo_v1\_build'
b=io.open(os.path.join(P,'gen_base.py'),encoding='utf-8').read()
b=b.replace("json.dump({'years': years}","raise SystemExit\njson.dump({'years': years}")
io.open(os.path.join(P,'gen_lib.py'),'w',encoding='utf-8').write(b)
print('lib', len(b))