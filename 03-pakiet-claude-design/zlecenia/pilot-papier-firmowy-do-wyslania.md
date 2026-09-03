# Pilot: papier firmowy i wizytówka — tekst gotowy do wklejenia w Claude Design

Ten plik istnieje z jednego powodu: **Claude Design nie widzi dysku właściciela**. Pracuje wyłącznie
na plikach wgranych do kanwy, więc każda ścieżka lokalna jest tam martwym adresem, który może zostać
wzięty za zadanie do wykonania albo za referencję do zweryfikowania. Wersja projektowa zlecenia
(`pilot-papier-firmowy.md`) ścieżki zawiera i ma je zawierać — czyta ją Claude Code, nie Claude Design.

**Źródło prawdy zostaje w `pilot-papier-firmowy.md`.** Ten plik jest jego przekładem na jeden ciągły
tekst. Gdy tamten się zmieni, ten trzeba przełożyć od nowa; nie rozstrzyga się tu niczego samodzielnie.

## Jak tego użyć

1. Wgraj na kanwę **12 plików** z listy niżej.
2. Skopiuj całość między znacznikami POCZĄTEK i KONIEC i wklej jako pierwszą wiadomość.
3. Wynik mierz formularzem `../../_robocze/pilot-papier-firmowy/protokol-pomiaru.md`.

## Paczka — 12 plików do wgrania na kanwę

| # | Plik | Rola |
|---|---|---|
| 1 | `format-paczki.md` | osiem zasad użycia specyfikacji |
| 2 | `papier-firmowy.md` | karta specyfikacji dokumentu: co obowiązkowe, co konwencja, co wybór |
| 3 | `paleta-barw.md` | 14 kolorów, kontrasty na trzech tłach, przepisane kolory etykiet |
| 4 | `siatka-a4.md` | siatka strony A4 |
| 5 | `typografia.md` | kroje i skala |
| 6 | `logotyp.md` | rozmiary, przestrzeń ochronna, zakazy modyfikacji |
| 7 | `palette-irin.json` | te same wartości maszynowo |
| 8 | `kontekst-firmy-sanitized.md` | dane rejestrowe dostawcy |
| 9 | `kontekst-firmy.md` | pełny kontekst firmy |
| 10 | `logo_irin_poziom.svg` | znak, wariant poziomy |
| 11 | `logo_irin_pion.svg` | znak, wariant pionowy |
| 12 | `logo_irin_sygnet.svg` | sygnet samodzielny |

`brandbook.dc.html` **nie wchodzi** do paczki: to kanwa inspiracyjna z wartościami, które zostały
później poprawione (moduł siatki, paleta). Dołączona obok specyfikacji dałaby dwa sprzeczne źródła.

---

## ——— POCZĄTEK TEKSTU DO WKLEJENIA ———

Projektujesz dokument dla **IRIN (Instytut Rozwoju i Nauki)** — polskiej firmy działającej
w obszarach: aplikacje dla przedstawicieli handlowych (narzędzie wewnętrzne), pozyskiwanie pożyczek
UE/BGK dla MŚP (doradztwo, nie instytucja finansowa), oraz dofinansowane szkolenia zawodowe
(KFS, BUR). Pełny kontekst firmy masz w załączonym `kontekst-firmy.md`.

### Co musisz zachować bez zmian

**Logotyp.** Użyj wyłącznie załączonych plików źródłowych: `logo_irin_poziom.svg` (podstawowy),
`logo_irin_pion.svg` (pola wąskie i wysokie), `logo_irin_sygnet.svg` (znak samodzielny) — wszystkie
jednokolorowe. Minimalny rozmiar 18 mm w druku, 90 px na ekranie. Przestrzeń ochronna:
x = wysokość liter sygnetu, mierzona od krawędzi znaku we wszystkich kierunkach; to miara względna,
skalująca się ze znakiem. Znaku się nie modyfikuje: bez zmiany koloru, bez obracania, pochylania
i odbijania, bez cienia, poświaty i obrysu, bez nieproporcjonalnego rozciągania — na ciemnym tle
stosuj wersję odwróconą, nie przebarwioną. Pełna specyfikacja: załączony `logotyp.md`.

**Typografia.** Krój **Manrope** (wagi 200–800) jako podstawowy; **Inconsolata** pomocniczo,
do danych liczbowych, metadanych i kodów usług.

