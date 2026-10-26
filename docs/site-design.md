# Design do próprio site

Direção: documentação de ferramenta profissional (Vercel, shadcn), dark mode padrão, foco em leitura e consulta recorrente. Um único elemento interativo de destaque: o simulador de cor da marca na página Cores.

## Tokens (`src/app/globals.css`)

As variáveis do shadcn/ui foram mapeadas para a paleta da v0.1. Escuro (classe `.dark`, padrão) e claro (`:root`):

| Papel | Escuro | Claro | Variável |
|---|---|---|---|
| Fundo | #0a0a0a | #ffffff | `--background` |
| Fundo 2 (cards, cabeçalhos de tabela) | #111111 | #fafafa | `--card` |
| Painel (código, item ativo) | #161616 | #f4f4f5 | `--muted` |
| Linha | #262626 | #e4e4e7 | `--border` |
| Linha suave | #1c1c1c | #efefef | `--line-2` |
| Texto | #ededed | #18181b | `--foreground` |
| Texto 2 | #a1a1a1 | #52525b | `--muted-foreground` |
| Texto 3 | #737373 | #71717a | `--subtle` |
| Destaque | #fafafa | #09090b | `--strong` |
| Hover | #1a1a1a | #f4f4f5 | `--accent` |

Status (cada um com `-bg` translúcido): verde `--st-impl` (Implementado), azul `--st-rec` (Recomendação), violeta `--st-prop` (Proposta), âmbar `--st-pend` (Pendente), vermelho `--st-bad` (exemplos ruins). Em Tailwind: `text-st-impl`, `bg-st-impl-bg` etc.

## Tipografia

Rethink Sans (mesma fonte do kit) para tudo; Geist Mono para código, tokens, prompts e metadados (`next/font/google`). Corpo 15/1.65; H1 36 (30 no mobile) semibold, tracking −0.025em; H2 22; H3 17. Linhas de texto até 72ch.

## Layout

Header fixo de 56px (marca, busca, versão, tema). Grade: navegação 264px | conteúdo (máx. 760px) | “Nesta página” 224px. Até 1240px some o índice; até 900px a navegação vira gaveta (`Sheet` do shadcn). Respeita `prefers-reduced-motion`.

## Componentes

- Do shadcn/ui (`src/components/ui`): `Command` + `Dialog` (busca), `Sheet` (navegação mobile), `Collapsible` (submenus de componentes), `Sonner` (toast).
- Do site (`src/components/docs`): ver `docs/conteudo.md`.
- Estilos do texto do MDX: classe `.docs-prose` em `globals.css`; tabelas em `.docs-table` (rolagem horizontal própria).
