# Zestaw szablonów uniwersalnych: tekst gotowy do wklejenia w Claude Design

Ten plik istnieje z tego samego powodu co pozostałe `*-do-wyslania.md`: **Claude Design nie widzi
dysku właściciela**, więc każda ścieżka lokalna jest tam martwym adresem, który może zostać wzięty
za zadanie do wykonania.

**Inaczej niż zlecenie pilota, ten plik nie ma osobnej wersji projektowej.** Powód: nie zamawia
konkretnego dokumentu, więc nie ma treści merytorycznej, którą trzeba by trzymać w dwóch wersjach.
Notatka dla właściciela stoi w części A niżej, przed znacznikiem POCZĄTEK, i tam wolno jej mieć
ścieżki. Tekst do wklejenia jest za znacznikiem i ścieżek nie ma.

---

## Część A: notatka dla właściciela

### Skąd ta forma zlecenia

Polecenie z 2026-09-03: „narazie potrzebuję lekkich szablonów uniwersalnych, żeby dało się je
przygotować jako wzorce dla różnego rodzaju pierdoletów", „merytoryką będziemy się martwić później",
„niech już wszystko robi". Zlecenie jest więc zestawem **układów z miejscami na treść**, nie
zestawem dokumentów. Wszystko na placeholderach.

### Czego to zlecenie świadomie nie robi

| Czego nie ma | Dlaczego |
|---|---|
| List pól prawnie obowiązkowych z `01-baza-wiedzy/prawo/bur.md` i `kfs.md` | Merytoryka odłożona decyzją właściciela. Szablon ma mieć miejsce na te pola, nie ich treść. |
| Pięciu decyzji o certyfikacie (orientacja, dziedzina, sygnatura, numeracja, PESEL) | Szablon „dokument z pieczęcią" jest uniwersalny, więc żadnej z nich nie wymaga. Wracają, gdy zamawiamy konkretne zaświadczenie. |
| Danych rzeczywistej usługi, uczestnika, programu, ceny | Repozytorium ich nie zawiera i zakazuje zgadywania. Placeholdery w nawiasach kwadratowych. |
| Szablonu materiału aplikacji sprzedażowej jako osobnej pozycji | `01-baza-wiedzy/uslugi/aplikacje-sprzedazowe.md` nie zna platformy, stanu wdrożenia ani ekranów. Szablon „notatka wewnętrzna" i „zestaw drobnych" pokrywają to, co da się dziś zaprojektować. |

### Dwie luki w warstwie 1, które wykrył pomiar kontrastu w tej sesji

Obie policzone od nowa wzorem WCAG 2.1, oba hexy obok wyniku. **Do decyzji właściciela, czy wchodzą
do `01-baza-wiedzy/identyfikacja/paleta-barw.md` jako zapisane zakazy.** W briefie niżej stoją już
jako reguły, bo bez nich szablon „plakietka statusu" i „pieczęć" wyszedłby nieczytelny.

**Luka 1: plakietka statusu nie może stać na wypełnieniu koloru dziedziny.** `paleta-barw.md` tego
nie zakazuje, a zmierzone kontrasty są poniżej progu 3:1 dla grafiki we wszystkich trzech parach:

| Para | Hexy | Kontrast |
|---|---|---|
| Karmin na Aksamicie | `#9E2B2B` / `#452430` | **1,83:1** |
| Karmin na Miedzi | `#9E2B2B` / `#7A5638` | **1,13:1** |
| Karmin na Onyksie | `#9E2B2B` / `#33474F` | **1,32:1** |

**Luka 2: Złoto foliowe zawodzi nie tylko na Pergaminie.** `paleta-barw.md` zakazuje mu wyłącznie
tła Pergaminu (2,55:1). Pomiar pokazuje dwa dalsze tła poniżej progu 3:1:

| Para | Hexy | Kontrast |
|---|---|---|
| Złoto foliowe na Miedzi | `#A8874E` / `#7A5638` | **1,94:1** |
| Złoto foliowe na Onyksie | `#A8874E` / `#33474F` | **2,90:1** |
| Złoto foliowe na Aksamicie | `#A8874E` / `#452430` | 4,03:1, przechodzi |
| Złoto foliowe na Kaszmirze | `#A8874E` / `#FBF8F2` | 3,17:1, przechodzi |

To ma bezpośredni skutek dla szablonu z pieczęcią: **pieczęć w Złocie foliowym działa na Aksamicie
i na papierze, a nie działa na Miedzi ani na Onyksie.** Dokument dziedziny Akademia AI albo
Pożyczki UE/BGK potrzebuje pieczęci w innym kolorze albo na innym tle.

**Kontrola metody:** ten sam skrypt odtworzył co do setnej dziewięć wartości z tabel
w `paleta-barw.md` (Pergamin na trzech kolorach dziedziny 10,26 / 4,94 / 7,37; Popiół na trzech
tłach 4,34 / 4,12 / 3,48; Karmin na Kaszmirze 6,99; Espresso na Złocie 5,09; biel na Rubryce 5,53).

### Co po powrocie wyniku

Formularz pomiaru dla tego zlecenia nie powstaje - to nie dokument z falsyfikatorami, tylko zestaw
układów. Wracają za to trzy rzeczy do wpisania: lista stopni pisma poniżej 7,5 pt, których
projektant faktycznie potrzebuje (wejście do decyzji o rozszerzeniu `01-baza-wiedzy/identyfikacja/typografia.md`),
propozycja siatki dla slajdu 16:9 (piąta specyfikacja, do zatwierdzenia), i lista prymitywów,
które w praktyce powtarzały się w szablonach.
### Rozszerzenie listy - polecenie z 2026-09-03

Doszło sześć pozycji: pakiet znaku i faviconów, wersje kolorystyczne wizytówek z powiększonym
sygnetem, rozbudowany szablon prezentacji, arkusz z wykresami i paletą pól, szablony social media,
plus „pomyśl co jeszcze potrzebne na start".

**Zlecenie zostało podzielone na trzy tury wklejania, i to jest rekomendacja, nie wymóg.** Powód
do obalenia: jedna wiadomość zamawiająca około sześćdziesięciu artboardów da sześćdziesiąt płytkich.
Jeżeli wolisz wkleić wszystko naraz, brief na to pozwala - tury są rozdzielone znacznikami, nie
zależnościami.

