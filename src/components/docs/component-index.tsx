import Link from "next/link";
import { CATEGORY_LABELS, componentHref, componentsByCategory, slugify } from "@/lib/components";
import { hasDeepDoc } from "@/lib/content";
import { StatusBadge } from "@/components/docs/status-badge";

/** Inventário de componentes por categoria, lido de src/data/components.json. */
export function ComponentIndex() {
  return componentsByCategory().map(([category, items]) => (
    <section key={category}>
      <h3 id={`cat-${slugify(category)}`}>{CATEGORY_LABELS[category] ?? category}</h3>
      <div className="docs-table">
        <table>
          <thead>
            <tr>
              <th>Componente</th>
              <th>Variantes</th>
              <th>Situação</th>
            </tr>
          </thead>
          <tbody>
            {items.map((c) => (
              <tr key={c.name}>
                <td>
                  <Link href={componentHref(c.name)}>{c.name}</Link>
                </td>
                <td>{c.variants}</td>
                <td>
                  {hasDeepDoc(c.name) ? (
                    <StatusBadge kind="rec">Completa</StatusBadge>
                  ) : (
                    <StatusBadge kind="prop">Pendente</StatusBadge>
                  )}
                  {!c.description && (
                    <>
                      {" "}
                      <StatusBadge kind="pend">Sem descrição</StatusBadge>
                    </>
                  )}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  ));
}
