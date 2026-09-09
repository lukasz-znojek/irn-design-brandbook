# Paleta barw IRIN - specyfikacja obowiązująca

**Status: ZATWIERDZONA przez foundera 2026-09-03; wpisana do warstwy 1 repozytorium 2026-09-09.** Nazwa systemu: **Regalia** (regalia-1.0.0), czternaście barw, prefiks tokenów `--irin-r-`.

Dane maszynowe: [`tokeny/palette-irin.json`](./tokeny/palette-irin.json). Siatka A4: [`siatka-a4.md`](./siatka-a4.md). Typografia: [`typografia.md`](./typografia.md). Logotyp: [`logotyp.md`](./logotyp.md). Ten plik opisuje wyłącznie kolor.

**Ten plik jest wywiedziony, nie źródłowy.** Wartości pochodzą z [`tokeny/palette-irin.json`](./tokeny/palette-irin.json) i to nie jest miejsce, w którym się je zmienia: zmiana idzie przez [`../../_robocze/narzedzia/zloz-palete.py`](../../_robocze/narzedzia/zloz-palete.py), a potem przez bramki `sprawdz-palete.py` i `sprawdz-zgodnosc-md.py`. Liczba wpisana tutaj ręcznie i nieobecna w danych maszynowych zamyka bramkę, i o to chodzi.

Metodologia kontrastu: WCAG 2.1, luminancja względna sRGB. Progi: tekst normalny AA 4,5:1, AAA 7:1; element interfejsu i grafika znacząca 3:1. Każda liczba w tym pliku jest policzona przy składaniu, nie przepisana.

## Czternaście barw

Każda barwa ma nazwę własną (tak się o niej mówi) i token (tak się jej używa w kodzie). Kontrasty na trzech tłach nośnych: Kość Słoniowa, Aksamit Nocy, Alabaster. **Pogrubienie oznacza wartość poniżej 3:1**, czyli para nie nadaje się nawet na grafikę znaczącą - w tabelach niżej każda taka para jest wypisana z rozstrzygnięciem.

| Barwa | Token | Hex | Rola | na Kości Słoniowej | na Aksamicie Nocy | na Alabastrze |
|---|---|---|---|---|---|---|
| Szafir Nocny | `--irin-r-szafir-nocny` | `#132246` | kolor marki: logotyp, pasy nagłówkowe, wypełnienia CTA | 14,09:1 | **1,22:1** | 11,94:1 |
| Atrament | `--irin-r-atrament` | `#07090C` | typografia główna: korpus, nagłówki, tabele | 17,99:1 | **1,04:1** | 15,25:1 |
| Kość Słoniowa | `--irin-r-kosc-sloniowa` | `#F7F3E9` | tło strony; wersja odwrócona znaku | nie dotyczy (to tło) | 17,25:1 | **1,18:1** |
| Aksamit Nocy | `--irin-r-aksamit-nocy` | `#080F1F` | tło ciemne: sekcje, stopki, okładki wewnętrzne | 17,25:1 | nie dotyczy (to tło) | 14,62:1 |
| Alabaster | `--irin-r-alabaster` | `#E4E1D8` | tła kart, wiersze naprzemienne, tekst drugi na ciemnym | **1,18:1** | 14,62:1 | nie dotyczy (to tło) |
| Grafit Jedwabny | `--irin-r-grafit-jedwabny` | `#606369` | tekst drugi na jasnym, linie struktury od 0,25 mm | 5,44:1 | 3,17:1 | 4,61:1 |
| Złoto Szampańskie | `--irin-r-zloto-szampanskie` | `#C4B790` | akcent do 5 %: kreska ozdobna od 0,5 mm, pieczęć, tłoczenie | **1,80:1** | 9,58:1 | **1,53:1** |
| Ametyst Dworski | `--irin-r-ametyst-dworski` | `#331F41` | materiał przekrojowy: kategorie i tagi wspólne | 13,41:1 | **1,29:1** | 11,37:1 |
| Muszla Różana | `--irin-r-muszla-rozana` | `#E8D6D6` | jasny akcent: cytaty, podświetlenia, ramki wyróżnień | **1,26:1** | 13,67:1 | **1,07:1** |
| Lapis Stonowany | `--irin-r-lapis-stonowany` | `#305686` | interakcja: odnośniki, stan aktywny, obrys focus | 6,77:1 | **2,55:1** | 5,73:1 |
| Złoto Antyczne | `--irin-r-zloto-antyczne` | `#75674B` | akcent informacyjny: podpowiedzi, metadane, ikony | 4,99:1 | 3,46:1 | 4,23:1 |
| Rubin Głęboki | `--irin-r-rubin-gleboki` | `#541319` | barwa dostępna, nieprzypisana do obszaru | 12,77:1 | **1,35:1** | 10,82:1 |
| Zieleń Butelkowa | `--irin-r-zielen-butelkowa` | `#0B3627` | barwa dostępna, nieprzypisana do obszaru | 12,06:1 | **1,43:1** | 10,22:1 |
| Bursztyn Wyciszony | `--irin-r-bursztyn-wyciszony` | `#9B5E30` | barwa dostępna, nieprzypisana do obszaru | 4,69:1 | 3,68:1 | 3,98:1 |

