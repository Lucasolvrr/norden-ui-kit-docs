import data from "@/data/components.json";
import relations from "@/data/component-relations.json";

export type KitComponent = {
  name: string;
  category: string;
  variants: number;
  properties: string;
  description: string;
};

export const CATEGORY_LABELS: Record<string, string> = {
  Actions: "Ações",
  Commerce: "Comércio",
  Brand: "Marca",
  Forms: "Formulários",
  Navigation: "Navegação",
  Search: "Busca",
  Layout: "Layout",
  Feedback: "Feedback",
};

const PROPERTY_TYPES: Record<string, string> = {
  TEXT: "Texto",
  BOOLEAN: "Liga/desliga",
  INSTANCE_SWAP: "Troca de instância",
};

export const components: KitComponent[] = data.components;
export const legacyComponents: string[] = data.legacy;
export const componentsExportedAt = data.exportedAt;
export const kitVersion = data.kitVersion;

export function slugify(s: string) {
  return s
    .normalize("NFD")
    .replace(/[̀-ͯ]/g, "")
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "");
}

export const componentSlug = (name: string) => slugify(name);
export const componentHref = (name: string) => `/componentes/${componentSlug(name)}`;

export function getComponent(slug: string) {
  return components.find((c) => componentSlug(c.name) === slug);
}

export function getRelated(name: string): string[] {
  return (relations as Record<string, string[]>)[name] ?? [];
}

/** Primeira frase da descrição do Figma (usada como lead da página). */
export function componentLead(c: KitComponent) {
  if (!c.description) return "Componente do kit sem descrição no Figma.";
  const first = c.description.split(". ")[0];
  return first.endsWith(".") ? first : first + ".";
}

/** Separa "Nome=[a|b]; Outro:TEXT" em propriedades de variante e demais propriedades. */
export function parseProperties(props: string) {
  const variant: { name: string; values: string[] }[] = [];
  const other: { name: string; type: string }[] = [];
  for (const part of props.split("; ").filter(Boolean)) {
    if (part.includes("=[")) {
      const [k, v] = part.split("=[");
      variant.push({ name: k, values: v.replace(/\]$/, "").split("|") });
    } else if (part.includes(":")) {
      const i = part.lastIndexOf(":");
      const t = part.slice(i + 1);
      other.push({ name: part.slice(0, i), type: PROPERTY_TYPES[t] ?? t });
    }
  }
  return { variant, other };
}

export function componentsByCategory() {
  const groups = new Map<string, KitComponent[]>();
  for (const c of components) {
    if (!groups.has(c.category)) groups.set(c.category, []);
    groups.get(c.category)!.push(c);
  }
  return [...groups.entries()];
}
