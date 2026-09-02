# Podgląd palety IRIN v2 - 7 wariantów na jednym układzie

**Status: ROZSTRZYGNIĘTE (2026-09-02). Wybrany wariant 2 - Kaszmir Wyciszony.**

Ten podgląd zostaje bez zmian, ze wszystkimi siedmioma wariantami - służy teraz jako zapis porównania, na podstawie którego zapadła decyzja. Obowiązująca specyfikacja: [`../../03-pakiet-claude-design/format-paczki.md`](../../03-pakiet-claude-design/format-paczki.md).

Ten dokument pokazuje siedem wariantów palety z [`palette-options-v2.md`](./palette-options-v2.md) na **identycznym układzie demonstracyjnym**: ta sama treść, ten sam układ, ta sama typografia. Jedyną zmienną jest kolor.

> **Wersja renderowana:** [`palette-preview-v2.dc.html`](./palette-preview-v2.dc.html) - tam każdy z siedmiu wariantów jest faktycznie narysowany, w kroju Manrope wczytanym z Google Fonts, w układzie jeden pod drugim. Markdown nie umie pokazać koloru, więc ten plik podaje mapowanie element → token → HEX, a plik `.dc.html` pokazuje wynik. Oba opisują ten sam układ.

## Typografia użyta w podglądzie - niezmieniona

Wszystkie stopnie, wagi i tracking pochodzą z `brandbook.dc.html` sekcja 04 („Typografia - jeden krój, osiem wag”). Podgląd nie wprowadza żadnego nowego kroju ani stopnia.

| Element podglądu | Krój i parametry |
|---|---|
| Tytuł okładki | Manrope 200 / 72 px / interlinia 0,92 / tracking -0,03em |
| H1 | Manrope 300 / 40 px / interlinia 1,0 / tracking -0,02em |
| H2 | Manrope 600 / 24 px / interlinia 1,1 / tracking -0,01em |
| H3 | Manrope 600 / 16 px / interlinia 1,3 |
| Lead | Manrope 500 / 16 px / interlinia 1,4 |
| Korpus | Manrope 400 / 13,5 px / interlinia 1,55 |
| Przypis, plakietka | Manrope 400-700 / 10 px |
| Kicker sekcji | Manrope 700 / 14 px / tracking 0,22em / wersaliki |
| Liczba prowadząca | Manrope 800 / 52 px |
| Numer usługi, dane liczbowe w tabeli | Inconsolata / 10,5 px |

Jedyne wyprowadzenie: kanwa nie definiuje H3, ma stopień „lead 16 px / waga 500”. H3 w podglądzie to ten sam stopień z wagą 600. Do potwierdzenia osobno.

## Układ demonstracyjny - wspólny dla wszystkich siedmiu wariantów

Każdy wariant pokazuje kolejno:

1. **Pasek 15 próbek** - wszystkie tokeny wariantu obok siebie.
2. **Strona tytułowa** - kicker, tytuł display „Akademia AI.”, lead o dofinansowaniu KFS, linia akcentowa, trzy liczby prowadzące.
3. **Hierarchia nagłówków** - H1 rozdziału, H2 sekcji, H3 podsekcji.
4. **Akapit** - korpus w `text-primary` i akapit pomocniczy w `text-secondary` z linkiem w treści.
5. **Boks informacyjny** - tło `neutral-light`, belka `info`, pod nim cztery plakietki stanów.
6. **Tabela** - cztery moduły szkolenia z efektami uczenia się, godzinami i statusem.
7. **CTA i link** - przycisk podstawowy, przycisk na akcencie, przycisk obrysowy, link samodzielny.
8. **Sekcja „prawo i zgodność”** - odwrócona, na `neutral-dark`, z podstawą prawną, obowiązkiem informacyjnym i numerem usługi.

Treść jest realna dla IRIN (szkolenie Akademii AI dofinansowane z KFS, karta usługi w BUR), żeby ocena palety odbywała się na dokumencie, jaki firma faktycznie wydaje, a nie na abstrakcyjnym wzorniku.

## Mapa elementów - który token maluje co

Ta tabela jest wspólna dla wszystkich siedmiu wariantów. Dalej każdy wariant podaje wyłącznie własne wartości HEX dla tych samych pozycji.

