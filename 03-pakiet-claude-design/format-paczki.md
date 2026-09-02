# Format paczki wejściowej dla Claude Design

Ten plik definiuje, co powinna zawierać paczka wejściowa przekazywana do Claude Design dla dowolnego dokumentu IRIN. Sama kompozycja, layout i grafika powstają w Claude Design — ten plik tylko określa, jakie materiały i informacje muszą się tam znaleźć, żeby to było możliwe.

## Paleta i siatka - zatwierdzone przez foundera

Siatka: zatwierdzona 2026-09-02, bez zmian. Paleta: kierunek zatwierdzony 2026-09-02, następnie wstrzymany do dopracowania i **ponownie zatwierdzony jako wariant 2 „Kaszmir Wyciszony”**. Pomiar siedmiu wariantów i uzasadnienie wyboru: `../02-branding/kolorystyka/palette-options-v2.md`. Historia pierwszej decyzji: `./propozycja-palety-i-siatki-do-potwierdzenia.md`. Dane maszynowe: `../02-branding/kolorystyka/tokens/palette-irin.json`.

### Siatka dokumentu A4

6 kolumn, moduł 25 mm, gutter 4 mm. Marginesy: 18 mm góra, 18 mm lewy, 22 mm prawy, 28 mm dół. Treść: 170 × 251 mm. Zastępuje wersję z `brandbook.dc.html` (moduł 32 mm), która nie mieściła się fizycznie na stronie A4. **Bez zmian względem decyzji z 2026-09-02.**

### Paleta - 14 kolorów, wariant 2 „Kaszmir Wyciszony”

System ma dwie warstwy i obie obowiązują naraz: **nazwa koloru** (tożsamość marki, reguła 80/15/5, przypisanie dziedzin) i **token semantyczny** (rola w dokumencie i w interfejsie). Ten sam kolor ma zawsze obie etykiety - Aksamit *jest* tokenem `primary`, nie ma osobnego koloru wiodącego obok Aksamitu.

| Kolor | Token | Hex | Rola | Kontrast na Kaszmir |
|---|---|---|---|---|
| Kaszmir | `surface` | `#FBF8F2` | papier, tło karty i tabeli | nie dotyczy (tło) |
| Muślin | `background` | `#F6F2E9` | tło strony | nie dotyczy (tło) |
| Pergamin | `neutral-light` | `#E7DFD2` | tło calloutu, pas nagłówka, etykieta na ciemnym wypełnieniu | nie dotyczy (tło) |
| Espresso | `neutral-dark`, `text-primary` | `#221A15` | tusz uniwersalny, tekst korpusu, tło sekcji odwróconej | 16,15:1 |
| Sepia | `text-secondary` | `#5E4E40` | tekst pomocniczy, metadane, przypisy, nagłówki kolumn | 7,50:1 |
| **Aksamit** | `primary` | `#452430` | kolor wiodący: nagłówki H1/H2, wypełnienie CTA; akcent dziedziny **Pedagogika** | 12,80:1 |
| **Miedź** | `secondary` | `#7A5638` | kolor wspierający: H3, podtytuły; akcent dziedziny **Akademia AI** | 6,16:1 |
| **Onyks** | `info` | `#33474F` | nota informacyjna, boks „podstawa prawna”; akcent dziedziny **Pożyczki UE/BGK** | 9,19:1 |
| Złoto foliowe | `accent` | `#A8874E` | pieczęć, sygnatura, cienka linia ozdobna | 3,17:1 |
| Werdykt | `success` | `#2E5241` | stan potwierdzony: zatwierdzona karta usługi, zdany egzamin | 8,26:1 |
| Rubryka | `warning` | `#8A6110` | stan wymagający uwagi: termin naboru, brakujący załącznik | 5,22:1 |
| Karmin | `error` | `#9E2B2B` | stan błędu: odrzucony wniosek, niespełniony wymóg | 6,99:1 |
| **Popiół** | `border` | `#938978` | linie tabeli, obrys karty i pola formularza | 3,25:1 |
| **Patyna** | `link` | `#2F5A63` | odnośnik w treści i w interfejsie | 7,17:1 |

