> **NIEAKTUALNE wobec palety obowiązującej - nie wysyłaj bez przepisania.**
> Ten plik niesie 8 wartości hex spoza palety Regalia, w tym barwy
> palet wycofanych v2 i v5.1. Powstał przed destylacją warstwy 1 z 2026-09-09.
> Obowiązujące wartości: [`../../01-baza-wiedzy/identyfikacja/paleta-barw.md`](../../01-baza-wiedzy/identyfikacja/paleta-barw.md).
> Oznaczone przy scaleniu gałęzi `claude/irin-visual-identity-vq9ddw`.

# Osiem szablonów uniwersalnych: instrukcja do kolejnego okna Claude Design

**Zastępuje TURĘ 1 z `szablony-uniwersalne-do-wyslania.md`.** Tamta powstała, zanim istniały księga
znaku i brandbook. Ta wersja odejmuje to, co już zrobione, i dokłada trzy rzeczy, których tamta
nie mogła znać.

---

## Część A: audyt, na którym stoi ta instrukcja

### Co sprawdziłem i czym

| Co | Pomiar | Wynik |
|---|---|---|
| Stan projektu | `DesignSync list_files` | 62 ścieżki; `guidelines/` ma **dziesięć** plików, `templates/` **jeden** - `papier-firmowy-wizytowka` |
| Czy nowe specyfikacje znaku istnieją | `list_files` | `guidelines/logotyp-wersje-kolorystyczne.md` i `guidelines/zasady-stosowania-znaku.md` - **oba są** |
| Czy szablony istnieją | `list_files` | **nie** - w `templates/` nie ma żadnego z ośmiu |
| Stopnie pisma w trzech gotowych plikach | skrypt liczący każde `font-size` wobec skali z `typografia.md` | poza skalą **56 %** użyć w brandbooku, **62 %** w księdze znaku, **60 %** w papierze |
| Kontrasty siedmiu wersji znaku | wzór WCAG 2.1, oba hexy obok wyniku | wszystkie przechodzą; najniższy to biel na Miedzi 6,53:1 |

### Trzy rzeczy zamknięte w ostatniej turze - nie ruszamy ich

1. **Stopka papieru mieści się w polu treści.** Poprzednia wersja miała `54mm 54mm 62mm` plus dwa
   guttery, czyli 178 mm w pojemniku 170 mm, i `overflow:hidden` obcinał 8 mm razem z NIP, REGON
   i telefonem. Teraz jest `repeat(4,1fr)` z gutterem 4 mm: (170 − 12) / 4 = **39,5 mm** na kolumnę.
   Domyka się.
2. **Znak nie jest już przebarwiany filtrem.** Poprzednia wersja miała łańcuch `filter:` celujący
   w Aksamit, a dający `#3D1922`. Teraz jest `fill: currentColor` plus `color:` - kolor podany
   wprost. `logotyp-wersje-kolorystyczne.md` zakazuje `filter:` jawnie.
3. **Siedem wersji kolorystycznych znaku jest rozstrzygnięte.** Nie jest już propozycją.

### Sprzeczność, którą znalazłem - i dokument, który ją rozstrzyga

**Dwie strony, oba pliki w projekcie, oba opisane jako zatwierdzone tego samego dnia:**

- `Brandbook IRIN.html`, rozdz. 02 „Kolor znaku" i rozdz. 04 „Czego się nie robi": „Znak jest
  jednokolorowy. Na ciemnym tle stosuje się wersję odwróconą, **nigdy przebarwioną na akcent
  dziedziny**." Czyli dwa kolory: Espresso i Pergamin.
- `Ksiega-znaku IRIN.html`, rozdz. 02 oraz `guidelines/logotyp-wersje-kolorystyczne.md`: **siedem**
  dopuszczonych kolorów, w tym trzy dziedzinowe, z regułą trzykrokową.

