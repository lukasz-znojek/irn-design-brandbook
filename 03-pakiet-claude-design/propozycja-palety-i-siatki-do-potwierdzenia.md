# DO POTWIERDZENIA — propozycja dopracowanej palety i siatki A4

**Status: projekt do zatwierdzenia przez foundera. Nic w tym pliku nie jest wiążącą specyfikacją, dopóki founder świadomie tego nie zaakceptuje — patrz zadanie 13 w `/PLAN.md` i sekcja o `brandbook.dc.html` w `/CLAUDE.md`.** Dopóki status się nie zmieni, `./format-paczki.md` nie traktuje niczego z tego pliku jako ostatecznej specyfikacji.

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
| **Miedź** | `#A15C2C` | akcent dziedziny: Akademia AI | **4,37:1** na Kaszmir | 3,7:1 "AA large" | **Nie spełnia AA dla tekstu normalnego (4,5:1).** Spełnia AA large (3:1) i AAA large (4,5:1) — na granicy. |
| Sepia | `#5B4837` | tekst pomocniczy | **7,36:1** na Kaszmir; 6,26:1 na Pergaminie | nie podano | AAA na Kaszmir ✓, AA (nie AAA) na Pergaminie |
| Karmin | `#8B2E3A` | link, stan aktywny | **7,01:1** na Kaszmir | nie podano | AAA (7:1) ✓ — na granicy |
| Pergamin | `#E4DACB` | drugi neutral (tło) | — | — | — |
| Werdykt | `#2F4A32` | stan potwierdzony (tło) | tekst Kaszmir na Werdykt: **8,32:1** | nie podano | AAA ✓ |
| Rubryka | `#D9AC4A` | marker CMYK (tło) | tekst Espresso na Rubryka: **6,38:1** | nie podano | AA (4,5:1) ✓, nie AAA |
| Złoto foliowe | `#B58540` | pieczęć, sygnatura (folia, nie tekst) | nie dotyczy — nigdy nie niesie tekstu | nie podano | nie dotyczy |

**Metodologia:** kontrast liczony wg standardowego wzoru WCAG 2.1 (luminancja względna sRGB), skryptem uruchomionym w tej sesji — nie przepisany z kanwy. Rozbieżności między liczbą zmierzoną a liczbą w kanwie (Aksamit, Onyks) nie zmieniają wniosku (obie i tak przechodzą AAA), ale pokazują, że liczby w kanwie są przybliżeniem, nie precyzyjnym pomiarem — stąd zalecenie, żeby przy każdej przyszłej zmianie palety przeliczać kontrast na nowo, nie kopiować starych liczb.

### Dwa realne problemy do decyzji foundera

1. **Miedź (`#A15C2C`, Akademia AI) nie nadaje się na kolor tekstu korpusu** — 4,37:1 nie spełnia progu AA dla normalnego tekstu (4,5:1), tylko dla tekstu dużego/pogrubionego i elementów graficznych. W kanwie Miedź bywa użyta jako kolor liczby ("648 zł" po dofinansowaniu, `brandbook.dc.html:344`) — przy dużym rozmiarze fontu (20 px) to mieści się w normie AA large, ale nie należy tym kolorem pisać zwykłego tekstu akapitowego. **Do decyzji: zaakceptować to ograniczenie użycia (Miedź tylko do dużych elementów), czy pogłębić odcień, żeby Miedź spełniała 4,5:1 też dla tekstu normalnego?**
2. **Karmin (`#8B2E3A`, link/stan) i Aksamit (`#4A1D26`, domena Pedagogika) są wizualnie zbliżone** — oba to ciemne bordo, wzajemny kontrast między nimi to tylko 1,71:1. Na dokumencie z dziedziny Pedagogika (gdzie Aksamit jest kolorem sygnującym dziedzinę) użycie Karminu na linku obok elementu w Aksamicie może się zlewać wizualnie i zacierać rozróżnienie "to jest link/stan" od "to jest kolor dziedziny". **Do decyzji: zaakceptować to ryzyko (dokumenty rzadko łączą oba kolory blisko siebie), czy zmienić odcień jednego z nich?**

## Siatka A4 — błąd w wymiarach, dwie poprawki do wyboru

