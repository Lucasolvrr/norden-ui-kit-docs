"use client";

import { useMemo, useState } from "react";
import { cn } from "@/lib/utils";

type RGB = [number, number, number];

// Mesma lógica do brand_palette.py da skill norden-ui-kit.
const parseHex = (h: string): RGB | null => {
  h = h.replace("#", "");
  if (h.length === 3) h = [...h].map((c) => c + c).join("");
  return /^[0-9a-f]{6}$/i.test(h) ? ([0, 2, 4].map((i) => parseInt(h.slice(i, i + 2), 16) / 255) as RGB) : null;
};
const toHex = (c: RGB) =>
  "#" +
  c
    .map((v) => Math.round(Math.max(0, Math.min(1, v)) * 255).toString(16).padStart(2, "0"))
    .join("")
    .toUpperCase();
const mix = (a: RGB, b: RGB, t: number) => a.map((v, i) => v + (b[i] - v) * t) as RGB;
const lum = (c: RGB) => {
  const f = (v: number) => (v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4));
  const [r, g, b] = c.map(f);
  return 0.2126 * r + 0.7152 * g + 0.0722 * b;
};
const contrast = (a: RGB, b: RGB) => {
  const x = lum(a);
  const y = lum(b);
  return (Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05);
};
const WHITE: RGB = [1, 1, 1];
const BLACK: RGB = [0, 0, 0];
const DARK = parseHex("1C1C21")!;

function palette(d: RGB) {
  const hover = mix(d, BLACK, lum(d) < 0.03 ? 0.45 : 0.14);
  const subtle = mix(d, WHITE, 0.92);
  let text = d;
  for (let s = 1; Math.min(contrast(text, WHITE), contrast(text, subtle)) < 4.5 && s <= 40; s++) {
    text = mix(d, BLACK, s * 0.025);
  }
  const on = contrast(WHITE, d) >= contrast(DARK, d) ? WHITE : DARK;
  const roles: [string, RGB, number, string][] = [
    ["default", d, contrast(on, d), "on-color sobre ele"],
    ["hover", hover, contrast(on, hover), "on-color sobre ele"],
    ["subtle", subtle, contrast(text, subtle), "text sobre ele"],
    ["text", text, contrast(text, WHITE), "sobre branco"],
    ["on-color", on, contrast(on, d), "sobre o default"],
  ];
  const notes: string[] = [];
  if (contrast(on, d) < 4.5)
    notes.push("O texto do botão fica abaixo de 4,5:1: registre a exceção ou use a versão “text” como fundo do botão.");
  if (toHex(text) !== toHex(d)) notes.push("A cor não tem contraste como texto: links e preço usam a versão escurecida.");
  return {
    roles,
    vars: {
      "--p-default": toHex(d),
      "--p-hover": toHex(hover),
      "--p-subtle": toHex(subtle),
      "--p-text": toHex(text),
      "--p-on": toHex(on),
    } as React.CSSProperties,
    note: notes.join(" ") || "Todos os pares passam no contraste mínimo.",
  };
}

/** Simulador de cor da marca (página Cores). */
export function BrandSimulator() {
  const [color, setColor] = useState("#ED1D24");
  const [hexInput, setHexInput] = useState("#ED1D24");
  const result = useMemo(() => palette(parseHex(color)!), [color]);

  return (
    <div className="my-4 rounded-xl border bg-card p-4">
      <label htmlFor="sim-color" className="text-[13px] text-muted-foreground">
        Cor primária
      </label>
      <div className="mt-1.5 flex gap-2">
        <input
          type="color"
          id="sim-color"
          aria-label="Escolher cor"
          value={color.toLowerCase()}
          onChange={(e) => {
            setColor(e.target.value);
            setHexInput(e.target.value.toUpperCase());
          }}
          className="h-[38px] w-11 rounded-lg border bg-background p-0.5"
        />
        <input
          type="text"
          aria-label="Hex da cor"
          spellCheck={false}
          value={hexInput}
          onChange={(e) => {
            setHexInput(e.target.value);
            const parsed = parseHex(e.target.value);
            if (parsed) setColor(toHex(parsed));
          }}
          className="h-[38px] w-[140px] rounded-lg border bg-background px-2.5 font-mono text-sm text-foreground"
        />
      </div>

      <div className="my-4 grid grid-cols-2 gap-2 min-[901px]:grid-cols-5">
        {result.roles.map(([name, c, ratio, label]) => (
          <div key={name} className="overflow-hidden rounded-[9px] border bg-background font-mono text-xs">
            <div className="h-[46px]" style={{ background: toHex(c) }} />
            <p className="!m-0 px-2.5 pt-2 text-foreground">{name}</p>
            <p className="!m-0 px-2.5 text-subtle">{toHex(c)}</p>
            <p className={cn("!m-0 px-2.5 pb-2", ratio < 4.5 ? "text-st-pend" : "text-muted-foreground")}>
              {ratio.toFixed(2).replace(".", ",")}:1 {label}
            </p>
          </div>
        ))}
      </div>

      <div
        style={result.vars}
        className="flex flex-wrap items-center gap-4 rounded-[10px] border bg-white p-[18px] text-[#1c1c21]"
      >
        <button
          type="button"
          className="h-11 rounded-[10px] bg-(--p-default) px-[18px] text-[15px] font-semibold text-(--p-on) hover:bg-(--p-hover)"
        >
          Adicionar ao carrinho
        </button>
        <span className="rounded-md bg-(--p-subtle) px-2 py-1 text-xs font-semibold text-(--p-text)">Novo</span>
        <span className="text-xl font-bold text-(--p-text)">R$ 49,90</span>
        <a className="text-sm font-medium text-(--p-text) underline underline-offset-[3px]">Ver detalhes do produto</a>
      </div>
      <p className="!mt-2.5 !mb-0 text-[13px] text-subtle">{result.note}</p>
    </div>
  );
}
