from helpers import *

def inicio():
    b = p('O Norden UI KIT é a base de interface que o time usa para começar qualquer e-commerce. Ele reúne, num arquivo do Figma, os fundamentos visuais (cores, tipografia, espaçamento, raios, sombras), os tokens que guardam essas decisões e os componentes mais usados numa loja: botões, cards de produto, preço, carrinho, filtros, busca, header, footer e outros.')
    b += p('Esta documentação explica o que existe no kit, por que cada decisão foi tomada e como usar o kit com IA para adaptar a marca de um cliente e montar as telas do projeto sem perder consistência.')
    b += callout('info', 'Como ler esta documentação', ul([
        'Se você está começando, siga a ordem do menu lateral: Introdução, Como trabalhar com IA, Style Guide e Adaptar para uma nova marca.',
        'Se já conhece o kit, use a busca (tecla <kbd>/</kbd> ou <kbd>Ctrl</kbd> + <kbd>K</kbd>) para ir direto ao tópico.',
        'Os selos indicam a natureza de cada informação: ' + badge('impl') + ' existe no arquivo do Figma; ' + badge('rec') + ' é uma boa prática; ' + badge('prop') + ' é uma melhoria sugerida; ' + badge('pend') + ' precisa ser confirmada pelo time.']))
    b += h2('O que o kit resolve')
    b += p('Todo e-commerce precisa das mesmas peças: card de produto, preço com desconto, botão de compra, carrinho, busca, filtros. Sem uma base, cada projeto redesenha essas peças do zero, com pequenas diferenças que viram retrabalho, inconsistência e handoff demorado.')
    b += ul(['<strong>Retrabalho:</strong> o card de produto e o preço já existem com todas as variações (promoção, indisponível, minicart, carrinho, busca).',
             '<strong>Inconsistência:</strong> cores, espaçamentos e raios vêm de tokens, então o mesmo papel tem sempre o mesmo valor.',
             '<strong>Troca de marca demorada:</strong> a identidade do cliente entra editando valores, não redesenhando componentes.',
             '<strong>Handoff confuso:</strong> nomes de tokens e propriedades seguem um padrão que o desenvolvimento consegue mapear.'])
    b += h2('Papel do Figma e papel da IA')
    b += p('O Figma é a fonte de verdade: é lá que vivem as variáveis, os estilos e os componentes. A IA é uma assistente que lê essa fonte de verdade e executa tarefas repetitivas ou trabalhosas: aplicar a paleta de uma marca nos tokens, montar uma tela a partir de um wireframe, revisar se um arquivo usa tokens, documentar componentes.')
    b += callout('warn', 'O objetivo não é gerar telas aleatórias', p('A IA só produz resultado consistente quando trabalha <em>dentro</em> do sistema: usando os componentes, tokens e regras que já existem. Uma imagem de referência sozinha não basta. Por isso esta documentação insiste em fornecer contexto, conferir o resultado e corrigir sem refazer.'))
    b += h2('O que preservar e o que personalizar')
    b += table(['Preservar em todo projeto', 'Personalizar por marca'], [
        ['Nomes de tokens, collections e componentes', 'Valores da collection <strong>Brand</strong> (cores, fontes, pesos)'],
        ['Estrutura dos componentes: variantes, propriedades e instâncias expostas', 'Preset de raio (collection <strong>Shape</strong>)'],
        ['Relação entre tokens: componente → token semântico → valor da marca', 'Margens e altura do header (collection <strong>Responsive</strong>)'],
        ['Regras de acessibilidade: contraste AA, texto de campo em 16px, áreas de toque', 'Logo, selos, formas de pagamento e ilustrações'],
        ['Ícones da biblioteca Phosphor', 'Pontos de ajuste documentados (ex.: preço em neutro, footer claro)']])
    b += h2('Por onde começar')
    b += ol(['Leia <a href="#arquitetura">Arquitetura do kit</a> para entender as camadas.',
             'Leia <a href="#ia">Como trabalhar com IA</a> antes de pedir qualquer coisa para uma ferramenta.',
             'Percorra o <a href="#cores">Style Guide</a>: cores, tipografia, espaçamento e tokens.',
             'Siga o tutorial <a href="#adaptar-marca">Adaptar para uma nova marca</a> no seu primeiro projeto.',
             'Consulte os <a href="#componentes">Componentes</a> e os <a href="#padroes">Padrões</a> ao montar as telas.'])
    return b

