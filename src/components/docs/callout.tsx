import { cn } from "@/lib/utils";

const BORDER = {
  info: "border-l-st-rec",
  warn: "border-l-st-pend",
  pending: "border-l-st-prop",
};

export function Callout({
  kind = "info",
  title,
  children,
}: {
  kind?: keyof typeof BORDER;
  title: string;
  children: React.ReactNode;
}) {
  return (
    <div className={cn("my-5 rounded-lg border border-l-2 bg-card px-4 py-3.5", BORDER[kind])}>
      <p className="!mt-0 !mb-1 text-sm font-semibold text-strong">{title}</p>
      <div className="[&>p]:!my-1 [&>ul]:!my-1">{children}</div>
    </div>
  );
}
