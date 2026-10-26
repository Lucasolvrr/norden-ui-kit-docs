import spacing from "@/data/spacing.json";
import { brandValue, COLOR_GROUP_LABELS, colorTokenGroups } from "@/lib/tokens";
import { HeadingNote, Swatch } from "@/components/docs/blocks";
import { Token } from "@/components/docs/token-button";

/** Amostras de uma cor da Brand, lidas de src/data/tokens.json. */
export function BrandColors({ group, roles }: { group: string; roles: string }) {
  return (
    <div className="my-3 mb-5 grid grid-cols-[repeat(auto-fill,minmax(112px,1fr))] gap-2">
      {roles.split(",").map((role) => {
        const hex = brandValue(`${group}/${role}`) ?? "—";
        return (
          <div key={role} className="overflow-hidden rounded-[9px] border bg-card font-mono text-xs">
            <span className="block h-[52px] border-b border-line-2" style={{ background: hex }} />
            <span className="block px-2.5 pt-2 text-foreground">{role}</span>
            <span className="block px-2.5 pb-2 text-subtle">{hex}</span>
          </div>
        );
      })}
    </div>
  );
}

/** Tabelas dos tokens semânticos (collection Color), agrupados por função. */
export function ColorTokens() {
  return colorTokenGroups().map(([group, rows]) => (
    <section key={group}>
      <h3 id={`tok-${group}`}>
        {COLOR_GROUP_LABELS[group] ?? group}
        <HeadingNote>{`${group}/*`}</HeadingNote>
      </h3>
      <div className="docs-table">
        <table>
          <thead>
            <tr>
              <th>Token</th>
              <th>Aponta para</th>
              <th>Uso</th>
            </tr>
          </thead>
          <tbody>
            {rows.map(([name, ref, hex, use]) => (
              <tr key={name}>
                <td className="whitespace-nowrap">
                  <Swatch color={hex.split(" ")[0]} />
                  <Token>{name}</Token>
                </td>
                <td>
                  <code>{ref}</code>
                </td>
                <td>{use}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  ));
}

/** Escala de espaçamento (collection Dimension), lida de src/data/spacing.json. */
export function SpacingScale() {
  return (
    <div className="my-4 overflow-hidden rounded-[10px] border">
      {(spacing as [string, string][]).map(([n, use]) => (
        <div
          key={n}
          className="grid grid-cols-[96px_1fr] items-center gap-3 border-b border-line-2 px-3.5 py-2 text-[13.5px] last:border-b-0 min-[901px]:grid-cols-[110px_270px_1fr]"
        >
          <code className="justify-self-start">spacing/{n}</code>
          <span
            className="h-2.5 max-w-64 rounded-[3px] bg-muted-foreground"
            style={{ width: Math.max(Number(n), 1) * 2 }}
          />
          <span className="col-span-full min-[901px]:col-auto">{use}</span>
        </div>
      ))}
    </div>
  );
}