| Tura | Co zamawia | Ile artboardów, orientacyjnie |
|---|---|---|
| 1 | osiem szablonów dokumentów A4 | 8 |
| 2 | znak, favicon, wizytówki, social media | 4 grupy, około 20 kadrów |
| 3 | prezentacja pełna, arkusz, wykresy, dodatki na start | około 30 slajdów plus 8 |

### Sprzeczność, którą trzeba nazwać: pozycja 1 wobec zakazu 1

**Polecenie:** „pakiet logo do użycia i faviconów w różnych kolorach".
**Zakaz 1 z `01-baza-wiedzy/identyfikacja/logotyp.md`**, zatwierdzony przez właściciela 2026-09-02:
„Nie zmieniamy koloru znaku. Ani sygnetu, ani wersji poziomej, ani pionowej. Znak jest
jednokolorowy; na ciemnym tle stosuje się wersję odwróconą, a nie przebarwioną."

Druga strona sprzeczności, niezależna od koloru: **favicon w 16 i 32 px stoi poniżej minimum
44 px** dla samodzielnego sygnetu z tabeli w `logotyp.md`. Favicon w ogóle nie mieści się
w obowiązującej specyfikacji, niezależnie od barwy.

**Rozstrzygnięcie w tym briefie:** pakiet dopuszczony (pozycja 9) idzie jako zlecenie, a wersje
kolorystyczne znaku i favicon (pozycja 10) jako **osobny artboard oznaczony jako propozycja,
z policzonym kontrastem każdej pary**. Decyzja o zmianie zakazu 1 należy do właściciela; brief jej
nie przesądza. Zmierzone, żeby decyzja miała liczby:

| Znak w kolorze | na Aksamicie | na Miedzi | na Onyksie | Próg 3:1 |
|---|---|---|---|---|
| Espresso `#221A15` (kolor źródłowy) | **1,26:1** | **2,62:1** | **1,76:1** | zawodzi wszędzie |
| Kaszmir `#FBF8F2` (wersja odwrócona) | 12,80:1 | 6,16:1 | 9,19:1 | przechodzi wszędzie |
| Pergamin `#E7DFD2` | 10,26:1 | 4,94:1 | 7,37:1 | przechodzi wszędzie |

Wniosek, który obowiązuje niezależnie od decyzji o kolorach: **na każdym z trzech kolorów dziedziny
wchodzi wersja odwrócona znaku, nie źródłowa.** To dotyczy wprost kolorowych wizytówek z pozycji 11.

### Pozycja 4 rozstrzygnięta pomiarem: paleta IRIN nie umie dać palety serii

Uruchomiony walidator palet kategorialnych na trzech wariantach zbudowanych z 14 kolorów IRIN,
tło Kaszmir `#FBF8F2`:

| Wariant | Skład | Wynik |
|---|---|---|
| A, kontrola negatywna | osiem kolorów nasyconych, łamie reguły IRIN | **FAIL** na 4 z 5 sprawdzeń |
| B, zgodny z regułami | tylko kolory nie zajęte przez dziedzinę ani status: Patyna, Złoto, Sepia, Popiół, Espresso | **FAIL** na 3 z 5 |
| C | trzy kolory dziedzin plus Złoto | **FAIL** na 3 z 5 |

**Przyczyna we wszystkich trzech jest ta sama i nie da się jej obejść doborem:** nasycenie każdego
koloru IRIN leży poniżej podłogi walidatora (od 0,016 do 0,085), czyli w wykresie wszystkie czytają
się jako odcienie szarości. To nie defekt palety - to skutek tego, że system nazywa się
**Kaszmir Wyciszony** i został celowo odsycony. Dwa dalsze ograniczenia dokładają się do tego:
kolory dziedzin są warstwą 15 % i obowiązuje jeden na dokument, a Werdykt, Rubryka i Karmin są
zarezerwowane dla statusów i nie wolno ich użyć jako „serii czwartej".

**Skutek: tożsamość serii na wykresie IRIN nie może opierać się na kolorze.** Brief zamawia więc
wykresy budowane na sekwencji jednego odcienia, małych wielokrotnościach, etykietach wprost przy
serii i fakturze - a nie na palecie ośmiu barw. **Do decyzji właściciela zostaje pytanie osobne:**
czy identyfikacja dostaje osobny, bardziej nasycony zestaw odcieni wyłącznie do wykresów, jako
piątą specyfikację. Bez tej decyzji kolorowych pulpitów nie da się zrobić poprawnie.

### Zmierzone wartości, na których stoi pozycja 4

**Pasy wierszy w tabeli:** Kaszmir `#FBF8F2` wobec Muślinu `#F6F2E9` daje **1,054:1** i mieści się
w zakresie używalnym dla zebry (około 1,03 - 1,12:1). Pergamin odpada: Kaszmir wobec Pergaminu
to **1,247:1**, czyli pas zaczyna się czytać jako dane, nie jako pomoc w czytaniu wiersza.

**Sekwencja dla wielkości, propozycja a nie specyfikacja** - odcienie Aksamitu mieszane z papierem
Kaszmir. Sekwencja ma własne kryteria przyjęcia, inne niż paleta kategorialna: jeden odcień,
jasność malejąca monotonicznie, różnica jasności między sąsiadami co najmniej 0,06 w OKLCH,
i jasny koniec co najmniej 2,0:1 na tle.

**Pierwsza wersja tej tabeli, wpisana w tej sesji, nie przechodziła i została wycofana:** jej jasny
koniec `#E5DFDB` dawał 1,25:1 wobec wymaganych 2,0:1. Poniżej wersja przeliczona i sprawdzona:

| Krok | Hex | OKLCH L | Kontrast na Kaszmirze | Różnica L do następnego |
|---|---|---|---|---|
| 1 | `#BBAEAE` | 0,762 | 2,03:1 | 0,107 |
| 2 | `#9E8B8F` | 0,655 | 3,03:1 | 0,110 |
| 3 | `#80696F` | 0,545 | 4,75:1 | 0,116 |
| 4 | `#634650` | 0,429 | 7,85:1 | 0,121 |
| 5 | `#452430` | 0,308 | 12,80:1 | - |

