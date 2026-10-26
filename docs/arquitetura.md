# Arquitetura do site

O site é gerado com **Next.js 16 (App Router)** em modo de export estático (`output: "export"`). O build produz HTML puro em `out/`, que pode ser hospedado em qualquer servidor estático: GitHub Pages (padrão deste repositório), Vercel, Netlify ou o servidor da empresa.

| Camada | Escolha | Por quê |
|---|---|---|
| Framework | Next.js 16 + React 19 | Stack mais difundida do ecossistema React; export estático sem servidor. |
| Componentes de interface | shadcn/ui (Radix) + Tailwind CSS v4 | Componentes acessíveis (diálogo de busca, gaveta mobile, menus recolhíveis, toast) copiados para o repositório e editáveis. |
| Conteúdo | MDX em `content/` | Texto em Markdown com componentes (`<Prompt>`, `<Callout>`…); revisão por pull request. |
| Dados do Figma | JSON em `src/data/` | Tokens e inventário de componentes separados do texto, atualizados pelo processo de `data-sync.md`. |
| Hospedagem | GitHub Pages via GitHub Actions | Gratuito para repositório público; cada push na `main` publica. |

## Estrutura

```
content/
  docs/<slug>.mdx            páginas de conteúdo (inicio, cores, adaptar-marca, skill…)
  componentes/<slug>.mdx     documentação completa de um componente (opcional)
src/
  app/                       rotas: /, /[slug], /componentes, /componentes/[slug], /search-index.json
  components/docs/           componentes usados no MDX (Prompt, Callout, Steps, BrandSimulator…)
  components/layout/         header, navegação lateral, busca, "Nesta página", artigo
  components/ui/             componentes do shadcn/ui (gerados pelo CLI)
  data/                      tokens.json, components.json, component-relations.json, spacing.json
  lib/nav.ts                 lista PAGES: ordem, grupos, títulos e leads de todas as páginas
  lib/site.ts                versão do kit e data de atualização exibidas no cabeçalho
  mdx-components.tsx         registra os componentes disponíveis no MDX
scripts/fix-export-segments.mjs   contorno de um bug do export estático do Next 16.4 (roda no postbuild)
legacy/v0.1/                 código-fonte e HTML da v0.1 (gerador Python) e o script de migração
```

## Modelo de páginas

- `src/lib/nav.ts` → `PAGES`: cada entrada tem grupo, slug, título, lead e rota. A ordem define a navegação lateral e os links anterior/próxima. Grupos `Componentes · <Categoria>` viram submenus recolhíveis.
- Páginas `kind: "doc"` leem `content/docs/<slug>.mdx`. A home (`/`) é o `inicio.mdx`.
- Páginas de componente são geradas a partir de `src/data/components.json`: selos, visão geral (descrição do Figma), tabelas de propriedades, relacionados e data da exportação. Se existir `content/componentes/<slug>.mdx`, ele entra como documentação completa e o selo muda para “Documentação completa”; senão aparece o aviso “Aprofundamento pendente”.
- O slug do componente é o nome sem acentos, em minúsculas e com hífens: `Commerce/Product Card` → `commerce-product-card`.
- Cabeçalho de toda página: grupo, H1, lead e “Kit v0.4 Beta · Atualizado em DD/MM/AAAA” (`src/lib/site.ts`; atualizar a cada versão).

## Comportamentos

- **Busca** (`/` ou Ctrl/Cmd+K): índice gerado no build em `/search-index.json` a partir do MDX e dos dados (tokens, componentes). Ignora acentos, exige todos os termos, título pesa mais, trecho com destaque, setas e Enter.
- **Nesta página**: gerado dos h2/h3 do conteúdo, com destaque da seção visível. Os títulos têm âncora (`/cores/#estados-de-interação`), então dá para compartilhar o link de uma seção.
- **Cópia**: “Copiar prompt”, “Copiar bloco” e clique no nome de um token, com toast de confirmação.
- **Tema**: escuro por padrão, alternância para claro, preferência salva no navegador (`next-themes`, chave `nd-theme`).
- **Simulador de marca** (`<BrandSimulator />`, página Cores): mesma lógica do `brand_palette.py` da skill norden-ui-kit (hover = mistura com preto 14% ou 45% em cores muito escuras; subtle = 92% branco; text escurece em passos de 2,5% até 4,5:1 sobre branco e sobre o subtle; on-color = branco ou #1C1C21, o de maior contraste).
- **Responsivo**: até 1240px some o índice da direita; até 900px a navegação vira gaveta (botão de menu).

## Build e publicação

```bash
npm install
npm run dev          # http://localhost:3000
npm run build        # gera out/ (e roda scripts/fix-export-segments.mjs)
npx serve out        # confere o resultado estático
```

O workflow `.github/workflows/deploy.yml` builda com `NEXT_PUBLIC_BASE_PATH=/<nome-do-repo>` e publica `out/` no GitHub Pages. Para hospedar na raiz de um domínio (Vercel, domínio próprio), deixe `NEXT_PUBLIC_BASE_PATH` vazio.

## Migração da v0.1

A v0.1 era um gerador Python que produzia um único HTML (`legacy/v0.1/`). O conteúdo foi convertido para MDX por `legacy/v0.1/migracao/convert.py`, e `verify.py` confirmou que o texto das 57 páginas é idêntico ao da v0.1 (a única diferença é o simulador, que agora já vem renderizado com os valores calculados). Correção feita na migração: o lead de componentes cuja descrição tem uma frase só terminava com “..” (ex.: CarouselControls).
