import type { MDXComponents } from "mdx/types";
import Link from "next/link";
import { Callout } from "@/components/docs/callout";
import { Prompt, PromptNote } from "@/components/docs/prompt";
import { StatusBadge } from "@/components/docs/status-badge";
import {
  Changelog,
  ChangelogEntry,
  Compare,
  CompareItem,
  Detail,
  Details,
  Flow,
  FlowStep,
  HeadingNote,
  Layer,
  Layers,
  MiniTitle,
  Step,
  Steps,
  Swatch,
  TypeSample,
} from "@/components/docs/blocks";
import { BrandColors, ColorTokens, SpacingScale } from "@/components/docs/tokens";
import { Token } from "@/components/docs/token-button";
import { BrandSimulator } from "@/components/docs/brand-simulator";
import { ComponentIndex } from "@/components/docs/component-index";

// Componentes disponíveis em todos os arquivos MDX de content/ (ver docs/conteudo.md).
const components: MDXComponents = {
  a: ({ href = "", ...props }) =>
    href.startsWith("/") ? <Link href={href} {...props} /> : <a href={href} {...props} />,
  table: (props) => (
    <div className="docs-table">
      <table {...props} />
    </div>
  ),
  Badge: StatusBadge,
  Callout,
  Prompt,
  PromptNote,
  Steps,
  Step,
  Details,
  Detail,
  Compare,
  CompareItem,
  Layers,
  Layer,
  Flow,
  FlowStep,
  Changelog,
  ChangelogEntry,
  MiniTitle,
  HeadingNote,
  Swatch,
  TypeSample,
  Token,
  BrandColors,
  ColorTokens,
  SpacingScale,
  BrandSimulator,
  ComponentIndex,
};

export function useMDXComponents(): MDXComponents {
  return components;
}
