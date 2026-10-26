import json
from helpers import *
D = json.load(open('vars.json'))
BRAND = {v[0]: v for v in D['Brand']['vars']}
COLOR = D['Color']

def _brand_group(prefix, roles):
    cells = ''
    for r in roles:
        n = f'{prefix}/{r}'; hx = BRAND[n][2]
        cells += f'<div class="chip"><span class="chip-sw" style="--sw:{hx}"></span><span class="chip-n">{r}</span><span class="chip-v">{hx}</span></div>'
    return f'<div class="chips">{cells}</div>'

def cores():
    b = p('As cores do kit funcionam em duas camadas. A camada <strong>Brand</strong> guarda as cores da identidade do cliente. A camada <strong>Color</strong> dá uma função a cada cor: “texto principal”, “fundo do botão primário”, “preço riscado”. Os componentes só usam a camada Color.')
    b += callout('info', 'Cor da marca × cor semântica', p('A cor da marca responde “qual é o vermelho da empresa?”. A cor semântica responde “qual cor usar no preço?”. Separar as duas permite trocar a marca inteira editando poucos valores, e permite mudar o papel de uma cor (ex.: preço em neutro) sem tocar na marca.'))
    b += h2('Cores da marca (Brand)')
    b += p('Cada cor de marca tem cinco papéis. Os valores abaixo são o padrão neutro do kit base, substituídos em cada projeto. ' + badge('impl'))
    b += table(['Papel', 'Para que serve'], [
        ['<code>default</code>', 'A cor oficial do manual.'],
        ['<code>hover</code>', 'Tom mais escuro, usado no hover do desktop. Decisão do kit: hover sempre escurece.'],
        ['<code>subtle</code>', 'Tom bem claro para fundos suaves, seleção discreta e chips ativos.'],
        ['<code>text</code>', 'Versão com contraste AA (4,5:1) sobre branco: links, preço, ícones e contornos. Em marcas claras (amarelo, laranja) fica mais escura que o default.'],
        ['<code>on-color</code>', 'Texto e ícone aplicados sobre o default, como a label do botão. Precisa de AA com o default.']])
    b += h3('Primary')
    b += p('A cor de ação e identidade mais forte: botão primário, links, seleção, preço.') + _brand_group('primary', ['default', 'hover', 'subtle', 'text', 'on-color'])
    b += h3('Secondary')
    b += p('Segunda cor institucional: faixas, fundos de apoio, áreas de destaque que não competem com a ação principal.') + _brand_group('secondary', ['default', 'hover', 'subtle', 'text', 'on-color'])
    b += h3('Accent')
    b += p('Destaque comercial: tags de promoção e texto de desconto (via tokens <code>commerce/*</code>).') + _brand_group('accent', ['default', 'hover', 'subtle', 'text', 'on-color'])
    b += h3('Neutral')
    b += p('Escala de 50 a 950 para fundos, superfícies, bordas e textos. Regra do kit: <strong>neutral/500 é o primeiro tom com AA sobre branco e sobre neutral/50</strong>, por isso é usado em texto terciário e preço riscado.') + _brand_group('neutral', ['50', '100', '200', '300', '400', '500', '600', '700', '800', '900', '950'])
    b += h3('Feedback')
    b += p('Sucesso, atenção, erro e informação, cada um com default (ícones e bordas), subtle (fundos) e text (textos com AA). São neutros em relação à marca: só mudam se conflitarem com ela.')
    for f in ['success', 'warning', 'error', 'info']:
        b += f'<p class="mini-t">{f}</p>' + _brand_group(f'feedback/{f}', ['default', 'subtle', 'text'])
    b += h2('Tokens semânticos (Color)')
    b += p('São 85 tokens agrupados por função. Cada um aponta para uma cor da Brand. Clique num nome para copiar.')
    groups = {}
    for name, ref, hx, use in COLOR:
        groups.setdefault(name.split('/')[0], []).append((name, ref, hx, use))
    labels = {'text': 'Texto', 'icon': 'Ícones', 'background': 'Fundos', 'surface': 'Superfícies', 'border': 'Bordas', 'commerce': 'Comércio', 'overlay': 'Sobreposição', 'shadow': 'Sombras'}
    for g, rows in groups.items():
        b += h3(f'{labels.get(g, g)} <span class="h-note">{g}/*</span>', f'tok-{g}')
        b += table(['Token', 'Aponta para', 'Uso'], [[f'<span class="sw" style="--sw:{hx.split(" ")[0]}"></span><button class="tok" type="button">{n}</button>', f'<code>{r}</code>', u] for n, r, hx, u in rows], 'tok-tbl')
    b += h2('Estados de interação')
    b += table(['Estado', 'Como o kit resolve'], [
        ['Hover', 'Só no desktop. Botões escurecem (<code>*/hover</code>); campos ganham borda escura (<code>border/hover</code>); itens de lista usam <code>surface/hover</code>.'],
        ['Focus', 'Existe o effect style <code>focus-ring</code> e o token <code>border/focus</code>. Os botões do kit não têm estado Focus por decisão de projeto. ' + badge('pend', 'Revisar acessibilidade de teclado')],
        ['Pressed', 'Não há estado Pressed nos botões. Itens de lista e menu usam <code>surface/pressed</code>.'],
        ['Disabled', 'Fundo <code>background/disabled</code> ou <code>background/button/disabled</code>, texto <code>text/disabled</code>. Texto desabilitado é isento de contraste mínimo, mas precisa ser perceptível.'],
        ['Selected', '<code>background/selected</code> e <code>border/selected</code> para controles marcados; <code>background/selected-subtle</code> para seleção suave.']])
    b += h2('Por que isso importa no e-commerce')
    b += ul(['<strong>Hierarquia de compra:</strong> o botão primário é a única coisa com a cor mais forte da tela; preço e desconto têm tokens próprios para se destacarem sem competir com o CTA.',
             '<strong>Confiança:</strong> estados de erro e sucesso consistentes em todo o funil (campo, carrinho, checkout).',
             '<strong>Legibilidade:</strong> textos com AA garantem leitura de preço, parcelamento e prazos, inclusive em telas pequenas e ao sol.'])
    b += h2('Erros comuns')
    b += ul(['Pintar com hex direto no componente. Sempre use um token.',
             'Usar a cor da marca como texto quando ela não passa contraste. Use <code>primary/text</code> (via <code>text/brand</code>).',
             'Trocar tudo pela cor primária: tags, preço, botões e faixas na mesma cor apagam a hierarquia.',
             'Recolorir sucesso e erro com as cores da marca sem necessidade.'])
    b += h2('Simulador de cor da marca')
    b += p('Teste uma cor primária e veja os cinco papéis que o kit precisa, com o contraste de cada um. É a mesma lógica do script de paleta usado no tutorial de adaptação. ' + badge('rec', 'Ferramenta de apoio'))
    b += '''<div class="sim" id="sim">
<div class="sim-in"><label for="sim-color">Cor primária</label><div class="sim-row"><input type="color" id="sim-color" value="#ED1D24" aria-label="Escolher cor"><input type="text" id="sim-hex" value="#ED1D24" spellcheck="false" aria-label="Hex da cor"></div></div>
<div class="sim-roles" id="sim-roles"></div>
<div class="sim-prev" id="sim-prev"><button type="button" class="sp-btn">Adicionar ao carrinho</button><span class="sp-tag">Novo</span><span class="sp-price">R$ 49,90</span><a class="sp-link">Ver detalhes do produto</a></div>
<p class="sim-note" id="sim-note"></p></div>'''
    b += h2('Adaptando para uma nova marca')
    b += p('Exemplo real: na adaptação da marca Stok Center (vermelho #ED1D24, grafite #414042, amarelo #FFF200), o amarelo virou <code>accent</code> e precisou de uma versão de texto escurecida (#797300), porque amarelo puro não tem contraste sobre branco. O vermelho com texto branco ficou em 4,37:1 e foi aceito como decisão de marca, documentada.')
    return b

