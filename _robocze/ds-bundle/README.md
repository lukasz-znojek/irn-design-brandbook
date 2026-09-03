# System projektowy IRIN

Instytut Rozwoju i Nauki — polska firma działająca w trzech obszarach: dofinansowane szkolenia
zawodowe (KFS, BUR), pośrednictwo w pozyskiwaniu pożyczek UE/BGK dla MŚP, oraz wewnętrzna
aplikacja dla przedstawicieli handlowych. Ten system służy dokumentom drukowanym i do wysyłki
w PDF: pismom firmowym, zaświadczeniom, kartom usług, viewbookom.

**Cała treść dokumentów jest po polsku** — to dotyczy etykiet, nagłówków i mikrocopy w layoutcie,
nie tylko akapitów.

## Idiom: zmienne CSS, nie klasy narzędziowe

Ten system nie ma komponentów w kodzie. Ma tokeny i klasy skali typograficznej, wszystkie
osiągalne z `styles.css`:

- **Kolor:** `var(--irin-<nazwa>)` po nazwie własnej (`--irin-aksamit`, `--irin-popiol`)
  albo `var(--irin-<token>)` po roli (`--irin-primary`, `--irin-border`). Obie formy wskazują
  tę samą wartość; w kodzie używaj tokenu, w rozmowie nazwy.
- **Typografia:** klasy `.irin-display`, `.irin-h1`, `.irin-h2`, `.irin-h3`, `.irin-lead`,
  `.irin-korpus`, `.irin-meta`, `.irin-kicker`, `.irin-liczba`, `.irin-dane`.
- **Siatka:** `.irin-siatka` daje sześć kolumn z gutterem 4 mm. Wymiary strony i marginesy
  jako `--irin-margines-gora`, `--irin-margines-bok`, `--irin-margines-dol`.
- **Linie:** `.irin-linia-struktury` (Popiół, 0,25 mm) i `.irin-kreska-ozdobna`
  (Złoto foliowe, 0,5 mm).
- **Odstępy:** `.irin-odstep-1`, `.irin-odstep-2`, `.irin-odstep-4` — 6, 12 i 24 mm.

Nie wymyślaj własnego słownika klas. Czego nie ma w tej liście, składaj własnym CSS-em
na zmiennych `--irin-*`, nigdy na wartościach wpisanych na sztywno.

## Osiem reguł, bez których same wartości są niekompletne

1. **Jeden kolor dziedziny na dokument** — Aksamit (Pedagogika), Miedź (Akademia AI) albo
   Onyks (Pożyczki UE/BGK), nigdy dwa naraz. To warstwa 15 % reguły 80/15/5.
2. **Kolor etykiety na wypełnieniu jest przepisany**, nie dobierany. Tabela w `guidelines/paleta-barw.md`.
3. **Kolor nigdy nie jest jedynym nośnikiem statusu** — każdy stan potrzebuje słowa albo ikony.
4. **Hierarchię buduje waga jednego kroju**, nie zmiana rodziny. Manrope na wszystko,
   Inconsolata wyłącznie na liczby, kody usług i metadane. Trzeciego kroju nie ma.
5. **H3 i lead nie stoją bezpośrednio obok siebie** — różnią się wyłącznie wagą przy tym samym
   stopniu 16 px. Gdy muszą sąsiadować, rozdziela je kicker.
6. **Sześć kolumn zawsze.** Liczba kolumn jest elementem tożsamości wspólnym dla trzech dziedzin,
   nie parametrem dobieranym per dokument.
7. **Linia ma kolor i minimalną grubość.** Struktura: Popiół, od 0,25 mm. Ozdoba: Złoto foliowe,
   od 0,5 mm, nigdy na tle Pergaminu. Rubryką nie pisze się tekstu na Pergaminie.
8. **Na materiale IRIN nie stawia się znaku Funduszy Europejskich, znaku barw RP ani flagi UE.**
   IRIN jest doradcą zewnętrznym, nie beneficjentem — Podręcznik informacji i promocji FE,
   rozdz. 8.7, s. 22. Nazwę programu wolno napisać w treści; oznaczyć nim materiału nie.

## Czego ten system jeszcze nie potwierdził

Trzy wartości mają policzoną podstawę, ale **nie przeszły wydruku**. Są w systemie oznaczone
i nie należy ich traktować jak zamkniętych:

- **Grubość linii 0,25 mm i 0,5 mm** — kontrast policzony, widoczność na papierze nie sprawdzona.
- **Minimalny rozmiar samodzielnego sygnetu 10 mm / 44 px** — odczyt z kanwy foundera,
  nie potwierdzony osobno.
- **Pełne pokrycie polskich diakrytyków na wagach 500 i 600** — potwierdzone w zakresie,
  w jakim je zmierzono, nie glif po glifie.

## Gdzie leży prawda

`guidelines/` zawiera cztery specyfikacje obowiązujące w całości: `paleta-barw.md`,
`siatka-a4.md`, `typografia.md`, `logotyp.md`, oraz `zasady-uzycia.md` z ośmioma regułami wyżej.
Dane maszynowe: `tokens/palette-irin.json`. Przy składaniu czytaj te pliki, nie streszczenie —
każda liczba ma tam wypisany rachunek, którym się ją odtwarza.
