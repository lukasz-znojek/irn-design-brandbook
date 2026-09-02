# Podgląd wariantów palety v2 - jeden układ, siedem kolorystyk

**Status: propozycja do wyboru przez foundera. Żaden wariant nie jest finalny; obowiązująca paleta w `03-pakiet-claude-design/format-paczki.md` pozostaje bez zmian do decyzji.**

Ten plik jest generowany skryptem `narzedzia/generuj-podglad-i-kontrast.py` z `tokens/palette-options-v2.json`. Pełna specyfikacja, kontrasty i trade-offs: [`palette-options-v2.md`](./palette-options-v2.md).

## Jak obejrzeć podgląd z prawdziwą typografią

Właściwy podgląd wizualny to plik [`palette-preview-v2.html`](./palette-preview-v2.html): jeden dokument, siedem sekcji o identycznym układzie, różniących się wyłącznie tokenami koloru. Krój Manrope (wagi 200-800) i Inconsolata są ładowane z Google Fonts tym samym adresem, którego używa `brandbook.dc.html`, więc do poprawnego renderu potrzebne jest połączenie z internetem. GitHub nie renderuje plików HTML w podglądzie repozytorium - pobierz gałąź i otwórz plik lokalnie w przeglądarce (logotyp wczytuje się z korzenia repozytorium ścieżką względną).

Paski próbek poniżej (SVG) renderują się bezpośrednio na GitHubie i pokazują same kolory; etykiety na nich nie są demonstracją typografii.

## Wspólny układ demonstracyjny

Każdy wariant pokazuje tę samą sekwencję komponentów, przepisanych z `brandbook.dc.html` (§ 00 okładka, § 04 skala typograficzna, tabele i drogowskazy z § 02-§ 06):

1. strona tytułowa (pas górny z logotypem, pasy akcentu, tytuł display, lead, mapowanie dziedzin),
2. hierarchia nagłówków H1 / H2 / H3,
3. akapit korpusu z przypisem,
4. box informacyjny,
5. tabela z etykietami stanu,
6. przyciski CTA (podstawowy, drugi, akcentowy),
7. link w tekście i liczby prowadzące,
8. sekcja „prawo / compliance” z listą elementów obowiązkowych zaświadczenia (treść z `02-szablony-dokumentow/certyfikat.md`) i boxem ostrzegawczym.

Typografia jest identyczna we wszystkich siedmiu sekcjach i nie była przedmiotem zmian - tabela poniżej podaje ją raz, a przy każdym wariancie zmienia się tylko kolumna z kolorem.

| Element układu | Token koloru | Typografia (bez zmian, z brandbook.dc.html) |
|---|---|---|
| Strona tytułowa - pas górny | neutral-dark (tło), neutral-light (tekst), accent (linia i pasy) | Manrope 700 · 10,5 px · wersaliki · tracking 0,26 em |
| Strona tytułowa - tytuł display | primary | Manrope 200 · 72 px · interlinia 0,92 · tracking -0,03 em |
| Strona tytułowa - lead | text-secondary | Manrope 500 · 16 px · interlinia 1,4 |
| Nagłówek H1 | primary | Manrope 300 · 40 px · interlinia 1,0 · tracking -0,02 em |
| Nagłówek H2 | secondary | Manrope 600 · 24 px · interlinia 1,1 · tracking -0,01 em |
| Nagłówek H3 (drogowskaz) | accent | Manrope 700 · 9,5 px · wersaliki · tracking 0,2 em |
| Akapit korpusu | text-primary na surface | Manrope 400 · 13,5 px · interlinia 1,55 |
| Przypis / metadane | text-secondary; kody w Inconsolata | Manrope 400 · 10 px · interlinia 1,5 |
| Box informacyjny | border (ramka), info (lewa krawędź 3 px i tytuł), background (tło) | tytuł: drogowskaz 700; treść: Manrope 400 · 12,5 px |
| Tabela - nagłówki kolumn | secondary; linia dolna neutral-dark | Manrope 700 · 9,5 px · wersaliki · tracking 0,2 em |
| Tabela - wiersze | text-primary; linie border; wiersze parzyste neutral-light; liczby w Inconsolata 600 | Manrope 400 · 13 px |
| Tabela - etykiety stanu | success / warning / error / info (tło) z tekstem o najwyższym kontraście | Manrope 700 · 8,5 px · wersaliki · tracking 0,14 em |
| CTA podstawowe | primary (tło), background (tekst) | Manrope 700 · 11 px · wersaliki · tracking 0,16 em |
| CTA drugie | primary (obrys i tekst), bez tła | jak wyżej |
| CTA akcentowe | accent (tło), tekst background albo neutral-dark - wybór wg kontrastu | jak wyżej |
| Link w tekście | link; po najechaniu primary; podkreślenie z odsunięciem 2 px | dziedziczy z akapitu |
| Liczba prowadząca | accent / primary | Manrope 800 · 52 px · tabular · tracking -0,02 em |
| Sekcja prawo / compliance | neutral-dark (linia górna), etykiety stanu, box ostrzegawczy z krawędzią warning | H2 600 · 24 px; lista 400 · 12,5 px; podstawa prawna Inconsolata 10 px |

