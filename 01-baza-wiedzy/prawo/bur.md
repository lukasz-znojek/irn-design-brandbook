# Baza Usług Rozwojowych (BUR) — wymogi certyfikacji

Status weryfikacji: **wszystkie sekcje merytoryczne tego pliku są odczytane u źródła** - z sześciu plików PDF dostarczonych bezpośrednio przez foundera 2026-09-02 i przechowywanych w `./zrodla/`. Sekcje „Karta Usługi”, „Kod usługi” i „Zaświadczenie” odczytano 2026-09-02 (Załączniki 2g i 4). Sekcje „Warunek wpisu do BUR”, „Karta Dostawcy Usług”, „Ocena usługi po zakończeniu”, „Usługi zdalne”, „Dostępność”, „Publikowanie usług” i „Licencja na materiały” odczytano 2026-09-06 z Regulaminu oraz Załączników 1, 3 i 5 - te trzy załączniki były wcześniej dostarczone, ale nieprzeczytane. Domeny PARP pozostają zablokowane przez politykę sieciową środowiska Claude Code (pomiar powtórzony 2026-09-06; szczegóły: `./weryfikacja-u-zrodla.md`).

Jedyne, co w tym pliku nadal pochodzi ze źródeł wtórnych, to **nazwy konkretnych certyfikatów jakości** (SUS 2.0/3.0, ISO 9001) - patrz zastrzeżenie w sekcji „Warunek wpisu do BUR”.

## Co to jest BUR

Baza Usług Rozwojowych to internetowy rejestr podmiotów świadczących usługi rozwojowe (szkoleniowe, doradcze, coachingowe, e-learningowe), współfinansowane ze środków publicznych, prowadzony przez Polską Agencję Rozwoju Przedsiębiorczości (PARP). Podstawa prawna rejestru: rozporządzenie Ministra Rozwoju i Finansów z dnia 29 sierpnia 2017 r. w sprawie rejestru podmiotów świadczących usługi rozwojowe. Bieżące zasady działania samej bazy (poza rejestrem) określa **Regulamin Bazy Usług Rozwojowych** — dokument aktualizowany kilkukrotnie w ciągu roku (znalezione wersje: obowiązująca od 1 stycznia 2026 r., zmieniona od 13 marca 2026 r. i od 5 maja 2026 r.) — co oznacza, że szczegóły proceduralne poniżej trzeba sprawdzać w wersji regulaminu obowiązującej w dniu tworzenia konkretnego dokumentu, nie zakładać, że pozostają stałe.

## Warunek wpisu do BUR

Źródło pierwotne: **Regulamin BUR § 11 „Warunki i wymagania dla uzyskania wpisu do BUR”** (`./zrodla/regulamin-bazy-uslug-rozwojowych_wersja-2026-05-05.pdf`, s. 18-21), który powtarza i doprecyzowuje § 4-7 rozporządzenia Ministra Funduszy i Polityki Regionalnej z 28 lipca 2023 r. w sprawie rejestru podmiotów świadczących usługi rozwojowe. Cztery grupy warunków, spełniane łącznie:

1. **Potencjał techniczny** (§ 11 ust. 1) - pomieszczenia ze sprzętem i pomocami dydaktycznymi, bezpieczne i higieniczne warunki, obsługa osób ze szczególnymi potrzebami (pkt 3 - patrz sekcja „Dostępność” niżej) oraz, dla usług zdalnych, określenie szczegółowych wymagań technicznych i materiały dydaktyczne w formie dostosowanej do zdalnej realizacji (pkt 4).
2. **Potencjał ekonomiczny** (§ 11 ust. 2) - brak zaległości podatkowych i składkowych, brak zarządu komisarycznego, brak wniosku o upadłość, brak postępowania likwidacyjnego, naprawczego albo restrukturyzacyjnego.
3. **Potencjał kadrowy** (§ 11 ust. 3) - osoby realizujące usługę mają doświadczenie zawodowe albo kwalifikacje zdobyte nie wcześniej niż 5 lat przed datą publikacji usługi w BUR; dostawca trzyma poświadczone za zgodność z oryginałem kopie dokumentów.
4. **Należyta jakość** (§ 11 ust. 4, dziewięć wymagań) - w tym pkt 1: „posiada określoną misję swojej działalności oraz zdefiniowane cele strategiczne i operacyjne, które są okresowo weryfikowane i aktualizowane”; pkt 6: skuteczna komunikacja z usługobiorcą wraz z obsługą reklamacji i działaniami korygującymi; pkt 9: **certyfikat albo dokument poświadczający akredytację**, potwierdzający spełnienie pkt 1-8 i ust. 3.

Certyfikat wydaje jednostka niepowiązana osobowo ani kapitałowo z dostawcą, po audycie w siedzibie dostawcy i na podstawie dokumentów (§ 11 ust. 5, s. 20-21). **Dane firmy na certyfikacie muszą być zgodne z aktualnym dokumentem rejestrowym** (§ 11 ust. 5 zdanie pierwsze) - to ma bezpośredni skutek dla warstwy 2: nazwa IRIN na dokumentach związanych z BUR to nazwa rejestrowa, nie nazwa handlowa.

Poza tym: konto dostawcy w systemie BUR (`uslugirozwojowe.parp.gov.pl`) i publikacja **Karty Usługi** dla każdej usługi - dopiero po publikacji usługa jest widoczna w wyszukiwarce BUR. Wpis do BUR jest bezpłatny; kosztem po stronie IRIN jest uzyskanie i utrzymanie certyfikatu jakości.

**Co tu pozostaje niesprawdzone:** nazwy konkretnych certyfikatów uznawanych przez PARP (SUS 2.0/3.0, ISO 9001) pochodzą ze źródeł wtórnych. Regulamin ich nie wymienia, a Załącznik 1 (poz. 20, s. 11) odsyła po listę do „Strefy dla Dostawców Usług” na stronie BUR - dokumentu, którego nie mamy. Falsyfikator: pobranie tej listy ze strony BUR albo dostarczenie jej przez foundera.