Trzy warunki spełnione: jasny koniec 2,03:1 przy progu 2,0; najmniejsza różnica jasności 0,107
przy progu 0,06; jasność malejąca na każdym kroku. Krok 1 nadal nie nadaje się pod tekst
ani pod cienką linię (2,03:1 to poniżej progu 3:1 dla grafiki) - działa jako wypełnienie
powierzchni z etykietą obok.


---

## ——— POCZĄTEK TURY 1 ———

Projektujesz **zestaw szablonów uniwersalnych** dla IRIN (Instytut Rozwoju i Nauki) - nie konkretne
dokumenty. Zadanie polega na przygotowaniu układów z miejscami na treść, z których da się potem
złożyć dowolny drobny dokument firmy: kartę usługi, zaświadczenie, harmonogram, okładkę, slajd,
notatkę. Treść merytoryczna i dane wejściowe przyjdą w kolejnych turach.

Specyfikacje, wobec których pracujesz, masz w projekcie: `siatka-a4.md`, `typografia.md`,
`paleta-barw.md`, `logotyp.md`, `zasady-uzycia.md`, dane maszynowe `tokens/palette-irin.json`
oraz kontekst firmy w `kontekst-firmy.md`. Wszystkie są zatwierdzone.

### Zasada nadrzędna: wszystko na placeholderach

**Zero zmyślonych danych.** Żadnych nazwisk uczestników, nazw szkoleń, numerów zaświadczeń, kodów
usług, cen, dat ani danych osób. Każde miejsce na treść dostaje placeholder w nawiasach
kwadratowych, nazwany tak, żeby było widać, co tam wejdzie: `[TYTUŁ USŁUGI]`,
`[NUMER IDENTYFIKACYJNY USŁUGI]`, `[IMIĘ I NAZWISKO]`, `[LICZBA GODZIN]`, `[DATA]`.

Placeholder ma być **realnej długości**, nie jednowyrazowy - inaczej szablon nie pokaże, czy blok
wytrzyma prawdziwą treść. Tam, gdzie potrzebny jest tekst ciągły, użyj neutralnego zdania po polsku
z pełnym zestawem diakrytyków, nie łaciny.

**Nie odtwarzaj formatu kodu usługi BUR.** Struktura tego numeru nie jest zdefiniowana w żadnym
źródle PARP, więc na wzorze stoi `[NUMER IDENTYFIKACYJNY USŁUGI]`, a nie wymyślony wzór cyfr.

### Osiem szablonów, każdy jako osobny artboard

Wszystkie na **A4 pion 210 × 297 mm**, poza szablonem 6. Każdy z przełącznikiem siatki.

**1. Karta jednostronicowa.** Dla: karta usługi, karta produktu, opis szkolenia, jednostronicowa
oferta. Strefy: pas nagłówka ze znakiem, kicker z nazwą kategorii, tytuł, blok metryk (pary
etykieta-wartość w Inconsolacie), treść w kolumnie tekstu, stopka firmowa.

**2. Dokument z pieczęcią - dwie odmiany na jednym artboardzie, obok siebie.** Dla: zaświadczenie,
certyfikat, potwierdzenie, podziękowanie.
- odmiana **kolumnowa**: treść i metryki w jednej kolumnie, sygnatura na dole
- odmiana **z panelem metryk**: metryki w bloku kontrastowym, żeby zostały czytelne po kopii
  czarno-białej

**Nie wybieraj lepszej i nie sugeruj wyboru.** Obie mają istnieć, bo reguła doboru zależy od kanału
dystrybucji, a tej reguły jeszcze nie ma. Kryterium będzie pomiarem: czy numer i kod zostają
czytelne po kopii mono.

**3. Tabela danych regulowanych.** Dla: harmonogram, ramowy program, lista efektów uczenia się,
cennik. Strefy: nagłówek tabeli, wiersze danych, wiersz sumy wyróżniony, przypis pod tabelą.
Pokaż tabelę na tyle długą, żeby było widać, co się dzieje przy przejściu na drugą stronę.

**4. Okładka.** Dla: viewbook, program, raport, oferta. Strefy: display, kicker, oznaczenie edycji
`[EDYCJA RRRR/RRRR]`, znak, jedno pole na obraz albo płaską plamę koloru.

**5. Rozkładówka katalogowa.** Dla: katalog usług, lista szkoleń. Siatka kart na sześciu kolumnach -
pokaż co najmniej sześć kart, żeby było widać rytm i to, co się dzieje z kartą o dłuższym tytule.

**6. Slajd 16:9 - trzy odmiany na jednym artboardzie.** Tytułowy, treściowy, tabelaryczny.

**Uwaga: siatka slajdu nie istnieje i nie wolno jej wziąć „na oko".** `siatka-a4.md` obowiązuje
wyłącznie na A4 pion i sama mówi, że inny format unieważnia całe sprawdzenie. Zrób więc tak:
- **sześć kolumn zostaje** - to element tożsamości wspólny dla trzech dziedzin, nie parametr
  dobierany per format
- moduł, gutter i marginesy **proponujesz Ty**, i podajesz **rachunek szerokości**: suma sześciu
  kolumn i pięciu gutterów musi równać się szerokości pola treści **co do milimetra**, tak jak
  na A4 pion domyka się 6 × 25 + 5 × 4 = 170 mm
- oznacz ten artboard jako **propozycję**; siatkę slajdu zatwierdza właściciel, nie Ty

**7. Notatka wewnętrzna.** A4 pion, jedna strona, ton wewnętrzny. Strefy: jawne oznaczenie poziomu
materiału (`SZKIC - KONSULTACJA WEWNĘTRZNA`), tytuł, treść, brak pełnego bloku rejestrowego -
notatka nie jest pismem wychodzącym.

**8. Zestaw drobnych, jeden artboard.** Elementy, które powtarzają się w szablonach wyżej i mają
mieć jedną postać:
- plakietka statusu w czterech stanach: potwierdzony (Werdykt), wymaga uwagi (Rubryka),
  błąd i korekta (Karmin), informacja (Onyks) - **każdy z etykietą słowną obok koloru**
