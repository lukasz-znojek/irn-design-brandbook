# POMIAR - stan paczki systemu projektowego IRIN

Data pomiaru: 2026-09-09. Gałąź: `claude/irin-pomiar-raport-xsbs7j`, stan `e16b944`.
Wykonawca: Claude Code, etap 1 promptu ze strony projektowej (Claude Design).

Wszystkie liczby w tym pliku zostały **policzone w tej sesji**, nie przepisane. Przy każdej stoi
rachunek albo komenda. Skrypty pomiarowe są jednorazowe i leżą poza repozytorium
(`/tmp/.../scratchpad/`: `kontrast.py`, `geometria.py`, `glify.py`, `licencja.py`, `bbox.mjs`,
`ladowanie.mjs`, `linki.py`) - zgodnie z poleceniem nie wchodzą do paczki, bo nie mają testów.

---

## 1. Werdykt jednym zdaniem

> **Uzupełnione 2026-09-09, rozdz. 9.** Po tym werdykcie uzyskałem dostęp do projektu Claude Design
> i zmierzyłem go. Paleta „Regalia” istnieje i jest zatwierdzona; rekomendacja B w pytaniu 1 była
> błędna. Rozdziały 3.2, 3.3 i 7 zostają jako zapis stanu wiedzy sprzed tego odczytu - ich zdania
> o repozytorium są nadal prawdziwe, zdania o stronie projektowej rozstrzyga rozdz. 9.

**Paczka jest wewnętrznie spójna w wartościach, które sama deklaruje - 25 z 25 kontrastów
i cała arytmetyka siatki odtworzyły się co do setnej - ale rozjeżdża się z rzeczywistością
na 8 pozycjach, z czego najpoważniejsza jest ta, że raport ze strony projektowej opisuje
paczkę o innej palecie, innym prefiksie tokenów i innej strukturze plików niż ta, którą
to repozytorium publikuje.**

Rozbicie: 6 rozjazdów wewnątrz repozytorium (rozdz. 3), 2 rozjazdy między repozytorium
a raportem projektowym, których nie da się rozstrzygnąć bez wglądu w tamtą stronę (rozdz. 7).
Z siedmiu pozycji zgłoszonych przez stronę projektową do `/design-sync` **cztery są fałszywe
wobec tego repozytorium** (rozdz. 3.2).

---

## 2. Inwentarz

### 2.1 Co paczka faktycznie eksportuje

`.design-sync/config.json` wskazuje `bundleDir: "_robocze/ds-bundle"`. To jest cała paczka
wysyłana do Claude Design.

| Plik | Rola | Linii | Ostatnia zmiana |
|---|---|---|---|
| `_robocze/ds-bundle/styles.css` | arkusz bazowy, 2 x `@import` | 49 | 2026-09-03T05:18:43 |
| `_robocze/ds-bundle/tokens/tokens.css` | 28 zmiennych koloru + siatka + kroje | 41 | 2026-09-03T05:14:01 |
| `_robocze/ds-bundle/tokens/palette-irin.json` | dane maszynowe, kopia warstwy 1 | 412 | 2026-09-03T05:14:01 |
| `_robocze/ds-bundle/fonts/fonts.css` | 4 x `@font-face`, fonty jako data URI | 41 (127 729 B) | 2026-09-03T05:18:43 |
| `_robocze/ds-bundle/guidelines/*.md` | 5 plików: 4 kopie specyfikacji + zasady użycia | 434 razem | 2026-09-03T05:14:01 |
| `_robocze/ds-bundle/components/**/*.html` | 8 kart podglądu (4 fundamenty, 4 prymitywy) | 302 razem | 2026-09-03T05:14:01 |
| `_robocze/ds-bundle/README.md` | idiom paczki, 8 reguł | 64 | 2026-09-03T05:14:01 |
| `_robocze/ds-bundle/_ds_needs_recompile` | flaga, treść: `1` | 1 | 2026-09-03T05:14:01 |

**Czy są komponenty kodowe: nie.** Nie ma `package.json`, `dist/`, Storybooka ani żadnego
budowania. Osiem plików w `components/` to **karty podglądu HTML**, nie komponenty do importu -
każda jest samodzielnym dokumentem z `<link rel="stylesheet" href="../../../styles.css">`.
`.design-sync/config.json:6` mówi to wprost i pokrywa się z pomiarem.

Pytanie z promptu - czy `"components": []` po stronie projektowej to prawda, czy artefakt
synchronizacji - **rozstrzyga się tak: po stronie repozytorium komponentów kodowych nie ma
w ogóle**, więc pusta lista jest prawdziwa co do komponentów, ale gubi 8 kart podglądu, które
w paczce fizycznie są. Czy manifest ma je liczyć, to decyzja, nie błąd (pytanie 4 w rozdz. 8).

### 2.2 Reszta repozytorium, z rolami

| Obszar | Plików | Rola |
|---|---|---|
| `01-baza-wiedzy/identyfikacja/` | 6 | **jedyne źródło prawdy** dla koloru, siatki, typografii, logotypu |
| `01-baza-wiedzy/prawo/` | 8 md + 10 PDF (8,7 MB) | przepisy i źródła; PDF-y to 79 % objętości repozytorium |
| `01-baza-wiedzy/firma/`, `uslugi/`, `_szablony/` | 8 | kontekst firmy i usług |
| `02-szablony-dokumentow/` | 8 | karty specyfikacji treści (warstwa 2) |
| `03-pakiet-claude-design/` | 6 | format paczki, prompt bazowy, zlecenie pilota |
| `_robocze/` | 60 | poligon i archiwum; z tego `copilot-v1/` to 29 plików |
| korzeń | 3 SVG + `brandbook.dc.html` + 5 md | logotypy, kanwa foundera, PLAN, MAPA-DROGOWA |
| `.github/workflows/` | 5 | 4 wyzwalacze agenta + tablica projektów |

### 2.3 Pliki martwe albo bez odwołań

Nic w tym repozytorium nie jest starsze niż 2026-09-02, więc kryterium „nikt nie zmieniał
od miesięcy" nie łapie niczego. Kryterium „nic się do niego nie odwołuje" łapie 12 plików:

| Plik | Ocena |
|---|---|
| 8 kart w `_robocze/ds-bundle/components/**` | **nie martwe** - odnajduje je adnotacja `<!-- @dsCard -->`, nie import. Wynik zerowy jest artefaktem metody. |
| `_robocze/ds-bundle/_ds_needs_recompile` | flaga mechanizmu synchronizacji; nie wiadomo, czy odczytana |
| `.design-sync/config.json` | czytany przez `/design-sync`, nie przez repozytorium |
| `_robocze/brandbook-warianty/notatka-warianty.md` | **osierocona** - `PLAN.md` opisuje decyzję o wariancie 1, ale nie linkuje notatki |
| `_robocze/skasowane-galezie-2026-09-03.md` | **martwy** - zapis jednorazowej operacji, nikt go nie czyta |

Osobno: `.gitignore` to w 26 z 32 linii szablon dla projektów **AL / Dynamics 365 Business
Central** (`.alcache/`, `*.bclicense`, `rad.json`). Do tego repozytorium nie ma nic. Żywe są
tylko trzy ostatnie wpisy (`.mcp.json`, `.agentsroom/`, `.DS_Store`).

---

## 3. Rozjazdy wartości

### 3.1 Rozjazdy wewnątrz repozytorium

