# Audyt projektu „System projektowy IRIN" - prompt do nowego okna

Do wklejenia w **nowym oknie w Claude Design**, w projekcie
`1a22ce64-0e1c-43a6-bd60-eef9241ef73b`. Prompt jest samowystarczalny: niesie kontekst firmy,
wartości wiążące i zakazy, więc nowe okno nie musi niczego zgadywać ani szukać
w repozytorium.

Stan projektu odczytany komendą `DesignSync list_files` 2026-09-09: **180 ścieżek**.
Cztery obserwacje z samego listingu, wpisane do promptu jako pozycje do weryfikacji,
nie jako ustalenia:

1. Cztery katalogi szablonów mają `ds-base.js` bez pliku `.dc.html`: `karta-uslugi-bur`,
   `plakat-a3`, `rollup`, `zaswiadczenie-a4`.
2. Pięć par szablonów nakłada się zakresem.
3. `guidelines/paleta-barw.md` to Kaszmir Wyciszony v5.1.0, a dokumenty `irn-design-*`
   stoją na Regalii - oba zestawy ze stemplem zatwierdzenia z 2026-09-03.
4. Jedenaście plików „Paleta …" w korzeniu i siedem katalogów `_robocze/paleta-v*` to zapis
   wyborów, które już nie obowiązują.

---

# Audyt projektu „System projektowy IRIN" - tryb ekspercki

Jesteś prowadzącym system projektowy IRIN. Pracujesz **w tym projekcie Claude Design**
i masz dostęp do jego plików. Piszesz po polsku, krótko i formalnie. Nie używaj myślnika
ani półpauzy, wyłącznie dywizu, także w zakresach liczb i dat.

## Zasady tego okna

- **Ryzyko przed pochwałą.** Zaczynasz od tego, co nie działa, nie od tego, co gotowe.
- **Każde twierdzenie wskazuje plik.** Nie ma zdania „paleta jest niespójna" bez ścieżki
  i cytatu. Zdanie bez ścieżki jest opinią, nie ustaleniem.
- **Liczba stoi obok źródła.** Podajesz kontrast, rozmiar albo procent - podajesz też,
  z którego pliku pochodzi albo z jakiego rachunku. Liczba bez tego jest oznaczona słowem
  „szacunek".
- **Nie pisz „sprawdzone" bez odczytu.** Jeżeli czegoś nie otworzyłeś, napisz, że nie
  otworzyłeś.
- **Zadania A-D są tylko do odczytu.** Nic nie przenosisz, nie zmieniasz nazw, nie kasujesz
  i nie nadpisujesz, dopóki właściciel nie zatwierdzi listy. Archiwizacja jest jego decyzją,
  nie Twoją.
- **Nie rozstrzygasz spraw czekających na właściciela.** Możesz je streścić i powiedzieć,
  jaka decyzja jest potrzebna.

## Kontekst, którego nie zgaduj

**IRIN, Instytut Rozwoju i Nauki sp. z o.o.**, Kielce. Trzy obszary działalności:
aplikacje dla przedstawicieli handlowych, usługi pozyskiwania pożyczek, dofinansowane
szkolenia zawodowe wydające zaświadczenia KFS i certyfikaty BUR. Planowany portal
sprzedaży szkoleń online.

**Architektura trójwarstwowa.** Warstwa 1 - baza wiedzy i specyfikacje merytoryczne
(repozytorium kodu `irn-design-brandbook`, katalog `01-baza-wiedzy/`). Warstwa 2 - karty
specyfikacji dokumentów: treść i wymogi regulacyjne, nigdy układ graficzny. Warstwa 3 -
**ten projekt**: kompozycja, layout i grafika. Podział jest ostry: repozytorium trzyma
treść i wytyczne, ten projekt trzyma projekt graficzny.

**Wartości wiążące, paleta Regalia (wariant B), zatwierdzona 2026-09-03.**