## Wariant 1 - Kaszmir Aksamit (obecna, uporządkowana)

![Wariant 1 - pasek 15 tokenów](./podglad/paleta-wariant-1.svg)

Obecna zatwierdzona paleta 12 barw przepisana na 15 tokenów, bez zmiany żadnej zatwierdzonej wartości - punkt odniesienia dla pozostałych sześciu. Jedyny dodatek to token info, którego obecna paleta nie miała.

Sekcja w podglądzie HTML: `palette-preview-v2.html#wariant-1`.

| Element układu | Kolor w tym wariancie |
|---|---|
| Strona tytułowa: pas górny / tekst pasa / pasy akcentu | `#1E1611` / `#E4DACB` / `#8C5026` |
| Tytuł display i H1 | `#4A1D26` |
| Lead i przypisy (text-secondary) | `#5B4837` |
| H2 i nagłówki kolumn tabeli (secondary) | `#1B2B26` |
| H3 drogowskaz, liczba prowadząca, CTA akcentowe (accent) | `#8C5026` (tekst CTA: `#F7F3EA`) |
| Akapit (text-primary) na karcie (surface) na tle strony (background) | `#1E1611` na `#F2ECE1` na `#F7F3EA` |
| Box informacyjny: krawędź i tytuł (info), ramka (border) | `#2E4F4A`, `#C3BDB3` |
| Tabela: linie (border), wiersze parzyste (neutral-light) | `#C3BDB3`, `#E4DACB` |
| Etykiety stanu: success / warning / error / info | `#2F4A32` / `#D9AC4A` (tekst `#1E1611`) / `#AC151F` / `#2E4F4A` |
| CTA podstawowe: tło / tekst | `#4A1D26` / `#F7F3EA` |
| Link (po najechaniu: primary) | `#AC151F` |

Mapowanie dziedzin (propozycja, poza 15 tokenami): Pedagogika - primary (Aksamit); Akademia AI - accent (Miedź); Pożyczki UE/BGK - secondary (Onyks).

## Wariant 2 - Atrament i Papier (granat instytucjonalny na ciepłym papierze)

![Wariant 2 - pasek 15 tokenów](./podglad/paleta-wariant-2.svg)

Zachowuje ciepły papier i edytorski charakter obecnego kierunku, ale główny kolor przesuwa z bordo na głęboki granat atramentu - ton instytutu i doradcy finansowego, czytelny w kopii czarno-białej. Brąz zamiast złota utrzymuje wątek pieczęci bez efektu folii.

Sekcja w podglądzie HTML: `palette-preview-v2.html#wariant-2`.

