// Pomiar obwiedni znaku widocznego w trzech plikach SVG.
// Odtwarza tablicę OBWIEDNIE z _robocze/narzedzia/zloz-palete.py.
// Uruchomienie: node _robocze/narzedzia/zmierz-znak.mjs
// Playwright jest zainstalowany globalnie, a NODE_PATH nie dziala dla modulow ESM
// (Node ignoruje te zmienna przy import), wiec sciezka musi byc bezwzgledna.
// Import domyslny plus destrukturyzacja, bo pakiet jest CommonJS i nie ma
// nazwanego eksportu chromium.
import pw from '/opt/node22/lib/node_modules/playwright/index.js';
const { chromium } = pw;
import fs from 'node:fs';
import path from 'node:path';

const ROOT = path.resolve(import.meta.dirname, '../..');
const PLIKI = ['logo_irin_poziom.svg', 'logo_irin_pion.svg', 'logo_irin_sygnet.svg'];

const b = await chromium.launch();
const p = await b.newPage();
for (const nazwa of PLIKI) {
  await p.setContent('<body style="margin:0">' +
    fs.readFileSync(path.join(ROOT, nazwa), 'utf8') + '</body>');
  const w = await p.evaluate(() => {
    const svg = document.querySelector('svg');
    const vb = svg.viewBox.baseVal;
    let x0 = Infinity, y0 = Infinity, x1 = -Infinity, y1 = -Infinity, n = 0;
    for (const el of svg.querySelectorAll('path,polygon,rect,circle,ellipse,polyline,line')) {
      const cs = getComputedStyle(el);
      if (cs.fill === 'none' && cs.stroke === 'none') continue;  // przezroczysty prostokąt tła
      const bb = el.getBBox();
      if (bb.width === 0 && bb.height === 0) continue;
      x0 = Math.min(x0, bb.x); y0 = Math.min(y0, bb.y);
      x1 = Math.max(x1, bb.x + bb.width); y1 = Math.max(y1, bb.y + bb.height); n++;
    }
    return { vbW: vb.width, vbH: vb.height, x0, y0, x1, y1, n };
  });
  const szer = w.x1 - w.x0, wys = w.y1 - w.y0;
  console.log(`${nazwa}:`);
  console.log(`  viewBox   ${w.vbW} x ${w.vbH}`);
  console.log(`  obwiednia [${w.x0.toFixed(3)}, ${w.y0.toFixed(3)}, ` +
              `${szer.toFixed(3)}, ${wys.toFixed(3)}]  (${w.n} kształtów)`);
  console.log(`  współczynnik pola ${(szer / w.vbW).toFixed(3)}`);
}
await b.close();
