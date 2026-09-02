# Propozycja dopracowanej palety i siatki A4

> **Aktualizacja 2026-09-02 (późniejsza tego samego dnia): paleta z tego dokumentu została wstrzymana i zastąpiona.**
> Founder wstrzymał automatyczne przyjęcie palety opisanej niżej, uznając, że wymaga dopracowania. Powstało siedem wariantów do wyboru (`../02-branding/kolorystyka/palette-options-v2.md`), z których **wybrany został wariant 2 „Kaszmir Wyciszony”** - i to on jest teraz obowiązującą specyfikacją w `./format-paczki.md`.
> Ten dokument **zostaje w całości i bez zmian** jako zapis pierwszej decyzji: pomiaru siatki A4, wykrytego błędu wymiarów, pogłębienia Miedzi i zmiany Karminu. Siatka A4 uzgodniona tutaj (6 kolumn, moduł 25 mm) **obowiązuje nadal** - wstrzymanie dotyczyło wyłącznie palety barw.
> Czego wariant 2 nie unieważnia: metodologii pomiaru, wniosku o błędzie wymiarów siatki, ani zasady, że przy każdej zmianie palety kontrast liczy się na nowo, a nie kopiuje starych liczb.

**Status: ZATWIERDZONE w całości przez foundera (2026-09-02)** — siatka A4 (Opcja 1) i paleta barw (Miedź pogłębiona, Karmin zmieniony na wyrazistą karmazynową czerwień). Obie specyfikacje są już wpisane jako obowiązujące w `./format-paczki.md`. Ten plik zostaje jako zapis pomiaru i uzasadnienia decyzji — nie jest już "do potwierdzenia".

## Punkt wyjścia

`brandbook.dc.html` (canvas foundera) zawiera już rozbudowany system o nazwie "Colorbook Kaszmir Aksamit dopracowany": 12 nazwanych kolorów pogrupowanych w bazę (3), akcenty dziedzinowe (3) i funkcjonalne (6), regułę proporcji 80/15/5 i siatkę A4 (6 kolumn / moduł 32 mm / gutter 4 mm). Ten dokument **nie przepisuje** tej listy — sprawdza ją: mierzy kontrast kolorów wg wzoru WCAG 2.1 (a nie wg liczb wpisanych ręcznie w kanwie) i sprawdza, czy siatka fizycznie mieści się na stronie A4. Tam, gdzie pomiar potwierdza kanwę — mówi to wprost. Tam, gdzie pomiar wykrywa rozbieżność, opisuje ją i proponuje poprawkę do wyboru przez foundera.

## Paleta — zmierzone kontrasty (WCAG 2.1, wzór na luminancję względną)

| Kolor | Hex | Rola (wg kanwy) | Kontrast zmierzony | Kontrast wg kanwy | Próg WCAG |
|---|---|---|---|---|---|
| Kaszmir | `#F2ECE1` | papier / tło karty | — (kolor bazowy, tło) | — | — |
| Espresso | `#1E1611` | tusz uniwersalny (tekst korpusu) | **15,16:1** na Kaszmir | nie podano | AAA (7:1) ✓ z dużym zapasem |
| Muślin | `#F7F3EA` | tło strony | Espresso na Muślin: **16,10:1** | nie podano | AAA ✓ |
| Aksamit | `#4A1D26` | akcent dziedziny: Pedagogika | **11,95:1** na Kaszmir | 10,4:1 AAA | AAA (7:1) ✓ — liczba w kanwie zaniżona, wniosek ten sam |
| Onyks | `#1B2B26` | akcent dziedziny: Pożyczki UE/BGK | **12,58:1** na Kaszmir | 13,4:1 AAA | AAA (7:1) ✓ — liczba w kanwie zawyżona, wniosek ten sam |
| **Miedź** (nowa) | `#8C5026` | akcent dziedziny: Akademia AI | **5,42:1** na Kaszmir | — | AA (4,5:1) ✓ — po pogłębieniu, patrz niżej |
| Sepia | `#5B4837` | tekst pomocniczy | **7,36:1** na Kaszmir; 6,26:1 na Pergaminie | nie podano | AAA na Kaszmir ✓, AA (nie AAA) na Pergaminie |
| **Karmin** (nowy) | `#AC151F` | link, stan aktywny | **6,17:1** na Kaszmir | — | AAA (7:1) blisko ✓ — po zmianie odcienia, patrz niżej |
| Pergamin | `#E4DACB` | drugi neutral (tło) | — | — | — |
| Werdykt | `#2F4A32` | stan potwierdzony (tło) | tekst Kaszmir na Werdykt: **8,32:1** | nie podano | AAA ✓ |
| Rubryka | `#D9AC4A` | marker CMYK (tło) | tekst Espresso na Rubryka: **6,38:1** | nie podano | AA (4,5:1) ✓, nie AAA |
| Złoto foliowe | `#B58540` | pieczęć, sygnatura (folia, nie tekst) | nie dotyczy — nigdy nie niesie tekstu | nie podano | nie dotyczy |