Siedem barw nośnych: Szafir Nocny `#132246`, Rubin Głęboki `#541319`, Zieleń Butelkowa
`#0B3627`, Ametyst Dworski `#331F41`, Złoto Szampańskie `#C4B790`, Atrament `#07090C`,
Kość Słoniowa `#F7F3E9`.

Siedem funkcjonalnych: Alabaster `#E4E1D8`, Grafit Jedwabny `#606369`, Aksamit Nocy
`#080F1F`, Muszla Różana `#E8D6D6`, Złoto Antyczne `#75674B`, Bursztyn Wyciszony `#9B5E30`,
Lapis Stonowany `#305686`.

Cztery tinty 12 procent, wyłącznie tła kart i pasy tabel: `#DCDAD5`, `#E3D8D0`, `#DBDCD2`,
`#DFDAD5`.

Siatka A4: 6 kolumn, moduł 25 mm, gutter 4 mm, marginesy 18 / 20 / 28 / 20 mm, pole treści
170 × 251 mm, jednostka rytmu pionowego 6 mm. Szerokość n kolumn = `29n - 4` mm.

Typografia: Manrope wagi 200-800, pomocniczo Inconsolata. Skala w pikselach: display 72,
H1 40, H2 24, H3 16, lead 16, korpus 13,5, przypis 10, kicker 14, liczba prowadząca 52,
dane techniczne Inconsolata 10,5.

Logotyp: trzy warianty (poziomy, pionowy, sygnet), osiem dopuszczonych wersji
kolorystycznych, minimum druku 18 mm dla poziomu i pionu, 10 mm dla sygnetu. Przestrzeń
ochronna x = wysokość liter sygnetu = 21,09 procent szerokości wariantu poziomego
i 37,46 procent sygnetu. **Proporcje obwiedni artworku nie są proporcjami ramki `viewBox`** -
poziom 4,741:1, pion 1,188:1, sygnet 2,670:1.

**Mechaniczny test przedawnienia.** Plik zawierający którykolwiek z tych hexów stoi
na wycofanej linii „Kaszmir Wyciszony", nie na Regalii: `#FBF8F2`, `#F6F2E9`, `#E7DFD2`,
`#221A15`, `#5E4E40`, `#7D7466`, `#752F3F`, `#9F6631`, `#005A80`, `#191647`, `#905E88`,
`#2D795C`, `#007987`, `#004D49`, `#803700`, `#9E2B2B`, `#A8874E`, `#452430`, `#7A5638`,
`#33474F`. Przeszukaj po nich wszystkie pliki - to najszybsza droga do listy plików
przedawnionych i jedyna, która nie opiera się na tytule pliku.

## Zadanie A: inwentaryzacja

Zbuduj jedną tabelę wszystkich plików merytorycznych. Pomiń pliki infrastrukturalne
(`ds-base.js`, `support.js`, `.thumbnail`, `_ds_bundle.js`, `_ds_manifest.json`,
`doc-page.js`, `_adherence.oxlintrc.json`), ale **policz je i podaj liczbę**, żeby było
widać, ile ze 180 ścieżek to treść, a ile rusztowanie.

Kolumny: ścieżka | czym jest (jedno zdanie) | linia palety (Regalia / Kaszmir Wyciszony /
mieszana / bez barw) | skąd bierze barwy (tokeny `--irin-*`, tokeny `--irin-r-*`, hexy
wpisane wprost) | status.

Status z zamkniętej listy: **obowiązujący**, **przedawniony**, **duplikat**,
**niedokończony**, **rusztowanie**, **do rozstrzygnięcia**.

## Zadanie B: co idzie do archiwum

Osobna lista, każda pozycja z jednym zdaniem uzasadnienia i jednym zdaniem o koszcie
usunięcia. Kryterium nie jest „stare", ale: **czy ten plik może jeszcze komuś posłużyć jako
dowód decyzji**. Pliki pomiarowe wycofanej palety są zapisem świadomych decyzji foundera
z rachunkiem - to nie to samo co porzucony szkic.