- blok podpisu: kreska sygnatury plus `[IMIĘ I NAZWISKO]` i `[STANOWISKO]`
- blok metryk: trzy do pięciu par etykieta-wartość w Inconsolacie
- blok kodu identyfikacyjnego, wyróżniony, dla numerów dokumentów i usług
- pieczęć w Złocie foliowym
- pole placeholdera: obrys pola z etykietą, dla treści, której jeszcze nie ma
- oznaczenie poziomu materiału: `SZKIC`

### Reguły twarde - te obowiązują w każdym szablonie

**Siatka.** A4 pion 210 × 297 mm, sześć kolumn, moduł 25 mm, gutter 4 mm, marginesy 18 mm góra,
20 mm lewy, 20 mm prawy, 28 mm dół, pole treści 170 × 251 mm. Szerokość n kolumn liczy się jako
29n − 4, czyli **25, 54, 83, 112, 141, 170 mm** - blok, który nie ma jednej z tych szerokości,
wisi między kolumnami. Krawędzie kolumn: lewe 20, 49, 78, 107, 136, 165 mm; prawe 45, 74, 103,
132, 161, 190 mm.

**Sprawdź każdy blok tym rachunkiem, zanim oddasz artboard.** W pierwszej turze pilota stopka
strony pierwszej miała 178 mm w pojemniku 170 mm i `overflow:hidden` obcinał 8 mm razem z danymi
rejestrowymi - bez żadnego ostrzeżenia.

**Rytm pionowy.** Odstęp między blokami treści jest wielokrotnością 6 mm: dopuszczone 6, 12, 18,
24 i 48 mm. Nie dotyczy wnętrza komponentu - światło pod linią, padding komórki i odstęp
etykieta-wartość dobierasz do stopnia pisma. Margines górny 18 mm jest strefą znaku i nagłówka,
dolny 28 mm strefą stopki; treść nie wchodzi do żadnej z nich, a tekst stopki nie schodzi bliżej
niż 12 mm od krawędzi strony.

**Linie.** Linię niosącą strukturę - linia tabeli, obrys karty, obrys pola, rozdzielenie bloków -
prowadzisz Popiołem `#7D7466`, nie cieniej niż **0,25 mm**. Złoto foliowe `#A8874E` jest wyłącznie
kreską ozdobną, pieczęcią i sygnaturą, nie cieniej niż **0,5 mm**. Podaj przy każdej użytej linii
jej grubość i tło.

**Jeden kolor dziedziny na dokument.** Aksamit `#452430` to Pedagogika, Miedź `#7A5638` to
Akademia AI, Onyks `#33474F` to Pożyczki UE/BGK. Nigdy dwa naraz. Szablon uniwersalny buduj na
Aksamicie, ale **pokaż na jednym z artboardów, że da się go przełożyć na dwa pozostałe** - kolor
dziedziny ma być jednym miejscem do podmiany, nie dziesięcioma.

**Kolor nigdy nie jest jedynym nośnikiem statusu.** Po konwersji do skali szarości Werdykt,
Rubryka, Karmin i Onyks mają zbliżoną jasność, a osobny tryb monochromatyczny został odrzucony -
więc etykieta słowna albo ikona obok koloru jest jedynym zabezpieczeniem, nie jednym z dwóch.

**Kolory zestawień - przeliczone wzorem WCAG 2.1, nie do dobierania na oko.**

Etykieta na wypełnieniu jest przepisana:

| Wypełnienie | Kolor napisu | Kontrast |
|---|---|---|
| Aksamit `#452430` | Pergamin `#E7DFD2` | 10,26:1 |
| Miedź `#7A5638` | Pergamin `#E7DFD2` | 4,94:1 |
| Onyks `#33474F` | Pergamin `#E7DFD2` | 7,37:1 |
| Karmin `#9E2B2B` | Pergamin `#E7DFD2` | 5,60:1 |
| Werdykt `#2E5241` | Pergamin `#E7DFD2` | 6,62:1 |
| Rubryka `#8A6110` | biel `#FFFFFF` | 5,53:1 |
| Złoto foliowe `#A8874E` | Espresso `#221A15` | 5,09:1 |
| Espresso `#221A15` | Kaszmir `#FBF8F2` | 16,15:1 |

Trzy zakazy, każdy z liczbą:

1. **Plakietka statusu nigdy nie stoi na wypełnieniu koloru dziedziny.** Karmin na Aksamicie
   1,83:1, na Miedzi 1,13:1, na Onyksie 1,32:1 - wszystkie poniżej progu 3:1 dla grafiki. Plakietka
   stoi na papierze: Karmin na Kaszmirze 6,99:1, na Muślinie 6,63:1, na Pergaminie 5,60:1.
2. **Pieczęć w Złocie foliowym działa tylko na Aksamicie i na papierze.** Złoto na Aksamicie
   4,03:1 i na Kaszmirze 3,17:1 przechodzą. Złoto na Onyksie 2,90:1, na Miedzi 1,94:1 i na
   Pergaminie 2,55:1 **nie przechodzą**. W dokumencie dziedziny Akademia AI albo Pożyczki UE/BGK
   pieczęć potrzebuje innego tła albo innego koloru.
3. **Rubryką nie pisze się tekstu na Pergaminie** (4,18:1 wobec progu 4,5:1 dla tekstu).
   Ostrzeżenie idzie wtedy Espresso z etykietą słowną, a Rubryka zostaje wypełnieniem plakietki.

**Typografia.** Manrope 200-800 na wszystko, Inconsolata 300-700 wyłącznie na liczby, kody i
metadane. Hierarchię buduje waga jednego kroju, nie zmiana rodziny - nie dobieraj trzeciego kroju.
Skala obowiązująca, w milimetrach przy 96 dpi: display 19,05 · H1 10,58 · H2 6,35 · H3 4,23 ·
lead 4,23 · korpus 3,57 · kicker 3,70 · przypis 2,65 · Inconsolata 2,78 · liczba prowadząca 13,76.
H3 różni się od leadu **wyłącznie wagą** (600 wobec 500), więc te dwa poziomy nie stoją bezpośrednio
obok siebie; jeśli muszą, wchodzi kicker.