Wszystkie kontrasty policzone wzorem WCAG 2.1 na luminancji względnej sRGB. Progi: tekst normalny AA 4,5:1, AAA 7:1; element interfejsu i grafika znacząca 3:1. **Każda para tekstowa w tej palecie przechodzi co najmniej AA, każdy element interfejsu co najmniej 3:1** - w tej palecie nie ma ani jednej pozycji poniżej progu.

### Etykieta na wypełnieniu - kolor przepisany, nie dowolny

Kiedy kolor jest tłem przycisku, plakietki albo pieczęci, kolor napisu na nim **nie jest wyborem projektowym**. Obowiązuje ta tabela:

| Wypełnienie | Kolor etykiety | Kontrast |
|---|---|---|
| Aksamit `#452430` | Pergamin `#E7DFD2` | 10,26:1 |
| Miedź `#7A5638` | Pergamin `#E7DFD2` | 4,94:1 |
| Onyks `#33474F` | Pergamin `#E7DFD2` | 7,37:1 |
| Złoto foliowe `#A8874E` | Espresso `#221A15` | 5,09:1 |
| Werdykt `#2E5241` | Pergamin `#E7DFD2` | 6,62:1 |
| Rubryka `#8A6110` | biel `#FFFFFF` | 5,53:1 |
| Karmin `#9E2B2B` | Pergamin `#E7DFD2` | 5,60:1 |

### Reguła proporcji 80/15/5 - obowiązuje bez zmian

- **80% - baza:** Kaszmir (tło karty), Muślin (tło strony), Pergamin (drugie tło neutralne), Espresso (tekst korpusu), Sepia (tekst pomocniczy), Popiół (linie). Wszystko, co nie niesie znaczenia kategoryzującego.
- **15% - sygnał dziedziny:** dokładnie jeden z trzech - Aksamit (Pedagogika), Miedź (Akademia AI), Onyks (Pożyczki UE/BGK) - na dokument. Nie mieszać dwóch kolorów dziedzinowych na jednej stronie.
- **5% - aktywność i honor:** Patyna wyłącznie do odnośników i stanów aktywnych, Werdykt do stanu potwierdzonego, Rubryka do stanu wymagającego uwagi, Karmin do stanu błędu, Złoto foliowe **wyłącznie** jako pieczęć, sygnatura albo cienka linia - nigdy jako tło większej powierzchni.

### Kolor nigdy nie jest jedynym nośnikiem statusu

Po konwersji do skali szarości Werdykt, Rubryka, Karmin i Onyks mają zbliżoną jasność. Każdy status w dokumencie IRIN **musi** mieć etykietę słowną albo ikonę obok koloru. To wymóg dostępności (WCAG 1.4.1 „Użycie koloru”), nie preferencja - i dotyczy tak samo zaświadczeń drukowanych mono, jak ekranu.

### Co dokładnie zmieniło się względem palety z 2026-09-02

Poprzednia paleta miała 12 kolorów; ta ma 14. Żaden kolor nie został usunięty, żadna nazwa nie zniknęła, dwa kolory doszły. Wszystkie hexy są nowe, ale dwanaście z nich to przesunięcia w obrębie tego samego koloru, a nie inne barwy.

