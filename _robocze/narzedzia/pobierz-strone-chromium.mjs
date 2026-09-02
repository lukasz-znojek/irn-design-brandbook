import { chromium } from 'playwright';
import fs from 'fs';
// Chromium w sandboxie nie czyta zmiennych HTTPS_PROXY, więc proxy podajemy jawnie (wg /root/.ccr/README.md).
const browser = await chromium.launch({ headless: true, proxy: { server: process.env.HTTPS_PROXY }, args: ['--disable-features=PostQuantumKyber,UseMLKEM,EncryptedClientHello','--disable-http2','--disable-quic','--ignore-certificate-errors','--ssl-version-max=tls1.2'] });
const ctx = await browser.newContext({
  userAgent: 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128 Safari/537.36',
  acceptDownloads: true, ignoreHTTPSErrors: true, locale: 'pl-PL',
});
const page = await ctx.newPage();
const [url, outHtml, pdfUrl, outPdf] = process.argv.slice(2);
await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 }).catch(e => console.error('goto:', e.message));
await page.waitForTimeout(8000);
const html = await page.content();
fs.writeFileSync(outHtml, html);
console.log('title:', await page.title(), 'len:', html.length);
const links = await page.$$eval('a[href]', as => as.map(a => [a.textContent.trim().replace(/\s+/g, ' ').slice(0, 90), a.href]));
const hits = links.filter(([t, h]) => /regulamin|za[lł][aą]cznik|\.pdf|\.docx/i.test(t + h));
for (const h of hits.slice(0, 120)) console.log(h[0], '|', h[1]);
if (pdfUrl) {
  const resp = await ctx.request.get(pdfUrl, { timeout: 60000 });
  console.log('pdf status:', resp.status(), resp.headers()['content-type']);
  fs.writeFileSync(outPdf, await resp.body());
}
await browser.close();
