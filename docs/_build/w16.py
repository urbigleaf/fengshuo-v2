import io,re,os
R=r'D:\user\Documents\GitHub\fengshuo_v1'
for f in ['exhibitions\\2008-tales.html','exhibitions\\2012-carnival.html']:
    p=os.path.join(R,f)
    s=io.open(p,encoding='utf-8').read()
    ps=re.findall(r'<p>(.*?)</p>', s, re.S)
    txt=''.join(re.sub(r'<[^>]+>','',x) for x in ps)
    imgs=re.findall(r'<img[^>]+src="([^"]+)"', s)
    miss=[u for u in imgs if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(p),u)))]
    import unicodedata
    # detect mojibake by checking for chars in the typical gbk-misread ranges
    bad=sum(1 for ch in txt if 0x3400<=ord(ch)<=0x4DBF)
    print('%-34s %6d bytes | %4d body chars | %2d imgs | missing %d | surrog %d' % (f, len(s.encode('utf-8')), len(txt), len(imgs), len(miss), bad))
    print('    title paras:', [t[:24] for t in ps[:2]])