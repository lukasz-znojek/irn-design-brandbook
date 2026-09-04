# Logotyp IRIN - specyfikacja obowiązująca

**Status: ZATWIERDZONA.** Wydanie 02, na palecie **Regalia** (zatwierdzonej 2026-09-03).
Wersje kolorystyczne rozstrzygnięte przez właściciela 2026-09-04. To jest jedyne źródło prawdy
dla użycia znaku IRIN.

Kolor: [`paleta-barw.md`](./paleta-barw.md). Siatka: [`siatka-a4.md`](./siatka-a4.md).
Typografia: [`typografia.md`](./typografia.md).
Dane maszynowe: [`tokeny/palette-irin.json`](./tokeny/palette-irin.json).

Wszystkie kontrasty policzone od nowa 2026-09-04 wzorem WCAG 2.1. **Próg dla znaku to 3:1 dla
grafiki znaczącej**, nie 4,5:1 dla tekstu.

## Trzy pliki źródłowe

Leżą w korzeniu repozytorium. Wszystkie trzy są jednokolorowe: ścieżki nie mają atrybutu `fill`,
więc przyjmują `currentColor`; jedyny jawny `fill="none"` to przezroczysty prostokąt tła.
**Pliki nie definiują żadnej barwy** - barwa bierze się z reguły niżej.

| Plik | `viewBox` | Obwiednia artworku | Zastosowanie |
|---|---|---|---|
| `logo_irin_poziom.svg` | 281,333 × 158,667 | 184,213 × 38,854 | wariant podstawowy |
| `logo_irin_pion.svg` | 184,837 × 162,834 | 103,728 × 87,312 | pola wąskie i wysokie |
| `logo_irin_sygnet.svg` | 184,837 × 162,834 | 103,728 × 38,853 | znak samodzielny |

## Proporcja: korekta wobec dotychczasowego zapisu

**Do 2026-09-04 ten plik, `CLAUDE.md` i oba wydania księgi znaku podawały proporcje odczytane
z `viewBox`. To są proporcje pustej ramki, nie znaku.** Obwiednia artworku została zmierzona
w szablonie `templates/zestaw-drobnych/` przez `getBBox` na złożonej kanwie:

| Wariant | Proporcja `viewBox` (zapis dawny) | Proporcja artworku (obowiązująca) | Artwork zajmuje |
|---|---|---|---|
| poziom | 1,773:1 | **4,741:1** | 16,0 % powierzchni ramki |
| pion | 1,135:1 | **1,188:1** | 30,1 % powierzchni ramki |
| sygnet | 1,135:1 | **2,670:1** | 13,4 % powierzchni ramki |

**Skutek praktyczny, który trzeba znać przy każdym użyciu.** Jeżeli podasz kontenerowi
`width: 18mm` i wstawisz plik bez zmiany `viewBox`, sam znak będzie miał **11,8 mm** w wariancie
poziomym (65,5 % szerokości ramki) i **10,1 mm** w sygnecie (56,1 %) - czyli poniżej minimum,
którego pilnujesz. Minimum 18 mm i 10 mm dotyczy **znaku**, nie ramki.

**Dwa poprawne sposoby.** Albo nadpisujesz `viewBox` obwiednią artworku i wtedy szerokość
kontenera równa się szerokości znaku - tak robią szablony w `templates/`, wpisując obwiednie
jako stałe. Albo zostawiasz plik i dzielisz docelową szerokość znaku przez udział: 18 / 0,655
= **27,5 mm** kontenera dla poziomu, 10 / 0,561 = **17,8 mm** dla sygnetu.

**Pomiaru w czasie działania nie stosuj.** `getBBox` zaraz po wstrzyknięciu SVG potrafi zwrócić
0 × 0, a wtedy kontener bierze proporcję pustej ramki i znak rośnie poza strefę - to zmierzony
błąd, opisany w kodzie szablonu `zestaw-drobnych`. Obwiednie są stałe, więc wpisuje się je jako
wartości.

## Minimalny rozmiar

