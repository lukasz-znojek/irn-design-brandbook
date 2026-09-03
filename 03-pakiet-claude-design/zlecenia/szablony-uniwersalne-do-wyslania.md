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

---

## ——— POCZĄTEK TEKSTU DO WKLEJENIA ———

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

## ——— KONIEC TEKSTU DO WKLEJENIA ———
