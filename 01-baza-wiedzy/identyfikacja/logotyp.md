# Logotyp IRIN - specyfikacja obowiązująca

**Status: ZATWIERDZONA przez foundera.** Minimalny rozmiar i przestrzeń ochronna potwierdzone wcześniej; cztery zakazy modyfikacji potwierdzone 2026-09-02. To jest jedyne źródło prawdy dla użycia znaku IRIN.

Kolor: [`paleta-barw.md`](./paleta-barw.md). Siatka: [`siatka-a4.md`](./siatka-a4.md). Typografia: [`typografia.md`](./typografia.md).
Dane maszynowe: [`tokeny/palette-irin.json`](./tokeny/palette-irin.json), klucz `logotyp`.
Jak logotyp wchodzi do zlecenia dla Claude Design: [`../../03-pakiet-claude-design/format-paczki.md`](../../03-pakiet-claude-design/format-paczki.md).

## Trzy pliki źródłowe

Leżą w korzeniu repozytorium. Proporcje odczytane z atrybutu `viewBox` w tej sesji, nie przepisane.

| Plik | viewBox | Proporcja | Zastosowanie |
|---|---|---|---|
| `logo_irin_poziom.svg` | 281,333 × 158,667 | 1,773:1 | wariant podstawowy |
| `logo_irin_pion.svg` | 184,837 × 162,834 | 1,135:1 | pola wąskie i wysokie |
| `logo_irin_sygnet.svg` | 184,837 × 162,834 | 1,135:1 | znak samodzielny |

**Wszystkie trzy są jednokolorowe.** Ścieżki graficzne nie mają zdefiniowanego atrybutu `fill`, więc renderują się domyślnym czarnym; jedyny jawny `fill="none"` dotyczy przezroczystego prostokąta tła. Pliki źródłowe **nie definiują żadnej palety barw** - kolor znaku bierze się z reguł niżej, nie z plików.

**Obserwacja do sprawdzenia przy pierwszym realnym użyciu:** plik pionowy i sygnet mają identyczny `viewBox`, choć różnią się zawartością (pionowy waży 15,8 kB wobec 9,6 kB sygnetu, czyli ma więcej ścieżek). Praktyczny skutek: oba mają tę samą proporcję ramki, więc podstawienie jednego za drugi nie zmieni wymiarów pola. To **nie znaczy**, że wolno je zamieniać - to dwa różne warianty znaku o różnym przeznaczeniu.

## Minimalny rozmiar

| Nośnik | Minimum | Status |
|---|---|---|
| Druk | 18 mm szerokości | **zatwierdzone** |
| Ekran | 90 px szerokości | **zatwierdzone** |
| Sygnet samodzielny | 10 mm / 44 px | odczyt z `brandbook.dc.html`, **nie potwierdzony osobno** |

Wiersz o sygnecie pochodzi z tabeli w kanwie foundera i nie był rozstrzygany razem z dwoma pozostałymi. Do potwierdzenia przy pierwszym dokumencie używającym samodzielnego sygnetu.

## Przestrzeń ochronna

Jednostka **x = wysokość liter sygnetu**. To miara względna, skalująca się razem ze znakiem, a nie stała liczba milimetrów.

Żaden element graficzny, tekstowy ani krawędź strony nie wchodzi bliżej niż **x** z każdej strony logotypu.

Konsekwencja praktyczna: przy logotypie w minimalnym rozmiarze 18 mm przestrzeń ochronna też jest mała, więc znak w minimalnym rozmiarze nadal wymaga świadomego odsunięcia od krawędzi - nie da się tego załatwić jednym marginesem strony dla wszystkich wielkości znaku.

## Zakazy - wszystkie wiążące

Zatwierdzone przez foundera 2026-09-02. Wcześniej były odczytem z `brandbook.dc.html` opatrzonym dopiskiem „do potwierdzenia"; dopisek już nie obowiązuje.

1. **Nie zmieniamy koloru znaku.** Ani sygnetu, ani wersji poziomej, ani pionowej. Znak jest jednokolorowy; na ciemnym tle stosuje się wersję odwróconą, a nie przebarwioną.
2. **Nie obracamy, nie pochylamy, nie odbijamy lustrzanie.**
3. **Nie dodajemy cienia, poświaty ani obrysu.**
4. **Nie rozciągamy nieproporcjonalnie.** Skalowanie wyłącznie z zachowaniem proporcji podanych w tabeli wyżej.

Dlaczego zakaz koloru jest tu najważniejszy: pliki źródłowe nie niosą własnej palety, więc bez tej reguły każde zlecenie dla Claude Design mogłoby pokolorować znak według uznania. Logotyp jest jedynym elementem tożsamości, którego nie da się odtworzyć z żadnej innej specyfikacji po zepsuciu - paletę, siatkę i skalę można przeliczyć na nowo, znaku nie.

**Piąta zasada z kanwy, nadal nie potwierdzona:** „nie umieszczamy na akcentach dziedzinowych poniżej kontrastu 4,5:1". Jest to reguła o kontraście, nie o modyfikacji znaku, i nie była przedmiotem decyzji z 2026-09-02. W obecnej palecie wszystkie trzy akcenty dziedzinowe (Aksamit 12,80:1, Miedź 6,16:1, Onyks 9,19:1 na papierze Kaszmir) i tak przekraczają ten próg, więc reguła nikogo dziś nie ogranicza - ale przy przyszłej zmianie palety warto ją potwierdzić albo skreślić świadomie.
