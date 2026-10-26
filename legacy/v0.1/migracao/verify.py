"""Compara o texto de cada página da v0.1 com o site exportado (out/).

uso: python -I verify.py <html_v01> <out_dir>
"""
import difflib, os, re, sys
from html.parser import HTMLParser

HTML_PATH, OUT = sys.argv[1:3]


class TextGrab(HTMLParser):
    """Coleta o texto dentro de elementos que casam com `match(tag, attrs)`."""

    def __init__(self, match):
        super().__init__(convert_charrefs=True)
        self.match, self.depth, self.cur, self.found = match, 0, None, []
        self.stack = []

    def handle_starttag(self, tag, attrs):
        if tag in ('input', 'br', 'img', 'meta', 'link', 'hr'):
            return
        a = dict(attrs)
        if self.cur is None and self.match(tag, a):
            self.cur = []
            self.depth = len(self.stack)
            self.key = a
        self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag in ('input', 'br', 'img', 'meta', 'link', 'hr'):
            return
        while self.stack:
            t = self.stack.pop()
            if t == tag:
                break
        if self.cur is not None and len(self.stack) == self.depth:
            self.found.append((self.key, ' '.join(self.cur)))
            self.cur = None

    def handle_data(self, d):
        if self.cur is not None:
            self.cur.append(d)


def norm(t):
    return re.sub(r'\s+', ' ', t).strip()


src = open(HTML_PATH, encoding='utf-8').read()
g = TextGrab(lambda t, a: t == 'section' and 'page' in a.get('class', ''))
g.feed(src)
orig = {}
for a, _ in g.found:
    pass
# texto só do .prose de cada seção
for sec in re.findall(r'<section class="page"[^>]*data-id="([^"]+)".*?</section>', src, re.S):
    pass
pairs = re.findall(r'<section class="page" id="pg-[^"]+" data-id="([^"]+)"(.*?)</section>', src, re.S)

bad = 0
for pid, body in pairs:
    pg = TextGrab(lambda t, a: t == 'div' and a.get('class') == 'prose')
    pg.feed(body)
    o = norm(pg.found[0][1])
    if pid == 'inicio':
        path = os.path.join(OUT, 'index.html')
    elif pid.startswith('c-'):
        path = os.path.join(OUT, 'componentes', pid[2:], 'index.html')
    else:
        path = os.path.join(OUT, pid, 'index.html')
    if not os.path.exists(path):
        print('FALTA', pid, path)
        bad += 1
        continue
    ng = TextGrab(lambda t, a: 'data-docs-content' in a)
    ng.feed(open(path, encoding='utf-8').read())
    n = norm(ng.found[0][1])
    # espaços em volta de pontuação variam entre os dois renderizadores
    k = lambda s: re.sub(r'\s+([,.;:)!?])', r'\1', re.sub(r'([(])\s+', r'\1', s)).replace(' ', '')
    if k(o) != k(n):
        bad += 1
        ow, nw = o.split(' '), n.split(' ')
        print('==== DIFERENÇA', pid)
        a, b = k(o), k(n)
        i = next((i for i in range(min(len(a), len(b))) if a[i] != b[i]), min(len(a), len(b)))
        print('   orig:', ascii(a[max(0, i - 60):i + 60]))
        print('   novo:', ascii(b[max(0, i - 60):i + 60]))
        continue
        for line in list(difflib.unified_diff(ow, nw, lineterm='', n=3))[2:40]:
            print('  ', line)
print('páginas:', len(pairs), 'com diferença:', bad)

