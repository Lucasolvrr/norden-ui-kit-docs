"use client";

import { useEffect, useMemo, useState } from "react";
import { useRouter } from "next/navigation";
import {
  Command,
  CommandDialog,
  CommandEmpty,
  CommandInput,
  CommandItem,
  CommandList,
} from "@/components/ui/command";
import { site } from "@/lib/site";
import type { SearchEntry } from "@/lib/search-index";

type Indexed = SearchEntry & { n: string; nt: string };

const norm = (s: string) => s.normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase();
const SUGGESTED = ["/", "/ia", "/cores", "/adaptar-marca", "/componentes", "/skill"];

let cache: Promise<Indexed[]> | null = null;
function loadIndex() {
  cache ??= fetch(`${site.basePath}/search-index.json`)
    .then((r) => r.json() as Promise<SearchEntry[]>)
    .then((entries) => entries.map((e) => ({ ...e, n: norm(e.text), nt: norm(e.title) })))
    .catch(() => {
      cache = null;
      return [];
    });
  return cache;
}

/** Trecho em volta do primeiro termo, com os termos destacados. */
function Snippet({ entry, terms }: { entry: Indexed; terms: string[] }) {
  const k = entry.n.indexOf(terms[0]);
  const start = Math.max(0, k - 50);
  const raw = entry.text.slice(start, start + 140);
  const n = norm(raw);
  const parts: React.ReactNode[] = [];
  let i = 0;
  while (i < raw.length) {
    const hit = terms.find((t) => n.startsWith(t, i));
    if (hit) {
      parts.push(<mark key={i} className="bg-transparent font-semibold text-strong">{raw.slice(i, i + hit.length)}</mark>);
      i += hit.length;
    } else {
      const next = terms.map((t) => n.indexOf(t, i)).filter((x) => x > i);
      const j = next.length ? Math.min(...next) : raw.length;
      parts.push(raw.slice(i, j));
      i = j;
    }
  }
  return <span className="block truncate text-[13px] text-muted-foreground">{parts}</span>;
}

export function SearchDialog({ open, onOpenChange }: { open: boolean; onOpenChange: (o: boolean) => void }) {
  const router = useRouter();
  const [index, setIndex] = useState<Indexed[]>([]);
  const [query, setQuery] = useState("");

  useEffect(() => {
    if (open) loadIndex().then(setIndex);
  }, [open]);

  const handleOpenChange = (o: boolean) => {
    if (!o) setQuery("");
    onOpenChange(o);
  };

  const terms = useMemo(() => norm(query).split(/\s+/).filter(Boolean), [query]);
  const results = useMemo(() => {
    if (!terms.length) return SUGGESTED.map((h) => index.find((e) => e.href === h)).filter((e): e is Indexed => !!e);
    return index
      .filter((e) => terms.every((t) => e.n.includes(t) || e.nt.includes(t)))
      .map((e) => ({ e, s: terms.reduce((a, t) => a + (e.nt.includes(t) ? 10 : 0) + (e.n.split(t).length - 1), 0) }))
      .sort((a, b) => b.s - a.s)
      .slice(0, 14)
      .map((x) => x.e);
  }, [index, terms]);

  return (
    <CommandDialog
      open={open}
      onOpenChange={handleOpenChange}
      title="Buscar"
      description="Buscar componentes, tokens e prompts na documentação"
      className="top-[12vh] translate-y-0 sm:max-w-[640px]"
    >
      <Command shouldFilter={false}>
        <CommandInput placeholder="Buscar componentes, tokens, prompts…" value={query} onValueChange={setQuery} />
        <CommandList className="max-h-[60vh]">
          <CommandEmpty>Nada encontrado. Tente outro termo, como “preço”, “token” ou “prompt”.</CommandEmpty>
          {results.map((e) => (
            <CommandItem
              key={e.href}
              value={e.href}
              onSelect={() => {
                router.push(e.href);
                handleOpenChange(false);
              }}
              className="block px-3 py-2"
            >
              <span className="text-[14.5px] font-medium text-strong">{e.title}</span>
              <span className="ml-2 text-xs text-subtle">{e.group}</span>
              {terms.length > 0 && <Snippet entry={e} terms={terms} />}
            </CommandItem>
          ))}
        </CommandList>
      </Command>
    </CommandDialog>
  );
}
