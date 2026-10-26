<!-- BEGIN:nextjs-agent-rules -->

## This is NOT the Next.js you know

This version has breaking changes — APIs, conventions, and file structure may all differ from your training data. Read the relevant guide in `node_modules/next/dist/docs/` (resolved from this file's directory; in monorepos the `next` package may not be visible from the repo root) before writing any code. Heed deprecation notices.

This block is written and re-added by `next dev` — verify at `node_modules/next/dist/server/lib/generate-agent-files.js`. Removing it from a diff only re-creates the uncommitted change; committing it with your work keeps the tree clean.

<!-- END:nextjs-agent-rules -->

# Site de documentação do Norden UI KIT

Plataforma de conhecimento para os designers da Norden/Wecode entenderem, adaptarem e expandirem o Norden UI KIT (design system base de e-commerce VTEX/FastStore no Figma, arquivo `UvGPurA87NxEPGeaAJ8bHH`) com ajuda de IA. Não é catálogo de componentes: ensina o que é, por que existe, como foi pensado, como usar no Figma e com IA, e como adaptar para outra marca.

## Antes de qualquer tarefa

1. `docs/brief.md`: briefing e critérios de sucesso.
2. `docs/arquitetura.md`: estrutura do código, modelo de páginas, build e publicação.
3. Conteúdo: `docs/conteudo.md` (como editar o MDX) e `docs/content-rules.md` (regras editoriais e fatos do kit).
4. Visual: `docs/site-design.md`.
5. Pendências: `docs/backlog.md`.

## Regras que não mudam

- **Veracidade:** todo dado sobre o kit (tokens, componentes, variantes, propriedades, descrições) vem do Figma. Não invente componentes, variantes, tokens, decisões ou capacidades de ferramentas de IA. O que não estiver confirmado leva o selo `<Badge kind="pend" />`.
- **Selos de status:** Implementado (existe no Figma), Recomendação (boa prática), Proposta (melhoria/backlog), Pendente de validação (time precisa confirmar). Diferencie sempre o que existe do que é proposta.
- **Modelo de conteúdo:** cada assunto responde o que é, por que existe, como foi pensado no kit, como usar no Figma e com IA, como adaptar. Prompts são específicos de cada contexto (nada de prompt genérico com nome trocado).
- **Idioma e tom:** português do Brasil, didático, para designers que podem não conhecer design systems nem IA. Frases diretas, sentence case, aspas tipográficas “ ” e apóstrofo ’ em todo texto lido, inclusive dentro dos prompts.
- **Visual:** dark mode como padrão (com alternância para claro), linguagem de ferramenta profissional (Vercel/shadcn): limpa, discreta, foco em leitura. Nada de landing page promocional ou grade de cards superficiais.
- **Documentação viva:** ao incluir componente, token ou regra, atualize também `content/docs/changelog.mdx` e a página Manutenção (a busca indexa sozinha). Mudanças importantes passam por pull request e revisão do time antes de publicar.
- **Regra do kit refletida no site:** todo componente precisa de descrição no campo Component information do Figma; o site mostra o selo “Sem descrição no Figma” quando falta.

## Verificar uma mudança

```bash
npm run lint
npm run build   # precisa gerar todas as páginas sem erro
npx serve out   # conferir no navegador, em dark e light, desktop e mobile (393px)
```
