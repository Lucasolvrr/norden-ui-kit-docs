"use client";

import { copyText } from "@/components/docs/copy-button";

/** Nome de token que copia ao clicar. */
export function Token({ children }: { children: string }) {
  return (
    <button
      type="button"
      onClick={() => copyText(children, `Token copiado: ${children}`)}
      className="border-0 border-b border-dashed border-subtle bg-transparent p-0 font-mono text-[12.5px] text-foreground hover:border-solid hover:text-strong"
    >
      {children}
    </button>
  );
}