| Element układu | Kolor w tym wariancie |
|---|---|
| Strona tytułowa: pas górny / tekst pasa / pasy akcentu | `#141A26` / `#E5E0D5` / `#875512` |
| Tytuł display i H1 | `#1F2D4F` |
| Lead i przypisy (text-secondary) | `#56544F` |
| H2 i nagłówki kolumn tabeli (secondary) | `#7A5A36` |
| H3 drogowskaz, liczba prowadząca, CTA akcentowe (accent) | `#875512` (tekst CTA: `#F8F5EE`) |
| Akapit (text-primary) na karcie (surface) na tle strony (background) | `#141A26` na `#F2EEE4` na `#F8F5EE` |
| Box informacyjny: krawędź i tytuł (info), ramka (border) | `#2B5F8E`, `#C9C2B4` |
| Tabela: linie (border), wiersze parzyste (neutral-light) | `#C9C2B4`, `#E5E0D5` |
| Etykiety stanu: success / warning / error / info | `#2E6B4F` / `#C98F1B` (tekst `#141A26`) / `#B0322E` / `#2B5F8E` |
| CTA podstawowe: tło / tekst | `#1F2D4F` / `#F8F5EE` |
| Link (po najechaniu: primary) | `#1F5AA6` |

Mapowanie dziedzin (propozycja, poza 15 tokenami): Pedagogika - secondary (brąz umbra); Akademia AI - info (błękit stalowy); Pożyczki UE/BGK - primary (granat).

## Wariant 3 - Zieleń Instytutu (leśna zieleń i mosiądz)

![Wariant 3 - pasek 15 tokenów](./podglad/paleta-wariant-3.svg)

Głęboka zieleń jako kolor rozwoju i stabilności finansowej, mosiądz jako ciepły akcent honorowy; neutrale lekko zszarzałe, żeby zieleń nie wpadała w ton ekologiczny. Kierunek najbardziej odległy od czerwieni, więc najbezpieczniejszy dla osób z deuteranopią w połączeniu z czerwienią błędu.

Sekcja w podglądzie HTML: `palette-preview-v2.html#wariant-3`.

| Element układu | Kolor w tym wariancie |
|---|---|
| Strona tytułowa: pas górny / tekst pasa / pasy akcentu | `#16201A` / `#E2E5DB` / `#8F5C16` |
| Tytuł display i H1 | `#1F3D2E` |
| Lead i przypisy (text-secondary) | `#4F5A52` |
| H2 i nagłówki kolumn tabeli (secondary) | `#5A6B54` |
| H3 drogowskaz, liczba prowadząca, CTA akcentowe (accent) | `#8F5C16` (tekst CTA: `#F6F5EF`) |
| Akapit (text-primary) na karcie (surface) na tle strony (background) | `#16201A` na `#EFEFE6` na `#F6F5EF` |
| Box informacyjny: krawędź i tytuł (info), ramka (border) | `#2C6B85`, `#C6CBBE` |
| Tabela: linie (border), wiersze parzyste (neutral-light) | `#C6CBBE`, `#E2E5DB` |
| Etykiety stanu: success / warning / error / info | `#2F7A4E` / `#D19B2C` (tekst `#16201A`) / `#A9302C` / `#2C6B85` |
| CTA podstawowe: tło / tekst | `#1F3D2E` / `#F6F5EF` |
| Link (po najechaniu: primary) | `#8A5814` |

Mapowanie dziedzin (propozycja, poza 15 tokenami): Pedagogika - accent (mosiądz); Akademia AI - info (morski); Pożyczki UE/BGK - primary (leśna zieleń).

## Wariant 4 - Grafit techniczny (chłodne neutrale, jeden ciepły akcent)

![Wariant 4 - pasek 15 tokenów](./podglad/paleta-wariant-4.svg)

Chłodny grafit i biel zamiast papieru - ton produktu cyfrowego, dopasowany do Akademii AI, aplikacji handlowej i przyszłego portalu; jeden palony akcent pomarańczowy ociepla całość. Świadomie najbardziej korporacyjny wariant zestawu.

