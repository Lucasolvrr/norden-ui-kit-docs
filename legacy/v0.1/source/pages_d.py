from helpers import *
from comps import LEGACY

SKILL_FULL = '''## Papel
Você está trabalhando com o Norden UI KIT, o design system base de
e-commerce do time (VTEX/FastStore), no Figma. Seu trabalho é adaptar,
expandir e usar o kit sem quebrar sua arquitetura.

## Antes de qualquer alteração
1. Leia esta instrução inteira e a documentação do kit.
2. Inspecione o arquivo: collections de variáveis (Brand, Primitives,
   Color, Shape, Dimension, Responsive, Prototype), text styles,
   effect styles e componentes da página Componentes.
3. Confirme que o arquivo é uma cópia do kit para o projeto.
   O arquivo base nunca é editado por um projeto.
4. Apresente um plano: o que vai reaproveitar, o que vai criar,
   e as dúvidas. Espere aprovação quando houver decisão em aberto.

## Arquitetura (preserve)
- Brand guarda os valores da marca. Color, Shape, Dimension e
  Responsive guardam tokens com função. Componentes usam só tokens
  com função; nunca hex nem números soltos.
- Nomes: componentes Categoria/Nome em inglês; peças internas com _;
  variantes Propriedade=Valor; tokens funcao/detalhe;
  text styles Grupo/Tamanho/Peso · tamanho/altura.
- Ícones só da biblioteca Phosphor Icons (Outline, Regular; Fill no
  estado ativo), trocados por instance swap e pintados com icon/*.
- Auto layout em todos os níveis, com gaps e paddings em spacing/*.

## Reutilização
- Procure um componente existente antes de criar qualquer coisa.
- Se faltar um detalhe, amplie o componente existente (variante,
  boolean, text property, instance swap) em vez de duplicar.
- Configure instâncias pelas propriedades. Não destaque instâncias.

## Regras de design do kit
- Botões: Default, Hover (só desktop, tom mais escuro) e Disabled.
- Texto de campos de formulário sempre em 16px.
- Contraste AA (4,5:1) para texto; exceções precisam ser registradas.
- Conteúdo real: use textos, preços e regras fornecidos.
  Não invente dados comerciais.

## Documentação obrigatória
- Todo componente criado ou alterado precisa ter o campo
  Component information (descrição) preenchido: o que é e quando
  usar, o que cada variante muda, propriedades não óbvias,
  peças expostas, interações e regras.

## Honestidade
- Não invente componentes, variantes, tokens ou regras.
- Diferencie o que já existe do que você está propondo.
- Se faltar contexto essencial, pergunte antes de executar.

## Entrega
- Explique o que mudou, onde, e o impacto esperado.
- Mostre prints do resultado.
- Valide: nenhuma cor sem variável, todo texto com estilo,
  instâncias ligadas, descrição preenchida.
- Liste pendências e o que precisa de aprovação.'''

SKILL_SHORT = '''Use o Norden UI KIT como fonte de verdade.
Antes de alterar, inspecione o arquivo e me mostre um plano.
Só tokens (nada de hex), só text styles, ícones Phosphor,
auto layout com spacing/*. Reaproveite e amplie componentes
existentes; não duplique, não destaque instâncias.
Preencha a descrição de todo componente que criar ou alterar.
Não invente nada; pergunte quando faltar contexto.
No final: prints, lista do que mudou e pendências.'''

def skill():
    b = p('Uma instrução geral, reutilizável, que ensina qualquer IA a trabalhar dentro do kit. Cole no início de cada conversa (versão resumida) ou carregue como skill nas ferramentas compatíveis (versão completa).')
    b += h2('Versão completa')
    b += p('Para tarefas complexas: adaptar uma marca, criar componentes, montar fluxos. Cada bloco pode ser copiado separadamente.')
    b += prompt('Skill geral do Norden UI KIT (completa)', SKILL_FULL)
    b += h2('Versão resumida')
    b += p('Para o dia a dia: ajustes pontuais, dúvidas, revisões rápidas.')
    b += prompt('Skill geral do Norden UI KIT (resumida)', SKILL_SHORT)
    b += h2('Como usar em cada ferramenta')
    b += table(['Ferramenta', 'Como fornecer a skill'], [
        ['Claude (skills)', 'Existe a skill <code>norden-ui-kit</code> empacotada, com referências de tokens, componentes, mapeamento de wireframe e um script de paleta de cores. Instale pelo arquivo .skill. ' + badge('impl', 'Disponível')],
        ['Outras IAs de chat', 'Cole a versão completa como primeira mensagem ou nas instruções do projeto/espaço de trabalho.'],
        ['Agente de IA dentro do Figma', 'Cole a versão resumida e escreva nomes de tokens e estilos por extenso no pedido.'],
        ['IAs que geram código', 'Cole a versão completa e acrescente: “converta tokens em variáveis CSS com o mesmo nome”.']])
    b += callout('warn', 'Nem toda ferramenta lê arquivos ou acessa o Figma', p('Algumas só veem o que você cola na conversa. Nesses casos, inclua os nomes dos componentes e tokens relevantes no próprio pedido, ou anexe prints com as propriedades visíveis.'))
    b += h2('Manter a skill sincronizada')
    b += ol(['Toda versão nova do kit (ex.: v0.5) gera uma revisão da skill.', 'Componentes novos entram no inventário da skill e nesta documentação no mesmo dia.', 'Regras novas (como a documentação obrigatória) entram primeiro aqui, com o selo da versão, e depois na skill.', 'A skill empacotada é atualizada a partir do texto desta página.'])
    b += callout('pending', 'Planejado', p('Uma skill específica para gestão do UI KIT (para qualquer IA que assuma a manutenção do kit) está no backlog, com todos os guidelines detalhados. ' + badge('prop', 'Backlog C42')))
    return b

