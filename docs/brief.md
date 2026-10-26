# Briefing (resumo fiel do documento do usuário)

## Objetivo
Site de documentação para o UI Kit de e-commerce do time de Design. Fonte central de conhecimento para criar novos e-commerces: explicar **como o kit funciona, por que cada decisão foi tomada, como usar e como reproduzir, adaptar e expandir com IA**. Documentação viva, que evolui com o kit. Resultado: qualquer designer entende o kit, adapta à marca do cliente no Figma e usa IA para conduzir o projeto com consistência.

## Público
Designers de produto e UI/UX de e-commerce. Não presumir que conhecem design systems, prompts, variáveis/estilos/variantes/auto layout, como dar contexto à IA ou como adaptar sem quebrar a arquitetura. Explicar o conceito antes de exigir a aplicação.

Cinco perguntas por assunto: 1) O que é? 2) Por que existe? 3) Como foi pensado no kit? 4) Como usar no Figma e com IA? 5) Como adaptar para outro projeto?

## Estrutura pedida
1. **Introdução ao UI Kit**: finalidade, problemas que resolve, papel do Figma e da IA, o que preservar × personalizar, arquitetura e mapa de etapas.
2. **Como trabalhar com IA**: contexto, referências, instruções verificáveis, dividir tarefas, alterar sem quebrar, avaliar, alucinações, iterar, consistência; prompts ruins × bons; fazer a IA consultar a documentação antes.
3. **Style Guide** (uma das mais importantes): cores (marca × semânticas, feedback, estados, finalidade, contexto, acessibilidade, erros), tipografia (hierarquia no e-commerce), espaçamento/grid/dimensões/raios/bordas/sombras/responsividade, variáveis e tokens (primitivos, semânticos, de componente, de ambiente). Exemplo de adaptação para nova marca em cada tópico.
4. **Adaptar para nova marca**: 10 etapas (analisar material → validar antes das páginas), cada uma com objetivo, contexto, instruções no Figma, erros comuns, critérios de validação e prompt pronto. Prompts preservam nomenclatura, não trocam tudo pela cor primária, preservam feedback, consideram contraste, apontam informação ausente. Adaptar para ferramentas que não editam o Figma.
5. **Componentes**: baseados no inventário real. Por componente: identificação, fundamentação, especificação (anatomia, variantes, propriedades, estados, comportamento, responsividade, acessibilidade, tokens), utilização (quando usar/evitar, erros, combinações), implementação com IA e pelo menos um prompt (criar variante, adaptar marca, versão responsiva, corrigir, expandir sem duplicar).
6. **Padrões de interface**: header, busca, menus, cards, listagens, filtros, PDP, carrinho/minicart, formulários, modais/drawers, feedback, banners, checkout, estados vazios/carregamento/erro; regras de composição e prompts de páginas/fluxos.
7. **Processo de novo projeto**: 10 etapas do entendimento ao handoff, com papel da IA e critérios.
8. **Skill geral para IA**: versão completa e resumida, adaptação por ferramenta, como fornecer contexto, como manter sincronizada.

## Padrão de cada página (quando aplicável)
Visão geral, Objetivo, Fundamentação, Funcionamento, Aplicação no e-commerce, Implementação no Figma, Uso com IA, Prompt de exemplo, Validação, Erros comuns, Relacionamentos, Atualizações.

## Manutenção
Fácil incluir componentes, atualizar tokens, revisar, registrar decisões, histórico, identificar conteúdo desatualizado, incluir novas ferramentas. Ligar cada informação à fonte (Figma, inventário). **Não inventar sincronização automática** inexistente; propor processo viável. Preparar para automações futuras (IA detectar mudanças e sugerir atualizações). Revisão do time antes de publicar mudanças importantes.

## Interface
Consulta recorrente: navegação lateral, busca global, hierarquia clara, índice contextual, blocos de código/prompt, copiar prompts (inteiro ou partes), exemplos visuais, original × adaptado, links entre conteúdos, indicadores de atualizado/em revisão, versão e data, responsivo, boa leitura longa. Visual de ferramenta profissional. Referências: documentação da Vercel e do shadcn-svelte, **dark mode**.

## Estratégia de implementação
1 Diagnóstico → 2 Arquitetura da informação → 3 Protótipo da plataforma → 4 Conteúdo inicial (introdução, Style Guide, tutorial de marca, skill geral, componentes mais importantes, ampliação progressiva) → 5 Validação (designer sem experiência consegue seguir? prompts têm contexto?) → 6 Manutenção. A v0.1 cobre as etapas 1 a 4 (conteúdo inicial).

## Critérios de sucesso
Designer entende o kit sem explicação individual; time entende o porquê de cada fundamento; adaptação de marca guiada; IA usada sem perder consistência; cada tópico com exemplos e prompts; ensina a validar; conteúdo fiel ao kit real; novos componentes sem reconstruir a plataforma; evolui com o kit; referência durante todo o projeto.
