# Norden UI KIT · Documentação

Documentação viva do **Norden UI KIT**, o design system base de e-commerce (VTEX/FastStore) do time de Design da Norden/Wecode no Figma. Não é um catálogo de componentes: o site explica o que é cada parte do kit, por que existe, como foi pensada, como usar no Figma e com IA, e como adaptar para a marca de um cliente.

**Site:** https://lucasolvrr.github.io/norden-ui-kit-docs/

## Stack

- [Next.js 16](https://nextjs.org) (App Router, export estático)
- [shadcn/ui](https://ui.shadcn.com) + [Tailwind CSS v4](https://tailwindcss.com)
- Conteúdo em [MDX](https://mdxjs.com); dados do Figma em JSON
- Publicação no GitHub Pages via GitHub Actions

## Rodar localmente

Requer Node.js 20 ou mais recente.

```bash
npm install
npm run dev     # http://localhost:3000
npm run build   # gera o site estático em out/
```

## Onde fica cada coisa

| O quê | Onde |
|---|---|
| Texto das páginas | `content/docs/*.mdx` |
| Documentação completa de componentes | `content/componentes/*.mdx` |
| Tokens e inventário exportados do Figma | `src/data/*.json` |
| Ordem e títulos das páginas | `src/lib/nav.ts` |
| Versão do kit e data exibidas | `src/lib/site.ts` |
| Componentes usados no MDX | `src/components/docs/` |

## Documentação do projeto

- [`docs/conteudo.md`](docs/conteudo.md): como editar o conteúdo e os componentes do MDX
- [`docs/content-rules.md`](docs/content-rules.md): regras editoriais e de veracidade
- [`docs/brief.md`](docs/brief.md): briefing e critérios de sucesso
- [`docs/arquitetura.md`](docs/arquitetura.md): estrutura do código, build e publicação
- [`docs/data-sync.md`](docs/data-sync.md): como atualizar os dados do Figma
- [`docs/site-design.md`](docs/site-design.md): tokens e componentes visuais do site
- [`docs/backlog.md`](docs/backlog.md): o que falta fazer

## Contribuir

1. Crie uma branch a partir da `main`.
2. Edite o conteúdo ou os dados seguindo `docs/content-rules.md`.
3. Rode `npm run build` para conferir.
4. Abra um pull request. Mudanças importantes passam pela revisão do time antes de publicar.

Ao fazer merge na `main`, o GitHub Actions publica o site.

## Histórico

A v0.1 era um HTML único gerado por Python. O código-fonte original e o script de migração para MDX ficam em `legacy/v0.1/`.
