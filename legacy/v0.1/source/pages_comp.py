from helpers import *
from comps import COMPS
CATS = {'Actions': 'Ações', 'Commerce': 'Comércio', 'Brand': 'Marca', 'Forms': 'Formulários', 'Navigation': 'Navegação', 'Search': 'Busca', 'Layout': 'Layout', 'Feedback': 'Feedback'}
def cid(name): return 'c-' + slug(name)
TYPES = {'TEXT': 'Texto', 'BOOLEAN': 'Liga/desliga', 'INSTANCE_SWAP': 'Troca de instância'}
REL = {
 'Actions/Button': ['Actions/Icon Button', 'Commerce/Product Card', 'Marketing/Newsletter'],
 'Commerce/Tag': ['Commerce/Product Card', 'Commerce/Price Block'],
 'Commerce/Price Block': ['Commerce/Product Card', 'Commerce/Product Card Horizontal', 'Commerce/Tag'],
 'Commerce/Product Card': ['Commerce/Price Block', 'Commerce/Tag', 'Actions/Favorite Button', 'Actions/Button', 'Actions/Icon Button', 'Commerce/Grocery Button'],
 'Commerce/Product Card Horizontal': ['Commerce/Price Block', 'Commerce/Quantity Selector', 'Search/Search Panel'],
 'Commerce/Grocery Button': ['Commerce/Cart Button', 'Commerce/Quantity Selector', 'Commerce/Product Card'],
 'Commerce/Cart Button': ['Commerce/Grocery Button', 'Header'],
 'Forms/Input': ['Forms/Select', 'Search/Search Bar', 'Marketing/Newsletter'],
 'Header': ['Brand/Logo', 'Commerce/Cart Button', 'Search/Search Bar', 'Navigation/Menu Item'],
 'Search/Search Panel': ['Search/Search Bar', 'Search/Search Term', 'Commerce/Product Card Horizontal'],
 'Footer/Footer': ['Footer/Link Group', 'Marketing/Newsletter', 'Brand/Logo'],
 'Forms/Filter Item': ['Forms/Checkbox', 'Navigation/Accordion Item'],
 'Navigation/Menu Item': ['Navigation/Menu Header', 'Navigation/Menu Shortcut', 'Navigation/Accordion Item'],
}
DEEP = {
 'Actions/Button': dict(
  why='Toda tela de loja tem uma ação principal (comprar, adicionar, finalizar) e ações de apoio. O botão padroniza altura, área de toque, hierarquia visual e estados, para o cliente reconhecer a ação principal sem pensar.',
  decisions=['Três níveis de ênfase: Primary (fundo na cor da marca), Secondary (contorno), Tertiary (só texto).', 'Só três estados: Default, Hover (desktop, tom mais escuro) e Disabled. Sem Focus e Pressed, por decisão de projeto.', 'Alturas ligadas a <code>size/control/*</code>: SM 40, MD 48, LG 56.', 'Ícone e texto usam o mesmo token, para nunca ficarem com cores diferentes.'],
  anatomy=['Container: auto layout horizontal, altura <code>size/control/*</code>, raio <code>radius/button</code>.', 'Ícone à esquerda (opcional, Phosphor).', 'Label: estilo Button/Small, Medium ou Large.', 'Ícone à direita (opcional).'],
  tokens=['<code>background/button/primary/default</code> e <code>/hover</code>', '<code>text/button/primary · secondary · tertiary · disabled</code>', '<code>border/button/secondary/default</code> e <code>/hover</code>', '<code>background/button/tertiary/hover</code>', '<code>background/button/disabled</code>', '<code>radius/button</code>, <code>size/control/*</code>'],
  use=['Primary: uma ação principal por área (adicionar ao carrinho, finalizar compra).', 'Secondary: ações alternativas (ver mais, salvar na lista).', 'Tertiary: ações leves (cancelar, limpar, links de ação).', 'LG no CTA principal da PDP e do checkout.'],
  avoid=['Dois Primary lado a lado competindo pela atenção.', 'Botão só com ícone: use Actions/Icon Button.', 'Hover em telas mobile.'],
  errors=['Mudar a cor do botão por override em vez de reapontar o token.', 'Destacar a instância para trocar o texto (use a propriedade Label).', 'Usar SM em ações principais no mobile: a área de toque fica pequena.'],
  a11y=['Label com contraste AA sobre o fundo (<code>primary/on-color</code> × <code>primary/default</code>).', 'Área de toque mínima de 40px; padrão 48px.', 'Foco por teclado ainda não tem estado próprio. ' + badge('pend')],
  prompts=[('Criar uma variante destrutiva sem duplicar o botão', '''No Actions/Button do arquivo [link], adicione o valor Destructive
à propriedade Variant, com os estados Default, Hover e Disabled
nos tamanhos SM, MD e LG.
- Fundo: proponha tokens novos background/button/destructive/default
  e /hover apontando para feedback/error/default e um tom mais escuro.
- Texto e ícone: text/button/primary.
- Mantenha as propriedades Label e ícones ligadas como nas outras
  variantes. Não altere as variantes existentes.
- Atualize a descrição do componente.
Mostre o plano antes de executar.'''), ('Verificar o botão depois de trocar a marca', '''Na página Componentes da cópia [link], tire print das 27 variantes
do Actions/Button e confira:
- Primary: label com contraste 4,5:1 sobre o fundo.
- Hover mais escuro que o Default.
- Secondary com contorno visível sobre branco.
- Disabled perceptível, mas claramente inativo.
Liste problemas por variante, sem corrigir.''')],
  validate=['Todas as cores aparecem como variáveis.', 'Label editável pela propriedade.', 'Hover mais escuro que o Default.', 'Alturas 40/48/56.']),
 'Commerce/Tag': dict(
  why='Selos comunicam promoção, novidade e indisponibilidade antes do preço. Padronizar os tipos evita que cada projeto invente cores para a mesma mensagem.',
  decisions=['Cinco tipos fixos, cada um com função: Promo, Discount, New, Neutral, Dark.', 'Promo e Discount usam os tokens <code>commerce/*</code>, que apontam para a cor accent.', 'Dark é reservado para indisponível/esgotado.'],
  anatomy=['Container com raio <code>radius/tag</code> e padding pequeno (<code>spacing/2</code>–<code>8</code>).', 'Ícone opcional (Show icon + Icon).', 'Label.'],
  tokens=['<code>commerce/promo-background</code>, <code>commerce/promo-content</code>', '<code>commerce/discount</code>', '<code>radius/tag</code>'],
  use=['Discount: percentual (“-15%”).', 'Promo: campanha (“Frete grátis”, “Pontos em dobro”).', 'New: lançamento.', 'Neutral: informação (“Mais opções”).', 'Dark: indisponível.'],
  avoid=['Mais de duas tags no mesmo card.', 'Tag com frase longa: use texto de apoio no card.', 'Criar cor nova para uma campanha sem token.'],
  errors=['Pintar a tag por override para “combinar” com uma campanha.', 'Usar Discount para campanhas sem percentual.'],
  a11y=['Texto da tag com contraste AA sobre o fundo dela.', 'Não comunicar só por cor: o texto da tag precisa ser claro sozinho.'],
  prompts=[('Adicionar um tipo de tag para campanha da marca', '''O cliente tem uma campanha recorrente ("Mais por menos") com cor
própria (azul #1F31A1). No Commerce/Tag do arquivo [link]:
1. Proponha tokens novos para o fundo e o texto dessa tag
   (ex.: commerce/campaign-background e commerce/campaign-content),
   apontando para variáveis novas da Brand.
2. Adicione Type=Campaign nos tamanhos SM e MD, ligado a esses tokens.
3. Atualize a descrição do componente.
Não altere os tipos existentes. Mostre o plano antes.''')],
  validate=['Cada tipo usa tokens, nunca hex.', 'Label editável.', 'Contraste AA em todos os tipos.']),
 'Commerce/Price Block': dict(
  why='O preço é a informação mais lida de uma loja e tem muitas formas: preço atual, original riscado, desconto, Pix, parcelamento. Um bloco único garante a mesma ordem e hierarquia em card, PDP e carrinho.',
  decisions=['Linhas independentes que somem sem deixar espaço vazio.', 'Três tamanhos por contexto: LG (PDP), MD (card), SM (minicart, carrinho, busca).', 'Preço riscado sempre em <code>commerce/price-old</code> (neutral/500, com AA).'],
  anatomy=['Linha 1: preço original riscado + desconto (opcionais).', 'Linha 2: preço atual + sufixo (“à vista”).', 'Selo de Pix (Tag exposta).', 'Linha de parcelamento.'],
  tokens=['<code>commerce/price</code>, <code>commerce/price-old</code>, <code>commerce/discount</code>', 'Text styles Price/Large, Medium, Small e Old'],
  use=['Configure as linhas pelas propriedades conforme o produto.', 'A linha Installments também serve para preço por unidade ou faixa de quantidade.'],
  avoid=['Montar preço com textos soltos fora do componente.', 'Mostrar desconto sem preço original.'],
  errors=['Deixar a linha de parcelamento ligada com texto de exemplo.', 'Usar o tamanho LG dentro de cards.'],
  a11y=['Preço riscado com contraste AA (neutral/500).', 'Não depender só do riscado: o desconto deve estar escrito.'],
  prompts=[('Configurar o preço a partir do wireframe', '''No card do frame [link], o wireframe mostra
"De R$ 59,90 por R$ 47,92" e "ou 3x de R$ 15,97".
Configure o Price Block exposto do card:
- Show old price ligado, Old price "R$ 59,90"
- Price "R$ 47,92"
- Show installments ligado com o texto do parcelamento
- Show discount e Show Pix desligados
Não altere outros cards.''')],
  validate=['Linhas desligadas não deixam espaço.', 'Tamanho certo para o contexto.', 'Valores vindos do conteúdo real.']),
 'Commerce/Product Card': dict(
  why='É o componente mais repetido de uma loja e o que mais gerava retrabalho entre projetos. Reúne imagem, selos, favoritar, nome, preço e ação de compra com todas as variações comuns.',
  decisions=['Estados de negócio, não visuais: Default, Sale, Unavailable.', 'Três formatos de CTA: Full, Compact e None.', 'Peças internas expostas: tudo se configura pelo painel, sem desmontar o card.', 'Nome com no máximo 2 linhas e reticências; imagem com proporção travada.'],
  anatomy=['Mídia (_Product Card Media): imagem, tag e favoritar.', 'Marca (opcional) e nome.', 'Price Block MD.', 'CTA: Button (Full) ou Icon Button (Compact).', 'Chip “Mais opções” (Show options).'],
  tokens=['<code>surface/default</code>, <code>surface/media</code>, <code>border/default</code>', '<code>radius/card</code>, <code>radius/media</code>', 'Tokens do Price Block, Tag e Button'],
  use=['Vitrines, PLP e busca em grade.', 'Sale quando há preço original e desconto.', 'Unavailable para produto sem estoque.'],
  avoid=['Cards de tamanhos diferentes na mesma grade.', 'Trocar a imagem destacando a instância (troque o fill da camada Image).'],
  errors=['Esticar o card sem respeitar a proporção da imagem.', 'Ligar Sale sem preencher o preço original.'],
  a11y=['Área de toque do CTA com pelo menos 40px.', 'Indisponibilidade comunicada por texto, não só pela imagem esmaecida.'],
  prompts=[('Montar uma vitrine de 4 produtos', '''No frame [link], monte uma vitrine horizontal com 4 instâncias de
Commerce/Product Card (State=Default, CTA=Full), gap spacing/16.
Use os produtos do anexo: nome, preço e imagem.
O segundo produto está em promoção: State=Sale com preço original
e tag de desconto do anexo.
Configure tudo pelas propriedades e instâncias expostas.'''), ('Criar um estado novo sem duplicar o card', '''Preciso de um estado "Pré-venda" no Commerce/Product Card do arquivo [link].
Antes de criar, avalie se dá para resolver com o que existe
(Tag Type=New ou Promo + texto do botão).
Só se não der, proponha o valor novo em State, com as mesmas
peças expostas das outras variantes. Mostre o plano antes.''')],
  validate=['Todas as variantes com as mesmas peças expostas.', 'Nome trunca em 2 linhas.', 'Imagem mantém proporção.']),
 'Commerce/Grocery Button': dict(
  why='Em supermercados e atacarejos o cliente compra várias unidades e ajusta a quantidade direto no card. O botão vira seletor de quantidade sem levar a outra tela.',
  decisions=['Três estados de quantidade: 0 (Adicionar), 1 (lixeira, 1, +) e 2+ (−, n, +).', 'O número vem de variáveis de protótipo (<code>cart/quantity-label</code>), para o protótipo funcionar de verdade.', 'O Cart Button do header acompanha a quantidade.'],
  anatomy=['Estado 0: botão com ícone e “Adicionar”.', 'Estados 1 e 2+: ação de remover/diminuir, número e “+”.'],
  tokens=['<code>background/button/primary/*</code>, <code>text/button/primary</code>', 'Collection Prototype: <code>cart/quantity</code>, <code>cart/quantity-label</code>, <code>cart/has-items</code>'],
  use=['Cards de supermercado, atacarejo e farmácia.', 'Telas estáticas com quantidade: aplique o mode “With items” da collection Prototype no frame.'],
  avoid=['Usar em produtos de compra unitária (moda, eletrônicos).'],
  errors=['Duplicar variantes e esquecer de refazer as interações: as setas passam a apontar para variantes erradas.', 'Nomes de variante repetidos no set (o Figma marca erro e as trocas falham).'],
  a11y=['Botões de + e − com área de toque de pelo menos 32px.', 'Número legível com contraste AA.'],
  prompts=[('Adicionar um tamanho sem quebrar as interações', '''No Commerce/Grocery Button do arquivo [link], crie Size=LG
(altura size/control/lg) para Quantity 0, 1 e 2+.
Depois de criar, refaça as interações do grupo LG copiando as do
grupo MD: Adicionar → 1; lixeira → 0; + no 1 → 2+; + no 2+ soma 1;
− no 2+ volta para 1 se a quantidade for 2.
Confirme que nenhum nome de variante ficou repetido e
liste para onde cada interação aponta.''')],
  validate=['Nenhum nome de variante repetido.', 'Cada interação aponta para a variante do mesmo tamanho.', 'O badge do Cart Button acompanha no protótipo.']),
 'Forms/Input': dict(
  why='Campos aparecem em busca, login, cadastro, CEP e checkout. Padronizar estados e tamanhos reduz erros de preenchimento e abandono.',
  decisions=['Texto sempre em 16px (evita zoom automático no iOS).', 'Ícone à esquerda para busca; à direita para senha (olho).', 'Error troca o texto de apoio pela mensagem de erro.', 'Hover só no desktop.'],
  anatomy=['Label (opcional).', 'Campo: ícones opcionais, texto, ícone de status em Success/Error.', 'Texto de apoio ou mensagem de erro.'],
  tokens=['<code>border/default</code>, <code>border/hover</code>, <code>border/focus</code>, <code>border/error</code>, <code>border/success</code>', '<code>text/placeholder</code>, <code>text/error</code>', '<code>radius/input</code>, <code>size/control/md</code>'],
  use=['Formulários, CEP, cupom, newsletter.', 'Mensagens de erro específicas (“CEP inválido”), nunca genéricas.'],
  avoid=['Placeholder no lugar da label em formulários longos.', 'Texto menor que 16px.'],
  errors=['Mudar o tamanho da fonte do campo por override.', 'Usar Error sem preencher a mensagem.'],
  a11y=['Label visível ou associada.', 'Erro comunicado por texto e ícone, não só pela cor da borda.'],
  prompts=[('Montar o formulário de endereço', '''No frame [link], monte o formulário de endereço do checkout com
Forms/Input (Show label ligado): CEP, Rua, Número, Complemento,
Bairro, Cidade e Estado (Forms/Select). Gap spacing/16.
Mostre o CEP no estado Error com a mensagem "CEP não encontrado".
Não crie campos novos; use só Input e Select.''')],
  validate=['Texto em 16px.', 'Estados com tokens de borda corretos.', 'Mensagens de erro específicas.']),
 'Header': dict(
  why='O header concentra os caminhos mais usados: menu, busca, conta e carrinho. Ele precisa ser consistente em todas as telas e funcionar no protótipo.',
  decisions=['Logo é instância de Brand/Logo: troca de marca em um só lugar.', 'Menu é um slot (instance swap) à esquerda.', 'Carrinho é o Commerce/Cart Button, com badge ligado às variáveis do protótipo.', 'Fica na página Layout Mobile porque abre o menu como overlay.'],
  anatomy=['Barra de status (iOS).', 'Barra principal: slot de menu, logo, ícones de ação e Cart Button.', 'Search Bar (Show Searchbar).'],
  tokens=['<code>surface/default</code>, <code>border/default</code>', 'Tokens do Cart Button e do Search Bar'],
  use=['Em todas as telas da loja; State2 no checkout (sem distrações).'],
  avoid=['Recriar o header por tela: use a instância e as propriedades.'],
  errors=['Perder o link do overlay do menu ao duplicar telas.', 'Esquecer de ajustar <code>layout/header-padding-top</code> quando o header muda de altura.'],
  a11y=['Ícones com área de toque de pelo menos 40px.', 'Badge do carrinho com contraste AA.'],
  prompts=[('Adaptar o header para um projeto', '''No Header da cópia [link]:
1. Confirme que o logo é instância de Brand/Logo (não imagem solta).
2. Mantenha o slot de menu e o Cart Button.
3. Meça a altura final do header em cada estado e atualize
   layout/header-padding-top na collection Responsive.
Liste o que mudou.''')],
  validate=['Logo trocado pelo Brand/Logo.', 'Menu abre o overlay.', 'Badge acompanha o protótipo.']),
}