| Kolor | Było | Jest | Na czym polega zmiana |
|---|---|---|---|
| Kaszmir | `#F2ECE1` | `#FBF8F2` | papier rozjaśniony i odsycony, żeby karta wyraźniej odcinała się od strony |
| Muślin | `#F7F3EA` | `#F6F2E9` | tło strony przygaszone o włos, w parze ze zmianą wyżej |
| Pergamin | `#E4DACB` | `#E7DFD2` | rozjaśniony, mniej żółty |
| Espresso | `#1E1611` | `#221A15` | minimalnie rozjaśniony; nadal najciemniejszy kolor palety |
| Sepia | `#5B4837` | `#5E4E40` | odsycona, mniej rudy |
| Aksamit | `#4A1D26` | `#452430` | odsycony i przesunięty od bordo ku śliwce; spokojniejszy |
| Miedź | `#8C5026` | `#7A5638` | odsycona, bardziej brązowa niż rudo-pomarańczowa |
| **Onyks** | `#1B2B26` | `#33474F` | **istotna zmiana**: z prawie-czerni na łupkowy błękit. Powód: stary Onyks miał wobec Espresso kontrast 1,05:1, czyli był nieodróżnialny od zwykłego tekstu i nie niósł żadnego sygnału. Nowy ma 1,76:1 wobec Espresso - to nadal niewiele w luminancji, ale barwa jest teraz jawnie inna (chłodny łupek wobec ciepłej czerni), więc różnicę widać okiem. |
| Złoto foliowe | `#B58540` | `#A8874E` | pogłębione. Powód: stare złoto dawało 2,79:1 na papierze, czyli **nie przechodziło progu 3:1** dla linii i ikon. Nowe daje 3,17:1, więc wolno go użyć jako cienkiej kreski, a nie tylko plamy. |
| Werdykt | `#2F4A32` | `#2E5241` | przesunięty od zieleni butelkowej ku morskiej |
| **Rubryka** | `#D9AC4A` | `#8A6110` | **zmiana roli, nie tylko odcienia**: było jasne złoto używane jako tło z ciemnym tekstem, jest ciemny bursztyn używany jako tło z tekstem białym albo jako kolor tekstu na papierze. Powód: stara Rubryka nie nadawała się na tekst (kontrast 1,7:1 na papierze), więc token `warning` nie miał czym pisać. |
| Karmin | `#AC151F` | `#9E2B2B` | przygaszony, mniej sygnalizacyjny |
| **Popiół** | *nie istniał* | `#938978` | **kolor nowy**. Powód: wcześniej linie tabeli rysowało się pełnym Espresso, więc każda kreska miała wagę ramki i tabela nie miała hierarchii linii cienkiej i grubej. |
| **Patyna** | *nie istniał* | `#2F5A63` | **kolor nowy**. Powód: wcześniej odnośnik i komunikat błędu były fizycznie tym samym kolorem (Karmin, kontrast wzajemny 1,00:1), więc czytelnik nie mógł ich odróżnić inaczej niż z kontekstu zdania. |

**Dwie nazwy nowe, zatwierdzone przez foundera (2026-09-02):** „Popiół” (`border`) i „Patyna” (`link`). Trzymają się konwencji pozostałych dwunastu - materiał albo barwnik, jak Kaszmir, Aksamit, Sepia, Karmin, Miedź, Onyks - a „Patyna” wiąże się dodatkowo znaczeniowo z Miedzią. Obie nazwy są obowiązujące na równi z pozostałymi dwunastoma.

**Jedno ryzyko, które zostaje w tej palecie:** Patyna (`#2F5A63`) i Onyks (`#33474F`) mają kontrast wzajemny 1,28:1. Jeśli odnośnik trafi do wnętrza boksu informacyjnego rysowanego Onyksem, oba kolory się zleją. Zabezpieczenie: odnośnik wewnątrz boksu `info` zawsze z podkreśleniem.

## Elementy paczki, potwierdzone i gotowe do użycia

### 1. Logotyp

Trzy pliki źródłowe w korzeniu repozytorium: `logo_irin_poziom.svg` (podstawowy, proporcja ok. 1,773:1), `logo_irin_pion.svg` (pola wąskie/wysokie, proporcja ok. 1,135:1), `logo_irin_sygnet.svg` (samodzielny znak). Wszystkie trzy są jednokolorowe (czarne na przezroczystym tle) — same w sobie nie definiują żadnej palety barw (patrz `/CLAUDE.md`).

