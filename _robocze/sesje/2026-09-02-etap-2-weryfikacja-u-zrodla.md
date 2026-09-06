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

---

## Część 3 (2026-09-06): trzy nieprzeczytane załączniki, pomiar diakrytyków, pomiar sieci

Nowa sesja, ta sama sprawa. Zapis dopisany do tego pliku zgodnie ze zleceniem.

### Rozbieżność wobec briefu, stwierdzona na starcie

Brief zakładał, że PR #69 jest otwarty jako draft i że pozycje 7-8 z `weryfikacja-u-zrodla.md` czekają na odczyt. Sprawdzenie w GitHubie: **PR #69 został scalony 2026-09-03**, gałąź `claude/etap-2-regulamin-bur` po scaleniu usunięta, a sesja z 2026-09-03 zamknęła pozycje 4-8 u źródła - z maszyny, na której domeny rządowe były osiągalne. Brief opisywał stan sprzed czterech dni.

Skutki proceduralne: gałąź odtworzono z aktualnego `main` (dwa commity przeniesione przez rebase, konflikt w `weryfikacja-u-zrodla.md` rozstrzygnięty na rzecz nowszej treści z `main`), a praca poszła do **nowego PR-a**, bo scalonego PR-a nie da się użyć ponownie.

### Pomiar sieci - wykonany mimo nieaktualnego założenia

Zlecenie kazało spróbować pozycji 7 (`it.kielce.pl`) i 8 (`gov.pl`) przez `curl`, potem Chromium, maksymalnie dwie próby na domenę. Wykonano dokładnie tyle, choć obie pozycje były już zamknięte - bo pomiar mierzy coś, czego nie zastąpi żaden odczyt: stan dostępu z tego konkretnego środowiska.

| Próba | Adres | Wynik |
|---|---|---|
| 1, `curl` | `it.kielce.pl`, `www.it.kielce.pl`, `gov.pl`, `www.gov.pl` | `curl: (56) CONNECT tunnel failed, response 403` |
| 1, `curl` (kontrolnie) | `dziennikustaw.gov.pl`, `isap.sejm.gov.pl`, `uslugirozwojowe.parp.gov.pl` | to samo |
| 2, Chromium | `it.kielce.pl` | `net::ERR_TUNNEL_CONNECTION_FAILED` |

Diagnostyka `$HTTPS_PROXY/__agentproxy/status` wypisała dla każdej domeny `"kind": "connect_rejected"` z sygnaturą czasową tej sesji. Nie podjęto trzeciej próby ani żadnej próby obejścia.

**Wniosek:** pomiar **potwierdza**, a nie obala, ustalenie z 2026-09-03, że blokada jest własnością środowiska, nie projektu. Sesja lokalna u foundera sięga do domen rządowych, sesja zdalna w chmurze nie sięga. Reguła praktyczna wpisana do `weryfikacja-u-zrodla.md` i `MAPA-DROGOWA.md`.

Uwaga techniczna: `_robocze/narzedzia/pobierz-strone-chromium.mjs` nie uruchamia się z katalogu repozytorium, bo `playwright` jest zainstalowany globalnie w `/opt/node22/lib/node_modules`, a Node nie szuka tam pakietów przy imporcie ESM. Obejście: skopiować skrypt do katalogu roboczego i dowiązać tam `node_modules`. Na wynik pomiaru to nie wpływa.

### Podagenci: cztery uruchomione, cztery padły

