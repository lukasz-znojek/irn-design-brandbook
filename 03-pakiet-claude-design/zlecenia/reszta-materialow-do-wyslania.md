# Reszta materiałów IRIN: instrukcja do kolejnego okna Claude Design

Stan na 2026-09-04, po audycie czterech dokumentów wzorcowych i ośmiu szablonów.

---

## Część A: audyt dla właściciela

### Co sprawdziłem i czym

| Co | Pomiar | Wynik |
|---|---|---|
| Stan projektu | `DesignSync list_files` | 8 szablonów w `templates/` **gotowych**, cztery dokumenty `irn-design-*`, sześć iteracji palety w `_robocze/paleta-v3` … `v7` |
| 12 twierdzeń kontrastowych z `irn-design-paleta-kolorow.md` | przeliczenie wzorem WCAG 2.1 | **11 zgodnych co do setnej**, 1 rozbieżne |
| Macierz 48 zestawień z `irn-design-ksiega-znaku.md` | to samo | **45 zgodnych**, 3 rozbieżne |
| Sześć wartości „policzonych w tej sesji" z księgi znaku | to samo | 5 zgodnych, 1 rozbieżna |
| Paleta w `tokens/tokens.css` | `get_file` | **ani Kaszmir Wyciszony, ani Regalia** - wersja v5 z sześcioma obszarami i wartościami spoza obu palet |
| Czy szablony zależą od tokenów | `get_file` na `templates/zestaw-drobnych/` | **nie** - hexy Regalii wpisane wprost, więc renderują się poprawnie |
| Proporcje znaku | obwiednie z szablonu wobec `viewBox` w plikach SVG | zapisane proporcje to proporcje **pustej ramki**, nie znaku |

### Cztery korekty liczbowe

| # | Gdzie | Podane | Policzone | Przyczyna wskazana |
|---|---|---|---|---|
| 01 | Złoto Antyczne na Aksamicie Nocy - w palecie **i** w rozdz. „Dark mode" brandbooka | 3,94:1 | **3,46:1** | 3,94 to kontrast **poprzedniej** wartości `#7E7053`, sprzed pociemnienia do `#75674B`; odtwarza się na starym hexie co do setnej. Tabela par zabronionych nie została przeliczona po zmianie |
| 02 | „Cztery barwy nośne różnią się o mniej niż 2 punkty" | < 2,00 | **2,03** | rozpiętość Szafir 14,09 do Zieleń 12,06. Twierdzenie nieprawdziwe o 0,03; **reguła, którą uzasadniało, zostaje** i ma mocniejszą podstawę: Rubin i Zieleń wypadają w mono identycznie, 70 % K |
| 03 | Kolumna tintu w macierzy 48 zestawień | Ametyst 10,64 · Rubin 10,13 · Zieleń 9,57 | **10,70 · 10,11 · 9,66** | trzy liczby policzono wobec tintu Szafiru `#DCDAD5`, nie wobec tintu z własnego wiersza - wbrew podpisowi pod tabelą |
| 04 | Biel czysta na Aksamicie Nocy | 19,17:1 | **19,12:1** | żadna sąsiednia wartość Aksamitu nie odtwarza 19,17; przepisanie. Pozycja i tak nieużywana w składzie |

**Żaden z tych czterech błędów nie zmienia wyroku projektowego** - pary zabronione zostają zabronione, tinty przechodzą z ogromnym zapasem, reguła o dziedzinach stoi. Wszystkie cztery wpisałem jako korekty do `01-baza-wiedzy/identyfikacja/paleta-barw.md` i `tokeny/palette-irin.json`.

### Znalezisko własne: proporcje znaku

**Proporcje w `logotyp.md`, `CLAUDE.md` i obu wydaniach księgi znaku to proporcje `viewBox`, nie znaku.**

| Wariant | `viewBox` | Obwiednia artworku | Artwork zajmuje |
|---|---|---|---|
| poziom | 1,773:1 | **4,741:1** | 65,5 % szerokości ramki, 16,0 % powierzchni |
| pion | 1,135:1 | **1,188:1** | 56,1 % szerokości, 30,1 % powierzchni |
| sygnet | 1,135:1 | **2,670:1** | 56,1 % szerokości, 13,4 % powierzchni |

Skutek: `width:18mm` na kontenerze bez nadpisania `viewBox` daje znak o szerokości **11,8 mm**, czyli poniżej minimum, którego pilnujemy. Żeby znak miał 18 mm, kontener musi mieć **27,5 mm** (poziom) albo **32,1 mm** (pion); sygnet 10 mm wymaga kontenera **17,8 mm**. Szablony w `templates/` robią to poprawnie, nadpisując `viewBox` obwiednią. Wpisane do `logotyp.md` wydanie 02.

