> **NIEAKTUALNE wobec palety obowiązującej - nie wysyłaj bez przepisania.**
> Ten plik niesie 5 wartości hex spoza palety Regalia, w tym barwy
> palet wycofanych v2 i v5.1. Powstał przed destylacją warstwy 1 z 2026-09-09.
> Obowiązujące wartości: [`../../01-baza-wiedzy/identyfikacja/paleta-barw.md`](../../01-baza-wiedzy/identyfikacja/paleta-barw.md).
> Oznaczone przy scaleniu gałęzi `claude/irin-visual-identity-vq9ddw`.

# Pilot, tura poprawek: tekst gotowy do wklejenia w Claude Design

Ten plik istnieje z tego samego powodu co `pilot-papier-firmowy-do-wyslania.md`: **Claude Design
nie widzi dysku właściciela**, więc każda ścieżka lokalna jest tam martwym adresem, który może
zostać wzięty za zadanie do wykonania.

**Do czego się odnosi.** Pierwsza tura zlecenia została wykonana - w projekcie design-system
`1a22ce64-0e1c-43a6-bd60-eef9241ef73b` leży `templates/papier-firmowy-wizytowka/PapierFirmowyWizytowka.dc.html`
z czterema artboardami. Ten plik jest **drugą turą**: listą rzeczy, które w tej kanwie odbiegają
od zatwierdzonych specyfikacji, z podaniem czym każda została zmierzona.

**Źródło prawdy o wynikach:** `_robocze/pilot-papier-firmowy/protokol-pomiaru.md`. Ten plik jest
przekładem tamtego na tekst bez ścieżek; po każdej zmianie tam trzeba go przełożyć od nowa.

**Czego ta tura nie robi.** Nie rozstrzyga przebarwienia znaku filtrem CSS - właściciel odłożył tę
decyzję do obejrzenia całości pracy. Nie zmienia sygnetu na rewersie: 22 mm to jego polecenie.
Nie zamawia nowych artboardów.

## Jak tego użyć

1. Otwórz w Claude Design projekt `System projektowy IRIN` i w nim kanwę papieru firmowego.
   Załączniki są już w projekcie - **nie wgrywaj ich ponownie**.
2. Skopiuj całość między znacznikami POCZĄTEK i KONIEC i wklej jako wiadomość.
3. Wynik odczytam z plików projektu; pomiary właściciela idą na koniec, po zamknięciu poprawek.

---

## ——— POCZĄTEK TEKSTU DO WKLEJENIA ———

Dziękuję za pierwszą turę papieru firmowego i wizytówki IRIN. Kanwę przeczytałem plik po pliku
i przeliczyłem wartości wobec zatwierdzonych specyfikacji. Poniżej jest **trzy rzeczy do zrobienia
i jedna do zaraportowania** - nic więcej. Cztery Twoje uwagi do właściciela zostały zapisane
i nie wymagają od Ciebie nic dodatkowego.

Specyfikacje, wobec których liczyłem, masz w projekcie: `siatka-a4.md`, `typografia.md`,
`paleta-barw.md`, `logotyp.md`, `zasady-uzycia.md` oraz dane maszynowe `tokens/palette-irin.json`.

### 1. Stopka strony pierwszej jest o 8 mm szersza od pola treści i obcina dane rejestrowe

**To jest defekt, nie wybór.** Rachunek, do odtworzenia w jednej linii:

- stopka ma `grid-template-columns: 54mm 54mm 62mm` i `column-gap: 4mm`
- suma: 54 + 54 + 62 + 2 × 4 = **178 mm**
- pojemnik: `left: 20mm; right: 20mm` na stronie 210 mm = **170 mm**
- nadmiar: **8 mm**, a artboard ma `overflow: hidden`, więc nadmiar jest po cichu obcinany,
  bez żadnego ostrzeżenia

Obcinana jest trzecia kolumna stopki, czyli **NIP, REGON, telefon i adres strony**. Dane rejestrowe
są w karcie specyfikacji papieru firmowego w sekcji „Elementy prawnie obowiązkowe" - art. 206
Kodeksu spółek handlowych - więc to nie jest kwestia estetyki: dokument w tym stanie nie spełnia
wymogu treści.

**Naprawa, która dodatkowo siada na siatkę:** trzy bloki po dwie kolumny.

- 54 + 4 + 54 + 4 + 54 = **170 mm**, czyli dokładnie pole treści
- każdy blok ma 54 mm, czyli 2 × 25 mm modułu plus 4 mm gutteru, więc jego krawędzie leżą
  na krawędziach kolumn 1-2, 3-4 i 5-6