**Rozstrzyga `guidelines/logotyp-wersje-kolorystyczne.md`, bo mówi o tym wprost:** „Do 2026-09-03
obowiązywał zakaz »Nie zmieniamy koloru znaku.« - nowa decyzja **zawęża** ten zakaz do: »nie
zmieniamy koloru znaku poza siedem wersji z tej tabeli.«" To jest zapis decyzji, nie interpretacja.

**Wniosek: brandbook jest w tym jednym punkcie przedawniony.** Rozdziały 02 i 04 trzeba poprawić -
to osobne zadanie, nie część tej tury. Instrukcja niżej mówi projektantowi wprost, żeby na znaku
nie szedł za brandbookiem.

Do poprawienia w repozytorium, poza kanwą: `01-baza-wiedzy/identyfikacja/logotyp.md` nadal ma zakaz 1
w brzmieniu „Nie zmieniamy koloru znaku" bez odsyłacza do zawężenia.

### Czego draft instrukcji nie wiedział

| Luka | Skutek, gdyby została |
|---|---|
| Draft wymienia **trzy** nowe pliki, a jest **cztery**: brakuje `Brandbook IRIN.html` (17 rozdziałów) | Projektant nie wczyta największego z gotowych plików |
| Brandbook **już zawiera** „Papier firmowy - trzy dziedziny", „Wizytówka - cztery ujęcia", „Znak na sześciu tłach", „Stopka i sygnatura" | Kolejna tura zrobiłaby je po raz drugi |
| Draft nie mówi o sprzeczności brandbook / księga | Projektant przeczyta oba i zgadnie |
| Draft nie mówi, że **powiększenie sygnetu nie zostało wykonane** - w brandbooku rozdz. 15 i w pliku papieru nadal stoi 22 mm, choć prosiłeś dwa razy | Prośba przepadłaby po raz trzeci |
| Draft nie niesie pomiaru stopni pisma | Szablony powtórzą ten sam rozjazd |
| Draft nie mówi, że plik papieru ma trzy bloki o szerokościach spoza siatki | Szablony skopiują je z gotowego pliku |

### Stopnie pisma - pomiar rozdziela dwie różne sprawy

To nie jest jedna usterka, a dwie, i mają różne rozwiązania.

**Sprawa pierwsza: chybienia o kilka pikseli.** Wartości leżące blisko istniejącego poziomu skali,
ale nie na nim. Te są do poprawy od razu, bez żadnej decyzji:

| Użyte | Najbliższy poziom skali | Ile użyć w trzech plikach |
|---|---|---|
| 10,5 px | 10 px, przypis | 23 |
| 11 px | 10 px, przypis | 38 |
| 11,5 px | 10 px, przypis | 16 |
| 12 px | 13,5 px, korpus | 19 |
| 13 px | 13,5 px, korpus | 1 |
| 15 px | 14 px, kicker | 2 |
| 22 px | 24 px, H2 | 4 |
| 28, 32, 36, 44, 48, 68 px | 24, 40 albo 52 px | 10 |

**Sprawa druga: brak poziomów poniżej podłogi.** Najmniejszy poziom skali to Manrope 10 px, czyli
2,65 mm i 7,5 pt. Poniżej nie ma nic, a stopka, blok metryk i wizytówka tego potrzebują. Użyte
wartości poniżej podłogi: 9,5 px (7,13 pt), 9 px (6,75 pt), 8,5 px (6,38 pt), 8 px (6,00 pt),
7,5 px (5,63 pt). **To jest luka specyfikacji, nie błąd projektanta** - i zamyka ją decyzja
właściciela, nie kolejna tura.

**Jedna wartość jest osobno i jest defektem:** brandbook używa gdzieś **4,5 px, czyli 1,19 mm
i 3,38 pt**, oraz 5,5 px (4,13 pt). Poniżej 5,4 pt pismo przestaje się czytać po druku. To do
poprawy w brandbooku niezależnie od decyzji o skali.

### Trzy szerokości w pliku papieru, których nie wolno kopiować do szablonów

Szerokość n kolumn liczy się jako 29n − 4, czyli **25, 54, 83, 112, 141, 170 mm**. Plik papieru
ma trzy bloki obok tych wartości:

