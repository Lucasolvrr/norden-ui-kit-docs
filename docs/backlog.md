# Backlog do site

## Conteúdo
- Aprofundar os 36 componentes sem documentação completa (prioridade sugerida: Product Card Horizontal, Icon Button, Quantity Selector, Cart Button, Select, Chip, Filter Item, Search Bar/Panel, Accordion, Footer, Toast).
- Exemplos visuais dos componentes (imagens exportadas do Figma) e comparações original × adaptado.
- Padrões: uma página por padrão (hoje é uma tabela única), com prompts de páginas e fluxos.
- Tipografia e espaçamento: exemplo de adaptação de marca em cada tópico (pedido no briefing).
- Indicadores “atualizado / em revisão” por página (hoje só a data geral).
- Validação com um designer sem experiência em IA (etapa 5 do briefing).

## Plataforma
- ~~Decidir migração e hospedagem~~ Feito: Next.js + shadcn/ui + MDX, GitHub Pages (ver `docs/arquitetura.md`).
- ~~Links profundos para seções~~ Feito: títulos com âncora.
- ~~Fluxo de revisão antes de publicar~~ Possível via pull request; falta proteger a branch `main` e definir revisores.
- “Copiar página” inteira (como o “Copy Page” do shadcn).
- Imagens: `next/image` está sem otimização (export estático); usar imagens já otimizadas.
- Remover `scripts/fix-export-segments.mjs` quando o Next corrigir os nomes dos arquivos de prefetch no export estático.

## Pendências do kit refletidas no site
Grid e largura máxima no desktop; header-padding-top definitivo; política de foco por teclado; ferramentas de IA aprovadas e permissões; descrições ausentes no Figma (C43); limpeza de referências antigas (C39); componentes vindos do projeto Stok (C38).
