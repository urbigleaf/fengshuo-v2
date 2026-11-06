import io,re
p=r'D:\user\Documents\GitHub\fengshuo_v1\_build\gen_p3.py'
g=io.open(p,encoding='utf-8').read()
# The 2012 and 2008 anchors each end with: &rarr;</span></div>'  followed by the next entry
for yr, nxt in (('2012','1994'), ('2008','1994')):
    pass
# Replace the </div>' that terminates an anchor-started entry.
# Strategy: split into the list block, then re-close per entry.
start=g.find('<a class="exh" href="2012-carnival.html">')
end=g.find('<div class="exh"><span class="exh__year">1994</span>')
blk=g[start:end]
print('block length:', len(blk))
print('block entries (</div> count):', blk.count("</div>'"))
new=blk.replace("&rarr;</span></div>'", "&rarr;</span></a>'")
print('after fix </div>:', new.count("</div>'"), '| </a>:', new.count("</a>'"))
g=g[:start]+new+g[end:]
io.open(p,'w',encoding='utf-8',newline='\n').write(g)
print('anchors open/close:', g.count('<a class="exh"'), g.count('</a>\''))