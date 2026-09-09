# Siatka dokumentu A4 - specyfikacja obowiązująca

**Status: ZATWIERDZONA.** Format 210 × 297 mm, 6 kolumn, moduł 25 mm, gutter 4 mm.

Dane maszynowe: [`tokeny/palette-irin.json`](./tokeny/palette-irin.json), klucz `siatka-a4`. Kolor: [`paleta-barw.md`](./paleta-barw.md). Typografia: [`typografia.md`](./typografia.md). Logotyp: [`logotyp.md`](./logotyp.md).

**Ten plik jest wywiedziony, nie źródłowy.** Wartości pochodzą z [`tokeny/palette-irin.json`](./tokeny/palette-irin.json); zmiana idzie przez [`../../_robocze/narzedzia/zloz-palete.py`](../../_robocze/narzedzia/zloz-palete.py) i bramki `sprawdz-palete.py` oraz `sprawdz-zgodnosc-md.py`.

## Parametry

| Parametr | Wartość |
|---|---|
| Format strony | 210 × 297 mm (A4 pionowo) |
| Kolumny | 6 |
| Moduł kolumny | 25 mm |
| Gutter | 4 mm |
| Margines górny | 18 mm |
| Margines lewy | 20 mm |
| Margines prawy | 20 mm |
| Margines dolny | 28 mm |
| Pole treści | 170 × 251 mm = **426,70 cm2** |
| Jednostka odstępu | 6 mm |

Pole treści jest podstawą limitu akcentu z [`paleta-barw.md`](./paleta-barw.md): 5 % z 426,70 cm2 to 21,34 cm2 złota na stronie.

## Rachunek, który musi się zgadzać co do milimetra

`6 × 25 + 5 × 4 = 170 mm = 210 - 20 - 20`

Dopasowanie jest **dokładne**: suma kolumn i gutterów to 170 mm, szerokość pola treści to 170 mm, różnica zero. Bramka pomiarowa sprawdza tę równość przy każdym złożeniu, więc siatka nie może się rozjechać po cichu.

Konsekwencja: **każda zmiana modułu albo gutteru pociąga zmianę marginesu, i odwrotnie.** Nie ma tu wartości, którą da się poprawić w pojedynkę.

## Dlaczego 25 i 4

Równanie `6c + 5g = 170` ma 5 rozwiązań w liczbach całkowitych:

| Moduł | Gutter | Gutter wobec modułu |
|---|---|---|
| 25 mm **(obowiązujące)** | 4 mm | 16,0 % |
| 20 mm | 10 mm | 50,0 % |
| 15 mm | 16 mm | 106,7 % |
| 10 mm | 22 mm | 220,0 % |
| 5 mm | 28 mm | 560,0 % |

Wybrane jest pierwsze, bo gutter jest wtedy **szóstą częścią modułu**: kolumna czyta się jako kolumna, a nie jako pasek obok przerwy. W pozostałych parach gutter zbliża się do modułu albo go przekracza i siatka przestaje wyglądać na siatkę sześciokolumnową.

To nie jest historia decyzji, tylko uzasadnienie wartości obowiązującej - dlatego zostaje w specyfikacji.

## Rytm pionowy

**Zasada:** odstęp pionowy **między blokami treści** jest wielokrotnością 6 mm. Dopuszczone w praktyce: 6, 12, 18, 24 i 48 mm. Odstępu 8, 10 czy 15 mm w tym systemie nie ma.

**Czego ta zasada nie obejmuje: wnętrza komponentu.** Padding komórki tabeli, światło pod linią stopki, odstęp między etykietą a wartością w jednym wierszu danych - to wymiary wewnętrzne, dobierane do stopnia pisma, nie do jednostki strony. Granica jest ostra: jeżeli element da się przesunąć bez ruszania sąsiada, to jest wnętrze; jeżeli przesunięcie przesuwa następny blok, to jest odstęp i podlega jednostce.

**Reszta 5 mm zostaje na dole i nigdy nie jest odstępem.** Pole treści ma 251 mm, czyli 41 pełnych jednostek i 5 mm reszty. Ta reszta jest światłem pod ostatnim blokiem, nie luzem do rozdzielenia między odstępy.

## Dryf rytmu: 20,86 mm

Jednostka 6 mm **nie jest siatką linii bazowych tekstu** i nie musi nią być. Interlinia korpusu nie jest jej wielokrotnością, więc tekst układany na tę jednostkę rozjeżdża się z nią liniowo.

| Wielkość | Wartość |
|---|---|
| Jednostka odstępu | 6 mm = 22,68 px przy 96 dpi |
| Interlinia korpusu | 5,54 mm |
| Różnica na linię | 0,46 mm |
| Linii korpusu w polu treści | 45 |
| **Dryf na pełnej kolumnie** | **20,86 mm** |

Pełny rachunek, wraz z pułapką mnożenia zaokrąglonej różnicy, stoi w jednym miejscu: [`typografia.md`](./typografia.md), sekcja o interlinii korpusu. Tutaj jest wynik, tam wyprowadzenie - **nie ma dwóch źródeł tej liczby.**

Liczba 20,86 mm obala 19 mm, którą ten plik podawał wcześniej przy etykiecie „45 linii": 19 to dryf na 41 jednostkach siatki, nie na 45 liniach tekstu.

## Dwie strefy marginesów

- **Górne 18 mm:** strefa znaku i nagłówka strony, nie treści.
- **Dolne 28 mm:** strefa stopki: linia oddzielająca i jeden pas metadanych; dolna krawędź tekstu nie schodzi bliżej niż 12 mm od krawędzi strony.

Margines dolny jest szerszy od górnego i od boków nie przez pomyłkę: niesie stopkę, a nie zapas.

## Siatka slajdu 16:9 - PROPOZYCJA, nie specyfikacja

**Ta sekcja czeka na decyzję właściciela i do jej podjęcia nie jest specyfikacją obowiązującą.** Rachunek się domyka, ale domknięty rachunek nie jest zatwierdzeniem.

| Parametr | Propozycja |
|---|---|
| Kanwa | 1920 × 1080 px |
| Marginesy | 96 px z każdej strony |
| Pole treści | 1728 × 888 px |
| Kolumny | 6, moduł 253 px, gutter 42 px |
| Jednostka pionowa | 24 px |

Kontrola pozioma: `6 × 253 + 5 × 42 = 1728 px`, czyli dokładnie pole treści.
Kontrola pionowa: `888 / 24 = 37`, bez reszty.

Proporcja gutteru do modułu wynosi 42/253 = 16,6 %, wobec 4/25 = 16,0 % na A4. Slajd jest więc o włos luźniejszy, co przy oglądaniu z odległości działa na korzyść.

**Co ta propozycja obala.** Rozdz. 17 brandbooka podaje gutter 32 px przy marginesie 96 px, a wtedy `(1728 - 5 × 32) / 6 = 261,33 px` na kolumnę, czyli liczba niecałkowita. Ta para wartości nie domyka się i nie da się jej złożyć bez zaokrąglania kolumn.

**Wariant alternatywny, gdyby gutter 32 px miał zostać:** marginesy 100 px, pole 1720 px, moduł `(1720 - 5 × 32) / 6 = 260 px`. Też się domyka i to jest druga droga do wyboru.
