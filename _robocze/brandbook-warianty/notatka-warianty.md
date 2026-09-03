# Trzy warianty księgi marki — notatka warsztatowa

> **ROZSTRZYGNIĘTE 2026-09-03: founder wybrał wariant 1 „Kaszmir uporządkowany”** - wbrew rekomendacji z sekcji 5, świadomie. Zapis decyzji wraz z kosztem i pomiarem rozstrzygającym: `/PLAN.md`, sekcja „Decyzje foundera - rozstrzygnięte”. Warianty 2 i 3 zostają w tym katalogu jako archiwum.
>
> Przy okazji zamknięto punkt 1.4 tej notatki, pozycję pierwszą („czy pliki otworzą się w Claude Design”). **Założenie było błędne w obie strony**, sprawdzone 2026-09-03 na dokumentacji skilla `design`: runtime nie jest wstrzykiwany sam, wiersz `<script src="./support.js"></script>` musi stać w `<head>` dosłownie, a ścieżki obrazów muszą być samą nazwą pliku, bo seeder zapisuje je pod nazwą bazową - `../../logo_irin_poziom.svg` wyrenderowałoby się jako pusta ramka, bez ostrzeżenia. Obie rzeczy poprawione **wyłącznie w wariancie 1**; warianty 2 i 3 zostają z wadą, bo są archiwum, i przed ewentualnym użyciem wymagają tej samej poprawki.

**Status: propozycja w poligonie roboczym, nie specyfikacja.** `CLAUDE.md` tego repozytorium mówi,
że layout, kompozycja i grafika powstają wyłącznie w Claude Design. Te trzy pliki nie omijają tej
reguły — są materiałem wejściowym do rozmowy o kierunku i do zlecenia w Claude Design, leżą
w `_robocze/`, który `CLAUDE.md` nazywa poligonem roboczym, i **nie mają statusu źródła prawdy**.

Data: 2026-09-03. Gałąź: `warianty-brandbooka`. Nic nie zostało scommitowane ani wypchnięte.

---

## 1. Ryzyka — przed jakąkolwiek pochwałą

### 1.1. Znalazłem trzy pary poniżej progu, których `paleta-barw.md` nie wypisuje

Plik specyfikacji podaje kontrasty **na papierze Kaszmir**. Przeliczyłem wszystkie pary wzorem
WCAG 2.1 na luminancji względnej sRGB i na innych tłach trzy z nich nie przechodzą:

| Para | Kontrast | Próg | Skutek |
|---|---|---|---|
| Popiół `#938978` na Pergaminie `#E7DFD2` | **2,61:1** | 3:1 dla grafiki | linia tabeli i obrys karty **wewnątrz calloutu** są niewidoczne |
| Złoto foliowe `#A8874E` na Pergaminie `#E7DFD2` | **2,55:1** | 3:1 dla grafiki | cienka linia ozdobna na tle calloutu nie przechodzi |
| Rubryka `#8A6110` jako **tekst** na Pergaminie | **4,18:1** | 4,5:1 dla tekstu | ostrzeżenie pisane Rubryką w calloucie nie przechodzi AA |

Odtworzenie: `python3` ze wzorem WCAG na `01-baza-wiedzy/identyfikacja/tokeny/palette-irin.json`,
skrypt w treści tej sesji. Wszystkie trzy warianty tych par unikają — ale **specyfikacja
tego nie zabrania, bo o nich nie wie**. To jest wniosek do warstwy 1, nie do plików wariantów.
Nie poprawiam `paleta-barw.md`: zmiana pliku instrukcji jest decyzją właściciela.

### 1.2. Mój własny błąd, złapany przez miernik

Pierwsza wersja wszystkich trzech plików pisała etykietę na wypełnieniu Rubryki **Pergaminem**
(4,18:1), zamiast przepisanej w `paleta-barw.md` **bieli `#FFFFFF`** (5,53:1). To złamanie reguły 2
z `format-paczki.md` — kolor etykiety na wypełnieniu nie jest wyborem projektowym. Poprawione
w pięciu miejscach w trzech plikach; koszt: jedno przejście skryptu, bez przepisywania plików.

Wniosek: sam bym tego nie zauważył okiem, bo Pergamin na Rubryce wygląda poprawnie.
Miernik czytający tabelę nakazów wprost z pliku tokenów złapał to od razu.

### 1.3. Na pasie odwróconym żaden kolor dziedziny nie działa

Pomiar: Aksamit na Espresso **1,26:1**, Miedź **2,62:1**, Onyks **1,76:1**. Wszystkie trzy
poniżej 3:1, więc na czarnym pasie kolor dziedziny nie niesie żadnego sygnału.
Dotyczy to bezpośrednio wariantu 3, który stoi na pasach odwróconych — tam dziedzinę
sygnalizuje słowo i cienka linia Złota foliowego (5,09:1 na Espresso), nie barwa.