**Skala nie ma poziomów poniżej 7,5 pt i to jest znany brak, nie Twój błąd.** Jej najmniejszy
poziom to Manrope 2,65 mm (7,5 pt) i Inconsolata 2,78 mm (7,88 pt). Stopka, blok metryk i wizytówka
potrzebują mniej. Zrób tak: **użyj stopni, jakie są potrzebne, i zwróć ich listę** - po jednej
wartości na zastosowanie, z krótkim „bo". Nie dopisuj poziomów do skali sam; to decyzja
właściciela, a Twoja lista jest jej wejściem. Jednego progu nie przekraczaj w dół: **1,9 mm to
5,4 pt i poniżej tego pismo przestaje się czytać po druku**.

**Logotyp.** Wyłącznie pliki źródłowe z projektu: `logo_irin_poziom.svg` (podstawowy),
`logo_irin_pion.svg` (pola wąskie i wysokie), `logo_irin_sygnet.svg` (znak samodzielny). Minimalny
rozmiar 18 mm w druku, 90 px na ekranie. Przestrzeń ochronna x = wysokość liter sygnetu, mierzona
z każdej strony; to miara względna, skalująca się ze znakiem, nie stały margines strony.

**Znaku się nie modyfikuje: bez zmiany koloru, bez obracania, pochylania i odbijania, bez cienia,
poświaty i obrysu, bez nieproporcjonalnego rozciągania.** Na ciemnym tle wersja odwrócona, nie
przebarwiona. Jeżeli gdzieś potrzebujesz znaku w kolorze dziedziny, **zapisz to jako pytanie**, nie
zrób po cichu - i nigdy łańcuchem `filter:`, bo z niego nie da się odczytać, jaka barwa była
zamierzona. Jeżeli mimo wszystko zmieniasz kolor, ustaw go wprost wartością hex z palety.

**Zakaz znaków instytucjonalnych.** Na żadnym materiale IRIN nie stawia się znaku Funduszy
Europejskich, znaku barw Rzeczypospolitej Polskiej ani flagi Unii Europejskiej. Dotyczy to
w szczególności szablonów, które kiedyś obsłużą dziedzinę Pożyczki UE/BGK. **To zakaz, nie brak
obowiązku:** IRIN jest doradcą zewnętrznym, nie beneficjentem, a Podręcznik informacji i promocji
Funduszy Europejskich nie pozwala umieszczać w zestawieniu znaków podmiotów, które beneficjentami
nie są. Nazwę programu wolno napisać w treści; oznaczyć nim materiału - nie.

**Język.** Cała treść po polsku, w tym etykiety, nagłówki i mikrocopy, nie tylko akapity. Każdy
szablon niech gdzieś niesie zdanie z pełnym zestawem polskich diakrytyków, w każdej użytej wadze:
„Żółć, gęś, źdźbło, ćma, łódź, ńandu, świt, żółw: ĄĆĘŁŃÓŚŹŻ ąćęłńóśźż."

### Format wyniku

Żywa kanwa, wszystkie szablony na jednej kanwie, każdy jako osobny artboard z podpisem, co obsługuje.
Przełącznik siatki nad artboardami A4. PDF-u w tej turze nie potrzebuję.

Przy każdym szablonie dopisz **jedno zdanie o tym, co w nim jest do podmiany**, żeby dało się
go użyć bez czytania Twojego kodu. Jeżeli którakolwiek reguła wyżej okazała się niewykonalna
w praktyce, napisz to jako uwagę - **nie obchodź jej po cichu**.

Trzy rzeczy do zwrotu razem z kanwą:

1. lista stopni pisma poniżej 7,5 pt, których faktycznie potrzebowałeś, z uzasadnieniem po jednym
   zdaniu,
2. propozycja siatki slajdu 16:9 z rachunkiem szerokości domykającym się co do milimetra,
3. lista elementów, które powtarzały się w szablonach na tyle, że powinny zostać prymitywami.

## ——— KONIEC TURY 1 ———

---

## ——— POCZĄTEK TURY 2 ———

Druga tura tego samego zestawu: **znak, favicon, wizytówki i social media**. Specyfikacje masz
w projekcie: `logotyp.md`, `paleta-barw.md`, `typografia.md`, `siatka-a4.md`, `zasady-uzycia.md`,
`tokens/palette-irin.json`.

**Reguły z tury pierwszej obowiązują bez zmian**, w szczególności: wszystko na placeholderach
w nawiasach kwadratowych i zero zmyślonych danych; jeden kolor dziedziny na materiał; kolor nigdy
nie jest jedynym nośnikiem statusu; linia struktury Popiołem `#7D7466` nie cieniej niż 0,25 mm,
Złoto foliowe `#A8874E` nie cieniej niż 0,5 mm; na materiale IRIN nie ma znaku Funduszy
Europejskich, znaku barw RP ani flagi Unii Europejskiej.

### 9. Pakiet znaku do użycia - to jest zlecenie

Trzy warianty znaku (`logo_irin_poziom.svg`, `logo_irin_pion.svg`, `logo_irin_sygnet.svg`)
pokazane na pięciu tłach: Kaszmir `#FBF8F2`, Muślin `#F6F2E9`, Pergamin `#E7DFD2`,
Espresso `#221A15`, Aksamit `#452430`.

Na każdym tle **wersja właściwa, nie przebarwiona**: na trzech jasnych znak w kolorze źródłowym,
na dwóch ciemnych wersja odwrócona. Podstawa liczbowa, przeliczona wzorem WCAG 2.1:

| Znak w kolorze | na Aksamicie | na Miedzi | na Onyksie | na Espresso |
|---|---|---|---|---|
| Espresso `#221A15`, kolor źródłowy | 1,26:1 | 2,62:1 | 1,76:1 | 1,00:1 |
| Kaszmir `#FBF8F2`, wersja odwrócona | 12,80:1 | 6,16:1 | 9,19:1 | 16,15:1 |

Próg 3:1 dla grafiki znaczącej. **Znak w kolorze źródłowym nie przechodzi na żadnym z trzech
kolorów dziedziny** - na każdym z nich wchodzi wersja odwrócona.