def _props(props):
    var, other = [], []
    for part in [x for x in props.split('; ') if x]:
        if '=[' in part:
            k, v = part.split('=[', 1); var.append([f'<code>{k}</code>', ', '.join(f'<code>{o}</code>' for o in v.rstrip(']').split('|'))])
        elif ':' in part:
            k, t = part.rsplit(':', 1); other.append([f'<code>{k}</code>', TYPES.get(t, t)])
    return var, other

def comp_page(name, cat, n, props, desc):
    d = DEEP.get(name)
    b = '<div class="meta-row">' + badge('impl') + (badge('impl', 'Descrição no Figma') if desc else badge('pend', 'Sem descrição no Figma')) + (badge('rec', 'Documentação completa') if d else badge('prop', 'Aprofundamento pendente')) + f'<span class="meta-n">{n} variante{"s" if n != 1 else ""}</span></div>'
    b += h2('Visão geral', 'visao-geral')
    b += p(esc_keep(desc) if desc else 'Este componente ainda não tem descrição no campo Component information do Figma. Pela regra do kit, ela é obrigatória. ' + badge('pend'))
    var, other = _props(props)
    b += h2('Variantes e propriedades', 'variantes')
    if var: b += table(['Propriedade de variante', 'Valores'], var)
    if other: b += table(['Propriedade', 'Tipo'], other)
    if not var and not other: b += p('Sem propriedades configuráveis: edite o componente principal.')
    if d:
        b += h2('Por que existe', 'por-que') + p(d['why'])
        b += h2('Decisões a preservar', 'decisoes') + ul(d['decisions'])
        b += h2('Anatomia', 'anatomia') + ol(d['anatomy'])
        b += h2('Tokens e estilos', 'tokens-comp') + ul(d['tokens'])
        b += h2('Quando usar', 'quando-usar') + ul(d['use']) + h3('Quando evitar', 'quando-evitar') + ul(d['avoid'])
        b += h2('Acessibilidade', 'acessibilidade') + ul(d['a11y'])
        b += h2('Erros comuns', 'erros') + ul(d['errors'])
        b += h2('Com IA', 'com-ia')
        for t, txt in d['prompts']: b += prompt(t, txt)
        b += h2('Como validar', 'validar') + ul(d['validate'])
    else:
        b += callout('pending', 'Aprofundamento pendente', p('Fundamentação, anatomia, erros comuns e prompts específicos deste componente ainda serão escritos. Até lá, use a visão geral acima, as propriedades e a <a href="#skill">skill geral</a>.'))
    rel = REL.get(name)
    if rel:
        b += h2('Relacionados', 'relacionados') + ul([f'<a href="#{cid(r)}">{r}</a>' for r in rel])
    b += h2('Atualizações', 'atualizacoes') + p('Dados exportados do Figma em 26/10/2026 (kit v0.4).')
    return b

def esc_keep(s): return s

def index_page():
    b = p(f'Inventário real do arquivo: {len(COMPS)} componentes publicáveis na versão atual, agrupados por categoria. Peças internas (nomes com _) aparecem dentro das páginas dos componentes que as usam.')
    b += callout('info', 'Legenda', p(badge('rec', 'Documentação completa') + ' fundamentação, anatomia, prompts e validação. ' + badge('prop', 'Aprofundamento pendente') + ' só dados do Figma por enquanto. ' + badge('pend', 'Sem descrição no Figma') + ' descrição obrigatória ainda não preenchida.'))
    groups = {}
    for name, cat, n, props, desc in COMPS: groups.setdefault(cat, []).append((name, n, desc))
    for cat, items in groups.items():
        b += h3(CATS.get(cat, cat), 'cat-' + slug(cat))
        b += table(['Componente', 'Variantes', 'Situação'], [[f'<a href="#{cid(nm)}">{nm}</a>', str(n), (badge('rec', 'Completa') if nm in DEEP else badge('prop', 'Pendente')) + ('' if desc else ' ' + badge('pend', 'Sem descrição'))] for nm, n, desc in items])
    return b