**Metodologia:** kontrast liczony wg standardowego wzoru WCAG 2.1 (luminancja względna sRGB), skryptem uruchomionym w tej sesji — nie przepisany z kanwy. Rozbieżności między liczbą zmierzoną a liczbą w kanwie (Aksamit, Onyks) nie zmieniają wniosku (obie i tak przechodzą AAA), ale pokazują, że liczby w kanwie są przybliżeniem, nie precyzyjnym pomiarem — stąd zalecenie, żeby przy każdej przyszłej zmianie palety przeliczać kontrast na nowo, nie kopiować starych liczb.

### Dwa problemy — ROZWIĄZANE decyzją foundera (2026-09-02)

**1. Miedź pogłębiona.** Founder wybrał pogłębienie odcienia zamiast ograniczenia użycia. Metoda: ten sam odcień/nasycenie (H 24,6° / S 57%), jasność obniżona z 40% do 35%.

| | Hex | Kontrast na Kaszmir | Kontrast na Pergaminie |
|---|---|---|---|
| Miedź — stara | `#A15C2C` | 4,37:1 (nie AA tekst) | — |
| **Miedź — nowa** | **`#8C5026`** | **5,42:1 (AA, blisko AAA large)** | **4,61:1 (AA)** |

Miedź w nowym odcieniu można używać jako kolor tekstu normalnego, nie tylko dużych elementów — ograniczenie z propozycji roboczej już nie obowiązuje.

**2. Karmin zmieniony na wyrazistą karmazynową czerwień.** Founder wybrał zmianę odcienia zamiast akceptacji ryzyka. Stary Karmin (`#8B2E3A`) i Aksamit (`#4A1D26`) leżały niemal w tym samym wąskim paśmie barwy (348°–352° w skali HSL) — różniły je głównie jasność i nasycenie, nie barwa, stąd wizualne zlewanie się. Poprawka: przesunięcie w stronę czystszej, bardziej nasyconej czerwieni (karmazyn) i podniesienie nasycenia z 50% do 78% — Karmin ma teraz czytelnie inny charakter (żywa czerwień) niż Aksamit (przyciemnione, stonowane bordo), nie tylko inny numer barwy.

| | Hex | HSL | Kontrast na Kaszmir | Kontrast na Pergaminie |
|---|---|---|---|---|
| Karmin — stary | `#8B2E3A` | 352° / 50% / 36% | 7,01:1 (AAA, na granicy) | nie liczono |
| **Karmin — nowy** | **`#AC151F`** | **356° / 78% / 38%** | **6,17:1 (AAA)** | **5,25:1 (AA)** |
| Aksamit (bez zmian, dla porównania) | `#4A1D26` | 348° / 44% / 20% | 11,95:1 | — |

**Zastrzeżenie metodologiczne:** wzajemny kontrast WCAG między nowym Karminem a Aksamitem (miara luminancji, nie barwy) pozostaje niski — WCAG mierzy jasność, nie odróżnialność barwy. Rzeczywista poprawa czytelności różnicy bierze się stąd, że nowy Karmin jest wyraźnie bardziej nasycony (żywa czerwień) niż stonowany, przyciemniony Aksamit — to różnica odczytywana okiem, nie liczbą kontrastu. Jeśli po zobaczeniu obu kolorów obok siebie na realnym dokumencie różnica nadal wyda się za mała, wróć do tego punktu.

## Siatka A4 — ZATWIERDZONA (Opcja 1)

**Founder wybrał Opcję 1, zgodnie z rekomendacją niżej.** Obowiązująca siatka A4: 6 kolumn, moduł 25 mm, gutter 4 mm, marginesy 18 mm góra / 18 mm lewy / 22 mm prawy / 28 mm dół — treść 170 × 251 mm. Wpisana jako obowiązująca specyfikacja w `./format-paczki.md`. Historia decyzji i uzasadnienie pomiaru — niżej, bez zmian.

### Błąd w wymiarach, który doprowadził do tej decyzji

