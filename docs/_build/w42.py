import io,glob,os
for f in sorted(glob.glob(r'D:\user\Documents\GitHub\fengshuo_v1\_build\*.py')):
    s=io.open(f,encoding='utf-8').read()
    if '#tales' in s and 'exh' in s:
        print(os.path.basename(f), '-> #tales count', s.count('#tales'), '| #carnival', s.count('#carnival'))