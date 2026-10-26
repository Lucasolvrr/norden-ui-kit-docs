import data from "@/data/tokens.json";

/** [nome, tipo, valor, descrição] exportados da collection Brand. */
export type BrandVar = [string, string, string, string];
/** [token, aponta_para, hex_resolvido, uso] exportados da collection Color. */
export type ColorToken = [string, string, string, string];

export const brandVars = data.Brand.vars as BrandVar[];
export const colorTokens = data.Color as ColorToken[];

export function brandValue(name: string) {
  return brandVars.find((v) => v[0] === name)?.[2];
}

export const COLOR_GROUP_LABELS: Record<string, string> = {
  text: "Texto",
  icon: "Ícones",
  background: "Fundos",
  surface: "Superfícies",
  border: "Bordas",
  commerce: "Comércio",
  overlay: "Sobreposição",
  shadow: "Sombras",
};

export function colorTokenGroups() {
  const groups = new Map<string, ColorToken[]>();
  for (const t of colorTokens) {
    const g = t[0].split("/")[0];
    if (!groups.has(g)) groups.set(g, []);
    groups.get(g)!.push(t);
  }
  return [...groups.entries()];
}