### Co zamknęły szablony

- **Miara x policzona** z obwiedni: sygnet **37,46 %** szerokości, poziom **21,09 %**. Dla sygnetu 22 mm x = 8,24 mm. To zamyka pozycję, która wisiała od trzech tur.
- **Diakrytyki na wszystkich siedmiu wagach Manrope** plus dwie wagi Inconsolaty, w jednym miejscu do obejrzenia (`templates/zestaw-drobnych/`). Wymaga tylko Twojego spojrzenia.
- **Sygnet na rewersie wizytówki:** zmierzone, że **30 mm mieści się** na 85 × 55 mm z zapasem (marginesy po 27,5 mm, przestrzeń ochronna x = 11,24 mm). Twoja prośba o powiększenie ma wreszcie liczbę.

### Co zaktualizowałem w repozytorium

`01-baza-wiedzy/identyfikacja/paleta-barw.md` (przepisany na Regalię, wszystkie kontrasty przeliczone skryptem), `tokeny/palette-irin.json` (v3, z korektami i kolizjami rol), `identyfikacja/logotyp.md` (wydanie 02: osiem wersji, matryca 48 zestawień, proporcje artworku, miara x, dziesięć zakazów), `CLAUDE.md`, `MAPA-DROGOWA.md`, `01-baza-wiedzy/00-INDEX.md`, `identyfikacja/README.md`, plus banner archiwalny na `propozycja-palety-i-siatki-do-potwierdzenia.md`.

### Jedna rzecz, której nie zrobiłem bez Twojej zgody

**`tokens/tokens.css` w projekcie Claude Design.** Nadpisanie go zmieniłoby barwy w wydaniu 01 brandbooka i księgi znaku, bo te pliki czytają `--irin-*`. Bezpieczny wariant: **dopisać** tokeny Regalii pod nowymi nazwami i zostawić stare jako przestarzałe z niezmienionymi wartościami - wtedy nic się nie psuje, a nowa praca ma czym się posługiwać. Cofnięcie: wysłanie poprzedniej wersji pliku, którą mam.

---

## ——— POCZĄTEK TEKSTU DO WKLEJENIA ———

Kontynuujemy system projektowy IRIN. Cztery dokumenty wzorcowe i osiem szablonów uniwersalnych są
gotowe. Ta tura robi **resztę nośników**.

### Co jest zrobione - wczytaj, nie przerabiaj

**Cztery dokumenty wzorcowe. To one są źródłem prawdy:**

1. `irn-design-paleta-kolorow.html` + `.md` - paleta finalna **Regalia**: 7 barw nośnych,
   7 funkcjonalnych, 4 tinty dziedzinowe 12 %.
2. `irn-design-ksiega-koloru.html` - księga koloru, wydanie 01, 13 stron, rozdz. 00-10.
3. `irn-design-ksiega-znaku.html` + `.md` - księga znaku, wydanie 02, 15 stron: osiem wersji
   kolorystycznych, matryca 48 zestawień, dobór w trzech krokach, dwanaście antywzorców.
4. `irn-design-brandbook.html` + `.md` - brandbook, wydanie 02, 32 strony, rozdz. 00-30:
   typografia, siatka, wszystkie nośniki, dane i wykresy, dark mode, motion, dostępność, governance.

**Osiem szablonów uniwersalnych w `templates/`:** `karta-uslugi`, `zaswiadczenie`, `tabela-danych`,
`okladka`, `katalog-uslug`, `slajd-16-9`, `notatka-wewnetrzna`, `zestaw-drobnych`. Wszystkie na
Regalii, z hexami wpisanymi wprost. **Nie przerabiaj ich** - to z nich składasz nośniki.

**Czego nie czytasz jako źródła:** `Brandbook IRIN.html` (wydanie 01, 60 stron),
`Ksiega-znaku IRIN.html` (wydanie 01, 11 stron), `guidelines/paleta-barw.md`,
`guidelines/logotyp-wersje-kolorystyczne.md`, `guidelines/zasady-stosowania-znaku.md`.
Wszystkie opisują **poprzednią paletę** i żadna ich wartość barwna nie obowiązuje.
`Papier firmowy i wizytowka.html` też nie jest wzorem - stoi na poprzedniej palecie i jest
do ponownego wydania w tej turze.

