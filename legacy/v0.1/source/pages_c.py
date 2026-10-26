from helpers import *

def _step(obj, ctx, figma, errs, valid, ptitle, ptext):
    return (f'<dl class="sdl"><dt>Objetivo</dt><dd>{obj}</dd><dt>Contexto necessário</dt><dd>{ctx}</dd><dt>No Figma</dt><dd>{figma}</dd><dt>Erros comuns</dt><dd>{errs}</dd><dt>Como validar</dt><dd>{valid}</dd></dl>' + prompt(ptitle, ptext))

def adaptar():
    b = p('Este tutorial leva você do kit base até uma cópia com a identidade do cliente, pronta para receber as telas. Cada etapa tem objetivo, contexto, instruções no Figma, erros comuns, critérios de validação e um prompt pronto.')
    b += callout('info', 'Antes de começar', ul(['Duplique o arquivo base e renomeie para “Norden UI KIT — [Cliente]”. O arquivo base nunca é editado por um projeto.', 'Reúna o material de marca: manual, logo em SVG, fontes, site atual e, se houver, o wireframe.', 'Tenha em mãos a <a href="#skill">skill geral</a> para colar no início da conversa com a IA.']))
    items = [
     ('Analisar o material de marca', _step('Entender a identidade antes de mexer em qualquer valor.', 'Manual de marca, site atual, logo, fontes.', 'Nada ainda. Separe as referências numa página de trabalho, se quiser.', 'Tratar cores de rascunho do wireframe (cinzas, azul padrão de ferramenta) como cores da marca.', 'Você consegue listar as cores oficiais, a fonte e o estilo de cantos da marca.',
       'Analisar a marca sem alterar nada', '''## Tarefa
Analise o material de marca anexo (manual, prints do site, logo).
Não altere nenhum arquivo.
## O que eu preciso de volta
1. Cores oficiais (hex) e onde cada uma aparece.
2. Fonte(s) e pesos usados.
3. Estilo de cantos (retos, levemente arredondados, pílula).
4. O que estiver ausente ou ambíguo, marcado como "não encontrado".
Não invente valores.''')),
     ('Identificar cores, tipografia e diretrizes', _step('Classificar o que foi encontrado nos papéis do kit.', 'Resultado da etapa 1.', 'Nada ainda.', 'Forçar três cores quando a marca tem uma. Nesse caso, secondary pode ser um tom escuro neutro.', 'Cada cor da marca tem um papel: primary, secondary ou accent.',
       'Classificar as cores nos papéis do kit', '''Com base na análise anterior, classifique as cores da marca nos
papéis do Norden UI KIT:
- primary: cor de ação e identidade (botões, links, seleção)
- secondary: segunda cor institucional (faixas, fundos de apoio)
- accent: destaque comercial (promoção, desconto)
Explique a escolha de cada uma. Se a marca tiver menos de três
cores, diga o que sugere para o papel vazio e por quê.''')),
     ('Mapear diferenças com o Style Guide', _step('Saber o que muda e o que fica.', 'Collections Brand, Color e Shape da cópia.', 'Abra Local variables e compare com as cores e fontes levantadas.', 'Querer mudar tokens semânticos antes da Brand.', 'Você tem uma lista do que muda na Brand e de quais pontos de ajuste podem ser necessários.',
       'Mapear o que muda no kit', '''Inspecione a cópia do kit [link]: collections Brand, Color e Shape.
Compare com a análise da marca e liste:
1. Variáveis da Brand que mudam (valor atual → novo).
2. Variáveis que ficam como estão.
3. Pontos de ajuste que podem ser necessários
   (preço em neutro, promoções em verde, footer claro).
Não altere nada.''')),
     ('Definir a paleta e as funções', _step('Gerar os cinco papéis de cada cor (default, hover, subtle, text, on-color) e escolher os neutros.', 'Cores classificadas na etapa 2.', 'Use o <a href="#cores">simulador</a> ou o script de paleta da skill para gerar os valores.', 'Usar a cor da marca como texto sem checar contraste; hover mais claro que o default.', 'Todos os pares críticos com AA ou com a exceção documentada.',
       'Gerar os papéis de cada cor', '''Para cada cor (primary, secondary, accent), gere os papéis do kit:
- default: a cor oficial
- hover: mais escura que o default
- subtle: a cor misturada com ~92% de branco
- text: versão com contraste 4,5:1 sobre branco e sobre o subtle
- on-color: branco ou neutro escuro, o de maior contraste com o default
Escolha também a escala de neutros (fria, quente ou neutra),
garantindo neutral/500 com 4,5:1 sobre branco e sobre neutral/50.
Mostre uma tabela com os valores e o contraste de cada par.''')),
     ('Adaptar tipografia e fundamentos', _step('Configurar fonte, pesos, raio e layout.', 'Fonte da marca disponível no Figma do time.', 'Brand: <code>font/family/*</code> e <code>font/weight/*</code>. Shape: escolha o preset e apague os outros modes. Responsive: margens e altura do header.', 'Fonte instalada só num computador; nome do peso escrito errado; ajustar raio em cada componente.', 'Os text styles mostram a fonte nova; botões e campos têm o raio do preset.',
       'Configurar fonte e raio', '''Na cópia do kit [link]:
1. Confirme que a fonte "[Nome]" está disponível no Figma.
   Se não estiver, pare e me avise.
2. Atualize font/family/heading e font/family/body.
3. Atualize font/weight/* com os nomes exatos dos estilos da fonte.
4. Na collection Shape, mantenha só o mode "[preset]" e apague os outros.
Mostre um print de Button, Input e Product Card depois.''')),
     ('Atualizar variáveis e estilos', _step('Aplicar os valores na collection Brand.', 'Tabela da etapa 4 aprovada.', 'Local variables › Brand: edite os valores. Não renomeie nem apague variáveis.', 'Editar tokens da Color em vez da Brand; criar variáveis novas sem necessidade.', 'Nenhum nome mudou; só valores.',
       'Aplicar a paleta na Brand', '''Aplique na collection Brand da cópia [link] exatamente os valores
da tabela aprovada. Regras:
- Só altere valores. Não renomeie, não apague, não crie variáveis.
- Não altere feedback/* (sucesso, atenção, erro, informação)
  a menos que eu peça.
Ao final, liste cada variável alterada com valor antigo e novo.''')),
     ('Validar contraste e hierarquia', _step('Garantir legibilidade e que a ação principal se destaca.', 'Valores aplicados.', 'Confira os pares: primary/on-color × primary/default; primary/text × branco; neutral/500 × branco e × neutral/50; accent/on-color × accent/default.', 'Aceitar contraste baixo sem registrar a decisão.', 'Pares com 4,5:1 ou exceção documentada na página Começe por aqui.',
       'Checar contraste', '''Calcule o contraste dos pares abaixo na cópia [link] e marque
os que ficam abaixo de 4,5:1:
- primary/on-color sobre primary/default
- primary/text sobre branco e sobre primary/subtle
- neutral/500 sobre branco e sobre neutral/50
- accent/on-color sobre accent/default
Para cada falha, proponha uma correção que preserve a marca.''')),
     ('Verificar os componentes', _step('Confirmar que tudo continua funcionando com a nova marca.', 'Página Componentes da cópia.', 'Percorra Button, Tag, Price Block, Product Card, Input, Header e Footer.', 'Olhar só o botão primário.', 'Nenhum componente com cor sem token, texto ilegível ou hierarquia invertida.',
       'Revisar componentes depois da troca', '''Na página Componentes da cópia [link], tire prints de:
Actions/Button, Commerce/Tag, Commerce/Price Block,
Commerce/Product Card, Forms/Input, Header e Footer/Footer.
Aponte qualquer problema de contraste, cor fora de token
ou elemento que ficou com a cor errada para a função.''')),
     ('Identificar adaptações específicas', _step('Decidir os pontos de ajuste da marca.', 'Estratégia comercial do cliente.', 'Reaponte tokens semânticos só quando a estratégia pedir: <code>commerce/price → neutral/900</code>; <code>commerce/promo-* → feedback/success/*</code>; tokens <code>*/footer</code> para footer claro.', 'Criar componentes novos para resolver o que um token resolve.', 'Cada ajuste está registrado com o motivo.',
       'Avaliar pontos de ajuste', '''Considerando a marca e o site atual do cliente, avalie se o projeto
precisa destes ajustes e justifique cada um:
1. Preço em neutro em vez da cor da marca.
2. Promoções em verde ou vermelho.
3. CTA de compra na cor secundária.
4. Footer claro.
Não aplique nada; só recomende.''')),
     ('Validar antes de construir páginas', _step('Fechar a base antes de começar as telas.', 'Todas as etapas anteriores.', 'Atualize a página Começe por aqui da cópia: nome do projeto, versão, data e decisões.', 'Começar telas com a base pela metade e corrigir depois em todo lugar.', 'Checklist completo e decisões documentadas.',
       'Checklist final da base', '''Revise a cópia [link] e confirme item por item:
- Brand com as cores e fontes aprovadas
- Um único mode em Shape
- Layout ajustado (margens e altura do header)
- Logo, selos e formas de pagamento trocados
- Nenhuma cor sem variável nos componentes
- Contraste verificado e exceções registradas
Responda com OK ou PENDENTE para cada item.'''))]
    b += steps(items)
    b += h2('Quando a ferramenta não edita o Figma')
    b += p('Se a IA só analisa imagens ou gera código, use os mesmos prompts pedindo uma <strong>tabela de valores</strong> como resultado, e aplique você mesmo em Local variables. Para geração de código, peça que os tokens virem variáveis CSS com o mesmo nome (ex.: <code>--color-text-primary</code>).')
    return b