Do tego samego artboardu dołóż dwie demonstracje, bo bez nich pakiet jest niekompletny:

- **przestrzeń ochronna** x = wysokość liter sygnetu, pokazana obrysem z każdej strony znaku,
  przy dwóch różnych wielkościach - żeby było widać, że to miara względna, a nie stały margines,
- **minimalne rozmiary:** pełny znak 18 mm w druku i 90 px na ekranie, sygnet samodzielny
  10 mm i 44 px. Pokaż każdy dokładnie w minimum, obok tego samego znaku w rozmiarze wygodnym.

### 10. Wersje kolorystyczne znaku i favicon - OSOBNY artboard, oznaczony jako PROPOZYCJA

**To nie jest zlecenie pakietu.** Właściciel poprosił o „logo w różnych kolorach", a obowiązujący
`logotyp.md` ma zakaz 1: znaku się nie przebarwia, na ciemnym tle wchodzi wersja odwrócona.
Twoim zadaniem jest **przygotować materiał do jego decyzji**, nie rozstrzygnąć ją.

Oznacz ten artboard słowem PROPOZYCJA i pokaż:

- znak w Aksamicie `#452430`, Miedzi `#7A5638`, Onyksie `#33474F` i Złocie foliowym `#A8874E`,
  każdy na papierze Kaszmir, **z policzonym kontrastem wobec tła obok każdej wersji**,
- kolor ustawiony **wprost wartością hex**, nigdy łańcuchem `filter:`. Filtr użyty w pierwszej
  turze pilota celował w Aksamit `#452430`, a dawał `#3D1922` - z łańcucha filtrów nie da się
  odczytać, jaka barwa była zamierzona.

**Favicon - i druga część sprzeczności, niezależna od koloru.** Rozmiary do przygotowania:
16, 32, 48, 180 i 512 px. Sygnet w 16 i 32 px stoi **poniżej minimum 44 px** z tabeli
w `logotyp.md`, czyli favicon w ogóle nie mieści się w obowiązującej specyfikacji.

Zrób z tym trzy rzeczy: pokaż sygnet w każdym z pięciu rozmiarów bez żadnych zmian, żeby było
widać, co się z nim dzieje w 16 i 32 px; **zaproponuj uproszczenie** znaku na te dwa rozmiary jako
osobną pozycję, też oznaczoną jako propozycja; i napisz jednym zdaniem, co konkretnie w sygnecie
przestaje się czytać poniżej 44 px. Uproszczenie jest utworem pochodnym od znaku, więc nie wchodzi
do użycia bez decyzji właściciela.

### 11. Wizytówka - cztery wersje kolorystyczne

Format 85 × 55 mm, awers i rewers, wszystkie pola osoby jako placeholdery: `[IMIĘ I NAZWISKO]`,
`[STANOWISKO]`, `[TELEFON]`, `[E-MAIL]`. Dane firmowe w brzmieniu z pierwszej tury.

Cztery wersje, każda z jednym kolorem, nigdy dwoma:

| Wersja | Tło awersu | Zastosowanie | Znak na awersie |
|---|---|---|---|
| ogólnofirmowa | Kaszmir `#FBF8F2` | dokument całej firmy, bez sygnału dziedziny | kolor źródłowy |
| Pedagogika | Aksamit `#452430` | dziedzina Pedagogika | wersja odwrócona, 12,80:1 |
| Akademia AI | Miedź `#7A5638` | dziedzina Akademia AI | wersja odwrócona, 6,16:1 |
| Pożyczki UE/BGK | Onyks `#33474F` | dziedzina Pożyczki UE/BGK | wersja odwrócona, 9,19:1 |

**Sygnet na rewersie: powiększ go wobec 22 mm z pierwszej tury.** Właściciel prosił o to
dwukrotnie. Podaj **zmierzoną szerokość w milimetrach** przy każdej wersji - to wchodzi do
protokołu. Rewers zostaje na tle Espresso `#221A15` z sygnetem w wersji odwróconej (16,15:1).

Jedna rzecz do sprawdzenia u siebie, zanim oddasz: **przestrzeń ochronna x wokół powiększonego
sygnetu.** Im większy sygnet na karcie 85 × 55 mm, tym mniej miejsca zostaje na wymagane
odsunięcie od krawędzi - jeżeli x nie mieści się, napisz to, a nie zmniejszaj x po cichu.

### 12. Social media - sześć formatów, pięć typów treści

Formaty w pikselach: **1080 × 1080** (kwadrat), **1080 × 1350** (portret 4:5),
**1080 × 1920** (pełny ekran, 9:16), **1200 × 630** (podgląd odnośnika, OG),
**1584 × 396** (baner LinkedIn), **400 × 400** (awatar).

Typy treści, każdy jako jeden kadr: **cytat**, **ogłoszenie szkolenia**, **post z jedną wielką
liczbą** (skala ma na to poziom: liczba prowadząca 13,76 mm), **post z terminem**,
**karuzela w trzech klatkach** (otwarcie, rozwinięcie, wezwanie do działania).

**Siatka: żaden z tych formatów nie ma zatwierdzonej siatki.** `siatka-a4.md` obowiązuje wyłącznie
na A4 pion. Sześć kolumn zostaje jako element tożsamości; moduł, gutter i marginesy **proponujesz
Ty, z rachunkiem szerokości domykającym się co do milimetra albo piksela**. Oznacz to jako
propozycję.

**Zakazane sformułowania - te obowiązują szczególnie tutaj, bo to kanał, w którym się pojawiają.**
Podstawa: karta prezentacji sprzedażowej w warstwie 2, sekcja „Zasady twarde".

- Nigdy: „gwarancja dofinansowania", „za darmo", „bezpłatnie".
- Nigdy nie podawaj terminu naboru, którego nie ma w ogłoszeniu instytucji finansującej.
- W kanale KFS: „usługa kwalifikuje się do wniosku o środki", **nigdy** „KFS to sfinansuje" -
  decyzja urzędu pracy jest uznaniowa.
- Przy każdej wzmiance o dofinansowaniu zastrzeżenie: poziom zależy od statusu klienta i oceny
  wniosku, środki do wyczerpania alokacji naboru.