**Siatka, paleta i typografia.** Wszystkie trzy specyfikacje są zatwierdzone i masz je w załącznikach:
`paleta-barw.md` (14 kolorów, tokeny semantyczne, przepisane kolory etykiet, reguła 80/15/5),
`siatka-a4.md` (6 kolumn, moduł 25 mm, gutter 4 mm) i `typografia.md` (Manrope 200–800 plus
Inconsolata, dziesięciopoziomowa skala). Dane maszynowe wszystkich trzech: `palette-irin.json`.
Trzymaj się dokładnie tych wartości, nie przybliżaj ich „na oko”. Osiem zasad ich użycia —
w `format-paczki.md`; trzy najważniejsze: kolor nigdy nie jest jedynym nośnikiem statusu,
hierarchię typograficzną buduje waga jednego kroju, a na tle Pergaminu obowiązują inne kolory linii
i ostrzeżeń niż na Kaszmirze, bo trzy pary spadają tam pod próg kontrastu.

### Co rozstrzyga treść dokumentu

Zanim zaprojektujesz układ, przeczytaj:

1. **Kartę specyfikacji dokumentu** — załączony `papier-firmowy.md`. Mówi, co w treści jest prawnie
   obowiązkowe (musi się znaleźć, nie wolno pominąć ani zniekształcić), co jest konwencją
   organizacyjną IRIN (przyjęty zwyczaj, zmienny za zgodą właściciela), a co **swobodnym wyborem
   projektowym** — to ostatnie jest Twoim polem manewru jako projektanta.
2. **Powiązane pliki z bazy wiedzy**, wskazane przez tę kartę — fakty o firmie, obowiązujące
   przepisy (KFS, BUR, pożyczki UE/BGK), wytyczne usługowe. Elementy prawnie obowiązkowe wynikają
   stąd — nie modyfikuj ich treści, tylko formę.

**Jeśli karta specyfikacji albo plik bazy wiedzy ma status „do potwierdzenia” albo „brak danych”** —
nie domyślaj się treści za właściciela. Zaprojektuj miejsce na tę treść (placeholder) i zapytaj,
zamiast wypełniać czymś zmyślonym.

### Język

Cała treść tekstowa dokumentu jest po polsku — to dotyczy też etykiet, nagłówków i mikrocopy
w layoutcie, nie tylko akapitów.

### Zlecenie

**Typ dokumentu:** dwa elementy jednego zlecenia.

1. **Papier firmowy** IRIN, A4 pion, wersja do druku i wersja do wysyłki jako PDF. Jedna strona
   pierwsza (z pełnym blokiem danych rejestrowych) i jedna strona kolejna (z blokiem skróconym),
   bo pismo dłuższe niż strona nie powtarza całej stopki.
2. **Wizytówka** 85 × 55 mm, awers i rewers, jeden wzór z polami na dane osoby.

**Karta specyfikacji:** załączony `papier-firmowy.md`. Sekcja „Elementy prawnie obowiązkowe”
to treść, której nie wolno pominąć ani skrócić na stronie pierwszej papieru; sekcja „Konwencja
organizacyjna IRIN” obowiązuje jako przyjęty zwyczaj; sekcja „Swobodny wybór projektowy” to Twoje
pole manewru.

**Dane rejestrowe do umieszczenia** (z załączonego `kontekst-firmy-sanitized.md`, potwierdzone
przez właściciela):

- firma: Instytut Rozwoju i Nauki sp. z o.o.
- siedziba i adres: ul. Karola Olszewskiego 6, 25-663 Kielce
- KRS 0001032499, NIP 9592061542, REGON 525113640
- sąd rejestrowy: Sąd Rejonowy w Kielcach, X Wydział Gospodarczy Krajowego Rejestru Sądowego
- kapitał zakładowy: 40 000,00 zł

**Dane kontaktowe do umieszczenia** (konwencja IRIN): e-mail **biuro@irin.pl**,
telefon **+48 453 049 912**, strona **www.irin.pl**. Format zapisu telefonu nie jest regułą —
karta specyfikacji go nie narzuca.

**Pola wizytówki:** imię i nazwisko, stanowisko, telefon bezpośredni, e-mail. Na wzorze użyj
placeholderów w nawiasach kwadratowych, nie zmyślonych osób.

**Kolor wiodący:** Aksamit w roli `primary`, zgodnie z tabelą w `paleta-barw.md`. Papier firmowy
jest dokumentem całej firmy, nie jednej dziedziny; nie sygnalizuj żadnej z trzech dziedzin. Jeżeli
w trakcie pracy uznasz, że dokument bez koloru dziedzinowego wypada niejednoznacznie wobec reguły
80/15/5, zapisz to jako uwagę do właściciela, nie wybieraj dziedziny samodzielnie.

**Znak:** na papierze wariant poziomy `logo_irin_poziom.svg`; na wizytówce wariant do Twojego wyboru
między poziomym a pionowym na awersie, a na rewersie sygnet `logo_irin_sygnet.svg` samodzielnie.
Zmierz i zapisz, w jakiej szerokości sygnet stoi na rewersie — to potrzebne do protokołu pomiaru.

