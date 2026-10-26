# Como editar o conteúdo

Todo o texto do site fica em arquivos `.mdx` dentro de `content/`. MDX é Markdown com componentes: títulos com `##`, listas com `-`, **negrito**, `código`, links `[texto](/cores)` e, quando precisa, componentes como `<Prompt>` e `<Callout>`.

Antes de escrever, leia `docs/content-rules.md` (regras editoriais e de veracidade) e `docs/brief.md` (o briefing).

## Tarefas comuns

| Tarefa | Onde |
|---|---|
| Corrigir ou ampliar o texto de uma página | `content/docs/<slug>.mdx` |
| Escrever a documentação completa de um componente | criar `content/componentes/<slug>.mdx` (modelo abaixo) |
| Adicionar uma página nova | criar `content/docs/<slug>.mdx` e incluir a entrada em `PAGES` (`src/lib/nav.ts`) |
| Atualizar tokens ou inventário do Figma | `docs/data-sync.md` |
| Relacionar componentes | `src/data/component-relations.json` |
| Mudar versão do kit / data exibida | `src/lib/site.ts` |
| Registrar a mudança | `content/docs/changelog.mdx` e, se for pendência, `content/docs/manutencao.mdx` |

A busca indexa tudo sozinha no build.

## Componentes disponíveis no MDX

Registrados em `src/mdx-components.tsx`.

**Selos de status**: diferencie sempre o que existe do que é proposta.
```mdx
<Badge kind="impl" />                       Implementado (existe no Figma)
<Badge kind="rec" />                        Recomendação
<Badge kind="prop" />                       Proposta
<Badge kind="pend" />                       Pendente de validação
<Badge kind="pend">Revisar acessibilidade</Badge>   rótulo próprio
```

**Prompt copiável**: o texto vai num bloco de código. Linhas que começam com `## ` abrem blocos que podem ser copiados separadamente. Use aspas tipográficas “ ” no texto.
````mdx
<Prompt title="Classificar as cores nos papéis do kit">

```
## Tarefa
Com base na análise anterior, classifique as cores da marca…

## O que eu preciso de volta
1. …
```

</Prompt>
````

**Aviso**: `kind` = `info`, `warn` ou `pending`.
```mdx
<Callout kind="warn" title="Fonte da marca precisa estar disponível">

Texto em Markdown.

</Callout>
```

**Etapas numeradas** (só para sequências reais), com a lista objetivo/contexto/etc.:
```mdx
<Steps>

<Step title="Analisar o material de marca">

<Details>
<Detail term="Objetivo">Entender a identidade antes de mexer em qualquer valor.</Detail>
<Detail term="Como validar">Você consegue listar as cores oficiais.</Detail>
</Details>

</Step>

</Steps>
```

**Prompt ruim × melhor**:
````mdx
<Compare>

<CompareItem kind="bad" label="Ruim">

```
Faz uma página de produto bonita.
```

</CompareItem>

<CompareItem kind="good" label="Melhor">

```
No arquivo [link], página Layout Mobile, crie a PDP mobile…
```

</CompareItem>

</Compare>
````

**Outros**: `<Layers>/<Layer title>`, `<Flow>/<FlowStep code>`, `<Changelog>/<ChangelogEntry version date>`, `<MiniTitle>`, `<HeadingNote>`, `<Swatch color="#ED1D24" />`, `<TypeSample size={20} weight={700}>R$ 129,90</TypeSample>`, `<PromptNote>`.

**Componentes de dados** (leem `src/data/`, não escreva os valores à mão):
`<BrandColors group="primary" roles="default,hover,subtle,text,on-color" />`, `<ColorTokens />`, `<SpacingScale />`, `<ComponentIndex />`, `<BrandSimulator />`.

### Cuidados de sintaxe

MDX trata alguns caracteres como código. No texto corrido, escape `<`, `{`, `}`, `*` e `_` com barra invertida: `\_Product Card Media`, `\{valor\}`. Dentro de `código` e de blocos de código não precisa escapar.

## Modelo de documentação completa de componente

`content/componentes/<slug>.mdx`. O cabeçalho, os selos, a visão geral, as propriedades, os relacionados e a data vêm automaticamente dos dados do Figma; o arquivo traz só o aprofundamento, nesta ordem:

```mdx
## Por que existe
## Decisões a preservar
## Anatomia
## Tokens e estilos
## Quando usar
### Quando evitar
## Acessibilidade
## Erros comuns
## Com IA        (pelo menos um <Prompt> específico do componente)
## Como validar
```

Veja `content/componentes/actions-button.mdx` como referência. Ao criar o arquivo, o selo do componente muda para “Documentação completa” no índice e na página.