## Dwa układy, nie czternaście barw na stronie

Materiał IRIN stoi na jednym z dwóch układów, a nie na całej palecie naraz:

- **układ jasny** - Atrament na Kości Słoniowej, 17,99:1 (AAA);
- **odwrócenie** - Kość Słoniowa na Aksamicie Nocy, 17,25:1 (AAA).

**Maksymalnie dwa tła na dokument.** Trzecie tło nie dodaje informacji, tylko rozmywa hierarchię i mnoży pary do sprawdzenia. Alabaster jest tłem karty i pasa tabeli wewnątrz układu jasnego, nie trzecim układem.

## Gniazdo obszaru

**Barwy nie są przypisane do obszarów działalności, bo obszary są wymienne.** Materiał obszarowy nadpisuje u siebie te dwa tokeny i nic więcej. Materiał bez obszaru wychodzi poprawnie bez żadnej podmiany.

- Token barwy: `--irin-r-dziedzina`, domyślnie wskazuje Szafir Nocny (`#132246`).
- Token tintu: `--irin-r-tint-dziedzina`, domyślnie tint szafir (`#DCDAD5`).

Cztery barwy dostępne do wstawienia w gniazdo:

| Barwa | Token | Hex | Kość Słoniowa na tej barwie | Ocena |
|---|---|---|---|---|
| Rubin Głęboki | `--irin-r-rubin-gleboki` | `#541319` | 12,77:1 | AAA |
| Zieleń Butelkowa | `--irin-r-zielen-butelkowa` | `#0B3627` | 12,06:1 | AAA |
| Bursztyn Wyciszony | `--irin-r-bursztyn-wyciszony` | `#9B5E30` | 4,69:1 | AA |
| Ametyst Dworski | `--irin-r-ametyst-dworski` | `#331F41` | 13,41:1 | AAA |

Najmniejszy zapas z czterech ma Bursztyn Wyciszony: 4,69:1 przy progu 4,5:1 dla tekstu, czyli zapas 0,19. Przy tej barwie obszaru nie schodzi się ze stopniem pisma poniżej korpusu i nie stawia się na niej tekstu drugiego.

**Pułapka:** Rubin Głęboki bywa też barwą oznaczenia - nie podmieniaj go globalnie.

**Decyzja właściciela.** 2026-09-09: barwy dostępne są DOBIERANE DO MATERIAŁU, nie przypisane do obszarów działalności. Rozstrzyga to sprzeczność między dwiema decyzjami po stronie projektowej i zamyka falsyfikator, który do tej pory stał otwarty.

## Regalia nie ma tokenów stanu

W tej palecie **nie ma** `success`, `warning` ani `error`. To decyzja, nie przeoczenie.

**Powód.** Trzy barwy, które mogłyby je pełnić, są jednocześnie kandydatami na barwy obszarów; przypisanie ich do roli statusu zabetonowałoby to, co ma być wymienne.

**Skutek.** Stan niesie słowo plus jedna z barw nośnych dobrana w dokumencie. Kolor nigdy nie jest jedynym nośnikiem statusu (WCAG 1.4.1). Plakietka „zatwierdzone" bez słowa „zatwierdzone" jest błędem dostępności, nie oszczędnością miejsca.

## Tinty 12 procent

Cztery tinty powstają z mieszania barwy z Kością Słoniową przy kryciu 12 %. Nie są osobnymi barwami palety i nie wolno ich wpisywać ręcznie: odtwarzają się z mieszania co do bajtu i bramka to sprawdza.

| Tint | Token | Hex | Podstawa | Atrament na tincie |
|---|---|---|---|---|
| Szafir 12 % | `--irin-r-tint-szafir` | `#DCDAD5` | Szafir Nocny `#132246` | 14,27:1 |
| Rubin 12 % | `--irin-r-tint-rubin` | `#E3D8D0` | Rubin Głęboki `#541319` | 14,24:1 |
| Zieleń 12 % | `--irin-r-tint-zielen` | `#DBDCD2` | Zieleń Butelkowa `#0B3627` | 14,41:1 |
| Ametyst 12 % | `--irin-r-tint-ametyst` | `#DFDAD5` | Ametyst Dworski `#331F41` | 14,36:1 |

