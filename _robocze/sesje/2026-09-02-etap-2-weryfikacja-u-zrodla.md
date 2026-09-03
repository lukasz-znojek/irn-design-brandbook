# Sesja 2026-09-02 - Etap 2, weryfikacja u źródła (próba pobrania dokumentów PARP)

## Zlecenie

Pobranie trzech plików PDF z PARP (aktualny Regulamin BUR, Załącznik nr 2 - Karta Usługi, Załącznik nr 12 - Zaświadczenie), sprawdzenie, czy po 6 lipca 2026 nie ma nowszej wersji regulaminu, i wpisanie odczytu do `bur.md` oraz kart specyfikacji dla pozycji 1-3 z `01-baza-wiedzy/prawo/weryfikacja-u-zrodla.md`. Przy nadmiarze czasu: pozycja 7 (operator PSF w świętokrzyskim, `it.kielce.pl`) i pozycja 8 (Księga Tożsamości Wizualnej FE, `gov.pl/web/fundusze-regiony`).

## Rozbieżność wobec briefu, stwierdzona na starcie

Brief tej sesji zakładał istnienie trzech plików z wcześniejszej sesji: `_robocze/sesje/2026-09-02-etap-2-weryfikacja-u-zrodla.md` (ten plik - nie istniał przed tą sesją), `_robocze/narzedzia/pobierz-strone-chromium.mjs` i `_robocze/narzedzia/tekst-z-pdf.py`, a także sekcji „Adresy plików PARP do pobrania ręcznie” w `weryfikacja-u-zrodla.md`. Żaden z tych czterech elementów nie istniał w repozytorium - ani na `main`, ani na gałęzi `claude/etap-2-weryfikacja-zrodla-v05npm` (identyczna z `main`, zero dodatkowych commitów). Brief opisywał też wcześniejszy wynik próby pobrania jako stronę zabezpieczenia Incapsula (HTTP 200, ok. 200 B, skrypt `_Incapsula_Resource`) - ten opis nigdzie w repozytorium się nie znalazł. Materiał, na którym opierał się brief, nie został scommitowany w żadnej wcześniejszej sesji; ta sesja nie odtwarzała go z pamięci, tylko zmierzyła stan sieci od nowa.

## Co zmierzono

Trzy niezależne narzędzia, ten sam wniosek:

| Narzędzie | Domena testowa | Wynik |
|---|---|---|
| `curl` | `uslugirozwojowe.parp.gov.pl`, `parp.gov.pl`, `www.parp.gov.pl`, `dziennikustaw.gov.pl`, `isap.sejm.gov.pl`, `bur-subregion.pl`, `it.kielce.pl`, `gov.pl` | `connect_rejected` - proxy: „gateway answered 403 to CONNECT (policy denial)” |
| Chromium (Playwright) | `uslugirozwojowe.parp.gov.pl` | `net::ERR_TUNNEL_CONNECTION_FAILED` (ta sama trasa sieciowa co `curl`) |
| `WebFetch` (osobna infrastruktura) | `uslugirozwojowe.parp.gov.pl`, `dziennikustaw.gov.pl`, `it.kielce.pl`, `www.gov.pl` | `EGRESS_BLOCKED` - „Access to [domena] is blocked by the network egress proxy” |

Kontrola skali: `example.com` i `google.com` też kończą się `connect_rejected`; `github.com` łączy się (HTTP 400 na pustej ścieżce - odpowiedź serwera, nie blokada). Wniosek: to ogólna polityka sieciowa środowiska (lista dozwolonych domen - npm, PyPI, GitHub, API Anthropic i kilka innych z `no_proxy`), z domyślną odmową dla reszty internetu - nie zabezpieczenie konkretnej strony PARP. Żadne dostępne narzędzie nie mogło tego obejść; zgodnie z poleceniem sesja nie próbowała.

Falsyfikator zapisany w `weryfikacja-u-zrodla.md`: pomiar `curl -sS http://127.0.0.1:<port>/__agentproxy/status` w nowej sesji pokazujący którąś z tych domen bez `connect_rejected`, albo świadome rozszerzenie listy dozwolonych domen przez foundera.