| Blok w `Papier firmowy i wizytowka.html` | Ma | Powinien mieć |
|---|---|---|
| `.hdr .logo` | 52 mm | **54 mm** (2 kolumny) |
| `.recipient` | 80 mm | **83 mm** (3 kolumny) |
| `.lead` `max-width` | 150 mm | **141 mm** (5 kolumn) albo 112 mm (4 kolumny) |

Różnice są po 2-9 mm, więc na oko niewidoczne - i właśnie dlatego wejdą do szablonów przez kopiowanie,
jeżeli tego nie napisać.

### Uwaga bez działania

`logotyp-wersje-kolorystyczne.md` podaje dla bieli i czerni próg **4,5:1**, a system używa **3:1**
dla grafiki znaczącej. Próg jest więc surowszy, niż wymaga reszta systemu - i nikogo nie ogranicza,
bo najniższa zmierzona wartość to biel na Miedzi **6,53:1**. Zostawiam bez zmiany; zapisuję tylko,
żeby ktoś tego później nie „poprawił" w dół, myśląc że to pomyłka.

---

## ——— POCZĄTEK TEKSTU DO WKLEJENIA ———

Kontynuujemy pracę nad systemem projektowym IRIN. Poprzednia tura domknęła **księgę znaku
i brandbook** - teraz robimy osiem szablonów uniwersalnych.

### Co jest już zrobione - do wczytania, nie do przerabiania

**Cztery pliki z ostatniej tury, wszystkie zatwierdzone 2026-09-03:**

1. **`Brandbook IRIN.html`** - 19-stronicowy brandbook, 17 rozdziałów: fundamenty, znak (trzy
   warianty, minimum i przestrzeń ochronna, czego się nie robi), kolor (Kaszmir Wyciszony,
   proporcja i etykiety), krój (Manrope i Inconsolata, wagi i polski alfabet), siatka (A4 pion,
   jednostka 6 mm), osiem zasad użycia, zastosowania (papier firmowy i wizytówka), warianty
   (znak na sześciu tłach, papier w trzech dziedzinach, wizytówka w czterech ujęciach, stopka
   i sygnatura), kolofon.
2. **`Ksiega-znaku IRIN.html`** - 11-stronicowa księga znaku: okładka, spis, siedem rozdziałów
   (konstrukcja, siedem wersji kolorystycznych, przestrzeń ochronna i minima, matryca teł,
   współistnienie, kolor dziedziny i 80/15/5, dwanaście antywzorców).
3. **`guidelines/logotyp-wersje-kolorystyczne.md`** - specyfikacja siedmiu dopuszczonych wersji
   znaku i reguła trzykrokowa doboru.
4. **`guidelines/zasady-stosowania-znaku.md`** - cztery reguły ramowe, matryca teł,
   współistnienie, dwanaście antywzorców.

**Kontekst obowiązujący, do czytania:** `guidelines/paleta-barw.md`, `guidelines/siatka-a4.md`,
`guidelines/typografia.md`, `guidelines/logotyp.md`, `guidelines/zasady-uzycia.md`,
`guidelines/papier-firmowy.md`, `guidelines/kontekst-firmy.md`, `tokens/palette-irin.json`,
`README.md`. Pełny brief właściciela: `uploads/szablonyuniwersalnedowyslania.md`.

**Czego NIE robimy po raz drugi.** Brandbook zawiera już znak na sześciu tłach, papier firmowy
w trzech dziedzinach, wizytówkę w czterech ujęciach oraz stopkę i sygnaturę. Te cztery rzeczy są
gotowe - nie powtarzaj ich jako artboardów.

### Jedna sprzeczność między gotowymi plikami - i jak ją rozstrzygamy

Brandbook w rozdziałach 02 i 04 mówi, że znak ma dwa kolory (Espresso na jasnym, Pergamin na
ciemnym) i że przebarwienie na akcent dziedziny jest zakazane. Księga znaku i
`logotyp-wersje-kolorystyczne.md` mówią, że dopuszczonych wersji jest **siedem**, w tym trzy
dziedzinowe.

