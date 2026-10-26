"use client";

import { toast } from "sonner";
import { cn } from "@/lib/utils";

export async function copyText(text: string, message = "Copiado") {
  try {
    await navigator.clipboard.writeText(text);
  } catch {
    const area = document.createElement("textarea");
    area.value = text;
    area.style.position = "fixed";
    area.style.opacity = "0";
    document.body.appendChild(area);
    area.select();
    try {
      document.execCommand("copy");
    } catch {}
    area.remove();
  }
  toast(message);
}

export function CopyButton({
  text,
  message,
  className,
  children,
  ...props
}: { text: string; message?: string } & React.ComponentProps<"button">) {
  return (
    <button
      type="button"
      onClick={() => copyText(text, message)}
      className={cn(
        "rounded-md border bg-muted px-2.5 py-1 text-[12.5px] whitespace-nowrap text-muted-foreground hover:border-subtle hover:text-foreground",
        className,
      )}
      {...props}
    >
      {children}
    </button>
  );
}
