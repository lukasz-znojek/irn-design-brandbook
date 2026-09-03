# Zlecenie pilotażowe: papier firmowy i wizytówka

Pierwszy dokument IRIN przeprowadzony przez pełną ścieżkę z `/CLAUDE.md`: paczka z tego repozytorium, prompt bazowy, kompozycja w Claude Design, wnioski z powrotem do warstwy 1. Decyzja foundera o pilocie i jego wybór: `/MAPA-DROGOWA.md`, sekcja „Dlaczego pilotem jest papier firmowy”.

Ten plik nie powtarza żadnej specyfikacji. Zawiera trzy rzeczy: skład paczki, treść sekcji „Zlecenie” do wklejenia na końcu `../prompt-bazowy.md`, oraz protokół pomiaru, czyli co po powrocie z Claude Design wpisać do warstwy 1.

## 1. Skład paczki

Wszystkie pliki z tego repozytorium, bez modyfikacji, w kolejności czytania przez Claude Design:

| Kolejność | Plik | Rola w paczce |
|---|---|---|
| 1 | `../prompt-bazowy.md` z sekcją „Zlecenie” zastąpioną treścią z punktu 2 niżej | instrukcja główna |
| 2 | `../format-paczki.md` | siedem zasad użycia specyfikacji |
| 3 | `/02-szablony-dokumentow/papier-firmowy.md` | co jest prawnie obowiązkowe, co konwencją, co wyborem |
| 4 | `/01-baza-wiedzy/identyfikacja/paleta-barw.md` | kolory i przepisane kolory etykiet |
| 5 | `/01-baza-wiedzy/identyfikacja/siatka-a4.md` | siatka strony A4 |
| 6 | `/01-baza-wiedzy/identyfikacja/typografia.md` | kroje i skala |
| 7 | `/01-baza-wiedzy/identyfikacja/logotyp.md` | rozmiary, przestrzeń ochronna, zakazy |
| 8 | `/01-baza-wiedzy/identyfikacja/tokeny/palette-irin.json` | te same wartości maszynowo |
| 9 | `/01-baza-wiedzy/firma/kontekst-firmy-sanitized.md` | dane rejestrowe dostawcy |
| 10 | `/logo_irin_poziom.svg`, `/logo_irin_pion.svg`, `/logo_irin_sygnet.svg` | znak, trzy warianty |

`brandbook.dc.html` **nie wchodzi** do paczki. To kanwa inspiracyjna z wartościami, które zostały później poprawione (moduł siatki, paleta); dołączenie jej obok specyfikacji dałoby Claude Design dwa sprzeczne źródła.

## 2. Treść sekcji „Zlecenie”

Skopiuj `../prompt-bazowy.md` w całości i zastąp jego ostatnią sekcję „Zlecenie” poniższym tekstem. Pola w nawiasach kwadratowych uzupełnia founder przed wysłaniem; żadnego nie zgaduj.

---

### Zlecenie

**Typ dokumentu:** dwa elementy jednego zlecenia.

1. **Papier firmowy** IRIN, A4 pion, wersja do druku i wersja do wysyłki jako PDF. Jedna strona pierwsza (z pełnym blokiem danych rejestrowych) i jedna strona kolejna (z blokiem skróconym), bo pismo dłuższe niż strona nie powtarza całej stopki.
2. **Wizytówka** 85 × 55 mm, awers i rewers, jeden wzór z polami na dane osoby.

**Karta specyfikacji:** `/02-szablony-dokumentow/papier-firmowy.md`. Sekcja „Elementy prawnie obowiązkowe” to treść, której nie wolno pominąć ani skrócić na stronie pierwszej papieru; sekcja „Konwencja organizacyjna IRIN” obowiązuje jako przyjęty zwyczaj; sekcja „Swobodny wybór projektowy” to Twoje pole manewru.

**Dane rejestrowe do umieszczenia** (z `/01-baza-wiedzy/firma/kontekst-firmy-sanitized.md`, potwierdzone przez foundera 2026-09-02):

- firma: Instytut Rozwoju i Nauki sp. z o.o.
- siedziba i adres: ul. Karola Olszewskiego 6, 25-663 Kielce
- KRS 0001032499, NIP 9592061542, REGON 525113640
- sąd rejestrowy: Sąd Rejonowy w Kielcach, X Wydział Gospodarczy Krajowego Rejestru Sądowego
- kapitał zakładowy: 40 000,00 zł