**Rozstrzyga `logotyp-wersje-kolorystyczne.md`** - zapisano tam wprost, że decyzja z 2026-09-03
zawęża dawny zakaz do „nie zmieniamy koloru znaku poza siedem wersji z tej tabeli". Brandbook jest
w tym jednym punkcie przedawniony i będzie poprawiony osobno.

**Dla Ciebie znaczy to jedno: w sprawie koloru znaku idź za księgą znaku, nie za brandbookiem.**
Siedem wersji: Espresso `#221A15`, Pergamin `#E7DFD2`, Aksamit `#452430`, Miedź `#7A5638`,
Onyks `#33474F`, biel czysta `#FFFFFF`, czerń czysta `#000000`. Dobór regułą trzykrokową: kanał
druku, potem jasność tła, potem dziedzina. Wątpliwość rozstrzyga się na korzyść Espresso.

### Co robimy w tej turze

Osiem szablonów jako `templates/<slug>/<Slug>.dc.html`, każdy z
`<helmet><script src="./ds-base.js"></script></helmet>` i z komentarzem
`<!-- @template name="…" description="…" -->` w pierwszej linii.

**Wszystko na placeholderach w [NAWIASACH KWADRATOWYCH].** Zero zmyślonych nazwisk, cen, numerów,
kodów usług, dat. Placeholdery realnej długości - jednowyrazowy nie pokaże, czy blok wytrzyma
prawdziwą treść. Nie odtwarzaj formatu kodu usługi BUR: jego struktura nie jest zdefiniowana
w żadnym źródle PARP, więc stoi `[NUMER IDENTYFIKACYJNY USŁUGI]`.

1. **`templates/karta-uslugi/`** - jednostronicowa karta usługi, produktu albo oferty. A4 pion.
   Pas nagłówka ze znakiem, kicker kategorii, tytuł, blok metryk (pary etykieta-wartość
   w Inconsolacie), kolumna tekstu, stopka firmowa.
2. **`templates/zaswiadczenie/`** - dokument z pieczęcią, **dwie odmiany na jednym artboardzie
   obok siebie**: kolumnowa (treść i metryki w jednej kolumnie, sygnatura na dole) oraz z panelem
   metryk (metryki w bloku kontrastowym, żeby zostały czytelne po kopii mono).
   **Nie wybieraj lepszej i nie sugeruj wyboru** - obie mają istnieć, bo reguła doboru zależy od
   kanału dystrybucji, a tej reguły jeszcze nie ma.
3. **`templates/tabela-danych/`** - tabela regulowana: harmonogram, ramowy program, efekty uczenia
   się, cennik. Nagłówek, wiersze, wiersz sumy wyróżniony, przypis. Tabela na tyle długa, żeby było
   widać przejście na drugą stronę: powtórzony nagłówek i oznaczenie kontynuacji.
4. **`templates/okladka/`** - okładka viewbooka, programu, raportu, oferty. Display, kicker,
   oznaczenie edycji `[EDYCJA RRRR/RRRR]`, znak, jedno pole na obraz albo płaską plamę koloru.
5. **`templates/katalog-uslug/`** - rozkładówka katalogowa, siatka kart na sześciu kolumnach.
   Minimum sześć kart, żeby było widać rytm i to, co się dzieje z kartą o dłuższym tytule.
6. **`templates/slajd-16-9/`** - slajd 16:9, **trzy odmiany na jednym artboardzie**: tytułowy,
   treściowy, tabelaryczny. Szczegóły o siatce niżej.
7. **`templates/notatka-wewnetrzna/`** - A4 pion, jedna strona, ton wewnętrzny. Jawne oznaczenie
   poziomu materiału (`SZKIC - KONSULTACJA WEWNĘTRZNA`), tytuł, treść, **brak pełnego bloku
   rejestrowego** - notatka nie jest pismem wychodzącym.