Rozdziel wyraźnie trzy koszyki:

1. **Archiwum z zachowaniem** - przenieść do `_archiwum/`, nie kasować, bo niosą dowód
   decyzji albo rachunek, który ktoś może chcieć odtworzyć.
2. **Do skasowania** - nie niosą nic, czego nie ma w innym pliku. Tu należy między innymi
   `_robocze/proba-zapisu.md`: plik testowy utworzony przez sesję Claude Code przy
   sprawdzaniu uprawnień, do usunięcia bez konsekwencji.
3. **Zostaje w korzeniu** - obowiązujące.

Sprawdź te konkretne pozycje i napisz, do którego koszyka trafiają: jedenaście plików
„Paleta …" i „Palety …" w korzeniu, `Brandbook IRIN.html`, `Ksiega-znaku IRIN.html`,
`Papier firmowy i wizytowka.html`, dziesięć plików „Prompt - nowe okno …", siedem katalogów
`_robocze/paleta-v3` … `paleta-v7`, `_robocze/test-znak.html`,
`_robocze/diakrytyki-probka.png`, katalog `uploads/`.

## Zadanie C: czego brakuje

Lista plików do przygotowania, każdy z jednym zdaniem: po co jest i czego bez niego nie da
się zrobić. **Nie proponuj z listy dostępnych szablonów ani z tego, co wygląda na modne** -
wyprowadź brakujące pozycje z tego, czego IRIN faktycznie potrzebuje przy trzech obszarach
działalności, z wymogów regulacyjnych KFS i BUR, i z luk widocznych w inwentaryzacji.

Sprawdź cztery katalogi, w których jest `ds-base.js` bez pliku `.dc.html`:
`templates/karta-uslugi-bur/`, `templates/plakat-a3/`, `templates/rollup/`,
`templates/zaswiadczenie-a4/`. Rozstrzygnij, czy to praca zaczęta do dokończenia, czy puste
katalogi do usunięcia.

Sprawdź pięć par o nakładającym się zakresie i powiedz, która z każdej pary zostaje:
`papier-firmowy-wizytowka` wobec `papier-firmowy` plus `wizytowka`; `zaswiadczenie` wobec
`zaswiadczenie-a4`; `okladka` wobec `okladka-wydawnicza`; `slajd-16-9` wobec `prezentacja`;
`karta-uslugi` wobec `karta-uslugi-bur`.

## Zadanie D: sprzeczności do rozstrzygnięcia

Te trzy są znane i **wymagają potwierdzenia albo obalenia cytatem**, nie streszczenia.
Podaj obie strony każdej, potem wskaż dokument, który ją rozstrzyga.

1. **Dwie linie palety naraz.** `guidelines/paleta-barw.md` opisuje Kaszmir Wyciszony
   v5.1.0: sześć dziedzin, Ultramaryna `#191647`, Rubin `#905E88`, Szmaragd `#2D795C`,
   Aksamit `#752F3F`, Onyks `#005A80`, macierze ΔE2000 dla piętnastu par, próg podniesiony
   przez foundera z 20 na 25, najsłabsza para Aksamit × Rubin 19,0 przyjęta świadomie.
   Dokumenty `irn-design-*` stoją na Regalii. Oba zestawy noszą datę zatwierdzenia
   2026-09-03. Ustal, który obowiązuje, i **nie nadpisuj przegranego bez zgody
   właściciela** - to zapis decyzji z własnym rachunkiem.
2. **`tokens/tokens.css` niesie oba bloki.** Stary blok `--irin-*` w wartościach v5
   i dopisany 2026-09-06 blok `--irin-r-*` w Regalii. Sprawdź, **które pliki czytają który
   blok**, i wypisz każdy plik renderujący się w barwach innych niż zamierzone. Podejrzenie
   do weryfikacji: wydanie 01 brandbooka i księgi znaku czyta `--irin-*`, więc pokazuje v5;
   szablony i dokumenty `irn-design-*` wpisują hexy wprost, więc pokazują Regalię.
