# Arkusz wzorcowy IRIN (.xlsx)

**Ryzyko przed opisem: tego pliku nie otwarto w Excelu ani w LibreOffice Calc.** W tym kontenerze
LibreOffice nie ma żadnego modułu aplikacyjnego - `ls /usr/lib/libreoffice/share/registry/` pokazuje
wyłącznie `main.xcd`, `Langpack-en-US.xcd`, `lingucomponent.xcd`, `pdfimport.xcd` i `xsltfilter.xcd`,
bez `calc.xcd`, `writer.xcd`, `impress.xcd` i `draw.xcd`. Weryfikacja poniżej to **odczyt OOXML
wprost z archiwum** plus odczyt zwrotny przez openpyxl. Falsyfikator: otwarcie w Excelu
z zainstalowanym Manrope.

Trzy arkusze:

| Arkusz | Co zawiera |
|---|---|
| `Tabela` | wzorcowa tabela: nagłówek, dziesięć wierszy z pasami, wiersz sumy, legenda rodzajów pól |
| `Wykresy` | blok danych i pięć wykresów: słupki grupowane, skumulowane, poziome, linie, jedna seria |
| `Legenda` | każda użyta barwa z hexem, kontrastem i rolą; stopnie serii; sześć zasad z warstwy 1 |

Liczby w tabeli i na wykresach są **wypełnieniem przykładowym, nie danymi IRIN** - napisane jest
to w arkuszu, nie tylko tutaj. Pola treściowe zostają placeholderami w nawiasach kwadratowych.

## Jak to odtworzyć

```
python3 -m pip install openpyxl
TOKENY=../../01-baza-wiedzy/identyfikacja/tokeny/palette-irin.json \
WYNIK=$PWD/arkusz-irin.xlsx python3 buduj-arkusz.py
```

Generator **czyta stopnie serii z `palette-irin.json`**, nie ma ich wpisanych. Zmiana palety
w warstwie 1 zmienia wykresy przy najbliższym przebiegu.

## Barwy i skąd pochodzą

| Element | Barwa | Kontrast | Źródło roli |
|---|---|---|---|
| Nagłówek tabeli | Szafir Nocny `#132246`, tekst Kość Słoniowa | 14,09:1 | „kolor marki, pasy nagłówkowe" |
| Pas nieparzysty | Kość Słoniowa `#F7F3E9` | Atrament 17,99:1 | „tło strony" |
| Pas parzysty | Alabaster `#E4E1D8` | Atrament 15,25:1, Grafit 4,61:1 | „tła kart" |
| Pole do wpisania | Muszla Różana `#E8D6D6` | Atrament 14,26:1 | „cytaty, podświetlenia" |
| Ramka pola do wpisania | Lapis Stonowany `#305686` | 6,77:1 na Kości Słoniowej | „stan aktywny" |
| Tekst drugorzędny i linie | Grafit Jedwabny `#606369` | 5,44 / 4,61:1 | „tekst drugorzędny na jasnym, linie" |
| Obrys serii wykresu | Atrament `#07090C`, 0,25 mm | 17,99:1 do tła | „linia niosąca strukturę" |

Wszystkie kontrasty policzone wzorem WCAG 2.1 w tej sesji. Pełne macierze:
`01-baza-wiedzy/identyfikacja/paleta-barw.md`, sekcje „Jasne tła nie są wymienne"
i „Wykresy - jedna barwa, cztery stopnie krycia".

## Para pasów wierszy - wybór ma koszt

Użyta jest **Kość Słoniowa + Alabaster**: kontrast pasów 1,180:1, ΔL* 6,36. To rekomendacja,
nie decyzja właściciela - czeka w `PLAN.md`, zadanie S5. Powód wyboru: to jedyna para w Regalii,
przy której **Grafit Jedwabny utrzymuje AA** na obu pasach (5,44 i 4,61:1). Para cichsza
(Alabaster + tint 12 %, ΔL* 2,46) spycha Grafit do 4,31:1, czyli poniżej progu.

Zmiana to jedna stała w generatorze: `ALABASTER` w wyrażeniu `pas = KOSC if k % 2 == 0 else ALABASTER`.

## Rodzaje pól - każdy ma sygnał nie-kolorowy

`paleta-barw.md` wymaga, żeby kolor nigdy nie był jedynym nośnikiem (WCAG 1.4.1). Cztery rodzaje:

| Rodzaj | Kolor | Sygnał nie-kolorowy |
|---|---|---|
| do wpisania | Muszla Różana | ramka Lapis Stonowany po bokach, komórka odblokowana |
| policzone formułą | brak własnego tła | kursywa, Grafit Jedwabny, formuła widoczna, komórka zablokowana |
| stałe, tylko do czytania | brak własnego tła | pismo proste Atramentem, komórka zablokowana |
| suma | Alabaster | linia górna Grafitem 0,25 mm, pismo pogrubione |