| # | Wartość | Plik i wiersz | Jest | Ma być | Na jakiej podstawie |
|---|---|---|---|---|---|
| R1 | Dryf rytmu pionowego na pełnej kolumnie | `01-baza-wiedzy/identyfikacja/siatka-a4.md:139`; `typografia.md:41`; `tokeny/palette-irin.json:104` | **19 mm przy 45 liniach** | **20,86 mm przy 45 liniach**, albo 19,01 mm przy **41** liniach | rachunek w rozdz. 4.2. 19 mm to dryf na 41 liniach; „45" pochodzi skądinąd. Dwie liczby z różnych rachunków zostały zapisane w jednym wierszu. |
| R2 | Marginesy w etykiecie podglądu siatki | `_robocze/pilot-papier-firmowy/Main.dc.html:29` | `marginesy 18 / 22 / 28 / 18 mm` | `20 / 20` na bokach | ten sam plik, wiersz 17: `padding: 18mm 20mm 28mm 20mm`. Etykieta przeczy kodowi obok. Poprawka 18/22 -> 20/20 z 2026-09-03 nie dotarła do napisu. |
| R3 | Popiół w wybranym układzie księgi marki | `_robocze/brandbook-warianty/wariant-1-kaszmir-uporzadkowany.dc.html`, 2 wystąpienia (te same 2 w wariantach 2 i 3) | `#938978` | `#7D7466` | `paleta-barw.md:39`. Chronologia: warianty to commit `1cd1fef` z 2026-09-03T03:21, pociemnienie Popiołu to `2c4bee1` z 04:06 - poprawka jest o 45 minut młodsza od plików. Wariant 1 jest **wybrany przez foundera**, więc to nie archiwum. Skutek: 2,61:1 na Pergaminie zamiast 3,48:1, próg 3:1 niespełniony. |
| R4 | Odnośniki względne w paczce | `_robocze/ds-bundle/guidelines/*.md`, **17 martwych odnośników** | wskazują `./tokeny/…`, `../../03-pakiet-claude-design/…`, `../01-baza-wiedzy/…` | ścieżki wewnątrz paczki | `linki.py`: 110 odnośników względnych w `.md`, 17 nie trafia w plik. Wszystkie w `guidelines/` - pliki są bajt w bajt kopiami warstwy 1, przeniesionymi na inną głębokość, więc ścieżki się urwały. To jest ta „ścieżka, której nie ma", o którą pyta prompt. |
| R5 | Pilot nie używa paczki | `_robocze/pilot-papier-firmowy/*.dc.html`, 4 pliki | fonty z `fonts.googleapis.com`, **zero** `var(--irin-*)`, **zero** `styles.css`, wszystkie 8 barw wpisane hexem | paczka ma fonty osadzone i tokeny | porównanie plików. Skutek praktyczny: zmiana palety w tokenach **nie przejdzie** na nośniki pilota. |
| R6 | Brakujący `support.js` | 4 x `<script src="./support.js">` w artboardach pilota | pliku nie ma w repozytorium | dostarcza go środowisko Claude Design | `ls` zwraca „No such file". Prawdopodobnie w porządku, ale niepotwierdzone - do sprawdzenia przy zasiewie. |

### 3.2 Siedem pozycji zgłoszonych przez stronę projektową - weryfikacja

> **Zakres tej tabeli: wyłącznie repozytorium.** Wszystkie werdykty niżej są prawdziwe wobec plików
> w tym repozytorium i pozostają w mocy. Po stronie projektowej te same pozycje mają inne
> rozstrzygnięcie - zmierzone w rozdz. 9.2 i 9.5.

Prompt kazał zweryfikować każdą własnym pomiarem przed wykonaniem. Wynik:

| Pozycja z rozdz. 6 raportu projektowego | Werdykt | Dowód |
|---|---|---|
| Jedenasty poziom skali **8,5 px = 6,4 pt** | **do decyzji, i liczba jest niedokładna** | W repozytorium `8.5px` występuje **wyłącznie** w `brandbook.dc.html` (4 razy, stopki kanwy foundera) - w żadnej obowiązującej specyfikacji. Rachunek: 8,5 x 72/96 = 6,375 pt, czyli **6,38 pt** przy obowiązującej regule dwóch miejsc po przecinku, nie 6,40. Najmniejszy dziś poziom to 10 px = 7,50 pt. |
| Współczynniki **0,655 / 0,561** | **POTWIERDZONE własnym pomiarem** | Zmierzone w Chromium (`getBBox`, `bbox.mjs`): poziom 184,213/281,333 = **0,6548**; pion i sygnet 103,728/184,837 = **0,5612**. Wartości ze strony projektowej odtwarzają się co do trzeciego miejsca. Skutki w rozdz. 4.3. |
| Dryf rytmu: **19 mm** kontra **20,70 mm** | **obie strony mają źle** | Poprawnie 20,86 mm przy 45 liniach (rozdz. 4.2). 20,70 mm to skutek mnożenia przez zaokrąglone 0,46; 19 mm to dryf na 41 liniach. |
| Zapis **NIP ciągiem** | **JUŻ ZROBIONE, nie ma czego zmieniać** | `grep 9592061542`: 7 wystąpień, **wszystkie ciągiem**, w tym `StopkaFirmowa.html:12` i `BlokDanychRejestrowych.html:16`. Zero wystąpień `959-206-15-42`. |
| Osiem kart renderuje **poprzednią paletę** | **FAŁSZ wobec tego repozytorium** | Wszystkie 8 kart otwarte w Chromium na serwerze lokalnym (`ladowanie.mjs`): tokeny rozwiązują się do `#FBF8F2 / #7D7466 / #A8874E / #2E5241 / #8A6110 / #9E2B2B`, czyli do palety obowiązującej. Siedem kart używa wyłącznie `var(--irin-*)`; ósma (`Paleta.html`) wpisuje 14 hexów wprost jako próbki i **wszystkie 14 zgadzają się** z `paleta-barw.md`. Zero błędów konsoli i sieci na każdej z ośmiu. |
| `styles.css` niesie **Muślin, Espresso i Popiół** zamiast **Kości Słoniowej, Atramentu i Grafitu** | **FAŁSZ w obu połowach** | `grep -E '#[0-9A-Fa-f]{3,6}' styles.css` zwraca **zero** literalnych hexów - arkusz operuje wyłącznie tokenami. Nazwy „Kość Słoniowa", „Atrament", „Grafit" nie występują w repozytorium **ani razu** (jedyny „grafit" to opis odrzuconego wariantu 3 palety w archiwum). |
| `_ds_manifest.json` z pustą listą | **pliku nie ma w repozytorium** | `grep -r _ds_manifest`: jedyne trafienie to komentarz w `.design-sync/config.json`, i dotyczy `_ds_bundle.js`, nie manifestu. |

### 3.3 Rozjazd, który nie jest pozycją na liście, tylko podstawą

Prompt każe sprawdzić „czternaście hexów palety **Regalia**", tokeny `--irin-r-*`,
`--irin-r-dziedzina`, `--irin-r-limit-zlota-cm2`, `_ds_bundle.js` i blok poprzedniej palety
w pierwszych ~75 wierszach `tokens.css`.

| Czego szukałem | Wynik `grep` |
|---|---|
| `Regalia` | **0 wystąpień w całym repozytorium** |
| prefiks `--irin-r-` | **0 wystąpień** |
| `--irin-r-limit-zlota-cm2` | **0 wystąpień** |
| `426,70` / `21,34` zapisane w plikach | **0 wystąpień** (choć rachunek je odtwarza - rozdz. 4.4) |
| `_ds_bundle.js` | **0**, poza zdaniem „Bez `_ds_bundle.js`" w konfiguracji |
| blok poprzedniej palety w `tokens.css` | **nie istnieje** - plik ma 41 wierszy, w tym 28 zmiennych bieżącej palety i ani jednej archiwalnej |
| brak tokenów stanu (`success`, `warning`, `error`) | **przeciwnie: wszystkie trzy są**, `tokens.css:20-25`, z nazwami Werdykt, Rubryka, Karmin |

> **Rozstrzygnięte w rozdz. 9.** Regalia istnieje - po stronie projektowej, dopisana do
> `tokens/tokens.css` 2026-09-06. Wniosek niżej („strona projektowa opisuje inną paczkę”) był
> błędny; poprawny brzmi: **strona projektowa opisuje paczkę nowszą o dwa pokolenia palety.**

To nie jest siedem drobnych rozbieżności, tylko jedna duża: **strona projektowa opisuje inną
paczkę.** Obowiązująca tu paleta nazywa się **„Kaszmir Wyciszony"**, wersja `v2`, zatwierdzona
przez foundera 2026-09-02 (`palette-irin.json:3-6`), prefiks tokenów to `--irin-`, a reguła
„paleta nie ma tokenów stanu" jest wprost sprzeczna z zawartością pliku. Trzy możliwości - którą
przyjąć, rozstrzyga właściciel (pytanie 1 w rozdz. 8), nie ja.

### 3.4 Gdzie zgodność jest pełna

Żeby lista rozjazdów nie sugerowała chaosu tam, gdzie go nie ma:

- `01-baza-wiedzy/identyfikacja/{paleta-barw,siatka-a4,typografia,logotyp}.md` i ich kopie
  w `_robocze/ds-bundle/guidelines/` są **bajt w bajt identyczne** (`diff -q`, 4 z 4).