| Element układu | Tło | Tekst / kolor elementu | Typografia |
|---|---|---|---|
| Strona - tło | `background` | - | - |
| Karta dokumentu - tło | `surface` | - | - |
| Kicker nad tytułem | `surface` | `text-secondary` | Manrope 700 / 10,5 px / 0,24em / wersaliki |
| Tytuł okładki (display) | `surface` | `primary` | Manrope 200 / 72 px / interlinia 0,92 |
| Lead pod tytułem | `surface` | `text-secondary` | Manrope 500 / 16 px / interlinia 1,4 |
| Linia pod leadem | `accent` | - | - |
| Liczba prowadząca | `surface` | `primary` | Manrope 800 / 52 px |
| Liczba wyróżniona | `surface` | `accent` | Manrope 800 / 52 px |
| Nagłówek H1 | `surface` | `primary` | Manrope 300 / 40 px / interlinia 1,0 |
| Nagłówek H2 | `surface` | `primary` | Manrope 600 / 24 px / interlinia 1,1 |
| Nagłówek H3 | `surface` | `secondary` | Manrope 600 / 16 px / interlinia 1,3 |
| Akapit korpusu | `surface` | `text-primary` | Manrope 400 / 13,5 px / interlinia 1,55 |
| Akapit pomocniczy | `surface` | `text-secondary` | Manrope 400 / 13,5 px |
| Link w treści | `surface` | `link` | Manrope 400 / 13,5 px / podkreślenie |
| Boks informacyjny - tło | `neutral-light` | `text-primary` | Manrope 400 / 13,5 px |
| Boks informacyjny - krawędź | `info` | - | belka 4 px |
| Boks informacyjny - nagłówek | `neutral-light` | `primary` | Manrope 700 / 10,5 px / wersaliki |
| Tabela - nagłówek kolumny | `neutral-light` | `secondary` | Manrope 700 / 10 px / 0,14em / wersaliki |
| Tabela - komórka | `surface` | `text-primary` | Manrope 400 / 13,5 px |
| Tabela - wiersz naprzemienny | `background` | `text-primary` | Manrope 400 / 13,5 px |
| Tabela - liczba | `surface` | `text-primary` | Inconsolata / 10,5 px |
| Tabela - linie | `border` | - | 1 px, nagłówek i stopka 2 px |
| CTA podstawowe | `primary` | kolor etykiety przepisany dla tego wypełnienia | Manrope 600 / 13,5 px |
| CTA na akcencie | `accent` | kolor etykiety przepisany dla tego wypełnienia | Manrope 600 / 13,5 px |
| CTA obrysowe | `surface` | `primary` | Manrope 600 / 13,5 px, obrys 2 px w kolorze primary |
| Plakietka „zatwierdzone” | `success` | kolor etykiety przepisany dla tego wypełnienia | Manrope 700 / 10 px / wersaliki |
| Plakietka „termin naboru” | `warning` | kolor etykiety przepisany dla tego wypełnienia | Manrope 700 / 10 px / wersaliki |
| Plakietka „brak załącznika” | `error` | kolor etykiety przepisany dla tego wypełnienia | Manrope 700 / 10 px / wersaliki |
| Plakietka „nota” | `info` | kolor etykiety przepisany dla tego wypełnienia | Manrope 700 / 10 px / wersaliki |
| Sekcja prawo - tło | `neutral-dark` | `neutral-light` | Manrope 400 / 13,5 px |
| Sekcja prawo - kicker | `neutral-dark` | `accent` | Manrope 700 / 10,5 px / wersaliki |
| Sekcja prawo - numer usługi | `neutral-dark` | `accent` | Inconsolata / 10,5 px |

---

## Wariant 1 - Kaszmir Aksamit (bazowy)

Zatwierdzona 12-barwna paleta „Colorbook Kaszmir Aksamit” przemapowana bez zmiany odcieni na 15 tokenów semantycznych. Nie jest propozycją zmiany - jest punktem odniesienia, wobec którego mierzy się sześć pozostałych wariantów.

Podgląd renderowany: sekcja `#w1` w [`palette-preview-v2.dc.html`](./palette-preview-v2.dc.html).

### Ten sam układ, wartości tego wariantu

