import "server-only";
import spacing from "@/data/spacing.json";
import { PAGES } from "@/lib/nav";
import { components, componentSlug, getRelated, parseProperties } from "@/lib/components";
import { brandValue, colorTokens } from "@/lib/tokens";
import { readContent } from "@/lib/content";
import { STATUS_LABELS, type StatusKind } from "@/components/docs/status-badge";

export type SearchEntry = { href: string; title: string; group: string; text: string };

// Texto que os componentes de dados renderizam, para a busca encontrar tokens e componentes.
const DATA_TEXT: Record<string, () => string> = {
  ColorTokens: () => colorTokens.map((t) => t.join(" ")).join(" "),
  SpacingScale: () => (spacing as [string, string][]).map(([n, u]) => `spacing/${n} ${u}`).join(" "),
  ComponentIndex: () => components.map((c) => c.name).join(" "),
};

/** Converte MDX em texto corrido para indexação. */
function mdxToText(src: string) {
  return src
    .replace(/<Badge kind="(\w+)" \/>/g, (_, k: StatusKind) => STATUS_LABELS[k])
    .replace(/<BrandColors group="([^"]+)" roles="([^"]+)" \/>/g, (_, g: string, roles: string) =>
      roles
        .split(",")
        .map((r) => `${r} ${brandValue(`${g}/${r}`) ?? ""}`)
        .join(" "),
    )
    .replace(/<(\w+) \/>/g, (_, name: string) => DATA_TEXT[name]?.() ?? "")
    .replace(/<\/?[A-Za-z][^>]*?(?:(?:title|term|label|version|date|code)=(?:"([^"]*)"|\{"([^"]*)"\})[^>]*)?>/g, " $1$2 ")
    .replace(/^```.*$/gm, "")
    .replace(/\[([^\]]*)\]\([^)]*\)/g, "$1")
    .replace(/^#{1,6} |^\s*(?:[-*]|\d+\.) |^\|? ?-{3}.*$/gm, "")
    .replace(/\*\*|`|\|/g, " ")
    .replace(/\\(.)/g, "$1")
    .replace(/\s+/g, " ")
    .trim();
}

export function buildSearchIndex(): SearchEntry[] {
  return PAGES.map((p) => {
    let text = "";
    if (p.kind === "doc") {
      text = mdxToText(readContent("docs", p.slug) ?? "");
    } else {
      const c = components.find((x) => componentSlug(x.name) === p.slug)!;
      const { variant, other } = parseProperties(c.properties);
      text = [
        c.description,
        ...variant.map((v) => `${v.name} ${v.values.join(" ")}`),
        ...other.map((o) => `${o.name} ${o.type}`),
        mdxToText(readContent("componentes", p.slug) ?? ""),
        ...getRelated(c.name),
      ].join(" ");
    }
    return { href: p.href, title: p.title, group: p.group.replace(" · ", " / "), text: `${p.lead} ${text}` };
  });
}
