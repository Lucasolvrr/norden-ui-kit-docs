import Link from "next/link";
import { notFound } from "next/navigation";
import { DocArticle } from "@/components/layout/doc-article";
import { Callout } from "@/components/docs/callout";
import { StatusBadge } from "@/components/docs/status-badge";
import {
  componentHref,
  componentsExportedAt,
  getComponent,
  getRelated,
  kitVersion,
  parseProperties,
} from "@/lib/components";
import { hasDeepDoc } from "@/lib/content";
import { getComponentPage, PAGES } from "@/lib/nav";

export function generateStaticParams() {
  return PAGES.filter((p) => p.kind === "component").map((p) => ({ slug: p.slug }));
}

export const dynamicParams = false;

export async function generateMetadata({ params }: PageProps<"/componentes/[slug]">) {
  const page = getComponentPage((await params).slug);
  return page ? { title: page.title, description: page.lead } : {};
}

const formatDate = (iso: string) => iso.split("-").reverse().join("/");

/**
 * Página de componente: dados do Figma (src/data/components.json) +
 * documentação completa opcional em content/componentes/<slug>.mdx.
 */
export default async function ComponentPage({ params }: PageProps<"/componentes/[slug]">) {
  const { slug } = await params;
  const page = getComponentPage(slug);
  const c = getComponent(slug);
  if (!page || !c) notFound();

  const deep = hasDeepDoc(c.name);
  const Deep = deep ? (await import(`../../../../content/componentes/${slug}.mdx`)).default : null;
  const { variant, other } = parseProperties(c.properties);
  const related = getRelated(c.name);

  return (
    <DocArticle page={page}>
      <div className="mt-4 flex flex-wrap items-center gap-2">
        <StatusBadge kind="impl" />
        {c.description ? (
          <StatusBadge kind="impl">Descrição no Figma</StatusBadge>
        ) : (
          <StatusBadge kind="pend">Sem descrição no Figma</StatusBadge>
        )}
        {deep ? (
          <StatusBadge kind="rec">Documentação completa</StatusBadge>
        ) : (
          <StatusBadge kind="prop">Aprofundamento pendente</StatusBadge>
        )}
        <span className="ml-1 font-mono text-xs text-subtle">
          {c.variants} variante{c.variants !== 1 && "s"}
        </span>
      </div>

      <h2 id="visao-geral">Visão geral</h2>
      {c.description ? (
        <p>{c.description}</p>
      ) : (
        <p>
          Este componente ainda não tem descrição no campo Component information do Figma. Pela regra do kit, ela é
          obrigatória. <StatusBadge kind="pend" />
        </p>
      )}

      <h2 id="variantes">Variantes e propriedades</h2>
      {variant.length > 0 && (
        <div className="docs-table">
          <table>
            <thead>
              <tr>
                <th>Propriedade de variante</th>
                <th>Valores</th>
              </tr>
            </thead>
            <tbody>
              {variant.map((v) => (
                <tr key={v.name}>
                  <td>
                    <code>{v.name}</code>
                  </td>
                  <td>
                    {v.values.map((o, i) => (
                      <span key={o}>
                        {i > 0 && ", "}
                        <code>{o}</code>
                      </span>
                    ))}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
      {other.length > 0 && (
        <div className="docs-table">
          <table>
            <thead>
              <tr>
                <th>Propriedade</th>
                <th>Tipo</th>
              </tr>
            </thead>
            <tbody>
              {other.map((o) => (
                <tr key={o.name}>
                  <td>
                    <code>{o.name}</code>
                  </td>
                  <td>{o.type}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
      {!variant.length && !other.length && <p>Sem propriedades configuráveis: edite o componente principal.</p>}

      {Deep ? (
        <Deep />
      ) : (
        <Callout kind="pending" title="Aprofundamento pendente">
          <p>
            Fundamentação, anatomia, erros comuns e prompts específicos deste componente ainda serão escritos. Até lá,
            use a visão geral acima, as propriedades e a <Link href="/skill">skill geral</Link>.
          </p>
        </Callout>
      )}

      {related.length > 0 && (
        <>
          <h2 id="relacionados">Relacionados</h2>
          <ul>
            {related.map((r) => (
              <li key={r}>
                <Link href={componentHref(r)}>{r}</Link>
              </li>
            ))}
          </ul>
        </>
      )}

      <h2 id="atualizacoes">Atualizações</h2>
      <p>
        Dados exportados do Figma em {formatDate(componentsExportedAt)} (kit v{kitVersion}).
      </p>
    </DocArticle>
  );
}