Jeżeli trzeci blok nie mieści treści w 54 mm, przenieś część danych do bloku drugiego albo dodaj
drugi wiersz stopki - byle suma szerokości nie przekroczyła 170 mm. **Nie zmieniaj marginesów
strony**: 20 mm z każdej strony jest wartością zatwierdzoną.

Sprawdź tym samym rachunkiem stopkę strony kolejnej. Tam użyłeś `flex` z `justify-content:
space-between`, więc nadmiaru nie ma - ale potwierdź, że tekst nie wychodzi za 170 mm.

### 2. Trzy bloki nie siadają prawą krawędzią na kolumnie

Krawędzie kolumn na A4 pion przy module 25 mm i gutterze 4 mm:

| Kolumna | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| lewa krawędź, mm | 20 | 49 | 78 | 107 | 136 | 165 |
| prawa krawędź, mm | 45 | 74 | 103 | 132 | 161 | 190 |

Szerokość n kolumn liczy się jako 29n − 4: **25, 54, 83, 112, 141, 170 mm**.

Co zmierzyłem w kanwie:

| Element | Zakres w mm | Prawa krawędź | Najbliższa szerokość z siatki |
|---|---|---|---|
| logo poziome, strona 1 | 20 .. 72 | nie siada, kolumna 2 kończy się na 74 | **54 mm** (2 kolumny) |
| blok adresata | 20 .. 99 | nie siada, kolumna 3 kończy się na 103 | **83 mm** (3 kolumny) |
| lead i korpus, `max-width: 150mm` | 20 .. 170 | nie siada, kolumna 5 kończy się na 161 | **141 mm** (5 kolumn) albo **112 mm** (4 kolumny) |
| pas kickera i H3 | 20 .. 190 | siada obustronnie | bez zmian |
| przełącznik siatki | `repeat(6, 25mm)` + `4mm` = 170 mm | zgodne | bez zmian |

Pierwsze dwa doprowadź do szerokości z ostatniej kolumny - to poprawki po 2 i 4 mm, więc układ
się nie zmieni, a bloki przestaną wisieć między kolumnami.

**Trzeci zostawiam Tobie jako wybór projektowy**, bo to jest długość wiersza, nie tylko siatka.
141 mm przy korpusie 3,57 mm daje wiersz około 39 firetów, czyli dłuższy niż wygodny zakres
60-75 znaków; 112 mm daje około 31 firetów. Wybierz i **napisz, którą wartość wziąłeś i dlaczego** -
to wchodzi do specyfikacji siatki jako pierwsze użycie.

### 3. Znak: nie dodawaj nowego przebarwienia

Znak w plikach źródłowych jest jednokolorowy i nie niesie własnej palety. Na kanwie każdy
`<img>` ze znakiem ma łańcuch `filter:`. Przeliczyłem, w jaki kolor ten łańcuch trafia, emulując
go wg specyfikacji Filter Effects na czarnym znaku wejściowym:

| Miejsce | Kolor, w który filtr celuje wg Twojego opisu | Wynik rachunku |
|---|---|---|
| strona pierwsza, strona kolejna, awers | Aksamit `#452430` | **`#3D1922`** |
| rewers na tle Espresso | Kaszmir `#FBF8F2` | **`#F6F3EB`** |

Żaden z dwóch wyników nie jest kolorem z palety; drugi jest najbliżej Muślinu `#F6F2E9`,
nie Kaszmiru.

**Co z tym robisz w tej turze: nic, oprócz jednej rzeczy.** Czy znak wolno przebarwiać na jasnym
tle, rozstrzyga właściciel po obejrzeniu całości - `logotyp.md` dziś tego nie pozwala i wyjątek
przewiduje tylko dla wersji odwróconej na ciemnym tle. Do jego decyzji **nie wprowadzaj
przebarwienia w żadnym nowym miejscu**. Jeżeli musisz gdzieś zmienić kolor znaku, zapisz to jako
pytanie, a nie jako zrobione.

Jedno możesz poprawić bez decyzji: **jeżeli zostawiasz przebarwienie, ustaw kolor wprost wartością
hex z palety, nie łańcuchem filtrów.** Filtr nie trafia w kolor i nikt nie potrafi z niego odczytać,
jaka barwa była zamierzona.

### 4. Do zaraportowania, nie do naprawy: skala nie ma poziomów dla małego pisma

Zestawiłem 22 stopnie pisma użyte na czterech artboardach z dziesięciopoziomową skalą
z `typografia.md`, przy tolerancji 0,05 mm. **7 zgodnych, 15 poza skalą, czyli 68 procent.**

