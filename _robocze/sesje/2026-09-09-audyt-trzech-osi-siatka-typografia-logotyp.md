# Audyt trzech pozostałych osi: siatka, typografia, logotyp

Domknięcie audytu z 2026-09-09. Notatka `2026-09-09-audyt-czterech-dokumentow-os-palety.md`
objęła wyłącznie oś palety i kontrastu i wprost wymieniła trzy osie nietknięte. Tu są te trzy.

Źródło: te same cztery pliki przekazane przez właściciela jako najaktualniejszy stan wytycznych
(`irn-design-brandbook` 175 kB, `irn-design-ksiega-znaku` 86 kB, `irn-design-ksiega-koloru` 83 kB,
`irn-design-paleta-kolorow` 45 kB). Wzorzec: `01-baza-wiedzy/identyfikacja/siatka-a4.md`,
`typografia.md`, `logotyp.md`.

**Metoda: maszynowa.** Z HTML zdjęto znaczniki, potem wyciągnięto wszystkie wartości `mm`, `px`,
`pt` i wszystkie zapisy stopnia pisma wzorcem `(Manrope|Inconsolata) … <liczba> px`, i porównano
z wartościami warstwy 1. Każdą liczbę kontrastu policzono od nowa wzorem WCAG 2.1, żadnej nie
przepisano. Skrypty stały w katalogu roboczym sesji, nie w repozytorium - wynik jest odtwarzalny
z opisu, bo każdy rachunek jest w tej notatce wypisany.

**Trzy ustalenia twarde, każde obalone rachunkiem, nie opinią.** Poniżej najpierw one, potem to,
co się zgadza.

## Oś siatki: jedna liczba nie zgadza się z żadnym rachunkiem

Rozdział 10 brandbooka podaje: „Dryf na pełnej kolumnie 45 linii = **19 mm**". Ta sama liczba
stoi drugi raz w spisie treści.

Rachunek, który ją obala - w całości z liczb, które **brandbook sam podaje trzy wiersze wyżej**:

| Krok | Wartość w brandbooku | Sprawdzenie |
|---|---|---|
| interlinia korpusu | 13,5 px × 1,55 = 20,93 px = 5,54 mm | 13,5 × 1,55 = 20,925 px = 5,5364 mm |
| różnica na linię | 1,75 px = 0,46 mm | 22,68 - 20,925 = 1,755 px = 0,4636 mm |
| linii w polu treści | 45 | 251 / 5,5364 = 45,34 |
| **dryf** | **19 mm** | 45 × 0,4636 = **20,86 mm** |

Liczba 19 nie wychodzi też z zaokrąglonych składników brandbooka: 45 × 0,46 = 20,70 mm.
Nie ma drogi, którą z 45 linii i różnicy 0,46 mm otrzyma się 19.

Skąd się wzięła, wie warstwa 1: `siatka-a4.md` wiersz 72 zapisuje, że 19 mm to dryf
na **41 jednostkach siatki**, nie na 45 liniach tekstu - czyli pomiar nie tej wielkości.
Warstwa 1 poprawiła to u siebie, brandbook niesie wartość sprzed poprawki.

**Rozstrzyga warstwa 1**, i nie na zasadzie starszeństwa dokumentu, tylko dlatego, że rachunek
brandbooka przeczy własnemu wynikowi. Do poprawienia jest brandbook, w dwóch miejscach.

## Oś typografii: skala zamknięta o jeden poziom za wcześnie, i dwa stopnie pod podłogą

### Dziesięć wobec jedenastu

Rozdział 07 brandbooka nosi tytuł „Skala **dziesięciu** poziomów" i zdanie: „Skala jest zamknięta:
stopnia spoza tej dziesiątki nie ma".

`typografia.md` wiersz 3: „Skala ma **11** poziomów, od Display 72 px do podłogi składu 8,5 px".
Jedenasty poziom to **Techniczny, Inconsolata 8,5 px = 6,38 pt**, opisany w wierszu 38 jako
„podłoga składu: nagłówki tabel, przypisy, pas nadawcy".

