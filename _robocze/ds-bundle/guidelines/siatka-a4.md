# Siatka dokumentu A4 - specyfikacja obowiązująca

**Status: ZATWIERDZONA przez foundera (2026-09-02).** To jest jedyne źródło prawdy dla siatki dokumentów IRIN.

Dane maszynowe: [`tokeny/palette-irin.json`](./tokeny/palette-irin.json), klucz `siatka-a4`.
Kolor: [`paleta-barw.md`](./paleta-barw.md). Typografia: [`typografia.md`](./typografia.md).
Jak siatka wchodzi do zlecenia dla Claude Design: [`../../03-pakiet-claude-design/format-paczki.md`](../../03-pakiet-claude-design/format-paczki.md).
Pomiar i historia decyzji: [`../../03-pakiet-claude-design/propozycja-palety-i-siatki-do-potwierdzenia.md`](../../03-pakiet-claude-design/propozycja-palety-i-siatki-do-potwierdzenia.md).

## Parametry

| Parametr | Wartość |
|---|---|
| Format strony | A4 pion, 210 × 297 mm |
| Kolumny | 6 |
| Moduł kolumny | 25 mm |
| Gutter | 4 mm |
| Margines górny | 18 mm |
| Margines lewy | 20 mm |
| Margines prawy | 20 mm |
| Margines dolny | 28 mm |
| Pole treści | 170 × 251 mm |

Liczba kolumn (sześć) jest wspólna dla wszystkich trzech dziedzin - to element tożsamości systemu, nie parametr do dobierania per dokument.

## Sprawdzenie, że siatka fizycznie mieści się na stronie

Szerokość pola treści: 210 - 20 (lewy) - 20 (prawy) = **170 mm**.
Suma siatki: 6 × 25 + 5 × 4 = 150 + 20 = **170 mm**.
**Dopasowanie dokładne**, bez zapasu i bez nadmiaru.

Wysokość pola treści: 297 - 18 (górny) - 28 (dolny) = **251 mm**.

Liczby przeliczone w tej sesji, nie przepisane z żadnego dokumentu. Falsyfikator: inny format albo inna orientacja strony niż A4 pion - wtedy całe to sprawdzenie trzeba wykonać od nowa.

## Marginesy boczne wyrównane - poprawka 2026-09-03

Do 2026-09-03 marginesy boczne wynosiły 18 mm z lewej i 22 mm z prawej. Ta asymetria nie miała
uzasadnienia: dokumenty IRIN nie są oprawiane ani bindowane, więc nie ma krawędzi, która
potrzebowałaby zapasu. Powstała jako reszta z rachunku, nie jako decyzja.

**Poprawka nic nie kosztuje.** Pole treści ma tak samo 170 mm w obu układach:

| Układ | Rachunek | Pole treści | Zgodność z siatką 170 mm |
|---|---|---|---|
| dawny 18 / 22 | 210 - 18 - 22 | 170 mm | zgodne |
| **obowiązujący 20 / 20** | 210 - 20 - 20 | **170 mm** | zgodne |

Siatka, moduł, gutter i wysokość pola treści są nietknięte - zmienia się wyłącznie położenie
bloku treści na stronie, o 2 mm w prawo.

**Marginesy pionowe zostają niesymetryczne celowo:** 18 mm u góry, 28 mm u dołu. Cięższy margines
dolny to reguła składu, nie przeoczenie - blok treści posadzony optycznie w połowie strony leży
wyżej niż w połowie geometrycznej.

**Falsyfikator:** jeśli któryś dokument IRIN ma być bindowany, zszywany albo dziurkowany, wraca
margines wewnętrzny większy od zewnętrznego, a wtedy asymetria jest uzasadniona i tę sekcję
trzeba napisać od nowa. Papier firmowy i wizytówka takiej krawędzi nie mają.

## Dlaczego moduł to 25 mm, a nie 32 mm z kanwy

