import {
  CATEGORY_LABELS,
  componentHref,
  componentLead,
  componentSlug,
  components,
} from "@/lib/components";

export type DocPage = {
  /** Grupo da navegação; "Componentes · Ações" vira submenu recolhível. */
  group: string;
  slug: string;
  title: string;
  lead: string;
  href: string;
  /** "doc" lê content/docs/<slug>.mdx; "component" monta a página a partir dos dados do Figma. */
  kind: "doc" | "component";
};

const doc = (group: string, slug: string, title: string, lead: string): DocPage => ({
  group,
  slug,
  title,
  lead,
  href: slug === "inicio" ? "/" : `/${slug}`,
  kind: "doc",
});

// A ordem desta lista define a navegação lateral e os links anterior/próxima.
export const PAGES: DocPage[] = [
  doc("Começando", "inicio", "Norden UI KIT", "A base de interface do time para e-commerce: fundamentos, tokens e componentes, e como usá-los com IA."),
  doc("Começando", "arquitetura", "Arquitetura do kit", "Camadas, collections, páginas e convenções de nome."),
  doc("Trabalhar com IA", "ia", "Como trabalhar com IA", "Dar contexto, pedir de forma verificável, conferir e iterar."),
  doc("Style Guide", "cores", "Cores", "Cores da marca, tokens semânticos e estados de interação."),
  doc("Style Guide", "tipografia", "Tipografia", "Família, escala responsiva e hierarquia no e-commerce."),
  doc("Style Guide", "espacamento", "Espaçamento, layout e forma", "Escalas de espaço, alturas de controle, breakpoints, raios e sombras."),
  doc("Style Guide", "tokens", "Variáveis e tokens", "Como os valores se organizam e se propagam."),
  doc("Guias", "adaptar-marca", "Adaptar para uma nova marca", "Do kit base à identidade do cliente, em dez etapas."),
  doc("Guias", "processo", "Processo de um novo projeto", "Do briefing ao handoff."),
  doc("Componentes", "componentes", "Componentes", "Inventário real do kit e situação da documentação."),
  ...components.map<DocPage>((c) => ({
    group: `Componentes · ${CATEGORY_LABELS[c.category] ?? c.category}`,
    slug: componentSlug(c.name),
    title: c.name,
    lead: componentLead(c),
    href: componentHref(c.name),
    kind: "component",
  })),
  doc("Padrões", "padroes", "Padrões de interface", "Como os componentes se combinam em partes da loja."),
  doc("IA e manutenção", "skill", "Skill geral para IA", "A instrução que ensina qualquer IA a trabalhar dentro do kit."),
  doc("IA e manutenção", "manutencao", "Manutenção da documentação", "Fontes de verdade, atualização, revisão e pendências."),
  doc("IA e manutenção", "changelog", "Changelog", "Histórico do kit e da documentação."),
];

export const DOC_PAGES = PAGES.filter((p) => p.kind === "doc");

export function getDocPage(slug: string) {
  return DOC_PAGES.find((p) => p.slug === slug);
}

export function getComponentPage(slug: string) {
  return PAGES.find((p) => p.kind === "component" && p.slug === slug);
}

export function getPrevNext(page: DocPage) {
  const i = PAGES.indexOf(page);
  return { prev: PAGES[i - 1], next: PAGES[i + 1] };
}

export type NavGroup = {
  title: string;
  items: { title: string; href: string }[];
  subgroups: { title: string; items: { title: string; href: string }[] }[];
};

export function getNavGroups(): NavGroup[] {
  const groups: NavGroup[] = [];
  for (const p of PAGES) {
    const [top, sub] = p.group.split(" · ");
    let g = groups.find((x) => x.title === top);
    if (!g) groups.push((g = { title: top, items: [], subgroups: [] }));
    if (!sub) {
      g.items.push({ title: p.slug === "componentes" ? "Visão geral" : p.title, href: p.href });
      continue;
    }
    let s = g.subgroups.find((x) => x.title === sub);
    if (!s) g.subgroups.push((s = { title: sub, items: [] }));
    s.items.push({ title: p.title.split("/").at(-1)!, href: p.href });
  }
  return groups;
}
