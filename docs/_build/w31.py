import io,re
p=r'D:\user\Documents\GitHub\fengshuo_v1\exhibitions\index.html'
s=io.open(p,encoding='utf-8').read()
print('has 2008 link:', '2008-tales' in s)
print('has 2012 link:', '2012-carnival' in s)
m=re.search(r'<main.*?</main>', s, re.S)
print('main len:', len(m.group(0)) if m else 0)
i=s.find('<section')
print('--- first 1200 chars of body ---')
print(s[i:i+1200] if i>0 else s[:1200])