# Paleta barw IRIN - specyfikacja obowiązująca

**Status: ZATWIERDZONA przez właściciela 2026-09-03.** Nazwa systemu: **Regalia** (wariant B).
To jest jedyne źródło prawdy dla kolorów IRIN.

**Ta specyfikacja zastąpiła w całości paletę „Kaszmir Wyciszony" (14 kolorów, zatwierdzoną
2026-09-02).** Żadna nazwa i żaden hex ze starej palety nie obowiązuje. Wypadły: Kaszmir, Muślin,
Pergamin, Espresso, Sepia, Popiół, Miedź, Onyks, Karmin, Patyna, Werdykt, Rubryka, Aksamit
(dawny `#452430`), Złoto foliowe. Historia i uzasadnienie wyboru: dokumenty `irn-design-*`
w projekcie Claude Design `1a22ce64-0e1c-43a6-bd60-eef9241ef73b`.

Dane maszynowe: [`tokeny/palette-irin.json`](./tokeny/palette-irin.json).
Siatka A4: [`siatka-a4.md`](./siatka-a4.md). Typografia: [`typografia.md`](./typografia.md).
Logotyp: [`logotyp.md`](./logotyp.md). Ten plik opisuje wyłącznie kolor.

**Wszystkie kontrasty w tym pliku policzone od nowa 2026-09-04** wzorem WCAG 2.1 na luminancji
względnej sRGB, skryptem, nie przepisane z żadnego dokumentu. Progi: tekst normalny AA 4,5:1,
AAA 7:1; element interfejsu i grafika znacząca 3:1.

## Barwy nośne · 7

| # | Nazwa | HEX | CMYK (Coated FOGRA39) | Σ | Rola | na Kości Słoniowej | na Aksamicie Nocy |
|---|---|---|---|---|---|---|---|
| 01 | **Szafir Nocny** | `#132246` | 100/90/45/40 | 275 % | kolor marki, pasy nagłówkowe, wypełnienie CTA | 14,09:1 | 1,22:1 |
| 02 | **Rubin Głęboki** | `#541319` | 35/100/85/45 | 265 % | dziedzina Szkolenia zawodowe | 12,77:1 | 1,35:1 |
| 03 | **Zieleń Butelkowa** | `#0B3627` | 95/50/80/60 | 285 % | dziedzina Pożyczki UE/BGK, status pozytywny | 12,06:1 | 1,43:1 |
| 04 | **Ametyst Dworski** | `#331F41` | 75/90/40/45 | 250 % | materiał przekrojowy, kategorie, tagi | 13,41:1 | 1,29:1 |
| 05 | **Złoto Szampańskie** | `#C4B790` | 18/20/45/0 | 83 % | akcent do 5 %: linia, pieczęć, tłoczenie | 1,80:1 | 9,58:1 |
| 06 | **Atrament** | `#07090C` | 70/60/55/100 | 285 % | typografia główna | 17,99:1 | 1,04:1 |
| 07 | **Kość Słoniowa** | `#F7F3E9` | 1/2/7/0 | 10 % | tło strony | tło | 17,25:1 |

## Barwy funkcjonalne · 7

| # | Nazwa | HEX | CMYK | Σ | Rola | na Kości Słoniowej | na Aksamicie Nocy |
|---|---|---|---|---|---|---|---|
| 08 | **Alabaster** | `#E4E1D8` | 5/5/11/0 | 21 % | tła kart; tekst drugorzędny na ciemnym | 1,18:1 | 14,62:1 |
| 09 | **Grafit Jedwabny** | `#606369` | 55/45/40/15 | 155 % | tekst drugorzędny na jasnym, linie | 5,44:1 | 3,17:1 |
| 10 | **Aksamit Nocy** | `#080F1F` | 95/85/45/65 | 290 % | tło ciemne, stopka | 17,25:1 | tło |
| 11 | **Muszla Różana** | `#E8D6D6` | 3/15/10/0 | 28 % | cytaty, podświetlenia | 1,26:1 | 13,67:1 |
| 12 | **Złoto Antyczne** | `#75674B` | 40/45/70/25 | 180 % | podpowiedzi, metadane | 4,99:1 | 3,46:1 |
| 13 | **Bursztyn Wyciszony** | `#9B5E30` | 22/65/95/12 | 194 % | ostrzeżenie; dziedzina Akademia AI | 4,69:1 | 3,68:1 |
| 14 | **Lapis Stonowany** | `#305686` | 85/62/20/10 | 177 % | odnośniki, stan aktywny | 6,77:1 | 2,55:1 |

