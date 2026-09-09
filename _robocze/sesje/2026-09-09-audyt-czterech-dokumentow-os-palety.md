# Audyt czterech dokumentów wzorcowych, oś palety

Wykonany 2026-09-09 na czterech plikach przekazanych przez właściciela jako najaktualniejszy
stan wytycznych: `irn-design-paleta-kolorow`, `irn-design-ksiega-koloru`,
`irn-design-ksiega-znaku`, `irn-design-brandbook`.

**Metoda: maszynowa, nie czytanie prozy.** Z każdego pliku wyciągnięto wszystkie wartości hex
i wszystkie liczby w formacie kontrastu, potem porównano z pełną macierzą 19 barw Regalii
(14 nośnych i funkcjonalnych, 4 tinty, biel) policzoną od nowa wzorem WCAG 2.1. Kryterium:
liczba **odtwarza się**, jeżeli istnieje para barw Regalii dająca dokładnie tę wartość
po zaokrągleniu do dwóch miejsc.

Dlaczego tak, a nie przez czytanie: cztery agenty audytowe uruchomione do tego zadania zostały
skasowane przy przerwaniu tury i ich praca przepadła. Metoda maszynowa jest zresztą mocniejsza -
sprawdza liczby, nie zdania o liczbach.

## Ustalenie 1: wszystkie cztery dokumenty stoją na Regalii

| Dokument | Rozmiar | Hexy Regalii | Hexy wycofanej linii | Hexy spoza obu list |
|---|---|---|---|---|
| paleta-kolorow | 43 kB | **18/18** | 2 | 3 |
| ksiega-koloru | 80 kB | **18/18** | 0 | 1 |
| ksiega-znaku | 82 kB | **18/18** | 7 | 2 |
| brandbook | 167 kB | **18/18** | 4 | 2 |

Hexy wycofanej linii wystąpiły **wyłącznie jako cytat historyczny**, sprawdzone w kontekście:

- `paleta-kolorow`: `#7E7053` i `#A7693C` w tabeli „Co zmieniono wobec wariantu Regalia",
  w kolumnie „Było".
- `ksiega-znaku`: siedem hexów w jednym zdaniu opisującym dawną rozbieżność - „księga podawała
  Aksamit `#452430`, Miedź `#7A5638`, Onyks `#33474F`, gdy `tokens.css` nosił `#752F3F`,
  żadnej Miedzi i `#005A80`".
- `brandbook`: cztery hexy pojedynczo, w tym samym charakterze.

Hexy spoza obu list to barwy interfejsu podglądu (`#D5D0C6` tło kanwy, `#3F444B` i `#6B6357`
opisy artboardów, `#16264D`), nie wartości palety.

**Wniosek: żaden z czterech dokumentów nie stoi na wycofanej linii.** To istotne dla otwartej
sprawy dwóch równoległych palet: `guidelines/paleta-barw.md` w projekcie Claude Design
(Kaszmir Wyciszony v5.1.0) jest wobec tych czterech dokumentów pojedynczym plikiem odstającym,
a nie drugą żywą linią. Rozstrzygnięcie zostaje przy właścicielu, ale ciężar dowodu przesunął się.

## Ustalenie 2: jedna liczba w trzech dokumentach nie odtwarza się

Ze wszystkich liczb kontrastu w czterech plikach **odtworzyły się wszystkie poza jedną**:
`3,94`. Występuje w `paleta-kolorow`, `ksiega-koloru` i `brandbook`, i nie odpowiada żadnej
parze barw Regalii.

Rachunek, który zamyka sprawę:

| Para | Kontrast |
|---|---|
| Złoto Antyczne **wycofane** `#7E7053` na Aksamicie Nocy `#080F1F` | **3,9417** |
| Złoto Antyczne **obowiązujące** `#75674B` na Aksamicie Nocy `#080F1F` | **3,4577** |

`3,94` odtwarza się do czwartego miejsca po przecinku na hexie sprzed pociemnienia. Liczba nie
jest błędem rachunku, tylko liczbą policzoną dla innej barwy i nieprzeliczoną po jej zmianie.

**Trzy niezależne potwierdzenia zbiegają się na 3,46:** rachunek w `paleta-barw.md` z 2026-09-04,
rachunek w tej sesji, oraz - niezależnie od repozytorium - sama **Księga koloru**, która pisze:
„Rozbieżność do rozstrzygnięcia. `irn-design-paleta-kolorow` podaje dla tej pary 3,94 : 1.
Przeliczenie `#75674B` na `#080F1F` w tej księdze daje 3,46 : 1. Zakaz obowiązuje w obu
wariantach; różnica dotyczy zapisu, nie decyzji."