## Co zmierzono w pliku

Odczyt z rozpakowanego archiwum (`unzip -q arkusz-irin.xlsx -d rozp-x`):

| Sprawdzenie | Wynik |
|---|---|
| Formuły brutto | `G7 = E7*(1+F7)` … `G16` - kolumny zgodne z nagłówkami |
| Sumy | `E17 = SUM(E7:E16)`, `G17 = SUM(G7:G16)` |
| Barwy własne w `styles.xml` | dziesięć, wszystkie z kanałem alfa `FF` |
| Kroje w pliku | Manrope i Inconsolata (plus `Calibri` w stylu zero, którego openpyxl nie da się usunąć) |
| Stopnie pisma | 7,5 / 10 / 18 pt, czyli przypis, korpus i H2 ze skali |
| Siatka arkusza | wyłączona na wszystkich trzech arkuszach (`showGridLines="0"`) |
| Blokada okna | `ySplit="6"`, czyli sam nagłówek, bez blokowania kolumny |
| Marginesy wydruku | 20,00 / 20,00 / 18,00 / 28,00 mm - dokładnie siatka A4 |
| Pięć wykresów | `chart1..5.xml`, każdy z `min val="0"` na osi wartości |
| Kategorie osi | `strRef` na wszystkich pięciu, więc Excel pokaże „Okres 1", nie „1" |
| Obrys serii | `<a:ln w="9000">` = 0,7087 pt = **0,25 mm**, kolor `07090C` |
| Linia serii na wykresie liniowym | `w="18000"` = **0,5 mm** |
| Wypełnienia serii | `132246`, `535D74`, `858A98`, `B3B4B8` - stopnie z `palette-irin.json` |
| Podpisy osi | „Okres" i „Wartość" na każdym wykresie |
| Polskie znaki | odczyt zwrotny openpyxl: **zero komórek** z pozbawionym diakrytyku słowem |

Wykres liniowy ma **trzy serie, nie cztery** - to nie przeoczenie. Linia nie ma wypełnienia,
więc obrys Atramentem nie ma czego obrysować, a stopień 30 % zostaje ze swoim 1,87:1 wobec tła,
poniżej progu 3:1 z WCAG 1.4.11. Tytuł wykresu mówi to wprost.

## Ograniczenia Excela

| Pozycja | Skutek |
|---|---|
| Brak Manrope u odbiorcy | Excel podstawi krój systemowy i cała skala się przesunie. Excel nie zna listy zastępczej jak CSS, więc nie da się tego zabezpieczyć w pliku |
| Wagi Manrope | Excel zna tylko regular i bold, tak samo jak Word; wagi 500 i 600 ze skali nie są dostępne |
| `openpyxl` i kanał alfa | przy podaniu sześciu znaków hex openpyxl dopisuje alfę `00`, czyli pełną przezroczystość. Generator prefiksuje wszystkie barwy funkcją `A()` na `FF` |
| Motyw Office w pliku | plik niesie domyślny motyw pakietu (`4F81BD`, `C0504D`, `9BBB59`, `8064A2`, `4BACC6`, `F79646`). To rusztowanie openpyxl, nie wybór projektowy, ale „kolory motywu" w interfejsie Excela pokażą tę szóstkę, nie paletę IRIN |
| Format liczb | `#,##0.00` renderuje się według ustawień regionalnych odbiorcy; na polskim Excelu daje `1 585,50`, na angielskim `1,585.50`. Wartość w pliku jest jedna, wygląd zależy od maszyny |
| Szerokość kolumn | Excel liczy ją w znakach domyślnego kroju, nie w milimetrach, więc siatka 25 mm nie przenosi się na arkusz i nie jest tu odwzorowana |
| Ochrona komórek | ustawiona (`locked`), ale **arkusz nie jest chroniony hasłem** - blokada zadziała po włączeniu ochrony arkusza w Excelu |

## Czego nie sprawdzono

| Pozycja | Falsyfikator |
|---|---|
| Wygląd w Excelu i w Calc | otwarcie pliku; brak modułu Calc w kontenerze |
| Czytelność pasów i stopni serii na wydruku | pierwszy wydruk na drukarce biurowej |
| Czy pięć wykresów mieści się bez nachodzenia | Excel pozycjonuje je od zakotwiczeń `H6`, `H24`, `R6`, `R24`, `H42`; wysokość 8,5 cm i szerokość 15,5 cm są ustawione, ale nakładanie widać dopiero na ekranie |
| Zachowanie ochrony arkusza | włączenie ochrony i próba edycji pola zablokowanego |
