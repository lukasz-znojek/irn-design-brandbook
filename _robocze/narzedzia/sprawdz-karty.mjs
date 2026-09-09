// Otwiera osiem kart w Chromium i sprawdza, że tokeny rozwiązują się do wartości
// z palety, że nie ma tokenów stanu i że nie ma błędów konsoli ani HTTP.
// Tokeny czyta przez PRÓBNIK, bo getPropertyValue zwraca zadeklarowane var(...),
// a nie rozwiązaną barwę.
import pw from '/opt/node22/lib/node_modules/playwright/index.js';
const { chromium } = pw;
import http from 'node:http'; import fs from 'node:fs'; import path from 'node:path';
const ROOT = '_robocze/ds-bundle';
const typy = {'.css':'text/css','.html':'text/html; charset=utf-8','.svg':'image/svg+xml','.woff2':'font/woff2'};
const srv = http.createServer((q,s)=>{ const f=path.join(ROOT, decodeURIComponent(q.url.split('?')[0]));
  if(!fs.existsSync(f)||fs.statSync(f).isDirectory()){s.writeHead(404);return s.end();}
  s.writeHead(200,{'content-type':typy[path.extname(f)]||'text/plain'});
  fs.createReadStream(f).pipe(s); });
await new Promise(r=>srv.listen(8104,r));
const karty=[]; (function chodz(dir){ for(const e of fs.readdirSync(path.join(ROOT,dir),{withFileTypes:true})){
  const s=path.posix.join(dir,e.name); if(e.isDirectory())chodz(s); else if(e.name.endsWith('.html'))karty.push(s);}})('components');
const b = await chromium.launch(); const p = await b.newPage(); let zle=0;
for (const k of karty.sort()) {
  const bledy=[];
  const onC=m=>{if(m.type()==='error')bledy.push(m.text())};
  const onR=r=>{if(r.status()>=400)bledy.push('HTTP '+r.status()+' '+r.url())};
  p.on('console',onC); p.on('response',onR);
  await p.goto('http://127.0.0.1:8104/'+k,{waitUntil:'networkidle'});
  const w = await p.evaluate(async () => {
    await document.fonts.ready;
    const probnik = document.createElement('div');
    document.body.appendChild(probnik);
    const rozwiaz = nazwa => { probnik.style.color=''; probnik.style.color=`var(${nazwa})`;
      return getComputedStyle(probnik).color; };
    // Token stanu istnieje wtedy i tylko wtedy, gdy jest ZADEKLAROWANY na korzeniu.
    // Rozwiazywanie przez color() nie nadaje sie: color: var(--niezdefiniowany) jest
    // deklaracja nieprawidlowa, wiec element dziedziczy barwe tekstu i wyglada na token.
    const csRoot = getComputedStyle(document.documentElement);
    const stan = ['--irin-r-success','--irin-r-warning','--irin-r-error']
      .filter(n => csRoot.getPropertyValue(n).trim() !== '');
    const wynik = { surface: rozwiaz('--irin-r-surface'), text: rozwiaz('--irin-r-text'),
      dziedzina: rozwiaz('--irin-r-dziedzina'), tint: rozwiaz('--irin-r-tint-dziedzina'),
      stanow: stan.length, kroj: getComputedStyle(document.body).fontFamily.split(',')[0],
      karta: getComputedStyle(document.querySelector('.karta')).backgroundColor };
    probnik.remove(); return wynik;
  });
  p.off('console',onC); p.off('response',onR);
  const ok = w.surface==='rgb(247, 243, 233)' && w.text==='rgb(7, 9, 12)'
          && w.dziedzina==='rgb(19, 34, 70)' && w.tint==='rgb(220, 218, 213)'
          && w.stanow===0 && w.kroj==='Manrope' && bledy.length===0;
  if(!ok){ zle++; console.log('   szczegóły:', JSON.stringify(w), bledy); }
  console.log(`${ok?'OK  ':'ZŁE '} ${k.split('/').pop().padEnd(30)} surface=${w.surface} dziedzina=${w.dziedzina} tint=${w.tint} tokenów-stanu=${w.stanow} kroj=${w.kroj} błędy=${bledy.length}`);
}
console.log(`\nkart: ${karty.length}, złych: ${zle}`);
await b.close(); srv.close(); process.exit(zle?1:0);
