import "server-only";
import fs from "node:fs";
import path from "node:path";
import { componentSlug } from "@/lib/components";

const CONTENT_DIR = path.join(process.cwd(), "content");

/** Um componente tem documentação completa quando existe content/componentes/<slug>.mdx. */
export function hasDeepDoc(name: string) {
  return fs.existsSync(path.join(CONTENT_DIR, "componentes", `${componentSlug(name)}.mdx`));
}

export function readContent(kind: "docs" | "componentes", slug: string) {
  const file = path.join(CONTENT_DIR, kind, `${slug}.mdx`);
  return fs.existsSync(file) ? fs.readFileSync(file, "utf8") : null;
}