## Co zrobiono mimo blokady

- **`_robocze/narzedzia/tekst-z-pdf.py`** (nowy plik) - ekstrakcja tekstu z PDF przez `pypdf`, z numerem strony przy każdym fragmencie. Zmierzone w tej sesji: `pip3` **działa** w tym środowisku (wbrew założeniu brief"u „brak poppler i pip") - `pip3 install pypdf` się powiódł, ale sam import `pypdf` padał przez zepsutą zależność `cryptography` (brak `_cffi_backend`); naprawa: `pip3 install --force-reinstall cffi`. Skrypt robi tę naprawę automatycznie i został przetestowany na wygenerowanym pliku PDF (biblioteka `fpdf2`) - poprawnie zwrócił wpisany tekst z numerem strony.
- **`_robocze/narzedzia/pobierz-strone-chromium.mjs`** (nowy plik) - pobranie strony/pliku przez headless Chromium, dla przypadków gdy `curl` trafia na wyzwanie JS-owe zamiast zwykłej blokady sieciowej. Przetestowany na `github.com` (działa; wymagał `ignoreHTTPSErrors: true`, bo serwer pośredniczący w tym środowisku podmienia certyfikat na własny) i na zablokowanej domenie PARP (poprawnie zgłasza `ERR_TUNNEL_CONNECTION_FAILED`, ten sam mechanizm co `curl`, więc narzędzie nie omija blokady polityki sieciowej - tylko wyzwania na poziomie strony).
- **`01-baza-wiedzy/prawo/weryfikacja-u-zrodla.md`** - dodana kolumna Status do tabeli (pozycje 1, 2, 3, 7, 8: **niesprawdzone**, z odsyłaczem do sekcji z dokładną diagnozą; pozycje 4-6: poza zakresem tej sesji) i nowa sekcja „Co się nie udało w tej sesji” z metodologią i wnioskiem wyżej.

## Czego nie zrobiono i dlaczego (stan na koniec części 1 - część 2 niżej to zmienia)

- **`bur.md`, `karta-uslugi-bur.md`, `certyfikat.md`** - bez zmian treściowych *(nieaktualne od części 2: po dostarczeniu plików przez foundera wszystkie trzy zostały zaktualizowane)*. Żaden PDF nie został pobrany, więc nie było z czego przepisywać cytatów z numerem paragrafu; te trzy pliki już poprawnie oznaczały odpowiednie fragmenty jako niesprawdzone, z nazwanym powodem i falsyfikatorem - nadpisywanie ich samą datą kolejnej nieudanej próby nie wnosiłoby nic ponad to, co już mówi zaktualizowany `weryfikacja-u-zrodla.md`.
- **Pozycja 3** (format kodu usługi BUR) i **zadanie „sprawdź, czy po 6 lipca 2026 nie ma nowszej wersji regulaminu”** - niewykonalne bez dostępu do `uslugirozwojowe.parp.gov.pl` *(w części 2 pozycja 3 została odczytana z dostarczonych plików; pytanie o nowszą wersję regulaminu pozostaje niesprawdzone)*.
- **Zadanie 3** (pozycja 7 - regulamin ŚCITT, pozycja 8 - podręcznik FE) - te same domeny (`it.kielce.pl`, `gov.pl`) zablokowane tym samym mechanizmem; zmierzone i wpisane do tabeli statusów, treść nieodczytana.

## Gałąź

Brief harnessu tej sesji wskazywał gałąź `claude/etap-2-weryfikacja-zrodla-v05npm`; treść zlecenia w wiadomości od użytkownika wskazywała `claude/etap-2-regulamin-bur` i wyraźnie poleciła ją utworzyć z `main`. Potraktowano to jako jawne zezwolenie na odstępstwo od domyślnej gałęzi harnessu - praca poszła na `claude/etap-2-regulamin-bur`.

## Następny krok postulowany na koniec części 1 - **wykonany**, patrz część 2