Zasady **potwierdzone jako obowiązujące** (`/PLAN.md`, "Decyzje foundera — rozstrzygnięte"):
- minimalny rozmiar: 18 mm / 90 px,
- przestrzeń ochronna: x = wysokość liter sygnetu (jednostka względna, nie stała miara),
- zakaz zmiany koloru logotypu, zakaz obracania/pochylania/odbijania lustrzanego, zakaz cienia/poświaty/obrysu, zakaz nieproporcjonalnego rozciągania (te ostatnie cztery zasady są obserwacją z `brandbook.dc.html`, spójną z ogólną praktyką ochrony znaku — ale nie były oddzielnie potwierdzone przez foundera jak dwie pierwsze; do potwierdzenia przy pierwszym realnym użyciu, jeśli founder chce je uznać za wiążące, a nie tylko inspirację).

### 2. Typografia

Krój: **Manrope**, wagi 200-800; pomocniczo **Inconsolata** (dane liczbowe, metadane, kody usług). Oba kroje są darmowe i dostępne przez Google Fonts. Źródło skali: `brandbook.dc.html`, sekcja 04.

Hierarchię buduje **waga jednego kroju**, nie zmiana rodziny - to zasada systemu, nie szczegół. Obowiązująca skala:

| Poziom | Krój | Waga | Stopień | Interlinia | Tracking |
|---|---|---|---|---|---|
| Display (okładka) | Manrope | 200 | 72 px | 0,92 | -0,03em |
| H1 - rozdział | Manrope | 300 | 40 px | 1,0 | -0,02em |
| H2 - sekcja | Manrope | 600 | 24 px | 1,1 | -0,01em |
| **H3 - podsekcja** | Manrope | 600 | 16 px | 1,3 | 0 |
| Lead akapitu | Manrope | 500 | 16 px | 1,4 | 0 |
| Korpus | Manrope | 400 | 13,5 px | 1,55 | 0 |
| Przypis, metadane | Manrope | 400 | 10 px | 1,5 | 0 |
| Kicker - drogowskaz sekcji | Manrope | 700 | 14 px | 1,2 | 0,22em, wersaliki |
| Liczba prowadząca | Manrope | 800 | 52 px | 0,95 | -0,02em |
| Dane techniczne, kody usług | Inconsolata | 300-700 | 10,5 px | 1,5 | 0 |

**H3 - zatwierdzony przez foundera (2026-09-02).** Kanwa nie definiowała tego poziomu; H3 to stopień leadu (16 px) z wagą podniesioną do 600. Ruch zgodny z własną logiką systemu - różnicuje wagą, nie wprowadza nowego stopnia do skali. Odróżnia się od leadu wyłącznie wagą, więc H3 i lead nigdy nie powinny stać bezpośrednio obok siebie.

### 3. Treść merytoryczna — z warstwy 1 i 2

Dla każdego zlecenia do Claude Design paczka musi zawierać:
- **odpowiednią kartę specyfikacji z warstwy 2** (`/02-szablony-dokumentow/`) — określa, jakie elementy treści są prawnie obowiązkowe, konwencją organizacyjną i swobodnym wyborem projektowym dla danego typu dokumentu,
- **odpowiednie pliki z warstwy 1** (`/01-baza-wiedzy/`) wskazane przez tę kartę specyfikacji — fakty o firmie, przepisy prawne, wytyczne usługowe potrzebne do wypełnienia treści,
- **rzeczywiste dane wejściowe** dla konkretnego dokumentu (np. konkretne szkolenie, konkretny uczestnik, konkretne dane rejestrowe) — te nie są generowane w tym repozytorium i muszą przyjść od foundera przy każdym zleceniu.

## Czego paczka nie zawiera

Gotowego layoutu, kompozycji, wyboru konkretnych elementów graficznych poza logotypem — to wszystko rozstrzyga się w Claude Design, zgodnie z podziałem warstw z `/CLAUDE.md`.
