# Podpis mailowy IRIN

Plik: [`podpis-mailowy.html`](./podpis-mailowy.html). Paleta **Regalia**. Wersja 2026-09-08.

## Po co i na jakiej podstawie

`02-szablony-dokumentow/papier-firmowy.md` cytuje art. 206 Kodeksu spółek handlowych: pisma
i zamówienia handlowe składane przez spółkę **w formie papierowej i elektronicznej** muszą zawierać
firmę spółki z siedzibą i adresem, oznaczenie sądu rejestrowego z numerem KRS, NIP oraz wysokość
kapitału zakładowego. **Formuła „i elektronicznej" obejmuje wiadomość e-mail**, a e-mail jest dziś
głównym kanałem pism wychodzących IRIN - stąd ten plik. Cztery pozycje z bloku rejestrowego są
obowiązkowe i nie wolno ich skrócić ani usunąć.

REGON nie należy do tej czwórki i celowo go tu nie ma.

## Jak użyć

1. Wyeksportuj PNG znaku (szczegóły niżej) i umieść go pod stałym adresem.
2. Podmień `[ADRES-PNG-ZNAKU]` na ten adres.
3. Podmień pozostałe sześć placeholderów: imię i nazwisko, stanowisko, telefon, dwa razy adres
   e-mail (w `href` i w treści).
4. Wklej sam blok `<table>` do ustawień podpisu w kliencie pocztowym.

**Nie dodawaj `<style>`, klas CSS ani `display:flex`.** Gmail usuwa bloki `<style>`, Outlook
renderuje przez silnik Worda i nie zna nowoczesnego układu. Cały plik stoi na tabelach i stylach
w atrybutach - sprawdzone: zero `<style>`, zero `class=`, zero `flex`, zero `<svg>`.

## PNG znaku - jedna rzecz, którą łatwo zrobić źle

Brandbook, rozdz. 15, przewiduje w podpisie **wariant pionowy o szerokości 90 px**.

**PNG musi być wyeksportowany obcięty do obwiedni artworku, nie do `viewBox` pliku SVG.**
Obwiednia wariantu pionowego to 103,728 × 87,312 jednostki, czyli proporcja 1,188 : 1 - przy
szerokości 90 px daje **76 px wysokości**. Eksport z pełnego `viewBox` (184,837 × 162,834) dałby
znak o szerokości **51 px w kontenerze 90 px**, czyli poniżej minimum ekranowego 90 px, bo artwork
zajmuje tylko 56,1 procent szerokości ramki. Wywód: `01-baza-wiedzy/identyfikacja/logotyp.md`,
sekcja o proporcjach.

SVG w podpisie nie wchodzi - klienci pocztowi go nie renderują.

## Barwy - przeliczone na bieli, nie przepisane z palety

Klient pocztowy renderuje na bieli `#FFFFFF`, a paleta podaje kontrasty na Kości Słoniowej
`#F7F3E9`. Reguła z `paleta-barw.md` mówi, że na tłach spoza palety liczy się od nowa. Przeliczone
2026-09-08 wzorem WCAG 2.1:

| Barwa | HEX | Na bieli | Na Kości Słoniowej | Rola w podpisie |
|---|---|---|---|---|
| Atrament | `#07090C` | **19,94:1** | 17,99:1 | imię, telefon, adres |
| Grafit Jedwabny | `#606369` | **6,02:1** | 5,44:1 | stanowisko, blok rejestrowy, linia |
| Lapis Stonowany | `#305686` | **7,50:1** | 6,77:1 | odnośniki |
| Złoto Szampańskie | `#C4B790` | **2,00:1** | 1,80:1 | **nie użyte** |

**Biel jest jaśniejsza od Kości Słoniowej, więc wszystkie kontrasty rosną i żaden wyrok się nie
zmienia** - to było do sprawdzenia, nie do założenia.

**Dlaczego linia rozdzielająca idzie Grafitem, a nie Złotem Szampańskim.** W papierze złota kreska
jest akcentem ozdobnym i dlatego wolno jej stać poniżej progu 3:1 - ozdoba nie niesie informacji.
W podpisie ta sama linia **oddziela blok osoby od bloku kontaktu**, czyli niesie strukturę, więc
podlega progowi 3:1 dla grafiki znaczącej. Złoto na bieli daje 2,00:1 i by zniknęło; Grafit daje
6,02:1.

## Ryzyko, którego ten plik nie usuwa

**Tryb ciemny klienta pocztowego.** Część klientów wymusza ciemne tło. Przeliczone na typowym
ciemnym szarym `#1B1B1B`:

| Barwa | Kontrast na ciemnym szarym | Wynik |
|---|---|---|
| Atrament `#07090C` | 1,16:1 | znika |
| Grafit Jedwabny `#606369` | 2,86:1 | znika |
| Lapis Stonowany `#305686` | 2,30:1 | znika |
| Złoto Szampańskie `#C4B790` | 8,63:1 | jedyna, która przechodzi |

Paradoks jest zmierzony, nie retoryczny: **jedyna barwa czytelna po wymuszeniu ciemnego tła to ta,
której nie wolno użyć jako tekstu na jasnym.** Regalia jest paletą ciemnych barw na jasnym papierze
i w wymuszonym trybie ciemnym nie ma czym pisać.

**Co zrobiłem:** wrapper ma jawny `bgcolor="#FFFFFF"` i `background-color` w atrybucie `style`.
Klienty, które respektują zadeklarowane tło, zostawią podpis jasnym. **Czego to nie gwarantuje:**
klienty odwracające tło niezależnie od deklaracji (część wersji Outlooka i wymuszony tryb ciemny
Gmaila na Androidzie) nadal mogą pokazać ciemne tło z ciemnym tekstem.

**Falsyfikator: wysłać ten podpis do siebie i obejrzeć w trybie ciemnym w Gmailu na Androidzie
i w Outlooku na Windows.** Dopóki tego nie zrobisz, „podpis działa w trybie ciemnym" jest
twierdzeniem niesprawdzonym. Jeżeli okaże się nieczytelny, rozwiązania są dwa i oba są decyzją,
nie pomiarem: albo podpis idzie w jednej barwie bez bloku rejestrowego w kolorze, albo blok
rejestrowy dostaje jawne ciemne tło z Kością Słoniową jako tekstem (17,25:1) i wygląda inaczej
niż papier firmowy.

## Gdzie ten plik powinien mieszkać - luka w architekturze

`CLAUDE.md` definiuje trzy warstwy: baza wiedzy, karty specyfikacji, pakiet dla Claude Design.
**Żadna z nich nie jest miejscem na gotowy materiał wyjściowy** - warstwa 2 wprost zabrania
trzymania układu graficznego, a warstwa 3 to briefy, nie wyniki. Ten plik leży więc w `_robocze/`,
które `CLAUDE.md` opisuje jako poligon, z którego nic nie jest źródłem prawdy.

To jest niewygodne dla pliku, który ma iść do codziennego użytku. **Rekomendacja: czwarta warstwa
`04-materialy/` na wytworzone artefakty, których nie da się złożyć w Claude Design** - podpis
mailowy, szablon `.docx`, arkusz `.xlsx`. Trzy warstwy pokrywają wiedzę, specyfikacje i zlecenia;
wyników nie pokrywa żadna. Decyzja właściciela, nie moja - do tego czasu plik zostaje tutaj.