def padroes():
    b = p('Padrões são combinações de componentes que resolvem uma parte da loja. Esta página mostra o que já existe no kit para cada padrão e o que ainda falta.')
    rows = [
        ('Cabeçalho e navegação', 'Header (logo, slot de menu, Cart Button, Search Bar), Menu Item, Menu Shortcut, Menu Header, frames Menu e Submenu', badge('impl')),
        ('Busca', 'Search Bar (Default, Focused, Typing) + Search Panel (Suggestions, Results, No results) + Search Term', badge('impl')),
        ('Cards de produto', 'Product Card vertical (Default, Sale, Unavailable × CTA) e Product Card Horizontal (Minicart, Cart, Search)', badge('impl')),
        ('Listagens e grids', 'Product Card em grid; largura definida pelo grid. Regras de colunas por breakpoint', badge('pend')),
        ('Filtros e ordenação', 'Filter Item, Checkbox, Chip, Accordion; filtros Departamento/Simples/Preço e drawer Filtrar na página Layout Mobile', badge('impl') + ' ' + badge('pend', 'Mover para Componentes')),
        ('Página de produto (PDP)', 'Price Block LG, Quantity Selector, Button LG, Accordion para descrições', badge('pend', 'Sem padrão montado no kit')),
        ('Carrinho e minicart', 'Product Card Horizontal (Minicart, Cart), Quantity Selector, Grocery Button, Cart Button', badge('impl')),
        ('Formulários', 'Input, Select, Checkbox, Toggle', badge('impl') + ' ' + badge('pend', 'Sem Textarea e Radio')),
        ('Modais e drawers', 'Frames Drawer, Pop-up e Filtrar na página Layout Mobile, com overlay/scrim e elevation/3', badge('impl')),
        ('Mensagens de feedback', 'Toast (Success, Error, Warning, Info)', badge('impl')),
        ('Banners promocionais', 'Faixas de benefícios, brinde e frete grátis na página Layout Mobile', badge('pend', 'Sem documentação')),
        ('Checkout', 'Ainda não existe no kit', badge('prop', 'No backlog')),
        ('Estados vazios, carregamento e erro', 'Search Panel “No results”; Input Error. Skeleton e empty states gerais não existem', badge('prop', 'No backlog'))]
    b += table(['Padrão', 'Componentes envolvidos', 'Situação'], [[a, b2, s] for a, b2, s in rows])
    b += h2('Regras de composição')
    b += ul(['Reaproveite componentes antes de desenhar qualquer coisa. Se falta um detalhe, amplie o componente (nova variante ou propriedade) em vez de criar outro parecido.',
             'Telas: frame com auto layout vertical, largura ligada a <code>layout/viewport</code>, margem <code>layout/margin</code> e o mode Responsive do breakpoint aplicado ao frame.',
             'Seções separadas por <code>spacing/32</code>–<code>48</code> no mobile e <code>48</code>–<code>64</code> no desktop.',
             'Drawers e modais: <code>overlay/scrim</code> por trás, <code>elevation/3</code>, raio <code>radius/modal</code> (no bottom sheet, só nos cantos de cima).',
             'Componentes com interação de navegação (Header, menu, drawers) ficam na página de layout, não na página Componentes.'])
    b += h2('Montar uma tela a partir do wireframe')
    b += prompt('Montar a PLP mobile com componentes do kit', '''## Contexto
Arquivo: [link da cópia do kit]. Wireframe anexo.
Leia a skill do Norden UI KIT antes de começar.
## Tarefa
Monte a PLP mobile (393px) na página Layout Mobile, seguindo
a ordem do wireframe. Use só componentes existentes:
- Header (State=LoggedIn)
- Navigation/Breadcrumb
- Forms/Chip para ordenação (a opção ativa em Selected)
- Commerce/Product Card em grid de 2 colunas (largura pelo grid)
- Footer/Footer Device=Mobile
## Regras
- Configure tudo pelas propriedades; não destaque instâncias.
- Textos e preços do wireframe; não invente conteúdo.
- O que não tiver componente: monte com auto layout e tokens
  e liste no final como candidato a componente.
## Entrega
Print da tela e lista: elemento do wireframe → componente usado.''')
    b += h2('Mapa rápido: wireframe → componente')
    b += table(['No wireframe', 'Use'], [
        ['Tag com “%” ou “OFF”', 'Commerce/Tag Type=Discount'], ['Tag “Novo” ou “Lançamento”', 'Commerce/Tag Type=New'], ['Campanha (“Frete grátis”)', 'Commerce/Tag Type=Promo'], ['“Esgotado”', 'Tag Type=Dark + card State=Unavailable'],
        ['“De R$ X por R$ Y”', 'Price Block com Show old price'], ['“ou 3x de R$…”', 'Price Block, linha Installments'], ['Botão largo no card', 'Product Card CTA=Full'], ['Ícone de carrinho ao lado do preço', 'Product Card CTA=Compact'],
        ['“− 1 +”', 'Quantity Selector'], ['Item do minicart', 'Product Card Horizontal Context=Minicart'], ['Abas “A / B”', 'Navigation/Segmented Control'], ['FAQ, descrição expansível', 'Navigation/Accordion Item']])
    return b

