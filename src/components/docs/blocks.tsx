import { slugify } from "@/lib/components";
import { cn } from "@/lib/utils";

/* Etapas numeradas: só para conteúdo realmente sequencial. */
export function Steps({ children }: { children: React.ReactNode }) {
  return <ol className="!my-4 ![counter-reset:step] !max-w-none !list-none !p-0">{children}</ol>;
}

export function Step({ title, children }: { title: string; children: React.ReactNode }) {
  return (
    <li
      className={cn(
        "relative !my-0 ml-[13px] border-l pb-2 pl-11 [counter-increment:step] last:border-l-transparent",
        "before:absolute before:top-0 before:-left-3.5 before:grid before:size-7 before:place-items-center before:rounded-full before:border before:bg-background before:font-mono before:text-[12.5px] before:font-medium before:text-foreground before:content-[counter(step)]",
      )}
    >
      <h3 id={slugify(title)} className="!mt-0.5 !mb-2">
        {title}
      </h3>
      {children}
    </li>
  );
}

/* Lista objetivo / contexto / no Figma / erros / validação de cada etapa. */
export function Details({ children }: { children: React.ReactNode }) {
  return (
    <dl className="my-2 grid grid-cols-1 gap-x-4 gap-y-1.5 text-sm min-[901px]:grid-cols-[150px_1fr]">
      {children}
    </dl>
  );
}

export function Detail({ term, children }: { term: string; children: React.ReactNode }) {
  return (
    <>
      <dt className="mt-1.5 text-subtle min-[901px]:mt-0">{term}</dt>
      <dd>{children}</dd>
    </>
  );
}

/* Comparação de prompt ruim × melhor. */
export function Compare({ children }: { children: React.ReactNode }) {
  return <div className="my-4 grid grid-cols-1 gap-3 min-[901px]:grid-cols-2">{children}</div>;
}

export function CompareItem({
  kind,
  label,
  children,
}: {
  kind: "bad" | "good";
  label: string;
  children: React.ReactNode;
}) {
  return (
    <div className="rounded-[10px] border bg-card">
      <p
        className={cn(
          "!m-0 border-b px-3.5 py-2 text-[12.5px] font-semibold",
          kind === "bad" ? "text-st-bad" : "text-st-impl",
        )}
      >
        {label}
      </p>
      {children}
    </div>
  );
}

/* Camadas da arquitetura. */
export function Layers({ children }: { children: React.ReactNode }) {
  return <div className="my-5 grid">{children}</div>;
}

export function Layer({ title, children }: { title: string; children: React.ReactNode }) {
  return (
    <div className="border bg-card px-4 py-3.5 first:rounded-t-[10px] last:rounded-b-[10px] [&+&]:border-t-0">
      <p className="!mt-0 !mb-0.5 font-semibold text-strong">{title}</p>
      <p className="!m-0">{children}</p>
    </div>
  );
}

/* Propagação de um valor entre camadas. */
export function Flow({ children }: { children: React.ReactNode }) {
  return <div className="my-4 flex flex-wrap items-stretch gap-2">{children}</div>;
}

export function FlowStep({ code, children }: { code: string; children: React.ReactNode }) {
  return (
    <>
      <span
        aria-hidden="true"
        className="hidden size-3.5 rotate-45 self-center border-t-[1.5px] border-r-[1.5px] border-subtle [div+&]:block"
      />
      <div className="flex-[1_1_180px] rounded-[10px] border bg-card px-3.5 py-3">
        <code>{code}</code>
        <p className="!mt-1.5 !mb-0 text-[13.5px] text-muted-foreground">{children}</p>
      </div>
    </>
  );
}

/* Histórico de versões. */
export function Changelog({ children }: { children: React.ReactNode }) {
  return <div className="my-4 border-t">{children}</div>;
}

export function ChangelogEntry({
  version,
  date,
  children,
}: {
  version: string;
  date: string;
  children: React.ReactNode;
}) {
  return (
    <div className="grid grid-cols-1 gap-1 border-b border-line-2 py-4 min-[901px]:grid-cols-[150px_1fr] min-[901px]:gap-5">
      <div>
        <p className="!m-0 font-semibold text-strong">{version}</p>
        <p className="!m-0 font-mono text-xs text-subtle">{date}</p>
      </div>
      <p className="!m-0">{children}</p>
    </div>
  );
}

export function MiniTitle({ children }: { children: React.ReactNode }) {
  return <p className="!mt-4 !mb-1.5 font-mono text-xs font-medium text-subtle">{children}</p>;
}

export function HeadingNote({ children }: { children: React.ReactNode }) {
  return <span className="ml-2 font-mono text-xs font-normal text-subtle">{children}</span>;
}

export function Swatch({ color }: { color: string }) {
  return (
    <span
      title={color}
      style={{ background: color }}
      className="mr-2 inline-block size-3.5 rounded align-[-2px] shadow-[inset_0_0_0_1px_rgba(127,127,127,.35)]"
    />
  );
}

export function TypeSample({
  size,
  weight,
  uppercase,
  strike,
  children,
}: {
  size: number;
  weight: number;
  uppercase?: boolean;
  strike?: boolean;
  children: React.ReactNode;
}) {
  return (
    <span
      className="leading-tight whitespace-nowrap text-strong"
      style={{
        fontSize: size,
        fontWeight: weight,
        textTransform: uppercase ? "uppercase" : undefined,
        letterSpacing: uppercase ? ".04em" : undefined,
        textDecoration: strike ? "line-through" : undefined,
      }}
    >
      {children}
    </span>
  );
}
