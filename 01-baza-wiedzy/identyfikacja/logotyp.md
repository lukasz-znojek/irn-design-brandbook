# Logotyp IRIN - specyfikacja obowiązująca

**Status: ZATWIERDZONA.** Trzy warianty znaku, jednokolorowe. Minimalny rozmiar i przestrzeń ochronna potwierdzone przez foundera; cztery zakazy modyfikacji potwierdzone 2026-09-02.

Dane maszynowe: [`tokeny/palette-irin.json`](./tokeny/palette-irin.json), klucz `logotyp`. Kolor: [`paleta-barw.md`](./paleta-barw.md). Siatka: [`siatka-a4.md`](./siatka-a4.md). Typografia: [`typografia.md`](./typografia.md).

**Ten plik jest wywiedziony, nie źródłowy.** Obwiednie odtwarza pomiar w Chromium: `_robocze/narzedzia/zmierz-znak.mjs`. Wartość wpisana do generatora jest kopią pomiaru, nigdy odwrotnie - gdy pomiar się nie zgadza, poprawia się tabelę w generatorze, nie skrypt.

## Trzy pliki źródłowe

| Plik | viewBox | Obwiednia znaku widocznego | Proporcja znaku | Współczynnik pola | Zastosowanie |
|---|---|---|---|---|---|
| `logo_irin_poziom.svg` | 281,333 × 158,667 | x 48,561, y 59,907, 184,213 × 38,854 | 4,7412 | **0,655** | wariant podstawowy |
| `logo_irin_pion.svg` | 184,837 × 162,834 | x 40,555, y 37,761, 103,728 × 87,312 | 1,1880 | **0,561** | pola wąskie i wysokie |
| `logo_irin_sygnet.svg` | 184,837 × 162,834 | x 40,555, y 61,991, 103,728 × 38,853 | 2,6698 | **0,561** | znak samodzielny |

Wszystkie trzy pliki są **jednokolorowe**: ścieżki nie mają zadeklarowanego `fill`, więc renderują się domyślnym czarnym, a jedyny jawny `fill="none"` dotyczy przezroczystego prostokąta tła. Pliki źródłowe nie definiują żadnej barwy.

## Konwencja pomiaru: obwiednia znaku widocznego

**Każdy wymiar znaku podany w systemie IRIN jest szerokością OBWIEDNI ZNAKU WIDOCZNEGO, nie szerokością pola pliku. Pliki mają w viewBoksie puste pole; wstawienie znaku na szerokość pola daje znak mniejszy od zadeklarowanego.**

Skutek liczbowy, wypisany, bo bez niego liczba „18 mm" jest dwuznaczna:

| Jeżeli 18 mm zmierzysz jako | Znak widoczny ma wtedy | Braknie |
|---|---|---|
| szerokość pola pliku `logo_irin_poziom.svg` | 11,79 mm | 34,5 % |
| szerokość pola pliku `logo_irin_pion.svg` | 10,10 mm | 43,9 % |
| szerokość pola pliku `logo_irin_sygnet.svg` | 10,10 mm | 43,9 % |

W drugą stronę, czyli ile musi mieć **pole pliku**, żeby znak widoczny osiągnął 18 mm:

| Plik | Pole pliku |
|---|---|
| `logo_irin_poziom.svg` | **27,48 mm** |
| `logo_irin_pion.svg` | **32,09 mm** |
| `logo_irin_sygnet.svg` | **32,09 mm** |

Ta konwencja obowiązuje **każdy wymiar znaku podany w tym systemie**: minimalny rozmiar, przestrzeń ochronną i wielkość w każdym wzorze nośnika.

## Minimalny rozmiar

Wszystkie trzy wartości mierzone **w obwiedni znaku widocznego**, nie w polu pliku.

| Nośnik | Minimum | Stan |
|---|---|---|
| druk | **18 mm** szerokości | potwierdzone przez foundera |
| ekran | **90 px** szerokości | potwierdzone przez foundera |
| sygnet samodzielny | **10 mm** szerokości | **NIEPOTWIERDZONE NA WYDRUKU** - falsyfikator otwarty |

## Przestrzeń ochronna

**x = wysokość liter sygnetu, mierzona z każdej strony znaku; miara względna, skaluje się ze znakiem**

Miara jest względna, więc skaluje się ze znakiem i nie wymaga tabeli milimetrów. Przeliczenie z obwiedni, żeby dało się ją odłożyć na oko:

- **sygnet:** wysokość znaku to 37,5 % jego szerokości, więc `x` odkładane z każdej strony jest w tej proporcji;
- **wersja pozioma:** wysokość znaku to 21,1 % szerokości, czyli `x` jest tu wizualnie mniejsze wobec całej szerokości.

W przestrzeni ochronnej nie stoi nic: ani tekst, ani linia, ani krawędź kadru, ani inny znak.

## Cztery zakazy

1. nie zmieniamy koloru znaku; na ciemnym tle wersja odwrócona, nie przebarwiona;
2. nie obracamy, nie pochylamy, nie odbijamy lustrzanie;
3. nie dodajemy cienia, poświaty ani obrysu;
4. nie rozciągamy nieproporcjonalnie.

**Zakaz zmiany koloru jest z tych czterech najważniejszy**, bo jest jedynym, który łamie się przez przypadek, a nie przez pomysł. Znak wstawiony na ciemne tło i „rozjaśniony" filtrem przestaje być znakiem jednokolorowym: filtr zmienia wszystkie kanały naraz, więc barwa wychodzi spoza palety i nie da się jej policzyć w macierzy kontrastów. Na ciemnym tle wchodzi **wersja odwrócona**, czyli ten sam znak wypełniony Kością Słoniową, a nie znak przebarwiony.

## Barwa znaku w kodzie

**przez color kontenera i fill: currentColor; nigdy filter:**

```css
.znak { color: var(--irin-r-atrament); }
.znak svg path, .znak svg polygon, .znak svg rect:not([fill="none"]) { fill: currentColor; }
```

Dwa powody, dla których to jest jedyna dopuszczona droga. Po pierwsze, barwa znaku staje się wtedy tokenem palety i podlega tej samej macierzy kontrastów co tekst. Po drugie, wersja odwrócona to zmiana jednej właściwości `color` na kontenerze, a nie drugi plik SVG, który trzeba pamiętać, żeby zaktualizować.

## Dobór barwy znaku

| Sytuacja | Barwa znaku | Tło | Kontrast |
|---|---|---|---|
| domyślna | Atrament | Kość Słoniowa | 17,99:1 |
| wersja odwrócona | Kość Słoniowa | Aksamit Nocy | 17,25:1 |
| na barwie marki | Kość Słoniowa | Szafir Nocny | 14,09:1 |

**Na fotografii żadna liczba z tej tabeli nie obowiązuje.** Kontrast lokalny zdjęcia jest niepoliczalny: ta sama plama znaku wypada raz na jasnym niebie, raz na ciemnym budynku. Dlatego znak na zdjęciu siada na plamie neutralnej - prostokącie albo wygaszeniu w barwie nośnej - i kontrast liczy się do tej plamy, nie do zdjęcia.

## Falsyfikator otwarty

**Minimalny rozmiar samodzielnego sygnetu 10 mm** nie został sprawdzony na wydruku. Do tego czasu jest wartością przyjętą, nie zmierzoną: o czytelności znaku przy tej szerokości decyduje raster drukarki i chłonność papieru, a nie geometria pliku, więc w kodzie ani w renderze nie da się tego rozstrzygnąć.
