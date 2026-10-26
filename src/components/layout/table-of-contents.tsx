"use client";

import { useEffect, useState } from "react";
import { usePathname } from "next/navigation";
import { cn } from "@/lib/utils";

type Heading = { id: string; text: string; level: 2 | 3; el: HTMLElement };

/** "Nesta página": gerado dos h2/h3 do conteúdo, com destaque da seção visível. */
export function TableOfContents() {
  const pathname = usePathname();
  const [headings, setHeadings] = useState<Heading[]>([]);
  const [active, setActive] = useState<string | null>(null);

  useEffect(() => {
    const els = [...document.querySelectorAll<HTMLElement>("[data-docs-content] h2, [data-docs-content] h3")];
    // Lê os títulos depois que o conteúdo da nova página foi pintado.
    const frame = requestAnimationFrame(() => {
      setHeadings(
        els.map((el) => ({
          id: el.id,
          text: (el.childNodes[0]?.textContent ?? el.textContent ?? "").trim(),
          level: el.tagName === "H3" ? 3 : 2,
          el,
        })),
      );
      setActive(null);
    });
    const obs = new IntersectionObserver(
      (entries) => entries.forEach((e) => e.isIntersecting && setActive((e.target as HTMLElement).id)),
      { rootMargin: "-70px 0px -70% 0px" },
    );
    els.forEach((el) => obs.observe(el));
    return () => {
      cancelAnimationFrame(frame);
      obs.disconnect();
    };
  }, [pathname]);

  if (!headings.length) return null;

  return (
    <>
      <p className="mb-2 text-[12.5px] font-semibold">Nesta página</p>
      <nav>
        {headings.map((h) => (
          <a
            key={h.id + h.text}
            href={`#${h.id}`}
            onClick={(e) => {
              e.preventDefault();
              h.el.scrollIntoView({
                behavior: matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth",
              });
              history.replaceState(null, "", `#${h.id}`);
            }}
            className={cn(
              "block py-[3px] text-[13px] leading-[1.4] text-subtle hover:text-foreground",
              h.level === 3 && "pl-3",
              active === h.id && "text-foreground",
            )}
          >
            {h.text}
          </a>
        ))}
      </nav>
    </>
  );
}