def processo():
    b = p('O fluxo de trabalho de um projeto, do briefing ao handoff. Use esta página como checklist durante o projeto.')
    items = [
     ('Entender o projeto e a marca', p('Briefing, público, plataforma (VTEX/FastStore), manual de marca, site atual e wireframes. ') + p('<strong>IA:</strong> analisar o material e listar o que está faltando. <strong>Pronto quando:</strong> você sabe o que será desenhado e tem o material de marca.')),
     ('Preparar o arquivo', p('Duplicar o kit base, renomear, mover para o projeto do cliente. ') + p('<strong>Pronto quando:</strong> a cópia está no lugar certo e o arquivo base continua intocado.')),
     ('Adaptar o Style Guide', p('Seguir o tutorial <a href="#adaptar-marca">Adaptar para uma nova marca</a>. ') + p('<strong>IA:</strong> gerar a paleta, aplicar na Brand, configurar fonte e raio.')),
     ('Validar tokens e estilos', p('Contraste, text styles com a fonte nova, preset de raio. ') + p('<strong>Pronto quando:</strong> o checklist da etapa 10 do tutorial está completo.')),
     ('Adaptar componentes', p('Só o necessário: logo, assets, pontos de ajuste. Se o projeto exigir variações, amplie componentes existentes. ') + p('<strong>IA:</strong> criar variantes seguindo o padrão do kit e preencher a descrição de cada componente alterado.')),
     ('Construir páginas e fluxos', p('Uma seção por fluxo na página de layout, frames por breakpoint, componentes configurados por propriedades. ') + p('<strong>IA:</strong> montar telas a partir do wireframe, uma por vez.')),
     ('Validação visual e funcional', p('Prints, comparação com o wireframe, protótipo navegável quando houver interações.')),
     ('Acessibilidade e responsividade', p('Contraste, áreas de toque (mínimo 40–48px), texto de campos em 16px, versões mobile e desktop.')),
     ('Documentar decisões do projeto', p('Página Começe por aqui da cópia: versão, data, decisões de marca e exceções de contraste. Descrição preenchida em cada componente criado ou alterado.')),
     ('Preparar o handoff', p('Nomes de tokens e propriedades consistentes, componentes documentados, fluxos organizados por seção, pendências listadas.'))]
    b += steps(items)
    b += prompt('Revisão antes do handoff', '''Revise a cópia [link] para o handoff e responda em lista:
1. Frames de tela com cores ou textos fora de tokens/estilos.
2. Instâncias destacadas (detached) sem motivo.
3. Componentes criados ou alterados sem descrição.
4. Telas sem versão mobile ou desktop prevista.
5. Pendências que o desenvolvimento precisa saber.
Não corrija nada; só liste com o nome do frame.''')
    return b