### Pułapka, o której musisz wiedzieć: trzy palety w jednym projekcie

`tokens/tokens.css` **nie niesie Regalii**. Jest w wersji v5, z sześcioma obszarami i wartościami
spoza obu palet (`--irin-aksamit: #752F3F`, `--irin-onyks: #005A80`, `--irin-werdykt: #004D49`).
Synchronizacja arkusza jest po stronie repozytorium kodu i jeszcze nie nastąpiła.

**Dlatego: barwy podajesz wartością hex albo własnymi zmiennymi `--p-*`, nigdy tokenem
`--irin-*` barwnym.** Z `tokens.css` wolno wziąć wyłącznie `--irin-kroj`, `--irin-kroj-mono`
i zmienne siatki (`--irin-modul`, `--irin-gutter`, marginesy) - te są poprawne.

### Cztery korekty liczbowe do wniesienia

Przeliczyłem wszystkie liczby kontrastu w dokumentach wzorcowych. Cztery są błędne. Żadna nie
zmienia wyroku projektowego, ale **używaj wartości poprawionych**:

| Gdzie | Było | Jest |
|---|---|---|
| Złoto Antyczne `#75674B` na Aksamicie Nocy `#080F1F` | 3,94:1 | **3,46:1** |
| Rozpiętość czterech barw nośnych | < 2,00 punktu | **2,03 punktu** |
| Ametyst na tincie Ametystu `#DFDAD5` | 10,64 | **10,70** |
| Rubin na tincie Rubinu `#E3D8D0` | 10,13 | **10,11** |
| Zieleń na tincie Zieleni `#DBDCD2` | 9,57 | **9,66** |
| Biel czysta na Aksamicie Nocy | 19,17 | **19,12** |

Przyczyna pierwszej: 3,94 to kontrast poprzedniej wartości Złota Antycznego `#7E7053`. Przyczyna
trzech tintowych: policzono je wobec tintu Szafiru, nie wobec tintu z własnego wiersza.

### Znak: proporcja ramki nie jest proporcją znaku

Pliki SVG mają duży przezroczysty margines. Obwiednie artworku, zmierzone:

| Wariant | `viewBox` | Obwiednia artworku | Artwork zajmuje szerokości |
|---|---|---|---|
| poziom | 281,333 × 158,667 | **184,213 × 38,854** | 65,5 % |
| pion | 184,837 × 162,834 | **103,728 × 87,312** | 56,1 % |
| sygnet | 184,837 × 162,834 | **103,728 × 38,853** | 56,1 % |

**Nadpisuj `viewBox` obwiednią artworku**, tak jak robią to szablony w `templates/`, wpisując
obwiednie jako stałe. Wtedy szerokość kontenera równa się szerokości znaku i minimum 18 mm znaczy
to, co ma znaczyć. **Nie mierz w czasie działania** - `getBBox` zaraz po wstrzyknięciu SVG potrafi
zwrócić 0 × 0 i wtedy znak rośnie poza strefę; to zmierzony błąd, opisany w kodzie szablonu
`zestaw-drobnych`.

**Przestrzeń ochronna x** to wysokość artworku: **37,46 % szerokości** dla sygnetu i **21,09 %**
dla poziomu. Sygnet 22 mm → x = 8,24 mm; poziom 60 mm → x = 12,66 mm.

### Co robimy w tej turze - reszta nośników

Każdy nośnik według rozdziału brandbooka, który go opisuje. Składasz je z ośmiu szablonów, nie
od zera. Numer rozdziału podaję, żebyś nie szukał.

**Tura A - nośniki firmowe. Te idą pierwsze, bo dwa z nich są dziś na martwej palecie.**

| Plik | Nośnik | Rozdz. | Wariantów |
|---|---|---|---|
| `templates/papier-firmowy/` | Papier firmowy A4, **ponowne wydanie na Regalii** | 13 | 4: trzy dziedziny plus neutralny |
| `templates/wizytowka/` | Wizytówka 85 × 55 mm, **ponowne wydanie** | 14 | 5 plików: 4 awersy plus 1 rewers wspólny |
| `templates/koperta/` | Koperta DL i C5 | 15 | 1 |
| `templates/podpis-mailowy/` | Podpis mailowy | 15 | 1 |
| `templates/favicon/` | Favicon i awatar, komplet 16 / 32 / 180 / 512 px | 23 | 1 komplet |