Zgodnie ze zleceniem odczyt czterech dokumentów rozdzielono na czterech podagentów działających równolegle. Wszyscy czterej padli w ciągu kilku minut na limicie sesji (HTTP 429, „You've hit your session limit”). Pracę wykonano dalej szeregowo, w tej sesji, z ekstrakcją tekstu do plików roboczych i wyszukiwaniem po nich zamiast wczytywania całych dokumentów. **Wniosek na przyszłość: równoległe podagenty w tym projekcie zużywają limit szybciej, niż oszczędzają czas** - przy dokumentach, które i tak trzeba czytać cytat po cytacie, szeregowy odczyt z `grep` po wyekstrahowanym tekście jest tańszy.

### Co odczytano

Trzy załączniki dostarczone 2026-09-02 leżały w `zrodla/` nieprzeczytane - poza zakresem pozycji 1-3. Przeczytano je w całości plus Regulamin BUR (spis § 1-23, pełny odczyt § 11-20 i § 22-23, wyszukiwanie po całym pliku). Wyniki i cytaty z numerami paragrafów i stron: `01-baza-wiedzy/prawo/bur.md`.

Cztery ustalenia, które zmieniły dokumenty warstwy 1 i 2:

1. **Standard SUZ jest wiążący, nie doradczy** - § 15 ust. 3. Dotyczy każdej usługi zdalnej, więc i planowanego portalu szkoleń. Cztery z czternastu wymagań dotykają treści dokumentów: rzetelność informacji publikowanych o własnej działalności (SUZ-2, obejmuje dokumenty ofertowe i kanały marketingowe), jawna informacja o licencji na materiały (SUZ-3), zasady ustawy o dostępności cyfrowej (SUZ-1), standardy techniczne materiałów (SUZ-8).
2. **§ 16: materiał wgrany do BUR objęty jest bezterminową licencją dla Administratora BUR** z prawem przerabiania (ust. 2 pkt 6) i sublicencjonowania (pkt 7), przy zrzeczeniu się roszczeń. Cztery zakazy modyfikacji logotypu wiążą IRIN i jego wykonawców, nie wiążą PARP wobec plików w systemie.
3. **Dostosowanie materiałów dla osób ze szczególnymi potrzebami jest warunkiem wpisu do BUR** (§ 11 ust. 1 pkt 3), a potrzeba dostosowania nie może być powodem odmowy usługi (§ 15 ust. 1). W `program-szkolenia.md` pozycja 10 przeszła z **[WYBÓR]** na **[PRAWO]** / **[WYBÓR]**.
4. **Dokumenty BUR nie regulują znaków ani reklamy.** Pomiar na pełnym tekście sześciu dokumentów: „logo” i „logotyp” występują w korpusie dokładnie dwa razy, oba w jednej pozycji Załącznika 1. Żaden dokument nie daje prawa ani nie nakłada obowiązku posługiwania się znakiem BUR, logo PARP czy znakiem Funduszy Europejskich. Falsyfikator zapisany: materiały ze „Strefy dla Dostawców Usług”, których repozytorium nie ma.

Poza tym: sekcja „Ocena usługi po zakończeniu” w `bur.md` opisywała ankietę ze źródła wtórnego **nieprecyzyjnie** i została przepisana z odczytu (trzy pytania, skala 1-5, wagi 0,5/0,3/0,2, wzór oceny ogólnej). Sekcja „Warunek wpisu do BUR” przeszła ze źródeł wtórnych na § 11 - i przyniosła materiał, którego repozytorium nie ma: **misję oraz cele strategiczne i operacyjne IRIN** (§ 11 ust. 4 pkt 1).

### Pomiar 1 pilota, zamknięty w części bez foundera

Protokół pomiaru pilota (`_robocze/pilot-papier-firmowy/protokol-pomiaru.md`) to formularz czekający na oczy foundera. Pomiar 1 - polskie znaki na wagach 400, 500 i 600 - dał się jednak wykonać maszynowo, bo `main` zawiera od 2026-09-06 fonty osadzone w `_robocze/ds-bundle/fonts/fonts.css` jako data URI.

Nowe narzędzie: `_robocze/narzedzia/pokrycie-diakrytykow.py`. Wynik: **Manrope i Inconsolata mają 18/18 polskich diakrytyków z realnymi konturami**, a oba są fontami zmiennymi z ciągłą osią `wght` (Manrope 200-800, Inconsolata 200-900) - jeden plik na podzbiór, nie osobny plik na wagę. Glify nie mogą się więc różnić między wagami, a podstawienie z innego kroju jest niemożliwe. Otwarta zostaje ocena wizualna rysunku znaków.

**Dwie pułapki pomiarowe, obie zapisane w narzędziu, żeby nie wróciły:**

- **Podzbiory.** Ó i ó leżą w Latin-1, więc są w podzbiorze `latin`; pozostałe szesnaście znaków w `latin-ext`. Żaden pojedynczy plik nie ma kompletu i tak ma być. Pomiar na jednym pliku pokazuje „brakuje 16 znaków” i jest fałszywy.
- **Glify złożone.** Pierwsze podejście pokazało 16 pustych glifów Inconsolaty. To był artefakt licznika konturów, który przy glifie złożonym (baza plus znak diakrytyczny) zapisuje operację `addComponent` zamiast `moveTo`. Po rozłożeniu składników wynik brzmi 18/18. Sprawdzono osobno w tablicy `glyf`: wszystkie składniki są obecne w podzbiorze.

### Czego nie zrobiono i dlaczego

- **Pomiary 2-6 protokołu pilota** - wymagają obejrzenia kanwy w Claude Design, a pomiar 6 dodatkowo wydruku na papierze. Bez foundera nie do wykonania; statusy zostają puste, nie „wykonane”.
- **Nazwy certyfikatów jakości uznawanych przez PARP** - Regulamin ich nie wymienia, Załącznik 1 odsyła do „Strefy dla Dostawców Usług”. Zostaje ze źródeł wtórnych, z nazwanym falsyfikatorem.
- **Zakres art. 6 ustawy o zapewnianiu dostępności** - dokumenty PARP odsyłają do przepisu, którego repozytorium nie ma, a domena `isap.sejm.gov.pl` jest z tego środowiska nieosiągalna.
- **Usunięcie martwych gałęzi** - w repozytorium jest ich dziś ponad dwadzieścia. To operacja nieodwracalna z poziomu sesji i pozostaje decyzją foundera.
