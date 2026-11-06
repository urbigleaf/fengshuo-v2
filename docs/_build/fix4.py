import io
p=r'D:\user\Documents\GitHub\fengshuo_v1\_build\gen_p2.py'
g=io.open(p,encoding='utf-8').read()
old='''          '<div class="sect-head"><div class="sect-head__l"><span class="kicker">%s</span>'
          '<h2 class="sect-title"><span data-lang="zh">同年作品</span><span data-lang="en">Same year</span></h2></div></div>'
          '%s</div></section>' % (wk["year"], grid(same, "../"))) if same else "")'''
new='''          '<div class="sect-head"><div class="sect-head__l"><span class="kicker">%s</span>'
          '<h2 class="sect-title"><span data-lang="zh">同年作品</span><span data-lang="en">Same year</span></h2></div></div>'
          '%s</div></section>' % (wk["year"], wk["year"], grid(same, "../"))) if same else "")'''
print('anchor found:', old in g)
g=g.replace(old,new)
io.open(p,'w',encoding='utf-8',newline='\n').write(g)
print('ok')