| Nośnik | Minimum znaku | Szerokość kontenera bez korekty `viewBox` | Status |
|---|---|---|---|
| Druk, poziom i pion | 18 mm | 27,5 mm (poziom) / 32,1 mm (pion) | **zatwierdzone** |
| Ekran, poziom i pion | 90 px | 137 px (poziom) | **zatwierdzone** |
| Sygnet samodzielny | 10 mm / 44 px | 17,8 mm / 78 px | **niepotwierdzony osobno** |
| Grawer i tłoczenie | **brak wartości** | - | niesprawdzone |

Falsyfikator wiersza o sygnecie: favicon 16 i 32 px z rozdz. 23 brandbooka - to pierwsze realne
użycie sygnetu poniżej 44 px. Falsyfikator wiersza o grawerze: pierwsza próba grawerska;
18 mm dotyczy rastra drukarki, nie narzędzia.

## Przestrzeń ochronna - miara x, teraz policzona

Jednostka **x = wysokość liter sygnetu**, mierzona od krawędzi znaku z każdej strony. To miara
względna, skalująca się ze znakiem, a nie stała liczba milimetrów.

**Do 2026-09-04 x nie miało przeliczenia** i pozycja wisiała jako otwarta. Zmierzone z obwiedni
ścieżek: wysokość artworku wobec jego szerokości wynosi **37,46 %** dla sygnetu i **21,09 %**
dla wariantu poziomego. Stąd:

| Wariant | Szerokość znaku | x z każdej strony |
|---|---|---|
| sygnet | 10 mm | **3,75 mm** |
| sygnet | 16 mm | **5,99 mm** |
| sygnet | 22 mm | **8,24 mm** |
| sygnet | 30 mm | **11,24 mm** |
| poziom | 40 mm | **8,44 mm** |
| poziom | 60 mm | **12,66 mm** |
| poziom | 100 mm | **21,09 mm** |

Zastrzeżenie: to obwiednia ścieżek, nie pomiar optyczny wysokości liter. Falsyfikator: pomiar
optyczny dający inną wartość niż 37,46 % dla sygnetu.

## Osiem dopuszczonych wersji kolorystycznych

Znak jest jednokolorowy i przyjmuje `currentColor`. **Barwa spoza tej ósemki jest złamaniem
systemu, nie decyzją projektową** - pozostałe sześć barw palety ma przypisane inne role.

| # | Wersja | HEX | Rola | Kanał druku |
|---|---|---|---|---|
| 01 | **Atrament** | `#07090C` | podstawowa | wszystkie kanały, w tym jeden tusz |
| 02 | **Kość Słoniowa** | `#F7F3E9` | odwrócona | wybranie z zadruku, jeden tusz |
| 03 | **Szafir Nocny** | `#132246` | markowa | CMYK |
| 04 | **Ametyst Dworski** | `#331F41` | przekrojowa: katalog, spis, indeks, cennik | CMYK |
| 05 | **Rubin Głęboki** | `#541319` | dziedzina Szkolenia zawodowe | CMYK |
| 06 | **Zieleń Butelkowa** | `#0B3627` | dziedzina Pożyczki UE/BGK | CMYK |
| 07 | **Bursztyn Wyciszony** | `#9B5E30` | dziedzina Akademia AI | CMYK |
| 08 | **Złoto Szampańskie** | `#C4B790` | warunkowa: uszlachetnienie | folia, tłoczenie albo farba |

**Wersja podstawowa to Atrament na Kości Słoniowej: 17,99:1.**
Czerń czysta `#000000` i biel czysta `#FFFFFF` **nie należą do systemu** - decyzja właściciela
2026-09-04. W druku jednym tuszem znak idzie w Atramencie albo jako wybranie z zadruku;
w grawerze i tłoczeniu nie ma farby, więc nie ma barwy do zadeklarowania.

## Matryca teł · osiem wersji × sześć podłoży

`T` dopuszczone, `N` zakazane. Próg 3:1. Kolumna tintu pokazuje tint właściwy dla wersji
w wierszu; wersje poza dziedzinami mierzone na tincie Szafiru `#DCDAD5`.