**Zmierzony problem:** kanwa opisuje siatkę jako "6 kolumn, moduł 32 mm, gutter 4 mm" na stronie A4 (210 × 297 mm), z marginesami 18 mm góra/lewo, 22 mm prawo, 28 mm dół. Zsumowane 6 kolumn × 32 mm + 5 gutterów × 4 mm = **212 mm**. Sama szerokość strony A4 to 210 mm — więc **siatka nie mieści się na stronie nawet przy zerowych marginesach** (212 mm > 210 mm), a przy podanych marginesach dostępna szerokość treści to tylko 170 mm (210 − 18 − 22). Różnica wynosi 42 mm. To nie jest kwestia gustu — to jest niemożliwe geometrycznie, niezależnie od tego, jak founder ustawi marginesy. Falsyfikator tego wniosku: inny format strony niż A4 pion (np. A3, albo A4 poziom) — kanwa jednak wprost mówi "Siatka dokumentu A4" bez dopisku o orientacji poziomej.

Dwie poprawki, które faktycznie mieszczą się na A4 pion przy zachowanych marginesach 18/18/22/28 mm (170 mm szerokości treści):

**Opcja 1 — zachować 6 kolumn, zmniejszyć moduł.** Moduł 25 mm, gutter 4 mm: 6 × 25 + 5 × 4 = 150 + 20 = **170 mm — dokładne dopasowanie**. Zachowuje "sześć kolumn" jako część tożsamości systemu (kanwa: "Siatka jest wspólna dla wszystkich trzech dziedzin"), zmienia tylko wymiar modułu z 32 na 25 mm.

**Opcja 2 — zachować moduł 32 mm, zmniejszyć liczbę kolumn i skorygować prawy margines.** 5 kolumn, gutter 4 mm: 5 × 32 + 4 × 4 = 160 + 16 = **176 mm**. Przy tej szerokości treści prawy margines musiałby się zmniejszyć z 22 mm do 16 mm (210 − 18 − 176 = 16). Zachowuje moduł 32 mm z kanwy, zmienia liczbę kolumn (6 → 5) i jeden margines.

**Rekomendacja: Opcja 1 — wybrana przez foundera.** Liczba kolumn (sześć) jest w kanwie opisana jako element wspólny dla wszystkich trzech dziedzin — bardziej prawdopodobne, że to ona jest zamierzoną stałą systemu, a moduł 32 mm był tylko niesprawdzonym pomiarem.

## Reguła 80/15/5 — doprecyzowanie

Kanwa opisuje regułę opisowo (`brandbook.dc.html:213-215`); tu doprecyzowanie, które kolory wchodzą do której warstwy, żeby dało się to sprawdzić na gotowym dokumencie:

- **80% — baza:** Kaszmir (tło karty), Muślin (tło strony), Espresso (tekst korpusu), Pergamin (drugie tło neutralne), Sepia (tekst pomocniczy). Wszystko, co nie niesie znaczenia kategoryzującego.
- **15% — sygnał dziedziny:** dokładnie jeden z trzech — Aksamit (Pedagogika), Miedź `#8C5026` (Akademia AI), Onyks (Pożyczki UE/BGK) — na dokument. Nie mieszać dwóch kolorów dziedzinowych na jednej stronie.
- **5% — aktywność i honor:** Karmin `#AC151F` wyłącznie dla linków/stanów aktywnych, Werdykt dla stanu potwierdzonego, Rubryka jako marker. Złoto foliowe **wyłącznie** jako pieczęć/sygnatura — nigdy jako kolor tekstu czy tła większej powierzchni.

## Decyzje foundera (2026-09-02) — wszystkie cztery punkty rozstrzygnięte

1. **Nazwy i przypisania 12 kolorów** — przyjęte: founder edytował konkretne kolory pod tymi nazwami (Miedź, Karmin), nie zgłaszając zastrzeżeń do samego nazewnictwa ani przypisań dziedzinowych — traktowane jako akceptacja dorozumiana. Jeśli to złe odczytanie, popraw tutaj.
2. **Miedź** — pogłębiona do `#8C5026` (zamiast ograniczenia użycia).
3. **Karmin** — zmieniony na `#AC151F` (zamiast akceptacji ryzyka zbliżenia z Aksamitem).
4. **Siatka A4** — Opcja 1 (6 kolumn, moduł 25 mm).

Cała specyfikacja (paleta + siatka) jest teraz wpisana jako obowiązująca w `./format-paczki.md`.