- `palette-irin.json` w warstwie 1 i w paczce - **identyczne**.
- 14 hexów w `tokens.css`, w `palette-irin.json`, w `paleta-barw.md` i w karcie `Paleta.html`
  - **cztery źródła, ta sama liczba, zero rozjazdów**.
- `palette-irin.json` **nie ma** niepodpisanej sekcji archiwalnej. Dwa miejsca z dawnymi
  wartościami są etykietowane (`"zrodlo-wyboru": "… archiwum"` w wierszu 7,
  `"zmiana-2026-09-03"` w wierszu 207). Pułapki na czytelnika tu nie ma.
- Stare hexy palety 12-kolorowej (`#1E1611`, `#4A1D26`, `#B58540` i pozostałe) żyją wyłącznie
  w miejscach **jawnie historycznych**: tabela „co się zmieniło" w `paleta-barw.md`, opis kanwy
  w `CLAUDE.md`, archiwum `_robocze/paleta-v2/`. Jedynym wyjątkiem jest R3.

---

## 4. Kontrasty i procenty - przeliczone od zera

### 4.1 Kontrast WCAG 2.1, 14 kolorów na 3 tłach

Skrypt `kontrast.py`: luminancja względna sRGB, `(L_jaśniejsze + 0,05) / (L_ciemniejsze + 0,05)`.

| Kolor | Hex | Kaszmir | Muślin | Pergamin | Zgodność z zapisem |
|---|---|---|---|---|---|
| Espresso | `#221A15` | 16,15 | 15,32 | 12,95 | zgodne |
| Sepia | `#5E4E40` | 7,50 | 7,12 | 6,02 | zgodne |
| Aksamit | `#452430` | 12,80 | 12,14 | 10,26 | zgodne |
| Miedź | `#7A5638` | 6,16 | 5,85 | 4,94 | zgodne |
| Onyks | `#33474F` | 9,19 | 8,72 | 7,37 | zgodne |
| Złoto foliowe | `#A8874E` | 3,17 | 3,01 | **2,55** | zgodne (i zgodnie z zapisem pod progiem 3:1) |
| Werdykt | `#2E5241` | 8,26 | 7,83 | 6,62 | zgodne |
| Rubryka | `#8A6110` | 5,22 | 4,95 | **4,18** | zgodne (pod progiem 4,5:1 dla tekstu) |
| Karmin | `#9E2B2B` | 6,99 | 6,63 | 5,60 | zgodne |
| Popiół | `#7D7466` | 4,34 | 4,12 | 3,48 | zgodne |
| Patyna | `#2F5A63` | 7,17 | 6,80 | 5,75 | zgodne |

Etykiety na wypełnieniu, 7 par: 10,26 / 4,94 / 7,37 / 5,09 / 6,62 / 5,53 / 5,60 - **wszystkie
zgodne**. Pary wzajemne: Patyna x Onyks = **1,28**, Onyks x Espresso = **1,76** - zgodne.

**Bilans: 25 z 25 zadeklarowanych wartości odtworzyło się co do setnej. Zero rozjazdów
powyżej 0,05.** Falsyfikator z `paleta-barw.md:76` nie zadziałał - i to jest wynik, nie brak
wyniku: metoda liczenia w tym repozytorium jest sprawdzona.

### 4.1a Tinty 12 %

Prompt każe policzyć tinty 12 %. **W repozytorium nie ma ani jednej zadeklarowanej tinty** -
`grep` nie znajduje ani pojęcia, ani wartości. Nie ma więc z czym porównywać; poniżej są to
liczby nowe, nie weryfikacja. Policzyłem je i tak, bo pytanie o nie oznacza, że gdzieś istnieją.

Wynik zbiorczy (`kontrast.py`, mieszanie w sRGB, 12 % koloru na tle): **wszystkie 33 tinty
utrzymują Espresso powyżej 10,22:1, a Sepię powyżej 4,75:1.** Najciemniejsza tinta to Espresso
12 % na Pergaminie (`#CFC7BB`); najjaśniejsza - Złoto foliowe 12 % na Kaszmirze (`#F1EADE`).
Żadna nie schodzi poniżej progu AA dla tekstu normalnego.

### 4.2 Rytm pionowy - rozstrzygnięcie R1

```
interlinia korpusu = 13,5 px x 1,55            = 20,9250 px
                                                = 20,9250 x 25,4/96 = 5,5364 mm   (zapis: 5,54 - zgodne)
jednostka odstępu  = 6 mm                       = 22,6772 px
różnica na linię   = 22,6772 - 20,9250          = 1,7522 px = 0,4636 mm  (zapis: 0,46 - zgodne)

dryf x 41 linii = 41 x 0,463594 = 19,01 mm
dryf x 45 linii = 45 x 0,463594 = 20,86 mm      <- wartość poprawna dla 45 linii
                  z zaokrąglonym 0,46: 20,70 mm <- liczba strony projektowej
ile linii korpusu mieści 251 mm: 251 / 5,5364   = 45,34
ile jednostek 6 mm mieści 251 mm: 251 / 6       = 41,83 -> 41 pełnych, reszta 5 mm
```

**Rozstrzygnięcie: 20,86 mm.** Zapis „19 mm na pełnej kolumnie (45 linii)" łączy liczbę z jednego
rachunku (41 jednostek siatki) z etykietą z drugiego (45 linii tekstu). Pełna kolumna to
**45 linii**, bo tyle mieści się w 251 mm - i wtedy dryf wynosi 20,86 mm, nie 19. Strona
projektowa jest bliżej prawdy niż repozytorium, ale jej 20,70 mm pochodzi z mnożenia przez
wartość już zaokrągloną, więc gubi 0,16 mm.

Co ten rachunek **obala**: twierdzenie, że jednostka 6 mm może służyć jako siatka linii bazowych.
Nie może - i to ustalenie stoi tym mocniej, bo poprawiona liczba jest większa, nie mniejsza.
Czego **nie obala**: rozstrzygnięcia o marginesie dolnym 28 mm. Ono nie zależało od tej liczby.

### 4.3 Obwiednia znaku widocznego - skutek współczynników 0,655 / 0,561

Pomiar `bbox.mjs`: suma obwiedni wszystkich kształtów rysowanych, z pominięciem przezroczystego
prostokąta `fill="none"`.

| Plik | viewBox | Obwiednia widoczna | Udział szerokości |
|---|---|---|---|
| `logo_irin_poziom.svg` | 281,333 x 158,667 | 184,213 x 38,854 | **0,6548** |
| `logo_irin_pion.svg` | 184,837 x 162,834 | 103,728 x 87,312 | **0,5612** |
| `logo_irin_sygnet.svg` | 184,837 x 162,834 | 103,728 x 38,853 | **0,5612** |

**To jest realny problem specyfikacji, nie ciekawostka.** `logotyp.md:27-29` mówi „minimum
18 mm szerokości" i nie mówi, czy chodzi o szerokość pliku, czy o szerokość znaku. Różnica:

```
poziom, ramka 18 mm  -> znak widoczny 11,79 mm     (18 x 0,6548)
pion,   ramka 18 mm  -> znak widoczny 10,10 mm     (18 x 0,5612)
sygnet, ramka 10 mm  -> znak widoczny  5,61 mm     (10 x 0,5612)
ekran,  ramka 90 px  -> poziom 58,9 px, pion 50,5 px
ekran,  ramka 44 px  -> sygnet 24,7 px
```

Wstawiony dziś w 18 mm znak poziomy daje **11,79 mm faktycznego znaku** - o 35 % mniej, niż
sugeruje liczba w specyfikacji. Sygnet w 10 mm daje 5,61 mm.

**Hipoteza, nie ustalenie:** 18 x 0,5612 = 10,10 mm, czyli prawie dokładnie „10 mm" z wiersza
o sygnecie. Możliwe, że minimum sygnetu zostało w kanwie foundera zmierzone jako *widoczna*
szerokość znaku w ramce 18 mm. Falsyfikator: pytanie do foundera, którą krawędź mierzył.
Do czasu odpowiedzi to zbieg liczb, nie wyjaśnienie.