Brandbook nie ma tego poziomu ani słowa „podłoga" - sprawdzone wyszukiwaniem, zero trafień
na `podłog` w całym pliku.

### Skutek: brandbook łamie własne zdanie w 10 wystąpieniach na 36

Zliczenie wszystkich zapisów stopnia w brandbooku, z klasyfikacją wobec skali **właściwego kroju**
(Manrope: 72, 52, 40, 24, 16, 14, 13,5, 10; Inconsolata: 10,5 i 8,5):

| Krój i stopień | Gdzie | Ocena |
|---|---|---|
| Manrope 7,5 px | nagłówek tabeli | **pod podłogą 8,5 px** |
| Inconsolata 8 px | pas nadawcy na kopercie | **pod podłogą 8,5 px** |
| Inconsolata 9 px | kontakt na wizytówce | poza skalą |
| Manrope 9,5 px | rola na wizytówce | poza skalą |
| Manrope 13 px | imię na wizytówce | poza skalą |
| Inconsolata 10 px | identyfikator dokumentu na okładce | poza skalą Inconsolaty (jest 10,5) |
| Inconsolata 16 px | numer slajdu | poza skalą Inconsolaty |
| Manrope 18 px | kicker slajdu | poza skalą |
| Manrope 44 px | tytuł slajdu | poza skalą |
| Manrope 140 px | liczba prowadząca slajdu | poza skalą |

**10 z 36 wystąpień, czyli 27,8 procent.** Udział przekracza 5 procent, więc zgodnie z regułą
o klasyfikacji zbioru nie wyciągam z niego wniosku o „drobnych odstępstwach" - to jest rozjazd
systemowy, nie szum.

Dwa pierwsze wiersze są innej wagi niż osiem pozostałych. 7,5 px to **5,62 pt**, a 8 px to
**6,00 pt**, wobec podłogi 6,38 pt. `typografia.md` wiersz 52 stawia to jako regułę, nie jako
ostatni wiersz tabeli: „Nic mniejszego nie wchodzi do składu". Zbieżność jest przy tym
uderzająca: warstwa 1 wymienia jako zastosowania podłogi dokładnie **nagłówki tabel i pas
nadawcy** - czyli te dwa miejsca, w których brandbook schodzi niżej.

Osiem pozostałych wystąpień to wybór reguły, nie błąd rachunku: albo skala nie jest zamknięta
i trzeba to napisać, albo rozdziały nośnikowe mają się do niej dociągnąć. **Rekomendacja:
dociągnąć nośniki do skali, a slajd wyłączyć jawnie.** Uzasadnienie do obalenia: cztery z ośmiu
wystąpień (18, 44, 140 px i Inconsolata 16 px) to slajd 16:9, którego siatka jest w warstwie 1
jawnie oznaczona jako **propozycja, nie specyfikacja** (`siatka-a4.md` wiersz 81) - a skoro pole
jest inne, to stopnie z A4 nie muszą na nie przechodzić. Zostają wtedy cztery wystąpienia
na wizytówce i kopercie, czyli nośnikach małych, i tam różnica 13 wobec 13,5 px albo 9 wobec
10,5 px nie kupuje nic, czego nie da się kupić skróceniem tekstu. Obali tę rekomendację wydruk
wizytówki w skali 1:1, na którym kontakt w Inconsolacie 10,5 px nie mieści się w jednym wierszu.

### Co się na tej osi zgadza

Wszystkie dziesięć poziomów, które brandbook ma, zgadzają się z `typografia.md` co do kroju,
wagi, stopnia, interlinii i trackingu - sprawdzone wiersz po wierszu. Zapis `10,1 pt` wobec
`10,13 pt` w warstwie 1 **nie jest rozjazdem**: `typografia.md` wiersz 50 sam ustala, że strona
projektowa zapisuje jednomiejscowo, a repozytorium dwumiejscowo. Pozycja otwarta „stopień pisma
w druku" (korpus 10,1 pt wobec zakładanego minimum 12 pt) jest w brandbooku odnotowana jako
otwarta, z falsyfikatorem - czyli obsłużona poprawnie.