**HEX jest wiążący. CMYK jest referencyjny** i staje się wiążący po proofie cyfrowym na papierze
docelowym - to pozycja otwarta, patrz sekcja „Do potwierdzenia".

## Tinty dziedzinowe · 12 % krycia

Procent farby, nie nowe wartości palety. Wyłącznie tła kart i pasy tabel.

| Tint | HEX | Podstawa | Atrament na tincie |
|---|---|---|---|
| Szafir 12 % | `#DCDAD5` | Szafir Nocny na Kości Słoniowej | **14,27:1** |
| Rubin 12 % | `#E3D8D0` | Rubin Głęboki na Kości Słoniowej | **14,24:1** |
| Zieleń 12 % | `#DBDCD2` | Zieleń Butelkowa na Kości Słoniowej | **14,41:1** |
| Ametyst 12 % | `#DFDAD5` | Ametyst Dworski na Kości Słoniowej | **14,36:1** |

Rozrzut czterech tintów wobec Atramentu: 14,24 do 14,41:1, czyli 0,17 punktu. Tinty są nieodróżnialne kontrastem i **nie kodują dziedziny same** - obok tintu stoi słowo.

## Hierarchia powierzchni 80 / 15 / 5

- **80 % baza:** Kość Słoniowa (tło) plus Atrament (typografia), a w niej Grafit Jedwabny na linie
  i tekst drugorzędny, Alabaster na tła kart, tinty 12 % na karty dziedzinowe.
- **15 % sygnał:** Szafir Nocny **plus dokładnie jeden** kolor dziedziny na dokument.
- **5 % akcent:** Złoto Szampańskie - linia, pieczęć, tłoczenie. Limit 21,34 cm²
  na polu treści A4 (5 % z 170 × 251 mm = 426,70 cm²).
- **punktowo:** Lapis Stonowany, Złoto Antyczne, Bursztyn Wyciszony, Muszla Różana.

Pary bazowe: Atrament na Kości Słoniowej **17,99:1**, odwrócenie Kość Słoniowa
na Aksamicie Nocy **17,25:1**. Tekst drugorzędny: na jasnym Grafit Jedwabny
(5,44:1), na ciemnym Alabaster (14,62:1).

**Maksymalnie dwa tła na dokument:** Kość Słoniowa plus jedno ciemne (Aksamit Nocy albo Szafir Nocny).

## Cztery barwy nośne nie różnicują się kontrastem - dlaczego dziedziny wymagają słowa

| Barwa | na Kości Słoniowej | % K w mono (100 − L) |
|---|---|---|
| Szafir Nocny | 14,09:1 | 74 % |
| Ametyst Dworski | 13,41:1 | 72 % |
| Rubin Głęboki | 12,77:1 | 70 % |
| Zieleń Butelkowa | 12,06:1 | 70 % |

Rozpiętość: **2,03 punktu**. Rubin i Zieleń wypadają w mono identycznie (70 % K), więc
znak dziedziny Szkolenia i znak dziedziny Pożyczki są w druku jednokolorowym nieodróżnialne.
**Dziedziny nie wolno kodować samym kolorem** - wchodzi tint tła, słowo, albo oba.

**Korekta wobec dokumentu źródłowego:** `irn-design-paleta-kolorow.md` podaje, że cztery barwy
nośne różnią się „o mniej niż 2 punkty". Przeliczenie daje **2,03**, czyli o 0,03
punktu więcej - twierdzenie w tej formie jest nieprawdziwe. Reguła, którą uzasadniało, zostaje
w mocy i ma mocniejszą podstawę: równość w mono (70 % wobec 70 %), nie bliskość kontrastu.

## Pary zabronione i zamienniki

| Para | Kontrast | Próg | Zamiast tego |
|---|---|---|---|
| Złoto Szampańskie na Kości Słoniowej | **1,80:1** | 3:1 grafika | linia, tłoczenie albo wypełnienie z etykietą Atramentem (9,99:1) |
| Grafit Jedwabny na Aksamicie Nocy | **3,17:1** | 4,5:1 tekst | Alabaster (14,62:1) |
| Bursztyn Wyciszony na Aksamicie Nocy | **3,68:1** | 4,5:1 tekst | wypełnienie z etykietą Kością Słoniową |
| Złoto Antyczne na Aksamicie Nocy | **3,46:1** | 4,5:1 tekst | Złoto Szampańskie (9,58:1) |
| Bursztyn Wyciszony na Alabastrze | **3,98:1** | 4,5:1 tekst | Kość Słoniowa jako tło (4,69:1) |

