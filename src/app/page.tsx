import type { Metadata } from "next";
import { DocPage } from "@/components/layout/doc-page";
import { site } from "@/lib/site";

export const metadata: Metadata = { title: { absolute: site.title } };

export default function Home() {
  return <DocPage slug="inicio" />;
}
