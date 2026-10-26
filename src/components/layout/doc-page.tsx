import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { DocArticle } from "@/components/layout/doc-article";
import { getDocPage } from "@/lib/nav";

/** Página de conteúdo: lê content/docs/<slug>.mdx. */
export async function DocPage({ slug }: { slug: string }) {
  const page = getDocPage(slug);
  if (!page) notFound();
  const { default: Content } = await import(`../../../content/docs/${slug}.mdx`);
  return (
    <DocArticle page={page}>
      <Content />
    </DocArticle>
  );
}

export function docMetadata(slug: string): Metadata {
  const page = getDocPage(slug);
  return page ? { title: page.title, description: page.lead } : {};
}