*(Obie pozycje odczytane 2026-09-03 z odpisu pełnego w rejestrze KRS, `api-krs.ms.gov.pl`, stan z dnia 15.07.2026; zapis sądu pochodzi z pola „REJESTRACJA W KRAJOWYM REJESTRZE SĄDOWYM" odpisu, kwota z pola `wysokoscKapitaluZakladowego`. Founder potwierdza jednym spojrzeniem w odpis, zanim zlecenie pójdzie do Claude Design - dane rejestrowe zmieniają się wpisem, więc odczyt sprzed tygodnia nie jest gwarancją.)*

**Dane kontaktowe do umieszczenia** (konwencja IRIN, wartości od foundera): e-mail [E-MAIL], telefon [TELEFON], strona [ADRES STRONY]. **To jedyne trzy pola, które zostały do wypełnienia** - repozytorium ich celowo nie przechowuje (zasada minimalizacji, `kontekst-firmy-sanitized.md`), a zgadywać ich nie wolno.

**Pola wizytówki:** imię i nazwisko, stanowisko, telefon bezpośredni, e-mail. Na wzorze użyj placeholderów w nawiasach kwadratowych, nie zmyślonych osób.

**Kolor wiodący:** Aksamit w roli `primary`, zgodnie z tabelą w `paleta-barw.md`. Papier firmowy jest dokumentem całej firmy, nie jednej dziedziny; nie sygnalizuj żadnej z trzech dziedzin. Jeżeli w trakcie pracy uznasz, że dokument bez koloru dziedzinowego wypada niejednoznacznie wobec reguły 80/15/5, zapisz to jako uwagę do foundera, nie wybieraj dziedziny samodzielnie.

**Znak:** na papierze wariant poziomy `logo_irin_poziom.svg`; na wizytówce wariant do Twojego wyboru między poziomym a pionowym na awersie, a na rewersie sygnet `logo_irin_sygnet.svg` samodzielnie. Zmierz i zapisz, w jakiej szerokości sygnet stoi na rewersie; to potrzebne do protokołu pomiaru.

**Treść przykładowa pisma na stronie pierwszej** (tekst zastępczy do pokazania układu, nie korespondencja):

> **[Kicker]** OFERTA SZKOLENIOWA · WRZESIEŃ 2026
>
> **[Lead, Manrope 500]** Dziękujemy za zainteresowanie szkoleniami Instytutu Rozwoju i Nauki. Poniżej przedstawiamy zakres usług, które mogą zostać objęte wnioskiem o środki Krajowego Funduszu Szkoleniowego.
>
> **[H3, Manrope 600, bezpośrednio pod leadem, celowo]** Źródła finansowania, o które występuje pracodawca
>
> **[Korpus, Manrope 400]** Dofinansowanie zależy od decyzji powiatowego urzędu pracy i od priorytetów ustalonych na dany rok; nasza rola kończy się na przygotowaniu programu kształcenia i wzoru zaświadczenia. Żółć, gęś, źdźbło, ćma, łódź, ńandu, świt, żółw: ĄĆĘŁŃÓŚŹŻ ąćęłńóśźż.
>
> **[Dane techniczne, Inconsolata]** Nr pisma: IRIN/2026/09/0001 · Kod usługi BUR: [KOD]

Zdanie z żółcią i gęsią jest w tekście celowo: zawiera wszystkie polskie znaki diakrytyczne w obu wielkościach. Zachowaj je w każdej wadze użytej w piśmie.

**Format wyniku:** PDF w skali 1:1 dla obu elementów oraz podgląd z naniesioną siatką sześciu kolumn (25 mm, gutter 4 mm) na stronie pierwszej papieru.

---

## 3. Protokół pomiaru po powrocie z Claude Design

Pilot ma wartość tylko wtedy, gdy jego wynik trafi do warstwy 1. Cztery pomiary i jedno pytanie; każdy ma wpisane, gdzie ląduje.

| Nr | Co sprawdzić | Jak | Gdzie wpisać wynik |
|---|---|---|---|
| 1 | Polskie znaki na wagach 400, 500 i 600 (korpus, lead, H3) | Powiększyć zdanie testowe w PDF; szukać brakujących ogonków, kresek, zamienników z innego kroju. | `/01-baza-wiedzy/identyfikacja/typografia.md`, sekcja „Alfabet polski”: zmienić „pokrycie potwierdzone w zakresie, w jakim je zmierzono” na wynik, z datą. |
| 2 | Siatka 6 × 25 mm z realną treścią | Na podglądzie z siatką: czy blok danych rejestrowych, logotyp i kolumna tekstu siadają na kolumnach bez łamania modułu; czy margines prawy 22 mm nie wygląda na błąd. | `/01-baza-wiedzy/identyfikacja/siatka-a4.md`: dopisać sekcję „Pierwsze użycie” z wynikiem. |
| 3 | H3 bezpośrednio pod leadem | Czy różnica wagi 500 wobec 600 przy tym samym stopniu 16 px jest widoczna bez kickera. Jeśli nie, zasada 5 z `format-paczki.md` (użyj kickera) zostaje potwierdzona jako konieczna. | `/01-baza-wiedzy/identyfikacja/typografia.md`, sekcja o H3. |
| 4 | Sygnet samodzielny na rewersie wizytówki | Zmierzona szerokość sygnetu w mm i ocena czytelności. Jeśli stoi w 10 mm i jest czytelny, wiersz „10 mm / 44 px” w `logotyp.md` przechodzi z „nie potwierdzony osobno” na potwierdzony; jeśli nie, wpisać zmierzone minimum. | `/01-baza-wiedzy/identyfikacja/logotyp.md`, tabela minimalnych rozmiarów. |
| 5 | Dokument bez koloru dziedzinowego | Czy papier w samym Aksamicie jako `primary` czyta się jako spójny z systemem 80/15/5. Odpowiedź foundera po obejrzeniu wyniku. | `/01-baza-wiedzy/identyfikacja/paleta-barw.md`, sekcja o regule 80/15/5: dopisać zdanie o dokumentach ogólnofirmowych. |

**Czego ten pilot nie sprawdzi:** kontrastu Karminu obok Aksamitu na realnym dokumencie. Papier firmowy i wizytówka nie mają stanu błędu, więc Karmin się na nich nie pojawia. Ten falsyfikator czeka na pierwszy dokument ze statusami (certyfikat albo karta usługi BUR) i jest tak zapisany w `/MAPA-DROGOWA.md`, bramka B.

## 4. Co blokuje wysłanie

Nic decyzyjnego. **Stan na 2026-09-03: z pięciu pól w nawiasach kwadratowych zostały trzy.** Sąd rejestrowy i kapitał zakładowy odczytano z rejestru KRS i wpisano do punktu 2; do wypełnienia zostają e-mail, telefon i adres strony - dane operacyjne, których repozytorium celowo nie trzyma.

Po wysłaniu i powrocie wyniku: wykonać punkt 3, potem zaktualizować `/PLAN.md` (zadanie 22) i `/MAPA-DROGOWA.md` (bramka B).