8. **`templates/zestaw-drobnych/`** - elementy powtarzające się w szablonach wyżej: plakietka
   statusu w czterech stanach (potwierdzony/Werdykt, wymaga uwagi/Rubryka, błąd i korekta/Karmin,
   informacja/Onyks - **każda z etykietą słowną obok koloru**), blok podpisu, blok metryk, blok
   kodu identyfikacyjnego, pieczęć w Złocie foliowym, pole placeholdera, oznaczenie poziomu
   materiału.

### Reguły twarde

**Siatka A4.** 210 × 297 mm, sześć kolumn, moduł 25 mm, gutter 4 mm, marginesy 18 mm góra,
20 mm lewy, 20 mm prawy, 28 mm dół, pole treści 170 × 251 mm. Szerokość n kolumn = 29n − 4, czyli
**25, 54, 83, 112, 141, 170 mm**. Krawędzie kolumn: lewe 20, 49, 78, 107, 136, 165 mm; prawe 45,
74, 103, 132, 161, 190 mm.

**Trzech szerokości z pliku papieru nie kopiuj.** `Papier firmowy i wizytowka.html` ma logo
w nagłówku 52 mm (powinno 54), blok adresata 80 mm (powinno 83) i kolumnę tekstu `max-width:150mm`
(powinno 141 albo 112). Różnice po 2-9 mm są niewidoczne na oko i właśnie dlatego przechodzą przez
kopiowanie. W szablonach użyj wartości z siatki.

**Sprawdź każdy blok rachunkiem, zanim oddasz artboard.** W pierwszej turze pilota stopka miała
178 mm w pojemniku 170 mm i `overflow:hidden` obcinał 8 mm razem z danymi rejestrowymi, bez
ostrzeżenia. Dziś jest naprawiona - `repeat(4,1fr)` daje 39,5 mm na kolumnę.

**Rytm pionowy.** Odstęp między blokami treści jest wielokrotnością 6 mm: 6, 12, 18, 24, 48.
Nie dotyczy wnętrza komponentu - światło pod linią, padding komórki i odstęp etykieta-wartość
dobierasz do stopnia pisma. Margines górny 18 mm jest strefą znaku i nagłówka, dolny 28 mm strefą
stopki; treść nie wchodzi do żadnej z nich, a tekst stopki nie schodzi bliżej niż 12 mm od krawędzi.

**Linie.** Strukturę prowadzisz Popiołem `#7D7466`, nie cieniej niż **0,25 mm**. Złoto foliowe
`#A8874E` jest wyłącznie kreską ozdobną, pieczęcią i sygnaturą, nie cieniej niż **0,5 mm**.
Podaj przy każdej użytej linii jej grubość i tło.

**Jeden kolor dziedziny na dokument.** Aksamit - Pedagogika, Miedź - Akademia AI,
Onyks - Pożyczki UE/BGK. Nigdy dwa naraz. Szablony buduj na Aksamicie, ale w jednym artboardzie
pokaż, że kolor dziedziny da się podmienić na Miedź i Onyks w **jednym miejscu**, nie w dziesięciu.

**Kolor nigdy nie jest jedynym nośnikiem statusu.** Po konwersji do skali szarości Werdykt,
Rubryka, Karmin i Onyks mają zbliżoną jasność, a osobny tryb monochromatyczny został odrzucony -
etykieta słowna albo ikona obok koloru jest jedynym zabezpieczeniem, nie jednym z dwóch.

**Trzy zakazy kontrastowe, każdy z liczbą:**

1. **Plakietka statusu nigdy na wypełnieniu koloru dziedziny.** Karmin na Aksamicie 1,83:1,
   na Miedzi 1,13:1, na Onyksie 1,32:1 - wszystkie poniżej progu 3:1. Plakietka stoi na papierze:
   Karmin na Kaszmirze 6,99:1, na Muślinie 6,63:1, na Pergaminie 5,60:1.