Pilot używa dziś `width: 42mm` (papier), `30mm` (wizytówka awers), `24mm` (strona kolejna)
i `10mm` (sygnet na rewersie) - liczone na ramce pliku. Przy odczycie „18 mm = znak widoczny"
sygnet 10 mm łamie minimum; przy odczycie „18 mm = ramka" nie łamie. Pomiar 4 z protokołu
pilota mierzy dziś nie tę wielkość, o którą chodzi.

### 4.4 Procent zadruku akcentem

Podstawa - pole treści A4:
```
szer = 210 - 20 - 20 = 170 mm ;  wys = 297 - 18 - 28 = 251 mm
pole = 170 x 251 = 42 670 mm2 = 426,70 cm2       <- zgodne z liczbą strony projektowej
5 %  = 2 133,50 mm2 = 21,34 cm2                   <- zgodne
suma siatki: 6 x 25 + 5 x 4 = 170 mm = szerokość pola treści, dopasowanie dokładne
```

Zadruk Złotem foliowym `#A8874E` na czterech nośnikach pilota - jedyne w repozytorium nośniki
z podaną powierzchnią:

| Nośnik | Element | Wymiar | Powierzchnia | % pola treści | % całego nośnika |
|---|---|---|---|---|---|
| Papier firmowy s.1 (`Main.dc.html:44`) | kreska ozdobna, 6 kolumn | 170 x 0,5 mm | 85,00 mm2 | **0,20 %** | 0,14 % |
| Papier firmowy s.kolejna (`StronaKolejna.dc.html:36`) | kreska ozdobna, 6 kolumn | 170 x 0,5 mm | 85,00 mm2 | **0,20 %** | 0,14 % |
| Wizytówka awers (`WizytowkaAwers.dc.html:22`) | kreska pod stanowiskiem | 12 x 0,5 mm | 6,00 mm2 | **0,19 %** | 0,13 % |
| Wizytówka rewers (`WizytowkaRewers.dc.html:19`) | kreska pod sygnetem | 10 x 0,5 mm | 5,00 mm2 | **0,16 %** | 0,11 % |

Podstawa dla wizytówki: pole treści 73 x 43 mm = 3 139 mm2 (85 x 55 minus padding 6 mm),
cały nośnik 85 x 55 = 4 675 mm2.

**Limit wykorzystany w 3,98 %** (85,00 / 2 133,50). Zapas jest tak duży, że limit 5 % nie jest
dziś ograniczeniem dla żadnego nośnika - jest liczbą, której nikt nie dotyka.

**Rozjazd interpretacyjny, nie liczbowy.** Strona projektowa nazywa 21,34 cm2 „limitem złota".
W tym repozytorium (`paleta-barw.md:96`, `palette-irin.json:359`) pasmo 5 % dzieli **pięć
kolorów**: Patyna, Werdykt, Rubryka, Karmin i Złoto foliowe razem. Przypisanie całych 5 %
samemu złotu jest rozluźnieniem reguły, a nie jej zapisaniem. Pytanie 3 w rozdz. 8.

---

## 5. Kompatybilność

| Co | Komenda | Wynik | Wniosek |
|---|---|---|---|
| Build | `npm ci` | `npm error EUSAGE`; `ls package.json` -> brak pliku | **Nie ma czego budować.** Paczka to statyczne CSS, JSON, HTML i Markdown. „Czysty klon się buduje" jest tu pytaniem bez treści. |
| Zależności przeterminowane | `npm outdated` | brak wyjścia (brak projektu) | **Zero zależności runtime.** Nie ma czego aktualizować ani czym się zatruć. |
| Podatności | `npm audit` | `npm error ENOLOCK` | j.w. |
| Martwe zależności | - | nieuruchamiane, brak manifestu | j.w. |
| Node | `node -v` | v22.22.2 (tylko do skryptów pomiarowych) | wersja nieistotna dla paczki |
| Konsument: ładowanie bez bundlera | `ladowanie.mjs` - 8 kart przez `http://127.0.0.1:8099`, Chromium | **8 z 8 bez błędu**; zero błędów konsoli, zero żądań 4xx, zero `requestfailed` | **Ładuje się surowo.** Zero `import`, zero `type="module"`, zero JSX w całej paczce. `styles.css` przez `<link>` ciągnie `@import` fontów i tokenów, oba się rozwiązują. |
| Tokeny po stronie przeglądarki | j.w., `getComputedStyle` | `--irin-surface: #FBF8F2`, `--irin-border: #7D7466`, `--irin-accent: #A8874E`, `--irin-modul: 25mm` | wartości obowiązujące, nie poprzednie |
| Fonty: skąd | `fonts.css` | 4 x `@font-face`, `src: url(data:font/woff2;base64,…)`, **zero żądań sieciowych** | osadzone; commit `1ad0f9b` „koniec zależności od pobrania z sieci" jest prawdziwy |
| Fonty: diakrytyki **glif po glifie** | `glify.py` - `cmap` z rozpakowanych woff2 | `ĄĆĘŁŃÓŚŹŻ ąćęłńóśźż`: **18/18 dla Manrope, 18/18 dla Inconsolaty**. Podział: Ó i ó w podzbiorze `latin`, pozostałe 16 w `latin-ext`; `unicode-range` kieruje do właściwego kroju. **Każdy z 18 glifów ma niepusty kontur** (`BoundsPen`), więc żaden nie jest pustą ramką. | **Pokrycie pełne, potwierdzone glif po glifie.** Idzie dalej niż „potwierdzone zakresowo" ze strony projektowej. |
| Fonty: różnice między wagami | j.w., tabela `fvar` | **oba kroje są zmienne**: Manrope oś `wght` 200-800, Inconsolata oś `wght` 200-900 (CSS ogranicza do 300-700). Jeden zestaw glifów na całą oś. | **Pokrycie nie może różnić się między wagami** - to nie jest pomiar na próbie, tylko własność pliku. Falsyfikator „wagi 500 i 600 nie sprawdzone" **jest tym zamknięty na poziomie pokrycia**, ale nie na poziomie druku (rozdz. 7). |
| Fonty: licencja | `licencja.py`, tabela `name` | Manrope 4.504, Inconsolata 3.001; oba niosą `Copyright … Project Authors` i URL licencji `http://scripts.sil.org/OFL`. **W repozytorium nie ma pliku licencji** - `find -iname 'license*' -o -iname 'OFL*'` zwraca pusto. | Osadzenie jest **dozwolone** (SIL OFL na to pozwala wprost), ale OFL wymaga, żeby tekst licencji podróżował z fontem. **Brak pliku OFL przy `fonts.css` to naruszenie warunku dystrybucji.** Poprawka: dołożyć `_robocze/ds-bundle/fonts/OFL.txt`. |
| Druk: reguły | `grep -rn '@media print\|print-color-adjust\|@page'` | **zero trafień w całym repozytorium** | **Paczka nie ma ani jednej reguły druku.** Bez `print-color-adjust: exact` przeglądarka domyślnie **wygasza tła** przy drukowaniu, więc Pergamin pod calloutem i Kaszmir pod kartą znikną. Dla systemu, którego `ds-bundle/README.md:4` opisuje jako „służący dokumentom drukowanym", to jest luka, nie szczegół. |
| Druk: jednostki | przegląd `styles.css`, `tokens.css` | siatka, marginesy i grubości linii **w mm** (`25mm`, `4mm`, `.25mm`, `.5mm`); **cała skala typograficzna w px** (72, 40, 24, 16, 13,5, 10, 14, 52, 10,5) | mieszanka celowa i opisana (`typografia.md:35`), ale px zależy od zoomu i DPI kontekstu. Przy druku przez przeglądarkę 1 px = 1/96 cala tylko domyślnie. |

---

## 6. Aktualność - co jest z której epoki

Całe repozytorium powstało w dwóch dniach: **2026-09-02 i 2026-09-03**. Ostatni commit
na `main` to `e16b944`. Od 2026-09-03 nic nie ruszało kodu; dzisiejsza data to 2026-09-09,
czyli paczka stoi nietknięta 6 dni.

