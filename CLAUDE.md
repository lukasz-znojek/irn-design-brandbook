# CLAUDE.md — kontekst dla pracy w tym repozytorium

## Czym jest IRIN

IRIN (Instytut Rozwoju i Nauki) to polska firma działająca w trzech obszarach: aplikacje dla przedstawicieli handlowych, usługi pozyskiwania pożyczek, oraz dofinansowane szkolenia zawodowe wydające zaświadczenia KFS (Krajowy Fundusz Szkoleniowy) i certyfikaty BUR (Baza Usług Rozwojowych, PARP). Planowany jest też portal sprzedaży szkoleń online.

## Architektura trójwarstwowa

1. **Warstwa 1 — baza wiedzy** (`01-baza-wiedzy/`): kontekst firmy, przepisy prawne, wytyczne usługowe. Punkt wejścia: `01-baza-wiedzy/00-INDEX.md`.
2. **Warstwa 2 — szablony dokumentów** (`02-szablony-dokumentow/`): pliki `.md` jako wytyczne co do treści i wymogów regulacyjnych — nigdy jako układ graficzny.
3. **Warstwa 3 — pakiet i prompt dla Claude Design** (`03-pakiet-claude-design/`): kompozycja, layout i grafika powstają w Claude Design, nie w tym repozytorium.

## Zasady obowiązujące w tym repozytorium

- Każdy commitowany plik jest napisany po polsku: nazwy plików, nagłówki, treść. Wyjątkiem są identyfikatory techniczne wymuszone przez narzędzia.
- Layout, kompozycja i grafika powstają wyłącznie w Claude Design — to repozytorium przechowuje treść i wytyczne merytoryczne, nie projekt graficzny.
- `_robocze/` to poligon roboczy/archiwum — nic stamtąd nie jest źródłem prawdy bez ponownej weryfikacji.
- Każda karta specyfikacji dokumentu w warstwie 2 musi jawnie rozróżniać trzy kategorie: elementy **prawnie obowiązkowe**, **konwencję organizacyjną** IRIN i **swobodny wybór projektowy**.

## Co wynika z plików logotypu (`logo_irin_sygnet.svg`, `logo_irin_pion.svg`, `logo_irin_poziom.svg`)

- Ścieżki graficzne w każdym z trzech plików nie mają zdefiniowanego atrybutu `fill` — a więc renderują się domyślnym czarnym; jedyny jawny `fill="none"` dotyczy przezroczystego prostokąta tła. Wniosek: pliki źródłowe logotypu są jednokolorowe (czarne na przezroczystym tle) i same w sobie nie definiują żadnej palety barw.
- `logo_irin_sygnet.svg` i `logo_irin_pion.svg`: `viewBox="0 0 184.837 162.834"` (proporcja ok. 1.135:1).
- `logo_irin_poziom.svg`: `viewBox="0 0 281.333 158.667"` (proporcja ok. 1.773:1).
- Trzy pliki odpowiadają trzem wariantom logotypu: poziomy (podstawowy), pionowy (pola wąskie/wysokie), sygnet (samodzielny).
- Minimalny rozmiar, przestrzeń ochronna i zakazy modyfikacji **nie wynikają z geometrii SVG** - nie da się ich zmierzyć w tych plikach. Pochodzą z `brandbook.dc.html` i **zostały potwierdzone przez foundera**: minimalny rozmiar i przestrzeń ochronna wcześniej, cztery zakazy modyfikacji 2026-09-02. Obowiązująca specyfikacja: `01-baza-wiedzy/identyfikacja/logotyp.md`.

## Co wynika z `brandbook.dc.html`

To jest **wstępne canvas foundera** — punkt inspiracji i dowód zamierzonego kierunku, nie specyfikacja do odtworzenia. Wyekstrahowane fakty:

- Pełna nazwa firmy w pliku: "Instytut Rozwoju i Nauki". Trzy dziedziny nazwane wprost: Pedagogika, Akademia AI, Pożyczki UE/BGK.
- Krój pisma: **Manrope**, wagi 200–800; pomocniczo Inconsolata.
- Najczęstsze wartości hex w pliku: `#1E1611` (tusz/tekst), `#5B4837`, `#F2ECE1` (papier/tło), `#3A2C1E`, `#4A1D26`, `#D9A75B`, `#B58540`, `#E4DACB`, `#1B2B26`, `#A15C2C`, `#8B2E3A` — plik nazywa tę paletę "Colorbook Kaszmir Aksamit" i opisuje regułę proporcji 80/15/5 (baza / akcent dziedzinowy / akcja).
- Siatka dokumentu A4 w pliku: 6 kolumn, moduł 32 mm, gutter 4 mm, jednostka bazowa 6 mm.
- Przestrzeń ochronna logotypu opisana jako "x = wysokość liter sygnetu" — jednostka względna, nie stała miara. Minimalna szerokość podana w pliku: 18 mm / 90 px.
- Przykładowe zastosowania pokazane w pliku: okładka viewbooka, karta usługi BUR, dwie wersje certyfikatu (kolumnowa, pieczęć), papier firmowy, wizytówka.
- **Rozbieżność do potwierdzenia z founderem**: 12-barwna paleta i moduły siatki w pliku to jego robocza propozycja, a nie coś zmierzonego z geometrii logotypu — każda z tych wartości musi zostać przez niego świadomie zatwierdzona, zanim stanie się obowiązującą specyfikacją w `01-baza-wiedzy/`.

## Paleta barw - stan obowiązujący

Wartości hex wypisane wyżej opisują **plik `brandbook.dc.html`**, a nie obowiązującą paletę - to zapis tego, co jest w kanwie foundera, i pozostaje prawdziwy jako opis tego pliku.

Obowiązująca paleta to **14 kolorów, wariant 2 „Kaszmir Wyciszony”**, wybrany przez foundera spośród siedmiu wariantów. Jedyne źródło prawdy: `01-baza-wiedzy/identyfikacja/paleta-barw.md`. Tam też, od 2026-09-02, siatka A4 (`siatka-a4.md`), typografia (`typografia.md`) i logotyp (`logotyp.md`) - `03-pakiet-claude-design/format-paczki.md` już żadnej z tych czterech nie powtarza, tylko odsyła i dokłada zasady ich użycia w zleceniu. Dane maszynowe: `01-baza-wiedzy/identyfikacja/tokeny/palette-irin.json`. Porównanie siedmiu wariantów i uzasadnienie wyboru (archiwum): `_robocze/paleta-v2/palette-options-v2.md`. Historia pierwszej decyzji: `03-pakiet-claude-design/propozycja-palety-i-siatki-do-potwierdzenia.md`.

Rozbieżność opisana w punkcie wyżej jest **rozstrzygnięta**: paleta i siatka przeszły pomiar i świadomą decyzję foundera. Zapis zostaje jako historia, nie jako otwarta sprawa.

Dwie zasady, które muszą przetrwać każdą przyszłą zmianę palety: kontrast liczy się na nowo wzorem WCAG 2.1, nigdy nie kopiuje się starych liczb; kolor nigdy nie jest jedynym nośnikiem statusu - każdy stan potrzebuje etykiety słownej albo ikony obok koloru.
