import html, re
def esc(s): return html.escape(s, quote=False)
def slug(s):
    import unicodedata
    s = unicodedata.normalize('NFD', s).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')
def h2(t, i=None): return f'<h2 id="{i or slug(t)}">{t}</h2>'
def h3(t, i=None): return f'<h3 id="{i or slug(t)}">{t}</h3>'
def p(t): return f'<p>{t}</p>'
def ul(items): return '<ul>' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>'
def ol(items): return '<ol>' + ''.join(f'<li>{x}</li>' for x in items) + '</ol>'
def c(t): return f'<code>{t}</code>'
BADGES = {'impl': 'Implementado', 'rec': 'Recomendação', 'prop': 'Proposta', 'pend': 'Pendente de validação'}
def badge(k, label=None): return f'<span class="badge b-{k}">{label or BADGES[k]}</span>'
def callout(kind, title, body):
    return f'<div class="callout c-{kind}"><p class="callout-t">{title}</p><div>{body}</div></div>'
def table(headers, rows, cls=''):
    th = ''.join(f'<th>{h}</th>' for h in headers)
    tr = ''.join('<tr>' + ''.join(f'<td>{x}</td>' for x in r) + '</tr>' for r in rows)
    return f'<div class="tbl {cls}"><table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'
_pc = [0]
def prompt(title, text, note=None):
    """Texto do prompt; linhas que começam com '## ' abrem um bloco copiável separado."""
    _pc[0] += 1
    text = re.sub(r'"([^"\n]*)"', lambda m: "\u201c" + m.group(1) + "\u201d", text)
    segs, cur = [], []
    for line in text.strip('\n').split('\n'):
        if line.startswith('## ') and cur:
            segs.append(cur); cur = []
        cur.append(line)
    if cur: segs.append(cur)
    body = ''
    for s in segs:
        head = s[0][3:] if s[0].startswith('## ') else None
        content = '\n'.join(s[1:] if head else s).strip('\n')
        body += '<div class="pseg">' + (f'<div class="pseg-h"><span>{esc(head)}</span><button class="copy-seg" type="button" aria-label="Copiar o bloco {esc(head)}">Copiar bloco</button></div>' if head else '') + f'<pre>{esc((("## " + head + chr(10)) if head else "") + content)}</pre></div>'
    n = f'<p class="prompt-note">{note}</p>' if note else ''
    return f'<figure class="prompt" id="prompt-{_pc[0]}"><figcaption><span class="prompt-t">{title}</span><button class="copy-all" type="button">Copiar prompt</button></figcaption>{body}</figure>{n}'
def steps(items):
    """items: list of (title, html)"""
    return '<ol class="steps">' + ''.join(f'<li><h3 id="{slug(t)}">{t}</h3>{b}</li>' for t, b in items) + '</ol>'
def swatch(hexv, label=''):
    return f'<span class="sw" style="--sw:{hexv}" title="{hexv}"></span>{label}'
