# Weryfikacja przekazanego stanu i kanwa pilota - 2026-09-03, sesja druga

Ten plik jest protokołem pomiaru **zapisu przekazanego na starcie sesji**, nie nową specyfikacją.
Każde twierdzenie ma obok komendę albo nazwę pliku, z którego pochodzi. Nic z tego pliku nie wchodzi
do warstwy 1 bez decyzji właściciela.

## Wniosek jednym zdaniem

Pilot papieru firmowego **jest już zaprojektowany w Claude Design**, a nie „zero pomiarów": w projekcie
leży kanwa z czterema artboardami, blokiem pomiaru i czterema uwagami projektanta - natomiast dwa
pomiary z sześciu są nieważne, bo dokument odbiega od specyfikacji w dwóch miejscach.

## Co z przekazanego zapisu się nie potwierdziło

| Twierdzenie z zapisu | Czym zmierzone | Wynik |
|---|---|---|
| „Gałąź main jest ahead 2 wobec origin" | `git rev-list --left-right --count main...origin/main` | `0 0` - main jest zsynchronizowany |
| Commit `5704e16` „feat : Propozycje wariantów księgi marki" | `git cat-file -t 5704e16` | `fatal: Not a valid object name` - tego obiektu w tym klonie nie ma |
| „21 plików w projekcie" | `DesignSync list_files` | 58 ścieżek, z tego 19 katalogów, czyli **39 plików** |
| „ZERO z sześciu pomiarów jest wykonanych" | `DesignSync get_file templates/papier-firmowy-wizytowka/PapierFirmowyWizytowka.dc.html` | kanwa istnieje, ma blok „Protokół pomiaru" i cztery „Uwagi projektanta do właściciela" |
| „Przełącznik siatki działa osobno na każdym artboardzie" | ten sam plik: oba `.siatka` stoją pod jednym `sc-if value="{{ pokazSiatke }}"` | jeden przełącznik obsługuje obie strony A4; jest też drugi, na marginesy, którego zlecenie nie zamawiało; oba domyślnie wyłączone (`state = { pokazSiatke: false, pokazMarginesy: false }`) |

**Wyjaśnienie dwóch pierwszych wierszy, nie zarzut wobec zapisu:** ta sesja pracuje w świeżym klonie
zdalnym, nie na maszynie właściciela. Dwa niewysłane commity mogą istnieć u właściciela lokalnie
i po prostu nie ma ich tutaj - stąd nie da się ich ani przejrzeć, ani wysłać. Sprawa „nie wysyłaj
na origin" w tym środowisku nie ma przedmiotu: gałąź robocza `claude/irin-visual-identity-vq9ddw`
jest zsynchronizowana z `origin` (`git rev-list --left-right --count HEAD...origin/claude/irin-visual-identity-vq9ddw` → `0 0`),
a `main` jest 27 commitów za nią (`git rev-list --left-right --count main...HEAD` → `0 27`).

## Co z zapisu się potwierdziło

- Nazwy w projekcie są inne niż w repozytorium: `format-paczki.md` występuje jako
  `guidelines/zasady-uzycia.md`, katalog `tokeny/` jako `tokens/`. Prompt wołający starą nazwę
  każe Claude Design szukać pliku, którego nie ma.
- `guidelines/` ma dziś **osiem** plików: `paleta-barw.md`, `siatka-a4.md`, `typografia.md`,
  `logotyp.md`, `zasady-uzycia.md`, `papier-firmowy.md`, `kontekst-firmy.md`,
  `kontekst-firmy-sanitized.md`.
- Dublowanie SVG jest większe, niż mówił zapis: trzy pliki znaku leżą w `assets/`, w `uploads/`
  **i** w `templates/papier-firmowy-wizytowka/assets/`, czyli w trzech miejscach.
- `list_projects` i `get_project` nie były w tej sesji wywołane, więc o pułapce z listowaniem nic
  nie mierzę. Dowód, że projekt istnieje i jest czytelny: `list_files` i `get_file` na id
  `1a22ce64-0e1c-43a6-bd60-eef9241ef73b` zwróciły pełną treść.

## Dwie rozbieżności dokumentu wobec specyfikacji

### 1. Sygnet na rewersie ma 22 mm - to polecenie właściciela, nie odstępstwo (zarzut wycofany)

- Zlecenie (`03-pakiet-claude-design/zlecenia/pilot-papier-firmowy.md`, pomiar 4): „Sygnet stoi
  na rewersie dokładnie w 10 mm (poprawione 2026-09-03 z 12 mm, żeby pomiar w ogóle dotyczył
  spornej wartości)".