| Warstwa | Ostatnia zmiana | Uwaga |
|---|---|---|
| `styles.css`, `fonts/fonts.css` | 2026-09-03T05:18:43 | najmłodsze pliki w repozytorium |
| `tokens.css`, `palette-irin.json`, karty, `guidelines/` | 2026-09-03T05:14:01 | jeden commit synchronizacji, `19691a4` |
| `01-baza-wiedzy/identyfikacja/` | 2026-09-03T04:49:42 | **starsza o 24 minuty od paczki** |
| pilot papieru firmowego | 2026-09-03T04:06:51 | starszy o 68 minut |
| warianty księgi marki | 2026-09-03T03:21:04 | **starsze o 45 minut od poprawki Popiołu** - stąd R3 |
| `brandbook.dc.html` | 2026-09-02T01:32:23 | kanwa foundera, punkt wyjścia, nie specyfikacja |
| `_robocze/copilot-v1/` | 2026-09-02T00:19:12 | 29 plików po angielsku, z innego podejścia; nietknięte |

**Odpowiedź na pytanie „dlaczego karty renderują poprzednią paletę": nie renderują.** Kolejność
jest tu odwrotna niż w hipotezie ze strony projektowej - tokeny i karty zmieniono **jednym
commitem**, o 24 minuty **później** niż specyfikacje warstwy 1, więc karty są młodsze od źródła
prawdy, nie starsze. Zmierzone w przeglądarce, rozdz. 3.2.

**Ślady palet wycofanych.** Nazw „Oliwin", „Kość Słoniowa", „Atrament" (jako koloru), „Regalia”
w repozytorium **nie ma ani razu**. Nazwy Muślin, Espresso, Popiół, Aksamit, Miedź, Onyks
i Pergamin występują 427 razy łącznie, ale to nie są ślady palety wycofanej - **to jest paleta
obowiązująca**. Wycofanych hexów żywych jest dokładnie jeden przypadek: `#938978` w trzech
plikach wariantów księgi marki (R3). Wszystkie pozostałe stoją w kontekstach jawnie opisanych
jako historia albo archiwum.

**Odwołania do ścieżek nieistniejących:** 17, wszystkie w `_robocze/ds-bundle/guidelines/`,
opisane jako R4. `brandbook.dc.html` **istnieje** i wszystkie 48 odwołań do niego są poprawne.
`01-baza-wiedzy/identyfikacja/*.md` **istnieją** - urwane są tylko ścieżki *wewnątrz paczki*,
która trafia na drugą stronę bez tego katalogu. Dla czytelnika po stronie projektowej te
ścieżki faktycznie prowadzą donikąd i podejrzenie z promptu jest trafne.

---

## 7. Czego nie zmierzyłem i dlaczego

Rozdział najważniejszy. Poniżej wszystko, czego ten raport **nie** rozstrzyga.

1. **Nie widziałem strony projektowej.** Nie mam dostępu do projektu Claude Design, więc nie
   sprawdziłem: `_ds_manifest.json`, `_ds_bundle.js`, folderu `templates/`, dokumentów
   wzorcowych, ani pliku `_robocze/wykonanie-decyzji-2026-09-09.md`, do którego prompt odsyła
   jako do wejścia w etap 3. **Wszystkie zdania tego raportu o stronie projektowej opierają się
   wyłącznie na treści promptu**, a prompt sam każe traktować takie treści jak hipotezy.
   Konsekwencja: nie wiem, czy „Regalia” to paleta nowsza od „Kaszmiru Wyciszonego", czy raport
   projektowy opisuje inne repozytorium. **Bez tej odpowiedzi etap 3 nie ma na czym stanąć.**

2. **Nie było wydruku.** Trzy falsyfikatory zostają otwarte i muszą być tak oznaczone:
   - grubość linii struktury 0,25 mm (Popiół) i kreski ozdobnej 0,5 mm (Złoto foliowe) - czy
     drukarka biurowa je kładzie. Kontrast policzony, raster nie sprawdzony.
   - minimalny rozmiar samodzielnego sygnetu 10 mm / 44 px - i teraz dodatkowo obciążony
     pytaniem z rozdz. 4.3, którą krawędź mierzy.
   - **czytelność** diakrytyków na papierze przy wagach 500 i 600. Pokrycie glifami zamknąłem
     (18/18, kontury niepuste, kroje zmienne), ale to jest twierdzenie o zawartości pliku,
     **nie o wyglądzie ogonka przy 8 pt na wydruku**. Cieńsze wagi mają cieńsze kreski;
     pokrycie tego nie mierzy.

3. **Nie renderowałem kart w Claude Design, tylko w Chromium.** Osiem kart ładuje się bez błędu
   na serwerze lokalnym. To nie dowodzi, że ładują się tak samo w piaskowanej ramce panelu
   Design System - `fonts.css:2-5` sam podaje piaskownicę jako powód osadzenia fontów, więc
   różnice środowiska są tam znane i realne.

4. **Nie sprawdziłem, czy `support.js` dostarcza środowisko** (R6). Cztery artboardy pilota
   go wołają, w repozytorium go nie ma. Zakładam, że pochodzi z runtime'u Claude Design,
   ale to założenie, nie pomiar.

