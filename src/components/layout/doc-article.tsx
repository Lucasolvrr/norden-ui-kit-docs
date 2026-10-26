import Link from "next/link";
import { getPrevNext, type DocPage } from "@/lib/nav";
import { site } from "@/lib/site";

/** Cabeçalho, conteúdo e navegação anterior/próxima de uma página da documentação. */
export function DocArticle({ page, children }: { page: DocPage; children: React.ReactNode }) {
  const { prev, next } = getPrevNext(page);
  return (
    <article className="max-w-[760px]">
      <header className="mb-2 border-b border-line-2 pb-6">
        <p className="mb-2.5 text-[13px] text-subtle">{page.group.replace(" · ", " / ")}</p>
        <h1 className="text-[30px] leading-[1.15] font-semibold tracking-[-0.025em] text-balance text-strong min-[901px]:text-4xl">
          {page.title}
        </h1>
        <p className="mt-3 max-w-[62ch] text-[17px] text-muted-foreground">{page.lead}</p>
        <p className="mt-3.5 font-mono text-xs text-subtle">
          {site.kitVersion} · Atualizado em {site.updatedAt}
        </p>
      </header>

      <div className="docs-prose" data-docs-content>
        {children}
      </div>

      <nav aria-label="Navegação entre páginas" className="mt-16 flex justify-between gap-3 border-t border-line-2 pt-5">
        {prev && <PagerLink page={prev} label="Anterior" />}
        {next && <PagerLink page={next} label="Próxima" className="ml-auto text-right" />}
      </nav>
    </article>
  );
}

function PagerLink({ page, label, className = "" }: { page: DocPage; label: string; className?: string }) {
  return (
    <Link
      href={page.href}
      className={`flex max-w-[48%] flex-col gap-0.5 rounded-[10px] border px-3.5 py-2.5 hover:border-subtle ${className}`}
    >
      <small className="text-xs text-subtle">{label}</small>
      <span className="font-medium text-strong">{page.title}</span>
    </Link>
  );
}
