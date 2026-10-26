(function(){
const $=(s,r=document)=>r.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];
const pages=$$('.page'),ids=pages.map(p=>p.dataset.id);
const toast=$('#toast');let tt;
function say(m){toast.textContent=m;toast.classList.add('on');clearTimeout(tt);tt=setTimeout(()=>toast.classList.remove('on'),1600)}
async function copy(t,msg){try{await navigator.clipboard.writeText(t)}catch(e){const a=document.createElement('textarea');a.value=t;a.style.position='fixed';a.style.opacity='0';document.body.appendChild(a);a.select();try{document.execCommand('copy')}catch(_){}a.remove()}say(msg||'Copiado')}
// theme
try{const t=localStorage.getItem('nd-theme');if(t)document.documentElement.dataset.theme=t}catch(e){}
$('.theme-btn').addEventListener('click',()=>{const d=document.documentElement;d.dataset.theme=d.dataset.theme==='light'?'dark':'light';try{localStorage.setItem('nd-theme',d.dataset.theme)}catch(e){}});
// mobile nav
const mb=$('.menu-btn');mb.addEventListener('click',()=>{const o=document.body.classList.toggle('nav-open');mb.setAttribute('aria-expanded',o)});
// router
let obs;
function show(id){
 if(!ids.includes(id))id='inicio';
 pages.forEach(p=>p.hidden=p.dataset.id!==id);
 const pg=$('#pg-'+id);document.title=pg.dataset.title+' · Norden UI KIT';
 $$('.side a').forEach(a=>{if(a.dataset.id===id){a.setAttribute('aria-current','page');const d=a.closest('details');if(d)d.open=true}else a.removeAttribute('aria-current')});
 document.body.classList.remove('nav-open');mb.setAttribute('aria-expanded','false');
 // toc
 const hs=$$('.prose h2, .prose h3',pg),toc=$('#toc');toc.innerHTML='';
 hs.forEach(h=>{const a=document.createElement('a');a.href='#'+id;a.textContent=h.childNodes[0].textContent.trim();a.className=h.tagName==='H3'?'l3':'';a.addEventListener('click',e=>{e.preventDefault();h.scrollIntoView({behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth'})});a._h=h;toc.appendChild(a)});
 if(obs)obs.disconnect();
 obs=new IntersectionObserver(es=>{es.forEach(e=>{if(e.isIntersecting){$$('#toc a').forEach(a=>a.classList.toggle('on',a._h===e.target))}})},{rootMargin:'-70px 0px -70% 0px'});hs.forEach(h=>obs.observe(h));
 // prev / next
 const i=ids.indexOf(id),pn=$('.pn',pg);pn.innerHTML='';
 const mk=(j,cls,lab)=>{if(j<0||j>=pages.length)return;const p=pages[j],a=document.createElement('a');a.href='#'+p.dataset.id;a.className=cls;a.innerHTML='<small>'+lab+'</small><span></span>';a.querySelector('span').textContent=p.dataset.title;pn.appendChild(a)};
 mk(i-1,'pv','Anterior');mk(i+1,'nx','Próxima');
 window.scrollTo(0,0);
}
const cur=()=>decodeURIComponent((location.hash||'#inicio').slice(1));
window.addEventListener('hashchange',()=>show(cur()));
show(cur());
// copy actions
document.addEventListener('click',e=>{
 const all=e.target.closest('.copy-all');if(all){const f=all.closest('.prompt');copy($$('pre',f).map(p=>p.textContent).join('\n\n'),'Prompt copiado');return}
 const seg=e.target.closest('.copy-seg');if(seg){copy($('pre',seg.closest('.pseg')).textContent,'Bloco copiado');return}
 const tok=e.target.closest('.tok');if(tok){copy(tok.textContent,'Token copiado: '+tok.textContent)}
});
// search
const norm=s=>s.normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();
const idx=pages.map(p=>({id:p.dataset.id,t:p.dataset.title,g:p.dataset.group,raw:p.textContent.replace(/\s+/g,' ').trim()})).map(o=>Object.assign(o,{n:norm(o.raw),nt:norm(o.t)}));
const box=$('#search'),q=$('#q'),res=$('#results');let sel=0,items=[];
function open(){box.hidden=false;q.value='';render('');setTimeout(()=>q.focus(),10)}
function close(){box.hidden=true}
function esc(s){return s.replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]))}
function render(v){
 const terms=norm(v).split(/\s+/).filter(Boolean);
 if(!terms.length){items=idx.filter(o=>['inicio','ia','cores','adaptar-marca','componentes','skill'].includes(o.id))}
 else{items=idx.filter(o=>terms.every(t=>o.n.includes(t))).map(o=>({o,s:terms.reduce((a,t)=>a+(o.nt.includes(t)?10:0)+(o.n.split(t).length-1),0)})).sort((a,b)=>b.s-a.s).map(x=>x.o).slice(0,14)}
 sel=0;res.innerHTML='';
 if(!items.length){res.innerHTML='<li class="r-empty">Nada encontrado. Tente outro termo, como “preço”, “token” ou “prompt”.</li>';return}
 items.forEach((o,i)=>{let snip='';if(terms.length){const k=o.n.indexOf(terms[0]);const st=Math.max(0,k-50);snip=esc(o.raw.slice(st,st+140));terms.forEach(t=>{snip=snip.replace(new RegExp('('+t.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+')','gi'),'<mark>$1</mark>')})}
  const li=document.createElement('li');li.innerHTML='<a href="#'+o.id+'" role="option"><span class="r-t"></span><span class="r-g"></span>'+(snip?'<span class="r-s">'+(st=>st)(snip)+'</span>':'')+'</a>';$('.r-t',li).textContent=o.t;$('.r-g',li).textContent=o.g;res.appendChild(li)});
 mark();
}
function mark(){$$('#results a').forEach((a,i)=>a.setAttribute('aria-selected',i===sel))}
q.addEventListener('input',()=>render(q.value));
q.addEventListener('keydown',e=>{const n=items.length;if(e.key==='ArrowDown'){sel=(sel+1)%n;mark();e.preventDefault()}else if(e.key==='ArrowUp'){sel=(sel-1+n)%n;mark();e.preventDefault()}else if(e.key==='Enter'&&n){location.hash=items[sel].id;close()}});
res.addEventListener('click',e=>{if(e.target.closest('a'))close()});
box.addEventListener('click',e=>{if(e.target===box)close()});
$('.search-btn').addEventListener('click',open);
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&!box.hidden){close();return}const tag=(e.target.tagName||'').toLowerCase();if((e.key==='/'&&!['input','textarea'].includes(tag))||((e.ctrlKey||e.metaKey)&&e.key.toLowerCase()==='k')){e.preventDefault();open()}});
// brand simulator
const sim=$('#sim');
if(sim){
 const hx=h=>{h=h.replace('#','');if(h.length===3)h=[...h].map(c=>c+c).join('');return /^[0-9a-f]{6}$/i.test(h)?[0,2,4].map(i=>parseInt(h.slice(i,i+2),16)/255):null};
 const toHex=c=>'#'+c.map(v=>Math.round(Math.max(0,Math.min(1,v))*255).toString(16).padStart(2,'0')).join('').toUpperCase();
 const mix=(a,b,t)=>a.map((v,i)=>v+(b[i]-v)*t);
 const lum=c=>{const f=v=>v<=.03928?v/12.92:Math.pow((v+.055)/1.055,2.4);const[r,g,b]=c.map(f);return .2126*r+.7152*g+.0722*b};
 const ct=(a,b)=>{const x=lum(a),y=lum(b);return (Math.max(x,y)+.05)/(Math.min(x,y)+.05)};
 const W=[1,1,1],K=[0,0,0],DARK=hx('1C1C21');
 function run(v){const d=hx(v);if(!d)return;
  const hover=mix(d,K,lum(d)<.03?.45:.14),subtle=mix(d,W,.92);let text=d,s=0;while(Math.min(ct(text,W),ct(text,subtle))<4.5&&s<40){s++;text=mix(d,K,s*.025)}
  const on=ct(W,d)>=ct(DARK,d)?W:DARK;
  const roles=[['default',d,ct(on,d),'on-color sobre ele'],['hover',hover,ct(on,hover),'on-color sobre ele'],['subtle',subtle,ct(text,subtle),'text sobre ele'],['text',text,ct(text,W),'sobre branco'],['on-color',on,ct(on,d),'sobre o default']];
  $('#sim-roles').innerHTML=roles.map(([n,c,r,l])=>'<div class="role"><div class="role-sw" style="--sw:'+toHex(c)+'"></div><p class="rn">'+n+'</p><p class="rv">'+toHex(c)+'</p><p class="rc'+(r<4.5?' bad':'')+'">'+r.toFixed(2).replace('.',',')+':1 '+l+'</p></div>').join('');
  const pv=$('#sim-prev');pv.style.setProperty('--p-default',toHex(d));pv.style.setProperty('--p-hover',toHex(hover));pv.style.setProperty('--p-subtle',toHex(subtle));pv.style.setProperty('--p-text',toHex(text));pv.style.setProperty('--p-on',toHex(on));
  const notes=[];if(ct(on,d)<4.5)notes.push('O texto do botão fica abaixo de 4,5:1: registre a exceção ou use a versão “text” como fundo do botão.');if(toHex(text)!==toHex(d))notes.push('A cor não tem contraste como texto: links e preço usam a versão escurecida.');
  $('#sim-note').textContent=notes.join(' ')||'Todos os pares passam no contraste mínimo.';
 }
 const ci=$('#sim-color'),ti=$('#sim-hex');
 ci.addEventListener('input',()=>{ti.value=ci.value.toUpperCase();run(ci.value)});
 ti.addEventListener('input',()=>{const h=hx(ti.value);if(h){ci.value=toHex(h);run(ti.value)}});
 run(ci.value);
}
})();