**Sygnet na rewersie wizytówki: podnieś do 30 mm.** Zmierzone: mieści się na 85 × 55 mm z zapasem -
po 27,5 mm marginesu bocznego, przy przestrzeni ochronnej x = 11,24 mm. Dotychczasowe 22 mm było
wartością bez uzasadnienia, a właściciel prosił o powiększenie dwa razy. Podaj zmierzoną szerokość
przy oddaniu.

**Favicon 16 i 32 px jest falsyfikatorem minimum sygnetu 10 mm / 44 px.** Napisz wprost, co
w sygnecie przestaje się czytać poniżej 44 px, i czy komplet wymaga uproszczonego rysunku znaku.
Uproszczenie jest utworem pochodnym - proponujesz, nie wprowadzasz.

**Tura B - nośniki wydawnicze i prezentacyjne.**

| Plik | Nośnik | Rozdz. | Wariantów |
|---|---|---|---|
| `templates/okladka-wydawnicza/` | Okładka wydawnicza | 16 | 4 |
| `templates/prezentacja/` | Prezentacja 16 : 9 | 17 | 2 typy slajdu |
| `templates/rollup/` | Roll-up 85 × 200 cm | 18 | 4 |
| `templates/plakat-a3/` | Plakat A3 | 18 | 4 |

**Okładka jest jedynym nośnikiem blisko limitu złota: 4,7 % przy progu 5 %.** Podaj policzony
procent zadruku złotem przy każdym wariancie. Pas dolny nie rośnie powyżej 4 mm, a złota ramka
albo tłoczona pieczęć wykluczają pas - jedno albo drugie.

**Siatka slajdu 16 : 9:** użyj propozycji, która stoi w `templates/slajd-16-9/`, i **powtórz przy
oddaniu jej rachunek szerokości**. Jeżeli tam rachunku nie ma, podaj go: suma sześciu kolumn
i pięciu gutterów musi równać się szerokości pola treści co do jednostki. Siatka slajdu **nadal
nie jest zatwierdzona** - oznacz ją jako propozycję.

**Roll-up: pole martwe 25 cm u dołu jest konwencją rynkową, nie pomiarem.** Zostaw je i zapisz
jako założenie.

**Tura C - dokumenty regulowane i domknięcie zestawu.**

| Plik | Nośnik | Rozdz. | Wariantów |
|---|---|---|---|
| `templates/zaswiadczenie-a4/` | Zaświadczenie o ukończeniu | 19 | 1, **bez barwy dziedziny** |
| `templates/karta-uslugi-bur/` | Karta usługi BUR, tabele i formularze | 20 | 3, tint dziedziny |
| `irn-design-ksiega-koloru.md` | **brakująca para `.md`** do księgi koloru | - | 1 |

**Księga koloru łamie własną regułę zestawu.** Brandbook, rozdz. „Numeracja", mówi: `pliki systemu:
irn-design-<temat>.<html|md>`, **para obowiązkowa**. Trzy dokumenty mają parę, księga koloru nie ma.
Napisz brakujący `.md` na tej samej zasadzie co pozostałe: rozdziały, liczby z odsyłaczem, wykaz
do potwierdzenia z falsyfikatorem przy każdej pozycji.

**Zaświadczenie:** pieczęć tłoczona bez farby nie wchodzi do limitu 5 %; pieczęć farbą złotą wchodzi
i wtedy ramka 0,4 mm wypada. Jedno albo drugie - pokaż które i dlaczego.

**Karta usługi BUR:** wszystkie pola personalne i numery jako placeholdery w nawiasach kwadratowych.
**Formatu numeru identyfikacyjnego usługi nie odtwarzaj** - nie definiuje go żadne źródło PARP.

### Reguły twarde - Regalia

**Paleta, wartości wiążące:**

| Rola | Barwa | HEX |
|---|---|---|
| tło strony | Kość Słoniowa | `#F7F3E9` |
| typografia | Atrament | `#07090C` |
| kolor marki | Szafir Nocny | `#132246` |
| tło ciemne, stopka | Aksamit Nocy | `#080F1F` |
| tła kart, tekst drugi na ciemnym | Alabaster | `#E4E1D8` |
| tekst drugi na jasnym, linie | Grafit Jedwabny | `#606369` |
| akcent do 5 % | Złoto Szampańskie | `#C4B790` |
| dziedzina Szkolenia zawodowe | Rubin Głęboki | `#541319` |
| dziedzina Pożyczki UE / BGK | Zieleń Butelkowa | `#0B3627` |
| dziedzina Akademia AI | Bursztyn Wyciszony | `#9B5E30` |
| materiał przekrojowy | Ametyst Dworski | `#331F41` |
| odnośnik, obrys focus | Lapis Stonowany | `#305686` |
| metadane | Złoto Antyczne | `#75674B` |
| cytat, podświetlenie | Muszla Różana | `#E8D6D6` |

