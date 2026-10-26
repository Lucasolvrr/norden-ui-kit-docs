import type { Metadata } from "next";
import { Geist_Mono, Rethink_Sans } from "next/font/google";
import { ThemeProvider } from "next-themes";
import { Toaster } from "@/components/ui/sonner";
import { SiteHeader } from "@/components/layout/site-header";
import { SidebarNav } from "@/components/layout/sidebar-nav";
import { TableOfContents } from "@/components/layout/table-of-contents";
import { site } from "@/lib/site";
import "./globals.css";

const rethink = Rethink_Sans({ variable: "--font-rethink", subsets: ["latin"] });
const geistMono = Geist_Mono({ variable: "--font-geist-mono", subsets: ["latin"] });

export const metadata: Metadata = {
  title: { default: site.title, template: `%s · ${site.name}` },
  description: site.description,
};

const stickyColumn = "sticky top-(--header-h) h-[calc(100vh-var(--header-h))] overflow-auto";

export default function RootLayout({ children }: LayoutProps<"/">) {
  return (
    <html lang="pt-BR" className={`${rethink.variable} ${geistMono.variable}`} suppressHydrationWarning>
      <body>
        <ThemeProvider attribute="class" defaultTheme="dark" enableSystem={false} storageKey="nd-theme" disableTransitionOnChange>
          <SiteHeader />
          <div className="mx-auto grid max-w-[1480px] grid-cols-[minmax(0,1fr)] min-[901px]:grid-cols-[248px_minmax(0,1fr)] min-[1241px]:grid-cols-[264px_minmax(0,1fr)_224px]">
            <aside className={`${stickyColumn} hidden border-r border-line-2 py-6 pr-4 pl-5 pb-12 [scrollbar-width:thin] min-[901px]:block`}>
              <SidebarNav />
            </aside>
            <main id="main" className="min-w-0 px-5 pt-7 pb-20 min-[901px]:px-14 min-[901px]:pt-10 min-[901px]:pb-24">
              {children}
            </main>
            <aside aria-label="Nesta página" className={`${stickyColumn} hidden py-10 pr-5 pl-2 min-[1241px]:block`}>
              <TableOfContents />
            </aside>
          </div>
          <Toaster position="bottom-center" />
        </ThemeProvider>
      </body>
    </html>
  );
}
