from helpers import *
import pages_a, pages_b, pages_c, pages_d, pages_comp
from comps import COMPS

PAGES = [
 ('Começando', 'inicio', 'Norden UI KIT', 'A base de interface do time para e-commerce: fundamentos, tokens e componentes, e como usá-los com IA.', pages_a.inicio),
 ('Começando', 'arquitetura', 'Arquitetura do kit', 'Camadas, collections, páginas e convenções de nome.', pages_a.arquitetura),
 ('Trabalhar com IA', 'ia', 'Como trabalhar com IA', 'Dar contexto, pedir de forma verificável, conferir e iterar.', pages_a.ia),
 ('Style Guide', 'cores', 'Cores', 'Cores da marca, tokens semânticos e estados de interação.', pages_b.cores),
 ('Style Guide', 'tipografia', 'Tipografia', 'Família, escala responsiva e hierarquia no e-commerce.', pages_b.tipografia),
 ('Style Guide', 'espacamento', 'Espaçamento, layout e forma', 'Escalas de espaço, alturas de controle, breakpoints, raios e sombras.', pages_b.espacamento),
 ('Style Guide', 'tokens', 'Variáveis e tokens', 'Como os valores se organizam e se propagam.', pages_b.tokens),
 ('Guias', 'adaptar-marca', 'Adaptar para uma nova marca', 'Do kit base à identidade do cliente, em dez etapas.', pages_c.adaptar),
 ('Guias', 'processo', 'Processo de um novo projeto', 'Do briefing ao handoff.', pages_c.processo),
 ('Componentes', 'componentes', 'Componentes', 'Inventário real do kit e situação da documentação.', pages_comp.index_page),
]
for name, cat, n, props, desc in COMPS:
    PAGES.append(('Componentes · ' + pages_comp.CATS.get(cat, cat), pages_comp.cid(name), name, desc.split('. ')[0] + '.' if desc else 'Componente do kit sem descrição no Figma.', (lambda a=(name, cat, n, props, desc): pages_comp.comp_page(*a))))
PAGES += [
 ('Padrões', 'padroes', 'Padrões de interface', 'Como os componentes se combinam em partes da loja.', pages_c.padroes),
 ('IA e manutenção', 'skill', 'Skill geral para IA', 'A instrução que ensina qualquer IA a trabalhar dentro do kit.', pages_d.skill),
 ('IA e manutenção', 'manutencao', 'Manutenção da documentação', 'Fontes de verdade, atualização, revisão e pendências.', pages_d.manutencao),
 ('IA e manutenção', 'changelog', 'Changelog', 'Histórico do kit e da documentação.', pages_d.changelog),
]

def nav():
    out, last = '', None
    groups = {}
    order = []
    for g, i, t, l, f in PAGES:
        top = g.split(' · ')[0]
        if top not in groups: groups[top] = []; order.append(top)
        groups[top].append((g, i, t))
    for top in order:
        out += f'<div class="nav-g"><p class="nav-gt">{top}</p>'
        if top == 'Componentes':
            out += f'<a href="#componentes" data-id="componentes">Visão geral</a>'
            sub = {}
            for g, i, t in groups[top]:
                if ' · ' in g: sub.setdefault(g.split(' · ')[1], []).append((i, t))
            for s, items in sub.items():
                out += f'<details class="nav-sub"><summary>{s}</summary>' + ''.join(f'<a href="#{i}" data-id="{i}">{t.split("/")[-1]}</a>' for i, t in items) + '</details>'
        else:
            out += ''.join(f'<a href="#{i}" data-id="{i}">{t}</a>' for g, i, t in groups[top])
        out += '</div>'
    return out

sections = ''
for g, i, t, l, f in PAGES:
    body = f()
    crumb = g.replace(' · ', ' / ')
    sections += f'<section class="page" id="pg-{i}" data-id="{i}" data-title="{esc(t)}" data-group="{esc(crumb)}" hidden><header class="ph"><p class="crumb">{crumb}</p><h1>{t}</h1><p class="lead">{l}</p><p class="ph-meta">Kit v0.4 Beta · Atualizado em 26/10/2026</p></header><div class="prose">{body}</div><nav class="pn" aria-label="Navegação entre páginas"></nav></section>'

CSS = open('style.css').read()
JS = open('app.js').read()
html_out = f'''<!doctype html>
<html lang="pt-BR" data-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Norden UI KIT · Documentação</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Rethink+Sans:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<header class="top">
 <button class="menu-btn" type="button" aria-label="Abrir navegação" aria-expanded="false"><svg width="18" height="18" viewBox="0 0 18 18" aria-hidden="true"><path d="M2 5h14M2 9h14M2 13h14" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg></button>
 <a class="brand" href="#inicio"><span class="brand-mark" aria-hidden="true"></span><span>Norden UI KIT</span><span class="brand-docs">Docs</span></a>
 <button class="search-btn" type="button" aria-label="Buscar na documentação"><svg width="15" height="15" viewBox="0 0 16 16" aria-hidden="true"><circle cx="7" cy="7" r="5" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M11 11l3.5 3.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg><span>Buscar na documentação</span><kbd>/</kbd></button>
 <span class="ver">Kit v0.4 Beta</span>
 <button class="theme-btn" type="button" aria-label="Alternar tema claro e escuro"><svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="6" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M8 2a6 6 0 0 1 0 12z" fill="currentColor"/></svg></button>
</header>
<div class="shell">
 <aside class="side" aria-label="Navegação da documentação"><nav>{nav()}</nav></aside>
 <main class="main" id="main">{sections}</main>
 <aside class="toc" aria-label="Nesta página"><p class="toc-t">Nesta página</p><nav id="toc"></nav></aside>
</div>
<div class="search" id="search" hidden><div class="search-box" role="dialog" aria-modal="true" aria-label="Buscar"><div class="search-in"><svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><circle cx="7" cy="7" r="5" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M11 11l3.5 3.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg><input id="q" type="search" placeholder="Buscar componentes, tokens, prompts…" autocomplete="off" spellcheck="false"><kbd>Esc</kbd></div><ul id="results" role="listbox"></ul></div></div>
<div class="toast" id="toast" role="status" aria-live="polite"></div>
<script>{JS}</script>
</body>
</html>'''
open(__import__('os').environ.get('OUT', 'dist/index.html'), 'w').write(html_out)
print(len(html_out), 'bytes,', len(PAGES), 'pages')