**Cztery dokumenty nie są więc jednomyślne:** Księga koloru ma 3,46 i nazywa źródło błędu,
`paleta-kolorow` i `brandbook` niosą 3,94. Do poprawienia są dwa dokumenty, nie warstwa 1.

## Ustalenie 3: to, co wyglądało na rozbieżność, nią nie jest

`paleta-kolorow` podaje `10,12`, a `ksiega-koloru` i `ksiega-znaku` `10,13`. **To dwie różne
pary**, nie dwa zapisy jednej:

| Wartość | Para |
|---|---|
| 10,12 | Rubin Głęboki `#541319` / Muszla Różana `#E8D6D6` |
| 10,13 | Rubin Głęboki `#541319` / tint Szafir `#DCDAD5` |

## Ustalenie 4: dwie wartości, których warstwa 1 nie ma

Obie policzone i potwierdzone w tej sesji, obie do dopisania.

| Wartość | Para | Skąd | Rachunek |
|---|---|---|---|
| **7,82:1** | Szafir Nocny `#132246` / Złoto Szampańskie `#C4B790` | ksiega-znaku | odtwarza się |
| **3,00:1** | Bursztyn Wyciszony `#9B5E30` na Szafirze Nocnym `#132246` | ksiega-koloru | **3,002** |

Druga jest ważniejsza: to **czwarta komórka zabroniona**, której tabela par zabronionych
w `paleta-barw.md` nie zawiera.

## Ustalenie 5: konflikt zasady, nie liczby

Księga koloru stawia regułę: **„Zakaz jest silniejszy od progu. Cztery komórki mieszczą się
w progu 3 : 1 dla dużego stopnia pisma, a mimo to są zakazane: Grafit (3,17), Złoto Antyczne
(3,46) i Bursztyn (3,68) na Aksamicie oraz Bursztyn na Szafirze (3,00)."**

`paleta-barw.md` dostała 2026-09-08 zastrzeżenie idące w drugą stronę: że próg 4,5:1 dotyczy
tekstu normalnego, a dla dużego obowiązuje 3:1, więc „zakaz dotyczy metadanych i przypisów,
nie nagłówków".

**Obie strony sporu, uczciwie:** moje zastrzeżenie dotyczyło **jasnych** podłoży (Kość Słoniowa,
Alabaster, tinty), a cztery komórki księgi leżą na **ciemnych** (Aksamit Nocy, Szafir Nocny).
Formalnie nie jest to ta sama teza. Spór dotyczy jednak zasady: czy przejście progu 3:1
dla dużego stopnia **licencjonuje** użycie, czy zakaz stoi ponad progiem. Jeżeli obowiązuje
reguła księgi, to moje zastrzeżenie na jasnych podłożach też jest za słabe i trzeba je przepisać.

**To pozycja dla właściciela.** Rozstrzyga ją Księga koloru jako dokument późniejszy
i bardziej szczegółowy, ale zmiana zasady dotyka każdego materiału, więc nie wpisuję jej
z własnej decyzji.

## Czego ten audyt NIE objął

Wyłącznie oś **palety i kontrastu**. Nietknięte zostają trzy osie, które miały własnych agentów:

1. **Siatka A4** - brandbook wobec `siatka-a4.md`: kolumny, moduł, gutter, marginesy, strefy.
2. **Typografia** - brandbook wobec `typografia.md`: kroje, wagi, stopnie, interlinie, tracking,
   a zwłaszcza w jakich jednostkach brandbook podaje stopnie i czy zgadza się to z przelicznikiem
   1 px = 0,75 pt.
3. **Logotyp** - ksiega-znaku wobec `logotyp.md`: osiem wersji kolorystycznych, minima, x,
   proporcje obwiedni, zakazy modyfikacji.

Nie objął też nazw obszarów działalności ani weryfikacji, które pliki w projekcie czytają który
blok `tokens.css`.

## Falsyfikator metody

Liczba kontrastu podana w dokumencie dla pary, której nie da się zidentyfikować z nazw obok
niej - wtedy „odtwarza się" znaczy tylko, że taka para w Regalii istnieje, a nie że dokument
przypisał ją poprawnie. Kontrola: przy każdej z pięciu liczb spornych sprawdzono kontekst
tekstowy, nie samą wartość.
