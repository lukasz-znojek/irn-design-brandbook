# Format paczki wejściowej dla Claude Design

Ten plik definiuje, co powinna zawierać paczka wejściowa przekazywana do Claude Design dla dowolnego dokumentu IRIN. Sama kompozycja, layout i grafika powstają w Claude Design — ten plik tylko określa, jakie materiały i informacje muszą się tam znaleźć, żeby to było możliwe.

## Siatka i paleta - zatwierdzone przez foundera

### Siatka dokumentu A4

6 kolumn, moduł 25 mm, gutter 4 mm. Marginesy: 18 mm góra, 18 mm lewy, 22 mm prawy, 28 mm dół. Treść: 170 × 251 mm. Zastępuje wersję z `brandbook.dc.html` (moduł 32 mm), która nie mieściła się fizycznie na stronie A4. **Bez zmian względem decyzji z 2026-09-02.**

### Paleta barw

**Pełna specyfikacja jest w warstwie 1: [`../01-baza-wiedzy/identyfikacja/paleta-barw.md`](../01-baza-wiedzy/identyfikacja/paleta-barw.md).** Tam są wszystkie 14 kolorów z hexami, tokenami semantycznymi, zmierzonymi kontrastami i przepisanymi kolorami etykiet na wypełnieniach. Dane maszynowe: [`../01-baza-wiedzy/identyfikacja/tokeny/palette-irin.json`](../01-baza-wiedzy/identyfikacja/tokeny/palette-irin.json). Ten plik świadomie jej nie powtarza - jedna paleta ma jedno miejsce, żeby nie dało się rozjechać dwóch kopii.

Trzy zasady, które **muszą** trafić do każdego zlecenia dla Claude Design razem z paletą, bo bez nich sama lista hexów jest niekompletna:

1. **Jeden kolor dziedziny na dokument.** Aksamit (Pedagogika), Miedź (Akademia AI) albo Onyks (Pożyczki UE/BGK) - nigdy dwa naraz. To warstwa 15% reguły 80/15/5.
2. **Kolor etykiety na wypełnieniu nie jest wyborem projektowym.** Na każdym kolorze, który bywa tłem przycisku albo plakietki, kolor napisu jest przepisany w tabeli w warstwie 1. Nie dobieraj go „na oko”.
3. **Kolor nigdy nie jest jedynym nośnikiem statusu.** Każdy stan potrzebuje etykiety słownej albo ikony obok koloru. Po konwersji do skali szarości Werdykt, Rubryka, Karmin i Onyks mają zbliżoną jasność, a osobny tryb monochromatyczny został odrzucony - więc to jest jedyne zabezpieczenie czytelności, nie jedno z dwóch.

Trzymaj się dokładnie wartości z warstwy 1, nie przybliżaj ich.

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