- Ceny, jeżeli wystąpią, opisane wprost jako netto albo brutto, w każdym miejscu.

Na wzorach użyj tych sformułowań w wersji poprawnej, jako placeholderów treści - żeby szablon
uczył zasady, a nie tylko jej nie łamał.

**Zakaz znaków instytucjonalnych ma tu ostrze:** materiał social media o dziedzinie
Pożyczki UE/BGK jest miejscem, w którym flaga Unii Europejskiej wydaje się naturalna. Nie wchodzi.
IRIN jest doradcą zewnętrznym, nie beneficjentem.

## ——— KONIEC TURY 2 ———

---

## ——— POCZĄTEK TURY 3 ———

Trzecia tura: **pełna prezentacja, arkusz z tabelą i wykresami, oraz dodatki na start**.
Reguły z tur 1 i 2 obowiązują bez zmian.

### 13. Prezentacja - szablon rozbudowany, każdy wariant slajdu

Format 16:9. **Siatka slajdu nie istnieje i nie wolno jej wziąć na oko** - `siatka-a4.md`
obowiązuje wyłącznie na A4 pion i sam ten plik mówi, że inny format unieważnia całe sprawdzenie.
Sześć kolumn zostaje; moduł, gutter i marginesy proponujesz Ty, z rachunkiem domykającym się
co do jednostki. Pierwszy artboard tury niech będzie **propozycją siatki slajdu**, z tym rachunkiem
wypisanym.

Warianty slajdu do przygotowania, każdy jako osobny slajd:

1. tytułowy
2. tytułowy w wersji roboczej, z oznaczeniem `SZKIC - KONSULTACJA WEWNĘTRZNA`
3. agenda albo spis treści
4. przerywnik sekcji
5. treść jednokolumnowa
6. treść dwukolumnowa
7. treść trzykolumnowa
8. tekst plus obraz, obraz po prawej
9. tekst plus obraz, obraz po lewej
10. obraz pełnoekranowy z podpisem
11. cytat
12. jedna wielka liczba z podpisem
13. trzy liczby obok siebie
14. tabela
15. wykres z opisem
16. dwa wykresy obok siebie
17. schemat procesu, cztery kroki poziomo
18. oś czasu
19. porównanie dwóch opcji, z plakietkami statusu
20. lista kroków numerowana
21. osoby, cztery kadry z placeholderem zdjęcia
22. slajd z zastrzeżeniem prawnym, na pełną szerokość
23. kontakt i wezwanie do działania
24. slajd końcowy ze znakiem

Dwie rzeczy do pilnowania w całości: **hierarchię buduje waga jednego kroju**, więc nie dobieraj
trzeciego; i **H3 różni się od leadu wyłącznie wagą** (600 wobec 500), więc te dwa poziomy nie
stoją bezpośrednio obok siebie - jeżeli muszą, wchodzi kicker.

### 14. Arkusz - układ tabeli, pasy wierszy, kodowanie typów pól

Jeden artboard z arkuszem wzorcowym, czytelnym w druku i na ekranie.

**Pasy wierszy - wartości zmierzone, nie do dobierania.** Zebra idzie na parze
Kaszmir `#FBF8F2` i Muślin `#F6F2E9`: kontrast **1,054:1**, czyli w zakresie, w którym pas pomaga
czytać wiersz, a nie udaje danych. Pergamin `#E7DFD2` **odpada**: wobec Kaszmiru daje **1,247:1**
i pas zaczyna się czytać jako wyróżnienie treści.

**Kodowanie typów pól - kolor plus etykieta, nigdy kolor sam.** Cztery typy, każdy z obrysem
Popiołem `#7D7466` co najmniej 0,25 mm i z widoczną etykietą albo ikoną:

- pole do wypełnienia przez człowieka
- pole liczone formułą, niedotykalne
- pole zablokowane
- pole z błędem walidacji

Do tego: nagłówek tabeli, wiersz sumy wyróżniony, przypis pod tabelą, oraz **zachowanie przy
przejściu tabeli na drugą stronę** - powtórzony nagłówek i oznaczenie kontynuacji.

### 15. Wykresy - i jedno zlecenie badawcze, o które prosił właściciel

**Zmierzone, żeby nie było niespodzianki:** uruchomiłem walidator palet kategorialnych na trzech
zestawach zbudowanych z 14 kolorów IRIN, na tle Kaszmir. Wszystkie trzy **nie przeszły**, i za
każdym razem z tego samego powodu: nasycenie każdego koloru IRIN leży między 0,016 a 0,085
w OKLCH, przy podłodze **0,10** - poniżej niej barwa czyta się jako szarość i przestaje nieść
tożsamość serii. Dodatkowo kolory najciemniejsze mają jasność 0,226 - 0,406 przy dolnej granicy
pasma **0,43**. To skutek tego, że system nazywa się Kaszmir Wyciszony i jest celowo odsycony,
a nie błąd palety.

**Część A: wykresy, które działają bez palety serii - to jest zlecenie.** Cztery przykłady:

- **słupki poziome** z etykietami wprost przy słupku, jedna seria, sekwencja odcieni Aksamitu
  na wielkość: `#BBAEAE` (2,03:1), `#9E8B8F` (3,03:1), `#80696F` (4,75:1), `#634650` (7,85:1),
  `#452430` (12,80:1). Na dwóch najjaśniejszych krokach nie stawiaj tekstu ani cienkiej linii.
- **linia w czasie**, grubość 2 px, znaczniki co najmniej 8 px, etykieta wprost przy końcu linii
- **małe wielokrotności** zamiast wielu serii na jednej osi - to jest odpowiedź na brak palety
- **schemat procesu** na czterech krokach

Reguły, które obowiązują niezależnie od palety: **nigdy dwie osie Y**; statusy Werdykt `#2E5241`,
Rubryka `#8A6110` i Karmin `#9E2B2B` są **zarezerwowane** i nie wolno ich użyć jako „serii
czwartej"; siatka i osie recesywne, nie konkurujące z danymi; przy dwóch albo więcej seriach
legenda jest zawsze, a przy czterech i mniej dodatkowo etykiety wprost; wartości i etykiety
noszą kolory tekstu, nie kolor serii; faktura kierunkowa (45 i 135 stopni) jako drugi nośnik
tożsamości obok koloru, dla druku mono i dla daltonizmu.

