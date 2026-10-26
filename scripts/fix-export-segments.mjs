// Contorno para o export estático do Next 16.4: o build grava os payloads de prefetch
// em pastas (`__next.$d$slug/__PAGE__.txt`), mas o navegador pede o arquivo com pontos
// (`__next.$d$slug.__PAGE__.txt`). Sem esta cópia, o prefetch das rotas dinâmicas dá 404.
import fs from "node:fs";
import path from "node:path";

const OUT = path.resolve("out");
let copied = 0;

function walk(dir) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (!entry.isDirectory()) continue;
    if (entry.name.startsWith("__next.")) flatten(full, dir, entry.name);
    else walk(full);
  }
}

function flatten(dir, parent, prefix) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    const name = `${prefix}.${entry.name}`;
    if (entry.isDirectory()) flatten(full, parent, name);
    else {
      fs.copyFileSync(full, path.join(parent, name));
      copied++;
    }
  }
}

walk(OUT);
console.log(`fix-export-segments: ${copied} arquivos de prefetch copiados`);
