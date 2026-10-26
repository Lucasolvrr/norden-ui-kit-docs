# Regras editoriais

- Português do Brasil, sentence case, voz ativa, frases curtas. Sem jargão sem explicação.
- Explique o conceito antes de pedir a aplicação. Cada assunto: o que é, por que existe, como foi pensado no kit, como usar (Figma e IA), como adaptar.
- Aspas tipográficas “ ” e apóstrofo ’ em todo texto lido. Aspas retas só em código.
- Dados do kit só do Figma. Fonte e data da exportação ficam registradas (página Manutenção). Se não confirmado: selo Pendente de validação.
- Diferencie: Implementado × Recomendação × Proposta × Pendente.
- Prompts: específicos do contexto, com onde (arquivo/frame), com o quê (componentes e tokens pelo nome exato), conteúdo real, o que não fazer e entrega verificável (print, lista do que mudou). Divida em blocos `## ` quando longo.
- Prompts de alteração pedem plano antes de executar quando há decisão em aberto, e escopo fechado em correções.
- Exemplos de adaptação podem citar o caso Stok Center (vermelho #ED1D24, grafite #414042, amarelo #FFF200; texto do vermelho #D51A20; on-color 4,37:1 aceito como decisão de marca; fonte D-DIN-PRO indisponível para a IA). Não inventar outros clientes.
- Numeração visual só para sequências reais (etapas). Nada de rótulos decorativos em caixa alta.
- Ao adicionar ou mudar algo: atualize changelog (versão e data), pendências da Manutenção e, se for regra, a página da Skill.

## Fatos do kit usados no conteúdo (v0.4, exportação de 26/10/2026)
- Collections: Brand (46, editada por projeto, sem escopo), Primitives (alpha preto 8/16/48 e escala de raio; oculta), Color (85 semânticos, mode Light), Shape (modes 10px padrão, None, 6px, 16px, 24px, Full; 8 tokens radius/*), Dimension (spacing 0–128 e size/control xs 32, sm 40, md 48, lg 56), Responsive (Mobile/Tablet/Desktop: viewport 393/768/1440, margin 16/32/40, header-padding-top 240/120/160 provisório, tamanhos de título), Prototype (cart/quantity, cart/quantity-label, cart/has-items; modes Empty/With items).
- Fonte padrão Rethink Sans; pesos por variável (o nome do peso muda entre fontes).
- Botões: Default, Hover (desktop, mais escuro), Disabled; sem Focus/Pressed. Inputs com texto 16px. Ícones Phosphor.
- Regra: todo componente com descrição no campo Component information.
- Ausentes: Radio, Textarea, padrão PDP, checkout, estados vazios/carregamento; versões desktop.
- Componentes sem descrição: Google, Facebook, Navigation/Bottom Nav, Navigation/Bottom Nav Item, Footer/Link.
- Referências antigas a limpar: Button, Slider, Filters (Drawer), Icon Button / Favorite, "angulo-direito (1) 2", Text Field, filtros e faixas na página Layout Mobile.
- Existe a skill `norden-ui-kit` (empacotada) com tokens, componentes, mapeamento wireframe → componente e script de paleta; a página Skill do site cita isso.