| Element układu | HEX tła | HEX tekstu / elementu |
|---|---|---|
| Strona - tło | `#F7F3EA` | - |
| Karta dokumentu - tło | `#F2ECE1` | - |
| Kicker nad tytułem | `#F2ECE1` | `#5B4837` |
| Tytuł okładki (display) | `#F2ECE1` | `#4A1D26` |
| Lead pod tytułem | `#F2ECE1` | `#5B4837` |
| Linia pod leadem | `#B58540` | - |
| Liczba prowadząca | `#F2ECE1` | `#4A1D26` |
| Liczba wyróżniona | `#F2ECE1` | `#B58540` |
| Nagłówek H1 | `#F2ECE1` | `#4A1D26` |
| Nagłówek H2 | `#F2ECE1` | `#4A1D26` |
| Nagłówek H3 | `#F2ECE1` | `#8C5026` |
| Akapit korpusu | `#F2ECE1` | `#1E1611` |
| Akapit pomocniczy | `#F2ECE1` | `#5B4837` |
| Link w treści | `#F2ECE1` | `#AC151F` |
| Boks informacyjny - tło | `#E4DACB` | `#1E1611` |
| Boks informacyjny - krawędź | `#1B2B26` | - |
| Boks informacyjny - nagłówek | `#E4DACB` | `#4A1D26` |
| Tabela - nagłówek kolumny | `#E4DACB` | `#8C5026` |
| Tabela - komórka | `#F2ECE1` | `#1E1611` |
| Tabela - wiersz naprzemienny | `#F7F3EA` | `#1E1611` |
| Tabela - liczba | `#F2ECE1` | `#1E1611` |
| Tabela - linie | `#1E1611` | - |
| CTA podstawowe | `#4A1D26` | `#E4DACB` (neutral-light) |
| CTA na akcencie | `#B58540` | `#1E1611` (neutral-dark) |
| CTA obrysowe | `#F2ECE1` | `#4A1D26` |
| Plakietka „zatwierdzone” | `#2F4A32` | `#E4DACB` (neutral-light) |
| Plakietka „termin naboru” | `#D9AC4A` | `#1E1611` (neutral-dark) |
| Plakietka „brak załącznika” | `#AC151F` | `#E4DACB` (neutral-light) |
| Plakietka „nota” | `#1B2B26` | `#E4DACB` (neutral-light) |
| Sekcja prawo - tło | `#1E1611` | `#E4DACB` |
| Sekcja prawo - kicker | `#1E1611` | `#B58540` |
| Sekcja prawo - numer usługi | `#1E1611` | `#B58540` |

### Jak ten wariant wypada na tym układzie

| Miejsce w układzie | Kontrast | Ocena |
|---|---|---|
| Akapit korpusu na karcie | 15,16:1 | AAA |
| Akapit pomocniczy na karcie | 7,36:1 | AAA |
| Nagłówki H1 i H2 | 11,95:1 | AAA |
| Nagłówek H3 | 5,43:1 | AA |
| Link w treści | 6,20:1 | AA |
| Tekst w boksie informacyjnym | 12,89:1 | AAA |
| Etykieta CTA podstawowego | 10,16:1 | AAA |
| Linie tabeli | 15,16:1 | OK (≥3:1) |

**Widoczne na tym układzie do sprawdzenia okiem:** accent jako linia/ikona na surface (2,79:1).

