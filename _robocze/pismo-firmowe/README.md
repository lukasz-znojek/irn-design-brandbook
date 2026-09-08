# Szablon pisma firmowego IRIN (.docx)

**Ryzyko przed opisem: tego pliku nie otwarto w Wordzie ani w LibreOffice.** W tym kontenerze
LibreOffice nie ma modułu Writer (brak `writer.xcd` w `/usr/lib/libreoffice/share/registry/`,
`soffice --convert-to pdf` zwraca „source file could not be loaded"), nie ma też `pdftoppm`.
Wszystkie liczby niżej pochodzą z **odczytu OOXML wprost z pliku** oraz z **symulacji układu
w Chromium** na tych samych wartościach i na prawdziwych krojach Manrope i Inconsolata.
To nie jest to samo, co render Worda - patrz sekcja „Czego nie sprawdzono".

Pliki:

| Plik | Co to jest |
|---|---|
| `pismo-irin.docx` | szablon: A4 pion, wyłącznie placeholdery w nawiasach kwadratowych |
| `buduj-pismo.js` | generator; każda liczba w szablonie jest tu policzona, nie wpisana |
| `znak-poziom.png` | znak wstawiony do nagłówka, 1572 × 332 px, Atrament `#07090C`, tło przezroczyste |
| `symulacja-ukladu.html` | odwzorowanie tych samych wymiarów w HTML, do pomiaru i podglądu |
| `podglad-ukladu.png` | render symulacji, 1800 × 2800 px przy 7,5591 px/mm; obraz jest większy od A4 o białe tło okna |
| `mierz-pasma-tuszu.py` | dekoder PNG bez zależności; wypisuje pasma tuszu w milimetrach |

## Jak to odtworzyć

```
node buduj-pismo.js                    # potrzebuje pakietu docx (npm), zmienna DOCX wskazuje sciezke
CH=/opt/pw-browsers/chromium-1194/chrome-linux/chrome
"$CH" --headless --disable-gpu --no-sandbox --allow-file-access-from-files \
      --virtual-time-budget=8000 --window-size=900,1400 --force-device-scale-factor=2 \
      --hide-scrollbars --screenshot=podglad-ukladu.png file://$PWD/symulacja-ukladu.html
python3 mierz-pasma-tuszu.py podglad-ukladu.png 7.5590551
```

## Skąd wzięły się wymiary

Wszystko z warstwy 1, nic z tej sesji:

| Wielkość | Wartość | Źródło |
|---|---|---|
| Format, marginesy 18 / 20 / 28 / 20 mm | pole treści 170 × 251 mm | `siatka-a4.md` |
| Szerokość n kolumn | `29n - 4` mm: 25, 54, 83, 112, 141, 170 | `siatka-a4.md` |
| Jednostka odstępu | 6 mm i wielokrotności | `siatka-a4.md` |
| Strefa nagłówka | margines górny 18 mm należy do znaku, nie do treści | `siatka-a4.md` |
| Strefa stopki | margines dolny 28 mm; tekst stopki nie bliżej niż 12 mm od krawędzi | `siatka-a4.md` |
| Stopnie i interlinie | skala px z `typografia.md`, przeliczona 1 px = 0,75 pt | `typografia.md` |
| Barwy: Atrament, Grafit, Szafir Nocny | `#07090C`, `#606369`, `#132246` | `paleta-barw.md` |
| Znak: wariant poziomy, 40 mm | minimum 18 mm; x = 8,44 mm dla 40 mm | `logotyp.md` |
| Cztery pozycje w stopce | art. 206 KSH | `02-szablony-dokumentow/papier-firmowy.md` |

## Co zmierzono w pliku .docx

Odczyt z rozpakowanego archiwum (`unzip -q pismo-irin.docx -d rozp`, potem regex na
`word/document.xml`, `word/styles.xml`, `word/header1.xml`, `word/footer1.xml`):

| Element | Zapis w pliku | W milimetrach | Wymóg |
|---|---|---|---|
| Strona | `w:w="11906" w:h="16838"` | 210,01 × 297,00 | A4 pion |
| Margines górny | `w:top="1020"` | 17,99 | 18 |
| Marginesy boczne | `w:left="1133" w:right="1133"` | 19,99 każdy | 20 |
| Margines dolny | `w:bottom="1587"` | 27,99 | 28 |
| Nagłówek od krawędzi | `w:header="510"` | 9,00 | wewnątrz 18 |
| Stopka od krawędzi | `w:footer="680"` | 11,99 | nie mniej niż 12 |
| Znak | `cx="1440000" cy="304122"` EMU | 40,000 × 8,448 | min. 18 szerokości |
| Tabulator prawy w stopce | `w:pos="9637"` | 169,99 | 170 |
| Wcięcie prawe korpusu | `w:right` w stylach | 58,00 → blok 112 | 4 kolumny |
| Wcięcie prawe adresata | `w:right` w `irinAdresat` | 86,99 → blok 83 | 3 kolumny |
| Wcięcie lewe sygnatury | `w:left` w `irinSygnatura` | 86,99 → blok 83 | 3 kolumny |

Pole treści z zapisu: 11906 - 1133 - 1133 = 9640 twipów = **170,04 mm**. Siatka wymaga 170 mm.
Nadmiar 0,04 mm bierze się z zaokrąglenia 20 mm do 1133 twipów (dokładnie 1133,858) i jest
poniżej rozdzielczości druku.

Osiem stylów akapitu i jeden styl znaku, wszystkie z przedrostkiem `irin`:

| Styl | Stopień | Interlinia | Tracking | Uwaga |
|---|---|---|---|---|
| `irinKorpus` | 20 półpkt = 10 pt | 314 tw = 15,70 pt | 0 | także styl domyślny dokumentu |
| `irinLead` | 24 = 12 pt | 336 tw = 16,80 pt | 0 | |
| `irinTemat` | 36 = 18 pt | 396 tw = 19,80 pt | -4 tw | `outlineLvl=1`, widoczny w nawigacji Worda |
| `irinPodsekcja` | 24 = 12 pt | 312 tw = 15,60 pt | 0 | `outlineLvl=2` |
| `irinKicker` | 21 = 10,5 pt | 252 tw = 12,60 pt | +46 tw | wersaliki |
| `irinMeta` | 15 = 7,5 pt | 225 tw = 11,25 pt | 0 | |
| `irinAdresat` | 20 = 10 pt | 314 tw | 0 | `w:after=0`, wiersze adresu bez odstępu |
| `irinSygnatura` | 20 = 10 pt | 314 tw | 0 | wyrównanie do prawej |
| `irinKod` (znak) | 16 = 8 pt | - | 0 | Inconsolata, dane techniczne |

Tracking policzony ze skali, nie dobrany: kicker 0,22em × 10,5 pt × 20 = **46 twipów**;
temat -0,01em × 18 pt × 20 = **-4 twipy**.

W pliku występują dokładnie dwa kroje: `Manrope` i `Inconsolata`. Sprawdzenie:
`grep -o 'w:ascii="[^"]*"' word/*.xml | sort -u`.

## Co zmierzono w symulacji układu

Pomiar w Chromium po `document.fonts.ready` (bez tego czekania fonty jeszcze nie działają
i wyniki są nieprawdziwe - patrz „Pułapki narzędzi"). Pozycje bloków względem górnej krawędzi
pola treści:

| Blok | Góra | Dół | Szerokość | Linie |
|---|---|---|---|---|
| etykieta ADRESAT | 24,00 | 27,97 | 112,00 | 1 |
| adresat, trzy wiersze | 27,97 | 44,59 | 83,00 | 1 + 1 + 1 |
| data | 56,58 | 62,65 | 170,04 | 1 |
| kicker | 74,65 | 79,09 | 112,00 | 1 |
| temat | 85,09 | 92,08 | 112,00 | 1 |
| lead | 104,08 | 115,93 | 112,00 | 2 |
| podsekcja | 127,93 | 133,43 | 112,00 | 1 |
| korpus, akapit 1 | 139,43 | 156,05 | 112,00 | 3 |
| korpus, akapit 2 | 162,05 | 173,13 | 112,00 | 2 |
| dane techniczne | 197,13 | 205,06 | 112,00 | 1 |
| sygnatura | 229,06 | 237,69 | 83,04 | 1 + 1 |

**Wykorzystane 237,69 mm z 251,02 mm, zapas 13,33 mm** - czyli ponad dwie jednostki rytmu.
Szablon mieści się na jednej stronie i ma miejsce na dłuższy temat albo dłuższą nazwę adresata.

Odstępy między blokami: 12, 12, 6, 12, 12, 6, 6, 24, 24 mm. **Każdy jest wielokrotnością 6 mm** -
to jest ta reguła z `siatka-a4.md`, której pilot papieru firmowego nie trzymał.

Pasma tuszu odczytane z `podglad-ukladu.png` (`mierz-pasma-tuszu.py`, próg 200 na kanale R):

| Element | Pasmo od góry strony | Sprawdzenie |
|---|---|---|
| znak | 9,00 - 17,33 mm | mieści się w strefie 18 mm; góra 9,00 ≥ x = 8,44 mm |
| ostatni blok treści | do 255,06 mm | pole treści kończy się na 269 mm |
| linia stopki | 270,67 mm, szerokość 169,86 mm | „na dolnej krawędzi pola treści albo niżej" - jest niżej |
| ostatni wiersz stopki | do 284,43 mm | 12,57 mm od krawędzi strony, próg 12 mm trzymany |
| lewa krawędź treści | 19,98 - 20,64 mm | margines 20 mm; wahanie to lewy odsadź glifu `[` |
| prawa krawędź stopki | 189,84 mm | pole treści kończy się na 190,0 mm |

Stopka ma trzy wiersze i żaden się nie łamie. Szerokości zmierzone: 89,67 + 19,90,
118,69 + 10,84, 76,80 + 16,92 mm - wszystkie sumy poniżej 170,04 mm, więc lewa i prawa
część nie kolidują.

## Kontrast - policzony w tej sesji, nie przepisany

Wzór WCAG 2.1, pary na papierze białym (dokument Worda nie ma tła strony):

| Pierwszy plan | Tło | Kontrast | AA 4,5:1 | AAA 7:1 |
|---|---|---|---|---|
| Atrament `#07090C` | biel `#FFFFFF` | **19,94:1** | tak | tak |
| Szafir Nocny `#132246` | biel `#FFFFFF` | **15,61:1** | tak | tak |
| Grafit `#606369` | biel `#FFFFFF` | **6,02:1** | tak | nie |
| Atrament `#07090C` | Kość Słoniowa `#F7F3E9` | **17,99:1** | tak | tak |
| Szafir Nocny `#132246` | Kość Słoniowa `#F7F3E9` | **14,09:1** | tak | tak |
| Grafit `#606369` | Kość Słoniowa `#F7F3E9` | **5,44:1** | tak | nie |

Najsłabszy kontrast niesie najmniejszy stopień: Grafit 7,5 pt w stopce i w metadanych,
6,02:1 na bieli, czyli **1,52 zapasu nad progiem AA** i brak AAA. Wynik 17,99:1 dla pary
bazowej zgadza się z `paleta-barw.md` policzonym niezależnie - to potwierdzenie tamtej liczby,
nie jej przepisanie.

## Ograniczenia Worda - zmierzone, nie założone

Word przechowuje stopień pisma w **półpunktach**, więc nie każdy poziom skali da się zapisać:

| Poziom skali | px | Dokładnie w pt | Półpunkty | Zapisane | Błąd |
|---|---|---|---|---|---|
| Korpus | 13,5 | 10,125 | 20,25 | **20 = 10 pt** | -0,125 pt = -1,2 % |
| Dane techniczne (Inconsolata) | 10,5 | 7,875 | 15,75 | **16 = 8 pt** | +0,125 pt = +1,6 % |
| pozostałe siedem poziomów | - | - | całkowite | bez zmian | 0 |

Konsekwencja dla interlinii korpusu: zapisano **314 twipów = 15,70 pt**, czyli wartość
bezwzględną ze skali (13,5 px × 1,55 = 20,93 px = 5,54 mm), a nie 1,55 × 10 pt = 310 twipów.
Wybrano wartość bezwzględną, bo `siatka-a4.md` liczy dryf rytmu w milimetrach na linię;
kosztem jest **efektywny mnożnik 1,57 zamiast 1,55**. Odwrotny wybór (310 tw) zachowałby
mnożnik i zmienił położenie każdej linii na stronie.

**Wagi Manrope.** Word wybiera w rodzinie tylko regular albo bold, więc:

| Waga w skali | Poziom | Co zrobi Word |
|---|---|---|
| 400 | korpus, metadane, adresat | regular, zgodnie |
| 500 | lead | **regular** - lead różni się od korpusu wyłącznie stopniem |
| 600 | temat, podsekcja | **bold (700)** - cięższe niż w projekcie |
| 700 | kicker | bold, zgodnie |

Skutek uboczny jest korzystny: `typografia.md` ostrzega, że H3 i lead różnią się wyłącznie
wagą i nie powinny stać obok siebie. W Wordzie H3 idzie na 700, a lead na 400, więc te dwa
poziomy rozjeżdżają się mocniej niż w projekcie, nie słabiej.

Aby odzyskać wagi 500 i 600, trzeba zainstalować je jako **osobne rodziny** („Manrope Medium",
„Manrope SemiBold") i wpisać te nazwy w generatorze. Bez tego Word podstawi to, co wyżej.

**Proporcja znaku.** `znak-poziom.png` ma 1572 × 332 px, czyli **4,73494:1**. Obwiednia
ścieżek w SVG to 184,213 × 38,854, czyli **4,74117:1**. Znak w szablonie jest więc szerszy
o **0,13 %** względem artworku - to szerokość antyaliasingu na krawędzi kadrowania, nie
rozciągnięcie. Falsyfikator: kadrowanie z progiem alfa innym niż zero dające inną proporcję.

## Czego nie sprawdzono

| Pozycja | Dlaczego | Falsyfikator |
|---|---|---|
| Render Worda albo LibreOffice | brak modułu Writer w kontenerze, brak `pdftoppm` | otwarcie pliku w Wordzie z zainstalowanym Manrope i pomiar linijką |
| Podstawienie kroju u odbiorcy bez Manrope | zależy od maszyny odbiorcy | otwarcie na czystym Windowsie: Word podstawi krój systemowy i cała skala się przesunie |
| Stopień pisma w druku | `typografia.md` nie ma minimum dla dokumentów regulowanych; korpus 10 pt jest mniejszy od typowych 12 pt w pismach urzędowych | wydruk i decyzja właściciela |
| Zachowanie na drugiej stronie | szablon jest jednostronicowy; nagłówek i stopka są zdefiniowane jako `default`, więc powtórzą się, ale przy dłuższej treści warto sprawdzić, czy znak na każdej stronie jest pożądany | pismo dłuższe niż jedna strona |
| CMYK | plik jest w RGB | proof drukarski |

## Pułapki narzędzi, na które ta sesja weszła

Zapisane, żeby następna sesja nie powtarzała pomiarów:

1. **`--virtual-time-budget` nie gwarantuje, że fonty są już podstawione.** Pierwszy pomiar
   układu wyszedł o 5,81 mm krótszy niż powtórzony na tym samym pliku: 241,39 zamiast
   247,20 mm, bo Chromium zmierzył tekst krojem zastępczym (próbka
   „Instytut Rozwoju i Nauki" 37,63 mm zamiast 38,84 mm w Manrope). Pomiar musi wisieć na
   `document.fonts.ready`.
2. **Zrzut ekranu o wysokości okna równej wysokości strony obcina dolne pasmo.** Przy
   `--window-size=794,1123` (dokładnie 297 mm) stopka nie renderowała się wcale; przy
   `--window-size=900,1400` renderuje się poprawnie. To artefakt zrzutu, nie układu.
3. **Okno niższe niż około 200 px daje pusty raster.** Trzy próby wykadrowania samej stopki
   (okna 60, 76 i 100 px) wyszły całkowicie białe; przy oknie 60 px na każdym
   `--force-device-scale-factor` od 1 do 4 zerowa liczba pikseli ciemniejszych od 200.
   Okno 170 px już renderowało.

## Pozycje otwarte - do decyzji właściciela

1. **Dane kontaktowe w stopce są placeholderami: `[e-mail firmowy]` i `[telefon]`.**
   Konwencja z `02-szablony-dokumentow/papier-firmowy.md` wymaga na papierze firmowym
   e-maila, telefonu i adresu strony. `www.irin.pl` wpisano, bo ta wartość jest już
   w commitowanym podpisie mailowym. Dwie pozostałe leżą wyłącznie w `_robocze/pilot-papier-firmowy/`
   (`biuro@irin.pl` i `+48 453 049 912`, zapisane tam jako podane przez foundera 2026-09-03),
   a `_robocze/` nie jest źródłem prawdy bez ponownej weryfikacji. Jedno słowo potwierdzenia
   zamienia dwa placeholdery na wartości.
2. **`Nr pisma: [numer pisma]` nie narzuca formatu.** Zapis `IRIN/RRRR/D/NNNNN` z przekazania
   jest w repozytorium sprawą czekającą na właściciela, więc szablon go nie odtwarza.
3. **Gdzie mają leżeć wytworzone materiały.** Ten katalog jest w `_robocze/`, tak samo jak
   podpis mailowy - a architektura z `CLAUDE.md` ma trzy warstwy i żadna nie jest warstwą
   gotowych plików. Rekomendacja bez zmian: czwarta warstwa `04-materialy/`, bo wtedy reguła
   „`_robocze/` nie jest źródłem prawdy" przestaje kolidować z plikami, które są produktem
   końcowym. Do decyzji nic nie przenoszę.
4. **Szerokość korpusu 112 mm to swobodny wybór projektowy tej sesji, nie wymóg.**
   Pełne 170 mm przy 10 pt daje wiersz około 96 znaków, czyli powyżej zakresu czytelności
   45-75; 112 mm daje około 64 znaki. Zmiana to jedna linia w `buduj-pismo.js`
   (`KORPUS_SZER = KOL(4)` na `KOL(6)`), po niej trzeba powtórzyć pomiar zapasu strony.
