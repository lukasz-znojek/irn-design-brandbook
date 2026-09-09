# Typografia IRIN - specyfikacja obowiązująca

**Status: ZATWIERDZONA.** Skala ma **11** poziomów, od Display 72 px do podłogi składu 8,5 px.

Dane maszynowe: [`tokeny/palette-irin.json`](./tokeny/palette-irin.json), klucz `typografia`. Kolor: [`paleta-barw.md`](./paleta-barw.md). Siatka: [`siatka-a4.md`](./siatka-a4.md). Logotyp: [`logotyp.md`](./logotyp.md).

**Ten plik jest wywiedziony, nie źródłowy.** Wartości pochodzą z [`tokeny/palette-irin.json`](./tokeny/palette-irin.json) i to nie jest miejsce, w którym się je zmienia: zmiana idzie przez [`../../_robocze/narzedzia/zloz-palete.py`](../../_robocze/narzedzia/zloz-palete.py), a potem przez bramki `sprawdz-palete.py` i `sprawdz-zgodnosc-md.py`.

## Kroje

- **Manrope**, wagi 200-800 (200, 300, 400, 500, 600, 700, 800) - krój podstawowy. Nagłówki, korpus, etykiety, liczby prowadzące.
- **Inconsolata**, wagi 300-700 (300, 400, 500, 600, 700) - krój pomocniczy. Wyłącznie dane liczbowe, kody usług, numery dokumentów i metadane.

Licencja: **SIL Open Font License 1.1**. Wymóg dystrybucji: tekst licencji podróżuje z fontem, jako `_robocze/ds-bundle/fonts/OFL.txt` obok osadzonych plików woff2. Oba kroje są zmienne (variable), czyli jeden plik niesie całą oś wagi, a nie osobny plik na wagę.

## Zasada systemu

Hierarchię buduje waga jednego kroju, nie zmiana rodziny. Manrope na wszystko, Inconsolata wyłącznie na liczby, kody usług i metadane. Trzeciego kroju nie ma.

Jedna rodzina znosi ryzyko niedopasowania metryk przy tłumaczeniach i przy przelewaniu tekstu; trzeci krój wprowadza to ryzyko z powrotem i nie daje nic w zamian.

## Skala obowiązująca

Jedenaście poziomów. Stopnie podane w pikselach (zapis źródłowy) i w punktach (przeliczenie 72/96 dla druku) - **przeliczenie jest w jednym miejscu, w danych maszynowych, nie poziom po poziomie w składzie.**

| Poziom | Krój | Waga | Stopień px | Stopień pt | Interlinia | Tracking | Rola |
|---|---|---|---|---|---|---|---|
| Display | Manrope | 200 | 72 px | 54,00 pt | 0,92 | -0,03em | okładka |
| H1 | Manrope | 300 | 40 px | 30,00 pt | 1,0 | -0,02em | rozdział |
| H2 | Manrope | 600 | 24 px | 18,00 pt | 1,1 | -0,01em | sekcja |
| H3 | Manrope | 600 | 16 px | 12,00 pt | 1,3 | - | podsekcja |
| Lead | Manrope | 500 | 16 px | 12,00 pt | 1,4 | - | lead akapitu |
| Korpus | Manrope | 400 | 13,5 px | 10,13 pt | 1,55 | - | korpus |
| Meta | Manrope | 400 | 10 px | 7,50 pt | 1,5 | - | przypis, metadane |
| Kicker | Manrope | 700 | 14 px | 10,50 pt | 1,2 | 0,22em, wersaliki | drogowskaz sekcji |
| Liczba prowadząca | Manrope | 800 | 52 px | 39,00 pt | 0,95 | -0,02em | liczba prowadząca |
| Dane | Inconsolata | 300-700 | 10,5 px | 7,88 pt | 1,5 | - | Inconsolata: dane, kody, metadane |
| Techniczny | Inconsolata | 300-700 | 8,5 px | 6,38 pt | 1,4 | - | podłoga składu: nagłówki tabel, przypisy, pas nadawcy |

Tracking jest ujemny na display i nagłówkach, dodatni na wersalikach. Waga Inconsolaty nie jest przypisana do poziomu: dobiera się ją w zakresie 300-700 do gęstości tabeli.

**H3 i Lead mają ten sam stopień (16 px) i różnią się wyłącznie wagą (600 wobec 500).** Dlatego nie stawia się ich bezpośrednio obok siebie. Kiedy podsekcja musi sąsiadować z leadem, wchodzi Kicker (700 / 14 px / wersaliki), bo różni się także stopniem i trackingiem.

## Podłoga składu: 8,5 px = 6,38 pt

To reguła, nie tylko ostatni wiersz tabeli.

Rachunek: 8,5 × 72/96 = 6,375 pt, w zapisie dwumiejscowym **6,38 pt** (i 2,25 mm).

