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

## Rozbieżność otwarta: jednostka bazowa 6 mm

`brandbook.dc.html` podaje jednostkę bazową 6 mm dla rytmu pionowego. Zmierzone: 251 mm / 6 mm = **41,83**, czyli 41 pełnych jednostek i **5 mm reszty**. Rytm pionowy nie domyka się na wysokości pola treści.

To nie jest błąd blokujący - reszta 5 mm może po prostu wypadać na dole strony, poniżej ostatniej linii bazowej. Ale jeśli rytm ma domykać się co do milimetra, margines dolny musiałby wynosić **33 mm** zamiast 28 mm: 297 - 18 - 33 = 246 mm, a 246 / 6 = 41 dokładnie.

**Status: do rozstrzygnięcia przez foundera.** Margines 28 mm został zatwierdzony 2026-09-02 i obowiązuje - tej wartości nie zmieniono. Ten punkt jest zapisany, żeby nie wyszedł jako niespodzianka przy pierwszym dokumencie z gęstym tekstem. Falsyfikator: jeśli jednostka 6 mm nie jest w ogóle wiążąca (kanwa podaje ją opisowo, bez zastosowania), rozbieżność nie ma znaczenia.
