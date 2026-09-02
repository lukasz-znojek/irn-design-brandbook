# Siatka dokumentu A4 - specyfikacja obowiązująca

**Status: ZATWIERDZONA przez foundera (2026-09-02).** To jest jedyne źródło prawdy dla siatki dokumentów IRIN.

Dane maszynowe: [`tokeny/palette-irin.json`](./tokeny/palette-irin.json), klucz `siatka-a4`.
Kolor: [`paleta-barw.md`](./paleta-barw.md). Typografia: [`typografia.md`](./typografia.md).
Jak siatka wchodzi do zlecenia dla Claude Design: [`../../03-pakiet-claude-design/format-paczki.md`](../../03-pakiet-claude-design/format-paczki.md).
Pomiar i historia decyzji: [`../../03-pakiet-claude-design/propozycja-palety-i-siatki-do-potwierdzenia.md`](../../03-pakiet-claude-design/propozycja-palety-i-siatki-do-potwierdzenia.md).

## Parametry

| Parametr | Wartość |
|---|---|
| Format strony | A4 pion, 210 × 297 mm |
| Kolumny | 6 |
| Moduł kolumny | 25 mm |
| Gutter | 4 mm |
| Margines górny | 18 mm |
| Margines lewy | 18 mm |
| Margines prawy | 22 mm |
| Margines dolny | 28 mm |
| Pole treści | 170 × 251 mm |

Liczba kolumn (sześć) jest wspólna dla wszystkich trzech dziedzin - to element tożsamości systemu, nie parametr do dobierania per dokument.

## Sprawdzenie, że siatka fizycznie mieści się na stronie

Szerokość pola treści: 210 - 18 (lewy) - 22 (prawy) = **170 mm**.
Suma siatki: 6 × 25 + 5 × 4 = 150 + 20 = **170 mm**.
**Dopasowanie dokładne**, bez zapasu i bez nadmiaru.

Wysokość pola treści: 297 - 18 (górny) - 28 (dolny) = **251 mm**.

Liczby przeliczone w tej sesji, nie przepisane z żadnego dokumentu. Falsyfikator: inny format albo inna orientacja strony niż A4 pion - wtedy całe to sprawdzenie trzeba wykonać od nowa.

## Dlaczego moduł to 25 mm, a nie 32 mm z kanwy

`brandbook.dc.html` opisuje siatkę jako 6 kolumn, moduł 32 mm, gutter 4 mm. Ta siatka jest geometrycznie niemożliwa na A4 pion: 6 × 32 + 5 × 4 = **212 mm**, czyli o 2 mm więcej niż cała szerokość strony (210 mm) i o 42 mm więcej niż pole treści przy podanych marginesach. Nie mieści się nawet przy marginesach zerowych.

Poprawka polegała na zmniejszeniu modułu z 32 do 25 mm przy zachowaniu sześciu kolumn i gutteru 4 mm - bo to liczba kolumn jest w kanwie opisana jako element wspólny systemu, a moduł 32 mm był niesprawdzonym pomiarem. Rozważana alternatywa (5 kolumn po 32 mm, prawy margines zmniejszony do 16 mm) została odrzucona przez foundera.

## Jednostka bazowa 6 mm - rozstrzygnięte

`brandbook.dc.html` podaje jednostkę bazową 6 mm. Pierwsze podejrzenie brzmiało, że rytm pionowy się nie domyka: 251 mm / 6 mm = 41,83, czyli 41 pełnych jednostek i 5 mm reszty, a domknięcie wymagałoby marginesu dolnego 33 mm. **Pomiar pokazał, że to jest zła diagnoza** i margines nie jest tu w ogóle problemem.

Żeby jednostka 6 mm mogła działać jako siatka linii bazowych tekstu, interlinia korpusu musiałaby być jej wielokrotnością. Nie jest:

| Wielkość | Wartość |
|---|---|
| Jednostka bazowa | 6 mm = 22,68 px (przy 96 dpi) |
| Interlinia korpusu | 13,5 px × 1,55 = 20,93 px = **5,54 mm** |
| Różnica na każdą linię | 1,75 px = **0,46 mm** |
| Dryf na pełnej kolumnie (45 linii) | **19 mm** |

Tekst korpusu rozjeżdża się z siatką 6 mm o niecały milimetr na linię i o prawie dwa centymetry na pełnej stronie. Zmiana marginesu dolnego z 28 na 33 mm nie ma z tym nic wspólnego - poprawiłaby wyłącznie dzielenie jednej liczby przez drugą, nie ustawiłaby ani jednej linii tekstu na siatce.

**Rozstrzygnięcie: margines dolny zostaje 28 mm, a jednostka 6 mm jest jednostką odstępu, nie siatką linii bazowych tekstu.** Służy do wymierzania przerw między blokami, marginesów wewnętrznych i wysokości elementów - tam dzielenie się wysokości strony nie ma znaczenia, bo bloki nie muszą wypełniać kolumny co do milimetra. Reszta 5 mm wypada poniżej ostatniej linii i jest po prostu dodatkowym światłem u dołu strony.

**Co by musiało się zmienić, gdyby founder jednak chciał prawdziwej siatki linii bazowych:** interlinia korpusu z 1,55 na około **1,68** (czyli 22,68 px przy stopniu 13,5 px). To zmiana typografii, nie siatki, i rozluźniłaby tekst o 8 procent - w dokumentach regulowanych, gdzie treści jest dużo, to realny koszt stron. Nikt o taką zmianę nie prosił, więc jej nie wprowadzono.

**Falsyfikator tego rozstrzygnięcia:** jeśli jednostka 6 mm miała w zamyśle foundera dotyczyć właśnie linii bazowych tekstu, a nie odstępów - wtedy wracamy do tego punktu i rozmawiamy o interlinii, nadal nie o marginesie.