`brandbook.dc.html` opisuje siatkę jako 6 kolumn, moduł 32 mm, gutter 4 mm. Ta siatka jest geometrycznie niemożliwa na A4 pion: 6 × 32 + 5 × 4 = **212 mm**, czyli o 2 mm więcej niż cała szerokość strony (210 mm) i o 42 mm więcej niż pole treści przy podanych marginesach. Nie mieści się nawet przy marginesach zerowych.

Poprawka polegała na zmniejszeniu modułu z 32 do 25 mm przy zachowaniu sześciu kolumn i gutteru 4 mm - bo to liczba kolumn jest w kanwie opisana jako element wspólny systemu, a moduł 32 mm był niesprawdzonym pomiarem. Rozważana alternatywa (5 kolumn po 32 mm, prawy margines zmniejszony do 16 mm) została odrzucona przez foundera.

## Dlaczego moduł 25 mm i gutter 4 mm, a nie inna para

Przy sześciu kolumnach i polu treści 170 mm równanie `6 × moduł + 5 × gutter = 170` ma pięć
rozwiązań w liczbach całkowitych:

| Gutter | Moduł | Ocena |
|---|---|---|
| **4 mm** | **25 mm** | **obowiązujące** - gutter jest szóstą częścią modułu, więc kolumna czyta się jako kolumna |
| 10 mm | 20 mm | gutter to połowa modułu; odstęp konkuruje z kolumną |
| 16 mm | 15 mm | gutter szerszy od połowy modułu; siatka rozpada się na paski |
| 22 mm | 10 mm | gutter dwukrotnie szerszy od modułu |
| 28 mm | 5 mm | moduł węższy od jednego słowa |

Para 25 / 4 nie jest więc wyborem estetycznym, tylko jedyną, która przy zadanych sześciu kolumnach
i 170 mm daje odstęp wyraźnie węższy od kolumny. To domyka pytanie „dlaczego akurat te liczby”:
liczba kolumn jest decyzją tożsamościową, szerokość pola treści wynika z formatu i marginesów,
a moduł i gutter są z nich policzone.

## Rytm pionowy - co jednostka 6 mm faktycznie wymierza

Sekcja niżej rozstrzyga, czym jednostka 6 mm **nie** jest (siatką linii bazowych). Tu jest
napisane, czym jest - bo do 2026-09-03 specyfikacja definiowała wyłącznie poziom, a pion
zostawiała projektantowi.

**Zasada:** odstęp pionowy **między blokami treści** jest wielokrotnością 6 mm. Dopuszczone
wartości w praktyce: 6, 12, 18, 24 i 48 mm. Odstępu 8, 10 czy 15 mm między blokami w tym
systemie nie ma.

**Czego ta zasada nie obejmuje: wnętrza komponentu.** Światło pod linią stopki, padding komórki
tabeli, odstęp między etykietą a wartością w jednym wierszu danych - to są wymiary wewnętrzne
i dobiera się je do stopnia pisma, nie do jednostki strony. Wymuszanie tam 6 mm rozpycha
komponenty i psuje właśnie ten rytm, który jednostka ma budować. Granica jest prosta: jeżeli
element da się przesunąć bez ruszania sąsiada, to jest wnętrze; jeżeli przesunięcie przesuwa
następny blok, to jest odstęp i podlega jednostce.

**Reszta 5 mm zostaje na dole i nigdy nie jest odstępem.** Pole treści ma 251 mm, czyli 41 pełnych
jednostek i 5 mm reszty. Ta reszta jest światłem pod ostatnim blokiem, nie luzem do rozdzielenia
między odstępy - inaczej rytm rozjeżdża się o niecały milimetr na każdym styku.

**Czego świadomie nie zrobiono:** marginesu dolnego nie zmieniono z 28 na 27 mm, choć wtedy pole
treści miałoby 252 mm, czyli równe 42 jednostki. Sekcja niżej rozstrzygnęła 2026-09-02, że taka
zmiana poprawia dzielenie liczb, a nie ustawia żadnego elementu - i nic w pomiarach z 2026-09-03
tego nie obaliło. Zmiana bez nowego pomiaru byłaby kosmetyką podaną jako poprawka.

