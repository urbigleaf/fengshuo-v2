import os,re,json
R=r'D:\user\Documents\GitHub\fengshuo_v1'
d=json.load(open(os.path.join(R,'_build','exh_full.json'),encoding='utf-8'))
def clean_line(t):
    t=re.sub(r'[ \t\u3000]+',' ',t).strip()
    # collapse accidental char duplication at line-wrap seams:  X X -> X
    t=re.sub(r'(.)\1(?=[，。、；：？！」）》\s])', r'\1', t)  # keeps legit doubles rarely
    return t
# only collapse a repeated char that sits at end of a wrapped line inside a space run
def dedupe(t):
    lines=t.split('\n')
    return '\n'.join(re.sub(r'[ \u3000]{2,}',' ',l).strip() for l in lines)
for k,v in d.items():
    v['paras']=[dedupe(p) for p in v['paras']]
    print(k, [len(p) for p in v['paras']])
open(os.path.join(R,'_build','exh_clean.json'),'w',encoding='utf-8').write(json.dumps(d,ensure_ascii=False,indent=1))
print('saved')