Tinty 12 %: Szafir `#DCDAD5`, Rubin `#E3D8D0`, Zieleń `#DBDCD2`, Ametyst `#DFDAD5`.
Atrament na każdym z nich przechodzi 14,2:1 i wyżej.

**Pary bazowe:** Atrament na Kości Słoniowej **17,99:1**; odwrócenie Kość Słoniowa na Aksamicie Nocy
**17,25:1**. Tekst drugorzędny: na jasnym Grafit Jedwabny 5,44:1, na ciemnym Alabaster 14,62:1.

**Pięć par zabronionych, z liczbą:**

1. Złoto Szampańskie na Kości Słoniowej **1,80:1** - złoto nigdy jako tło i nigdy jako tekst
   na jasnym. Wchodzi linia, tłoczenie albo wypełnienie z etykietą Atramentem (9,99:1).
2. Grafit Jedwabny na Aksamicie Nocy **3,17:1** - na ciemnym wchodzi Alabaster.
3. Bursztyn Wyciszony na Aksamicie Nocy **3,68:1** - wchodzi wypełnienie z etykietą Kością Słoniową.
4. Złoto Antyczne na Aksamicie Nocy **3,46:1** (nie 3,94) - wchodzi Złoto Szampańskie, 9,58:1.
5. Bursztyn Wyciszony na Alabastrze **3,98:1** - przechodzi próg 3:1 i **jest zakazany decyzją**.
   Bursztyn ma tylko jedno dopuszczone tło: Kość Słoniową, 4,69:1.

**Hierarchia 80 / 15 / 5.** 80 % baza: Kość Słoniowa plus Atrament, w niej Grafit na linie, Alabaster
na tła kart, tinty na karty dziedzinowe. 15 % sygnał: Szafir Nocny plus **dokładnie jeden** kolor
dziedziny na dokument. 5 % akcent: Złoto Szampańskie, limit **21,34 cm²** na polu treści A4
(5 % z 426,7 cm²). Podaj policzony procent złota przy każdym nośniku.

**Maksymalnie dwa tła na dokument:** Kość Słoniowa plus jedno ciemne.

**Dziedziny nie wolno kodować samym kolorem.** Cztery barwy nośne leżą w rozpiętości 2,03 punktu
kontrastu, a Rubin i Zieleń wypadają w mono identycznie - **70 % K obie**. Znak dziedziny Szkolenia
i znak dziedziny Pożyczki są w druku jednokolorowym nieodróżnialne. Wchodzi tint tła, słowo albo oba.

**Kolor nigdy nie jest jedynym nośnikiem statusu** - obok barwy stoi słowo albo ikona.

**Znak: osiem wersji, ani jedna więcej.** Atrament (podstawowa), Kość Słoniowa (odwrócona), Szafir
Nocny (markowa), Ametyst Dworski (przekrojowa), Rubin / Zieleń / Bursztyn (dziedziny), Złoto
Szampańskie (warunkowa, wyłącznie na ciemnym, w limicie 5 %). Czerń czysta i biel czysta **nie
należą do systemu**. Barwę ustawiasz przez `color` kontenera i `fill: currentColor`, **nigdy przez
`filter:`**.

**Dobór wersji w trzech krokach:** jasność podłoża → dziedzina → funkcja materiału. Wątpliwość
rozstrzyga Atrament na Kości Słoniowej.

**Minimum znaku:** 18 mm w druku i 90 px na ekranie dla poziomu i pionu, 10 mm i 44 px dla sygnetu
samodzielnego. Pamiętaj o korekcie kontenera z sekcji o proporcjach.

**Siatka A4:** 210 × 297 mm, sześć kolumn, moduł 25 mm, gutter 4 mm, marginesy 18 / 20 / 28 / 20 mm,
pole treści 170 × 251 mm. Szerokość n kolumn = 29n − 4, czyli **25, 54, 83, 112, 141, 170 mm**.
Krawędzie kolumn: lewe 20, 49, 78, 107, 136, 165 mm; prawe 45, 74, 103, 132, 161, 190 mm.
**Sprawdź każdy blok tym rachunkiem przed oddaniem** - w pierwszej turze pilota stopka miała 178 mm
w pojemniku 170 mm i `overflow:hidden` obcinał 8 mm razem z danymi rejestrowymi.

