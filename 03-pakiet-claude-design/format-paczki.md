# Format paczki wejściowej dla Claude Design

Ten plik definiuje, co powinna zawierać paczka wejściowa przekazywana do Claude Design dla dowolnego dokumentu IRIN. Sama kompozycja, layout i grafika powstają w Claude Design — ten plik tylko określa, jakie materiały i informacje muszą się tam znaleźć, żeby to było możliwe.

## Paleta i siatka — zatwierdzone przez foundera (2026-09-02)

Pełny pomiar, uzasadnienie i historia decyzji: `./propozycja-palety-i-siatki-do-potwierdzenia.md`.

### Siatka dokumentu A4

6 kolumn, moduł 25 mm, gutter 4 mm. Marginesy: 18 mm góra, 18 mm lewy, 22 mm prawy, 28 mm dół. Treść: 170 × 251 mm. Zastępuje wersję z `brandbook.dc.html` (moduł 32 mm), która nie mieściła się fizycznie na stronie A4.

### Paleta — 12 kolorów

Dwa kolory zostały zmienione względem `brandbook.dc.html` po pomiarze kontrastu WCAG — **Miedź** i **Karmin** niżej mają nowy hex, wszystkie pozostałe kolory są bez zmian względem canvasu.

| Kolor | Hex | Rola | Kontrast na Kaszmir |
|---|---|---|---|
| Kaszmir | `#F2ECE1` | papier / tło karty | — |
| Espresso | `#1E1611` | tusz uniwersalny / tekst korpusu | 15,16:1 |
| Złoto foliowe | `#B58540` | pieczęć, sygnatura — nigdy tekst ani tło większej powierzchni | nie dotyczy |
| Aksamit | `#4A1D26` | akcent dziedziny: Pedagogika | 11,95:1 |
| **Miedź** | **`#8C5026`** | akcent dziedziny: Akademia AI | 5,42:1 |
| Onyks | `#1B2B26` | akcent dziedziny: Pożyczki UE/BGK | 12,58:1 |
| Pergamin | `#E4DACB` | drugi neutral (tło) | — |
| Sepia | `#5B4837` | tekst pomocniczy | 7,36:1 |
| **Karmin** | **`#AC151F`** | link, stan aktywny | 6,17:1 |
| Muślin | `#F7F3EA` | tło strony | — |
| Werdykt | `#2F4A32` | stan potwierdzony (tło, z tekstem Kaszmir) | 8,32:1 (tekst) |
| Rubryka | `#D9AC4A` | marker w CMYK (tło, z tekstem Espresso) | 6,38:1 (tekst) |

**Reguła proporcji 80/15/5:** 80% powierzchni dokumentu — Kaszmir/Muślin/Pergamin (tła) i Espresso/Sepia (tekst); 15% — dokładnie jeden kolor dziedziny (Aksamit / Miedź / Onyks) na dokument, nigdy dwa naraz; 5% — Karmin wyłącznie do linków/stanów aktywnych, Werdykt do stanu potwierdzonego, Rubryka jako marker, Złoto foliowe wyłącznie jako pieczęć/sygnatura.

## Elementy paczki, potwierdzone i gotowe do użycia

### 1. Logotyp

Trzy pliki źródłowe w korzeniu repozytorium: `logo_irin_poziom.svg` (podstawowy, proporcja ok. 1,773:1), `logo_irin_pion.svg` (pola wąskie/wysokie, proporcja ok. 1,135:1), `logo_irin_sygnet.svg` (samodzielny znak). Wszystkie trzy są jednokolorowe (czarne na przezroczystym tle) — same w sobie nie definiują żadnej palety barw (patrz `/CLAUDE.md`).

Zasady **potwierdzone jako obowiązujące** (`/PLAN.md`, "Decyzje foundera — rozstrzygnięte"):
- minimalny rozmiar: 18 mm / 90 px,
- przestrzeń ochronna: x = wysokość liter sygnetu (jednostka względna, nie stała miara),
- zakaz zmiany koloru logotypu, zakaz obracania/pochylania/odbijania lustrzanego, zakaz cienia/poświaty/obrysu, zakaz nieproporcjonalnego rozciągania (te ostatnie cztery zasady są obserwacją z `brandbook.dc.html`, spójną z ogólną praktyką ochrony znaku — ale nie były oddzielnie potwierdzone przez foundera jak dwie pierwsze; do potwierdzenia przy pierwszym realnym użyciu, jeśli founder chce je uznać za wiążące, a nie tylko inspirację).

### 2. Typografia

Krój: **Manrope**, wagi 200-800; pomocniczo **Inconsolata** (np. do danych liczbowych, metadanych, kodów usług). Źródło: `brandbook.dc.html` — nie jest na liście rozbieżności wymagających potwierdzenia w `/CLAUDE.md` (w przeciwieństwie do palety i siatki), więc traktowany tu jako przyjęty kierunek, nie tylko inspiracja. Oba kroje są darmowe i dostępne przez Google Fonts.

### 3. Treść merytoryczna — z warstwy 1 i 2

Dla każdego zlecenia do Claude Design paczka musi zawierać:
- **odpowiednią kartę specyfikacji z warstwy 2** (`/02-szablony-dokumentow/`) — określa, jakie elementy treści są prawnie obowiązkowe, konwencją organizacyjną i swobodnym wyborem projektowym dla danego typu dokumentu,
- **odpowiednie pliki z warstwy 1** (`/01-baza-wiedzy/`) wskazane przez tę kartę specyfikacji — fakty o firmie, przepisy prawne, wytyczne usługowe potrzebne do wypełnienia treści,
- **rzeczywiste dane wejściowe** dla konkretnego dokumentu (np. konkretne szkolenie, konkretny uczestnik, konkretne dane rejestrowe) — te nie są generowane w tym repozytorium i muszą przyjść od foundera przy każdym zleceniu.

## Czego paczka nie zawiera

Gotowego layoutu, kompozycji, wyboru konkretnych elementów graficznych poza logotypem — to wszystko rozstrzyga się w Claude Design, zgodnie z podziałem warstw z `/CLAUDE.md`.
