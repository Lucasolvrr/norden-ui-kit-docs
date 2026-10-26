import { DocPage, docMetadata } from "@/components/layout/doc-page";
import { DOC_PAGES } from "@/lib/nav";

// "inicio" é a home (/) e "componentes" tem rota própria.
export function generateStaticParams() {
  return DOC_PAGES.filter((p) => !["inicio", "componentes"].includes(p.slug)).map((p) => ({ slug: p.slug }));
}

export const dynamicParams = false;

export async function generateMetadata({ params }: PageProps<"/[slug]">) {
  return docMetadata((await params).slug);
}

export default async function Page({ params }: PageProps<"/[slug]">) {
  return <DocPage slug={(await params).slug} />;
}
