# Paleta barw IRIN - 7 wariantów do wyboru (v2)

**Status: ROZSTRZYGNIĘTE (2026-09-02). Founder wybrał wariant 2 - Kaszmir Wyciszony.**

Obowiązująca specyfikacja wybranego wariantu: [`../../03-pakiet-claude-design/format-paczki.md`](../../03-pakiet-claude-design/format-paczki.md). Dane maszynowe wybranej palety: [`tokens/palette-irin.json`](./tokens/palette-irin.json).

Pozostałe sześć wariantów **zostaje w tym dokumencie w całości** - to zapis tego, co zostało zmierzone i odrzucone, a więc materiał na wypadek powrotu do decyzji. Nic tu nie zostało usunięte ani przepisane po wyborze; zmieniła się wyłącznie ta ramka statusu i notatka pod rekomendacją.

**Uwaga wdrożeniowa:** wybrany wariant został w `format-paczki.md` zmapowany na nazwany system 14 kolorów (Kaszmir, Aksamit, Miedź, Onyks...) i na regułę 80/15/5, żeby trzy akcenty dziedzinowe nie zniknęły - 15 tokenów semantycznych z tego dokumentu to ta sama paleta widziana od strony roli w dokumencie, nie osobny zestaw kolorów. Ten dokument nie zmienia ani nie unieważnia niczego, co zostało rozstrzygnięte wcześniej - paleta zatwierdzona 2026-09-02 i wpisana do `../../03-pakiet-claude-design/format-paczki.md` obowiązuje do chwili, w której founder wskaże numer wariantu z tej listy. Historia poprzedniej decyzji zostaje nienaruszona w `../../03-pakiet-claude-design/propozycja-palety-i-siatki-do-potwierdzenia.md`.

Podgląd wszystkich siedmiu wariantów na identycznym układzie demonstracyjnym: [`palette-preview-v2.md`](./palette-preview-v2.md) (opis) oraz [`palette-preview-v2.dc.html`](./palette-preview-v2.dc.html) (wersja renderowana, z realną typografią).

Dane maszynowe: [`tokens/palette-options-v2.json`](./tokens/palette-options-v2.json).

## Typografia - wykryta z repozytorium, niezmieniana

Kolorystyka jest jedyną rzeczą, którą ten dokument proponuje zmienić. Typografia poniżej pochodzi z `brandbook.dc.html` (sekcja 04) i z `../../03-pakiet-claude-design/format-paczki.md`; każdy wariant palety używa dokładnie tych samych krojów, wag i stopni.

| Poziom | Krój | Waga | Stopień | Interlinia | Tracking |
|---|---|---|---|---|---|
| Display (okładka) | Manrope | 200 | 72 px | 0,92 | -0,03em |
| H1 - rozdział | Manrope | 300 | 40 px | 1,0 | -0,02em |
| H2 - sekcja | Manrope | 600 | 24 px | 1,1 | -0,01em |
| H3 - podsekcja | Manrope | 600 | 16 px | 1,3 | 0 |
| Lead akapitu | Manrope | 500 | 16 px | 1,4 | 0 |
| Korpus | Manrope | 400 | 13,5 px | 1,55 | 0 |
| Przypis, metadane | Manrope | 400 | 10 px | 1,5 | 0 |
| Kicker (drogowskaz sekcji) | Manrope | 700 | 14 px | 1,2 | 0,22em, wersaliki |
| Liczba prowadząca | Manrope | 800 | 52 px | 0,95 | -0,02em |
| Dane techniczne, kody usług | Inconsolata | 300-700 | 10,5 px | 1,5 | 0 |

**H3 - zatwierdzony przez foundera (2026-09-02).** Kanwa nie definiowała tego poziomu; H3 to stopień leadu (16 px) z wagą podniesioną do 600. Wyprowadzenie z istniejącej skali, nie nowy krój ani nowy stopień. Wpisany do obowiązującej specyfikacji w `../../03-pakiet-claude-design/format-paczki.md`.

## Metodologia pomiaru kontrastu

Wszystkie liczby w tym dokumencie zostały policzone skryptem uruchomionym w tej sesji wzorem WCAG 2.1 na luminancji względnej sRGB. Żadna nie jest przepisana z `brandbook.dc.html` ani z poprzedniej propozycji - poprzedni pomiar wykazał, że liczby wpisane ręcznie w kanwie potrafiły być zawyżone albo zaniżone o ponad punkt.

Progi: **AA tekst normalny 4,5:1**, **AAA tekst normalny 7:1**, **AA tekst duży 3:1**, **element interfejsu i grafika znacząca 3:1**.

Dwa dodatkowe pomiary, których WCAG nie wymaga, ale które wychwytują realne defekty:

- **etykieta na wypełnieniu** - dla każdego koloru, który bywa tłem przycisku albo plakietki, wskazany jest ten kolor etykiety (`neutral-light`, biel albo `neutral-dark`), który przechodzi AA. Wariant nie jest oceniany za pary, których nie zaleca.
- **rozróżnialność** - kontrast wzajemny dwóch kolorów niosących różne znaczenia. Niski wynik nie łamie WCAG, ale oznacza, że dwa różne komunikaty wyglądają tak samo. WCAG mierzy jasność, nie barwę, więc ten pomiar jest sygnałem ryzyka, nie werdyktem.

## Skrót - 7 wariantów