## Oś logotypu: zakaz rozciągania podaje proporcje, które rozciągają znak

To jest najcięższe ustalenie tego audytu.

Księga znaku ma rozdział 01 w pełni zgodny z `logotyp.md`: viewBoksy, obwiednie
i **proporcje znaku 4,741 : 1, 1,188 : 1, 2,669 : 1**. Trzy akapity dalej, w tabeli doboru
wariantu, ta sama księga podaje inne liczby:

| Wariant | Proporcja w tabeli doboru | Proporcja obwiedni | Iloraz |
|---|---|---|---|
| Poziom | **1,773 : 1** | 4,7412 : 1 | 2,674 |
| Pion | **1,135 : 1** | 1,1880 : 1 | 1,047 |
| Sygnet | **1,135 : 1** | 2,6698 : 1 | 2,352 |

Skąd te dwie liczby, rachunek jednoznaczny:

- 281,333 / 158,667 = **1,7731** - to viewBox pliku `logo_irin_poziom.svg`;
- 184,837 / 162,834 = **1,1351** - to viewBox plików `logo_irin_pion.svg` i `logo_irin_sygnet.svg`.

Czyli tabela doboru podaje **proporcje pustej ramki jako proporcje znaku** - dokładnie ten błąd,
który `CLAUDE.md` i `logotyp.md` nazywają i korygują od 2026-09-04.

Dowód niezależny od rachunku: **pion i sygnet dostają w tabeli tę samą liczbę 1,135**, a to są
dwa różne znaki - jeden kwadratowy, drugi wyraźnie leżący. Jedna liczba na dwa różne kształty
może opisywać tylko to, co mają wspólne, czyli ramkę pliku.

**Dlaczego to jest cięższe od pomyłki w tabeli.** Ta sama para liczb stoi w antywzorcu 06,
czyli w zakazie rozciągania nieproporcjonalnego: „Skalowanie wyłącznie z proporcjami:
1,773 : 1 dla poziomu, 1,135 : 1 dla pionu i sygnetu". Kto wykona ten zakaz co do litery,
wstawi znak poziomy w pole 1,773 : 1 i **zniekształci go 2,674 razy** - bo znak widoczny ma
4,741 : 1. Zakaz przed deformacją jest zapisany liczbami, które deformację nakazują.

**Rozstrzyga `logotyp.md`**, bo jego liczby pochodzą z pomiaru `getBBox` w Chromium
(`_robocze/narzedzia/zmierz-znak.mjs`), a liczby z tabeli doboru odtwarzają się jako iloraz
wymiarów viewBoksu, czyli pola, nie znaku. Do poprawienia jest księga znaku, w dwóch miejscach:
tabela doboru i antywzorzec 06.

### Co się na tej osi zgadza, i to dokładnie

Sześć liczb kontrastu z księgi znaku policzonych od nowa wzorem WCAG 2.1:

| Para | Księga | Przeliczenie |
|---|---|---|
| Atrament `#07090C` na Kości Słoniowej `#F7F3E9` | 17,99 | 17,9907 |
| Kość Słoniowa `#F7F3E9` na Aksamicie Nocy `#080F1F` | 17,25 | 17,2533 |
| Kość Słoniowa `#F7F3E9` na Szafirze Nocnym `#132246` | 14,09 | 14,0911 |
| Złoto Szampańskie `#C4B790` na Aksamicie Nocy `#080F1F` | 9,58 | 9,5802 |
| Złoto Szampańskie `#C4B790` na Szafirze Nocnym `#132246` | 7,82 | 7,8243 |
| Złoto Szampańskie `#C4B790` na Kości Słoniowej `#F7F3E9` | 1,80 | 1,8009 |

**Sześć na sześć, co do setnej.** Współczynniki pola 0,655 i 0,561 też zgadzają się
z `logotyp.md`. Minima 18 mm / 90 px / sygnet 10 mm zgadzają się razem ze statusem: księga
opisuje minimum sygnetu jako „odczyt z kanwy foundera, **nie potwierdzony osobno**", tak samo
jak warstwa 1.

