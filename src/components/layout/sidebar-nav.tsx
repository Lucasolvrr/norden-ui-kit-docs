"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { ChevronRight } from "lucide-react";
import { Collapsible, CollapsibleContent, CollapsibleTrigger } from "@/components/ui/collapsible";
import { getNavGroups } from "@/lib/nav";
import { cn } from "@/lib/utils";

const groups = getNavGroups();

const normalize = (p: string) => (p.length > 1 ? p.replace(/\/$/, "") : p);

function NavLink({ href, title, active, nested }: { href: string; title: string; active: boolean; nested?: boolean }) {
  return (
    <Link
      href={href}
      aria-current={active ? "page" : undefined}
      className={cn(
        "block rounded-md px-2.5 py-[5px] text-sm leading-[1.45] text-muted-foreground hover:bg-accent hover:text-foreground",
        active && "bg-muted font-medium text-strong hover:bg-muted hover:text-strong",
        nested && "ml-3 rounded-l-none border-l pl-3",
      )}
    >
      {title}
    </Link>
  );
}

export function SidebarNav() {
  const pathname = normalize(usePathname());

  return (
    <nav aria-label="Navegação da documentação">
      {groups.map((g) => (
        <div key={g.title} className="mb-[22px]">
          <p className="mb-1.5 ml-2.5 text-[12.5px] font-semibold text-foreground">{g.title}</p>
          {g.items.map((i) => (
            <NavLink key={i.href} {...i} active={pathname === i.href} />
          ))}
          {g.subgroups.map((s) => {
            const containsActive = s.items.some((i) => pathname === i.href);
            return (
              <Collapsible key={s.title} defaultOpen={containsActive} className="group/sub">
                <CollapsibleTrigger className="flex w-full items-center justify-between rounded-md px-2.5 py-[5px] text-sm text-muted-foreground hover:bg-accent hover:text-foreground">
                  {s.title}
                  <ChevronRight className="size-3.5 text-subtle transition-transform group-data-[state=open]/sub:rotate-90" />
                </CollapsibleTrigger>
                <CollapsibleContent>
                  {s.items.map((i) => (
                    <NavLink key={i.href} {...i} active={pathname === i.href} nested />
                  ))}
                </CollapsibleContent>
              </Collapsible>
            );
          })}
        </div>
      ))}
    </nav>
  );
}