| # | Wariant | Kierunek w trzech słowach | `primary` | `accent` | `link` | Par poniżej progu | Najniższa para tekstowa |
|---|---|---|---|---|---|---|---|
| 1 | **Kaszmir Aksamit (bazowy)** | zatwierdzony, bez zmian | `#4A1D26` | `#B58540` | `#AC151F` | 1 | 5,27:1 (etykieta neutral-light na error) |
| 2 | **Kaszmir Wyciszony** | ten sam, dopracowany | `#452430` | `#A8874E` | `#2F5A63` | 0 | 5,09:1 (etykieta neutral-dark na accent) |
| 3 | **Papier i Grafit** | ciepły papier, grafit | `#2B3138` | `#A85E28` | `#1F5B7A` | 0 | 4,89:1 (etykieta #FFFFFF na accent) |
| 4 | **Instytut** | granat dokumentu urzędowego | `#1B3A5C` | `#B07A2E` | `#14507E` | 0 | 4,73:1 (etykieta neutral-dark na accent) |
| 5 | **Werdykt** | zieleń instytucjonalna | `#1E4A38` | `#B08237` | `#1D5A6B` | 0 | 4,87:1 (etykieta neutral-dark na accent) |
| 6 | **Druk Ekonomiczny** | mono, maksymalny kontrast | `#111111` | `#7A2418` | `#7A2418` | 0 | 5,88:1 (etykieta neutral-light na warning) |
| 7 | **Portal Cyfrowy** | ekranowy, pod portal | `#10505F` | `#C2410C` | `#0369A1` | 0 | 4,61:1 (secondary (H3) na surface) |

**Rekomendacja: wariant 2 - Kaszmir Wyciszony.** Uzasadnienie i falsyfikator w sekcji „Rekomendacja” na końcu dokumentu.

---

## Wariant 1 - Kaszmir Aksamit (bazowy)

Zatwierdzona 12-barwna paleta „Colorbook Kaszmir Aksamit” przemapowana bez zmiany odcieni na 15 tokenów semantycznych. Nie jest propozycją zmiany - jest punktem odniesienia, wobec którego mierzy się sześć pozostałych wariantów.

### Tokeny

| Token | HEX | Rola w dokumencie |
|---|---|---|
| `primary` | `#4A1D26` | kolor wiodący: nagłówki H1/H2, wypełnienie CTA, linia sekcji |
| `secondary` | `#8C5026` | kolor wspierający: H3, podtytuły, nagłówki kolumn w tabeli |
| `accent` | `#B58540` | akcent: pieczęć, sygnatura, cienka linia ozdobna, wyróżnik liczby |
| `neutral-dark` | `#1E1611` | najciemniejszy neutral: etykieta na jasnych wypełnieniach, tło stopki |
| `neutral-light` | `#E4DACB` | jasny neutral: tło calloutu, etykieta na ciemnych wypełnieniach, pas nagłówka |
| `success` | `#2F4A32` | stan potwierdzony: zatwierdzona karta usługi, zdany egzamin, wypłacone dofinansowanie |
| `warning` | `#D9AC4A` | stan wymagający uwagi: termin naboru, brakujący załącznik |
| `error` | `#AC151F` | stan błędu: odrzucony wniosek, niespełniony wymóg |
| `info` | `#1B2B26` | nota informacyjna, przypis regulacyjny, boks „podstawa prawna” |
| `background` | `#F7F3EA` | tło strony |
| `surface` | `#F2ECE1` | tło karty i tabeli, czyli papier dokumentu |
| `border` | `#1E1611` | linie tabeli, obrys karty, obrys pola formularza |
| `text-primary` | `#1E1611` | tekst korpusu |
| `text-secondary` | `#5B4837` | metadane, przypisy, opisy kolumn |
| `link` | `#AC151F` | odnośnik w treści i w interfejsie |

### Etykieta na wypełnieniu - kolor przepisany, nie dowolny

| Wypełnienie | Kolor etykiety | HEX etykiety | Kontrast | Ocena |
|---|---|---|---|---|
| `primary` `#4A1D26` | `neutral-light` | `#E4DACB` | 10,16:1 | AAA |
| `secondary` `#8C5026` | `neutral-light` | `#E4DACB` | 4,62:1 | AA |
| `accent` `#B58540` | `neutral-dark` | `#1E1611` | 5,43:1 | AA |
| `success` `#2F4A32` | `neutral-light` | `#E4DACB` | 7,08:1 | AAA |
| `warning` `#D9AC4A` | `neutral-dark` | `#1E1611` | 8,45:1 | AAA |
| `error` `#AC151F` | `neutral-light` | `#E4DACB` | 5,27:1 | AA |
| `info` `#1B2B26` | `neutral-light` | `#E4DACB` | 10,70:1 | AAA |

### Zmierzony kontrast par kluczowych

| Para | Kontrast | Ocena |
|---|---|---|
| text-primary na background | 16,10:1 | AAA |
| text-primary na surface | 15,16:1 | AAA |
| text-secondary na background | 7,81:1 | AAA |
| text-secondary na surface | 7,36:1 | AAA |
| primary (H1/H2) na surface | 11,95:1 | AAA |
| secondary (H3) na surface | 5,43:1 | AA |
| link na surface | 6,20:1 | AA |
| link na background | 6,58:1 | AA |
| text-primary na neutral-light (callout) | 12,89:1 | AAA |
| primary na neutral-light (naglowek callouta) | 10,16:1 | AAA |
| etykieta neutral-light na primary | 10,16:1 | AAA |
| etykieta neutral-dark na accent | 5,43:1 | AA |
| etykieta neutral-light na success | 7,08:1 | AAA |
| etykieta neutral-dark na warning | 8,45:1 | AAA |
| etykieta neutral-light na error | 5,27:1 | AA |
| etykieta neutral-light na info | 10,70:1 | AAA |
| border na surface | 15,16:1 | OK (≥3:1, element interfejsu) |
| border na background | 16,10:1 | OK (≥3:1, element interfejsu) |
| accent jako linia/ikona na surface | 2,79:1 | **poniżej 3:1** |

**Pary poniżej progu w tym wariancie:**

- `accent jako linia/ikona na surface` = 2,79:1 - PONIZEJ 3:1.

### Rozróżnialność kolorów o różnym znaczeniu

| Para znaczeniowa | Kontrast wzajemny | Odczyt |
|---|---|---|
| `link` wobec `error` | 1,00:1 | wysokie ryzyko zlania się |
| `link` wobec `primary` | 1,93:1 | rozróżnialne jasnością |
| `primary` wobec `secondary` | 2,20:1 | rozróżnialne jasnością |
| `success` wobec `primary` | 1,44:1 | ryzyko umiarkowane |
| `accent` wobec `warning` | 1,56:1 | ryzyko umiarkowane |
| `info` wobec `primary` | 1,05:1 | wysokie ryzyko zlania się |

### Rekomendowane użycie

Nagłówki: Aksamit (`primary`). CTA: wypełnienie Aksamit z etykietą Pergamin. Tła: Muślin (strona) i Kaszmir (karta). Tabele: linie pełnym Espresso, nagłówek kolumny Sepia wersalikami. Callouty: tło Pergamin, nagłówek Aksamit. Link: Karmin.

### Plusy

- Zero kosztu decyzyjnego - specyfikacja jest już zatwierdzona (2026-09-02) i wpisana do `03-pakiet-claude-design/format-paczki.md`.
- Najwyższy kontrast tekstu korpusu w całym zestawie po wariancie 6.
- Ciepły papier i bordo odróżniają IRIN od granatowo-białego standardu rynku szkoleniowego.

### Minusy

- `link` i `error` to fizycznie ten sam kolor `#AC151F` - kontrast wzajemny 1,00:1. Czytelnik nie odróżni odnośnika od komunikatu błędu inaczej niż z kontekstu zdania.
- `info` (Onyks `#1B2B26`) i `text-primary` (Espresso `#1E1611`) różnią się o 1,05:1 - token informacyjny nie niesie żadnego sygnału, bo wygląda jak zwykły tekst.
- `border` to pełne Espresso: każda linia w tabeli ma wagę ramki, nie ma miejsca na hierarchię linii cienkiej i grubej.
- Złoto foliowe jako linia lub ikona daje 2,79:1 - poniżej progu 3:1 dla elementów interfejsu (zgodnie zresztą z własnym zastrzeżeniem palety, że złoto jest pieczęcią, nie kreską).

### Ryzyka

- Ciepłe tła `#F7F3EA` i `#F2ECE1` w konwersji do CMYK potrafią żółknąć różnie na różnych maszynach - różnica papieru strony i karty (16,10 wobec 15,16) jest na tyle mała, że przy druku może zniknąć zupełnie.
- Brak osobnego koloru linku blokuje planowany portal sprzedaży szkoleń - w interfejsie odnośnik w kolorze błędu to defekt użyteczności, nie kwestia gustu.

### Co ten wniosek obala

Ten wniosek obala pokazanie dokumentu, w którym link i komunikat błędu występują obok siebie i są rozróżniane - jeśli w realnych dokumentach IRIN link nigdy nie sąsiaduje ze stanem błędu, zarzut traci moc.

---

## Wariant 2 - Kaszmir Wyciszony

Ten sam papier i ta sama rodzina bordo co w wariancie zatwierdzonym, ale z obniżonym nasyceniem akcentów, osobnym półtonem na obramowania i linkiem przesuniętym w głęboką morską zieleń, żeby przestał być tym samym kolorem co błąd.

### Tokeny

| Token | HEX | Rola w dokumencie |
|---|---|---|
| `primary` | `#452430` | kolor wiodący: nagłówki H1/H2, wypełnienie CTA, linia sekcji |
| `secondary` | `#7A5638` | kolor wspierający: H3, podtytuły, nagłówki kolumn w tabeli |
| `accent` | `#A8874E` | akcent: pieczęć, sygnatura, cienka linia ozdobna, wyróżnik liczby |
| `neutral-dark` | `#221A15` | najciemniejszy neutral: etykieta na jasnych wypełnieniach, tło stopki |
| `neutral-light` | `#E7DFD2` | jasny neutral: tło calloutu, etykieta na ciemnych wypełnieniach, pas nagłówka |
| `success` | `#2E5241` | stan potwierdzony: zatwierdzona karta usługi, zdany egzamin, wypłacone dofinansowanie |
| `warning` | `#8A6110` | stan wymagający uwagi: termin naboru, brakujący załącznik |
| `error` | `#9E2B2B` | stan błędu: odrzucony wniosek, niespełniony wymóg |
| `info` | `#33474F` | nota informacyjna, przypis regulacyjny, boks „podstawa prawna” |
| `background` | `#F6F2E9` | tło strony |
| `surface` | `#FBF8F2` | tło karty i tabeli, czyli papier dokumentu |
| `border` | `#938978` | linie tabeli, obrys karty, obrys pola formularza |
| `text-primary` | `#221A15` | tekst korpusu |
| `text-secondary` | `#5E4E40` | metadane, przypisy, opisy kolumn |
| `link` | `#2F5A63` | odnośnik w treści i w interfejsie |

### Etykieta na wypełnieniu - kolor przepisany, nie dowolny

| Wypełnienie | Kolor etykiety | HEX etykiety | Kontrast | Ocena |
|---|---|---|---|---|
| `primary` `#452430` | `neutral-light` | `#E7DFD2` | 10,26:1 | AAA |
| `secondary` `#7A5638` | `neutral-light` | `#E7DFD2` | 4,94:1 | AA |
| `accent` `#A8874E` | `neutral-dark` | `#221A15` | 5,09:1 | AA |
| `success` `#2E5241` | `neutral-light` | `#E7DFD2` | 6,62:1 | AA |
| `warning` `#8A6110` | `#FFFFFF` | `#FFFFFF` | 5,53:1 | AA |
| `error` `#9E2B2B` | `neutral-light` | `#E7DFD2` | 5,60:1 | AA |
| `info` `#33474F` | `neutral-light` | `#E7DFD2` | 7,37:1 | AAA |

### Zmierzony kontrast par kluczowych

| Para | Kontrast | Ocena |
|---|---|---|
| text-primary na background | 15,32:1 | AAA |
| text-primary na surface | 16,15:1 | AAA |
| text-secondary na background | 7,12:1 | AAA |
| text-secondary na surface | 7,50:1 | AAA |
| primary (H1/H2) na surface | 12,80:1 | AAA |
| secondary (H3) na surface | 6,16:1 | AA |
| link na surface | 7,17:1 | AAA |
| link na background | 6,80:1 | AA |
| text-primary na neutral-light (callout) | 12,95:1 | AAA |
| primary na neutral-light (naglowek callouta) | 10,26:1 | AAA |
| etykieta neutral-light na primary | 10,26:1 | AAA |
| etykieta neutral-dark na accent | 5,09:1 | AA |
| etykieta neutral-light na success | 6,62:1 | AA |
| etykieta #FFFFFF na warning | 5,53:1 | AA |
| etykieta neutral-light na error | 5,60:1 | AA |
| etykieta neutral-light na info | 7,37:1 | AAA |
| border na surface | 3,25:1 | OK (≥3:1, element interfejsu) |
| border na background | 3,09:1 | OK (≥3:1, element interfejsu) |
| accent jako linia/ikona na surface | 3,17:1 | OK (≥3:1, element interfejsu) |

**Pary poniżej progu w tym wariancie: brak.** Każda para tekstowa przechodzi co najmniej AA, każdy element interfejsu co najmniej 3:1.

### Rozróżnialność kolorów o różnym znaczeniu

| Para znaczeniowa | Kontrast wzajemny | Odczyt |
|---|---|---|
| `link` wobec `error` | 1,03:1 | wysokie ryzyko zlania się |
| `link` wobec `primary` | 1,79:1 | ryzyko umiarkowane |
| `primary` wobec `secondary` | 2,08:1 | rozróżnialne jasnością |
| `success` wobec `primary` | 1,55:1 | ryzyko umiarkowane |
| `accent` wobec `warning` | 1,64:1 | ryzyko umiarkowane |
| `info` wobec `primary` | 1,39:1 | ryzyko umiarkowane |

### Rekomendowane użycie

Nagłówki: `primary #452430`. H3 i podtytuły: `secondary #7A5638`. CTA: wypełnienie `primary`, etykieta `neutral-light`. Tabele: linie `border #938978`, nagłówek kolumny `text-secondary` wersalikami. Callouty: tło `neutral-light`, nagłówek `primary`. Link: `#2F5A63`. Złoto `#A8874E` wyłącznie jako cienka linia sygnaturowa.

### Plusy

- Naprawia wszystkie trzy zmierzone defekty wariantu zatwierdzonego: link przestaje być kolorem błędu, `border` dostaje własny półton 3,25:1, `info` przestaje udawać tekst korpusu.
- Zachowuje to, co founder już zatwierdził - ciepły papier, bordo jako kolor wiodący, złoto jako sygnaturę - więc koszt ponownego zatwierdzania jest najmniejszy z sześciu propozycji zmiany.
- Komplet par tekstowych na poziomie AA lub wyżej, zero wyjątków, zero pozycji poniżej progu.

### Minusy

- Chłodny morski link w całkowicie ciepłym systemie jest tonem obcym - to świadomy kompromis na rzecz rozróżnialności, ale widać go.
- Wyciszenie odbiera Aksamitowi część charakteru: `#452430` jest spokojniejszy i mniej rozpoznawalny niż `#4A1D26`.
- Różnica wizualna wobec wariantu 1 jest niewielka - jeśli oczekujesz widocznej zmiany kierunku, ten wariant jej nie da.

### Ryzyka

- „Wyciszenie” może zostać odczytane jako brak decyzji, a nie jako decyzja.
- Link `#2F5A63` i `info #33474F` różnią się o 1,15:1 - jeśli oba pojawią się na jednej karcie (odnośnik wewnątrz boksu informacyjnego), zleją się.

### Co ten wniosek obala

Ten wniosek obala sytuacja, w której niezadowolenie z obecnej palety dotyczy samego kierunku „ciepły papier plus bordo”, a nie jego szczegółów - wtedy poprawianie detali jest pracą w złą stronę, a odpowiedzią jest wariant 4 albo 7.

---

## Wariant 3 - Papier i Grafit

Ciepły papier zostaje, ale tusz przestaje być brązowy: cały szkielet typograficzny przechodzi na grafit, a jedynym kolorem pozostaje miedź. System przestaje wyglądać jak stara księga, zaczyna wyglądać jak dokument techniczny na dobrym papierze.

### Tokeny

| Token | HEX | Rola w dokumencie |
|---|---|---|
| `primary` | `#2B3138` | kolor wiodący: nagłówki H1/H2, wypełnienie CTA, linia sekcji |
| `secondary` | `#5A6470` | kolor wspierający: H3, podtytuły, nagłówki kolumn w tabeli |
| `accent` | `#A85E28` | akcent: pieczęć, sygnatura, cienka linia ozdobna, wyróżnik liczby |
| `neutral-dark` | `#16191D` | najciemniejszy neutral: etykieta na jasnych wypełnieniach, tło stopki |
| `neutral-light` | `#E6E2DA` | jasny neutral: tło calloutu, etykieta na ciemnych wypełnieniach, pas nagłówka |
| `success` | `#26614A` | stan potwierdzony: zatwierdzona karta usługi, zdany egzamin, wypłacone dofinansowanie |
| `warning` | `#8A5D0F` | stan wymagający uwagi: termin naboru, brakujący załącznik |
| `error` | `#A32D2A` | stan błędu: odrzucony wniosek, niespełniony wymóg |
| `info` | `#2A5670` | nota informacyjna, przypis regulacyjny, boks „podstawa prawna” |
| `background` | `#F6F3ED` | tło strony |
| `surface` | `#FCFAF6` | tło karty i tabeli, czyli papier dokumentu |
| `border` | `#8F8B83` | linie tabeli, obrys karty, obrys pola formularza |
| `text-primary` | `#16191D` | tekst korpusu |
| `text-secondary` | `#515961` | metadane, przypisy, opisy kolumn |
| `link` | `#1F5B7A` | odnośnik w treści i w interfejsie |

### Etykieta na wypełnieniu - kolor przepisany, nie dowolny

| Wypełnienie | Kolor etykiety | HEX etykiety | Kontrast | Ocena |
|---|---|---|---|---|
| `primary` `#2B3138` | `neutral-light` | `#E6E2DA` | 10,17:1 | AAA |
| `secondary` `#5A6470` | `neutral-light` | `#E6E2DA` | 4,66:1 | AA |
| `accent` `#A85E28` | `#FFFFFF` | `#FFFFFF` | 4,89:1 | AA |
| `success` `#26614A` | `neutral-light` | `#E6E2DA` | 5,62:1 | AA |
| `warning` `#8A5D0F` | `#FFFFFF` | `#FFFFFF` | 5,75:1 | AA |
| `error` `#A32D2A` | `neutral-light` | `#E6E2DA` | 5,48:1 | AA |
| `info` `#2A5670` | `neutral-light` | `#E6E2DA` | 6,10:1 | AA |

### Zmierzony kontrast par kluczowych

| Para | Kontrast | Ocena |
|---|---|---|
| text-primary na background | 15,92:1 | AAA |
| text-primary na surface | 16,91:1 | AAA |
| text-secondary na background | 6,42:1 | AA |
| text-secondary na surface | 6,83:1 | AA |
| primary (H1/H2) na surface | 12,60:1 | AAA |
| secondary (H3) na surface | 5,77:1 | AA |
| link na surface | 7,10:1 | AAA |
| link na background | 6,69:1 | AA |
| text-primary na neutral-light (callout) | 13,65:1 | AAA |
| primary na neutral-light (naglowek callouta) | 10,17:1 | AAA |
| etykieta neutral-light na primary | 10,17:1 | AAA |
| etykieta #FFFFFF na accent | 4,89:1 | AA |
| etykieta neutral-light na success | 5,62:1 | AA |
| etykieta #FFFFFF na warning | 5,75:1 | AA |
| etykieta neutral-light na error | 5,48:1 | AA |
| etykieta neutral-light na info | 6,10:1 | AA |
| border na surface | 3,25:1 | OK (≥3:1, element interfejsu) |
| border na background | 3,06:1 | OK (≥3:1, element interfejsu) |
| accent jako linia/ikona na surface | 4,69:1 | OK (≥3:1, element interfejsu) |

**Pary poniżej progu w tym wariancie: brak.** Każda para tekstowa przechodzi co najmniej AA, każdy element interfejsu co najmniej 3:1.

### Rozróżnialność kolorów o różnym znaczeniu

| Para znaczeniowa | Kontrast wzajemny | Odczyt |
|---|---|---|
| `link` wobec `error` | 1,05:1 | wysokie ryzyko zlania się |
| `link` wobec `primary` | 1,77:1 | ryzyko umiarkowane |
| `primary` wobec `secondary` | 2,18:1 | rozróżnialne jasnością |
| `success` wobec `primary` | 1,81:1 | rozróżnialne jasnością |
| `accent` wobec `warning` | 1,18:1 | wysokie ryzyko zlania się |
| `info` wobec `primary` | 1,67:1 | ryzyko umiarkowane |

### Rekomendowane użycie

Nagłówki: grafit `#2B3138`. Podtytuły i metadane: `#5A6470`. CTA: wypełnienie grafit z etykietą `neutral-light`; wariant alternatywny - wypełnienie miedź `#A85E28` z etykietą białą. Tabele: linie `#8F8B83`. Callouty: tło `#E6E2DA`. Link: `#1F5B7A`.

### Plusy

- Najczytelniejsze tabele w zestawie: neutralny grafit nie wnosi własnej temperatury, więc dane nie „ciepleją”.
- Miedź jako linia i ikona daje 4,69:1 - jedyny akcent w ciepłej rodzinie, który realnie nadaje się na cienką kreskę, a nie tylko na plamę.
- Najtańszy i najbardziej przewidywalny druk: grafit wychodzi tak samo na każdej maszynie, w odróżnieniu od bordo.

### Minusy

- Grafit jest neutralny, więc nie niesie żadnego znaczenia marki - to najłatwiejszy wariant do pomylenia z dowolną inną firmą doradczą.
- `accent` (miedź `#A85E28`) i `warning` (`#8A5D0F`) różnią się o 1,18:1 - akcent marki i ostrzeżenie to praktycznie ta sama plama.
- Znika Aksamit, czyli jedyny kolor, który w kanwie foundera miał własną nazwę i przypisaną dziedzinę (Pedagogika).

### Ryzyka

- To wariant, w którym najłatwiej wyjść „jak każdy” - cała różnica trzyma się na jednym akcencie, więc wystarczy użyć go oszczędnie i marka znika.
- Trzy dziedziny IRIN tracą kolory dziedzinowe - reguła 80/15/5 wymaga wtedy przebudowy, bo nie ma trzech akcentów dziedzinowych, tylko jeden akcent w ogóle.

### Co ten wniosek obala

Ten wniosek obala pokazanie, że trzy dziedziny IRIN nie muszą być rozróżniane kolorem - jeśli rozróżnia je układ albo piktogram, zarzut o utracie kolorów dziedzinowych upada.

---

## Wariant 4 - Instytut

Granat dokumentu urzędowego jako kolor wiodący, przy zachowanym ciepłym papierze. Dokument ma wyglądać wiarygodnie na biurku operatora dofinansowania, w PARP i w BGK, a nie w portfolio agencji.

### Tokeny

| Token | HEX | Rola w dokumencie |
|---|---|---|
| `primary` | `#1B3A5C` | kolor wiodący: nagłówki H1/H2, wypełnienie CTA, linia sekcji |
| `secondary` | `#3E6285` | kolor wspierający: H3, podtytuły, nagłówki kolumn w tabeli |
| `accent` | `#B07A2E` | akcent: pieczęć, sygnatura, cienka linia ozdobna, wyróżnik liczby |
| `neutral-dark` | `#131A21` | najciemniejszy neutral: etykieta na jasnych wypełnieniach, tło stopki |
| `neutral-light` | `#E6E1D6` | jasny neutral: tło calloutu, etykieta na ciemnych wypełnieniach, pas nagłówka |
| `success` | `#1F6B4F` | stan potwierdzony: zatwierdzona karta usługi, zdany egzamin, wypłacone dofinansowanie |
| `warning` | `#8F6412` | stan wymagający uwagi: termin naboru, brakujący załącznik |
| `error` | `#A32F30` | stan błędu: odrzucony wniosek, niespełniony wymóg |
| `info` | `#1F5F7D` | nota informacyjna, przypis regulacyjny, boks „podstawa prawna” |
| `background` | `#F6F4EF` | tło strony |
| `surface` | `#FDFCF9` | tło karty i tabeli, czyli papier dokumentu |
| `border` | `#878C90` | linie tabeli, obrys karty, obrys pola formularza |
| `text-primary` | `#131A21` | tekst korpusu |
| `text-secondary` | `#47525D` | metadane, przypisy, opisy kolumn |
| `link` | `#14507E` | odnośnik w treści i w interfejsie |

### Etykieta na wypełnieniu - kolor przepisany, nie dowolny

| Wypełnienie | Kolor etykiety | HEX etykiety | Kontrast | Ocena |
|---|---|---|---|---|
| `primary` `#1B3A5C` | `neutral-light` | `#E6E1D6` | 8,92:1 | AAA |
| `secondary` `#3E6285` | `neutral-light` | `#E6E1D6` | 4,89:1 | AA |
| `accent` `#B07A2E` | `neutral-dark` | `#131A21` | 4,73:1 | AA |
| `success` `#1F6B4F` | `neutral-light` | `#E6E1D6` | 4,92:1 | AA |
| `warning` `#8F6412` | `#FFFFFF` | `#FFFFFF` | 5,25:1 | AA |
| `error` `#A32F30` | `neutral-light` | `#E6E1D6` | 5,36:1 | AA |
| `info` `#1F5F7D` | `neutral-light` | `#E6E1D6` | 5,38:1 | AA |

### Zmierzony kontrast par kluczowych

| Para | Kontrast | Ocena |
|---|---|---|
| text-primary na background | 15,96:1 | AAA |
| text-primary na surface | 17,09:1 | AAA |
| text-secondary na background | 7,26:1 | AAA |
| text-secondary na surface | 7,77:1 | AAA |
| primary (H1/H2) na surface | 11,33:1 | AAA |
| secondary (H3) na surface | 6,22:1 | AA |
| link na surface | 8,26:1 | AAA |
| link na background | 7,71:1 | AAA |
| text-primary na neutral-light (callout) | 13,45:1 | AAA |
| primary na neutral-light (naglowek callouta) | 8,92:1 | AAA |
| etykieta neutral-light na primary | 8,92:1 | AAA |
| etykieta neutral-dark na accent | 4,73:1 | AA |
| etykieta neutral-light na success | 4,92:1 | AA |
| etykieta #FFFFFF na warning | 5,25:1 | AA |
| etykieta neutral-light na error | 5,36:1 | AA |
| etykieta neutral-light na info | 5,38:1 | AA |
| border na surface | 3,31:1 | OK (≥3:1, element interfejsu) |
| border na background | 3,09:1 | OK (≥3:1, element interfejsu) |
| accent jako linia/ikona na surface | 3,61:1 | OK (≥3:1, element interfejsu) |

**Pary poniżej progu w tym wariancie: brak.** Każda para tekstowa przechodzi co najmniej AA, każdy element interfejsu co najmniej 3:1.

### Rozróżnialność kolorów o różnym znaczeniu

| Para znaczeniowa | Kontrast wzajemny | Odczyt |
|---|---|---|
| `link` wobec `error` | 1,21:1 | wysokie ryzyko zlania się |
| `link` wobec `primary` | 1,37:1 | ryzyko umiarkowane |
| `primary` wobec `secondary` | 1,82:1 | rozróżnialne jasnością |
| `success` wobec `primary` | 1,81:1 | rozróżnialne jasnością |
| `accent` wobec `warning` | 1,42:1 | ryzyko umiarkowane |
| `info` wobec `primary` | 1,66:1 | ryzyko umiarkowane |

### Rekomendowane użycie

Nagłówki: granat `#1B3A5C`. Podtytuły: `#3E6285`. CTA: wypełnienie granat, etykieta `neutral-light`. Tabele: linie `#878C90`, nagłówek kolumny granatem wersalikami. Callouty prawne: tło `#E6E1D6`, lewa krawędź granatowa. Link: `#14507E`. Złoto `#B07A2E` na pieczęć i sygnaturę certyfikatu.

### Plusy

- Najwyższy kontrast linku w zestawie po wariancie 6 - 8,26:1 na karcie i 7,71:1 na tle strony.
- Granat na ciepłym papierze to połączenie nietypowe: daje powagę urzędową bez chłodu, który niesie granat na bieli.
- Najlepiej ze wszystkich wariantów obsługuje dokumenty regulowane - kartę usługi BUR, zaświadczenie KFS, wniosek pożyczkowy - bo mówi kodem wizualnym, który ich odbiorca już zna.

### Minusy

- Granat jest najbardziej obsadzonym kolorem w polskim B2B i w finansach - ryzyko nierozróżnialności jest tu najwyższe z całego zestawu.
- `link` i `primary` różnią się o 1,37:1 - odnośnik wewnątrz nagłówka albo tuż pod nim praktycznie ginie.
- Odchodzi najdalej od tego, co zostało zatwierdzone 2026-09-02: Aksamit znika całkowicie, a z 12 barw zostaje sam ciepły papier i złoto.

### Ryzyka

- Ton może wyjść „bank albo urząd” zamiast „instytut” - to trafia w Pożyczki UE/BGK, ale rozmija się z Akademią AI, która ma brzmieć współcześnie.
- Przy druku offsetowym głębokie granaty często zbijają się w czerń - różnica `#1B3A5C` i `text-primary #131A21` wynosi 1,50:1 i może zniknąć.

### Co ten wniosek obala

Ten wniosek obala sprawdzenie, kto faktycznie czyta dokumenty IRIN - jeśli główną publicznością są działy HR firm, a nie operatorzy dofinansowania, argument o kodzie urzędowym przestaje działać.

---

## Wariant 5 - Werdykt

Kolor Werdykt, który w zatwierdzonej palecie pełnił funkcję stanu potwierdzonego, awansuje na kolor wiodący. Zieleń instytucjonalna niesie rozwój i staranność bez fintechowego granatu, a złoto zostaje jako sygnatura.

### Tokeny

| Token | HEX | Rola w dokumencie |
|---|---|---|
| `primary` | `#1E4A38` | kolor wiodący: nagłówki H1/H2, wypełnienie CTA, linia sekcji |
| `secondary` | `#3C6B54` | kolor wspierający: H3, podtytuły, nagłówki kolumn w tabeli |
| `accent` | `#B08237` | akcent: pieczęć, sygnatura, cienka linia ozdobna, wyróżnik liczby |
| `neutral-dark` | `#14201A` | najciemniejszy neutral: etykieta na jasnych wypełnieniach, tło stopki |
| `neutral-light` | `#E2E4DC` | jasny neutral: tło calloutu, etykieta na ciemnych wypełnieniach, pas nagłówka |
| `success` | `#226B45` | stan potwierdzony: zatwierdzona karta usługi, zdany egzamin, wypłacone dofinansowanie |
| `warning` | `#8B6212` | stan wymagający uwagi: termin naboru, brakujący załącznik |
| `error` | `#A22E2C` | stan błędu: odrzucony wniosek, niespełniony wymóg |
| `info` | `#26596B` | nota informacyjna, przypis regulacyjny, boks „podstawa prawna” |
| `background` | `#F5F4EE` | tło strony |
| `surface` | `#FCFBF6` | tło karty i tabeli, czyli papier dokumentu |
| `border` | `#898D87` | linie tabeli, obrys karty, obrys pola formularza |
| `text-primary` | `#14201A` | tekst korpusu |
| `text-secondary` | `#455249` | metadane, przypisy, opisy kolumn |
| `link` | `#1D5A6B` | odnośnik w treści i w interfejsie |

### Etykieta na wypełnieniu - kolor przepisany, nie dowolny

| Wypełnienie | Kolor etykiety | HEX etykiety | Kontrast | Ocena |
|---|---|---|---|---|
| `primary` `#1E4A38` | `neutral-light` | `#E2E4DC` | 7,82:1 | AAA |
| `secondary` `#3C6B54` | `neutral-light` | `#E2E4DC` | 4,78:1 | AA |
| `accent` `#B08237` | `neutral-dark` | `#14201A` | 4,87:1 | AA |
| `success` `#226B45` | `neutral-light` | `#E2E4DC` | 5,02:1 | AA |
| `warning` `#8B6212` | `#FFFFFF` | `#FFFFFF` | 5,45:1 | AA |
| `error` `#A22E2C` | `neutral-light` | `#E2E4DC` | 5,52:1 | AA |
| `info` `#26596B` | `neutral-light` | `#E2E4DC` | 6,01:1 | AA |

### Zmierzony kontrast par kluczowych

| Para | Kontrast | Ocena |
|---|---|---|
| text-primary na background | 15,23:1 | AAA |
| text-primary na surface | 16,20:1 | AAA |
| text-secondary na background | 7,46:1 | AAA |
| text-secondary na surface | 7,93:1 | AAA |
| primary (H1/H2) na surface | 9,69:1 | AAA |
| secondary (H3) na surface | 5,92:1 | AA |
| link na surface | 7,43:1 | AAA |
| link na background | 6,99:1 | AA |
| text-primary na neutral-light (callout) | 13,08:1 | AAA |
| primary na neutral-light (naglowek callouta) | 7,82:1 | AAA |
| etykieta neutral-light na primary | 7,82:1 | AAA |
| etykieta neutral-dark na accent | 4,87:1 | AA |
| etykieta neutral-light na success | 5,02:1 | AA |
| etykieta #FFFFFF na warning | 5,45:1 | AA |
| etykieta neutral-light na error | 5,52:1 | AA |
| etykieta neutral-light na info | 6,01:1 | AA |
| border na surface | 3,26:1 | OK (≥3:1, element interfejsu) |
| border na background | 3,06:1 | OK (≥3:1, element interfejsu) |
| accent jako linia/ikona na surface | 3,33:1 | OK (≥3:1, element interfejsu) |

**Pary poniżej progu w tym wariancie: brak.** Każda para tekstowa przechodzi co najmniej AA, każdy element interfejsu co najmniej 3:1.

### Rozróżnialność kolorów o różnym znaczeniu

| Para znaczeniowa | Kontrast wzajemny | Odczyt |
|---|---|---|
| `link` wobec `error` | 1,09:1 | wysokie ryzyko zlania się |
| `link` wobec `primary` | 1,30:1 | ryzyko umiarkowane |
| `primary` wobec `secondary` | 1,64:1 | ryzyko umiarkowane |
| `success` wobec `primary` | 1,56:1 | ryzyko umiarkowane |
| `accent` wobec `warning` | 1,58:1 | ryzyko umiarkowane |
| `info` wobec `primary` | 1,30:1 | ryzyko umiarkowane |

### Rekomendowane użycie

Nagłówki: zieleń `#1E4A38`. Podtytuły: `#3C6B54`. CTA: wypełnienie zieleń, etykieta `neutral-light`. Tabele: linie `#898D87`. Callouty: tło `#E2E4DC`. Link: `#1D5A6B`. Złoto `#B08237` na pieczęć certyfikatu.

### Plusy

- Wyrasta z koloru, który jest już w zatwierdzonej palecie - to nie import z zewnątrz, tylko przesunięcie akcentu.
- Odróżnia IRIN od granatowego standardu branży finansowej przy zachowaniu powagi.
- Ciepła zieleń dobrze znosi papier - lepiej niż granat, który na kremowym podłożu szarzeje.

### Minusy

- `success` (`#226B45`) i `primary` (`#1E4A38`) różnią się o 1,56:1 - kolor marki i kolor „potwierdzone” należą do tej samej rodziny, więc stan potwierdzenia przestaje być sygnałem i staje się tłem.
- `link` (`#1D5A6B`) wobec `primary` to 1,30:1 - najniższa rozróżnialność linku w całym zestawie.
- Zieleń w kontekście dofinansowań bywa odczytana jako obietnica tematyczna („zielone dotacje”, ESG), której IRIN nie składa.

### Ryzyka

- Kolizja semantyczna `primary` z `success` jest tu problemem strukturalnym, nie kosmetycznym - każdy dokument ze statusem „zatwierdzone” traci na czytelności.
- Ryzyko odczytu branżowego: odbiorca może założyć, że IRIN specjalizuje się w dofinansowaniach środowiskowych.

### Co ten wniosek obala

Ten wniosek obala rozstrzygnięcie, że stan „potwierdzone” będzie w dokumentach IRIN sygnalizowany ikoną i etykietą słowną, a nie samą plamą koloru - wtedy kolizja `primary` z `success` przestaje mieć znaczenie.

---

## Wariant 6 - Druk Ekonomiczny

Prawie monochromatyczny system z jednym ceglanym akcentem, zaprojektowany pod najgorszy realny scenariusz dystrybucji: zaświadczenie KFS skserowane, zeskanowane i wydrukowane mono w dziale kadr. Nie jest propozycją tożsamości - jest trybem przetrwania.

### Tokeny

| Token | HEX | Rola w dokumencie |
|---|---|---|
| `primary` | `#111111` | kolor wiodący: nagłówki H1/H2, wypełnienie CTA, linia sekcji |
| `secondary` | `#3D3D3D` | kolor wspierający: H3, podtytuły, nagłówki kolumn w tabeli |
| `accent` | `#7A2418` | akcent: pieczęć, sygnatura, cienka linia ozdobna, wyróżnik liczby |
| `neutral-dark` | `#0A0A0A` | najciemniejszy neutral: etykieta na jasnych wypełnieniach, tło stopki |
| `neutral-light` | `#E8E6E1` | jasny neutral: tło calloutu, etykieta na ciemnych wypełnieniach, pas nagłówka |
| `success` | `#2A4F35` | stan potwierdzony: zatwierdzona karta usługi, zdany egzamin, wypłacone dofinansowanie |
| `warning` | `#6B5307` | stan wymagający uwagi: termin naboru, brakujący załącznik |
| `error` | `#8E1B1B` | stan błędu: odrzucony wniosek, niespełniony wymóg |
| `info` | `#2E4560` | nota informacyjna, przypis regulacyjny, boks „podstawa prawna” |
| `background` | `#FBFAF7` | tło strony |
| `surface` | `#FFFFFF` | tło karty i tabeli, czyli papier dokumentu |
| `border` | `#928F89` | linie tabeli, obrys karty, obrys pola formularza |
| `text-primary` | `#0A0A0A` | tekst korpusu |
| `text-secondary` | `#4A4A4A` | metadane, przypisy, opisy kolumn |
| `link` | `#7A2418` | odnośnik w treści i w interfejsie |

### Etykieta na wypełnieniu - kolor przepisany, nie dowolny

| Wypełnienie | Kolor etykiety | HEX etykiety | Kontrast | Ocena |
|---|---|---|---|---|
| `primary` `#111111` | `neutral-light` | `#E8E6E1` | 15,14:1 | AAA |
| `secondary` `#3D3D3D` | `neutral-light` | `#E8E6E1` | 8,71:1 | AAA |
| `accent` `#7A2418` | `neutral-light` | `#E8E6E1` | 8,04:1 | AAA |
| `success` `#2A4F35` | `neutral-light` | `#E8E6E1` | 7,42:1 | AAA |
| `warning` `#6B5307` | `neutral-light` | `#E8E6E1` | 5,88:1 | AA |
| `error` `#8E1B1B` | `neutral-light` | `#E8E6E1` | 7,25:1 | AAA |
| `info` `#2E4560` | `neutral-light` | `#E8E6E1` | 7,88:1 | AAA |

### Zmierzony kontrast par kluczowych

| Para | Kontrast | Ocena |
|---|---|---|
| text-primary na background | 18,97:1 | AAA |
| text-primary na surface | 19,80:1 | AAA |
| text-secondary na background | 8,49:1 | AAA |
| text-secondary na surface | 8,86:1 | AAA |
| primary (H1/H2) na surface | 18,88:1 | AAA |
| secondary (H3) na surface | 10,86:1 | AAA |
| link na surface | 10,03:1 | AAA |
| link na background | 9,61:1 | AAA |
| text-primary na neutral-light (callout) | 15,87:1 | AAA |
| primary na neutral-light (naglowek callouta) | 15,14:1 | AAA |
| etykieta neutral-light na primary | 15,14:1 | AAA |
| etykieta neutral-light na accent | 8,04:1 | AAA |
| etykieta neutral-light na success | 7,42:1 | AAA |
| etykieta neutral-light na warning | 5,88:1 | AA |
| etykieta neutral-light na error | 7,25:1 | AAA |
| etykieta neutral-light na info | 7,88:1 | AAA |
| border na surface | 3,22:1 | OK (≥3:1, element interfejsu) |
| border na background | 3,09:1 | OK (≥3:1, element interfejsu) |
| accent jako linia/ikona na surface | 10,03:1 | OK (≥3:1, element interfejsu) |

**Pary poniżej progu w tym wariancie: brak.** Każda para tekstowa przechodzi co najmniej AA, każdy element interfejsu co najmniej 3:1.

### Rozróżnialność kolorów o różnym znaczeniu

| Para znaczeniowa | Kontrast wzajemny | Odczyt |
|---|---|---|
| `link` wobec `error` | 1,11:1 | wysokie ryzyko zlania się |
| `link` wobec `primary` | 1,88:1 | rozróżnialne jasnością |
| `primary` wobec `secondary` | 1,74:1 | ryzyko umiarkowane |
| `success` wobec `primary` | 2,04:1 | rozróżnialne jasnością |
| `accent` wobec `warning` | 1,37:1 | ryzyko umiarkowane |
| `info` wobec `primary` | 1,92:1 | rozróżnialne jasnością |

### Rekomendowane użycie

Nagłówki: `#111111`. Podtytuły: `#3D3D3D`. CTA: wypełnienie `#111111` albo obrys 2 px z etykietą `#7A2418`. Tabele: linie `#928F89`, nagłówek kolumny czernią wersalikami. Callouty: tło `#E8E6E1` z lewą krawędzią 3 px. Link: `#7A2418` z obowiązkowym podkreśleniem.

### Plusy

- Najwyższe kontrasty w całym zestawie: 18,97:1 dla tekstu na tle strony i 19,80:1 na karcie.
- Każda para przechodzi AA, większość AAA - to jedyny wariant, w którym żaden token nie wymaga zastrzeżenia.
- Zaświadczenie w tej palecie przetrwa kserowanie, skan i druk laserowy bez utraty jakiegokolwiek znaczenia niesionego kolorem.

### Minusy

- Nie jest tożsamością marki - po odjęciu koloru IRIN wygląda jak dowolny formularz urzędowy.
- Po konwersji do skali szarości `success`, `error` i `info` mają zbliżoną jasność - kolor przestaje nieść znaczenie i wymusza etykietę słowną oraz ikonę przy każdym stanie.
- `accent` i `warning` różnią się o 1,37:1 - w druku mono zleją się całkowicie.

### Ryzyka

- Największe ryzyko tego wariantu to jego zaleta: jest tak bezpieczny, że łatwo przyjąć go na stałe i stracić markę.
- Zerowe ciepło - traci się jedyny element, który w kanwie foundera był nazwany wprost (papier Kaszmir).

### Co ten wniosek obala

Ten wniosek obala pomiar realnego kanału dystrybucji zaświadczeń - jeśli zaświadczenia KFS trafiają do odbiorcy wyłącznie jako kolorowy PDF i nikt ich nie kseruje, cała przewaga tego wariantu znika.

---

## Wariant 7 - Portal Cyfrowy

Jedyny wariant zaprojektowany pod ekran, a nie pod papier: chłodna biel jako powierzchnia, morski `primary` i żywy miedziano-pomarańczowy przycisk akcji. Adresuje planowany portal sprzedaży szkoleń, który w żadnym z pozostałych wariantów nie ma właściwego CTA.

### Tokeny

| Token | HEX | Rola w dokumencie |
|---|---|---|
| `primary` | `#10505F` | kolor wiodący: nagłówki H1/H2, wypełnienie CTA, linia sekcji |
| `secondary` | `#2A7F93` | kolor wspierający: H3, podtytuły, nagłówki kolumn w tabeli |
| `accent` | `#C2410C` | akcent: pieczęć, sygnatura, cienka linia ozdobna, wyróżnik liczby |
| `neutral-dark` | `#0F172A` | najciemniejszy neutral: etykieta na jasnych wypełnieniach, tło stopki |
| `neutral-light` | `#E7EDF0` | jasny neutral: tło calloutu, etykieta na ciemnych wypełnieniach, pas nagłówka |
| `success` | `#15803D` | stan potwierdzony: zatwierdzona karta usługi, zdany egzamin, wypłacone dofinansowanie |
| `warning` | `#B45309` | stan wymagający uwagi: termin naboru, brakujący załącznik |
| `error` | `#B91C1C` | stan błędu: odrzucony wniosek, niespełniony wymóg |
| `info` | `#0369A1` | nota informacyjna, przypis regulacyjny, boks „podstawa prawna” |
| `background` | `#F7F9FA` | tło strony |
| `surface` | `#FFFFFF` | tło karty i tabeli, czyli papier dokumentu |
| `border` | `#8A9093` | linie tabeli, obrys karty, obrys pola formularza |
| `text-primary` | `#0F172A` | tekst korpusu |
| `text-secondary` | `#4B5563` | metadane, przypisy, opisy kolumn |
| `link` | `#0369A1` | odnośnik w treści i w interfejsie |

### Etykieta na wypełnieniu - kolor przepisany, nie dowolny

| Wypełnienie | Kolor etykiety | HEX etykiety | Kontrast | Ocena |
|---|---|---|---|---|
| `primary` `#10505F` | `neutral-light` | `#E7EDF0` | 7,61:1 | AAA |
| `secondary` `#2A7F93` | `#FFFFFF` | `#FFFFFF` | 4,61:1 | AA |
| `accent` `#C2410C` | `#FFFFFF` | `#FFFFFF` | 5,18:1 | AA |
| `success` `#15803D` | `#FFFFFF` | `#FFFFFF` | 5,02:1 | AA |
| `warning` `#B45309` | `#FFFFFF` | `#FFFFFF` | 5,02:1 | AA |
| `error` `#B91C1C` | `neutral-light` | `#E7EDF0` | 5,47:1 | AA |
| `info` `#0369A1` | `neutral-light` | `#E7EDF0` | 5,02:1 | AA |

### Zmierzony kontrast par kluczowych

| Para | Kontrast | Ocena |
|---|---|---|
| text-primary na background | 16,91:1 | AAA |
| text-primary na surface | 17,85:1 | AAA |
| text-secondary na background | 7,16:1 | AAA |
| text-secondary na surface | 7,56:1 | AAA |
| primary (H1/H2) na surface | 8,99:1 | AAA |
| secondary (H3) na surface | 4,61:1 | AA |
| link na surface | 5,93:1 | AA |
| link na background | 5,62:1 | AA |
| text-primary na neutral-light (callout) | 15,11:1 | AAA |
| primary na neutral-light (naglowek callouta) | 7,61:1 | AAA |
| etykieta neutral-light na primary | 7,61:1 | AAA |
| etykieta #FFFFFF na accent | 5,18:1 | AA |
| etykieta #FFFFFF na success | 5,02:1 | AA |
| etykieta #FFFFFF na warning | 5,02:1 | AA |
| etykieta neutral-light na error | 5,47:1 | AA |
| etykieta neutral-light na info | 5,02:1 | AA |
| border na surface | 3,24:1 | OK (≥3:1, element interfejsu) |
| border na background | 3,06:1 | OK (≥3:1, element interfejsu) |
| accent jako linia/ikona na surface | 5,18:1 | OK (≥3:1, element interfejsu) |

**Pary poniżej progu w tym wariancie: brak.** Każda para tekstowa przechodzi co najmniej AA, każdy element interfejsu co najmniej 3:1.

### Rozróżnialność kolorów o różnym znaczeniu

| Para znaczeniowa | Kontrast wzajemny | Odczyt |
|---|---|---|
| `link` wobec `error` | 1,09:1 | wysokie ryzyko zlania się |
| `link` wobec `primary` | 1,52:1 | ryzyko umiarkowane |
| `primary` wobec `secondary` | 1,95:1 | rozróżnialne jasnością |
| `success` wobec `primary` | 1,79:1 | ryzyko umiarkowane |
| `accent` wobec `warning` | 1,03:1 | wysokie ryzyko zlania się |
| `info` wobec `primary` | 1,52:1 | ryzyko umiarkowane |

### Rekomendowane użycie

Nagłówki: `#10505F`. Podtytuły: `#2A7F93`. CTA: wypełnienie `#C2410C` z etykietą białą - jedyny naprawdę „klikalny” przycisk w całym zestawie. Tabele: linie `#8A9093`, wiersz naprzemienny `#F7F9FA`. Callouty: tło `#E7EDF0`. Link: `#0369A1` z podkreśleniem.

### Plusy

- Jedyny wariant z realnym kolorem akcji - `#C2410C` na bieli daje 5,18:1 i działa też jako ikona oraz obrys.
- Komplet stanów semantycznych czytelnych na ekranie w standardzie, który zna każdy użytkownik sklepu internetowego.
- Najlepsza podstawa pod tryb ciemny, bo neutralne tło `#0F172A` jest już w palecie jako `neutral-dark`.

### Minusy

- Zrywa z ciepłym papierem, czyli z jedynym elementem tożsamości nazwanym w kanwie po imieniu - dokument drukowany w tej palecie nie wygląda jak IRIN.
- `accent` (`#C2410C`) i `warning` (`#B45309`) różnią się o 1,03:1 - przycisk akcji i ostrzeżenie są nierozróżnialne, co w interfejsie sprzedażowym jest defektem poważnym.
- Najbardziej „domyślnie SaaS” ze wszystkich siedmiu - paleta rozpoznawalna jako biblioteka komponentów, nie jako marka.

### Ryzyka

- Rozdwojenie marki na wersję papierową i ekranową - to najdroższy długoterminowo skutek w całym zestawie.
- Biały `#FFFFFF` jako `surface` w druku oznacza brak papieru Kaszmir, czyli rezygnację z nazwy własnej całego systemu.

### Co ten wniosek obala

Ten wniosek obala decyzja, że portal sprzedaży szkoleń dostaje własną, jawnie oddzieloną paletę produktową - wtedy „rozdwojenie marki” jest zamierzone, a nie ryzykowne.

---

## Trade-offs - porównanie zbiorcze

Jedna tabela, siedem wierszy, pięć wymiarów. Ocena w skali: **wysoka / średnia / niska**, wyprowadzona z pomiarów wyżej, nie z wrażenia.

| # | Wariant | Czytelność druku | Zgodność z decyzją z 2026-09-02 | Odrębność rynkowa | Gotowość do portalu | Higiena semantyczna |
|---|---|---|---|---|---|---|
| 1 | Kaszmir Aksamit (bazowy) | wysoka | **pełna** | wysoka | **niska** (link = błąd) | **niska** (2 kolizje) |
| 2 | Kaszmir Wyciszony | wysoka | wysoka | wysoka | średnia | **wysoka** |
| 3 | Papier i Grafit | **wysoka** | średnia | niska | średnia | średnia |
| 4 | Instytut | średnia | niska | **niska** | wysoka | średnia |
| 5 | Werdykt | wysoka | średnia | wysoka | średnia | niska |
| 6 | Druk Ekonomiczny | **najwyższa** | niska | **najniższa** | niska | średnia (mono) |
| 7 | Portal Cyfrowy | niska | **najniższa** | niska | **wysoka** | średnia |

**Jak czytać kolumny:**

- *Czytelność druku* - kontrast tekstu korpusu i przewidywalność odcienia w CMYK. Wysoka oznacza, że wynik na papierze nie zależy od maszyny.
- *Zgodność z decyzją z 2026-09-02* - ile z zatwierdzonej palety „Kaszmir Aksamit” zostaje. Pełna oznacza brak zmiany, najniższa oznacza wymianę systemu.
- *Odrębność rynkowa* - jak trudno pomylić dokument IRIN z dokumentem innej firmy szkoleniowej albo doradczej.
- *Gotowość do portalu* - czy paleta ma odrębny kolor akcji i komplet czytelnych stanów na ekranie.
- *Higiena semantyczna* - czy dwa kolory o różnym znaczeniu (link i błąd, marka i potwierdzenie, akcent i ostrzeżenie) dają się rozróżnić.

### Ryzyka wspólne dla całego zestawu

- **Druk mono.** W każdym wariancie poza 6 stany `success`, `error` i `info` po konwersji do skali szarości mają zbliżoną jasność. Wniosek dotyczy wszystkich siedmiu: żaden komunikat statusu w dokumencie IRIN nie może być niesiony samym kolorem - potrzebuje etykiety słownej albo ikony. To jest wymóg dostępności (WCAG 1.4.1 „Użycie koloru”), nie preferencja.
- **Ciepłe tła w CMYK.** Warianty 1-5 opierają się na papierze o odcieniu kremowym. Różnica między `background` a `surface` wynosi w nich poniżej jednego punktu kontrastu, więc na części maszyn zniknie i karta przestanie odcinać się od strony. Zabezpieczenie: karta dostaje obrys `border`, nie tylko własne tło.
- **Złoto jako linia.** W wariancie 1 złoto foliowe daje 2,79:1 na karcie, czyli nie nadaje się na cienką kreskę ani ikonę. W wariantach 2-5 akcent złoty jest ciemniejszy i przekracza 3:1, ale margines jest wąski - każde rozjaśnienie złota trzeba przeliczyć na nowo.
- **Kolor jako jedyny nośnik dziedziny.** Reguła 80/15/5 przypisuje dziedzinę kolorowi. W wariantach 3, 6 i 7 nie ma trzech kolorów dziedzinowych, więc reguła wymaga przebudowy albo drugiego nośnika (piktogram, układ okładki).

---

## Rekomendacja

**Wariant 2 - Kaszmir Wyciszony.**

Powód jest w pomiarach, nie w guście. Wariant zatwierdzony 2026-09-02 ma trzy zmierzone defekty funkcjonalne, które pojawiają się w każdym dokumencie zawierającym odnośnik, status i tabelę: `link` i `error` to ten sam kolor (1,00:1), `info` jest nieodróżnialny od tekstu korpusu (1,05:1), a `border` to pełny tusz, więc tabela nie ma hierarchii linii. Wariant 2 usuwa dokładnie te trzy defekty i nie rusza niczego poza nimi - papier Kaszmir, rodzina bordo i złoto jako sygnatura zostają. To jedyny wariant w zestawie z zerem par poniżej progu, który jednocześnie nie unieważnia decyzji podjętej dwa dni wcześniej.

**Co ten wniosek obala:** jeśli powodem wstrzymania palety jest sam kierunek „ciepły papier plus bordo”, a nie jego szczegóły, to wariant 2 jest pracą w złą stronę i rekomendacja upada - wtedy odpowiedzią jest wariant 4 (granat urzędowy) albo 7 (ekranowy). Ta różnica jest jedynym pytaniem, na które nie da się odpowiedzieć pomiarem.

**Rekomendacja dodatkowa - ODRZUCONA przez foundera (2026-09-02).** Proponowałem przyjąć wariant 6 jako obowiązkowy tryb mono obok wybranego, dla zaświadczeń KFS i certyfikatów, które bywają kserowane. Founder wybrał jedną paletę na wszystko. Skutek do zapamiętania: w druku mono Werdykt, Rubryka, Karmin i Onyks mają zbliżoną jasność, więc jedynym zabezpieczeniem czytelności statusu pozostaje obowiązkowa etykieta słowna albo ikona - ta zasada obowiązuje tym bardziej, im mniej mamy trybów.

**Rozstrzygnięcie (2026-09-02): founder wybrał wariant 2.** Rekomendacja została przyjęta. Wariant 2 jest wpisany jako obowiązujący w `../../03-pakiet-claude-design/format-paczki.md`; otwarte pozostają trzy sprawy poboczne: czy wariant 6 wchodzi jako obowiązkowy tryb mono, czy katalog `02-branding/` zostaje pod tym numerem, i czy poziom H3 zostaje na wadze 600.

---

## Walidacja tego dokumentu

| Sprawdzenie | Wynik |
|---|---|
| Liczba wariantów | 7 (wymagane 7) |
| Liczba tokenów w każdym wariancie | 15 (wymagane 15) |
| Spójność nazw tokenów między wariantami | 1 unikalny zestaw nazw, czyli identyczny we wszystkich |
| Pary poniżej progu w całym zestawie | 1 |
| Typografia | niezmieniona; Manrope 200-800 plus Inconsolata, skala z `brandbook.dc.html` sekcja 04 |
| Nadpisanie palety w plikach docelowych | **nie nastąpiło** - `format-paczki.md` i `propozycja-palety-i-siatki-do-potwierdzenia.md` nietknięte |

Jedyna pozycja poniżej progu w całym zestawie to `accent` jako linia interfejsu w wariancie 1 (2,79:1) - to nie jest błąd tej propozycji, tylko zmierzona własność palety zatwierdzonej, zgodna zresztą z jej własnym zastrzeżeniem, że złoto foliowe jest pieczęcią, a nie kreską.
