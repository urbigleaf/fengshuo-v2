# -*- coding: utf-8 -*-
"""Build responsive image derivatives (AVIF/WebP/JPG) for fengshuo_v1."""
import json, os, subprocess, sys, shutil

ROOT   = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # fengshuo_v1
REPO   = os.path.dirname(ROOT)                                          # GitHub
SRC    = os.path.join(REPO, 'fengshuo', 'docs', 'wp-content', 'uploads')
OUT    = os.path.join(ROOT, 'assets', 'img')
MAGICK = r'C:\Program Files\ImageMagick-7.1.2-Q16-HDRI\magick.exe'

WIDTHS = [400, 700, 1100, 1600]

def run(args):
    p = subprocess.run(args, capture_output=True)
    if p.returncode != 0:
        raise RuntimeError(p.stderr.decode('utf-8', 'ignore')[:400])

def main():
    with open(os.path.join(ROOT, '_build', 'works-source.json'), encoding='utf-8') as f:
        works = json.load(f)
    os.makedirs(OUT, exist_ok=True)
    made = 0
    for w in works:
        s = os.path.join(SRC, w['src'].replace('/', os.sep))
        if not os.path.exists(s):
            print('MISSING', w['slug']); continue
        # probe real pixel size
        try:
            dim = subprocess.run([MAGICK, 'identify', '-format', '%w %h', s],
                                 capture_output=True).stdout.decode().split()
            sw, sh = int(dim[0]), int(dim[1])
        except Exception:
            sw, sh = 1600, 1600
        base = w['slug']
        variants = []
        for tw in WIDTHS:
            if tw > sw:
                continue
            th = max(1, round(sh * tw / sw))
            stem = f'{base}-{tw}'
            dst_w = os.path.join(OUT, stem + '.webp')
            if not os.path.exists(dst_w):
                run([MAGICK, s, '-resize', f'{tw}x{th}>', '-strip',
                     '-quality', '76', '-define', 'webp:method=6', dst_w])
                run([MAGICK, s, '-resize', f'{tw}x{th}>', '-strip',
                     '-quality', '60', os.path.join(OUT, stem + '.avif')])
                run([MAGICK, s, '-resize', f'{tw}x{th}>', '-strip',
                     '-quality', '80', '-sampling-factor', '4:2:0',
                     '-interlace', 'Plane', os.path.join(OUT, stem + '.jpg')])
                made += 1
            variants.append((stem, tw, th))
        w['variants'] = [{'stem': v[0], 'w': v[1], 'h': v[2]} for v in variants]
        w['srcW'], w['srcH'] = sw, sh
    with open(os.path.join(ROOT, '_build', 'works-images.json'), 'w', encoding='utf-8') as f:
        json.dump(works, f, ensure_ascii=False, indent=1)
    print(f'DONE variants_sets={made} works={len(works)}')

if __name__ == '__main__':
    main()