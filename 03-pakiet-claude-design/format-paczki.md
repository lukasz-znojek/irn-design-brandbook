# Format paczki wejściowej dla Claude Design

Ten plik definiuje, co powinna zawierać paczka wejściowa przekazywana do Claude Design dla dowolnego dokumentu IRIN. Sama kompozycja, layout i grafika powstają w Claude Design — ten plik tylko określa, jakie materiały i informacje muszą się tam znaleźć, żeby to było możliwe.

## Status palety i siatki — ważne zastrzeżenie

**Paleta barw i moduły siatki A4 nie są tu jeszcze wpisane jako ostateczna specyfikacja.** Zadanie to jest oznaczone w `/PLAN.md` jako **[FOUNDER]** — kierunek z `brandbook.dc.html` jest zaakceptowany, ale wymaga dopracowania (dokładny pomiar wartości hex, zaplanowanie kombinacji kolorów, poprawienie siatki A4, która w obecnym opisie nie mieści się fizycznie na stronie). Dopracowana propozycja czeka na zatwierdzenie foundera w `./propozycja-palety-i-siatki-do-potwierdzenia.md`. **Dopóki founder jej nie zaakceptuje, paczka wejściowa do Claude Design nie powinna zawierać stałej listy kolorów ani wymiarów siatki jako wiążącej specyfikacji** — Claude Design powinien albo pracować bez zdefiniowanej palety/siatki (tylko z logo i typografią, patrz niżej), albo zapytać foundera wprost, jeśli decyzja jest potrzebna do konkretnego zlecenia.

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