## Strefa stopki - dolny margines jest jej, nie treści

Pilot papieru firmowego ustawił stopkę 12 mm od dolnej krawędzi strony, czyli **poniżej pola
treści**, którego dolna krawędź leży 28 mm od spodu. To nie jest błąd projektanta, tylko luka
w tej specyfikacji: mówiła, gdzie kończy się treść, i nie mówiła, gdzie stoi stopka.

**Rozstrzygnięcie:** dolny margines 28 mm jest **strefą stopki**. Wolno w niej stać wyłącznie
linii oddzielającej i jednemu pasowi metadanych - dane rejestrowe, numer strony, numer pisma.
Treść dokumentu nie wchodzi tam nigdy. Górna krawędź linii stopki leży na dolnej krawędzi pola
treści albo niżej; dolna krawędź tekstu stopki nie schodzi bliżej niż 12 mm od krawędzi strony,
bo poniżej zaczyna się obszar nierozpoznawalny dla części drukarek biurowych.

To samo dotyczy marginesu górnego 18 mm: jest strefą znaku i nagłówka strony, nie treści.

**Falsyfikator obu stref:** dokument, w którym stopka albo nagłówek muszą pomieścić więcej niż
jeden pas - wtedy strefa jest za wąska i wraca pytanie o marginesy, tym razem z pomiarem
wysokości realnej stopki, nie z rachunku dzielenia.

## Jednostka bazowa 6 mm - rozstrzygnięte

`brandbook.dc.html` podaje jednostkę bazową 6 mm. Pierwsze podejrzenie brzmiało, że rytm pionowy się nie domyka: 251 mm / 6 mm = 41,83, czyli 41 pełnych jednostek i 5 mm reszty, a domknięcie wymagałoby marginesu dolnego 33 mm. **Pomiar pokazał, że to jest zła diagnoza** i margines nie jest tu w ogóle problemem.

Żeby jednostka 6 mm mogła działać jako siatka linii bazowych tekstu, interlinia korpusu musiałaby być jej wielokrotnością. Nie jest:

| Wielkość | Wartość |
|---|---|
| Jednostka bazowa | 6 mm = 22,68 px (przy 96 dpi) |
| Interlinia korpusu | 13,5 px × 1,55 = 20,93 px = **5,54 mm** |
| Różnica na każdą linię | 1,75 px = **0,46 mm** |
| Dryf na pełnej kolumnie (45 linii) | **19 mm** |

Tekst korpusu rozjeżdża się z siatką 6 mm o niecały milimetr na linię i o prawie dwa centymetry na pełnej stronie. Zmiana marginesu dolnego z 28 na 33 mm nie ma z tym nic wspólnego - poprawiłaby wyłącznie dzielenie jednej liczby przez drugą, nie ustawiłaby ani jednej linii tekstu na siatce.

**Rozstrzygnięcie: margines dolny zostaje 28 mm, a jednostka 6 mm jest jednostką odstępu, nie siatką linii bazowych tekstu.** Służy do wymierzania przerw między blokami, marginesów wewnętrznych i wysokości elementów - tam dzielenie się wysokości strony nie ma znaczenia, bo bloki nie muszą wypełniać kolumny co do milimetra. Reszta 5 mm wypada poniżej ostatniej linii i jest po prostu dodatkowym światłem u dołu strony.

**Co by musiało się zmienić, gdyby founder jednak chciał prawdziwej siatki linii bazowych:** interlinia korpusu z 1,55 na około **1,68** (czyli 22,68 px przy stopniu 13,5 px). To zmiana typografii, nie siatki, i rozluźniłaby tekst o 8 procent - w dokumentach regulowanych, gdzie treści jest dużo, to realny koszt stron. Nikt o taką zmianę nie prosił, więc jej nie wprowadzono.

**Falsyfikator tego rozstrzygnięcia:** jeśli jednostka 6 mm miała w zamyśle foundera dotyczyć właśnie linii bazowych tekstu, a nie odstępów - wtedy wracamy do tego punktu i rozmawiamy o interlinii, nadal nie o marginesie.