**Rytm pionowy:** odstęp między blokami to wielokrotność 6 mm (6, 12, 18, 24, 48). Wnętrze
komponentu dobierasz do stopnia pisma. Margines górny 18 mm to strefa znaku i nagłówka, dolny
28 mm strefa stopki; treść nie wchodzi w żadną, a tekst stopki nie schodzi bliżej niż 12 mm
od krawędzi.

**Linie:** struktura Grafitem Jedwabnym od **0,25 mm**, ozdoba Złotem Szampańskim od **0,5 mm**,
siatka wykresu **0,15 mm**. Na ciemnym linia idzie Alabastrem albo Złotem Szampańskim, nigdy
Grafitem.

**Typografia:** Manrope 200-800 na wszystko, Inconsolata 300-700 wyłącznie na liczby, kody
i metadane. Granica: „czy ktoś to przepisze znak po znaku". Trzeciego kroju nie ma. Skala
w pikselach: display 72 · H1 40 · H2 24 · H3 16 · lead 16 · korpus 13,5 · przypis 10 · kicker 14 ·
liczba prowadząca 52 · Inconsolata 10,5. H3 i lead mają ten sam stopień i różni je tylko waga
(600 wobec 500), więc nie stoją obok siebie - rozdziela je kicker.

**Stopień pisma w druku jest pozycją otwartą.** Korpus 13,5 px to 10,1 pt, przypis 10 px to 7,5 pt,
a zakładane minimum dla dokumentu regulowanego bywa 12 pt. Nie podnoś skali sam - to przeliczenie
wszystkich dokumentów A4 i zmiana liczby stron. Jeżeli w nośniku regulowanym stopień okaże się
za mały, **zapisz to jako uwagę z liczbą**, nie zmieniaj.

**Wykresy:** dokument jednej dziedziny to **jedna barwa w czterech stopniach krycia 100 / 72 / 50 /
30 %** - serie różni jasność, nie odcień, więc działają w mono. Dokument przekrojowy może użyć barw
dziedzin, bo wtedy barwa kategorii nie koduje, tylko ją powtarza; warunek: każda oś podpisana
słowem. Maksymalnie cztery serie, oś Y od zera, bez 3D, cienia i gradientu.

**Zakaz twardy:** na materiale IRIN nie stawia się znaku Funduszy Europejskich, znaku barw
Rzeczypospolitej Polskiej ani flagi Unii Europejskiej - **także gdy usługa faktycznie jest
dofinansowana**. IRIN jest doradcą zewnętrznym i dostawcą usługi, nie beneficjentem. Nazwę programu
wolno napisać w treści. Nie odwzorowuj żadnego z tych znaków, także przekreślonego.

**Placeholdery:** wszystkie dane osobowe, numery, ceny i daty w nawiasach kwadratowych, realnej
długości. Zero zmyślonych wartości. Dane kontaktowe IRIN (e-mail, telefon, adres strony) **nie mają
potwierdzonej wartości w repozytorium** - placeholder, nie wymyślona wartość.

**Język:** cała treść po polsku, w tym etykiety, nagłówki i mikrocopy.

### Forma wyniku

Każdy nośnik jako `templates/<slug>/<Slug>.dc.html` z komentarzem
`<!-- @template name="…" description="…" -->` w pierwszej linii. Przy każdym w odpowiedzi jedno
zdanie, co w środku jest do podmiany.

Jeżeli którakolwiek reguła okazała się niewykonalna, **napisz to jako uwagę w kodzie i idź dalej -
nie obchodź jej po cichu**.

Do zwrotu razem z nośnikami:

1. Policzony procent zadruku Złotem Szampańskim przy każdym nośniku, wobec limitu 21,34 cm² na A4.
2. Zmierzona szerokość sygnetu na rewersie wizytówki.
3. Odpowiedź, co w sygnecie przestaje się czytać poniżej 44 px, i czy favicon wymaga uproszczonego
   rysunku znaku.
4. Rachunek szerokości siatki slajdu 16 : 9, domykający się co do jednostki.
5. Lista stopni pisma poniżej 7,5 pt, jeżeli były potrzebne, po jednej wartości na zastosowanie
   z uzasadnieniem w jednym zdaniu.
6. Lista elementów, które powtórzyły się na tyle, że powinny wejść do `components/prymitywy/`.

Zaczynaj bez pytań - wszystko powyżej jest ustalone.

## ——— KONIEC TEKSTU DO WKLEJENIA ———