**Korekta wobec dokumentu źródłowego, druga.** `irn-design-paleta-kolorow.md` i rozdział
„Dark mode" brandbooka podają dla Złota Antycznego na Aksamicie Nocy **3,94:1**. Przeliczenie daje
**3,46:1**. Przyczyna wskazana: 3,94 to kontrast **poprzedniej** wartości
Złota Antycznego `#7E7053`, sprzed pociemnienia do `#75674B` - ta sama liczba odtwarza się co do
setnej na starym hexie. Tabela par zabronionych nie została przeliczona po zmianie. Wyrok się nie
zmienia (para zabroniona w obu rachunkach), zmienia się liczba.

## Etykieta na wypełnieniu - kolor przepisany, nie dobierany

| Wypełnienie | Kolor etykiety | Kontrast |
|---|---|---|
| Szafir Nocny `#132246` | Kość Słoniowa `#F7F3E9` | 14,09:1 |
| Rubin Głęboki `#541319` | Kość Słoniowa `#F7F3E9` | 12,77:1 |
| Zieleń Butelkowa `#0B3627` | Kość Słoniowa `#F7F3E9` | 12,06:1 |
| Ametyst Dworski `#331F41` | Kość Słoniowa `#F7F3E9` | 13,41:1 |
| Aksamit Nocy `#080F1F` | Kość Słoniowa `#F7F3E9` | 17,25:1 |
| Bursztyn Wyciszony `#9B5E30` | Kość Słoniowa `#F7F3E9` | 4,69:1 |
| Złoto Antyczne `#75674B` | Kość Słoniowa `#F7F3E9` | 4,99:1 |
| Lapis Stonowany `#305686` | Kość Słoniowa `#F7F3E9` | 6,77:1 |
| Grafit Jedwabny `#606369` | Kość Słoniowa `#F7F3E9` | 5,44:1 |
| Złoto Szampańskie `#C4B790` | Atrament `#07090C` | 9,99:1 |
| Alabaster `#E4E1D8` | Atrament `#07090C` | 15,25:1 |
| Muszla Różana `#E8D6D6` | Atrament `#07090C` | 14,26:1 |

## Kolor nigdy nie jest jedynym nośnikiem statusu