def manutencao():
    b = p('Esta documentação acompanha o kit. Esta página explica de onde vêm as informações, como atualizar e como revisar antes de publicar.')
    b += h2('Fontes de verdade')
    b += table(['Informação', 'Fonte', 'Como esta documentação obtém'], [
        ['Variáveis e valores', 'Arquivo Norden UI KIT no Figma (Local variables)', 'Exportação manual, feita por IA com acesso ao Figma.'],
        ['Componentes, variantes e propriedades', 'Página Componentes do arquivo', 'Exportação manual do inventário.'],
        ['Descrição de cada componente', 'Campo Component information', 'Copiada na exportação. É a fonte principal da seção “Visão geral” de cada componente.'],
        ['Versão e changelog', 'Página Começe por aqui', 'Copiada a cada versão.'],
        ['Decisões de design', 'Conversas e revisões do time', 'Registradas aqui com a data e o selo correspondente.']])
    b += p('Última exportação do Figma: <strong>26/10/2026</strong>. Não existe sincronização automática: os dados são atualizados pelo processo abaixo. ' + badge('impl'))
    b += h2('Processo de atualização')
    b += ol(['Uma mudança é feita no kit (componente novo, token, regra).', 'A descrição do componente é preenchida no Figma (regra obrigatória).', 'Uma IA com acesso ao Figma exporta variáveis e inventário e compara com a versão anterior.', 'As páginas afetadas são atualizadas e marcadas como “em revisão”.', 'Alguém do time revisa e aprova.', 'O changelog recebe a entrada com versão e data.'])
    b += prompt('Detectar mudanças no kit desde a última exportação', '''Exporte do arquivo Norden UI KIT [link]:
- todas as variáveis (nome, valor, alias, descrição)
- todos os componentes (nome, variantes, propriedades, descrição)
Compare com a exportação anterior (anexa) e liste:
1. O que foi adicionado.
2. O que foi removido ou renomeado.
3. Valores alterados.
4. Componentes sem descrição.
Não altere o Figma.''')
    b += h2('Selos de status')
    b += table(['Selo', 'Significado'], [[badge('impl'), 'Existe no arquivo do Figma e foi conferido na última exportação.'], [badge('rec'), 'Boa prática recomendada; não está imposta pelo arquivo.'], [badge('prop'), 'Melhoria sugerida ou no backlog; ainda não existe.'], [badge('pend'), 'Informação que o time precisa confirmar.']])
    b += h2('Pendências conhecidas')
    b += ul([
        'Componentes sem descrição no Figma: Google, Facebook, Navigation/Bottom Nav, Navigation/Bottom Nav Item e Footer/Link (backlog C43).',
        'Referências antigas ainda na página Componentes ou fora dela: ' + ', '.join(LEGACY) + '.',
        'Ausentes no kit: Radio, Textarea, padrão de PDP, checkout, estados vazios e de carregamento.',
        'Versões desktop dos componentes e telas; proposta de alternar mobile/desktop só redimensionando o frame (backlog C36).',
        '<code>layout/header-padding-top</code> provisório; grid de colunas e largura máxima no desktop não definidos.',
        'Política de foco por teclado nos botões (o estilo <code>focus-ring</code> existe, mas não é usado).',
        'Ferramentas de IA aprovadas e permissões de edição do arquivo base.'])
    return b

def changelog():
    b = p('Histórico das grandes atualizações do kit, copiado da página Começe por aqui, e da própria documentação.')
    rows = [
        ('Docs v0.1', '26/10/2026', 'Primeira versão desta plataforma: introdução, IA, Style Guide, tutorial de adaptação, componentes com dados reais do Figma, padrões, processo, skill e manutenção.'),
        ('Kit v0.4', '14/10/2026', 'Navegação, layout e feedback: Checkbox, Toggle, Chip, Segmented Control, Filter Item, Accordion, Breadcrumb, menu mobile, Bottom Nav, Header com nova busca, Footer com Newsletter, drawers e Toast.'),
        ('Kit v0.3', '14/10/2026', 'Nova linguagem visual (clean, inspirada no shadcn); botões só com Default, Hover e Disabled; Inputs e Select refeitos; raio padrão 10px; Grocery Button e Cart Button com variáveis de protótipo.'),
        ('Kit v0.2', '13/10/2026', 'Componentes de e-commerce: Button, Icon Button, Tag, Price Block, Quantity Selector, Product Card vertical e horizontal, Logo, Input e Select.'),
        ('Kit v0.1', '13/10/2026', 'Foundations: collections Brand, Color, Shape, Dimension e Responsive; presets de raio; tipografia, sombras e alturas de controle.')]
    b += '<div class="log">' + ''.join(f'<div class="log-row"><div><p class="log-v">{v}</p><p class="log-d">{d}</p></div><p>{t}</p></div>' for v, d, t in rows) + '</div>'
    b += h2('Regras incluídas depois da v0.4')
    b += ul(['Documentação obrigatória no campo Component information para todo componente. ' + badge('impl', 'Regra ativa')])
    return b