Przy takim udziale nie twierdzę, że dokument łamie regułę piętnaście razy. Bardziej prawdopodobne
jest to, że **skala nie ma czym pisać stopki ani wizytówki**: jej najmniejszy poziom to Manrope
10 px, czyli 2,65 mm i 7,5 pt, a Inconsolata 10,5 px, czyli 2,78 mm i 7,88 pt. Poniżej nie ma nic.

Poza skalą, wraz z przeliczeniem na punkty:

| Miejsce | Krój | Użyte | W punktach | Najbliższy poziom skali |
|---|---|---|---|---|
| data w nagłówku, wartości danych technicznych | Inconsolata | 2,90 mm | 8,22 pt | 2,78 mm |
| sygnatura | Manrope | 2,80 mm | 7,94 pt | 2,65 mm |
| identyfikacja pisma i numer strony, strona 2 | Inconsolata | 2,60 mm | 7,37 pt | 2,78 mm |
| stopka i stanowisko na wizytówce | Manrope | 2,50 mm | 7,09 pt | 2,65 mm |
| wartości w stopce | Inconsolata | 2,50 mm | 7,09 pt | 2,78 mm |
| etykiety danych technicznych | Inconsolata | 2,40 mm | 6,80 pt | 2,78 mm |
| telefon i e-mail na awersie | Inconsolata | 2,30 mm | 6,52 pt | 2,78 mm |
| etykiety w stopce, `irin.pl` na rewersie | Inconsolata | 2,20 mm | 6,24 pt | 2,78 mm |
| **etykiety Tel. i E-mail na awersie** | Inconsolata | **1,90 mm** | **5,39 pt** | 2,78 mm |
| imię i nazwisko na awersie | Manrope | 3,30 mm | 9,35 pt | 3,57 mm |

Jedna z tych wartości jest problemem niezależnym od skali: **1,90 mm to 5,39 pt**, czyli poniżej
progu, na którym pismo na wizytówce jeszcze się czyta po druku offsetowym, a tym bardziej
biurowym. Ta jedna podnieś, niezależnie od tego, co właściciel zdecyduje o skali.

**Czego od Ciebie potrzebuję:** listy stopni, których faktycznie potrzebujesz w stopce, w blokach
metadanych i na wizytówce - po jednej wartości na zastosowanie, z krótkim „bo". Nie zgaduj, jakie
poziomy dopisać do skali; specyfikacja jest zatwierdzona i jej rozszerzenie to decyzja właściciela.
Twoja lista jest wejściem do tej decyzji.

### Czego nie zmieniamy w tej turze

- **Rewers: `logo_irin_poziom.svg` w szerokości 50 mm mierzonej po obwiedni znaku widocznego (komponent Logotyp przycina `viewBox` do obwiedni, pole ochronne wypada) - powyżej minimum 18 mm w druku, wyśrodkowany w obu osiach na tle Aksamit Nocy (`--irin-r-aksamit-nocy` `#1B1A17`), znak w Kości Słoniowej przez `currentColor`; bloku tekstowego nadawcy na rewersie nie ma. Wycofano polecenia sygnetu (22 mm i 30 mm) - poziomy wariant utrzymuje regułę jednorazowego użycia sygnetu na karcie (awers: sygnet 10 mm w bloku koloru dziedziny 22 mm, karta 85 × 55 mm).**
- **Marginesy strony:** 18 mm góra, 20 mm lewy, 20 mm prawy, 28 mm dół. Zatwierdzone.
- **Sześć kolumn, moduł 25 mm, gutter 4 mm, format A4 pion.** Poza dyskusją.
- **Kolor wiodący Aksamit, bez sygnału dziedziny.** Papier firmowy jest dokumentem całej firmy.
- **Dane rejestrowe i kontaktowe w brzmieniu, w jakim są na kanwie.** Zgodne z rejestrem KRS.
- **Placeholdery w nawiasach kwadratowych na wizytówce i w kodzie usługi.** Mają zostać.
- **Zdanie z pełnym zestawem polskich diakrytyków** w każdej użytej wadze. Ma zostać.
- **Przełącznik siatki i przełącznik marginesów.** Zostają; drugi jest dodatkiem, o który nie
  prosiłem, i jest przydatny.

### Format wyniku

Poprawiona kanwa, ta sama, nie nowa. Po każdej poprawce podaj w jednym zdaniu, co zmieniłeś
i jaką wartość wziąłeś - to wchodzi do protokołu pomiaru. PDF-u w tej turze nie potrzebuję;
pomiary właściciela na wydruku idą po zamknięciu poprawek.

## ——— KONIEC TEKSTU DO WKLEJENIA ———
