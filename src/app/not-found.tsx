import Link from "next/link";

export default function NotFound() {
  return (
    <div className="max-w-[760px]">
      <h1 className="text-4xl font-semibold tracking-[-0.025em] text-strong">Página não encontrada</h1>
      <p className="mt-3 text-[17px] text-muted-foreground">
        Este endereço não existe na documentação. Use a busca ou volte para o <Link href="/" className="underline underline-offset-[3px]">início</Link>.
      </p>
    </div>
  );
}