**Zmierzony problem:** kanwa opisuje siatkę jako "6 kolumn, moduł 32 mm, gutter 4 mm" na stronie A4 (210 × 297 mm), z marginesami 18 mm góra/lewo, 22 mm prawo, 28 mm dół. Zsumowane 6 kolumn × 32 mm + 5 gutterów × 4 mm = **212 mm**. Sama szerokość strony A4 to 210 mm — więc **siatka nie mieści się na stronie nawet przy zerowych marginesach** (212 mm > 210 mm), a przy podanych marginesach dostępna szerokość treści to tylko 170 mm (210 − 18 − 22). Różnica wynosi 42 mm. To nie jest kwestia gustu — to jest niemożliwe geometrycznie, niezależnie od tego, jak founder ustawi marginesy. Falsyfikator tego wniosku: inny format strony niż A4 pion (np. A3, albo A4 poziom) — kanwa jednak wprost mówi "Siatka dokumentu A4" bez dopisku o orientacji poziomej.

Dwie poprawki, które faktycznie mieszczą się na A4 pion przy zachowanych marginesach 18/18/22/28 mm (170 mm szerokości treści):

**Opcja 1 — zachować 6 kolumn, zmniejszyć moduł.** Moduł 25 mm, gutter 4 mm: 6 × 25 + 5 × 4 = 150 + 20 = **170 mm — dokładne dopasowanie**. Zachowuje "sześć kolumn" jako część tożsamości systemu (kanwa: "Siatka jest wspólna dla wszystkich trzech dziedzin"), zmienia tylko wymiar modułu z 32 na 25 mm.

**Opcja 2 — zachować moduł 32 mm, zmniejszyć liczbę kolumn i skorygować prawy margines.** 5 kolumn, gutter 4 mm: 5 × 32 + 4 × 4 = 160 + 16 = **176 mm**. Przy tej szerokości treści prawy margines musiałby się zmniejszyć z 22 mm do 16 mm (210 − 18 − 176 = 16). Zachowuje moduł 32 mm z kanwy, zmienia liczbę kolumn (6 → 5) i jeden margines.

**Rekomendacja: Opcja 1.** Liczba kolumn (sześć) jest w kanwie opisana jako element wspólny dla wszystkich trzech dziedzin — bardziej prawdopodobne, że to ona jest zamierzoną stałą systemu, a moduł 32 mm był tylko niesprawdzonym pomiarem. Ale to jest rekomendacja do obalenia przez foundera, nie decyzja — może chcieć odwrotnie.

## Reguła 80/15/5 — doprecyzowanie

Kanwa opisuje regułę opisowo (`brandbook.dc.html:213-215`); tu doprecyzowanie, które kolory wchodzą do której warstwy, żeby dało się to sprawdzić na gotowym dokumencie:

- **80% — baza:** Kaszmir (tło karty), Muślin (tło strony), Espresso (tekst korpusu), Pergamin (drugie tło neutralne), Sepia (tekst pomocniczy). Wszystko, co nie niesie znaczenia kategoryzującego.
- **15% — sygnał dziedziny:** dokładnie jeden z trzech — Aksamit (Pedagogika), Miedź (Akademia AI, z zastrzeżeniem o kontraście wyżej), Onyks (Pożyczki UE/BGK) — na dokument. Nie mieszać dwóch kolorów dziedzinowych na jednej stronie.
- **5% — aktywność i honor:** Karmin wyłącznie dla linków/stanów aktywnych (z zastrzeżeniem o zbliżeniu do Aksamitu wyżej), Werdykt dla stanu potwierdzonego, Rubryka jako marker. Złoto foliowe **wyłącznie** jako pieczęć/sygnatura — nigdy jako kolor tekstu czy tła większej powierzchni.

## Co dokładnie ma zatwierdzić founder

1. Nazwy i przypisania 12 kolorów jako oficjalne nazewnictwo marki IRIN (Kaszmir, Espresso, Złoto foliowe, Aksamit, Miedź, Onyks, Pergamin, Sepia, Karmin, Muślin, Werdykt, Rubryka) — czy zostają, czy founder chce inne nazwy/przypisania dziedzin.
2. Ograniczenie użycia Miedzi do dużych elementów (nie tekstu korpusu) — akceptacja albo zlecenie pogłębienia odcienia.
3. Ryzyko zbliżenia Karmin/Aksamit — akceptacja albo zmiana odcienia.
4. Wybór między Opcją 1 (moduł 25 mm) a Opcją 2 (5 kolumn, margines 16 mm) dla siatki A4 — albo trzecia opcja własna foundera.

Dopiero po tej decyzji odpowiednia treść trafia do `./format-paczki.md` jako obowiązująca specyfikacja.