Sekcja w podglądzie HTML: `palette-preview-v2.html#wariant-4`.

| Element układu | Kolor w tym wariancie |
|---|---|
| Strona tytułowa: pas górny / tekst pasa / pasy akcentu | `#15181C` / `#E6E8EB` / `#B84A0B` |
| Tytuł display i H1 | `#22272E` |
| Lead i przypisy (text-secondary) | `#4B5563` |
| H2 i nagłówki kolumn tabeli (secondary) | `#4A5563` |
| H3 drogowskaz, liczba prowadząca, CTA akcentowe (accent) | `#B84A0B` (tekst CTA: `#F7F8FA`) |
| Akapit (text-primary) na karcie (surface) na tle strony (background) | `#15181C` na `#FFFFFF` na `#F7F8FA` |
| Box informacyjny: krawędź i tytuł (info), ramka (border) | `#175CD3`, `#D0D5DB` |
| Tabela: linie (border), wiersze parzyste (neutral-light) | `#D0D5DB`, `#E6E8EB` |
| Etykiety stanu: success / warning / error / info | `#1E7B4B` / `#B7791F` (tekst `#15181C`) / `#B42318` / `#175CD3` |
| CTA podstawowe: tło / tekst | `#22272E` / `#F7F8FA` |
| Link (po najechaniu: primary) | `#175CD3` |

Mapowanie dziedzin (propozycja, poza 15 tokenami): Pedagogika - accent (palony pomarańcz); Akademia AI - info (błękit); Pożyczki UE/BGK - secondary (grafit średni).

## Wariant 5 - Terakota i piasek (ciepły, ziemisty, ludzki)

![Wariant 5 - pasek 15 tokenów](./podglad/paleta-wariant-5.svg)

Najcieplejszy wariant: terakota jako główny kolor, oliwka jako przeciwwaga, piaskowe tła. Buduje ton szkoleń dla ludzi (Pedagogika, HR), kosztem powagi finansowej. Najbliższy obecnej Miedzi, ale rozjaśniony i bez bordo.

Sekcja w podglądzie HTML: `palette-preview-v2.html#wariant-5`.

| Element układu | Kolor w tym wariancie |
|---|---|
| Strona tytułowa: pas górny / tekst pasa / pasy akcentu | `#2B1F17` / `#EBDFCC` / `#914A14` |
| Tytuł display i H1 | `#8E3B1E` |
| Lead i przypisy (text-secondary) | `#6A5646` |
| H2 i nagłówki kolumn tabeli (secondary) | `#5C6A3B` |
| H3 drogowskaz, liczba prowadząca, CTA akcentowe (accent) | `#914A14` (tekst CTA: `#FAF5EC`) |
| Akapit (text-primary) na karcie (surface) na tle strony (background) | `#2B1F17` na `#F4EBDC` na `#FAF5EC` |
| Box informacyjny: krawędź i tytuł (info), ramka (border) | `#3B6D8C`, `#D6C7B0` |
| Tabela: linie (border), wiersze parzyste (neutral-light) | `#D6C7B0`, `#EBDFCC` |
| Etykiety stanu: success / warning / error / info | `#377033` / `#D9A441` (tekst `#2B1F17`) / `#B3261E` / `#3B6D8C` |
| CTA podstawowe: tło / tekst | `#8E3B1E` / `#FAF5EC` |
| Link (po najechaniu: primary) | `#3B6D8C` |

Mapowanie dziedzin (propozycja, poza 15 tokenami): Pedagogika - primary (terakota); Akademia AI - info (błękit przygaszony); Pożyczki UE/BGK - secondary (oliwka).

## Wariant 6 - Bordo akademickie (uroczyste, dyplomowe, chłodne neutrale)

![Wariant 6 - pasek 15 tokenów](./podglad/paleta-wariant-6.svg)

