import { nodeText } from "@/lib/node-text";
import { CopyButton } from "@/components/docs/copy-button";

/** Divide o prompt em blocos: cada linha que começa com "## " abre um bloco copiável. */
function segments(text: string) {
  const segs: string[][] = [];
  let cur: string[] = [];
  for (const line of text.replace(/^\n+|\n+$/g, "").split("\n")) {
    if (line.startsWith("## ") && cur.length) {
      segs.push(cur);
      cur = [];
    }
    cur.push(line);
  }
  if (cur.length) segs.push(cur);
  return segs.map((lines) => ({
    head: lines[0].startsWith("## ") ? lines[0].slice(3) : null,
    text: lines.join("\n").replace(/^\n+|\n+$/g, ""),
  }));
}

/**
 * Prompt pronto para copiar. No MDX, o texto vai num bloco de código:
 *
 * <Prompt title="...">
 * ```
 * texto do prompt
 * ```
 * </Prompt>
 */
export function Prompt({ title, children }: { title: string; children: React.ReactNode }) {
  const segs = segments(nodeText(children));
  const full = segs.map((s) => s.text).join("\n\n");
  return (
    <figure className="my-5 overflow-hidden rounded-[10px] border bg-card">
      <figcaption className="flex items-center justify-between gap-3 border-b py-2.5 pr-3 pl-3.5">
        <span className="text-[13.5px] font-semibold text-strong">{title}</span>
        <CopyButton text={full} message="Prompt copiado">
          Copiar prompt
        </CopyButton>
      </figcaption>
      {segs.map((s, i) => (
        <div key={i} className="group border-dashed [&+&]:border-t">
          {s.head && (
            <div className="flex items-center justify-between pt-2 pr-3 pl-3.5 font-mono text-xs font-medium text-subtle">
              <span>{s.head}</span>
              <CopyButton
                text={s.text}
                message="Bloco copiado"
                aria-label={`Copiar o bloco ${s.head}`}
                className="opacity-0 transition-opacity group-hover:opacity-100 focus-visible:opacity-100"
              >
                Copiar bloco
              </CopyButton>
            </div>
          )}
          <pre>{s.text}</pre>
        </div>
      ))}
    </figure>
  );
}

export function PromptNote({ children }: { children: React.ReactNode }) {
  return <p className="text-[13px] text-subtle">{children}</p>;
}