### 1.4. Trzy rzeczy, których nie zmierzyłem

- **Czy pliki otworzą się w Claude Design.** Pominąłem `<script src="./support.js">`, bo ta ścieżka
  nie istnieje w repozytorium — to jeden z zerwanych zasobów kanwy. Zakładam, że Claude Design
  wstrzykuje własny runtime przy otwarciu. **Falsyfikator: pierwszy import.** Jeśli się nie otworzy,
  wraca jedna linia w `<head>`.
- **Wydruk.** Wymiary pisane są w `mm`, więc przeglądarka mapuje je przez 96 dpi i siatka na ekranie
  jest tą samą siatką co na A4. Nie wydrukowałem żadnej strony ani nie wygenerowałem PDF.
- **Przepełnienie kolumn przy dłuższej treści.** Arkusze mają twarde `height:297mm` i `overflow:hidden`.
  Przy dłuższym tekście treść zostanie **ucięta bez ostrzeżenia**, nie przeleje się na kolejną stronę.

---

## 2. Co zmierzyłem w kanwie — z komendami

| Pomiar | Komenda | Wynik |
|---|---|---|
| Rozmiar | `wc -l -c brandbook.dc.html` | 534 wiersze, 54 859 bajtów |
| Sekcje | `grep -c '<section' brandbook.dc.html` | 9 |
| Zerwane zasoby | `grep -o 'src="[^"]*"' brandbook.dc.html \| sort \| uniq -c` | `uploads/…poziom.svg` ×8, `…pion.svg` ×2, `…sygnet.svg` ×1, `./support.js` ×1 |
| Brak katalogu | `ls uploads` | nie istnieje; trzy SVG leżą w korzeniu |
| Paleta | skrypt `python3` porównujący hexy z `tokeny/palette-irin.json` | tokeny 15, kanwa 16 unikalnych / 295 wystąpień, **część wspólna 0** |
| Moduł siatki | `grep -o 'moduł [0-9]* mm' brandbook.dc.html` | `moduł 32 mm` ×2 → 6 × 32 + 5 × 4 = 212 mm |

**Sprostowanie do pomiaru „kanwa nie zna poziomu H3”.** `grep -c 'H3'` daje 0, ale ten grep jest
czuły na wielkość liter: `grep -o '<h3' brandbook.dc.html | wc -l` daje **1**. W wierszu 311 kanwa
używa znacznika `<h3>` jako displayu 56 px / waga 200. Wniosek merytoryczny się nie zmienia
— *poziom typograficzny* H3 (Manrope 600 / 16 px) w kanwie nie istnieje — ale komenda mierzy
co innego, niż mówi jej opis.

---

## 3. Osie wariacji — dlaczego te trzy

Warianty różnią się **układem, rytmem i nośnikiem hierarchii**, nie doborem koloru.
Kolor dziedziny jest w każdym inny, ale to skutek reguły 1, a nie oś wariacji.

| | Wariant 1 · Kaszmir uporządkowany | Wariant 2 · Marginalia | Wariant 3 · Tabliczka |
|---|---|---|---|
| **Układ** | przepływ redakcyjny na pełnych 6 kolumnach | stały podział 2 + 4: kolumna aparatu i kolumna treści | siatka kafli 6 / 3 / 2 plus pasy odwrócone na spad |
| **Rytm** | ciągły, wymierzany jednostką 6 mm | rejestrowy — wiersze rozdzielone włosową linią Popiołu | blokowy, perkusyjny; kafel jest jednostką |
| **Hierarchię niesie** | **stopień pisma** (pełna skala 72 → 10 px) | **położenie na siatce** (skala ścięta do H2/H3/lead/korpus) | **powierzchnia** (pas odwrócony / papier / callout) plus liczba prowadząca |
| **Kolor dziedziny** | Aksamit (Pedagogika) | Onyks (Pożyczki UE/BGK) | Miedź (Akademia AI) |

**Wariant 1** — ten sam zamysł co kanwa, przeniesiony na specyfikację obowiązującą; wybieram go
jako punkt odniesienia, bo pokazuje, ile zmienia sama wymiana warstwy faktów, bez ruszania kompozycji.

**Wariant 2** — hierarchia niesiona przez położenie, nie przez stopień; wybieram tę oś, bo dokument,
w którym znaczenie siedzi w kolumnie, przeżywa druk monochromatyczny i czytelnika skanującego
wyłącznie lewy brzeg.