Founder wkleja do czatu trzy pliki PDF: aktualny Regulamin BUR, Załącznik nr 2, Załącznik nr 12 (albo dopuszcza wymienione domeny w polityce sieciowej środowiska). Po dostarczeniu - narzędzia z tej sesji (`tekst-z-pdf.py`) są gotowe do użycia bez dodatkowego przygotowania.

## Część 2 (tego samego dnia): pliki dostarczone, pozycje 1-3 odczytane

Founder wkleił do czatu sześć plików PDF ze strony `serwis-uslugirozwojowe.parp.gov.pl/component/site/site/serwis-informacyjny-bur/#regulamin` (adres, którego ta sesja sama nie mogła osiągnąć - próba z tym konkretnym adresem dała ten sam wynik co wcześniej, `connect_rejected`/`EGRESS_BLOCKED`): Regulamin BUR oraz Załączniki 1, 2g, 3, 4 i 5. **Załącznika nr 12 wśród nich nie było.**

Odczyt (`_robocze/narzedzia/tekst-z-pdf.py`, bez błędów, każdy cytat porównany z numerem strony w PDF przed wpisaniem):
- **Regulamin BUR**, wersja obowiązująca od 5 maja 2026 r., 35 stron. § 23 „Załączniki” wymienia jako integralną część Regulaminu wyłącznie Załączniki 1-5 - to wyjaśniło brak Załącznika 12: nie zaginął, przestał istnieć w tej wersji numeracji.
- **Załącznik 2g** (Karta Usługi - usługa szkoleniowa), wersja obowiązująca **od 6 lipca 2026 r.**, 76 stron - dokładnie ta data, której brief kazał szukać. Pełna lista pól „Pole obowiązkowe" z numerami pozycji i stron przepisana do `bur.md` i skrócona do `karta-uslugi-bur.md`.
- **Załącznik 4** (Zasady funkcjonowania Dostawców Usług), wersja od 31 marca 2026 r., 21 stron, Rozdział 2 pkt 3 (s. 6-7) - tu, nie w osobnym „Załączniku 12", jest dziś ośmiopunktowa lista treści obowiązkowej zaświadczenia. Przepisana do `bur.md` i `certyfikat.md`.
- **Kod usługi**: żaden z sześciu dokumentów nie definiuje wewnętrznej struktury „numeru identyfikacyjnego Usługi rozwojowej" - to jest teraz odczytany fakt (dokumenty przeczytane, odpowiedzi w nich nie ma), nie brak dostępu. Zapis `2025/00817/PPUR` z `brandbook.dc.html` pozostaje niepotwierdzony.
- Załączniki 1 (Karta Dostawcy Usług), 3 (System Oceny Usług Rozwojowych) i 5 (Standard Usług Zdalnego Uczenia się, luty 2021) - dostarczone i zapisane w `zrodla/`, ale nieprzeczytane w tej sesji; poza zakresem pozycji 1-3.

Pliki źródłowe zapisane w `01-baza-wiedzy/prawo/zrodla/` z polską nazwą i datą wersji z okładki dokumentu. Zaktualizowane: `bur.md` (sekcje Karta Usługi, Kod usługi, Zaświadczenie, banner statusu, Źródła), `weryfikacja-u-zrodla.md` (pozycje 1-3: odczytane u źródła), `karta-uslugi-bur.md` i `certyfikat.md` (finalna lista elementów prawnie obowiązkowych, sekcje „Status weryfikacji” usunięte).

**Niesprawdzone pozostaje:** czy między 6 lipca 2026 (data na okładce Załącznika 2g) a dniem odczytu (2026-09-02) PARP opublikowała nowszą wersję - sieć nadal zablokowana, więc nie sprawdzono. Falsyfikator: publikacja nowszej daty na `uslugirozwojowe.parp.gov.pl`, albo kolejny plik od foundera z późniejszą datą na okładce.

Pozycje 7 (ŚCITT/`it.kielce.pl`) i 8 (Księga Tożsamości Wizualnej FE/`gov.pl`) - founder nie dostarczył plików dla tych domen w tej turze; pozostają niesprawdzone, zadanie 3 nie zostało domknięte.