5. **Nie mierzyłem objętości dokumentu w wariancie 1** księgi marki. `PLAN.md` sam wskazuje ten
   pomiar jako otwarty („złożyć jeden realny dokument z warstwy 2 i policzyć strony") i nic
   w moich danych go nie zastępuje.

6. **Nie zweryfikowałem żadnej treści prawnej.** Osiem plików w `01-baza-wiedzy/prawo/` i dziesięć
   PDF-ów źródłowych zostawiłem nietknięte - pomiar dotyczył identyfikacji, nie zgodności
   z przepisami.

7. **Nie policzyłem kontrastu na tłach spoza palety** - zdjęcie, skan, papier inny niż biały
   maszynowy. `paleta-barw.md:74` wprost to wyłącza i ja też nie mam na to danych.

8. **Nie sprawdziłem, czy `_ds_needs_recompile` cokolwiek robi.** Plik zawiera `1` i nic
   w repozytorium go nie czyta.

**Udział pozycji niesklasyfikowanych.** Prompt każe podać go przy klasyfikacji zbioru.
Zbiór: 7 pozycji zgłoszonych do `/design-sync`. Sklasyfikowane: 7 (4 fałszywe, 1 potwierdzona,
1 obie strony błędne, 1 już zrobiona). **Niesklasyfikowane: 0, czyli 0 %** - poniżej progu 5 %,
więc wniosek z tego pomiaru wolno wyciągać.

---

## 8. Pytania do właściciela

Otwarte decyzje w jednym zdaniu każda, w kolejności zależności:
(1) czym jest „Regalia” wobec „Kaszmiru Wyciszonego"; (2) czy 8,5 px wchodzi jako poziom skali;
(3) czy 5 % to limit samego złota, czy pasma pięciu kolorów; (4) czy karty podglądu mają być
w manifeście; (5) czy paczka dostaje reguły druku; (6) czy poprawiam wariant 1 księgi marki;
(7) którą krawędź znaku mierzy minimum 18 mm.

Pierwsze jest jedyne blokujące - reszta czeka na jego odpowiedź, bo jeśli obowiązuje inna
paleta, część pozostałych pytań przestaje mieć sens.

---

**1. Czym jest paleta „Regalia” wobec obowiązującego tu „Kaszmiru Wyciszonego"?**
W repozytorium nie ma jej ani razu; prefiks `--irin-r-`, `_ds_manifest.json`, `_ds_bundle.js`
i blok poprzedniej palety w `tokens.css` też nie istnieją (rozdz. 3.3).

- **A. „Regalia” to nowsza paleta, którą strona projektowa już przyjęła.** Wtedy tu brakuje
  całej decyzji: 14 nowych hexów, nowy prefiks, nowe kontrasty do przeliczenia od zera.
- **B. Raport projektowy opisuje inną paczkę albo inne repozytorium.** Wtedy niczego nie
  zmieniam, a lista siedmiu pozycji do `/design-sync` odpada w całości.

**Rekomendacja: B, i to nie z ostrożności, tylko z liczb.** Cztery z siedmiu pozycji tamtej
listy są sprawdzalnie fałszywe wobec tego repozytorium (karty renderują paletę bieżącą - 8 z 8
zmierzonych w przeglądarce; `styles.css` nie ma ani jednego literalnego hexa; NIP jest już
ciągiem we wszystkich 7 miejscach; `_ds_manifest.json` nie istnieje). Lista opisująca stan,
którego w czterech na siedem punktów nie ma, opisuje coś innego. **Falsyfikator, który to obali:
pokaż mi 14 hexów Regalii albo commit, w którym tu weszły.** Jeden taki dowód przewraca
rekomendację na A.

---

**2. Czy 8,5 px wchodzi do systemu, i jako co?**
Dziś ta liczba żyje wyłącznie w kanwie foundera (`brandbook.dc.html`, 4 stopki). Rachunek:
8,5 x 0,75 = **6,375 pt = 6,38 pt**, nie 6,40.

- **A. Jako jedenasty poziom skali** w `styles.css`, `typografia.md` i karcie `Typografia`.
- **B. Jako podłoga składu** - zapis „niżej niż 8,5 px nie schodzimy", bez własnej klasy.

**Rekomendacja: B.** Dodanie jedenastego poziomu daje projektantowi nowy stopień do wyboru
tam, gdzie dziś sięga po 10 px; podłoga niczego nie dodaje, a odcina dół. 6,38 pt to rozmiar,
przy którym Manrope na wadze 400 na papierze offsetowym jest już na granicy - a wydruku
próbnego nie było (rozdz. 7 pkt 2), więc **nie mam dowodu, że ten stopień w ogóle się drukuje**.
Wpuszczanie go jako pełnoprawnego poziomu skali przed wydrukiem to zapisanie wartości
niesprawdzonej jako ustalonej.

---

**3. Limit 5 % dotyczy samego Złota foliowego czy całego pasma pięciu kolorów?**
`paleta-barw.md:96` przypisuje 5 % pięciu kolorom razem (Patyna, Werdykt, Rubryka, Karmin,
Złoto foliowe). Strona projektowa liczy 21,34 cm2 jako limit samego złota.

- **A. Pasmo dzielone, tak jak dziś** - suma pięciu kolorów nie przekracza 21,34 cm2.
- **B. Limit osobny dla złota**, pozostałe cztery bez własnego pułapu.

**Rekomendacja: A**, bo tak stoi w zatwierdzonej specyfikacji i zmiana wymagałaby decyzji,
nie doprecyzowania. Koszt jest dziś zerowy: pilot wykorzystuje **3,98 % limitu**
(85,00 z 2 133,50 mm2), więc przy żadnym z czterech nośników rozstrzygnięcie niczego nie zmienia.
Zmieni, gdy pojawi się dokument ze statusami - certyfikat albo karta usługi BUR, gdzie Werdykt,
Rubryka i Karmin wejdą jako plakietki.

---

**4. Czy 8 kart podglądu ma być widoczne w manifeście paczki?**
Komponentów kodowych nie ma i nie planowano - karty to samodzielne HTML-e z `@dsCard`.

- **A. Pusta lista zostaje** - manifest opisuje komponenty do importu, a takich nie ma.
- **B. Manifest wymienia 8 kart** jako zawartość podglądu.

**Rekomendacja: A.** Wpisanie kart do listy komponentów obiecuje agentowi projektowemu coś,
czego nie dostanie - `ds-bundle/README.md:14` mówi wprost „ten system nie ma komponentów
w kodzie". Pusta lista jest prawdziwa; niepusta byłaby wygodna i myląca.

---

**5. Czy paczka dostaje reguły druku?**
Dziś **zero** wystąpień `@media print`, `print-color-adjust` i `@page` w całym repozytorium.
Bez `print-color-adjust: exact` tła Pergaminu i Kaszmiru znikają przy drukowaniu z przeglądarki.

- **A. Tak, do `styles.css`** - blok `@media print` z `print-color-adjust: exact` i `@page`
  z formatem A4 i marginesami zerowymi (marginesy niesie już layout dokumentu).
- **B. Nie** - druk idzie przez eksport PDF z Claude Design, więc reguły CSS są bez znaczenia.

**Rekomendacja: A.** `ds-bundle/README.md:4` opisuje ten system jako służący „dokumentom
drukowanym i do wysyłki w PDF". System o takim opisie, który przy `Ctrl+P` gubi wszystkie tła,
ma lukę w miejscu swojego głównego zastosowania. Koszt: kilkanaście wierszy CSS. Ryzyko
odwrotne - że ktoś raz wydrukuje kartę usługi z białym tłem zamiast Pergaminu i nie zauważy.

---

**6. Czy poprawiam `#938978` na `#7D7466` w wariancie 1 księgi marki?**
Founder wybrał wariant 1; pliki są o 45 minut starsze od poprawki Popiołu, więc niosą wartość,
która daje 2,61:1 na Pergaminie przy progu 3:1.

- **A. Poprawić wszystkie trzy warianty** (2 wystąpienia w każdym, 6 razem).
- **B. Poprawić tylko wariant 1**, dwa pozostałe zostawić jako archiwum stanu z 03:21.

**Rekomendacja: A**, mimo że warianty 2 i 3 są archiwum. Powód: podmiana jest mechaniczna
i sprawdzalna (`sed`, 6 wystąpień, `grep` potwierdza zero pozostałych), a archiwum niosące
wartość poniżej progu dostępności jest pułapką dla następnego czytelnika dokładnie tak samo
jak plik żywy. **Uwaga: to jest zmiana kodu i etap 1 jej nie obejmuje** - czeka na etap 3.

---

**7. Minimum 18 mm mierzy szerokość pliku czy szerokość znaku widocznego?**
Zmierzone: znak zajmuje 0,655 szerokości pliku (poziom) i 0,561 (pion, sygnet). Przy odczycie
„ramka" znak poziomy w minimum ma faktycznie 11,79 mm.

- **A. Ramka pliku** - dzisiejszy pilot jest zgodny, nic nie trzeba ruszać, ale realny znak
  bywa o 35 % mniejszy od liczby w specyfikacji.
- **B. Znak widoczny** - wtedy `logotyp.md` dostaje przeliczone ramki (27,49 mm dla poziomego,
  32,08 mm dla pionowego i sygnetu), a sygnet 10 mm na rewersie wizytówki łamie minimum.

**Rekomendacja: B, ale bez zmiany liczby, tylko z dopisaniem, którą krawędź mierzy.**
Minimalny rozmiar istnieje po to, żeby znak był czytelny - a czytelność zależy od znaku,
nie od przezroczystego marginesu wokół niego. Zapis, który mierzy ramkę, mierzy nie to,
co miał chronić. **Falsyfikator: jeśli founder mierzył 18 mm linijką na wydruku ramki,
odpowiedź brzmi A** i wtedy w specyfikacji trzeba dopisać, że realny znak ma 11,79 mm -
też jawnie, bo dziś tego nie widać nigdzie.

---

## Koniec etapu 1

Zgodnie z poleceniem: **zatrzymuję się.** Nie przechodzę do etapu 2 i nie zmieniam żadnego
pliku poza tym raportem. Etap 2 zaczyna się od Twojej odpowiedzi na pytanie 1 - reszta
od niej zależy.

---

# 9. Uzupełnienie z 2026-09-09: paleta Regalia, po odczycie projektu Claude Design

Właściciel wskazał plik `irn-design-ksiega-koloru.html` jako miejsce, w którym leży paleta
obowiązująca, i polecił sprawdzić, czy właściwe pliki jej używają. Dostęp do projektu
`System projektowy IRIN` (`1a22ce64-0e1c-43a6-bd60-eef9241ef73b`) okazał się możliwy przez
`DesignSync`, metody `list_files` i `get_file`. Ten rozdział zastępuje domysły z rozdz. 3.3 i 7
pomiarem.

## 9.0 Korekta

**Rekomendacja B w pytaniu 1 rozdz. 8 była błędna.** Postawiłem tam, że raport projektowy opisuje
inne repozytorium, i podałem falsyfikator: „pokaż mi 14 hexów Regalii albo commit, w którym tu
weszły”. **Falsyfikator zadziałał.** Regalia istnieje, jest zatwierdzona 2026-09-03 i dopisana do
`tokens/tokens.css` po stronie projektowej 2026-09-06. Obowiązuje odpowiedź **A**: to jest paleta
nowsza, a repozytorium za nią nie nadąża.

Cztery pozycje, które w rozdz. 3.2 nazwałem fałszywymi, były prawdziwe **wobec repozytorium**
i pozostają prawdziwe w tym zakresie - ale opisywały stan strony projektowej, nie tego
repozytorium, i tam mają inne rozstrzygnięcie. Rozbicie w rozdz. 9.5.

## 9.1 Regalia - 14 wartości, sprawdzone od zera

Paleta leży w dwóch miejscach po stronie projektowej: jako drugi blok `:root` w `tokens/tokens.css`
(prefiks `--irin-r-*`, dopisany 2026-09-06) i jako dokument `irn-design-ksiega-koloru.html`.

| # | Nazwa | Hex | Rola | na Kości Słoniowej |
|---|---|---|---|---|
| 01 | Szafir Nocny | `#132246` | kolor marki, CTA, pas nagłówkowy | 14,09 |
| 02 | Atrament | `#07090C` | typografia główna | **17,99** |
| 03 | Kość Słoniowa | `#F7F3E9` | tło strony | tło |
| 04 | Aksamit Nocy | `#080F1F` | tło ciemne, stopka, okładka | 17,25 (odwrócone) |
| 05 | Alabaster | `#E4E1D8` | tła kart, tekst drugi na ciemnym | 1,18 |
| 06 | Grafit Jedwabny | `#606369` | tekst drugi na jasnym, linie 0,25 mm | 5,44 |
| 07 | Złoto Szampańskie | `#C4B790` | akcent do 5 %, wyłącznie linia i tłoczenie | **1,80 - zakaz tekstu** |
| 08 | Ametyst Dworski | `#331F41` | materiał przekrojowy | 13,41 |
| 09 | Muszla Różana | `#E8D6D6` | cytaty, podświetlenia | 1,26 |
| 10 | Lapis Stonowany | `#305686` | odnośniki, focus | 6,77 |
| 11 | Złoto Antyczne | `#75674B` | metadane | 4,99 |
| 12 | Rubin Głęboki | `#541319` | barwa dostępna, nieprzypisana | 12,77 |
| 13 | Zieleń Butelkowa | `#0B3627` | barwa dostępna, nieprzypisana | 12,06 |
| 14 | Bursztyn Wyciszony | `#9B5E30` | barwa dostępna, nieprzypisana | 4,69 |

Plus cztery tinty 12 %: `#DCDAD5` (Szafir), `#E3D8D0` (Rubin), `#DBDCD2` (Zieleń), `#DFDAD5` (Ametyst).

**Wynik weryfikacji (`regalia.py`, `reg2.py`): 30 z 30 zadeklarowanych wartości odtworzyło się
co do setnej.** 23 kontrasty z `tokens.css`, 7 z `irn-design-paleta-kolorow.html`, zero rozjazdów
powyżej 0,05. Cztery tinty odtworzyły się **co do bajtu** z mieszania 12 % barwy na Kości Słoniowej.
Limit złota: 170 × 251 mm = 426,70 cm², 5 % = 21,34 cm² - zgodne z `--irin-r-limit-zlota-cm2`.

**Regalia jest paletą zmierzoną, nie deklarowaną.** To jest jej mocna strona i trzeba to powiedzieć
przed listą rozjazdów.

## 9.2 Odpowiedź na pytanie właściciela: które pliki jej używają

Pokrycie pełne, bez próbkowania: **16 z 16 szablonów, 8 z 8 kart, 4 z 4 dokumentów, oba arkusze,
oba pliki tokenów. Pozycji niesklasyfikowanych: 0, czyli 0 %.**

### Po stronie projektowej - na Regalii

| Plik | Jak używa |
|---|---|
| `tokens/tokens.css`, drugi blok `:root` | 14 barw + 4 tinty + gniazdo `--irin-r-dziedzina` + limit |
| `irn-design-ksiega-koloru.html` | 325 wystąpień hexów Regalii, zero obcych |
| `irn-design-brandbook.html` | 97 wystąpień; 4 hexy palety v2 stoją wyłącznie w prozie o historii |
| `irn-design-ksiega-znaku.html` | 188 wystąpień; 10 obcych, wszystkie w prozie o historii |
| `irn-design-paleta-kolorow.html` | pełna tabela 14 wartości z CMYK i OKLCH |
| **16 z 16 szablonów w `templates/`** | hexy Regalii wprost; 6 z nich czyta obszar z `--irin-r-dziedzina` |

### Po stronie projektowej - NIE na Regalii

| Plik | Co niesie | Skutek |
|---|---|---|
| `styles.css` | wyłącznie `var(--irin-*)`, zero `--irin-r-*` | arkusz bazowy, wpisany w `_ds_manifest.json` jako globalny, rozwiązuje się do palety v5.1 |
| **8 z 8 kart** w `components/` | `var(--irin-*)` plus hexy v2 wpisane wprost | patrz 9.5 |
| `tokens/palette-irin.json` | v5.1.0 „Kaszmir Wyciszony - siedem kolorów głównych” | dane maszynowe **nie znają Regalii w ogóle** |

### W repozytorium - zero Regalii

`grep` po całym repozytorium: **„Regalia” 0 wystąpień, prefiks `--irin-r-` 0 wystąpień, żaden
z 14 hexów Regalii nie występuje ani razu.** Wszystkie cztery specyfikacje warstwy 1,
`tokens.css`, `styles.css`, `palette-irin.json`, 8 kart i pilot papieru firmowego niosą paletę
**v2 „Kaszmir Wyciszony”** z 2026-09-02.

**Odpowiedź brzmi: nie, repozytorium nie jest zaktualizowane - i jest za Regalią nie o jeden krok,
tylko o dwa.**

```
repozytorium         v2   (2026-09-02)  Aksamit #452430 · Miedź #7A5638 · Onyks #33474F · 3 dziedziny
projekt, --irin-*    v5.1 (2026-09-03)  Aksamit #752F3F · Bursztyn #9F6631 · Onyks #005A80 · 6 dziedzin
projekt, --irin-r-*  Regalia (2026-09-03, dopisana 2026-09-06)  Szafir #132246 · gniazdo dziedziny
```

Repozytorium nie zna ani v3, ani v4, ani v4.1, ani v5, ani v5.1, ani Regalii. Po stronie
projektowej `_archiwum/iteracje-palety/` niesie ślady wszystkich sześciu iteracji.

## 9.3 Odwołanie w kółko - najpoważniejszy skutek

Komentarz otwierający blok Regalii w projektowym `tokens/tokens.css` brzmi:

> „Zrodlo prawdy: 01-baza-wiedzy/identyfikacja/paleta-barw.md w repozytorium.”

**Ten plik w repozytorium nie zawiera Regalii.** Zawiera 14 kolorów v2, nagłówek
„Status: ZATWIERDZONA przez foundera (2026-09-02)” i zdanie „To jest jedyne źródło prawdy dla
kolorów IRIN”. Ta sama deklaracja stoi w `tokens/palette-irin.json` po stronie projektowej,
w kluczu `specyfikacja-obowiazujaca`.

Skutek praktyczny: **każdy, kto pójdzie za wskazaniem źródła prawdy, wyląduje na palecie sprzed
sześciu dni i dwóch pokoleń.** To nie jest rozjazd wartości, tylko rozjazd samego wskaźnika, i on
psuje wszystkie pozostałe: dopóki repozytorium nie zna Regalii, `/design-sync` z repozytorium do
projektu **nadpisze Regalię paletą v2**.

## 9.4 Reguła synchronizacji została złamana w drugą stronę

`/CLAUDE.md` i prompt etapu 3 mówią zgodnie: hex, token, arkusz i komponent zmienia się
**w repozytorium**, a potem idzie sync; po stronie projektowej wszystko poza `templates/` jest
tylko do odczytu.

Zmierzony stan: `tokens/tokens.css` i `tokens/palette-irin.json` po stronie projektowej zostały
zmienione **tam**, nie tu - repozytorium nie ma ani bloku Regalii, ani żadnej z wersji v3-v5.1.
To są dokładnie te pliki, których reguła zabrania edytować po tamtej stronie.

Nie oceniam tej decyzji - praca w tamtym oknie była zmierzona i udokumentowana. Nazywam skutek:
**dwa źródła tokenów rozeszły się i żadne nie wie o drugim.**

## 9.5 Rozjazdy zmierzone przy tej okazji

| # | Rozjazd | Jest | Ma być | Podstawa |
|---|---|---|---|---|
| R7 | `quaternary` (Rubin `#905E88`) na Kaszmirze, `tokens/palette-irin.json`, tablica `kontrasty` | **10,62** | **4,78** | 10,62 to kontrast **wycofanego Oliwinu** `#3D3D00` (odtworzone co do setnej). Etykieta wiersza nadal brzmi „quaternary (Oliwin)”. Wymiana Oliwin → Rubin w v5.1 nie pociągnęła przeliczenia. |
| R8 | etykieta Pergamin na `quaternary`, tamże | **8,51** | **3,83** | ta sama przyczyna (8,51 to Pergamin na Oliwinie). **3,83 jest poniżej progu 4,5 dla tekstu.** Klucz `tokeny.quaternary` podaje inną etykietę - biel, 5,07 - i ta liczba jest poprawna. Dwa miejsca w jednym pliku podają dwie różne etykiety dla tego samego wypełnienia. |
| R9 | etykieta biel na `warning`, tamże | **8,04** | **8,52** | 8,04 to wartość wiersza sąsiedniego („warning na surface”, odtworzone dokładnie). Liczba przepisana z sąsiedztwa. |
| R10 | `error` (Karmin) na Kaszmirze, tamże | **5,94** | **6,99** | Karmin na czterech tłach palety daje 6,99 / 6,63 / 5,60 / 7,41. **Wartości 5,94 nie odtworzyłem z żadnej pary** - pochodzenia nie ustaliłem. |
| R11 | 8 kart w `components/` po stronie projektowej | próbki i liczby palety v2 | wartości tokena, który te karty rozwiązują | `Paleta.html` wpisuje 14 hexów wprost; **6 z 14 nie zgadza się z `tokens.css` po tamtej stronie (42,9 %)**. `PlakietkaStatusu.html` renderuje `var(--irin-success/warning/info)`, czyli v5.1, a wypisuje obok liczby v2: Werdykt 6,62 wobec 7,36 · Rubryka 5,53 wobec 8,52 · Onyks 7,37 wobec 5,73. Karmin 5,60 zgodny, bo hex się nie zmienił. |
| R12 | `--irin-r-link` (Lapis `#305686`) na Aksamicie Nocy | **2,55** | brak pozycji na liście par zabronionych | Zmierzone. Aksamit Nocy jest zadeklarowanym tłem („sekcje, stopki, okładki wewnętrzne”), Lapis jest tokenem odnośnika. 2,55 jest **gorsze niż trzy z czterech par już wpisanych na listę** (3,17 · 3,46 · 3,68). Reguła **istnieje**, ale mieszka w prozie jednego szablonu (`templates/podpis-mailowy`), nie w tabeli par zabronionych w `tokens.css` ani w Księdze koloru. |
| R13 | `templates/okladka` - domyślny obszar | `'Szkolenia zawodowe'` (Rubin) | `'Bez obszaru'` (Szafir) | Decyzja z 2026-09-09: obszary są wymienne, gniazdo domyślnie neutralne. `karta-uslugi`, `karta-uslugi-bur` i `tabela-danych` mają domyślnie `'Bez obszaru'`; `okladka` i `slajd-16-9` mają `'Szkolenia zawodowe'`. Dwa szablony na szesnaście odstają od decyzji. |
| R14 | `templates/zestaw-drobnych`, kafel 01 | dwa akapity, drugi przeczy pierwszemu | jeden akapit | Pierwszy: „Stan niesie słowo, nie barwa - wszystkie cztery plakietki mają jedno wykonanie”. Drugi: „Każdy stan ma słowo **obok barwy**… Zieleń i Rubin schodzą do 70 % K”. Drugi opisuje wycofane wykonanie barwne i został przy poprawce. |
| R15 | `templates/okladka-wydawnicza`, protokół pomiaru | „znak … **95 mm** od góry” | 96 mm | Kod ustawia `top:96mm`, a punkt o rytmie w tym samym pliku wywodzi 96 mm i nazywa 95 mm wartością poprawioną. Trzeci punkt nie został przepisany. |

**Bilans weryfikacji tablicy `kontrasty` w projektowym `palette-irin.json` (v5.1): sprawdzonych 30,
rozjazdów powyżej 0,05 - cztery.** Dla porównania: Regalia 30 z 30 zgodnych, repozytorium 25 z 25
zgodnych. Wadliwa jest wyłącznie warstwa pośrednia v5.1, i to w wierszach, które przeżyły wymianę
koloru bez przeliczenia - dokładnie ten błąd, przed którym ostrzega zasada „nie przepisuj cudzych liczb”.

## 9.6 Czego w tym uzupełnieniu nie zmierzyłem

1. **Nie czytałem `_robocze/*.md` po stronie projektowej** - ani audytu z 2026-09-09, ani
   `wykonanie-decyzji-2026-09-09.md`, do którego odsyła prompt. Rozjazdy R7-R15 znalazłem własnym
   pomiarem; **nie wiem, które z nich tamte raporty już opisują.** Możliwe, że część jest tam
   zgłoszona i moja lista je powiela.
2. **Nie sprawdziłem `_archiwum/iteracje-palety/`** (v3 do v7, 20 plików). Wiem, że istnieją;
   nie wiem, czy któryś jest nadal cytowany jako obowiązujący.
3. **Nadal nie było wydruku.** Regalia dokłada własne falsyfikatory, wprost w niej zapisane:
   CMYK bez proofu, Złoto Szampańskie na papierze niepowlekanym (83 % krycia przy L\* 78),
   przypisanie barw do obszarów. Żadnego z nich ten pomiar nie zamyka.
4. **Nie renderowałem niczego po stronie projektowej** - wszystkie liczby pochodzą z odczytu
   plików i przeliczenia, nie z otwarcia kanwy.
5. **Nie ruszyłem ani jednego pliku** - ani tu, ani tam. To nadal jest etap 1.

## 9.7 Pytanie 1 postawione na nowo

Pytanie „czym jest Regalia” jest **zamknięte**: nowszą paletą, zatwierdzoną 2026-09-03. Na jego
miejsce wchodzi pytanie o kierunek naprawy, i ono jest teraz jedyne blokujące.

**Jak repozytorium ma dogonić Regalię?**

- **A. Repozytorium przyjmuje Regalię jako paletę obowiązującą warstwy 1.** Cztery specyfikacje,
  `tokens.css`, `styles.css`, `palette-irin.json` i 8 kart przechodzą na 14 wartości Regalii;
  paleta v2 zostaje w pliku jako historia, tak jak dziś zostaje historia palety 12-kolorowej.
  Po tym `/design-sync` znów działa w jedną stronę i niczego nie nadpisuje.
- **B. Repozytorium przyjmuje najpierw v5.1, potem Regalię.** Dwa kroki, dwa przeliczenia
  kontrastów, dwa wpisy w rejestrze decyzji.

**Rekomendacja: A.** Powód nie jest wygodą, tylko liczbą: v5.1 to warstwa, w której **cztery z 30
kontrastów są błędne** (R7-R10), z czego jeden - etykieta na wypełnieniu Rubinu, 3,83 wobec progu
4,5 - jest defektem dostępności, a nie literówką. Przejście przez tę warstwę oznacza wpisanie do
warstwy 1 wartości, które i tak trzeba by natychmiast poprawić. Regalia przeszła pełną weryfikację
w tej sesji: 30 z 30 kontrastów i 4 z 4 tinty odtworzone co do setnej.

**Falsyfikator tej rekomendacji:** jeżeli istnieje wydany materiał na palecie v5.1, którego nie
wolno przebarwić, to v5.1 musi zostać w repozytorium jako warstwa równoległa i odpowiedź brzmi B.
Po stronie projektowej taki materiał jest - `_archiwum/wydania-01/` niesie cztery pliki wydania 01,
a komentarz w `tokens.css` mówi wprost, że stary blok `--irin-*` zostaje właśnie dla nich.
**Czego nie wiem: czy któryś z nich jest w obiegu poza projektem.** To jedno zdanie od Ciebie
rozstrzyga A czy B.

**Pozostałe sześć pytań z rozdz. 8 zmienia adresata, nie treść.** Pytania 2 (8,5 px), 3 (limit
5 %), 6 (Popiół w wariancie księgi marki) i 7 (którą krawędź mierzy minimum 18 mm) są po stronie
projektowej **już rozstrzygnięte** decyzjami z 2026-09-09 - 8,5 px wszedł jako jedenasty poziom,
limit liczy się od 426,70 cm², minimum mierzy obwiednię znaku widocznego ze współczynnikami
0,655 i 0,561. Do repozytorium żadna z tych decyzji nie dotarła. Wejdą razem z Regalią, tym samym
ruchem - albo nie wejdą wcale.