| Wersja \ podłoże | Kość Słoniowa | Alabaster | Muszla Różana | tint 12 % | Szafir Nocny | Aksamit Nocy |
|---|---|---|---|---|---|---|
| Atrament | 17,99 T | 15,25 T | 14,26 T | 14,27 T | 1,28 N | 1,04 N |
| Kość Słoniowa | 1,00 N | 1,18 N | 1,26 N | 1,26 N | 14,09 T | 17,25 T |
| Szafir Nocny | 14,09 T | 11,94 T | 11,17 T | 11,18 T | 1,00 N | 1,22 N |
| Ametyst Dworski | 13,41 T | 11,37 T | 10,63 T | 10,70 T | 1,05 N | 1,29 N |
| Rubin Głęboki | 12,77 T | 10,82 T | 10,12 T | 10,11 T | 1,10 N | 1,35 N |
| Zieleń Butelkowa | 12,06 T | 10,22 T | 9,56 T | 9,66 T | 1,17 N | 1,43 N |
| Bursztyn Wyciszony | 4,69 T | 3,98 N | 3,72 N | 3,72 N | 3,00 N | 3,68 N |
| Złoto Szampańskie | 1,80 N | 1,53 N | 1,43 N | 1,43 N | 7,82 T | 9,58 T |

**Trzy pola, w których wyrok nie wynika z liczby:**

- **Bursztyn Wyciszony na Alabastrze (3,98) i na Muszli Różanej (3,72)** przechodzą próg 3:1 i mimo to są zakazane - decyzją właściciela.
  Bursztyn jest jedyną wersją bez zapasu (na Kości Słoniowej 4,69), a znak
  przy 18 mm ma elementy cieńsze od kreski wersalika, więc nie dostaje ulgi. Na ciemnym wchodzi
  Kość Słoniowa.
- **Bursztyn na Szafirze (3,00) i na Aksamicie (3,68)** mieszczą się w progu albo są na jego granicy i też są zakazane, z tego samego powodu.
- **Złoto Szampańskie dostaje inny wyrok niż tekst.** Jako tekst na jasnym jest zabronione
  (1,80), jako znak na ciemnym wchodzi: Aksamit 9,58, Szafir 7,82 - w limicie 5 % powierzchni.

Oznaczenie zakazu w składzie: obrys **Rubinem Głębokim** `#541319`, znak `×` i liczba pod polem.
To świadome obciążenie - Rubin jest jednocześnie barwą dziedziny Szkolenia zawodowe.

## Dobór wersji - trzy kroki

1. **Jasność podłoża.** Ciemne (Szafir Nocny, Aksamit Nocy) → **Kość Słoniowa**. Wyjątek:
   uszlachetnienie - pieczęć, tłoczenie, obramowanie dyplomu - gdzie wolno **Złoto Szampańskie**
   w limicie 5 %. Jasne → krok 2.
2. **Dziedzina.** Jedna dziedzina → **Rubin Głęboki** / **Zieleń Butelkowa** / **Bursztyn
   Wyciszony** (Bursztyn wyłącznie na Kości Słoniowej). Obszar bez własnej barwy → **Szafir Nocny
   plus podpis słowem**, nigdy nowa barwa. Wielodziedzinowy albo pozadziedzinowy → krok 3.
3. **Funkcja materiału.** Reprezentacyjny (okładka, pismo, dyplom, oferta) → **Szafir Nocny**.
   Przekrojowy (katalog, spis, indeks, cennik) → **Ametyst Dworski**. Treściowy (tabela, karta
   usługi, załącznik) → **Atrament**.

**Reguła awaryjna:** wątpliwość rozstrzyga się na korzyść wersji podstawowej. Atrament na Kości
Słoniowej, 17,99:1, przechodzi zawsze.

## Zakazy - wszystkie wiążące

1. **Barwa spoza ósemki.** Lapis Stonowany, Grafit Jedwabny i Złoto Antyczne mają kontrast
   przechodzący próg (6,77, 5,44, 4,99) i mimo to nie są wersjami znaku - sygnał by kłamał.