2. **Pieczęć w Złocie foliowym tylko na Aksamicie i na papierze.** Złoto na Aksamicie 4,03:1
   i na Kaszmirze 3,17:1 przechodzą. Na Onyksie 2,90:1, na Miedzi 1,94:1, na Pergaminie 2,55:1 -
   nie przechodzą. W dokumencie Akademii AI albo Pożyczek pieczęć potrzebuje innego tła.
3. **Rubryką nie pisze się tekstu na Pergaminie** (4,18:1 przy progu 4,5:1). Ostrzeżenie idzie
   wtedy Espresso z etykietą słowną, a Rubryka zostaje wypełnieniem plakietki.

**Etykieta na wypełnieniu jest przepisana, nie dobierana:** na Aksamicie Pergamin 10,26:1,
na Miedzi Pergamin 4,94:1, na Onyksie Pergamin 7,37:1, na Karminie Pergamin 5,60:1, na Werdykcie
Pergamin 6,62:1, na Rubryce biel 5,53:1, na Złocie Espresso 5,09:1.

**Typografia i jedna rzecz, którą trzeba zrobić inaczej niż dotąd.** Manrope na wszystko,
Inconsolata na liczby, kody i metadane. Hierarchię buduje waga jednego kroju - nie dobieraj
trzeciego. Skala obowiązująca, w pikselach: display 72 · H1 40 · H2 24 · H3 16 · lead 16 ·
korpus 13,5 · kicker 14 · przypis 10 · Inconsolata 10,5 · liczba prowadząca 52.

Zmierzyłem trzy gotowe pliki i **od 56 do 62 procent użyć stopnia pisma leży poza skalą**. To dwie
różne sprawy i mają różne rozwiązania:

- **Chybienia o kilka pikseli - te popraw od razu.** 10,5 · 11 · 11,5 px zamiast 10; 12 i 13 px
  zamiast 13,5; 15 px zamiast 14; 22 i 28 px zamiast 24; 36 i 44 px zamiast 40; 48 px zamiast 52;
  68 px zamiast 72. W szablonach użyj wartości ze skali, nie zaokrągleń.
- **Brak poziomów poniżej 7,5 pt - to luka specyfikacji, nie Twój błąd.** Najmniejszy poziom skali
  to 10 px, czyli 2,65 mm i 7,5 pt. Stopka, blok metryk i wizytówka potrzebują mniej. Zrób tak:
  **użyj stopni, jakie są potrzebne, i zwróć ich listę** - po jednej wartości na zastosowanie,
  z uzasadnieniem w jednym zdaniu. Nie dopisuj poziomów do skali sam. Jednego progu nie przekraczaj
  w dół: **1,9 mm to 5,4 pt i poniżej tego pismo przestaje się czytać po druku.**

**H3 różni się od leadu wyłącznie wagą** (600 wobec 500) przy tym samym stopniu 16 px, więc te dwa
poziomy nie stoją bezpośrednio obok siebie. Jeżeli muszą, wchodzi kicker. Pilot papieru firmowego
sprawdził to na realnej treści i wynik brzmiał: różnica jest widoczna, ale słaba - bez kickera
podsekcja czyta się jako kontynuacja leadu.

**Znak.** Wyłącznie pliki źródłowe: `assets/logo_irin_poziom.svg`, `logo_irin_pion.svg`,
`logo_irin_sygnet.svg`. Kolor: siedem wersji z księgi znaku, dobór regułą trzykrokową, ustawiany
**wprost wartością hex albo tokenem**, przez `color` kontenera i `fill: currentColor` na ścieżkach -
**nigdy przez `filter:`**. Minimum: pełny znak 18 mm w druku i 90 px na ekranie, sygnet samodzielny
10 mm i 44 px. Przestrzeń ochronna x = wysokość liter sygnetu, mierzona z każdej strony; miara
względna, nie stały margines strony.

W projekcie są dwa katalogi z tymi samymi trzema plikami: `assets/` i `uploads/`. Księga znaku
czyta z `assets/`, plik papieru z `uploads/`. **W szablonach używaj `assets/`** - jednego adresu,
konsekwentnie.

