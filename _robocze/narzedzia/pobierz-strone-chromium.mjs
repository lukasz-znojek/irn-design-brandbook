// Pobiera stronę (albo plik, np. PDF) przez headless Chromium — dla adresów,
// które zwracają stronę zabezpieczenia (np. Incapsula) na zwykłe żądanie `curl`,
// bo wymagają wykonania JavaScriptu albo ciasteczka wystawianego po jego wykonaniu.
//
// Użycie:
//   node pobierz-strone-chromium.mjs <url> <plik-wyjsciowy> [--pdf]
//
// Bez `--pdf`: zapisuje surowe ciało odpowiedzi (HTML, albo plik binarny typu
// PDF, jeśli adres wskazuje bezpośrednio na PDF) pod `plik-wyjsciowy`.
// Z `--pdf`: renderuje stronę i drukuje ją do PDF (`page.pdf()`) — przydatne
// tylko dla stron HTML, nie dla adresów, które już serwują PDF.
//
// UWAGA: to narzędzie nie omija blokad na poziomie polityki sieciowej środowiska
// (serwer pośredniczący/proxy) — Chromium w tym środowisku łączy się przez ten
// sam serwer co `curl` (zmienna środowiskowa HTTPS_PROXY). Jeśli `curl` dostaje
// `connect_rejected`/403 na CONNECT, to narzędzie dostanie
// `net::ERR_TUNNEL_CONNECTION_FAILED` — potwierdzone w sesji 2026-09-02, Etap 2.
// Ma sens tylko wtedy, gdy `curl` dochodzi do serwera (kod HTTP, nie błąd
// połączenia), ale dostaje stronę zabezpieczenia zamiast właściwej treści.
//
// Wymaga zmiennej PLAYWRIGHT_BROWSERS_PATH ustawionej na katalog z Chromium
// (w tym środowisku: /opt/pw-browsers) — ustawiona domyślnie w tej sesji.

import { chromium } from 'playwright';
import { writeFile } from 'node:fs/promises';

const [, , url, wyjscie, ...reszta] = process.argv;
const tryb = reszta.includes('--pdf') ? 'pdf' : 'raw';

if (!url || !wyjscie) {
  console.error('Użycie: node pobierz-strone-chromium.mjs <url> <plik-wyjsciowy> [--pdf]');
  process.exit(1);
}

const browser = await chromium.launch({
  executablePath: process.env.PLAYWRIGHT_CHROMIUM_PATH || '/opt/pw-browsers/chromium',
  headless: true,
});
// Ruch wychodzący w tym środowisku idzie przez serwer pośredniczący (proxy),
// który podmienia certyfikat na własny (CA: /root/.ccr/ca-bundle.crt).
// Chromium tego CA nie zna z automatu, stąd ignoreHTTPSErrors — bez tego
// każde żądanie kończy się ERR_CERT_AUTHORITY_INVALID, niezależnie od tego,
// czy docelowa domena jest w ogóle dozwolona przez politykę sieciową.
const context = await browser.newContext({ ignoreHTTPSErrors: true });
const page = await context.newPage();

try {
  const odpowiedz = await page.goto(url, { waitUntil: 'networkidle', timeout: 30000 });
  const status = odpowiedz ? odpowiedz.status() : null;
  const typTresci = odpowiedz ? odpowiedz.headers()['content-type'] : null;
  console.log(`HTTP ${status} — ${typTresci}`);

  if (tryb === 'pdf') {
    await page.pdf({ path: wyjscie, format: 'A4' });
  } else {
    const cialo = await odpowiedz.body();
    await writeFile(wyjscie, cialo);
  }
  console.log(`Zapisano: ${wyjscie}`);
} catch (e) {
  console.error(`BŁĄD: ${e.message}`);
  process.exitCode = 1;
} finally {
  await browser.close();
}