Każdy status w dokumencie IRIN **musi** mieć etykietę słowną albo ikonę obok koloru. To wymóg
dostępności (WCAG 1.4.1 „Użycie koloru"), nie preferencja - i w tej palecie ma dodatkową
podstawę: w mono Rubin i Zieleń schodzą do tej samej wartości 70 % K.

## Minimalna grubość linii

| Rodzaj linii | Kolor | Minimalna grubość |
|---|---|---|
| Niosąca strukturę: linia tabeli, obrys karty, obrys pola, rozdzielenie bloków | Grafit Jedwabny `#606369` | **0,25 mm** |
| Ozdobna: kreska pod nagłówkiem, kreska sygnatury, obramowanie dyplomu | Złoto Szampańskie `#C4B790` | **0,5 mm** |
| Siatka wykresu | Grafit Jedwabny, krycie obniżone | **0,15 mm** |

Grafit Jedwabny na Kości Słoniowej daje 5,44:1, na Alabastrze 4,61:1 - oba nad progiem 3:1. **Na Aksamicie Nocy Grafit nie wchodzi**
(3,17:1); linia na ciemnym idzie Alabastrem albo Złotem Szampańskim.

Widoczność tych grubości na papierze docelowym **nie jest zmierzona** - kontrast jest policzony,
druk nie. Falsyfikator: pierwszy wydruk.

## Wykresy - jedna barwa, cztery stopnie krycia

Dokument jednej dziedziny: **jedna barwa dziedziny, cztery stopnie krycia 100 / 72 / 50 / 30 %**.
Serie różni jasność, nie odcień, więc działają w mono i przy zaburzeniach widzenia barw.
Dokument przekrojowy: serie mogą być barwami dziedzin, bo wtedy barwa kategorii nie koduje,
tylko ją powtarza - warunek: każda oś podpisana słowem. Maksymalnie cztery serie, oś Y od zera.

**Dlaczego nie paleta serii.** Sprawdzone walidatorem palet kategorialnych na palecie poprzedniej:
nasycenie każdej barwy leżało poniżej podłogi 0,10 w OKLCH, więc barwy czytały się jako szarości.
Regalia jest palettą jeszcze ciemniejszą i zwartą kontrastowo (cztery barwy nośne w rozpiętości
2,03 punktu), więc ten sam wniosek obowiązuje: **tożsamość serii nie może opierać się
na barwie**. Stopnie krycia jednej barwy rozwiązują to bez rozszerzania palety.

## Mapa tokenów

| Token | Barwa | Token | Barwa |
|---|---|---|---|
| `--irin-primary` | Szafir Nocny | `--irin-surface` | Kość Słoniowa |
| `--irin-surface-alt` | Alabaster | `--irin-surface-dark` | Aksamit Nocy |
| `--irin-text` | Atrament | `--irin-text-invert` | Kość Słoniowa |
| `--irin-text-muted` | Grafit Jedwabny | `--irin-border` | Grafit Jedwabny |
| `--irin-accent` | Złoto Szampańskie | `--irin-link` | Lapis Stonowany |
| `--irin-success` | Zieleń Butelkowa | `--irin-warning` | Bursztyn Wyciszony |
| `--irin-info` | Złoto Antyczne | `--irin-highlight` | Muszla Różana |

Barwa dziedziny wchodzi tokenem ustawianym na poziomie dokumentu, nie tokenem semantycznym.
Rubin Głęboki i Ametyst Dworski nie mają tokenu semantycznego.

**Trzy kolizje ról - rozwiązane decyzją z 2026-09-06.** Bursztyn Wyciszony miał być jednocześnie
ostrzeżeniem i barwą obszaru Akademia AI, Zieleń Butelkowa statusem pozytywnym i barwą obszaru
Pożyczki UE/BGK, a Rubin Głęboki oznaczeniem zakazu i barwą obszaru Szkolenia zawodowe. Decyzja
właściciela o wyjęciu obszarów z materiałów usuwa przyczynę: **tokenów `success`, `warning` i `error`
w Regalii nie ma.** Przypisanie roli statusu do barwy będącej kandydatem na obszar zabetonowałoby
to, co ma pozostać wymienne. **Status niesie słowo plus jedną z barw nośnych dobraną w dokumencie**,
nie token o nazwie roli - a wymóg etykiety słownej obok barwy i tak obowiązuje bezwarunkowo.

**Gniazdo obszaru.** Warstwa 15 % wchodzi przez dwa tokeny: `--irin-r-dziedzina` i
`--irin-r-tint-dziedzina`, domyślnie wskazujące na Szafir Nocny i jego tint. Materiał bez obszaru
wychodzi poprawnie bez żadnej podmiany; materiał obszarowy nadpisuje te dwa tokeny i nic więcej.

## Czego ta specyfikacja nie rozstrzyga

Kontrastów na tłach spoza palety: na kolorowym zdjęciu, na skanie, na papierze innym niż biały
maszynowy. Tam liczy się od nowa, nie przenosi tych liczb. Jeżeli na obrazie ma stanąć znak,
wchodzi plama neutralna z palety i mierzy się wobec niej.

## Do potwierdzenia

| # | Pozycja | Status | Falsyfikator |
|---|---|---|---|
| 01 | Rozbicia CMYK | bez proofu | proof cyfrowy na papierze docelowym |
| 02 | Złoto Szampańskie na papierze niepowlekanym | L* 78 przy 83 % krycia może zniknąć w tle | pierwszy wydruk dyplomu |
| 03 | Przypisanie barw do obszarów: Rubin → Szkolenia, Zieleń → Pożyczki, Bursztyn → Akademia AI | **zatwierdzone 2026-09-06 jako domyśl**, ale **nieużywane w żadnym materiale** - patrz wiersz 04 | pierwszy materiał, w którym warstwa obszarów zostanie włączona |
| 04 | Obszary działalności w materiałach | **rozstrzygnięte 2026-09-06: obszary wychodzą z materiałów.** Właściciel: „na razie czysty brandbook bez obszarów, które będą wymienne". Każdy nośnik ma jeden wariant neutralny; warstwa obszaru to jedno gniazdo `--irin-r-dziedzina` plus `--irin-r-tint-dziedzina`, domyślnie wskazujące na Szafir Nocny | decyzja właściciela o włączeniu warstwy obszarów |
| 05 | Trzy kolizje ról tokenów (Bursztyn, Zieleń, Rubin) | świadome obciążenie | pierwszy materiał, w którym rola i dziedzina wystąpią razem |
| 06 | Widoczność linii 0,25 i 0,5 mm | kontrast policzony, druk nie | pierwszy wydruk na papierze docelowym |

**Falsyfikator całej tej specyfikacji:** ponowne przeliczenie wzorem WCAG 2.1 na
`tokeny/palette-irin.json` dające inną wartość niż w tabelach wyżej.
