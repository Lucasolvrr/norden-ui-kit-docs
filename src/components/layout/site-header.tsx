"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { useTheme } from "next-themes";
import { Contrast, Menu, Search } from "lucide-react";
import { Sheet, SheetContent, SheetTitle } from "@/components/ui/sheet";
import { SearchDialog } from "@/components/layout/search-dialog";
import { SidebarNav } from "@/components/layout/sidebar-nav";
import { site } from "@/lib/site";

const iconButton =
  "grid size-[34px] place-items-center rounded-lg border bg-transparent text-muted-foreground hover:bg-accent hover:text-foreground";

export function SiteHeader() {
  const [searchOpen, setSearchOpen] = useState(false);
  const [navOpen, setNavOpen] = useState(false);
  const { resolvedTheme, setTheme } = useTheme();
  // "/" ou Ctrl/Cmd+K abrem a busca.
  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      const tag = (e.target as HTMLElement).tagName?.toLowerCase();
      if ((e.key === "/" && !["input", "textarea"].includes(tag)) || ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k")) {
        e.preventDefault();
        setSearchOpen(true);
      }
    };
    document.addEventListener("keydown", onKey);
    return () => document.removeEventListener("keydown", onKey);
  }, []);

  return (
    <header className="sticky top-0 z-50 flex h-(--header-h) items-center gap-4 border-b bg-background/88 px-5 backdrop-blur-md">
      <button type="button" aria-label="Abrir navegação" aria-expanded={navOpen} onClick={() => setNavOpen(true)} className={`${iconButton} min-[901px]:hidden`}>
        <Menu className="size-[18px]" />
      </button>

      <Link href="/" className="flex items-center gap-2.5 text-[15px] font-semibold whitespace-nowrap">
        <span aria-hidden="true" className="size-[18px] rounded-[5px] bg-[linear-gradient(135deg,var(--strong)_0_50%,var(--subtle)_50%_100%)]" />
        <span>{site.name}</span>
        <span className="font-medium text-subtle max-[560px]:hidden">Docs</span>
      </Link>

      <button
        type="button"
        aria-label="Buscar na documentação"
        onClick={() => setSearchOpen(true)}
        className="ml-auto flex h-[34px] items-center gap-2.5 rounded-lg border bg-card pr-2 pl-3 text-[13.5px] text-subtle hover:border-subtle hover:text-muted-foreground max-[560px]:w-[34px] max-[560px]:flex-none max-[560px]:justify-center max-[560px]:p-0 max-[900px]:max-w-80 max-[900px]:flex-1 min-[901px]:min-w-[280px]"
      >
        <Search className="size-[15px]" />
        <span className="flex-1 text-left max-[560px]:hidden">Buscar na documentação</span>
        <kbd className="max-[900px]:hidden">/</kbd>
      </button>

      <span className="rounded-full border px-2.5 py-[3px] font-mono text-xs font-medium whitespace-nowrap text-muted-foreground max-[900px]:hidden">
        {site.kitVersion}
      </span>

      <button
        type="button"
        aria-label="Alternar tema claro e escuro"
        onClick={() => setTheme(resolvedTheme === "light" ? "dark" : "light")}
        className={iconButton}
      >
        <Contrast className="size-4" />
      </button>

      <SearchDialog open={searchOpen} onOpenChange={setSearchOpen} />

      <Sheet open={navOpen} onOpenChange={setNavOpen}>
        <SheetContent side="left" className="w-[min(300px,85vw)] overflow-y-auto px-4 pt-6 pb-12">
          <SheetTitle className="sr-only">Navegação</SheetTitle>
          {/* Fecha a gaveta ao escolher uma página. */}
          <div onClick={(e) => (e.target as HTMLElement).closest("a") && setNavOpen(false)}>
            <SidebarNav />
          </div>
        </SheetContent>
      </Sheet>
    </header>
  );
}
