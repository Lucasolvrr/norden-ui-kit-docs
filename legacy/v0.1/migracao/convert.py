"""Migração única: HTML da v0.1 -> MDX + JSON para o site Next.js.

uso: python -I convert.py <html_v01> <dir_source_py> <repo_root>
"""
import json, os, re, sys, unicodedata
from html.parser import HTMLParser

HTML_PATH, SRC_DIR, ROOT = sys.argv[1:4]
VOID = {'input', 'br', 'img', 'hr', 'meta', 'link'}


class Node:
    def __init__(self, tag, attrs):
        self.tag, self.attrs, self.children = tag, dict(attrs), []

    @property
    def cls(self):
        return self.attrs.get('class', '').split()

    def text(self):
        return ''.join(c if isinstance(c, str) else c.text() for c in self.children)

    def kids(self, tag=None, cls=None):
        return [c for c in self.children if isinstance(c, Node) and (tag is None or c.tag == tag) and (cls is None or cls in c.cls)]

    def find(self, tag=None, cls=None):
        for c in self.children:
            if isinstance(c, Node):
                if (tag is None or c.tag == tag) and (cls is None or cls in c.cls):
                    return c
                r = c.find(tag, cls)
                if r:
                    return r


class Builder(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node('root', {})
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        n = Node(tag, attrs)
        self.stack[-1].children.append(n)
        if tag not in VOID:
            self.stack.append(n)

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                return

    def handle_data(self, data):
        self.stack[-1].children.append(data)


def slug(s):
    s = unicodedata.normalize('NFD', s).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')


def href(h):
    if not h.startswith('#'):
        return h
    i = h[1:]
    if i == 'inicio':
        return '/'
    if i.startswith('c-'):
        return '/componentes/' + i[2:]
    return '/' + i


def esc(t):
    t = re.sub(r'([\\`*_{}\[\]<>|~&])', r'\\\1', t)
    return t


def attr(v):
    return '"' + v + '"' if '"' not in v else '{' + json.dumps(v, ensure_ascii=False) + '}'


def code(t):
    return ('``' + t + '``') if '`' in t else ('`' + t + '`')


BADGE_DEFAULT = {'impl': 'Implementado', 'rec': 'Recomendação', 'prop': 'Proposta', 'pend': 'Pendente de validação'}


def inline(node):
    out = ''
    for c in node.children:
        if isinstance(c, str):
            out += esc(re.sub(r'\s+', ' ', c))
            continue
        t, cl = c.tag, c.cls
        if t == 'strong':
            out += '**' + inline(c).strip() + '**'
        elif t == 'em':
            out += '*' + inline(c).strip() + '*'
        elif t == 'code':
            out += code(c.text())
        elif t == 'kbd':
            out += '<kbd>' + esc(c.text()) + '</kbd>'
        elif t == 'a':
            out += '[' + inline(c) + '](' + href(c.attrs.get('href', '')) + ')'
        elif t == 'span' and 'badge' in cl:
            kind = [x[2:] for x in cl if x.startswith('b-')][0]
            label = c.text()
            out += f'<Badge kind="{kind}" />' if label == BADGE_DEFAULT[kind] else f'<Badge kind="{kind}">{esc(label)}</Badge>'
        elif t == 'span' and 'sw' in cl:
            out += f'<Swatch color="{c.attrs["style"].split(":", 1)[1].strip()}" />'
        elif t == 'button' and 'tok' in cl:
            out += '<Token>' + c.text() + '</Token>'
        elif t == 'span' and 'ts' in cl:
            st = dict(x.split(':', 1) for x in c.attrs['style'].split(';') if x)
            props = f'size={{{int(st["font-size"].rstrip("px"))}}} weight={{{st["font-weight"]}}}'
            if st.get('text-transform') == 'uppercase':
                props += ' uppercase'
            if st.get('text-decoration') == 'line-through':
                props += ' strike'
            out += f'<TypeSample {props}>{esc(c.text())}</TypeSample>'
        elif t == 'span' and 'h-note' in cl:
            out += ' <HeadingNote>' + esc(c.text()) + '</HeadingNote>'
        else:
            raise ValueError(f'inline desconhecido: {t} {cl}')
    return out


def para(s):
    s = s.strip()
    if re.match(r'^([#>+\-=]|\d+[.)])', s):
        s = '\\' + s if not s[0].isdigit() else re.sub(r'^(\d+)([.)])', r'\1\\\2', s)
    return s


def is_inline(n):
    return all(isinstance(c, str) or c.tag in ('strong', 'em', 'code', 'kbd', 'a', 'span', 'button') for c in n.children)


def li_block(li):
    if is_inline(li):
        return para(inline(li))
    return '\n\n'.join(blocks(li.children))


def lst(n, ordered):
    items = []
    for i, li in enumerate(n.kids('li'), 1):
        body = li_block(li)
        mark = f'{i}. ' if ordered else '- '
        items.append(mark + body.replace('\n', '\n' + ' ' * len(mark)))
    return '\n'.join(items)


def table(n):
    rows = []
    head = [para(inline(th)) or ' ' for th in n.find('thead').find('tr').kids('th')]
    for tr in n.find('tbody').kids('tr'):
        rows.append([inline(td).strip() for td in tr.kids('td')])
    out = '| ' + ' | '.join(head) + ' |\n| ' + ' | '.join('---' for _ in head) + ' |\n'
    out += '\n'.join('| ' + ' | '.join(r) + ' |' for r in rows)
    return out


def fence(text):
    assert '```' not in text
    return '```\n' + text + '\n```'


class Ctx:
    group = None  # prefixo atual das cores de marca
    emitted = set()


SKIP_UNTIL_NEXT_HEADING = object()


def blocks(children):
    out = []
    skip_tables = False
    for c in children:
        if isinstance(c, str):
            if c.strip():
                raise ValueError('texto solto em bloco: ' + c[:60])
            continue
        t, cl = c.tag, c.cls
        if t in ('h2', 'h3'):
            hid = c.attrs.get('id', '')
            if hid.startswith('tok-') or hid.startswith('cat-'):
                key = 'ColorTokens' if hid.startswith('tok-') else 'ComponentIndex'
                if key not in Ctx.emitted:
                    Ctx.emitted.add(key)
                    out.append(f'<{key} />')
                skip_tables = True
                continue
            skip_tables = False
            if t == 'h3':
                Ctx.group = c.text().strip().lower()
            out.append(('## ' if t == 'h2' else '### ') + inline(c).strip())
        elif skip_tables and t == 'div' and 'tbl' in cl:
            continue
        elif t == 'p' and 'mini-t' in cl:
            Ctx.group = 'feedback/' + c.text().strip()
            out.append('<MiniTitle>' + esc(c.text()) + '</MiniTitle>')
        elif t == 'p' and 'prompt-note' in cl:
            out.append('<PromptNote>' + inline(c).strip() + '</PromptNote>')
        elif t == 'p':
            assert not cl, cl
            out.append(para(inline(c)))
        elif t == 'ul':
            out.append(lst(c, False))
        elif t == 'ol' and 'steps' in cl:
            parts = ['<Steps>']
            for li in c.kids('li'):
                h = li.kids('h3')[0]
                rest = [x for x in li.children if x is not h]
                parts.append(f'<Step title={attr(h.text())}>\n\n' + '\n\n'.join(blocks(rest)) + '\n\n</Step>')
            parts.append('</Steps>')
            out.append('\n\n'.join(parts))
        elif t == 'ol':
            out.append(lst(c, True))
        elif t == 'div' and 'tbl' in cl:
            out.append(table(c))
        elif t == 'div' and 'callout' in cl:
            kind = [x[2:] for x in cl if x.startswith('c-')][0]
            title = c.find('p', 'callout-t')
            assert is_inline(title) and all(isinstance(x, str) for x in title.children), title.text()
            body = c.kids('div')[0]
            out.append(f'<Callout kind="{kind}" title={attr(title.text())}>\n\n' + '\n\n'.join(blocks(body.children)) + '\n\n</Callout>')
        elif t == 'figure' and 'prompt' in cl:
            title = c.find('span', 'prompt-t').text()
            text = '\n\n'.join(pre.text() for pre in [s.find('pre') for s in c.kids('div', 'pseg')])
            out.append(f'<Prompt title={attr(title)}>\n\n' + fence(text) + '\n\n</Prompt>')
        elif t == 'dl' and 'sdl' in cl:
            items = []
            dts, dds = c.kids('dt'), c.kids('dd')
            assert len(dts) == len(dds)
            for dt, dd in zip(dts, dds):
                items.append(f'<Detail term={attr(dt.text())}>{inline(dd).strip()}</Detail>')
            out.append('<Details>\n' + '\n'.join(items) + '\n</Details>')
        elif t == 'div' and 'cmp' in cl:
            parts = ['<Compare>']
            for side in c.kids('div'):
                kind = 'bad' if 'cmp-bad' in side.cls else 'good'
                label = side.find('p', 'cmp-t').text()
                parts.append(f'<CompareItem kind="{kind}" label={attr(label)}>\n\n' + fence(side.find('pre').text()) + '\n\n</CompareItem>')
            parts.append('</Compare>')
            out.append('\n\n'.join(parts))
        elif t == 'div' and 'layers' in cl:
            items = []
            for ly in c.kids('div', 'layer'):
                ps = ly.kids('p')
                items.append(f'<Layer title={attr(ps[0].text())}>{inline(ps[1]).strip()}</Layer>')
            out.append('<Layers>\n' + '\n'.join(items) + '\n</Layers>')
        elif t == 'div' and 'flow' in cl:
            items = []
            for st in c.kids('div'):
                items.append(f'<FlowStep code={attr(st.find("code").text())}>{inline(st.find("p")).strip()}</FlowStep>')
            out.append('<Flow>\n' + '\n'.join(items) + '\n</Flow>')
        elif t == 'div' and 'log' in cl:
            items = []
            for row in c.kids('div', 'log-row'):
                meta, body = row.kids()
                v, d = meta.find('p', 'log-v').text(), meta.find('p', 'log-d').text()
                items.append(f'<ChangelogEntry version={attr(v)} date={attr(d)}>{inline(body).strip()}</ChangelogEntry>')
            out.append('<Changelog>\n' + '\n'.join(items) + '\n</Changelog>')
        elif t == 'div' and 'chips' in cl:
            roles = [ch.find('span', 'chip-n').text() for ch in c.kids('div', 'chip')]
            out.append(f'<BrandColors group="{Ctx.group}" roles="{",".join(roles)}" />')
        elif t == 'div' and 'space-list' in cl:
            out.append('<SpacingScale />')
        elif t == 'div' and 'sim' in cl:
            out.append('<BrandSimulator />')
        else:
            raise ValueError(f'bloco desconhecido: {t} {cl}')
    return out


def to_mdx(nodes):
    Ctx.emitted = set()
    Ctx.group = None
    return '\n\n'.join(blocks(nodes)).strip() + '\n'


# ---------- leitura do HTML ----------
b = Builder()
b.feed(open(HTML_PATH, encoding='utf-8').read())
main = b.root.find('main')
sections = main.kids('section', 'page')
print(len(sections), 'seções')

# ---------- dados (fonte python da v0.1) ----------
sys.path.insert(0, SRC_DIR)
os.chdir(SRC_DIR)
from comps import COMPS, LEGACY  # noqa: E402
import pages_comp  # noqa: E402

data_dir = os.path.join(ROOT, 'src', 'data')
os.makedirs(data_dir, exist_ok=True)
comps = [dict(name=n, category=c, variants=v, properties=p, description=d) for n, c, v, p, d in COMPS]
json.dump(dict(exportedAt='2026-10-26', kitVersion='0.4', components=comps, legacy=LEGACY),
          open(os.path.join(data_dir, 'components.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
json.dump(pages_comp.REL, open(os.path.join(data_dir, 'component-relations.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
vars_json = json.load(open('vars.json', encoding='utf-8'))
json.dump(vars_json, open(os.path.join(data_dir, 'tokens.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

# escala de espaçamento (extraída do HTML gerado)
cores_like = {s.attrs['data-id']: s for s in sections}
sl = cores_like['espacamento'].find('div', 'space-list')
spacing = [[row.find('code').text().split('/')[1], row.kids('span')[-1].text()] for row in sl.kids('div', 'space-row')]
json.dump(spacing, open(os.path.join(data_dir, 'spacing.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

# ---------- MDX ----------
docs_dir = os.path.join(ROOT, 'content', 'docs')
comp_dir = os.path.join(ROOT, 'content', 'componentes')
os.makedirs(docs_dir, exist_ok=True)
os.makedirs(comp_dir, exist_ok=True)

for s in sections:
    pid = s.attrs['data-id']
    prose = s.find('div', 'prose')
    if not pid.startswith('c-'):
        open(os.path.join(docs_dir, pid + '.mdx'), 'w', encoding='utf-8', newline='\n').write(to_mdx(prose.children))
        continue
    name = s.attrs['data-title']
    if name not in pages_comp.DEEP:
        continue
    kids = [c for c in prose.children if isinstance(c, Node)]
    start = next(i for i, c in enumerate(kids) if c.tag == 'h2' and c.attrs.get('id') == 'por-que')
    end = next(i for i, c in enumerate(kids) if c.tag == 'h2' and c.attrs.get('id') in ('relacionados', 'atualizacoes'))
    open(os.path.join(comp_dir, slug(name) + '.mdx'), 'w', encoding='utf-8', newline='\n').write(to_mdx(kids[start:end]))

# leads das páginas de componentes, para conferir
print(json.dumps({s.attrs['data-title']: s.find('p', 'lead').text() for s in sections if s.attrs['data-id'].startswith('c-')}, ensure_ascii=False)[:600])
print('ok')