2. **Nie obracamy, nie pochylamy, nie odbijamy lustrzanie.**
3. **Nie dodajemy cienia, poświaty, obrysu ani efektu 3D.** W PDF rasteryzują znak.
4. **Nie rozciągamy nieproporcjonalnie.** Skalowanie wyłącznie z proporcją artworku z tabeli wyżej.
5. **Nie ustawiamy barwy łańcuchem `filter:`.** Z filtra nie da się odczytać zamierzonej barwy,
   a w PDF filtr często rasteryzuje znak. Barwa idzie przez `color` kontenera i `fill: currentColor`.
6. **Znak nigdy dwukolorowy** - nie łączy się sygnetu w jednej barwie z wordmarkiem w drugiej.
7. **Barwa dziedziny tylko z dziedziną.** Materiał bez dziedziny dostaje Szafir albo Atrament.
8. **Znak nigdy na zdjęciu bez plamy neutralnej.** Kontrast lokalny fotografii jest niepoliczalny,
   więc żadna liczba z matrycy nie obowiązuje.
9. **Znak stoi w dokumencie raz.** Powtórzony w ornamencie przestaje być podpisem.
10. **Nigdy w zestawieniu ze znakiem Funduszy Europejskich, znakiem barw RP ani flagą UE.**
    Zakaz twardy: IRIN jest doradcą zewnętrznym, nie beneficjentem.

Dwa błędy doboru wariantu, dotyczące kształtu pola, nie barwy: wariant poziomy naciągnięty
w polu wąskim (wchodzi pion albo sygnet) oraz sygnet samodzielny na okładce (wchodzi poziom albo pion).

## Druk znaku

| Sytuacja | Wersja | Zapis drukarski |
|---|---|---|
| Jeden tusz na jasnym papierze | Atrament | K100 bez podkładu |
| Jeden tusz, znak w wybraniu | Kość Słoniowa | wybranie z zadruku |
| Cztery farby, znak na jasnym | Atrament | K100 bez podkładu |
| Cztery farby, znak barwny | Szafir, Ametyst albo dziedzina | CMYK z `paleta-barw.md` |
| Uszlachetnienie na ciemnym | Złoto Szampańskie | folia, tłoczenie albo 18/20/45/0 |

**Znak zawsze K100 bez podkładu, niezależnie od wielkości.** To decyzja, nie pomiar: znak jest
konturem, nie plamą, a czernia kryta obowiązuje wyłącznie na plamach i pasach. Pasowanie czterech
farb rozmywa kontur sygnetu przy 18 mm.

**W mono** przeliczenie `100 − L`: Atrament 86 % K, Szafir 74 %, Ametyst 72 %, Rubin 70 %,
Zieleń 70 %, Bursztyn 46 %, Złoto Szampańskie 22 %. **Rubin i Zieleń wypadają identycznie**, więc
w druku jednokolorowym znak dziedziny Szkolenia i znak dziedziny Pożyczki są nieodróżnialne -
to potwierdzenie zakazu 7, nie defekt. Złoto przy 22 % w kanale jednokolorowym nie wchodzi wcale.

## Do potwierdzenia

| # | Pozycja | Status | Falsyfikator |
|---|---|---|---|
| 01 | Minimum sygnetu 10 mm / 44 px | niepotwierdzone osobno | favicon 16 i 32 px |
| 02 | Miara x jako procent szerowości | **policzona 2026-09-04** z obwiedni ścieżek | pomiar optyczny dający inną wartość |
| 03 | Minimum znaku w grawerze i tłoczeniu | brak wartości | pierwsza próba grawerska |
| 04 | Rubin jako barwa oznaczenia zakazu | świadome obciążenie | pierwszy materiał dziedziny Szkolenia z tabelą zakazów |
| 05 | Czwarta barwa dziedziny | **nie dobrana**; `tokens.css` opisuje sześć obszarów, paleta zna trzy barwy | decyzja właściciela |
| 06 | Piąta zasada z kanwy: znak nie na akcentach poniżej 4,5:1 | przestała być pusta | Kość Słoniowa na Bursztynie daje 4,69, zapas 0,19 punktu - potwierdzenie albo skreślenie reguły |