def tipografia():
    b = p('A tipografia define a ordem de leitura de cada tela: o que é título, o que é preço, o que é informação de apoio. No kit, a família e os pesos vêm de variáveis, e os tamanhos dos títulos mudam com o breakpoint.')
    b += h2('Família e pesos')
    b += table(['Variável (Brand)', 'Valor no kit base', 'Observação'], [
        ['<code>font/family/heading</code>', 'Rethink Sans', 'Títulos (Display e Heading).'],
        ['<code>font/family/body</code>', 'Rethink Sans', 'Corpo, labels, botões e preços.'],
        ['<code>font/weight/regular · medium · semibold · bold</code>', 'Regular · Medium · Semi Bold · Bold', 'O nome do peso muda entre fontes (“Semi Bold”, “SemiBold”, “Demi”). Escreva exatamente como aparece no Figma.']])
    b += callout('warn', 'Fonte da marca precisa estar disponível', p('Se a fonte do cliente estiver instalada só no computador de um designer, outras pessoas e ferramentas de IA não conseguem usá-la. Isso aconteceu no projeto Stok com a D-DIN-PRO: a IA precisou trocar a fonte para Roboto temporariamente para criar textos. Antes de trocar a fonte do kit, confirme que ela está disponível para o time.'))
    b += h2('Escala')
    rows = [
        ('Display/Large', '36 → 56', '44 → 64', 'Regular, Medium, SemiBold, Bold', 'Hero e banners.'),
        ('Display/Medium', '32 → 44', '40 → 52', 'Regular, Medium, SemiBold, Bold', 'Títulos de campanha.'),
        ('Heading/H1', '28 → 40', '36 → 48', 'Regular, Medium, SemiBold, Bold', 'Título da página (PLP, PDP, carrinho).'),
        ('Heading/H2', '24 → 32', '32 → 40', 'Regular, Medium, SemiBold, Bold', 'Título de seção e vitrine.'),
        ('Heading/H3', '20 → 24', '28 → 32', 'Regular, Medium, SemiBold, Bold', 'Subtítulo, título de card de conteúdo e de drawer.'),
        ('Heading/H4', '18 → 20', '26 → 28', 'Regular, Medium, SemiBold, Bold', 'Títulos pequenos, cabeçalhos de accordion.'),
        ('Body/Large', '18', '28', 'Regular, Medium, SemiBold, Bold', 'Textos de destaque e introduções.'),
        ('Body/Medium', '16', '24', 'Regular, Medium, SemiBold, Bold', 'Corpo padrão e texto de campos (sempre 16px).'),
        ('Body/Small', '14', '20', 'Regular, Medium, SemiBold, Bold', 'Nome de produto no card, descrições curtas.'),
        ('Label/Large · Medium · Small', '16 · 14 · 12', '24 · 20 · 16', 'Regular, Medium, SemiBold, Bold', 'Rótulos de campos, abas e filtros.'),
        ('Caption', '12', '16', 'Regular, Medium, SemiBold, Bold', 'Legendas, contadores, textos legais.'),
        ('Overline', '12', '16', 'Regular, Medium, SemiBold, Bold', 'Rótulos em caixa alta (títulos de grupo do footer).'),
        ('Button/Large · Medium · Small', '18 · 16 · 14', '24 · 24 · 20', 'Regular, Medium, SemiBold, Bold', 'Labels de botão por tamanho.'),
        ('Price/Large', '24 → 28', '32 → 36', 'Regular, Medium, SemiBold, Bold', 'Preço da PDP.'),
        ('Price/Medium', '18', '24', 'Regular, Medium, SemiBold, Bold', 'Preço no card.'),
        ('Price/Small', '14', '20', 'Regular, Medium, SemiBold, Bold', 'Preço no minicart, carrinho e busca.'),
        ('Price/Old', '12', '16', 'Regular, Medium, SemiBold, Bold', 'Preço riscado (já vem com tachado).')]
    def sample(n):
        g = n.split('/')[0]; size = {'Display': 30, 'Heading': 22, 'Price': 20}.get(g, 16)
        w = 700 if g in ('Display', 'Price') else 600 if g in ('Heading', 'Button', 'Label', 'Overline') else 400
        tt = 'text-transform:uppercase;letter-spacing:.04em;' if g == 'Overline' else ''
        dec = 'text-decoration:line-through;' if n == 'Price/Old' else ''
        txt = {'Price': 'R$ 129,90', 'Button': 'Adicionar', 'Overline': 'Institucional'}.get(g, 'Arroz tipo 1')
        return f'<span class="ts" style="font-size:{min(size,30)}px;font-weight:{w};{tt}{dec}">{txt}</span>'
    b += table(['Estilo', 'Tamanho (px)', 'Altura de linha', 'Pesos', 'Uso', 'Amostra'], [[f'<code>{a}</code>', s, l, w, u, sample(a)] for a, s, l, w, u in rows], 'type-tbl')
    b += p('Onde aparece “→”, o valor muda do mobile para o desktop por meio da collection Responsive. Um frame de tela no mode Mobile renderiza os títulos menores automaticamente. ' + badge('impl'))
    b += h2('Nome dos estilos')
    b += p('Formato <code>Grupo/Tamanho/Peso · tamanho/altura</code>, por exemplo <code>Body/Medium/Regular · 16/24</code>. O sufixo numérico ajuda a escolher o estilo sem abrir o painel.')
    b += h2('Hierarquia no e-commerce')
    b += table(['Tela', 'Como a tipografia organiza'], [
        ['Card de produto', 'Nome em Body/Small (até 2 linhas), preço em Price/Medium, preço riscado em Price/Old, parcelamento em Caption.'],
        ['PDP', 'Nome em Heading/H1, preço em Price/Large, descrições em Body/Medium.'],
        ['Carrinho e minicart', 'Nomes em Body/Small, preços em Price/Small, total em destaque com peso maior.'],
        ['Checkout', 'Labels de campos em Label/Medium e texto digitado em Body/Medium (16px).'],
        ['Menu e footer', 'Itens em Body/Medium, títulos de grupo em Overline ou Caption/SemiBold.']])
    b += h2('Erros comuns')
    b += ul(['Campo de formulário com texto menor que 16px: o iOS dá zoom na página ao focar.', 'Muitos pesos na mesma tela: escolha no máximo dois por bloco.', 'Usar Display em telas mobile densas: reserve para banners.', 'Escrever o nome do peso errado na variável (a fonte “quebra” e o Figma mostra fonte ausente).'])
    return b