Zachowuje bordo jako kolor marki, ale podnosi je i nasyca, a brązowe neutrale zamienia na chłodne szarości i biel - ton uczelni i dyplomu zamiast rzemieślniczego papieru. Złoto jako akcent honorowy (pieczęć, linia).

Sekcja w podglądzie HTML: `palette-preview-v2.html#wariant-6`.

| Element układu | Kolor w tym wariancie |
|---|---|
| Strona tytułowa: pas górny / tekst pasa / pasy akcentu | `#1B1A1C` / `#E8E4DF` / `#8A6A1C` |
| Tytuł display i H1 | `#6B1E2E` |
| Lead i przypisy (text-secondary) | `#57524E` |
| H2 i nagłówki kolumn tabeli (secondary) | `#2E3A47` |
| H3 drogowskaz, liczba prowadząca, CTA akcentowe (accent) | `#8A6A1C` (tekst CTA: `#FAF8F5`) |
| Akapit (text-primary) na karcie (surface) na tle strony (background) | `#1B1A1C` na `#FFFFFF` na `#FAF8F5` |
| Box informacyjny: krawędź i tytuł (info), ramka (border) | `#2F5F8A`, `#D5CFC7` |
| Tabela: linie (border), wiersze parzyste (neutral-light) | `#D5CFC7`, `#E8E4DF` |
| Etykiety stanu: success / warning / error / info | `#2C6B46` / `#C4922C` (tekst `#1B1A1C`) / `#B3261E` / `#2F5F8A` |
| CTA podstawowe: tło / tekst | `#6B1E2E` / `#FAF8F5` |
| Link (po najechaniu: primary) | `#8A2436` |

Mapowanie dziedzin (propozycja, poza 15 tokenami): Pedagogika - primary (bordo); Akademia AI - info (błękit); Pożyczki UE/BGK - secondary (łupek).

## Wariant 7 - Sygnał (monochrom i jeden żywy akcent)

![Wariant 7 - pasek 15 tokenów](./podglad/paleta-wariant-7.svg)

Czerń, biel, szarości i jeden intensywny akcent pomarańczowy: maksymalna odporność na druk, kserokopie i tanie monitory, tożsamość budowana typografią (Manrope) zamiast kolorem. Najbardziej odważny i najmniej ciepły wariant.

Sekcja w podglądzie HTML: `palette-preview-v2.html#wariant-7`.

| Element układu | Kolor w tym wariancie |
|---|---|
| Strona tytułowa: pas górny / tekst pasa / pasy akcentu | `#111111` / `#E6E6E6` / `#B84500` |
| Tytuł display i H1 | `#111111` |
| Lead i przypisy (text-secondary) | `#555555` |
| H2 i nagłówki kolumn tabeli (secondary) | `#3D3D3D` |
| H3 drogowskaz, liczba prowadząca, CTA akcentowe (accent) | `#B84500` (tekst CTA: `#FFFFFF`) |
| Akapit (text-primary) na karcie (surface) na tle strony (background) | `#111111` na `#F4F4F4` na `#FFFFFF` |
| Box informacyjny: krawędź i tytuł (info), ramka (border) | `#1B5FC1`, `#C8C8C8` |
| Tabela: linie (border), wiersze parzyste (neutral-light) | `#C8C8C8`, `#E6E6E6` |
| Etykiety stanu: success / warning / error / info | `#1B7A3D` / `#E3A81B` (tekst `#111111`) / `#C1281E` / `#1B5FC1` |
| CTA podstawowe: tło / tekst | `#111111` / `#FFFFFF` |
| Link (po najechaniu: primary) | `#0B57D0` |

Mapowanie dziedzin (propozycja, poza 15 tokenami): Pedagogika - accent (pomarańcz) - jedyny kolor dziedzinowy; pozostałe dziedziny rozróżniane etykietą tekstową, nie kolorem; Akademia AI - brak koloru - etykieta tekstowa; Pożyczki UE/BGK - brak koloru - etykieta tekstowa.
