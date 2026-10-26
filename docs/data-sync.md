# Atualizar os dados do Figma

Não há sincronização automática. O processo é manual, com uma IA que tenha acesso ao Figma (MCP do Figma, `use_figma`, arquivo `UvGPurA87NxEPGeaAJ8bHH`):

1. Exportar variáveis: para cada collection, nome, tipo, valor por mode, alias resolvido (nome → hex) e descrição.
2. Exportar componentes das páginas Componentes e Layout Mobile: nome, seção, nº de variantes, propriedades (`Nome=[a|b]` para variantes; `Nome:TEXT|BOOLEAN|INSTANCE_SWAP`) e descrição.
3. Comparar com `src/data/tokens.json` e `src/data/components.json` e listar: adicionados, removidos/renomeados, valores alterados, componentes sem descrição.
4. Atualizar os arquivos, rodar `npm run build`, revisar as páginas afetadas e registrar no changelog (`content/docs/changelog.mdx`) a versão do kit e a data da exportação. A data aparece nas páginas de componente (`exportedAt` em `components.json`) e no cabeçalho de todas as páginas (`src/lib/site.ts`).
5. Abrir um pull request para revisão do time antes de publicar.

Snippet de exportação de componentes (via `use_figma`, somente leitura):
```js
const comp = figma.root.children.find(p => /Componentes/.test(p.name)); await comp.loadAsync();
const out = [];
for (const c of comp.findAllWithCriteria({ types: ['COMPONENT_SET', 'COMPONENT'] })) {
  if (c.type === 'COMPONENT' && c.parent.type === 'COMPONENT_SET') continue;
  if (/^(Format|Weight)=/.test(c.name)) continue; // ícones Phosphor
  let props = []; try { props = Object.entries(c.componentPropertyDefinitions).map(([k, d]) => d.type === 'VARIANT' ? `${k}=[${d.variantOptions.join('|')}]` : `${k.split('#')[0]}:${d.type}`); } catch (e) {}
  out.push([c.name, c.type === 'COMPONENT_SET' ? c.children.length : 1, props.join('; '), c.description || '']);
}
return JSON.stringify(out);
```

## Formato dos arquivos

`src/data/tokens.json`
```json
{
  "Brand": { "modes": ["Norden Default"], "vars": [["primary/default", "C", "#1C1C21", "descrição"]] },
  "Color": [["text/primary", "neutral/900", "#1C1C21", "uso"]]
}
```

`src/data/components.json`
```json
{
  "exportedAt": "2026-10-26",
  "kitVersion": "0.4",
  "components": [
    { "name": "Actions/Button", "category": "Actions", "variants": 27,
      "properties": "Label:TEXT; Variant=[Primary|Secondary|Tertiary]", "description": "…" }
  ],
  "legacy": ["Button (referência antiga de botões)"]
}
```

A categoria precisa existir em `CATEGORY_LABELS` (`src/lib/components.ts`). Um componente novo ganha página e entrada no menu automaticamente.

`src/data/spacing.json`: `[["16", "uso"]]`, a escala da collection Dimension exibida em Espaçamento.