**Rola, poza którą tint nie wychodzi:** wyłącznie tła kart i pasy tabel w obrębie obszaru; nie kolor tekstu ani linii.

## Pary dopuszczone

Progi: tekst normalny AA 4,5:1, AAA 7:1; element interfejsu i grafika znacząca 3:1.

| Tekst albo znak | Tło | Kontrast | Rodzaj | Ocena | Zastosowanie |
|---|---|---|---|---|---|
| Atrament | Kość Słoniowa | 17,99:1 | tekst | AAA | korpus, nagłówki, tabele |
| Kość Słoniowa | Aksamit Nocy | 17,25:1 | tekst | AAA | sekcje ciemne, stopka |
| Atrament | Alabaster | 15,25:1 | tekst | AAA | karty, wiersze tabel |
| Alabaster | Aksamit Nocy | 14,62:1 | tekst | AAA | tekst drugi na ciemnym |
| Atrament | Muszla Różana | 14,26:1 | tekst | AAA | cytaty, wyróżnienia |
| Kość Słoniowa | Szafir Nocny | 14,09:1 | tekst | AAA | pas nagłówkowy, CTA |
| Kość Słoniowa | Ametyst Dworski | 13,41:1 | tekst | AAA | tagi, kategorie |
| Kość Słoniowa | Rubin Głęboki | 12,77:1 | tekst | AAA | wypełnienia sekcji |
| Kość Słoniowa | Zieleń Butelkowa | 12,06:1 | tekst | AAA | wypełnienia sekcji |
| Kość Słoniowa | Bursztyn Wyciszony | 4,69:1 | tekst | AA | etykieta na wypełnieniu obszaru; najciaśniejsza z czterech barw gniazda |
| Muszla Różana | Rubin Głęboki | 10,12:1 | tekst | AAA | etykieta na wypełnieniu |
| Atrament | Złoto Szampańskie | 9,99:1 | tekst | AAA | etykieta na wypełnieniu złotym |
| Złoto Szampańskie | Aksamit Nocy | 9,58:1 | tekst | AAA | kicker na tle ciemnym |
| Lapis Stonowany | Kość Słoniowa | 6,77:1 | tekst | AA | odnośniki i stan aktywny |
| Lapis Stonowany | Alabaster | 5,73:1 | tekst | AA | odnośnik na karcie |
| Grafit Jedwabny | Kość Słoniowa | 5,44:1 | tekst | AA | tekst drugi na jasnym |
| Złoto Antyczne | Kość Słoniowa | 4,99:1 | tekst | AA | podpowiedzi, metadane |
| Bursztyn Wyciszony | Kość Słoniowa | 4,69:1 | tekst | AA | jedyne dopuszczone tło Bursztynu |
| Grafit Jedwabny | Kość Słoniowa | 5,44:1 | grafika | OK | linia struktury od 0,25 mm |
| Atrament | tint Szafir 12 % | 14,27:1 | tekst | AAA | karta i pas tabeli na tincie Szafir 12 % |
| Atrament | tint Rubin 12 % | 14,24:1 | tekst | AAA | karta i pas tabeli na tincie Rubin 12 % |
| Atrament | tint Zieleń 12 % | 14,41:1 | tekst | AAA | karta i pas tabeli na tincie Zieleń 12 % |
| Atrament | tint Ametyst 12 % | 14,36:1 | tekst | AAA | karta i pas tabeli na tincie Ametyst 12 % |

## Pary zabronione

Każdy wiersz ma zamiennik. Zakaz bez zamiennika jest przeszkodą, nie regułą.

| Tekst albo znak | Tło | Kontrast | Próg | Zamiast tego |
|---|---|---|---|---|
| Złoto Szampańskie | Kość Słoniowa | **1,80:1** | 4,5:1 | złoto wyłącznie jako kreska, tłoczenie albo wypełnienie z etykietą Atramentem |
| Lapis Stonowany | Aksamit Nocy | **2,55:1** | 4,5:1 | odnośnik na tle ciemnym idzie Złotem Szampańskim (kontrast wyżej) albo Kością Słoniową z podkreśleniem |
| Bursztyn Wyciszony | Alabaster | **3,98:1** | 4,5:1 | Bursztyn ma jedno dopuszczone tło: Kość Słoniowa |
| Bursztyn Wyciszony | Aksamit Nocy | **3,68:1** | 4,5:1 | ostrzeżenie na ciemnym: wypełnienie bursztynowe z etykietą Kością Słoniową |
| Złoto Antyczne | Aksamit Nocy | **3,46:1** | 4,5:1 | na ciemnym wchodzi Złoto Szampańskie |
| Grafit Jedwabny | Aksamit Nocy | **3,17:1** | 4,5:1 | tekst drugi na ciemnym: Alabaster |