**Wariant 3** — reguła zamknięta w samodzielnym kaflu; wybieram tę oś, bo taki kafel daje się wyjąć
na slajd albo jednostronicówkę bez przerysowywania strony, a pas odwrócony daje księdze rytm,
którego przepływ redakcyjny nie ma.

---

## 4. Ryzyko każdego wariantu z osobna

**Wariant 1.** Najbliżej kanwy, więc najmniej pokazuje. Pełna skala 72 → 10 px na jednej stronie A4
robi dużo światła i przy realnej treści dokumentu regulowanego pierwsza sekcja zje pół strony.
Display 72 px jest tu użyty raz, ale kusi, żeby go powtórzyć.

**Wariant 2.** Kolumna aparatu zjada 54 mm z 170 mm — **32 % szerokości pola treści** na materiał,
którego nie trzeba przeczytać. To akceptowalne w księdze marki, ale w zaświadczeniu albo karcie
usługi BUR, gdzie treści jest dużo, ten sam układ wymusi więcej stron. Drugie ryzyko: przy braku
zawartości w lewej kolumnie wiersz wygląda na uszkodzony.

**Wariant 3.** Pasy odwrócone to duże płaszczyzny Espresso — w druku cyfrowym oznaczają realne
zużycie tonera i ryzyko odbicia na sąsiedniej stronie. Trzy strony z sześciu mają pas na spad,
co wymaga druku ze spadem i przycięciem; papier firmowy i zaświadczenie zwykle drukuje się
bez spadu na zwykłej drukarce. **To jest ograniczenie produkcyjne, nie estetyczne.**

---

## 5. Rekomendacja: wariant 2 „Marginalia”

Rekomenduję **wariant 2**, z jednego powodu: jako jedyny buduje hierarchię tak, że przeżywa
ograniczenie, które ta paleta ma zapisane w specyfikacji — po konwersji do skali szarości Werdykt,
Rubryka, Karmin i Onyks mają zbliżoną jasność, a osobny tryb monochromatyczny został przez foundera
**odrzucony** (`palette-irin.json`, klucz `tryb-mono`). W wariancie 2 znaczenie niesie kolumna
i słowo w Inconsolacie, więc dokument czyta się tak samo w kolorze i w czerni.

Czego ta rekomendacja **nie** rozstrzyga i czym to zmierzyć: kosztu 54 mm kolumny aparatu na
dokumencie o dużej objętości. Pomiar rozstrzygający — złożyć w wariancie 2 jeden realny dokument
z warstwy 2 (karta usługi BUR albo zaświadczenie KFS) i policzyć strony wobec wariantu 1.
Do tego czasu wybór wariantu 2 jest rekomendacją opartą na dostępności, nie na objętości.

Wariant 3 zostawiam jako kierunek na materiały ekranowe i prezentacyjne, gdzie spad i toner
nie są problemem.

---

## 6. Jak sprawdziłem, że pliki trzymają specyfikację

**Paleta — 100 % pokrycia, zero hexów spoza palety.** Skrypt czyta zbiór hexów
z `tokeny/palette-irin.json` i porównuje z każdym plikiem wariantu:

```
wariant-1-kaszmir-uporzadkowany.dc.html   15 unikalnych hexow, wszystkie w palecie
wariant-2-marginalia.dc.html              15 unikalnych hexow, wszystkie w palecie
wariant-3-tabliczka.dc.html               15 unikalnych hexow, wszystkie w palecie
brandbook.dc.html                         16 unikalnych, 16 spoza palety, pokrycie 0%
```

**Etykieta na wypełnieniu — tabela nakazów czytana z pliku tokenów, nie z mojego projektu.**
Miernik dostał próbkę z przypadkiem, który ma złapać, i takim, który ma przepuścić:

```
[OK]      wariant-1 / wariant-2 / wariant-3
[ZAWALIL] KONTROLA-NEGATYWNA  -> hex spoza palety #C0FFEE
                              -> etykieta na --rubryka: jest --pergamin, przepisana --biel
[OK]      KONTROLA-POZYTYWNA
zawalilo: 1 z 5 — oczekiwane: 1
```

**Siatka — rachunek szerokości dla każdego układu:**

| Wariant | Układ | Rachunek |
|---|---|---|
| 1 | pełne sześć kolumn | 6 × 25 + 5 × 4 = **170 mm** |
| 2 | aparat + treść | 54 + 4 + 112 = **170 mm** (aparat 2 × 25 + 4; treść 4 × 25 + 3 × 4) |
| 3 | kafle po 1 kolumnie | 6 × 25 + 5 × 4 = **170 mm** |
| 3 | kafle po 2 kolumny | 3 × 54 + 2 × 4 = **170 mm** |
| 3 | kafle po 3 kolumny | 2 × 83 + 1 × 4 = **170 mm** |