def espacamento():
    b = p('Espaço, tamanho e forma seguem escalas fechadas. Isso dá ritmo às telas e evita a sensação de “quase alinhado”.')
    b += h2('Escala de espaçamento')
    b += p('Grade de 4. O nome do token é o valor em pixels. Use em gaps e paddings. ' + badge('impl'))
    sp = [('0', 'Elementos colados.'), ('2', 'Ajuste fino: padding vertical de tags.'), ('4', 'Ícone e texto em elementos pequenos; label e campo.'), ('8', 'Ícone e texto em botões; itens próximos.'), ('12', 'Padding de cards e tags maiores; gap no card.'), ('16', 'Padding padrão de componentes; margem lateral no mobile.'), ('20', 'Padding de containers médios (drawers, modais no mobile).'), ('24', 'Gap entre cards de uma vitrine; padding de modais no desktop.'), ('32', 'Espaço entre blocos de uma seção.'), ('40', 'Blocos maiores; separação de seções no mobile.'), ('48', 'Separação de seções.'), ('64', 'Separação de seções no desktop.'), ('80', 'Respiro de banners e hero.'), ('96', 'Respiro de destaque no desktop.'), ('128', 'Grandes respiros; uso raro.')]
    b += '<div class="space-list">' + ''.join(f'<div class="space-row"><code>spacing/{n}</code><span class="space-bar" style="width:{max(int(n),1)*2}px"></span><span>{u}</span></div>' for n, u in sp) + '</div>'
    b += h2('Altura de controles')
    b += table(['Token', 'Altura', 'Uso'], [['<code>size/control/xs</code>', '32', 'Botões de ícone sobre imagens, quantidade do minicart.'], ['<code>size/control/sm</code>', '40', 'Contextos densos do desktop: chips, ordenação.'], ['<code>size/control/md</code>', '48', 'Padrão: botões, inputs, select, busca, quantidade. Área de toque confortável no mobile.'], ['<code>size/control/lg</code>', '56', 'CTA principal da PDP e do checkout.']])
    b += h2('Layout e breakpoints')
    b += table(['Token (Responsive)', 'Mobile', 'Tablet', 'Desktop'], [['<code>layout/viewport</code>', '393', '768', '1440'], ['<code>layout/margin</code>', '16', '32', '40'], ['<code>layout/header-padding-top</code>', '240', '120', '160']])
    b += p('As larguras seguem os breakpoints do FastStore. A margem é o padding lateral do frame de tela. O padding superior evita que o conteúdo fique embaixo do header, que fica sobreposto.')
    b += callout('pending', 'Pendente de validação', p('Os valores de <code>layout/header-padding-top</code> são provisórios: precisam ser iguais à altura final do header em cada breakpoint. Também falta definir grid de colunas e largura máxima de conteúdo no desktop. ' + badge('pend')))
    b += h2('Raios (Shape)')
    b += p('Cada tipo de componente tem seu token de raio, e cada mode da collection é um preset. Na cópia do projeto, escolha o preset e apague os outros: o que sobrar vira o padrão do arquivo. O nome do mode é o raio de botões e campos.')
    b += table(['Token', '10px (padrão)', 'None', '6px', '16px', '24px', 'Full'], [
        ['<code>radius/button</code>', '10', '0', '6', '16', '24', 'pílula'], ['<code>radius/input</code>', '10', '0', '6', '16', '24', 'pílula'], ['<code>radius/card</code>', '12', '0', '8', '24', '32', '16'], ['<code>radius/media</code>', '8', '0', '6', '16', '24', '12'], ['<code>radius/tag</code>', '6', '0', '4', '8', '12', 'pílula'], ['<code>radius/checkbox</code>', '6', '0', '4', '6', '6', '6'], ['<code>radius/modal</code>', '16', '0', '12', '32', '32', '24'], ['<code>radius/circle</code>', 'círculo', 'círculo', 'círculo', 'círculo', 'círculo', 'círculo']])
    b += p('Decisões: a mídia fica um degrau abaixo do card para acompanhar o padding interno; o checkbox fica sempre discreto para não parecer um radio; o círculo nunca muda.')
    b += h2('Sombras (elevation)')
    b += table(['Estilo', 'Composição', 'Uso'], [['<code>elevation/1</code>', 'y1 blur2 + y2 blur6', 'Cards em hover (desktop) e header fixo ao rolar.'], ['<code>elevation/2</code>', 'y2 blur4 spread−1 + y8 blur16 spread−4', 'Dropdowns, painel de busca, tooltips.'], ['<code>elevation/3</code>', 'y4 blur8 spread−2 + y20 blur40 spread−8', 'Modais e drawers.'], ['<code>focus-ring</code>', 'spread 4 + spread 2', 'Foco por teclado (anel duplo).']])
    b += p('As cores das sombras vêm de <code>shadow/soft</code> e <code>shadow/strong</code>. Para sombras tingidas pela marca, aponte esses tokens para uma cor da marca com transparência.')
    b += h2('Bordas')
    b += p('Não há tokens de espessura: bordas são fixas em 1px; 2px em seleção e destaques. A cor vem sempre de <code>border/*</code>.')
    b += h2('Erros comuns')
    b += ul(['Valores fora da escala (13, 15, 18px de gap).', 'Ajustar raio elemento por elemento em vez de escolher o preset.', 'Esquecer de aplicar o mode Mobile no frame de tela: títulos ficam no tamanho de desktop.', 'Sombra em tudo: reserve para elementos que realmente flutuam.'])
    return b