Pełne trade-offs tego wariantu: [`palette-options-v2.md`](./palette-options-v2.md#wariant-1-kaszmir-aksamit-bazowy).

---

## Wariant 2 - Kaszmir Wyciszony

Ten sam papier i ta sama rodzina bordo co w wariancie zatwierdzonym, ale z obniżonym nasyceniem akcentów, osobnym półtonem na obramowania i linkiem przesuniętym w głęboką morską zieleń, żeby przestał być tym samym kolorem co błąd.

Podgląd renderowany: sekcja `#w2` w [`palette-preview-v2.dc.html`](./palette-preview-v2.dc.html).

### Ten sam układ, wartości tego wariantu

| Element układu | HEX tła | HEX tekstu / elementu |
|---|---|---|
| Strona - tło | `#F6F2E9` | - |
| Karta dokumentu - tło | `#FBF8F2` | - |
| Kicker nad tytułem | `#FBF8F2` | `#5E4E40` |
| Tytuł okładki (display) | `#FBF8F2` | `#452430` |
| Lead pod tytułem | `#FBF8F2` | `#5E4E40` |
| Linia pod leadem | `#A8874E` | - |
| Liczba prowadząca | `#FBF8F2` | `#452430` |
| Liczba wyróżniona | `#FBF8F2` | `#A8874E` |
| Nagłówek H1 | `#FBF8F2` | `#452430` |
| Nagłówek H2 | `#FBF8F2` | `#452430` |
| Nagłówek H3 | `#FBF8F2` | `#7A5638` |
| Akapit korpusu | `#FBF8F2` | `#221A15` |
| Akapit pomocniczy | `#FBF8F2` | `#5E4E40` |
| Link w treści | `#FBF8F2` | `#2F5A63` |
| Boks informacyjny - tło | `#E7DFD2` | `#221A15` |
| Boks informacyjny - krawędź | `#33474F` | - |
| Boks informacyjny - nagłówek | `#E7DFD2` | `#452430` |
| Tabela - nagłówek kolumny | `#E7DFD2` | `#7A5638` |
| Tabela - komórka | `#FBF8F2` | `#221A15` |
| Tabela - wiersz naprzemienny | `#F6F2E9` | `#221A15` |
| Tabela - liczba | `#FBF8F2` | `#221A15` |
| Tabela - linie | `#938978` | - |
| CTA podstawowe | `#452430` | `#E7DFD2` (neutral-light) |
| CTA na akcencie | `#A8874E` | `#221A15` (neutral-dark) |
| CTA obrysowe | `#FBF8F2` | `#452430` |
| Plakietka „zatwierdzone” | `#2E5241` | `#E7DFD2` (neutral-light) |
| Plakietka „termin naboru” | `#8A6110` | `#FFFFFF` (#FFFFFF) |
| Plakietka „brak załącznika” | `#9E2B2B` | `#E7DFD2` (neutral-light) |
| Plakietka „nota” | `#33474F` | `#E7DFD2` (neutral-light) |
| Sekcja prawo - tło | `#221A15` | `#E7DFD2` |
| Sekcja prawo - kicker | `#221A15` | `#A8874E` |
| Sekcja prawo - numer usługi | `#221A15` | `#A8874E` |

### Jak ten wariant wypada na tym układzie

| Miejsce w układzie | Kontrast | Ocena |
|---|---|---|
| Akapit korpusu na karcie | 16,15:1 | AAA |
| Akapit pomocniczy na karcie | 7,50:1 | AAA |
| Nagłówki H1 i H2 | 12,80:1 | AAA |
| Nagłówek H3 | 6,16:1 | AA |
| Link w treści | 7,17:1 | AAA |
| Tekst w boksie informacyjnym | 12,95:1 | AAA |
| Etykieta CTA podstawowego | 10,26:1 | AAA |
| Linie tabeli | 3,25:1 | OK (≥3:1) |

**Żadna para w tym układzie nie schodzi poniżej progu.**

Pełne trade-offs tego wariantu: [`palette-options-v2.md`](./palette-options-v2.md#wariant-2-kaszmir-wyciszony).

---

## Wariant 3 - Papier i Grafit

Ciepły papier zostaje, ale tusz przestaje być brązowy: cały szkielet typograficzny przechodzi na grafit, a jedynym kolorem pozostaje miedź. System przestaje wyglądać jak stara księga, zaczyna wyglądać jak dokument techniczny na dobrym papierze.

Podgląd renderowany: sekcja `#w3` w [`palette-preview-v2.dc.html`](./palette-preview-v2.dc.html).

### Ten sam układ, wartości tego wariantu

| Element układu | HEX tła | HEX tekstu / elementu |
|---|---|---|
| Strona - tło | `#F6F3ED` | - |
| Karta dokumentu - tło | `#FCFAF6` | - |
| Kicker nad tytułem | `#FCFAF6` | `#515961` |
| Tytuł okładki (display) | `#FCFAF6` | `#2B3138` |
| Lead pod tytułem | `#FCFAF6` | `#515961` |
| Linia pod leadem | `#A85E28` | - |
| Liczba prowadząca | `#FCFAF6` | `#2B3138` |
| Liczba wyróżniona | `#FCFAF6` | `#A85E28` |
| Nagłówek H1 | `#FCFAF6` | `#2B3138` |
| Nagłówek H2 | `#FCFAF6` | `#2B3138` |
| Nagłówek H3 | `#FCFAF6` | `#5A6470` |
| Akapit korpusu | `#FCFAF6` | `#16191D` |
| Akapit pomocniczy | `#FCFAF6` | `#515961` |
| Link w treści | `#FCFAF6` | `#1F5B7A` |
| Boks informacyjny - tło | `#E6E2DA` | `#16191D` |
| Boks informacyjny - krawędź | `#2A5670` | - |
| Boks informacyjny - nagłówek | `#E6E2DA` | `#2B3138` |
| Tabela - nagłówek kolumny | `#E6E2DA` | `#5A6470` |
| Tabela - komórka | `#FCFAF6` | `#16191D` |
| Tabela - wiersz naprzemienny | `#F6F3ED` | `#16191D` |
| Tabela - liczba | `#FCFAF6` | `#16191D` |
| Tabela - linie | `#8F8B83` | - |
| CTA podstawowe | `#2B3138` | `#E6E2DA` (neutral-light) |
| CTA na akcencie | `#A85E28` | `#FFFFFF` (#FFFFFF) |
| CTA obrysowe | `#FCFAF6` | `#2B3138` |
| Plakietka „zatwierdzone” | `#26614A` | `#E6E2DA` (neutral-light) |
| Plakietka „termin naboru” | `#8A5D0F` | `#FFFFFF` (#FFFFFF) |
| Plakietka „brak załącznika” | `#A32D2A` | `#E6E2DA` (neutral-light) |
| Plakietka „nota” | `#2A5670` | `#E6E2DA` (neutral-light) |
| Sekcja prawo - tło | `#16191D` | `#E6E2DA` |
| Sekcja prawo - kicker | `#16191D` | `#A85E28` |
| Sekcja prawo - numer usługi | `#16191D` | `#A85E28` |

### Jak ten wariant wypada na tym układzie

| Miejsce w układzie | Kontrast | Ocena |
|---|---|---|
| Akapit korpusu na karcie | 16,91:1 | AAA |
| Akapit pomocniczy na karcie | 6,83:1 | AA |
| Nagłówki H1 i H2 | 12,60:1 | AAA |
| Nagłówek H3 | 5,77:1 | AA |
| Link w treści | 7,10:1 | AAA |
| Tekst w boksie informacyjnym | 13,65:1 | AAA |
| Etykieta CTA podstawowego | 10,17:1 | AAA |
| Linie tabeli | 3,25:1 | OK (≥3:1) |

**Żadna para w tym układzie nie schodzi poniżej progu.**

Pełne trade-offs tego wariantu: [`palette-options-v2.md`](./palette-options-v2.md#wariant-3-papier-i-grafit).

---

## Wariant 4 - Instytut

Granat dokumentu urzędowego jako kolor wiodący, przy zachowanym ciepłym papierze. Dokument ma wyglądać wiarygodnie na biurku operatora dofinansowania, w PARP i w BGK, a nie w portfolio agencji.

Podgląd renderowany: sekcja `#w4` w [`palette-preview-v2.dc.html`](./palette-preview-v2.dc.html).

### Ten sam układ, wartości tego wariantu

| Element układu | HEX tła | HEX tekstu / elementu |
|---|---|---|
| Strona - tło | `#F6F4EF` | - |
| Karta dokumentu - tło | `#FDFCF9` | - |
| Kicker nad tytułem | `#FDFCF9` | `#47525D` |
| Tytuł okładki (display) | `#FDFCF9` | `#1B3A5C` |
| Lead pod tytułem | `#FDFCF9` | `#47525D` |
| Linia pod leadem | `#B07A2E` | - |
| Liczba prowadząca | `#FDFCF9` | `#1B3A5C` |
| Liczba wyróżniona | `#FDFCF9` | `#B07A2E` |
| Nagłówek H1 | `#FDFCF9` | `#1B3A5C` |
| Nagłówek H2 | `#FDFCF9` | `#1B3A5C` |
| Nagłówek H3 | `#FDFCF9` | `#3E6285` |
| Akapit korpusu | `#FDFCF9` | `#131A21` |
| Akapit pomocniczy | `#FDFCF9` | `#47525D` |
| Link w treści | `#FDFCF9` | `#14507E` |
| Boks informacyjny - tło | `#E6E1D6` | `#131A21` |
| Boks informacyjny - krawędź | `#1F5F7D` | - |
| Boks informacyjny - nagłówek | `#E6E1D6` | `#1B3A5C` |
| Tabela - nagłówek kolumny | `#E6E1D6` | `#3E6285` |
| Tabela - komórka | `#FDFCF9` | `#131A21` |
| Tabela - wiersz naprzemienny | `#F6F4EF` | `#131A21` |
| Tabela - liczba | `#FDFCF9` | `#131A21` |
| Tabela - linie | `#878C90` | - |
| CTA podstawowe | `#1B3A5C` | `#E6E1D6` (neutral-light) |
| CTA na akcencie | `#B07A2E` | `#131A21` (neutral-dark) |
| CTA obrysowe | `#FDFCF9` | `#1B3A5C` |
| Plakietka „zatwierdzone” | `#1F6B4F` | `#E6E1D6` (neutral-light) |
| Plakietka „termin naboru” | `#8F6412` | `#FFFFFF` (#FFFFFF) |
| Plakietka „brak załącznika” | `#A32F30` | `#E6E1D6` (neutral-light) |
| Plakietka „nota” | `#1F5F7D` | `#E6E1D6` (neutral-light) |
| Sekcja prawo - tło | `#131A21` | `#E6E1D6` |
| Sekcja prawo - kicker | `#131A21` | `#B07A2E` |
| Sekcja prawo - numer usługi | `#131A21` | `#B07A2E` |

### Jak ten wariant wypada na tym układzie

| Miejsce w układzie | Kontrast | Ocena |
|---|---|---|
| Akapit korpusu na karcie | 17,09:1 | AAA |
| Akapit pomocniczy na karcie | 7,77:1 | AAA |
| Nagłówki H1 i H2 | 11,33:1 | AAA |
| Nagłówek H3 | 6,22:1 | AA |
| Link w treści | 8,26:1 | AAA |
| Tekst w boksie informacyjnym | 13,45:1 | AAA |
| Etykieta CTA podstawowego | 8,92:1 | AAA |
| Linie tabeli | 3,31:1 | OK (≥3:1) |

**Żadna para w tym układzie nie schodzi poniżej progu.**

Pełne trade-offs tego wariantu: [`palette-options-v2.md`](./palette-options-v2.md#wariant-4-instytut).

---

## Wariant 5 - Werdykt

Kolor Werdykt, który w zatwierdzonej palecie pełnił funkcję stanu potwierdzonego, awansuje na kolor wiodący. Zieleń instytucjonalna niesie rozwój i staranność bez fintechowego granatu, a złoto zostaje jako sygnatura.

Podgląd renderowany: sekcja `#w5` w [`palette-preview-v2.dc.html`](./palette-preview-v2.dc.html).

### Ten sam układ, wartości tego wariantu

| Element układu | HEX tła | HEX tekstu / elementu |
|---|---|---|
| Strona - tło | `#F5F4EE` | - |
| Karta dokumentu - tło | `#FCFBF6` | - |
| Kicker nad tytułem | `#FCFBF6` | `#455249` |
| Tytuł okładki (display) | `#FCFBF6` | `#1E4A38` |
| Lead pod tytułem | `#FCFBF6` | `#455249` |
| Linia pod leadem | `#B08237` | - |
| Liczba prowadząca | `#FCFBF6` | `#1E4A38` |
| Liczba wyróżniona | `#FCFBF6` | `#B08237` |
| Nagłówek H1 | `#FCFBF6` | `#1E4A38` |
| Nagłówek H2 | `#FCFBF6` | `#1E4A38` |
| Nagłówek H3 | `#FCFBF6` | `#3C6B54` |
| Akapit korpusu | `#FCFBF6` | `#14201A` |
| Akapit pomocniczy | `#FCFBF6` | `#455249` |
| Link w treści | `#FCFBF6` | `#1D5A6B` |
| Boks informacyjny - tło | `#E2E4DC` | `#14201A` |
| Boks informacyjny - krawędź | `#26596B` | - |
| Boks informacyjny - nagłówek | `#E2E4DC` | `#1E4A38` |
| Tabela - nagłówek kolumny | `#E2E4DC` | `#3C6B54` |
| Tabela - komórka | `#FCFBF6` | `#14201A` |
| Tabela - wiersz naprzemienny | `#F5F4EE` | `#14201A` |
| Tabela - liczba | `#FCFBF6` | `#14201A` |
| Tabela - linie | `#898D87` | - |
| CTA podstawowe | `#1E4A38` | `#E2E4DC` (neutral-light) |
| CTA na akcencie | `#B08237` | `#14201A` (neutral-dark) |
| CTA obrysowe | `#FCFBF6` | `#1E4A38` |
| Plakietka „zatwierdzone” | `#226B45` | `#E2E4DC` (neutral-light) |
| Plakietka „termin naboru” | `#8B6212` | `#FFFFFF` (#FFFFFF) |
| Plakietka „brak załącznika” | `#A22E2C` | `#E2E4DC` (neutral-light) |
| Plakietka „nota” | `#26596B` | `#E2E4DC` (neutral-light) |
| Sekcja prawo - tło | `#14201A` | `#E2E4DC` |
| Sekcja prawo - kicker | `#14201A` | `#B08237` |
| Sekcja prawo - numer usługi | `#14201A` | `#B08237` |

### Jak ten wariant wypada na tym układzie

| Miejsce w układzie | Kontrast | Ocena |
|---|---|---|
| Akapit korpusu na karcie | 16,20:1 | AAA |
| Akapit pomocniczy na karcie | 7,93:1 | AAA |
| Nagłówki H1 i H2 | 9,69:1 | AAA |
| Nagłówek H3 | 5,92:1 | AA |
| Link w treści | 7,43:1 | AAA |
| Tekst w boksie informacyjnym | 13,08:1 | AAA |
| Etykieta CTA podstawowego | 7,82:1 | AAA |
| Linie tabeli | 3,26:1 | OK (≥3:1) |

**Żadna para w tym układzie nie schodzi poniżej progu.**

Pełne trade-offs tego wariantu: [`palette-options-v2.md`](./palette-options-v2.md#wariant-5-werdykt).

---

## Wariant 6 - Druk Ekonomiczny

Prawie monochromatyczny system z jednym ceglanym akcentem, zaprojektowany pod najgorszy realny scenariusz dystrybucji: zaświadczenie KFS skserowane, zeskanowane i wydrukowane mono w dziale kadr. Nie jest propozycją tożsamości - jest trybem przetrwania.

Podgląd renderowany: sekcja `#w6` w [`palette-preview-v2.dc.html`](./palette-preview-v2.dc.html).

### Ten sam układ, wartości tego wariantu

| Element układu | HEX tła | HEX tekstu / elementu |
|---|---|---|
| Strona - tło | `#FBFAF7` | - |
| Karta dokumentu - tło | `#FFFFFF` | - |
| Kicker nad tytułem | `#FFFFFF` | `#4A4A4A` |
| Tytuł okładki (display) | `#FFFFFF` | `#111111` |
| Lead pod tytułem | `#FFFFFF` | `#4A4A4A` |
| Linia pod leadem | `#7A2418` | - |
| Liczba prowadząca | `#FFFFFF` | `#111111` |
| Liczba wyróżniona | `#FFFFFF` | `#7A2418` |
| Nagłówek H1 | `#FFFFFF` | `#111111` |
| Nagłówek H2 | `#FFFFFF` | `#111111` |
| Nagłówek H3 | `#FFFFFF` | `#3D3D3D` |
| Akapit korpusu | `#FFFFFF` | `#0A0A0A` |
| Akapit pomocniczy | `#FFFFFF` | `#4A4A4A` |
| Link w treści | `#FFFFFF` | `#7A2418` |
| Boks informacyjny - tło | `#E8E6E1` | `#0A0A0A` |
| Boks informacyjny - krawędź | `#2E4560` | - |
| Boks informacyjny - nagłówek | `#E8E6E1` | `#111111` |
| Tabela - nagłówek kolumny | `#E8E6E1` | `#3D3D3D` |
| Tabela - komórka | `#FFFFFF` | `#0A0A0A` |
| Tabela - wiersz naprzemienny | `#FBFAF7` | `#0A0A0A` |
| Tabela - liczba | `#FFFFFF` | `#0A0A0A` |
| Tabela - linie | `#928F89` | - |
| CTA podstawowe | `#111111` | `#E8E6E1` (neutral-light) |
| CTA na akcencie | `#7A2418` | `#E8E6E1` (neutral-light) |
| CTA obrysowe | `#FFFFFF` | `#111111` |
| Plakietka „zatwierdzone” | `#2A4F35` | `#E8E6E1` (neutral-light) |
| Plakietka „termin naboru” | `#6B5307` | `#E8E6E1` (neutral-light) |
| Plakietka „brak załącznika” | `#8E1B1B` | `#E8E6E1` (neutral-light) |
| Plakietka „nota” | `#2E4560` | `#E8E6E1` (neutral-light) |
| Sekcja prawo - tło | `#0A0A0A` | `#E8E6E1` |
| Sekcja prawo - kicker | `#0A0A0A` | `#7A2418` |
| Sekcja prawo - numer usługi | `#0A0A0A` | `#7A2418` |

### Jak ten wariant wypada na tym układzie

| Miejsce w układzie | Kontrast | Ocena |
|---|---|---|
| Akapit korpusu na karcie | 19,80:1 | AAA |
| Akapit pomocniczy na karcie | 8,86:1 | AAA |
| Nagłówki H1 i H2 | 18,88:1 | AAA |
| Nagłówek H3 | 10,86:1 | AAA |
| Link w treści | 10,03:1 | AAA |
| Tekst w boksie informacyjnym | 15,87:1 | AAA |
| Etykieta CTA podstawowego | 15,14:1 | AAA |
| Linie tabeli | 3,22:1 | OK (≥3:1) |

**Żadna para w tym układzie nie schodzi poniżej progu.**

Pełne trade-offs tego wariantu: [`palette-options-v2.md`](./palette-options-v2.md#wariant-6-druk-ekonomiczny).

---

## Wariant 7 - Portal Cyfrowy

Jedyny wariant zaprojektowany pod ekran, a nie pod papier: chłodna biel jako powierzchnia, morski `primary` i żywy miedziano-pomarańczowy przycisk akcji. Adresuje planowany portal sprzedaży szkoleń, który w żadnym z pozostałych wariantów nie ma właściwego CTA.

Podgląd renderowany: sekcja `#w7` w [`palette-preview-v2.dc.html`](./palette-preview-v2.dc.html).

### Ten sam układ, wartości tego wariantu

| Element układu | HEX tła | HEX tekstu / elementu |
|---|---|---|
| Strona - tło | `#F7F9FA` | - |
| Karta dokumentu - tło | `#FFFFFF` | - |
| Kicker nad tytułem | `#FFFFFF` | `#4B5563` |
| Tytuł okładki (display) | `#FFFFFF` | `#10505F` |
| Lead pod tytułem | `#FFFFFF` | `#4B5563` |
| Linia pod leadem | `#C2410C` | - |
| Liczba prowadząca | `#FFFFFF` | `#10505F` |
| Liczba wyróżniona | `#FFFFFF` | `#C2410C` |
| Nagłówek H1 | `#FFFFFF` | `#10505F` |
| Nagłówek H2 | `#FFFFFF` | `#10505F` |
| Nagłówek H3 | `#FFFFFF` | `#2A7F93` |
| Akapit korpusu | `#FFFFFF` | `#0F172A` |
| Akapit pomocniczy | `#FFFFFF` | `#4B5563` |
| Link w treści | `#FFFFFF` | `#0369A1` |
| Boks informacyjny - tło | `#E7EDF0` | `#0F172A` |
| Boks informacyjny - krawędź | `#0369A1` | - |
| Boks informacyjny - nagłówek | `#E7EDF0` | `#10505F` |
| Tabela - nagłówek kolumny | `#E7EDF0` | `#2A7F93` |
| Tabela - komórka | `#FFFFFF` | `#0F172A` |
| Tabela - wiersz naprzemienny | `#F7F9FA` | `#0F172A` |
| Tabela - liczba | `#FFFFFF` | `#0F172A` |
| Tabela - linie | `#8A9093` | - |
| CTA podstawowe | `#10505F` | `#E7EDF0` (neutral-light) |
| CTA na akcencie | `#C2410C` | `#FFFFFF` (#FFFFFF) |
| CTA obrysowe | `#FFFFFF` | `#10505F` |
| Plakietka „zatwierdzone” | `#15803D` | `#FFFFFF` (#FFFFFF) |
| Plakietka „termin naboru” | `#B45309` | `#FFFFFF` (#FFFFFF) |
| Plakietka „brak załącznika” | `#B91C1C` | `#E7EDF0` (neutral-light) |
| Plakietka „nota” | `#0369A1` | `#E7EDF0` (neutral-light) |
| Sekcja prawo - tło | `#0F172A` | `#E7EDF0` |
| Sekcja prawo - kicker | `#0F172A` | `#C2410C` |
| Sekcja prawo - numer usługi | `#0F172A` | `#C2410C` |

### Jak ten wariant wypada na tym układzie

| Miejsce w układzie | Kontrast | Ocena |
|---|---|---|
| Akapit korpusu na karcie | 17,85:1 | AAA |
| Akapit pomocniczy na karcie | 7,56:1 | AAA |
| Nagłówki H1 i H2 | 8,99:1 | AAA |
| Nagłówek H3 | 4,61:1 | AA |
| Link w treści | 5,93:1 | AA |
| Tekst w boksie informacyjnym | 15,11:1 | AAA |
| Etykieta CTA podstawowego | 7,61:1 | AAA |
| Linie tabeli | 3,24:1 | OK (≥3:1) |

**Żadna para w tym układzie nie schodzi poniżej progu.**

Pełne trade-offs tego wariantu: [`palette-options-v2.md`](./palette-options-v2.md#wariant-7-portal-cyfrowy).

---

## Co porównać, patrząc na siedem sekcji obok siebie

- **Link w akapicie pomocniczym.** W wariancie 1 ma dokładnie ten sam kolor co plakietka „brak załącznika”. Sprawdź, czy to przeszkadza na realnym dokumencie - to jest główny argument za wariantem 2.
- **Linie tabeli.** W wariancie 1 każda linia ma pełną wagę tuszu; w pozostałych linia cienka jest wyraźnie lżejsza od linii nagłówka. Sprawdź, która tabela czyta się szybciej.
- **Sekcja „prawo i zgodność”.** Wszystkie warianty odwracają ją na `neutral-dark`. Zobacz, czy akcent na numerze usługi jest jeszcze czytelny, czy już tylko dekoracyjny.
- **Cztery plakietki stanów.** Zmruż oczy albo wydrukuj mono. Jeśli cztery plakietki stają się jedną plamą, to potwierdza wniosek wspólny: status w dokumencie IRIN musi mieć etykietę słowną, nie sam kolor.
- **Strona tytułowa.** To jedyne miejsce, w którym paleta pracuje na dużej powierzchni. Wariant, który tu nie działa, nie będzie działał na okładce viewbooka ani na certyfikacie.

**Rekomendacja: wariant 2 - Kaszmir Wyciszony.** Uzasadnienie i falsyfikator: [`palette-options-v2.md`](./palette-options-v2.md#rekomendacja).

## Wybrany wariant

**Wariant 2 - Kaszmir Wyciszony.** Wpisany jako obowiązujący w `../../03-pakiet-claude-design/format-paczki.md` wraz z mapowaniem na nazwany system 14 kolorów i regułę 80/15/5. Żadna wcześniejsza decyzja nie została usunięta.