Kontrola negatywna: siatka z kanwy foundera, 6 × 32 + 5 × 4 = **212 mm**, czyli +42 mm wobec pola
treści i +2 mm wobec całej szerokości strony.

**Pliki bazowe — nietknięte.** `git status --short` pokazuje wyłącznie nowy katalog
`_robocze/brandbook-warianty/`; żaden istniejący plik nie ma statusu `M` ani `D`,
a `git diff main --stat` dla plików śledzonych jest pusty.

---

## 7. Siedem reguł z `format-paczki.md` — gdzie każda siedzi

| Reguła | Jak jest spełniona |
|---|---|
| 1. Jeden kolor dziedziny na dokument | Chrome każdego wariantu trzyma jeden kolor: Aksamit / Onyks / Miedź. Wszystkie trzy dziedzinowe pojawiają się wyłącznie jako **próbki opisane nazwą i hexem** w sekcjach 01 i 03 — to odczytanie zaakceptowane przez właściciela 2026-09-03. |
| 2. Etykieta na wypełnieniu przepisana | Sprawdzana skryptem przeciwko tabeli w `palette-irin.json`; złamanie było i zostało naprawione (punkt 1.2). |
| 3. Kolor nie jest jedynym nośnikiem statusu | Każda plakietka statusu ma znak i słowo: „✓ POTWIERDZONE”, „! WYMAGA UWAGI”, „✕ ODRZUCONE”. |
| 4. Hierarchię buduje waga jednego kroju | Wyłącznie Manrope 200–800; Inconsolata tylko na liczby, kody i metadane. Trzeciego kroju nie ma. |
| 5. H3 nie stoi bezpośrednio przy leadzie | Wariant 1 i 2: rozdziela je wiersz metadanych w Inconsolacie. Wariant 3: rozdziela je krawędź kafla. |
| 6. Sześć kolumn zawsze | Wariant 2 dzieli je 2 + 4, wariant 3 składa po 1 / 2 / 3 — moduł 25 mm i gutter 4 mm zachowane, suma 170 mm w każdym układzie. |
| 7. Bez znaków FE, barw RP i flagi UE | Żaden plik nie zawiera takiego znaku; zakaz jest **wypisany wprost** w sekcji 01 wariantów 1, 2 i 3 wraz z podstawą (Podręcznik FE, rozdz. 8.7, s. 22). |

---

## 8. Decyzje warsztatowe, które podjąłem sam

- **Ścieżki logotypu.** `../../logo_irin_poziom.svg` — działa lokalnie w przeglądarce z katalogu
  `_robocze/brandbook-warianty/`. Przy wgrywaniu do Claude Design ścieżki zamieniają się
  na `uploads/…`, tak jak w kanwie. Pliki SVG **nie zostały ruszone**.
- **Wersja odwrócona znaku.** W wariancie 3 logotyp na pasie Espresso dostaje `filter: invert(1)`.
  `logotyp.md` wprost dopuszcza wersję odwróconą na ciemnym tle i zakazuje wyłącznie przebarwienia
  — to jest odwrócenie, nie zmiana koloru.
- **Wymiary w milimetrach.** Cała geometria pisana w `mm`, nie w px. Dzięki temu rachunek siatki
  jest widoczny w kodzie i tożsamy z rachunkiem w `siatka-a4.md`, zamiast być przybliżeniem.
- **Sześć sekcji, nie dziewięć.** Zakres uzgodniony z właścicielem 2026-09-03. Certyfikat, papier
  firmowy i okładka raportu mają własne karty specyfikacji w warstwie 2 — rysowanie ich tutaj
  wyprzedzałoby tamten obieg.

---

## 9. Otwarte — do decyzji właściciela, nie moje

1. **Trzy pary poniżej progu (punkt 1.1).** Czy `paleta-barw.md` ma dostać kolumnę kontrastów
   na Pergaminie, czy raczej zdanie zakazujące Popiołu i Złota foliowego wewnątrz calloutu.
2. **`_robocze/.DS_Store`** — plik systemu macOS, nieśledzony przez git, nigdy nie commitowany,
   pojawił się przy tworzeniu nowego katalogu. Nie usuwam go i nie dopisuję go do `.gitignore`,
   bo `.gitignore` jest plikiem istniejącym, a zadanie zabrania edycji istniejących plików.
   Cofnięcie ewentualnego usunięcia: plik odtwarza się sam przy następnym otwarciu katalogu w Finderze.
3. **Czy warianty mają iść dalej.** Nic nie jest scommitowane. Gałąź `warianty-brandbooka` istnieje
   lokalnie i nie została wypchnięta; cofnięcie to `git checkout main && git branch -D warianty-brandbooka`
   plus skasowanie katalogu `_robocze/brandbook-warianty/`.
