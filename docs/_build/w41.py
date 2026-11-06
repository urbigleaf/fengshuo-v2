import io
R=r'D:\user\Documents\GitHub\fengshuo_v1'
s=io.open(R+r'\exhibitions\index.html',encoding='utf-8').read()
i=s.find('exh-list')
print('LIST BLOCK:', repr(s[i-60:i+520]))
print()
a=io.open(R+r'\about\index.html',encoding='utf-8').read()
j=a.find('2012-carnival')
print('ABOUT ref:', repr(a[j-120:j+80]))
g=io.open(R+r'\_build\gen_p3.py',encoding='utf-8').read()
print('gen_p3 has 2012 link:', '2012-carnival.html' in g)
print('gen_p3 has thumb:', 'exh__thumb' in g)