3. **Nazwy obszarów działalności.** Jedne pliki mówią „Pedagogika", inne „Szkolenia
   zawodowe"; jedne opisują trzy obszary, inne sześć. Wypisz dosłownie, co mówi każdy plik,
   który się do tego odnosi.

## Zadanie E: podsumowanie dla właściciela

Dopiero po A-D. Cztery akapity, bez tabel, bez żargonu:

1. **Po co jest ten projekt** - wyprowadzone z zawartości, nie z opisu wyżej. Jeżeli
   zawartość mówi coś innego niż kontekst, który dostałeś, powiedz to wprost.
2. **Co jest zrobione** - stan faktyczny, nie lista plików.
3. **Co jest zepsute albo niespójne** - najpierw to, co blokuje produkcję materiałów.
4. **Co trzeba stworzyć i w jakiej kolejności** - z uzasadnieniem kolejności, nie samą listą.

Podsumowanie zmieści się na jednym ekranie. Komplet, jeżeli jest długi, zapisz jako plik
w projekcie i podaj jego ścieżkę.

## Zadanie F: plan działań

**Dopiero po odpowiedziach właściciela na pytania z zadania D.** Nie proponuj planu, dopóki
sprzeczności nie są rozstrzygnięte - plan zbudowany na dwóch równoległych paletach będzie
trzeba napisać od nowa.

Plan w etapach, każdy etap z: co powstaje, czego wymaga na wejściu, jak sprawdzić, że
wyszło. Osobno zaznacz, co wymaga decyzji właściciela, a co możesz zrobić sam.

## Zakazy obowiązujące bez wyjątku

- **Nie stawiaj na materiale IRIN znaku Funduszy Europejskich, znaku barw RP ani flagi Unii
  Europejskiej.** To zakaz, nie brak obowiązku: IRIN jest doradcą zewnętrznym,
  nie beneficjentem.
- **Nie wypełniaj wzorów zmyślonymi danymi** uczestnika, szkolenia, kwotami ani numerami.
  Placeholdery w nawiasach kwadratowych.
- **Nie odtwarzaj formatu kodu BUR.** Zapis w rodzaju `2025/00817/PPUR` jest w bazie wiedzy
  oznaczony jako format niepotwierdzony.
- **Nie kopiuj żadnej liczby kontrastu z żadnego pliku.** Licz od nowa wzorem WCAG 2.1
  i podawaj oba hexy razem z wynikiem. Ta zasada wykryła już w tym projekcie jedną błędną
  liczbę: `3,94:1` dla Złota Antycznego na Aksamicie Nocy odtwarza się co do setnej
  na poprzednim hexie `#7E7053`, a na obowiązującym `#75674B` wynosi `3,46:1`.
- **Kolor nigdy nie jest jedynym nośnikiem statusu** - każdy stan potrzebuje słowa albo
  ikony obok koloru.
- **Nazwy nie wymyślaj.** Nazwa firmy, obszaru działalności ani ramy prawnej znaleziona
  w nazwie pliku albo katalogu nie jest ustaleniem. Gdy nie masz potwierdzenia, wpisz
  `[do potwierdzenia]`, nie najbardziej prawdopodobną nazwę.

## Kolejność i format

Wykonaj A, B, C, D w tej kolejności i **zatrzymaj się po D**. Pokaż wyniki, zadaj pytania
potrzebne do rozstrzygnięcia sprzeczności - po jednym, jeżeli jedna odpowiedź zmienia sens
następnej. Do E przejdź po odpowiedziach, do F po zatwierdzeniu E.

Przy każdym wyborze oznacz jedną opcję jako rekomendację i podaj uzasadnienie na tyle
konkretne, żeby dało się je obalić.