**Weryfikacja aktualizacyjna** (§ 13, s. 23): Oświadczenie o zgodności danych trzeba aktualizować **nie rzadziej niż co 12 miesięcy** od daty wpisu; brak aktualizacji blokuje publikowanie usług do czasu pozytywnej weryfikacji, ale nie odbiera pozostałych uprawnień.

**Powiązanie z KFS:** od 1 stycznia 2026 r. wpis do BUR jest też warunkiem prowadzenia szkoleń finansowanych z Krajowego Funduszu Szkoleniowego — patrz `./kfs.md`. Dla IRIN oznacza to jeden wspólny wymóg rejestrowy dla obu ścieżek szkoleniowych, nie dwa osobne.

**Powiązanie z PSF:** dla Podmiotowego Systemu Finansowania (PSF, patrz `./psf.md`) potwierdzone jest, że **usługa** musi być wybrana z BUR — warunek konieczny mechanizmu PSF niezależnie od regionu. Wpis **dostawcy** do BUR (konto + regulamin, jak w sekcji wyżej) jest tu wymagany pośrednio, tą samą drogą co dla każdej usługi w BUR — bo usługa nie może być opublikowana bez zarejestrowanego za nią dostawcy (Regulamin BUR, Załącznik nr 4 „Zasady funkcjonowania Dostawców usług"; źródła w `./psf.md`). To nie jest osobny, PSF-specyficzny przepis analogiczny do KFS — wynika z ogólnej mechaniki BUR. **Status: rozstrzygnięte 2026-09-03 dla jednego operatora** (WUP w Kielcach, województwo świętokrzyskie) - bez akredytacji regionalnej, ale z czterema obowiązkami ponad wpis do BUR; pełny zapis i granica tego ustalenia w `./psf.md`, sekcja „Co operator PSF nakłada na Dostawcę Usług ponad wpis do BUR”. Otwarte zostaje to samo pytanie dla pozostałych województw.

Pomiar 2026-09-06, wyjaśniający, dlaczego trzeba było sięgnąć po dokument operatora: w pełnym tekście Regulaminu BUR (wersja od 5 maja 2026 r., 35 stron) **nie występuje ani razu** słowo „PSF”, „operator” ani zwrot „podmiotowy system finansowania”. Regulamin nie rozstrzyga tego pytania w żadną stronę - ani nie zakazuje operatorom stawiania dodatkowych warunków, ani na to nie zezwala. **Praktyczny wniosek na przyszłość: dla kolejnego województwa żaden dokument PARP nie zastąpi regulaminu tamtejszego operatora** - trzeba pobrać i przeczytać ten regulamin, tak jak zrobiono to dla WUP w Kielcach.

## Karta Dostawcy Usług - publiczny profil firmy w BUR

Źródło: **Załącznik 1 do Regulaminu BUR, „Wzór formularza Karty Dostawcy Usług wraz z instrukcją jej wypełniania”, wersja obowiązująca od 1 stycznia 2026 r.** (`./zrodla/zalacznik-1-karta-dostawcy-uslug_wersja-2026-01-01.pdf`, 14 stron). Karta Dostawcy to profil firmy widoczny w BUR - dla brandbooka jest to nośnik marki, bo obok Karty Usługi jest jedynym miejscem, w którym IRIN prezentuje się w systemie.

**Pola obowiązkowe** (numeracja pozycji jak w załączniku): 4. NIP (10 znaków), 5. Nazwa podmiotu, 7. Forma prawna (wybór z listy), 10. Dane teleadresowe - siedziba i adres, 13. Nr telefonu, 14. Adres e-mail.

**Pola opcjonalne:** 1. Logo, 2. Instytucja zagraniczna, 3. REGON, 6. Nazwa stosowana w obrocie gospodarczym, 8. Załączniki (referencje, licencje), 9. Charakterystyka działalności firmy, 11-12. Zintegrowany Rejestr Kwalifikacji, 15. Strona internetowa.

Cztery ustalenia istotne dla identyfikacji IRIN:

- **Logo jest polem opcjonalnym.** Pełny zapis instrukcji (poz. 1, s. 1): „Pole opcjonalne / Podmiot świadczący Usługi rozwojowe/ Dostawca Usług ma możliwość dodania logotypu jakim posługuje się w obrocie gospodarczym.” Załącznik **nie podaje** wymaganego formatu pliku, wymiarów, proporcji, wagi ani wymagań co do tła. Dobór wariantu logotypu do tego pola jest więc swobodnym wyborem projektowym IRIN, nie wymogiem - patrz `/01-baza-wiedzy/identyfikacja/logotyp.md`.
- **Nazwa rejestrowa i nazwa handlowa to dwa osobne pola.** Poz. 5 (obowiązkowe) wymaga nazwy „zgodną z dokumentem rejestrowym np.: KRS, CEIDG, RSPO, POL-on, RAD-on, GUS”; poz. 6 (opcjonalne) to „Nazwa stosowana w obrocie gospodarczym”. Rozróżnienie nazwy rejestrowej i marki handlowej ma więc oparcie w źródle, nie jest samą konwencją IRIN. Instrukcja wylicza też znaki specjalne dopuszczone w nazwie: `-. , ' () / @ & " #; + _! $ : „`
- **Załączniki:** maksymalnie 10 dokumentów, maksymalna wielkość pliku 5 MB (poz. 8, s. 3). Obowiązuje zakaz zamieszczania danych osobowych osób trzecich bez ich wiedzy i podstawy prawnej; instrukcja wskazuje PESEL i adres zamieszkania jako przykłady. Dotyczy to referencji - z materiałów referencyjnych IRIN trzeba usuwać dane osobowe.
- **Oświadczenie o etyce zawodowej** (poz. 19, s. 10) obejmuje m.in. to, że dostawca „zapewnia poprawność i jasność sformułowań w zawieranych umowach”. To jedyny zapis w tym dokumencie dotykający języka dokumentów IRIN - i dotyczy umów, nie materiałów marketingowych.

Uwaga o samych dokumentach źródłowych: Załącznik 1 i Regulamin nazywają się „do Regulaminu Bazy Usług Rozwojowych (BUR)”, a Załącznik 3 - „do Regulaminu Rejestru Usług Rozwojowych”. Rozbieżność jest po stronie PARP, nie repozytorium; nie zmienia treści żadnego z tych dokumentów.

**Status: odczytane u źródła**, `./zrodla/zalacznik-1-karta-dostawcy-uslug_wersja-2026-01-01.pdf`, 2026-09-06.

## Karta Usługi - obowiązkowe pola

Źródło: **Załącznik nr 2g do Regulaminu Bazy Usług Rozwojowych, „Wzór formularza Karty Usługi wraz z instrukcją jej wypełniania - usługa szkoleniowa”, wersja obowiązująca od 6 lipca 2026 r.** (`./zrodla/zalacznik-2g-karta-uslugi-szkoleniowa_wersja-2026-07-06.pdf`, 76 stron). Regulamin przewiduje siedem wariantów Karty Usługi wg podrodzaju usługi (2a coaching, 2b doradztwo biznesowe, 2c egzamin, 2d mentoring, 2e o charakterze zawodowym, 2f studia podyplomowe, **2g usługa szkoleniowa** - Regulamin BUR § 23, `./zrodla/regulamin-bazy-uslug-rozwojowych_wersja-2026-05-05.pdf`, s. 35); IRIN świadczy usługi szkoleniowe, więc 2g jest właściwym wzorem.

Pola oznaczone w formularzu jako „Pole obowiązkowe” (numeracja jak w załączniku; strony w nawiasie odnoszą się do pliku 2g):
- **1.2 Rodzaj świadczonej usługi**, **1.3 Podrodzaj świadczonej usługi**, **1.4 Forma świadczenia usługi** (s. 2).
- **1.5 Wariant zajęć** - jeden z trzech: zajęcia indywidualne / zajęcia grupowe / zajęcia grupowe z praktyką indywidualną; nie występuje dla formy zdalnej; blokowane do edycji po publikacji usługi (s. 9-10).
- **1.6 Podstawa uzyskania wpisu do BUR**, **1.7 Usługa zamknięta** (s. 11-12).
- **2.1 Tytuł usługi**, **2.2 Kategoria usługi**, **2.3 Podkategoria usługi** (s. 12-13).
- **2.6 Grupa docelowa**, **2.7 Minimalna liczba Uczestników**, **2.8 Maksymalna liczba Uczestników** (s. 16-18).
- **3.1 Cel edukacyjny** wraz z **3.1.4 Efekty uczenia się** (s. 19-37).
- **3.2.1 Efekt usługi oraz kryteria jego weryfikacji**, **3.2.2 Metoda potwierdzenia** (dla celu biznesowego, jeśli wskazany).
- **4.1 Liczba godzin zegarowych usługi** - faktyczna liczba godzin uwzględniająca proces kształcenia i walidację, łącznie z przerwami zgodnie z harmonogramem; blokowane do edycji po publikacji (s. 49).
  - **4.1.1 w tym liczba godzin zajęć praktycznych indywidualnych** - obowiązkowe tylko dla wariantu „zajęcia grupowe z praktyką indywidualną” (s. 50).
  - **4.1.2 w tym liczba godzin zdalnych** - obowiązkowe tylko dla form mieszanych (stacjonarna/zdalna w czasie rzeczywistym połączona ze zdalną) (s. 50).
- **4.2-4.10 Stawka VAT i koszty** (netto/brutto, w tym walidacji i certyfikowania osobno, jeśli dotyczy).
- **5 Lokalizacja usługi** (s. 55).
- **6 Osoby prowadzące** - obowiązkowe, poza formą zdalną; dla osoby prowadzącej usługę: imię i nazwisko, adres e-mail, opis doświadczenia - każde obligatoryjne; dla osoby walidującej analogicznie, z zastrzeżeniem rozdzielności funkcji kształcenia i walidacji (s. 57-61).
- **7 Program i harmonogram usługi**, w tym **7.1 Ramowy program** i **7.2 Harmonogram usługi** (s. 61-65).
- **8 Dane kontaktowe** (s. 68).
- **9 Informacje dodatkowe** jako tytuł sekcji i **9.1 Informacja o materiałach dla uczestników** (s. 69).
- **10 Warunki techniczne** jako tytuł sekcji i **10.1 Warunki techniczne - opis**, **10.2 Kody dostępowe do usługi** (s. 71-72).

Suma godzin w harmonogramie musi być zgodna z liczbą godzin zegarowych zadeklarowaną w karcie (4.1, s. 49). **Status: odczytane u źródła**, `./zrodla/zalacznik-2g-karta-uslugi-szkoleniowa_wersja-2026-07-06.pdf`, 2026-09-02.

## Kod usługi

Regulamin BUR i Załącznik 4 („Zasady funkcjonowania Dostawców Usług”, wersja od 31 marca 2026 r., `./zrodla/zalacznik-4-zasady-funkcjonowania-dostawcow-uslug_wersja-2026-03-31.pdf`) potwierdzają, że każda usługa ma **„numer identyfikacyjny Usługi rozwojowej”** - nadawany przez system BUR i wymagany m.in. na dokumencie księgowym (Zał. 4, Rozdział 2, pkt 2) oraz na zaświadczeniu uczestnika (Zał. 4, Rozdział 2, pkt 3, s. 6-7 - patrz sekcja „Zaświadczenie” niżej). **Żaden z sześciu przejrzanych dokumentów PARP (Regulamin i Załączniki 1, 2g, 3, 4, 5) nie definiuje wewnętrznej struktury tego numeru** - czy i jak dzieli się na segmenty, co oznacza rok/kolejność/typ usługi. Zapis `2025/00817/PPUR` z `brandbook.dc.html` (canvas foundera, materiał inspiracyjny - patrz `/CLAUDE.md`) pozostaje więc **niepotwierdzonym formatem** - nie z powodu braku dostępu do źródła (jak poprzednio), tylko dlatego, że przejrzane dokumenty nie precyzują tej struktury. Praktyczny wniosek jest taki sam jak wcześniej: karta usługi BUR w warstwie 2 nie powinna zakładać żadnej konkretnej struktury numeru - ma wstawiać rzeczywisty numer nadany przez system dla danej usługi, bez próby jego rekonstrukcji czy formatowania.

**Status: odczytane u źródła** - struktura numeru nie jest zdefiniowana w przejrzanych dokumentach, 2026-09-02.

## Ocena usługi po zakończeniu

Źródło: **Załącznik 3 do Regulaminu BUR, „System Oceny Usług Rozwojowych”, wersja obowiązująca od 8 lipca 2025 r.** (`./zrodla/zalacznik-3-system-oceny-uslug-rozwojowych_wersja-2025-07-08.pdf`, 5 stron) oraz **Regulamin BUR § 15 ust. 5-6** (s. 24-25).

Wcześniejszy zapis tej sekcji („ankieta obejmuje aspekty merytoryczne i organizacyjne - zgodność z opisem, przydatność treści”) pochodził ze źródła wtórnego i **był nieprecyzyjny**. Odczyt pierwotny: obowiązuje jeden wzór ankiety dla wszystkich rodzajów usług, złożony z **trzech pytań** (Zał. 3, cz. I pkt 2 i 5, s. 1-2):

| Pytanie | Treść | Skala | Waga |
|---|---|---|---|
| P1 | „W jakim stopniu wg Pana/Pani opinii cel usługi rozwojowej został zrealizowany/osiągnięty?” | 1-5 | 0,5 |
| P2 | „W jakim stopniu zrealizowana usługa rozwojowa spełniła Pana/Pani oczekiwania pod względem jakości i zawartości merytorycznej?” | 1-5 | 0,3 |
| P3 | „W jakim stopniu polecił(a)by Pan/Pani tę usługę rozwojową innej osobie/innemu pracodawcy?” | 1-5 | 0,2 |

Ocena pojedynczej usługi: `0,5*P1 + 0,3*P2 + 0,2*P3` (Zał. 3, cz. II pkt 7, s. 4). Ocena ogólna: `OU = 0,5*OUD + 0,5*OUN`, gdzie OUD to średnia ocen uczestników, a OUN średnia ocen pracodawców delegujących; gdy oceniają wyłącznie uczestnicy, ich waga wynosi 1 (cz. II pkt 8-9, s. 4-5). Ocena wystawiona przez samego Dostawcę Usług jest **nieobowiązkowa i nie wchodzi do oceny ogólnej** (cz. I pkt 3, s. 1). Uczestnik odpowiada na P1-P3, pracodawca na P1 i P3, dostawca tylko na P1 (matryca, s. 2).

Obowiązki dostawcy i terminy:
- Aktualizacja listy uczestników i nadanie statusów („zaakceptowany”, „odrzucony”, „ukończył”, „nie ukończył”, „nie uczestniczył”) **nie później niż w ciągu 7 dni od zakończenia usługi** (Regulamin § 15 ust. 5-6, s. 24-25; Zał. 3, cz. II pkt 1, s. 3). Brak aktualizacji: status usługi zmienia się na „niezrealizowana”, uczestnicy automatycznie na „nie uczestniczył”, **ankiety się nie wygenerują**.
- Zmiana składu uczestników wobec pierwotnego zgłoszenia musi być zamknięta **najpóźniej w ostatnim dniu realizacji usługi** (Zał. 3, cz. II pkt 3, s. 3).
- Przypomnienia o ankiecie system wysyła w 8., 16., 24. i 28. dniu kalendarzowym od zakończenia usługi (cz. II pkt 6, s. 4).

Skutki dla marki: oceny usług przekładają się na **średnią ocenę Dostawcy Usług**, a obok uśrednionej oceny system prezentuje liczbę ankiet, na podstawie których ją wyliczono (cz. II pkt 11-12, s. 5). Dostawca ma podgląd i eksport ogólnych ocen swoich usług (cz. II pkt 10, s. 5).

**Czego Załącznik 3 nie reguluje:** nie ma w nim żadnego zakazu ani warunku posługiwania się ocenami z BUR we własnych materiałach dostawcy - przejrzano wszystkie 5 stron. Zakaz z cz. I pkt 6 (s. 3) dotyczy treści komentarzy wpisywanych do ankiety przez oceniających (treści sprzeczne z prawem, nawołujące do nienawiści, pornograficzne, powszechnie uważane za nieetyczne), nie materiałów marketingowych. Wniosek: podawanie oceny BUR w materiałach IRIN **wraz z liczbą ankiet** to konwencja organizacyjna IRIN (odwzorowanie tego, co pokazuje sam system), nie wymóg prawny - zapisana w `/02-szablony-dokumentow/karta-uslugi-bur.md` i `/02-szablony-dokumentow/prezentacja-sprzedazowa.md` (`material-sprzedazowy.md` jej nie dotyczy, bo opisuje materiał wewnętrzny dla handlowców, nie materiał dla klienta).

**Status: odczytane u źródła**, `./zrodla/zalacznik-3-system-oceny-uslug-rozwojowych_wersja-2025-07-08.pdf` i Regulamin § 15, 2026-09-06.

## Usługi zdalne - Standard SUZ jest wiążący

Regulamin BUR § 15 ust. 3 (s. 24): „W przypadku realizacji Usług rozwojowych realizowanych w formie zdalnej Dostawca Usług jest zobowiązany do jej świadczenia zgodnie ze Standardem Usług Zdalnego Uczenia się (SUZ), stanowiącym Załącznik 5 do Regulaminu.” Standard SUZ nie jest więc poradnikiem - **dla każdej usługi zdalnej IRIN jest wymogiem**. Ma to bezpośrednie znaczenie dla planowanego portalu szkoleń (`/01-baza-wiedzy/uslugi/portal-szkolen.md`).

Źródło: **Załącznik 5, „Standard Usług Zdalnego Uczenia się SUZ”, luty 2021** (`./zrodla/zalacznik-5-standard-uslug-zdalnego-uczenia-sie-suz_wersja-2021-02.pdf`, 15 stron, autorstwo PARP i Polskiej Izby Firm Szkoleniowych). Data w dokumencie zgadza się z nazwą pliku; dokument nie zawiera śladu nowszej aktualizacji. Standard ma 14 wymagań (SUZ-1 do SUZ-14) w trzech obszarach: relacja z klientem (SUZ-1 do 5), projektowanie usługi (SUZ-6 do 10), realizacja usługi (SUZ-11 do 14). Definicje: synchroniczność (równoczesny udział uczestników i trenera), asynchroniczność (interakcja uczestnika z materiałem bez równoczesnego udziału trenera), usługa mieszana (co najmniej dwie formy naraz, w tym stacjonarna) - s. 4 i 14.

Cztery wymagania, które dotykają dokumentów i materiałów IRIN:

- **SUZ-1** (s. 6): dostawca prowadzi działalność zgodnie z regulacjami dotyczącymi praw autorskich, ochrony danych osobowych, zakresu licencji i **ochrony wizerunku osób**. Zakres walidacji wymienia wprost: „Czy Dostawca Usług stosuje zasady ustawy o dostępności cyfrowej, stron internetowych i aplikacji mobilnych.” Dla portalu szkoleń to wymóg, nie dobra praktyka.
- **SUZ-2** (s. 7): „Dostawca Usług publikuje rzetelne informacje dotyczące swojej działalności w obszarze usług zdalnego uczenia się”, a zakres walidacji brzmi: „Czy informacje podawane przez Dostawcę Usług są zgodne z rzeczywistymi możliwościami i usługami tego podmiotu.” Jako źródła dowodów standard wymienia m.in. stronę internetową dostawcy, dokumenty ofertowe i publikacje w kanałach marketingowych (www, kanały SOME) - **materiały sprzedażowe IRIN są w zakresie tego wymagania**.
- **SUZ-3** (s. 7-8): dostawca „jasno komunikuje zakres licencji i dozwolony sposób użytkowania” produktów cyfrowych. Materiał przekazywany uczestnikowi potrzebuje więc jawnej informacji o licencji.
- **SUZ-8** (s. 10): materiały i narzędzia przygotowane „zgodnie z określonymi standardami technicznymi zapewniającymi ich dostępność i kompatybilność, również w kontekście urządzeń mobilnych”, z przywołaniem standardów SCORM i xAPI.

**Czego SUZ nie reguluje:** nie podaje żadnego poziomu WCAG, wartości kontrastu, minimalnej wielkości pisma ani wymogów typograficznych - przejrzano wszystkie 15 stron, łącznie ze słownikiem. Reguły kontrastu w `/01-baza-wiedzy/identyfikacja/paleta-barw.md` pozostają więc **konwencją IRIN**, nie wymogiem BUR; wymóg ustawowy wchodzi osobną drogą - przez SUZ-1 (ustawa o dostępności cyfrowej, dla serwisów i aplikacji) i przez § 11 ust. 1 pkt 3 Regulaminu (materiały dydaktyczne na wniosek osoby ze szczególnymi potrzebami, sekcja niżej).

**Status: odczytane u źródła**, `./zrodla/zalacznik-5-standard-uslug-zdalnego-uczenia-sie-suz_wersja-2021-02.pdf`, 2026-09-06.

## Dostępność dla osób ze szczególnymi potrzebami

Regulamin BUR § 11 ust. 1 pkt 3 (s. 18) - warunek potencjału technicznego, więc warunek samego wpisu do BUR: „w przypadku Usług rozwojowych, w których zainteresowanie udziałem wyrazi osoba ze szczególnymi potrzebami w rozumieniu art. 2 pkt 3 ustawy z dnia 19 lipca 2019 r. o zapewnianiu dostępności osobom ze szczególnymi potrzebami (Dz.U. z 2024 r. poz. 1411, z późn. zm.), **zapewnia na jej wniosek materiały dydaktyczne dostosowane do potrzeb tej osoby** oraz wypełnia wymagania w zakresie dostępności usług, o których mowa w art. 6 pkt 1 i 2 oraz pkt 3 lit. a, b i d tej ustawy”. Ten sam zapis powtarza Załącznik 1, poz. 16 (s. 7-8), jako oświadczenie składane przy wpisie.

Regulamin § 15 ust. 1 (s. 24) domyka to od drugiej strony: dostawca może odmówić świadczenia usługi tylko w uzasadnionych przypadkach, „z zastrzeżeniem, iż przypadki te nie dotyczą materiałów i wymogów, o których mowa w § 11 ust. 1 pkt 3” - czyli **potrzeba dostosowania materiałów nie może być powodem odmowy**.

Skutek dla warstwy 2 i 3: każdy szablon materiału dydaktycznego IRIN musi mieć przewidzianą ścieżkę wersji dostosowanej (na wniosek uczestnika), a nie jedną wersję graficzną bez alternatywy. To **element prawnie obowiązkowy**. Sam kształt dostosowania (powiększony druk, wersja tekstowa, opis alternatywny grafik) nie jest w tych dokumentach określony - odsyłają do art. 6 ustawy o zapewnianiu dostępności, którego treści nie mamy w repozytorium. **Niesprawdzone:** dokładny zakres art. 6 pkt 1, 2 i 3 lit. a, b, d tej ustawy - falsyfikator: odczyt ustawy z Dz.U. (domena zablokowana, patrz `./weryfikacja-u-zrodla.md`).

## Publikowanie usług i terminy zmian

Regulamin BUR § 14 (s. 23-24) i § 15 ust. 4 (s. 24):
- Jedna usługa - jedna Karta Usługi (§ 14 ust. 2). Karty tego samego dostawcy o tym samym terminie, lokalizacji, osobie prowadzącej lub kodzie dostępowym mogą zostać zablokowane do wyjaśnienia (ust. 3).
- Informacje z Karty Usługi są **ogólnodostępne**, wyjątkiem jest usługa zamknięta - wtedy widzi je tylko adresat usługi i Administrator Regionalny BUR (§ 14 ust. 5-6). Karta Usługi jest więc publicznym dokumentem marki.
- Wyszukiwarka BUR prezentuje usługi w kolejności wprowadzania, od ostatnio dodanej (§ 14 ust. 4) - kolejność nie zależy od oceny ani od żadnego elementu wizualnego.
- Terminy zmian: zmiana terminu rozpoczęcia albo miejsca - najpóźniej **6 dni** przed rozpoczęciem; obniżenie ceny - najpóźniej **1 dzień** przed rozpoczęciem; odwołanie usługi - do 1 dnia przed rozpoczęciem, a bez zapisanych uczestników do dnia zakończenia (§ 15 ust. 4).
- Usługi z dofinansowaniem: dostawca poddaje się **wizycie monitoringowej bez uprzedzenia** w dowolnym momencie usługi i przedstawia wyjaśnienia co do zakresu i kalkulacji ceny (§ 17, s. 26).

## Licencja na materiały zamieszczone w BUR

Regulamin BUR § 16 (s. 25-26) - ustalenie o bezpośrednim skutku dla logotypu i materiałów IRIN. Zamieszczając w BUR materiał mający charakter utworu, Dostawca Usług „udziela Administratorowi BUR na czas nieoznaczony nieodpłatnej, niewyłącznej licencji na korzystanie z udostępnionych utworów dla potrzeb świadczenia Usług rozwojowych w BUR oraz zrzeka się wszelkich roszczeń w stosunku do Administratora BUR w przypadku ich wykorzystania, w tym kopiowania”. Pola eksploatacji wyliczone w ust. 2 obejmują m.in. pkt 6: „łączenie całości lub części utworu z innymi utworami, w tym z programami komputerowymi, a także scalanie, dostosowywanie, przerabianie oraz dokonywanie wszelkich zmian służących połączeniu z innymi utworami” oraz pkt 7 - udzielanie dalszych licencji osobom trzecim.

Skutek: **cztery zakazy modyfikacji logotypu z `/01-baza-wiedzy/identyfikacja/logotyp.md` wiążą IRIN i wykonawców IRIN, ale nie wiążą Administratora BUR** w odniesieniu do materiałów wgranych do BUR. To nie jest powód, żeby zakazy zmieniać - to powód, żeby świadomie decydować, co IRIN wgrywa do systemu. Dostawca odpowiada też za uzyskanie zgód, gdy prawa do materiału przysługują osobom trzecim (ust. 1 zdanie ostatnie) - dotyczy zdjęć, krojów pisma i grafik licencjonowanych.

## Czego dokumenty BUR nie regulują

Pomiar wykonany 2026-09-06 na pełnym tekście wszystkich sześciu dokumentów z `./zrodla/` (Regulamin i Załączniki 1, 2g, 3, 4, 5), wyszukiwanie po rdzeniach: `logo`, `logotyp`, `znak`, `oznaczen`, `marka`, `marki`, `reklam`, `promocj`, `wizerun`:

- **Słowa „logo” i „logotyp” występują w całym korpusie dokładnie dwa razy - oba w Załączniku 1, poz. 1 (pole opcjonalne Karty Dostawcy).** Nigdzie indziej.
- W Regulaminie jedyne trafienia to „logowanie” (§ 1, o środkach identyfikacji elektronicznej) i „reklamacji” (§ 11 ust. 4 pkt 6, o obsłudze skarg) - żadne z nich nie dotyczy znaków ani reklamy.
- **Żaden z sześciu dokumentów nie nakłada obowiązku ani nie udziela prawa posługiwania się znakiem BUR, logo PARP ani znakiem Funduszy Europejskich.** Jedyne wystąpienie „Funduszy Europejskich” w korpusie to nazwy programów (FERS, FE dla Rozwoju Społecznego) w podstawie prawnej i przypisach, nie reguła oznaczania.
- Żaden dokument nie narzuca układu graficznego, kroju pisma, kolorów ani formy wizualnej Karty Usługi, zaświadczenia ani materiałów dydaktycznych.

Wniosek dla brandbooka: cała warstwa wizualna dokumentów BUR-owych IRIN jest **swobodnym wyborem projektowym**, ograniczonym tylko listami treści obowiązkowej (Karta Usługi - Zał. 2g, zaświadczenie - Zał. 4) i wymogiem dostępności (§ 11 ust. 1 pkt 3).

**Falsyfikator tego wniosku:** dokument PARP spoza tych sześciu - w szczególności materiały ze „Strefy dla Dostawców Usług” na stronie BUR, do której odsyła Załącznik 1 (poz. 20-21), oraz wytyczne informacyjno-promocyjne programów, z których pochodzi dofinansowanie - może nakładać obowiązki oznaczania, których tu nie widać. Brak reguły w tych sześciu dokumentach nie jest dowodem, że reguły nie ma w ogóle.

## Zaświadczenie / certyfikat ukończenia usługi

**Rozbieżność wobec wcześniejszego zapisu w tym pliku - rozstrzygnięta źródłem pierwotnym.** Wcześniejsza wersja tej sekcji zakładała istnienie osobnego „Załącznika nr 12 do Regulaminu - wzór Zaświadczenia” (wersja z 1 kwietnia 2025 r., z kopii lustrzanej na `bur-subregion.pl`). W aktualnym Regulaminie BUR (wersja od 5 maja 2026 r.) § 23 „Załączniki” wymienia jako integralną część Regulaminu wyłącznie Załączniki 1-5 - **Załącznika nr 12 już nie ma** (`./zrodla/regulamin-bazy-uslug-rozwojowych_wersja-2026-05-05.pdf`, s. 35). Nowszy dokument wygrywa: obowiązek wystawienia zaświadczenia i jego minimalna treść są dziś częścią **Załącznika 4 „Zasady funkcjonowania Dostawców Usług”, Rozdział 2 „Standardy świadczenia Usług rozwojowych”, pkt 3** (wersja obowiązująca od 31 marca 2026 r., `./zrodla/zalacznik-4-zasady-funkcjonowania-dostawcow-uslug_wersja-2026-03-31.pdf`, s. 6-7) - nie osobnego wzoru graficznego, tylko listy obowiązkowych elementów treści.

Zgodnie z tym przepisem Dostawca Usług **wydaje usługobiorcy zaświadczenie o skorzystaniu z Usługi rozwojowej, zawierające co najmniej**:
1. tytuł Usługi rozwojowej,
2. numer identyfikacyjny Usługi rozwojowej (patrz sekcja „Kod usługi” wyżej - struktura numeru nieokreślona, wstawić rzeczywisty numer z systemu),
3. datę świadczenia Usługi rozwojowej,
4. liczbę godzin Usługi rozwojowej,
5. informację na temat nabytych przez usługobiorcę efektów uczenia się lub innych osiągniętych efektów Usługi rozwojowej,
6. dane usługobiorcy,
7. numer identyfikacyjny wsparcia nadany w systemie teleinformatycznym (ID wsparcia) - dotyczy usług z dofinansowaniem, np. PSF/KFS,
8. kod kwalifikacji w Zintegrowanym Rejestrze Kwalifikacji zgodny z kodem wskazanym w opublikowanej informacji o usłudze - **tylko jeżeli usługobiorca nabył tę kwalifikację**.

Dostawca Usług ma też obowiązek wystawić korektę zaświadczenia w ciągu 7 dni od uzasadnionego wezwania usługobiorcy (ten sam punkt). Żaden z przejrzanych dokumentów nie narzuca układu graficznego zaświadczenia - to lista treści minimalnej, nie wzór wizualny; forma dokumentu (`/02-szablony-dokumentow/certyfikat.md`) pozostaje swobodnym wyborem projektowym w Claude Design.

**Status: odczytane u źródła**, `./zrodla/zalacznik-4-zasady-funkcjonowania-dostawcow-uslug_wersja-2026-03-31.pdf`, s. 6-7, 2026-09-02.

## Co z tego jest prawnie wiążące dla dokumentów IRIN

Prawnie obowiązkowe (wszystkie pozycje odczytane u źródła - Załączniki 2g i 4 dnia 2026-09-02, Regulamin oraz Załączniki 1, 3 i 5 dnia 2026-09-06):
- IRIN musi mieć aktualny wpis do BUR i certyfikat jakości potwierdzający spełnienie wymagań § 11 ust. 3 i ust. 4 pkt 1-8, żeby w ogóle prowadzić tę linię biznesową. Sama **nazwa** certyfikatu (SUS, ISO 9001) pozostaje ze źródeł wtórnych.
- IRIN musi mieć **określoną misję oraz zdefiniowane cele strategiczne i operacyjne, okresowo weryfikowane** (§ 11 ust. 4 pkt 1). To wymóg wpisu do BUR, nie ozdoba brandbooka - a treść misji jest materiałem, którego repozytorium jeszcze nie ma.
- Nazwa IRIN na dokumentach związanych z wpisem do BUR i na certyfikacie jakości musi być **zgodna z dokumentem rejestrowym** (§ 11 ust. 5; Zał. 1, poz. 5 i poz. 20). Nazwa handlowa ma osobne, opcjonalne pole (Zał. 1, poz. 6).
- Na wniosek osoby ze szczególnymi potrzebami IRIN musi zapewnić **materiały dydaktyczne dostosowane do jej potrzeb** i nie może z tego powodu odmówić usługi (§ 11 ust. 1 pkt 3 w związku z § 15 ust. 1).
- Usługi zdalne muszą być świadczone **zgodnie ze Standardem SUZ** (§ 15 ust. 3, Załącznik 5) - w tym z wymogiem rzetelności informacji publikowanych o własnej działalności (SUZ-2) i jasnego komunikowania zakresu licencji na materiały (SUZ-3).
- Karta usługi (wzór 2g - usługa szkoleniowa) musi zawierać wszystkie pola oznaczone jako obowiązkowe w Załączniku nr 2g - pełna lista wyżej. To są pola formularza w systemie PARP, nie materiał do zaprojektowania od nowa w warstwie 2, ale ich obecność w treści dokumentu (np. w karcie usługi drukowanej/PDF do dystrybucji, jeśli IRIN taką tworzy) jest wymogiem, nie wyborem.
- Zaświadczenie uczestnika musi zawierać co najmniej osiem elementów z Załącznika 4, Rozdział 2, pkt 3 - pełna lista wyżej.
- Numer identyfikacyjny usługi na obu dokumentach musi być rzeczywistym numerem nadanym przez system BUR - jego wewnętrzna struktura nie jest nigdzie zdefiniowana, więc nie wolno jej zakładać ani formatować od nowa.

Wszystko poza tym (układ graficzny, kolejność elementów na drukowanej karcie usługi, dodatkowe elementy wizualne, krój pisma, paleta) to konwencja organizacyjna IRIN lub swobodny wybór projektowy - nie wynika z regulaminu BUR; pomiar w sekcji „Czego dokumenty BUR nie regulują” wyżej.

Do rozważenia przy planowaniu materiałów, choć nie jest to wymóg wobec dokumentu: wszystko, co IRIN **wgrywa do BUR**, obejmuje szeroka licencja z § 16 (z prawem do przerabiania i sublicencjonowania). Wybór, które pliki tam trafiają, jest decyzją do podjęcia świadomie - patrz sekcja „Licencja na materiały zamieszczone w BUR”.

## Źródła

Pierwotne (odczytane bezpośrednio, pliki dostarczone przez foundera 2026-09-02, przechowywane w `./zrodla/`):
- Regulamin Bazy Usług Rozwojowych, wersja obowiązująca od 5 maja 2026 r. - `zrodla/regulamin-bazy-uslug-rozwojowych_wersja-2026-05-05.pdf`
- Załącznik nr 2g do Regulaminu BUR - Karta Usługi, usługa szkoleniowa, wersja obowiązująca od 6 lipca 2026 r. - `zrodla/zalacznik-2g-karta-uslugi-szkoleniowa_wersja-2026-07-06.pdf`
- Załącznik 4 do Regulaminu BUR - Zasady funkcjonowania Dostawców Usług, wersja obowiązująca od 31 marca 2026 r. - `zrodla/zalacznik-4-zasady-funkcjonowania-dostawcow-uslug_wersja-2026-03-31.pdf`
- Załącznik 1 do Regulaminu BUR - Karta Dostawcy Usług, wersja obowiązująca od 1 stycznia 2026 r. - `zrodla/zalacznik-1-karta-dostawcy-uslug_wersja-2026-01-01.pdf` *(przeczytany w całości 2026-09-06, 14 stron)*
- Załącznik 3 do Regulaminu BUR - System Oceny Usług Rozwojowych, wersja obowiązująca od 8 lipca 2025 r. - `zrodla/zalacznik-3-system-oceny-uslug-rozwojowych_wersja-2025-07-08.pdf` *(przeczytany w całości 2026-09-06, 5 stron)*
- Załącznik 5 do Regulaminu BUR - Standard Usług Zdalnego Uczenia się (SUZ), luty 2021 - `zrodla/zalacznik-5-standard-uslug-zdalnego-uczenia-sie-suz_wersja-2021-02.pdf` *(przeczytany w całości 2026-09-06, 15 stron)*

Regulamin BUR (35 stron) przejrzano 2026-09-06 w całości: spis paragrafów § 1-23, pełny odczyt § 11-§ 20 oraz § 22-23, wyszukiwanie po rdzeniach znakowych i marketingowych w całym pliku. Załącznik 2g i Załącznik 4 odczytano wcześniej, 2026-09-02.

Falsyfikator na przyszłość: żaden z powyższych plików nie jest datowany później niż 6 lipca 2026 r., a odczyty nastąpiły 2026-09-02 i 2026-09-06 - sieć PARP pozostała zablokowana przez cały czas trwania sesji (`./weryfikacja-u-zrodla.md`), więc nie sprawdzono, czy między 6 lipca a dniem odczytu PARP opublikowała nowszą wersję Regulaminu lub Załącznika 2g. Publikacja nowszej wersji na `uslugirozwojowe.parp.gov.pl` obala datowanie użyte wyżej. Ryzyko nie jest teoretyczne: § 22 ust. 3-4 Regulaminu (s. 34-35) daje Administratorowi BUR prawo do „dokonywania, w każdym czasie, jednostronnych zmian w Regulaminie BUR”, a zmiany „stają się obowiązujące w momencie ich opublikowania na stronie internetowej BUR” - bez okresu przejściowego. Każdy odczyt zapisany w tym pliku ma więc datę ważności, nie jest ustaleniem trwałym.

Wtórne (kontekst ogólny, sekcja „Warunek wpisu do BUR” wyżej - nieodczytane wprost):
- [Baza Usług Rozwojowych (BUR) — co to jest i jak działa — StartujzBUR](https://startujzbur.pl/baza-uslug-rozwojowych-co-to-jest/)
- [Certyfikacja SUS 2.0 — DEKRA](https://www.dekra-certification.com.pl/pl/certyfikacja-sus-2-0/)
- [SUS 3.0 — Standard Usług Szkoleniowo-Rozwojowych — PIFS](https://sus.pifs.org.pl/)
- [Rejestracja w Bazie Usług Rozwojowych z certyfikatem ISO 9001 — Multicert](https://multicert.pl/blog/rejestracja-baza-uslug-rozwojowych-iso-9001/)
- [Standard usługi rozwojowej od 5 maja 2026 r. — najważniejsze zmiany — PARP](https://www.parp.gov.pl/component/content/article/90425:standard-uslugi-rozwojowej-od-5-maja-2026-r-najwazniejsze-zmiany) *(nie pobrano bezpośrednio - domena zablokowana)*
- [Usługa rozwojowa: definicja i co musi zawierać opis usługi w BUR — Scheelite](https://scheelite.eu/usluga-rozwojowa-definicja-bur/)
- [Ocena usługi w BUR: na czym polega i jak wpływa na rynek usług — Scheelite](https://scheelite.eu/ocena-uslugi-w-bur-czym-jest-jak-dziala/)
