import { isValidElement, type ReactNode } from "react";

/** Texto puro de uma árvore React (usado para ler o conteúdo de blocos de código do MDX). */
export function nodeText(node: ReactNode): string {
  if (node == null || typeof node === "boolean") return "";
  if (typeof node === "string" || typeof node === "number") return String(node);
  if (Array.isArray(node)) return node.map(nodeText).join("");
  if (isValidElement<{ children?: ReactNode }>(node)) return nodeText(node.props.children);
  return "";
}