Osobno warto odnotować, że księga sama pilnuje granicy ilustracji: przy matrycy teł pisze,
że znak w polu matrycy ma 13,4 mm, czyli poniżej minimum 18 mm, i że pola są ilustracją
zestawienia, nie przykładem użycia. To jest wzorcowe postawienie sprawy, nie usterka.

### Dwie wartości, których nie ma w `logotyp.md`

| Wartość | Skąd | Status |
|---|---|---|
| minimum sygnetu na ekranie **44 px** | księga znaku, rozdz. 04 | **niepotwierdzone** - ta sama kanwa co 10 mm |
| uzasadnienie 90 px: „odpowiada 18 mm przy **127 dpi**" | księga znaku, rozdz. 04 | rachunek sprawdzony: 90 / (18 / 25,4) = 127,0 dpi |

`logotyp.md` ma minimum ekranowe tylko dla poziomu i pionu (90 px) i minimum sygnetu tylko
w druku (10 mm). Wiersza „sygnet na ekranie" nie ma w ogóle.

**Nie dopisuję żadnej z nich w tej turze.** `logotyp.md` jest plikiem wywiedzionym z
`tokeny/palette-irin.json` przez generator, więc dopisanie wiersza to zmiana generatora
i przebieg obu bramek, a 44 px jest wartością niepotwierdzoną z tego samego źródła, które
w warstwie 1 nosi już ostrzeżenie. To pozycja do decyzji, nie do cichego wpisania.

## Pozycje dla właściciela, po jednym zdaniu

1. **Skala: dziesięć czy jedenaście poziomów** - czy podłoga składu 8,5 px wchodzi do brandbooka
   jako poziom, czy zostaje regułą samej warstwy 1.
2. **Dwa stopnie pod podłogą** - nagłówek tabeli 7,5 px i pas nadawcy 8 px w brandbooku łamią
   regułę „nic mniejszego nie wchodzi do składu"; podnieść do 8,5 px czy obniżyć podłogę.
3. **Cztery stopnie wizytówki i koperty poza skalą** - dociągnąć do skali (rekomendacja) czy
   uznać nośniki małe za wyłączone.
4. **Slajd 16:9** - jawnie wyłączyć spod skali A4 i spod siatki A4, czy dociągnąć; przy okazji
   gutter 32 px nie domyka się, bo `(1728 - 5 × 32) / 6 = 261,33 px`.
5. **Sygnet na ekranie 44 px** - wpisać do `logotyp.md` ze statusem niepotwierdzonym, czy zostawić
   poza warstwą 1 do wydruku sprawdzającego.

Pozycje 1-4 są w brandbooku, 5 w warstwie 1. Poprawki w dwóch dokumentach z Claude Design
(dryf 19 mm, proporcje 1,773 / 1,135) nie są pozycjami do decyzji, tylko liczbami do poprawienia -
ale plików w projekcie nie nadpisuję bez zgody, bo nadpisania nie da się z sesji cofnąć.

## Falsyfikatory

- **Osi typografii:** zapis w brandbooku, którego wyciąg wzorcem `(Manrope|Inconsolata) … px`
  nie złapał, bo stopień podano inaczej niż liczbą przed „px" - wtedy udział 27,8 procent jest
  zaniżony albo zawyżony i trzeba go policzyć od nowa. Kontrola wykonana: wszystkie 36 wystąpień
  obejrzano w kontekście, żadne nie okazało się fałszywym trafieniem.
- **Osi logotypu:** plik SVG o viewBoksie równym obwiedni znaku - wtedy 1,773 i 4,741 byłyby tą
  samą liczbą i cała teza upada. Kontrola: `logotyp.md` wiersze 13-15 podają obwiednie zmierzone
  `getBBox`, różne od viewBoksów, a współczynniki pola 0,655 i 0,561 są w księdze znaku wpisane
  jawnie, czyli księga sama wie, że pole jest większe od znaku.
- **Osi siatki:** interlinia korpusu inna niż 1,55 albo pole treści inne niż 251 mm - obie liczby
  są w brandbooku i w warstwie 1 identyczne, więc dryf liczy się z tych samych składników po obu
  stronach.
