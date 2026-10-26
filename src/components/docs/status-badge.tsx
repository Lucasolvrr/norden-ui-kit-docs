import { cn } from "@/lib/utils";

export type StatusKind = "impl" | "rec" | "prop" | "pend";

export const STATUS_LABELS: Record<StatusKind, string> = {
  impl: "Implementado",
  rec: "Recomendação",
  prop: "Proposta",
  pend: "Pendente de validação",
};

const STYLES: Record<StatusKind, string> = {
  impl: "text-st-impl bg-st-impl-bg",
  rec: "text-st-rec bg-st-rec-bg",
  prop: "text-st-prop bg-st-prop-bg",
  pend: "text-st-pend bg-st-pend-bg",
};

/** Selo de status: Implementado, Recomendação, Proposta ou Pendente de validação. */
export function StatusBadge({ kind, children }: { kind: StatusKind; children?: React.ReactNode }) {
  return (
    <span
      className={cn(
        "inline-flex items-center gap-1.5 rounded-full px-2 py-1 align-[1px] text-xs leading-none font-medium whitespace-nowrap",
        "before:size-1.5 before:rounded-full before:bg-current before:content-['']",
        STYLES[kind],
      )}
    >
      {children ?? STATUS_LABELS[kind]}
    </span>
  );
}