- Kanwa: `<img src="./assets/logo_irin_sygnet.svg" ... width:22mm ...>`, a blok „Protokół pomiaru"
  na kanwie sam podaje „Sygnet na rewersie: **22 mm** szerokości".
- **Wycofanie, po odpowiedzi właściciela 2026-09-03:** 22 mm to jego polecenie („na rewersie
  kazałem go powiększyć"), a nie odstępstwo projektanta. Przedawniony jest **zapis w zleceniu
  i w formularzu**, nie dokument. Oba poprawione tego samego dnia.
- Skutek, który zostaje: sporną wartością w `01-baza-wiedzy/identyfikacja/logotyp.md` jest
  **10 mm / 44 px** (wiersz „nie potwierdzony osobno"). Sygnet w 22 mm o niej nic nie mówi -
  stoi powyżej zatwierdzonego minimum 18 mm dla pełnego znaku. **Pomiar 4 stracił nośnik**;
  trzy wyjścia i decyzja właściciela w `_robocze/pilot-papier-firmowy/protokol-pomiaru.md`,
  sekcja „Pomiar 4 stracił nośnik". Do jej podjęcia bramka B liczy pięć pomiarów, nie sześć.

### 2. Znak jest przebarwiony filtrem CSS

- `logotyp.md`, zakaz 1: „Nie zmieniamy koloru znaku. Ani sygnetu, ani wersji poziomej, ani
  pionowej. Znak jest jednokolorowy; na ciemnym tle stosuje się wersję odwróconą, a nie
  przebarwioną."
- Kanwa: **każdy** `<img>` ze znakiem ma atrybut `filter:` z łańcuchem
  `brightness(0) ... invert(...) sepia(...) saturate(...) hue-rotate(...) brightness(...) contrast(...)`.
- Policzone emulacją tego łańcucha wg specyfikacji Filter Effects (skrypt jednorazowy, wejście:
  czarny znak źródłowy - pliki SVG nie mają `fill`, patrz `logotyp.md`):

| Miejsce | W jaki kolor filtr celuje wg opisu na kanwie | Wynik emulacji | Uwaga |
|---|---|---|---|
| strona pierwsza, strona kolejna, awers wizytówki | Aksamit `#452430` | **`#3D1922`** | filtr nie trafia w żaden kolor palety |
| rewers wizytówki (tło Espresso) | Kaszmir `#FBF8F2` | **`#F6F3EB`** | najbliższy kolor palety to Muślin `#F6F2E9`, nie Kaszmir |

- **To rachunek, nie odczyt z renderu.** Falsyfikator: pipeta na żywej kanwie dająca inną wartość
  niż `#3D1922` na jasnym tle albo `#F6F3EB` na ciemnym.
- Rozbieżność ma dwie warstwy i tylko pierwsza jest decyzją właściciela: (a) czy przebarwienie znaku
  na **jasnym** tle jest naruszeniem zakazu 1, czy dopuszczonym sposobem użycia - na ciemnym tle
  „wersja odwrócona" jest w zakazie przewidziana wprost; (b) jeżeli dopuszczonym, to i tak **nie tym
  filtrem**, bo nie trafia w kolor z palety. Drugą warstwę da się naprawić bez decyzji: kolor znaku
  ustawia się wtedy wprost, wartością hex, nie łańcuchem filtrów.

## Trzecie ryzyko okazało się nieistniejące: kroje w projekcie SĄ osadzone

**Ta sekcja jest wycofaniem mojego własnego twierdzenia, nie ustaleniem.** Postawiłem hipotezę,
że projekt w Claude Design ładuje kroje z sieci, i zmierzyłem ją. Hipoteza upadła.

| Co | Pomiar | Wynik |
|---|---|---|
| Zdalny `fonts/fonts.css` wobec lokalnego `_robocze/ds-bundle/fonts/fonts.css` | `DesignSync get_file` + `sha256` obu | **bajt w bajt identyczne**: 127 729 B, `sha256` zaczyna się na `f80139aec8d4a268` |
| Czy kroje są osadzone | `grep -c "data:font/woff2"` na treści zdalnej | **4 bloki** na 4 reguły `@font-face` |
| Czy jest jakiekolwiek odwołanie sieciowe | `grep -c "url(http"` | **0** |
| Jedyna wzmianka o `googleapis` | `grep -n googleapis` | wiersz 3, w komentarzu nagłówkowym, nie w `src:` |

Osadzone są cztery kroje: Manrope `200 800` w podzbiorach latin i latin-ext oraz Inconsolata
`300 700` w tych samych dwóch podzbiorach. Podzbiór latin-ext niesie polskie diakrytyki, więc
pomiar 1 ma czym mierzyć.

**Co było źródłem błędu:** `_ds_manifest.json` podaje dla wszystkich czterech krojów `"files": []`
i `"remoteSrc": true`. To opis nieprawdziwy wobec pliku, który w projekcie faktycznie leży - albo
manifest powstał przy wcześniejszym wgraniu, albo jego parser nie klasyfikuje `data:` URI jako
pliku lokalnego. Wniosek na przyszłość: **`_ds_manifest.json` nie jest dowodem o zawartości
projektu; dowodem jest `get_file` na konkretnym pliku.**

Druga rzecz, którą to obala: mój wywód z historii git („plik dodano commitem `1ad0f9b`, czyli
po wysyłce `19691a4`, więc nie został wysłany") był nieuprawniony. Data wpisania pliku do git
nie mówi, kiedy ten plik pojawił się na dysku ani co wysłał `write_files`.

**Skutek operacyjny: nie ma czego wysyłać, a uwaga projektanta nr 4 na kanwie („Podgląd na kanwie
renderuje Manrope i Inconsolatę osadzone jako data URI") jest prawdziwa.** Pomiar 1 wolno wykonać
na żywej kanwie bez żadnego przygotowania. Zostaje jedno ograniczenie z tej samej uwagi, niezależne
od osadzenia: eksport do PDF idzie przez drukarkę Chromium i wyciąga metryki systemowe, więc
pomiarów wag i diakrytyków nadal nie robi się na PDF.

## Kontrast Karminu obok Aksamitu - policzony od nowa, nie przepisany

Wzór WCAG 2.1, luminancja względna sRGB, skrypt jednorazowy w tej sesji. Oba hexy podane obok wyniku:

| Para | Hexy | Kontrast |
|---|---|---|
| Karmin na Aksamicie | `#9E2B2B` / `#452430` | **1,83:1** |
| Karmin na Kaszmirze | `#9E2B2B` / `#FBF8F2` | 6,99:1 |
| Karmin na Muślinie | `#9E2B2B` / `#F6F2E9` | 6,63:1 |
| Karmin na Pergaminie | `#9E2B2B` / `#E7DFD2` | 5,60:1 |
| Pergamin jako etykieta na wypełnieniu Karminu | `#E7DFD2` / `#9E2B2B` | 5,60:1 |
| biel jako etykieta na wypełnieniu Karminu | `#FFFFFF` / `#9E2B2B` | 7,41:1 |
| Karmin na Espresso | `#9E2B2B` / `#221A15` | 2,31:1 |

**Kontrola metody:** ten sam skrypt odtworzył co do setnej sześć wartości z tabel w
`01-baza-wiedzy/identyfikacja/paleta-barw.md`: Karmin/Kaszmir 6,99, Karmin/Pergamin 5,60,
Popiół na trzech tłach 4,34 / 4,12 / 3,48, Espresso na Złocie foliowym 5,09. Metoda się zgadza,
więc 1,83:1 nie jest artefaktem rachunku.

**Co z tego wynika dla certyfikatu:** plakietka KOREKTA w Karminie **nie może** stać na wypełnieniu
Aksamitu ani Aksamit na Karminie - 1,83:1 to zlanie się dwóch plam. Karmin na papierze Kaszmir
(6,99:1) i Pergamin jako napis na wypełnieniu Karminu (5,60:1) przechodzą próg 4,5:1 dla tekstu.
Karmin na Espresso (2,31:1) też jest zakazany, a Espresso jest tłem rewersu wizytówki, więc
ta para nie jest hipotetyczna.

## Siatka na A4 poziom - rachunek, jeżeli orientacja się zmieni

`siatka-a4.md` obowiązuje wyłącznie na A4 pion i sama mówi: „Falsyfikator: inny format albo inna
orientacja strony niż A4 pion - wtedy całe to sprawdzenie trzeba wykonać od nowa". Oto to
sprawdzenie wykonane od nowa, dla A4 poziom 297 × 210 mm, przy zachowanych sześciu kolumnach.
Kryterium doboru jest to samo, którym `siatka-a4.md` uzasadnia parę 25 / 4: gutter ma być
wyraźnie węższy od kolumny, w pionie wychodzi 4/25 = 0,160, czyli około jednej szóstej.

| Margines boczny | Pole treści | Najbliższe rozwiązanie całkowite | gutter/moduł |
|---|---|---|---|
| 18 mm | 261 mm | 6 × 36 + 5 × 9 = 261 mm | 0,250 |
| **20 mm** (jak w pionie) | **257 mm** | **6 × 37 + 5 × 7 = 257 mm** | **0,189** |
| 22 mm | 253 mm | 6 × 38 + 5 × 5 = 253 mm | 0,132 |
| 25 mm | 247 mm | 6 × 37 + 5 × 5 = 247 mm | 0,135 |

Rytm pionowy też się zmienia: w pionie pole treści ma 251 mm = 41 jednostek po 6 mm plus 5 mm
reszty, w poziomie 210 − 18 − 28 = 164 mm = **27 jednostek plus 2 mm reszty**. Zdanie z `siatka-a4.md`
o „reszcie 5 mm na dole" przestaje być prawdziwe i sekcję „Rytm pionowy" trzeba by przepisać.

**Koszt zmiany orientacji, wypisany wprost:** nowa para moduł/gutter (37 / 7 przy marginesach 20 mm),
nowa reszta rytmu pionowego, nowa strefa stopki, i - najważniejsze - **nowa specyfikacja wymagająca
świadomej decyzji właściciela**, bo `siatka-a4.md` ma status ZATWIERDZONA i dotyczy tylko pionu.
To nie jest przeliczenie w tle, to otwarcie piątej specyfikacji identyfikacji.

## Czego jeszcze nie ma

| Plik albo zasób | Stan |
|---|---|
| `03-pakiet-claude-design/zlecenia/certyfikat-zaswiadczenie.md` | nie istnieje |
| `03-pakiet-claude-design/zlecenia/certyfikat-zaswiadczenie-do-wyslania.md` | nie istnieje |
| `_robocze/certyfikat/protokol-pomiaru.md` | nie istnieje, katalogu też nie ma |
| `guidelines/certyfikat.md`, `guidelines/bur.md`, `guidelines/kfs.md`, `guidelines/pozyczki-ue-bgk.md` w projekcie | nie istnieją; `guidelines/` ma osiem plików wymienionych wyżej |

## Otwarte decyzje właściciela

Kolejność jest istotna: pierwsze dwie zmieniają treść wszystkiego, co niżej, bo dotyczą znaku
i tego, na czym się mierzy.

1. ~~**Kanwa pilota:** zasiać od nowa czy poprawić.~~ **Zamknięte 2026-09-03:** kanwa zostaje,
   22 mm na rewersie jest polecenie właściciela. Na jej miejsce wchodzi decyzja węższa: **gdzie
   przenosi się pomiar 4**, który stracił nośnik - trzy wyjścia w formularzu pomiaru.
2. **Przebarwienie znaku filtrem CSS na jasnym tle:** naruszenie zakazu 1 do naprawy, czy dopuszczony
   sposób użycia do dopisania w `logotyp.md`.
3. ~~**Kroje w projekcie:** czy wysłać osadzony `fonts/fonts.css`.~~ **Zamknięte pomiarem 2026-09-03:**
   plik w projekcie jest identyczny z lokalnym, kroje są osadzone, nie ma czego wysyłać.
4. **Orientacja certyfikatu:** A4 pion (zatwierdzona siatka bez zmian) czy A4 poziom (rachunek wyżej,
   nowa specyfikacja do zatwierdzenia).
5. **Dziedzina certyfikatu, czyli kolor warstwy 15 %:** Aksamit (Pedagogika), Miedź (Akademia AI)
   albo Onyks (Pożyczki UE/BGK) - jeden na dokument.
6. **Osoba podpisująca:** jedna sygnatura czy dwie. Imion z `brandbook.dc.html` użyć nie wolno.
7. **Numeracja zaświadczeń:** czy `IRIN/RRRR/D/NNNNN` z kanwy jest realną konwencją firmy, czy
   wzór ma zostać z placeholderem.
8. **PESEL na dokumencie:** czy w ogóle, i w jakim maskowaniu.

Pozycje 4-8 blokują napisanie zlecenia certyfikatu. Pozycja 1 blokuje domknięcie bramki B.
Pozycja 2 została przez właściciela **odłożona**: decyzja po obejrzeniu pracy Claude Design.
Do tego czasu w zleceniach obowiązuje `logotyp.md` w brzmieniu dotychczasowym, czyli zakaz
przebarwiania na jasnym tle i wersja odwrócona na ciemnym.
Pozycja 3 jest zamknięta pomiarem.