**Część B: zaproponuj paletę serii - to jest zlecenie badawcze, nie decyzja.** Właściciel chce
wiedzieć, czy da się to zrobić. Warunki przyjęcia są policzalne i podaję je wprost, żeby nie było
zgadywania:

| Kryterium | Próg |
|---|---|
| jasność każdego koloru, OKLCH L, tło jasne | **0,43 - 0,77** |
| nasycenie każdego koloru, OKLCH C | **co najmniej 0,10** |
| odróżnialność sąsiadów w wadach widzenia barw, ΔE w OKLab ×100 | cel **8**, podłoga **6** i tylko przy drugim nośniku tożsamości |
| odróżnialność sąsiadów w widzeniu prawidłowym, ΔE | **co najmniej 15**, poniżej to twardy błąd |
| kontrast każdego koloru wobec tła | **co najmniej 3:1** |

Do tego trzy ograniczenia nie z walidatora, a z tożsamości IRIN: kolejność barw jest **stała
i nigdy nie zapętlana** (dziewiąta seria wchodzi do pozycji „Inne", nie dostaje nowego koloru);
maksimum osiem pozycji; i **nie wolno użyć trzech kolorów dziedziny ani trzech kolorów statusu**,
bo obie grupy mają już przypisane znaczenie.

Z liczb wyżej wynika, że kolory spełniające te progi będą **jaśniejsze i bardziej nasycone niż
cokolwiek w obecnych czternastu**, czyli będą nowe. Dlatego to wraca jako **propozycja piątej
specyfikacji identyfikacji**, do decyzji właściciela, a nie jako gotowa paleta do użycia.
**Podaj przy każdej pozycji jej hex, OKLCH L, OKLCH C i kontrast wobec Kaszmiru** - przeliczę
to tym samym walidatorem i wynik pójdzie do właściciela razem z Twoją propozycją.

### 16. Co jeszcze na start - pozycje dołożone z mojej propozycji

Pięć rzeczy, o które właściciel nie poprosił wprost, a które są potrzebne od pierwszego dnia.
Każda z uzasadnieniem, żeby dało się ją odrzucić.

1. **Materiały dla uczestnika szkolenia:** slajd szkoleniowy i handout na A4. Powód: karta usługi
   BUR ma pole obowiązkowe „Informacja o materiałach dla uczestników", więc materiały muszą
   istnieć, zanim usługa zostanie opublikowana.
2. **Oferta i kosztorys**, A4. Powód: to dokument, który wychodzi do klienta najczęściej,
   a obowiązuje w nim reguła twarda z warstwy 2 - cena opisana wprost jako netto albo brutto,
   w każdym miejscu, gdzie się pojawia.
3. **Potwierdzenie zapisu na szkolenie** i **lista obecności**, A4. Powód: dokumenty operacyjne
   obsługi szkolenia. **Nie twierdzę, że mają podstawę prawną** - żaden przejrzany dokument PARP
   ani przepis KFS ich nie wymienia; są potrzebne organizacyjnie.
4. **Znak wodny SZKIC** na pełną stronę A4, do nakładania na materiał roboczy. Powód: warstwa 2
   wymaga jawnego oznaczenia poziomu materiału, a dziś istnieje tylko plakietka, nie oznaczenie
   całej strony.
5. **Baner na stronę i obraz podglądu odnośnika** dla `www.irin.pl`. Powód: te dwa kadry są
   w tury 2 jako formaty (1584 × 396 i 1200 × 630), ale bez treści firmowej - tu dostają wersję
   ogólnofirmową, gotową do użycia.

### Format wyniku dla tur 2 i 3

Ta sama kanwa, nowe artboardy, każdy z podpisem i jednym zdaniem o tym, co jest w nim do podmiany.
Przy każdym artboardzie oznaczonym jako PROPOZYCJA napisz wprost, czego dotyczy decyzja
właściciela. Jeżeli którakolwiek reguła okazała się niewykonalna, napisz to jako uwagę -
**nie obchodź jej po cichu**.

Do zwrotu razem z kanwą, poza tym co w turze 1:

1. propozycje siatki dla trzech formatów bez zatwierdzonej siatki: slajd 16:9, kadry social media,
   wizytówka - każda z rachunkiem,
2. propozycja palety serii z czterema liczbami przy każdej pozycji, albo jasne stwierdzenie,
   że przy tych progach nie da się jej zbudować bez wyjścia poza charakter Kaszmiru Wyciszonego,
3. zmierzona szerokość powiększonego sygnetu na rewersie wizytówki, dla każdej wersji kolorystycznej,
4. jedno zdanie o tym, co w sygnecie przestaje się czytać poniżej 44 px.

## ——— KONIEC TURY 3 ———

---

## Część C: czego nie zlecamy Claude Design

Trzy rzeczy z listy właściciela nie są pracą projektową i powstają w repozytorium, nie na kanwie.
Wchodzą do `PLAN.md` jako zadania Claude Code.

| Co | Dlaczego nie na kanwie | Kto robi |
|---|---|---|
| Plik `.xlsx` arkusza z tabelą, pasami wierszy i wykresami | Claude Design projektuje wygląd arkusza, ale nie wyprodukuje działającego pliku z formułami, formatowaniem warunkowym i wykresami | Claude Code, po zamknięciu pozycji 14 i 15 |
| Szablon `.docx` do pisania pism | Sens tego szablonu polega na tym, że firma pisze pismo **bez** Claude Design; plik musi mieć styl akapitu, nagłówek i stopkę w formacie Worda | Claude Code, po zamknięciu tury 1 |
| Podpis e-mail w HTML | To kod, nie layout drukowany; wymaga tabel HTML i stylów inline, bo klienty pocztowe nie renderują nowoczesnego CSS | Claude Code |

Podpis e-mail ma jedno uzasadnienie merytoryczne, nie tylko wygodę: art. 206 Kodeksu spółek
handlowych wymaga danych rejestrowych na pismach spółki, a e-mail jest dziś głównym kanałem pism
wychodzących. Blok danych z papieru firmowego przenosi się tam bez zmian.