**Zakaz znaków instytucjonalnych.** Na żadnym materiale IRIN nie stawia się znaku Funduszy
Europejskich, znaku barw Rzeczypospolitej Polskiej ani flagi Unii Europejskiej. To zakaz, nie brak
obowiązku: IRIN jest doradcą zewnętrznym, nie beneficjentem. Nazwę programu wolno napisać w treści;
oznaczyć nim materiału - nie.

**Język.** Cała treść po polsku, w tym etykiety, nagłówki i mikrocopy.

### Slajd 16:9 - siatka nie istnieje i nie wolno jej wziąć na oko

`siatka-a4.md` obowiązuje wyłącznie na A4 pion i sam ten plik mówi, że inny format unieważnia całe
sprawdzenie. Zrób więc tak:

- **sześć kolumn zostaje** - to element tożsamości wspólny dla trzech dziedzin, nie parametr
  dobierany per format,
- moduł, gutter i marginesy **proponujesz Ty**, i podajesz **rachunek szerokości**: suma sześciu
  kolumn i pięciu gutterów musi równać się szerokości pola treści **co do jednostki**, tak jak
  na A4 pion domyka się 6 × 25 + 5 × 4 = 170 mm,
- **oznacz ten szablon jako propozycję** - siatkę slajdu zatwierdza właściciel, nie Ty.

### Jedna rzecz, o którą właściciel prosił dwa razy i nie została zrobiona

**Sygnet na rewersie wizytówki ma zostać powiększony.** Brandbook rozdz. 15 i
`Papier firmowy i wizytowka.html` nadal podają **22 mm**. Nie jest to zadanie tej tury, ale jeżeli
w szablonie „zestaw drobnych" albo gdziekolwiek indziej stawiasz sygnet samodzielnie, **podaj jego
zmierzoną szerokość w milimetrach** - to wchodzi do protokołu, a wartość na rewersie zostanie
poprawiona osobno.

### Pełny audyt glifów - ta tura może go zamknąć

Brandbook mówi wprost, że pełny audyt glifów Manrope zamyka „pierwszy realny dokument o dużym
pokryciu Manrope 500/600, w którym trafi się ź". Osiem szablonów jest tym dokumentem. Wstaw więc
w każdym szablonie zdanie testowe **w każdej użytej wadze, ze szczególną uwagą na 500 i 600**:

> Żółć, gęś, źdźbło, ćma, łódź, ńandu, świt, żółw: ĄĆĘŁŃÓŚŹŻ ąćęłńóśźż.

i **napisz w odpowiedzi, czy wszystkie 18 diakrytyków wyrenderowało się na wagach 500 i 600** -
w szczególności `ź` i `Ź`. To zamyka falsyfikator, który wisi od trzech tur.

### Forma wyniku

Osiem folderów `templates/<slug>/` z entry `<Slug>.dc.html` w PascalCase. Przy każdym szablonie
w odpowiedzi: jedno zdanie o tym, co w środku jest do podmiany.

Jeżeli którakolwiek reguła okazała się w praktyce niewykonalna, **napisz to jako uwagę w kodzie
i idź dalej - nie obchodź jej po cichu**.

Do zwrotu razem z szablonami:

1. Lista stopni pisma poniżej 7,5 pt, których faktycznie potrzebowałeś - po jednej wartości
   na zastosowanie, z uzasadnieniem w jednym zdaniu.
2. Propozycja siatki slajdu 16:9 z rachunkiem szerokości domykającym się co do jednostki.
3. Odpowiedź o diakrytykach na wagach 500 i 600, ze wskazaniem, czy `ź` i `Ź` się złożyły.
4. Lista elementów, które powtarzały się na tyle, że powinny zostać prymitywami w
   `components/prymitywy/`.

Zaczynaj bez pytań - wszystko powyżej jest ustalone.

## ——— KONIEC TEKSTU DO WKLEJENIA ———