Strona projektowa zapisuje `6,4 pt` - to ta sama liczba do jednego miejsca po przecinku. W repozytorium obowiązuje zapis dwumiejscowy.

Nic mniejszego nie wchodzi do składu. Adnotacje rysunku w makietach w skali są wyjątkiem i muszą być tak opisane w kodzie.

Najmniejszy poziom skali ma 8,5 px, czyli dokładnie tyle, ile podłoga - bramka pomiarowa sprawdza tę nierówność przy każdym złożeniu palety, więc poziom poniżej podłogi nie wejdzie do specyfikacji niezauważony.

## Interlinia korpusu a jednostka odstępu 6 mm

Pełny rachunek, bo to miejsce, w którym łatwo pomylić się dwa razy pod rząd:

1. interlinia korpusu: 13,5 × 1,55 = 20,925 px = **5,5364 mm** (w tabelach zaokrąglane do 5,54 mm);
2. jednostka odstępu: 6 mm = 22,68 px;
3. różnica na linię: 6 - 5,5364 = **0,4636 mm** (w tabelach zaokrąglane do 0,46 mm);
4. ile linii wchodzi w pole treści: 251 / 5,5364 = 45,34, czyli **45 linii**;
5. dryf na pełnej kolumnie: 45 × 0,4636 = **20,86 mm**.

**Mnożenie zaokrąglonej różnicy jest pułapką:** 45 × 0,46 daje 20,70 mm, czyli o 0,16 mm mniej. Mnoży się wartość dokładną, zaokrągla się dopiero wynik.

Ta liczba **obala 19 mm**, którą ten plik podawał wcześniej: 19 to dryf na 41 jednostkach siatki, nie na 45 liniach tekstu, czyli pomiar nie tego, co się liczy. **Nie obala** natomiast rozstrzygnięcia, że 6 mm jest jednostką odstępu, a nie siatką linii bazowych - poprawiona liczba jest większa, więc wniosek stoi mocniej niż przedtem.

Konsekwencja praktyczna: odstępy między blokami wymierza się jednostką 6 mm, a tekst wewnątrz bloku zostaje przy własnej interlinii. Pogoń za wyrównaniem akapitów do jednostki kończy się rozstrzelonymi odstępami między blokami.

## Alfabet polski - pokrycie zmierzone

Znaki: ĄĆĘŁŃÓŚŹŻ ąćęłńóśźż.

| Krój | Pokrycie |
|---|---|
| Manrope | **18/18** |
| Inconsolata | **18/18** |

Metoda: cmap rozpakowanych woff2, kontur sprawdzony BoundsPen; oba kroje zmienne, więc pokrycie nie może różnić się między wagami.

**Co pozostaje niepotwierdzone:** czytelność ogonków na wydruku przy stopniu podłogi - falsyfikator otwarty. Pokrycie glifu w foncie i czytelność ogonka na papierze to dwa różne twierdzenia; pierwsze jest zmierzone, drugie czeka na wydruk.

### Jak ten pomiar zrobiono

Narzędzie: `_robocze/narzedzia/pokrycie-diakrytykow.py`, uruchomione na
`_robocze/ds-bundle/fonts/fonts.css`, czyli na paczce z fontami osadzonymi jako
data URI. Pomiar powtarza się jednym poleceniem po każdej zmianie tego pliku.

| Krój | Podzbiory | Oś `wght` w pliku | Pokrycie | Puste glify |
|---|---|---|---|---|
| Manrope | 2 pliki (`latin`, `latin-ext`), razem 39 816 B | 200-800 | **18/18** | brak |
| Inconsolata | 2 pliki (`latin`, `latin-ext`), razem 54 576 B | 200-900, CSS udostępnia 300-700 | **18/18** | brak |

Trzy wnioski, każdy z własnym zakresem:

1. **Podstawienie z innego kroju jest w tej paczce niemożliwe.** Każdy z osiemnastu
   znaków ma odwzorowanie w tablicy `cmap` i realny kontur, więc przeglądarka nie ma
   powodu sięgać po krój zastępczy.
2. **Glify nie mogą różnić się między wagami.** Oba kroje są zmienne, z ciągłą osią
   `wght` i jednym plikiem na podzbiór - nie istnieje osobny plik dla wagi 500,
   w którym mogłoby czegoś brakować. Pytanie „czy komplet diakrytyków jest w każdej
   wadze" przestaje być dla tej paczki pytaniem empirycznym.
3. **Ó i ó siedzą w podzbiorze `latin`, pozostałe szesnaście w `latin-ext`.** Żaden
   pojedynczy plik nie ma kompletu i tak ma być - przeglądarka składa je po
   `unicode-range`. Kto zmierzy jeden plik osobno, zobaczy „brakuje 16 znaków"
   i wyciągnie fałszywy wniosek.

Zapis pochodzi z odczytu 2026-09-06 i wchodzi tu przy scaleniu gałęzi
`claude/etap-2-regulamin-bur`.