**Linie mają przepisany kolor i minimalną grubość.** Linię niosącą strukturę - linia tabeli, obrys
karty, obrys pola, rozdzielenie bloków - prowadzisz Popiołem `#7D7466`, nie cieniej niż **0,25 mm**.
Złoto foliowe `#A8874E` jest wyłącznie kreską ozdobną, pieczęcią i sygnaturą, nie cieniej niż
**0,5 mm**, i nigdy na tle Pergaminu. Podaj przy każdej użytej linii jej grubość w milimetrach
i tło, na którym stoi - to wchodzi do protokołu pomiaru.

**Siatkę wolno Ci dopracować - ale jako propozycję obok, nie po cichu w dokumencie.** Wartości
z `siatka-a4.md` są zatwierdzone i artboard główny trzyma je bez zmian: A4 pion, sześć kolumn,
moduł 25 mm, gutter 4 mm, marginesy 18 mm góra, 20 mm lewy, 20 mm prawy, 28 mm dół. Marginesy boczne zostały wyrównane 2026-09-03
(dawniej 18 lewy / 22 prawy, bez uzasadnienia); pionowe są niesymetryczne celowo, bo cięższy dół
to reguła składu. Jeżeli przy realnej treści zobaczysz, że któraś wartość jest do poprawy,
zrób trzy rzeczy:

1. Zostaw artboard główny na wartościach zatwierdzonych.
2. Dodaj **drugi artboard oznaczony jako propozycja**, z Twoją wersją siatki i tą samą treścią,
   żeby dało się je porównać obok siebie.
3. Napisz, co konkretnie zmieniasz i dlaczego, **z rachunkiem szerokości**: suma kolumn i gutterów
   musi się równać szerokości pola treści co do milimetra. Obecnie 6 × 25 + 5 × 4 = 170 mm i pole
   treści też ma 170 mm, dopasowanie jest dokładne, bez zapasu - każda zmiana modułu albo gutteru
   pociąga zmianę marginesu i odwrotnie.

Dwie rzeczy są poza dyskusją: **format A4 pion** i **sześć kolumn**. Liczba kolumn jest w tym
systemie elementem tożsamości wspólnym dla trzech dziedzin, nie parametrem dobieranym per dokument
- mówi o tym zasada 6 z `format-paczki.md`. Reszta parametrów jest otwarta na Twoją propozycję.

**Treść przykładowa pisma na stronie pierwszej** (tekst zastępczy do pokazania układu,
nie korespondencja):

> **[Kicker]** OFERTA SZKOLENIOWA · WRZESIEŃ 2026
>
> **[Lead, Manrope 500]** Dziękujemy za zainteresowanie szkoleniami Instytutu Rozwoju i Nauki.
> Poniżej przedstawiamy zakres usług, które mogą zostać objęte wnioskiem o środki Krajowego
> Funduszu Szkoleniowego.
>
> **[H3, Manrope 600, bezpośrednio pod leadem, celowo]** Źródła finansowania, o które występuje
> pracodawca
>
> **[Korpus, Manrope 400]** Dofinansowanie zależy od decyzji powiatowego urzędu pracy i od
> priorytetów ustalonych na dany rok; nasza rola kończy się na przygotowaniu programu kształcenia
> i wzoru zaświadczenia. Żółć, gęś, źdźbło, ćma, łódź, ńandu, świt, żółw: ĄĆĘŁŃÓŚŹŻ ąćęłńóśźż.
>
> **[Dane techniczne, Inconsolata]** Nr pisma: IRIN/2026/09/0001 · Kod usługi BUR: [KOD]

Zdanie z żółcią i gęsią jest w tekście celowo: zawiera wszystkie polskie znaki diakrytyczne w obu
wielkościach. Zachowaj je w każdej wadze użytej w piśmie.

H3 stoi bezpośrednio pod leadem **celowo**, wbrew zasadzie 5 z `format-paczki.md`. To jest
sprawdzian tej zasady, nie przeoczenie: chcemy zobaczyć, czy różnica wagi 500 wobec 600 przy tym
samym stopniu jest widoczna bez kickera. Nie wstawiaj kickera między lead a H3.

**Format wyniku:** podgląd na żywej kanwie z przełącznikiem siatki sześciu kolumn (25 mm,
gutter 4 mm) nad obiema stronami A4, oraz PDF w skali 1:1 dla obu elementów.

**Kolejność ma znaczenie: najpierw kanwa, potem PDF.** Eksport do PDF nie osadza krojów
z Google Fonts — w wyeksportowanym pliku tekst pokazuje krój zastępczy (`Segoe UI`/`Arial` zamiast
Manrope, `Courier New` zamiast Inconsolaty). Pomiarów dotyczących liter i wag nie da się więc
wykonać na PDF-ie; PDF służy do sprawdzenia proporcji, marginesów i skali 1:1.

## ——— KONIEC TEKSTU DO WKLEJENIA ———
