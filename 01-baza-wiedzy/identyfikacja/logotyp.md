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

## Logotyp w systemie BUR - dwa ustalenia z odczytu 2026-09-06

Odczyt dokumentów PARP (`/01-baza-wiedzy/prawo/bur.md`, sekcje „Karta Dostawcy Usług” i „Licencja na materiały zamieszczone w BUR”) dał dwie rzeczy dotyczące bezpośrednio tego pliku.

**1. Pole „Logo” w Karcie Dostawcy Usług jest opcjonalne i bez wymogów technicznych.** Załącznik 1 do Regulaminu BUR (wersja od 1 stycznia 2026 r.), poz. 1, s. 1: „Podmiot świadczący Usługi rozwojowe/ Dostawca Usług ma możliwość dodania logotypu jakim posługuje się w obrocie gospodarczym.” Załącznik nie podaje formatu pliku, wymiarów, proporcji, wagi ani wymagań co do tła. Wybór wariantu (poziomy, pionowy, sygnet) i przygotowanie pliku to więc **swobodny wybór projektowy** IRIN. Rekomendacja do rozstrzygnięcia przy zakładaniu profilu: wariant poziomy, bo profil w BUR jest polem szerokim - ale to dopiero propozycja, nie decyzja.

**2. Zakazy modyfikacji nie wiążą Administratora BUR.** Regulamin BUR § 16 ust. 1-2 (s. 25-26): materiał wgrany do BUR objęty jest bezterminową, nieodpłatną i niewyłączną licencją dla Administratora BUR, a pola eksploatacji obejmują wprost „scalanie, dostosowywanie, przerabianie oraz dokonywanie wszelkich zmian służących połączeniu z innymi utworami” (ust. 2 pkt 6) i udzielanie dalszych licencji (pkt 7); dostawca zrzeka się przy tym roszczeń.

Cztery zakazy wyżej pozostają w mocy - wiążą IRIN i wykonawców pracujących dla IRIN. Nie wiążą PARP w odniesieniu do plików wgranych do BUR. **Praktyczny wniosek: to nie jest powód do zmiany zakazów, tylko powód do świadomej decyzji, które pliki trafiają do systemu BUR.** Falsyfikator tego wniosku: zapis w dokumencie PARP spoza sześciu plików w `/01-baza-wiedzy/prawo/zrodla/` (np. w „Strefie dla Dostawców Usług”), który ograniczałby licencję z § 16 dla materiałów graficznych.

Uwaga o zakresie tego ustalenia: pomiar na pełnym tekście sześciu dokumentów PARP pokazał, że słowa „logo” i „logotyp” występują w całym korpusie **dokładnie dwa razy** - oba w tej jednej pozycji Załącznika 1. Żaden z tych dokumentów nie nakłada obowiązku ani nie daje prawa posługiwania się znakiem BUR, logo PARP ani znakiem Funduszy Europejskich.

**Piąta zasada z kanwy, przepisana na Regalię 2026-09-09:** kanwa mówiła „nie umieszczamy
na akcentach dziedzinowych poniżej kontrastu 4,5:1". Reguła dotyczy kontrastu, nie
modyfikacji znaku, i nie była przedmiotem decyzji z 2026-09-02. W Regalii barwy nie są
przypisane do obszarów, więc dotyczy ona czterech barw dostępnych w gnieździe
`--irin-r-dziedzina`: Kość Słoniowa na nich daje kolejno Rubin Głęboki 12,77:1, Zieleń Butelkowa 12,06:1, Bursztyn Wyciszony 4,69:1, Ametyst Dworski 13,41:1.
Wszystkie przechodzą próg 4,5:1 dla tekstu, ale **Bursztyn Wyciszony ma zapas 0,19**,
więc przy tej barwie obszaru reguła przestaje być teoretyczna. Zapis pochodzi
z odczytu 2026-09-06; poprzednia wersja tego akapitu wymieniała trzy akcenty palety v2
i została zastąpiona, bo tamtych barw w systemie nie ma.