Wiersz Lapisu Stonowanego na Aksamicie Nocy (2,55:1) wchodzi tu z pomiaru: reguła istniała, ale mieszkała w prozie jednego szablonu po stronie projektowej i nie było jej w żadnej specyfikacji, choć para jest gorsza od trzech już wpisanych. Zapis w specyfikacji jest kontekstem; blokadą jest bramka, która nie przepuści pary pod progiem bez wiersza w jednej z dwóch tabel.

## Pary, które nie wchodzą do składu

Pary pod progiem 3, które nie wchodzą do składu, bo są barwą ciemną na ciemnym tle albo jasną na jasnym. Wypisane jawnie, żeby bramka mogła sprawdzić, że żadna para pod progiem nie została przeoczona.

| Barwa | Tło | Kontrast |
|---|---|---|
| Szafir Nocny | Aksamit Nocy | **1,22:1** |
| Atrament | Aksamit Nocy | **1,04:1** |
| Ametyst Dworski | Aksamit Nocy | **1,29:1** |
| Rubin Głęboki | Aksamit Nocy | **1,35:1** |
| Zieleń Butelkowa | Aksamit Nocy | **1,43:1** |
| Kość Słoniowa | Alabaster | **1,18:1** |
| Alabaster | Kość Słoniowa | **1,18:1** |
| Złoto Szampańskie | Alabaster | **1,53:1** |
| Muszla Różana | Kość Słoniowa | **1,26:1** |
| Muszla Różana | Alabaster | **1,07:1** |

Ta lista nie jest ostrzeżeniem dla projektanta, bo nikt takiej pary nie złoży. Istnieje dla bramki: dopóki **każda** para pod progiem stoi albo tutaj, albo w tabeli par zabronionych z zamiennikiem, przeoczenie takie jak wiersz Lapisu nie przejdzie niezauważone.

## Reguła proporcji 80/15/5

- **80 % baza:** Kość Słoniowa, Atrament, Alabaster, Grafit Jedwabny.
- **15 % obszar:** dokładnie jedna barwa z gniazda na dokument, nigdy dwie naraz.
- **5 % akcent:** Złoto Szampańskie.

Limit akcentu policzony z pola treści A4: 170 x 251 mm = 426,70 cm2; 5 % = 21,34 cm2. Tyle **łącznie** złota na stronie, licząc pieczęć, kreski ozdobne i tłoczenie.

Poza budżetem akcentu, bo niosą funkcję, nie ozdobę: Lapis Stonowany, Złoto Antyczne, Muszla Różana.

**Złoto Szampańskie nigdy jako tekst na jasnym** (1,80:1 na Kości Słoniowej), nigdy jako tło większej powierzchni, nigdy jako linia niosąca strukturę. Wyłącznie kreska ozdobna od 0,5 mm, pieczęć i tłoczenie.

## Minimalna grubość linii

- linia niosąca strukturę: **0,25 mm**;
- kreska ozdobna: **0,5 mm**.

Poniżej tych wartości o widoczności decyduje raster drukarki, nie luminancja. NIEPOTWIERDZONE NA WYDRUKU - falsyfikator otwarty.

Na ekranie 0,25 mm renderuje się jako 1 px (0,94 px przy 96 dpi, przeglądarka zaokrągla obramowanie w górę). Wartość drukarska jest poprawna; ekran nie jest miejscem pomiaru grubości linii.

## Falsyfikatory otwarte

Twierdzenia, których **nie da się sprawdzić w kodzie** i które do potwierdzenia na materiale pozostają niesprawdzone, nie ustalone:

- grubość linii struktury 0,25 mm i kreski ozdobnej 0,5 mm na wydruku;
- minimalny rozmiar samodzielnego sygnetu 10 mm;
- czytelność diakrytyków na papierze przy stopniu podłogi 8,5 px;
- CMYK palety bez proofu na papierze docelowym;
- Złoto Szampańskie na papierze niepowlekanym.

Zamknięte 2026-09-09 decyzją właściciela: przypisanie barw dostępnych do obszarów działalności (barwy są dobierane do materiału).