def arquitetura():
    b = p('O kit é organizado em camadas. Cada camada só conversa com a vizinha, e é isso que permite trocar a marca sem tocar nos componentes.')
    b += '<div class="layers">' + ''.join(f'<div class="layer"><p class="layer-t">{t}</p><p>{d}</p></div>' for t, d in [
        ('Brand', 'Os valores da marca: cores (primary, secondary, accent, neutral, feedback) e fontes. É a única collection editada a cada projeto.'),
        ('Color, Shape, Dimension, Responsive', 'Tokens com função: “texto principal”, “fundo do botão primário”, “raio do card”, “margem da página”. Apontam para os valores da Brand ou de Primitives.'),
        ('Componentes', 'Usam somente os tokens com função. Nunca um hex, nunca um número solto.'),
        ('Telas e fluxos', 'Montadas com instâncias dos componentes, configuradas pelas propriedades.')]) + '</div>'
    b += h2('Collections do arquivo')
    b += table(['Collection', 'Modes', 'Para que serve'], [
        ['Brand', 'Norden Default', '46 variáveis de entrada da marca: cores e família/pesos de fonte. Sem escopo: não aparecem nos seletores, para ninguém aplicar direto.'],
        ['Primitives', 'Value', 'Valores crus que não mudam por marca: preto com transparência (sombras e scrim) e a escala de raios. Oculta da publicação.'],
        ['Color', 'Light', 'Tokens semânticos de cor, agrupados por função: text, icon, background, surface, border, commerce, overlay, shadow.'],
        ['Shape', '10px, None, 6px, 16px, 24px, Full', 'Raio por tipo de componente. Cada mode é um preset; o primeiro é o padrão do arquivo.'],
        ['Dimension', 'Value', 'Escala de espaçamento (grade de 4) e alturas de controles.'],
        ['Responsive', 'Mobile, Tablet, Desktop', 'Largura da tela, margem lateral, espaço do header e tamanhos de título que mudam por breakpoint.'],
        ['Prototype', 'Empty, With items', 'Variáveis do protótipo: quantidade do carrinho e se ele tem itens.']])
    b += h2('Páginas do arquivo')
    b += table(['Página', 'Conteúdo'], [
        ['Capa', 'Capa do arquivo.'],
        ['Começe por aqui', 'Introdução, versão (hoje v0.4 Beta) e changelog.'],
        ['Style guide', 'Foundations documentadas visualmente.'],
        ['Componentes', 'Biblioteca organizada em seções: Actions, Commerce, Forms, Brand, Navigation, Layout, Feedback.'],
        ['Layout Mobile e Layout Desktop', 'Telas e fluxos. Componentes com interações de navegação (Header, menu, drawers) ficam aqui.'],
        ['Layout Institucionais e E-mails transacionais', 'Páginas criadas, ainda sem conteúdo definido. ' + badge('pend')],
        ['Descartado', 'Referências antigas, mantidas só para consulta.']])
    b += h2('Convenções de nomenclatura')
    b += ul(['Componentes: <code>Categoria/Nome</code> em inglês (ex.: <code>Commerce/Product Card</code>). Peças internas começam com <code>_</code> (ex.: <code>_Product Card Media</code>).',
             'Variantes: <code>Propriedade=Valor</code> (ex.: <code>State=Sale, CTA=Full</code>).',
             'Tokens: função primeiro, depois detalhe (ex.: <code>background/button/primary/hover</code>, <code>text/secondary</code>).',
             'Text styles: <code>Grupo/Tamanho/Peso · tamanho/altura</code> (ex.: <code>Body/Medium/Regular · 16/24</code>).',
             'Textos de conteúdo nos componentes em português; nomes técnicos em inglês.'])
    b += h2('Mapa de um projeto novo')
    b += ol(['Duplicar o arquivo base e renomear para o cliente.', 'Aplicar a marca na collection Brand.', 'Escolher o preset de raio e ajustar o layout.', 'Trocar logo e assets.', 'Validar contraste e componentes.', 'Montar telas a partir do wireframe.', 'Validar, documentar decisões e preparar o handoff.'])
    b += p('O detalhe de cada etapa está em <a href="#processo">Processo de um novo projeto</a>.')
    return b

