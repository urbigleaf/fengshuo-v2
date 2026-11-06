import io,re,os
D=r'D:\user\Documents\GitHub\fengshuo\docs'
raw=open(os.path.join(D,'2012-狂欢冯硕个人作品展','index.html'),'rb').read()
print('utf8 ok?', end=' ')
try: s=raw.decode('utf-8'); print(True)
except UnicodeDecodeError as e: print('NO', e); s=raw.decode('utf-8','replace')
i=s.find('Andrian')
print('found Andrian at', i)
seg=s[i-200:i+80]
print('RAW SEGMENT repr:')
print(repr(seg))