def tokens():
    b = p('Tokens são variáveis com nome de função. Em vez de “#1C1C21”, o componente usa <code>text/primary</code>. Quando a marca muda, muda o valor; o nome e o componente continuam iguais.')
    b += h2('Os quatro tipos de valor')
    b += table(['Tipo', 'Onde fica no kit', 'Exemplo'], [
        ['Primitivos', 'Primitives (oculta) e Brand', '<code>radius/xl = 10</code>, <code>neutral/900 = #1C1C21</code>'],
        ['Semânticos', 'Color', '<code>text/secondary → neutral/600</code>'],
        ['De componente', 'Color (grupos button/footer) e Shape', '<code>background/button/primary/hover</code>, <code>radius/card</code>'],
        ['De ambiente e layout', 'Responsive, Dimension, Prototype', '<code>layout/margin</code>, <code>size/control/md</code>, <code>cart/quantity</code>']])
    b += h2('Como uma troca de marca se propaga')
    b += '<div class="flow"><div><code>Brand / primary/default</code><p>#1C1C21 → #ED1D24</p></div><span class="flow-a" aria-hidden="true"></span><div><code>Color / background/button/primary/default</code><p>continua apontando para primary/default</p></div><span class="flow-a" aria-hidden="true"></span><div><code>Actions/Button Primary</code><p>fica vermelho em todas as telas</p></div></div>'
    b += p('Um único valor editado atualiza todos os botões, links, seleções e preços do arquivo.')
    b += h2('Escopos')
    b += p('Cada token semântico tem escopo: tokens de texto só aparecem no seletor de cor de texto, tokens de borda só no de contorno. As variáveis da Brand não têm escopo, para que ninguém as aplique direto em componentes. ' + badge('impl'))
    b += h2('Quando criar um token novo')
    b += ul(['Quando uma função nova aparece em mais de um componente (ex.: os tokens <code>*/footer</code> nasceram com o footer escuro).', 'Quando um projeto precisa mudar o papel de uma cor sem afetar outras.', 'Nunca para um uso único que um token existente já resolve.'])
    b += prompt('Propor um token novo sem quebrar o sistema', '''Preciso de uma cor para o selo "Recomendado" (verde) no card de opção.
Antes de criar qualquer coisa:
1. Verifique se algum token existente já cumpre essa função
   (ex.: background/success-subtle + text/success).
2. Se nenhum servir, proponha o nome do token novo seguindo o
   padrão funcao/detalhe, a collection, o valor apontado e o escopo.
Não crie nada até eu aprovar.''')
    return b