def ia():
    b = p('Ferramentas de IA conseguem ler arquivos do Figma, interpretar imagens e executar alterações. Mas elas não conhecem o kit: tudo o que sabem sobre ele vem do contexto que você fornece. Esta página ensina a dar esse contexto, pedir de forma verificável e conferir o resultado.')
    b += h2('Antes de pedir: o contexto mínimo')
    b += table(['Contexto', 'Por que importa', 'Como fornecer'], [
        ['Arquivo de trabalho', 'A IA precisa saber onde alterar e que é uma cópia do kit, não o original.', 'Link do Figma do projeto (cópia do kit) e, se possível, do frame exato.'],
        ['Regras do kit', 'Sem regras, ela cria cores soltas, componentes duplicados e nomes fora do padrão.', 'A <a href="#skill">skill geral</a> (ou a versão resumida colada no início do pedido).'],
        ['Referência visual', 'Mostra a intenção: o que existe na tela e em que ordem.', 'Wireframe, print ou link de referência.'],
        ['Conteúdo real', 'Evita textos e preços inventados.', 'Textos, produtos, preços e regras do cliente.'],
        ['Critério de pronto', 'Permite que a IA confira o próprio trabalho.', 'Lista do que precisa estar certo ao final.']])
    b += h2('Prompts ruins e bons')
    b += h3('Pedido vago')
    b += '<div class="cmp"><div class="cmp-bad"><p class="cmp-t">Ruim</p><pre>Faz uma página de produto bonita para a loja.</pre></div><div class="cmp-good"><p class="cmp-t">Melhor</p><pre>No arquivo [link], página Layout Mobile, crie a PDP mobile (393px)\nusando só componentes do kit: Header, Breadcrumb, galeria com\n_Product Card Media, Price Block Size=LG, Quantity Selector MD e\nButton Primary LG “Adicionar ao carrinho”. Textos do anexo.\nNão crie cores nem componentes novos; se faltar algo, me avise.</pre></div></div>'
    b += p('O pedido melhor diz onde, com o quê, com qual conteúdo e o que não fazer. A IA não precisa adivinhar.')
    b += h3('Referência sem regra')
    b += '<div class="cmp"><div class="cmp-bad"><p class="cmp-t">Ruim</p><pre>Copia esse card do print.</pre></div><div class="cmp-good"><p class="cmp-t">Melhor</p><pre>Use o Commerce/Product Card existente. No print, o card tem tag\nde desconto, preço riscado e botão largo: isso é State=Sale e\nCTA=Full. Configure pelas propriedades; não desmonte a instância\ne não copie as cores do print (vêm dos tokens).</pre></div></div>'
    b += h3('Correção que destrói o resto')
    b += '<div class="cmp"><div class="cmp-bad"><p class="cmp-t">Ruim</p><pre>O botão está errado, refaz.</pre></div><div class="cmp-good"><p class="cmp-t">Melhor</p><pre>No Actions/Button, a variante Secondary Hover está com borda\ncinza; deveria usar border/button/secondary/hover. Corrija só\nessa variante e me mostre um print antes e depois.</pre></div></div>'
    b += h2('Divida tarefas grandes')
    b += p('Peça uma etapa por vez e confira antes de seguir. Um fluxo seguro para quase tudo:')
    b += ol(['<strong>Diagnóstico:</strong> “Leia o arquivo e me diga o que existe e o que falta. Não altere nada.”',
             '<strong>Plano:</strong> “Liste o que vai criar, o que vai reaproveitar e as dúvidas.”',
             '<strong>Execução por partes:</strong> uma tela, um componente ou um grupo de tokens por vez.',
             '<strong>Validação:</strong> print do resultado e checklist.',
             '<strong>Ajustes pontuais:</strong> correções com escopo fechado.'])
    b += h2('Como conferir o resultado')
    b += ul(['Clique nas cores: precisam aparecer como variáveis, nunca como hex.',
             'Clique nos textos: precisam ter um text style aplicado.',
             'Verifique se as instâncias continuam ligadas ao componente (não destacadas).',
             'Compare com a referência: ordem dos elementos, textos e estados.',
             'Teste o protótipo quando houver interações.'])
    b += h2('Sinais de alucinação')
    b += p('A IA pode afirmar que fez algo que não fez, ou citar algo que não existe. Desconfie quando:')
    b += ul(['Ela menciona um componente, variante ou token que você não encontra no arquivo.',
             'O relatório diz “tudo certo”, mas não mostra print nem lista o que mudou.',
             'Aparecem nomes fora do padrão (ex.: <code>BotaoVermelho</code>, <code>color-1</code>).',
             'Valores numéricos “redondos” demais para cores que deveriam vir do manual da marca.'])
    b += p('Peça sempre: “mostre o print e liste exatamente o que mudou”. E confira por amostragem.')
    b += h2('Iterar sem recomeçar')
    b += p('Quando algo sai errado, descreva o erro, o lugar e o resultado esperado, e limite o escopo. Recomeçar do zero costuma desfazer o que já estava certo.')
    b += prompt('Pedir uma correção com escopo fechado', '''No frame [nome/link], o card do meio está com a tag “Novo”,
mas no wireframe é desconto de 15%.
Troque só a Tag desse card para Type=Discount e texto “-15%”.
Não altere os outros cards nem o layout.
Ao final, mostre um print do frame.''')
    b += h2('Fazer a IA consultar a documentação primeiro')
    b += prompt('Abrir qualquer tarefa com consulta obrigatória', '''Antes de executar, leia a skill do Norden UI KIT e inspecione o
arquivo [link]: collections de variáveis, text styles e componentes.
Depois me responda, sem alterar nada:
1. Quais componentes e tokens você vai usar.
2. O que precisaria ser criado (se algo).
3. Que dúvidas você tem.
Só execute depois que eu aprovar o plano.''')
    b += h2('Diferenças entre ferramentas')
    b += table(['Tipo de ferramenta', 'O que consegue', 'Como adaptar o pedido'], [
        ['IA com acesso de escrita ao Figma (ex.: via MCP)', 'Ler e alterar variáveis, componentes e frames.', 'Pedidos completos, com etapas e validação por print.'],
        ['IA que só lê o Figma ou imagens', 'Analisar, mapear e escrever instruções.', 'Peça a análise e a lista de passos; você executa no Figma.'],
        ['IA que gera código', 'Criar HTML/CSS ou componentes de front.', 'Forneça os tokens (nomes e valores) e peça que use os mesmos nomes como variáveis CSS.'],
        ['Agente de IA dentro do Figma', 'Criar e editar camadas no arquivo aberto.', 'Prompts autocontidos, com nomes de tokens e estilos escritos por extenso.']])
    b += callout('pending', 'Pendente de validação', p('A lista de ferramentas aprovadas pelo time e suas permissões (quem pode editar o arquivo base, quem só edita cópias) ainda não foi definida. ' + badge('pend')))
    return b
