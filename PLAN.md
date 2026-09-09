# PLAN.md — kolejka zadań

Zadania w kolejności wykonania, jedno zdanie każde, z docelowym plikiem. Pozycje oznaczone **[FOUNDER]** wymagają decyzji foundera, zanim można je zacząć.

## Warstwa 1 — baza wiedzy

1. Spisać kontekst firmy IRIN (trzy linie biznesowe, model organizacyjny, historia) → `01-baza-wiedzy/firma/kontekst-firmy.md`. (uzupełnienie o mechanikę finansową/compliance, nieopisaną tam: `01-baza-wiedzy/firma/kontekst-firmy-sanitized.md`)
2. Zebrać obowiązujące przepisy dot. Krajowego Funduszu Szkoleniowego (KFS) → `01-baza-wiedzy/prawo/kfs.md`. (materiał źródłowy z dodatkowymi szczegółami — priorytety 2026, limity roczne wg wielkości firmy, checklista załączników wniosku: `01-baza-wiedzy/prawo/kontekst-kfs-sanitized.md`)
3. Zebrać wymogi certyfikacji BUR (Baza Usług Rozwojowych, PARP) → `01-baza-wiedzy/prawo/bur.md`.
4. Opisać regulacje dot. usług pożyczkowych UE/BGK → `01-baza-wiedzy/prawo/pozyczki-ue-bgk.md`.
5. Spisać wytyczne usługowe dla aplikacji przedstawicieli handlowych → `01-baza-wiedzy/uslugi/aplikacje-sprzedazowe.md`.
6. Spisać wytyczne dot. planowanego portalu sprzedaży szkoleń online → `01-baza-wiedzy/uslugi/portal-szkolen.md`. (portal jeszcze nie istnieje)
7. Uzupełnić `01-baza-wiedzy/00-INDEX.md` o odnośniki do wszystkich powyższych plików.

## Warstwa 1 — zrealizowane poza pierwotną kolejnością

Nie były ponumerowane wyżej, bo PLAN.md nie przewidywał jeszcze tych plików w chwili ich powstania:

- `01-baza-wiedzy/_szablony/karta-produktu.md` — szablon karty produktu/kanału dla warstwy 1.
- `01-baza-wiedzy/prawo/psf.md` — karta produktu PSF (Podmiotowy System Finansowania).
- `01-baza-wiedzy/prawo/kontekst-psf-sanitized.md` — bezpieczna wersja robocza materiału wewnętrznego o PSF, na której oparta jest `psf.md`.

## Warstwa 2 — szablony dokumentów

8. Karta specyfikacji viewbooka szkoleniowego → `02-szablony-dokumentow/viewbook.md`.
9. Karta specyfikacji karty usługi BUR → `02-szablony-dokumentow/karta-uslugi-bur.md`. (osobny dokument od `program-szkolenia.md` i `prezentacja-sprzedazowa.md` poniżej — karta usługi BUR to formalny dokument publikowany w BUR, nie program ani prezentacja)
10. Karta specyfikacji certyfikatu/zaświadczenia ukończenia szkolenia → `02-szablony-dokumentow/certyfikat.md`.
11. Karta specyfikacji papieru firmowego i wizytówki → `02-szablony-dokumentow/papier-firmowy.md`.
12. Karta specyfikacji materiałów aplikacji sprzedażowej → `02-szablony-dokumentow/material-sprzedazowy.md`.
13. Karta specyfikacji programu szkolenia → `02-szablony-dokumentow/program-szkolenia.md`.
14. Karta specyfikacji prezentacji produktowo-sprzedażowej → `02-szablony-dokumentow/prezentacja-sprzedazowa.md`.

## Warstwa 3 — pakiet Claude Design

15. Zdefiniować format paczki wejściowej dla Claude Design → `03-pakiet-claude-design/format-paczki.md`. **[FOUNDER] — rozstrzygnięte (2026-09-02):** siatka A4 (6 kolumn, moduł 25 mm, gutter 4 mm — poprawka błędu wymiarów z kanwy) i paleta zatwierdzone przez foundera; paleta obowiązuje w wersji 14-kolorowej „Kaszmir Wyciszony”. Obie specyfikacje leżą w `01-baza-wiedzy/identyfikacja/`, a `format-paczki.md` do nich odsyła i dokłada zasady użycia. Historia pierwszej decyzji: `03-pakiet-claude-design/propozycja-palety-i-siatki-do-potwierdzenia.md`.
16. Napisać prompt bazowy dla Claude Design, odwołujący się do warstw 1 i 2 → `03-pakiet-claude-design/prompt-bazowy.md`.

## Domknięcie projektu

Wykonanie zadań 20-23 śledzą issues w GitHubie (nadrzędne: #29 etap 2, #38 etap 4, #46 etap 5, #52 decyzje odłożone); ten plik zostaje źródłem decyzji i specyfikacji. Mapa zależności: `MAPA-DROGOWA.md`, sekcja „Śledzenie w GitHub”.

17. Etapy 0-5 z bramkami, podział na to, co robi Claude Code, co rozstrzyga founder i co wymaga odczytu dokumentów u źródła → `MAPA-DROGOWA.md`. Zrealizowane.
18. Etap 0, higiena: poprawić nieaktualne zdania w `00-INDEX.md`, `01-baza-wiedzy/README.md` i tym pliku; scalić PR #4, zamknąć PR #6. Zrealizowane 2026-09-02, poza usunięciem dwóch martwych gałęzi (blokuje to proxy sesji; do zrobienia w GitHubie ręcznie).
19. Etap 1, decyzje foundera blokujące pilota: forma prawna, siedziba i dane rejestrowe oraz konwencja papieru firmowego i wizytówki → `01-baza-wiedzy/firma/`, `02-szablony-dokumentow/papier-firmowy.md`. Zrealizowane 2026-09-02; sześć decyzji odłożonych do pierwszego użycia dokumentu zostaje w `MAPA-DROGOWA.md`.
20. Etap 2, weryfikacja prawna u źródła: osiem dokumentów z `01-baza-wiedzy/prawo/weryfikacja-u-zrodla.md` → pliki w `01-baza-wiedzy/prawo/` i karty w `02-szablony-dokumentow/`. **Pozycje 1-3 zrealizowane 2026-09-02**: founder dostarczył sześć PDF-ów PARP (`01-baza-wiedzy/prawo/zrodla/`), z których odczytano listę pól Karty Usługi (Załącznik 2g), osiem elementów zaświadczenia (Załącznik 4, Rozdział 2 pkt 3) i brak zdefiniowanej struktury numeru usługi; przy okazji ustalono, że Załącznik nr 12 nie istnieje w Regulaminie od 5 maja 2026 r. **Pozycje 4-6 zrealizowane 2026-09-03**: rozporządzenie o KFS (Dz.U. 2025 poz. 1641), ustawa o rynku pracy i służbach zatrudnienia (Dz.U. 2025 poz. 620) oraz ustawa o PARP (Dz.U. 2025 poz. 98) pobrane wprost z Dziennika Ustaw - sieć na maszynie foundera dopuszcza te domeny, wbrew pomiarowi z 2026-09-02 zrobionemu w środowisku w piaskownicy. Odczyt poprawił trzy błędy w `kfs.md` (warunek „co najmniej jeden pracownik”, krotności wiązane z priorytetem zamiast z zatrudnieniem, procenty podawane bez słowa „do”) i rozstrzygnął, że KFS nie narzuca treści zaświadczenia, tylko wymaga jego wzoru jako załącznika do wniosku. **Pozycje 7-8 zrealizowane 2026-09-03**: regulamin operatora PSF (WUP w Kielcach) pokazał brak akredytacji regionalnej, ale cztery obowiązki ponad wpis do BUR, w tym próg powiązań 10 % wobec 5 % w KFS; Podręcznik informacji i promocji FE rozstrzygnął, że IRIN jako doradca zewnętrzny nie ma prawa umieszczać znaku Funduszy Europejskich na własnych materiałach - weszło jako siódma zasada do `format-paczki.md`. **Zadanie zamknięte**; otwarte zostają dwie sprawy zależne od pierwszego klienta (regulamin jego urzędu pracy, regulamin operatora PSF spoza świętokrzyskiego), opisane w `weryfikacja-u-zrodla.md`, sekcja „Stan zbiorczy”.
21. Etap 3, karty warstwy 2: każde „do potwierdzenia przez foundera” zamienić na decyzję albo na status „otwarte do pierwszego użycia” z nazwą dokumentu → wszystkie pliki w `02-szablony-dokumentow/`. Zrealizowane 2026-09-02: zero znaczników, cztery pozycje otwarte do pierwszego zlecenia (viewbook: segmentacja i cykl; certyfikat: dwie wersje; karta usługi BUR: zapis dziedziny).
22. Etap 4, pilot: paczka i zlecenie gotowe w `03-pakiet-claude-design/zlecenia/pilot-papier-firmowy.md` (2026-09-02). **Zlecenie kompletne 2026-09-03**: wszystkie pięć pól wypełnionych - sąd rejestrowy i kapitał zakładowy z rejestru KRS, e-mail, adres strony i telefon od foundera. Kanwa pilota (artboardy `.dc.html` i `canvas.json`) przeniesiona z gałęzi `claude/project-roadmap-3cr739` do `/_robocze/pilot-papier-firmowy/`, uzupełniona i naprawiona 2026-09-03: komplet 18 diakrytyków w każdej z trzech wag (wcześniej tylko na wadze 400, co unieważniało główny falsyfikator typografii), sygnet na rewersie zmniejszony z 12 na 10 mm, stopień 12 px poza skalą zamieniony na 13,5 px. Adresy kanwy **sprawdzone w przeglądarce 2026-09-03**, co zamyka sprawę ciągnącą się przez trzy commity: publikacja z 2026-09-03 (`191cf137-…`) zwraca „Page not found" na profilu Personal, a kanwa z 2026-09-02 (`3c6ee053-…`) **działa** - otwiera się jako „Papier firmowy IRIN" z czterema artboardami. Jest jednak przedawniona: jej notatka mówi „Sygnet na rewersie ma 12 mm" i „Do uzupełnienia: kapitał zakładowy, telefon", czyli to wersja sprzed trzech poprawek z tego dnia. **Pomiarów nie robi się na żadnej z dwóch - kanwę zasiewa się od nowa z paczki**, a stara zostaje materiałem porównawczym. Szczegóły: `_robocze/pilot-papier-firmowy/README.md`. Zostaje przeprowadzenie zlecenia w Claude Design i wpisanie sześciu pomiarów do warstwy 1. **[FOUNDER]** przeprowadza przez Claude Design; potem Claude Code wpisuje wyniki protokołu pomiaru (polskie znaki na wagach 400-600, siatka 25 mm z treścią, H3 obok leadu, sygnet na rewersie, dokument bez koloru dziedzinowego, linie włosowe Popiołu i Złota foliowego na Muślinie - szósty pomiar dodany 2026-09-03; formularz: `_robocze/pilot-papier-firmowy/protokol-pomiaru.md`) → `01-baza-wiedzy/identyfikacja/`. Kontrast Karminu obok Aksamitu ten pilot nie sprawdzi; czeka na pierwszy dokument ze statusami.
23. Etap 5, zamknięcie: `PLAN.md` bez pozycji otwartych, `README.md` ze stanem „gotowe do użycia” i datą, tag `v1.0` na `main`.

## Decyzje foundera — rozstrzygnięte

- **Układ księgi marki - wariant 1 „Kaszmir uporządkowany” (2026-09-03)**: founder wybrał wariant 1 spośród trzech przygotowanych w `_robocze/brandbook-warianty/`. Oś wariacji to układ, rytm i nośnik hierarchii, nie kolor: wariant 1 prowadzi przepływ redakcyjny na pełnych sześciu kolumnach i **hierarchię niesie stopniem pisma** (pełna skala 72 → 10 px). Warianty 2 „Marginalia” (hierarchia przez położenie na siatce) i 3 „Tabliczka” (hierarchia przez powierzchnię, pasy odwrócone) zostają w `_robocze/` jako archiwum - nic nie kasujemy.

  **Decyzja jest wbrew rekomendacji notatki warsztatowej**, która wskazywała wariant 2, i to jest w porządku - ale koszt trzeba znać. Argument za wariantem 2 brzmiał: po konwersji do skali szarości Werdykt, Rubryka, Karmin i Onyks mają zbliżoną jasność, a tryb monochromatyczny został odrzucony (`palette-irin.json`, klucz `tryb-mono`), więc dokument budujący hierarchię położeniem czyta się tak samo w kolorze i w czerni. Wariant 1 buduje ją stopniem pisma, co w druku mono działa równie dobrze, natomiast ma inne ryzyko, wypisane w notatce: pełna skala 72 → 10 px robi dużo światła i przy realnej treści dokumentu regulowanego pierwsza sekcja potrafi zająć pół strony A4.

  **Pomiar, który tę wątpliwość rozstrzygnie:** złożyć w wariancie 1 jeden realny dokument z warstwy 2 (karta usługi BUR albo zaświadczenie KFS) i policzyć strony. Do tego czasu wybór stoi na kierunku, nie na objętości.

- **Paleta barw - wybór wariantu (2026-09-02, decyzja późniejsza)**: automatyczne przyjęcie palety z 2026-09-02 zostało wstrzymane jako wymagające dopracowania. Powstało siedem wariantów z pomiarem kontrastu (`_robocze/paleta-v2/palette-options-v2.md`); founder wybrał **wariant 2 „Kaszmir Wyciszony”** - 14 kolorów, z których 12 to przesunięcia kolorów już nazwanych, a dwa są nowe (Popiół jako `border`, Patyna jako `link`; obie nazwy zatwierdzone przez foundera 2026-09-02). Powód wyboru: usuwa trzy zmierzone defekty poprzedniej palety (link i błąd w tym samym kolorze, `info` nieodróżnialny od tekstu korpusu, obramowanie w pełnym tuszu), nie zmieniając kierunku „ciepły papier plus bordo”. Obowiązująca specyfikacja: `01-baza-wiedzy/identyfikacja/paleta-barw.md` (przeniesiona do warstwy 1 decyzją foundera 2026-09-02; `format-paczki.md` już jej nie duplikuje, tylko się do niej odwołuje). Siatka A4 i typografia bez zmian.
- **Siatka, typografia i logotyp przeniesione do warstwy 1 (2026-09-02)**: `identyfikacja/siatka-a4.md`, `identyfikacja/typografia.md` i `identyfikacja/logotyp.md`, obok palety. `03-pakiet-claude-design/format-paczki.md` nie powtarza już żadnej z trzech specyfikacji - odsyła do nich i dokłada osiem zasad użycia (siódma o kolorach na tle Pergaminu i ósma o zakazie znaku Funduszy Europejskich na materiałach IRIN, obie dopisane 2026-09-03), bez których same wartości są niekompletne. Zasady logotypu dołączyły tą samą drogą.
- **Jednostka bazowa 6 mm - rozstrzygnięta (2026-09-02)**: to jednostka odstępu między blokami, nie siatka linii bazowych tekstu. Pomiar: interlinia korpusu 5,54 mm nie jest wielokrotnością 6 mm, rozjazd 0,46 mm na linię i 19 mm na pełnej kolumnie, więc zmiana marginesu dolnego z 28 na 33 mm poprawiłaby wyłącznie dzielenie liczb, nie ustawiłaby ani jednej linii tekstu. Margines dolny zostaje 28 mm. Prawdziwa siatka linii bazowych wymagałaby interlinii około 1,68 zamiast 1,55, czyli zmiany typografii - nie wprowadzono. Szczegóły: `01-baza-wiedzy/identyfikacja/siatka-a4.md`.
- **Tryb monochromatyczny - odrzucony (2026-09-02)**: rozważany był wariant 6 „Druk Ekonomiczny” jako osobny tryb mono dla zaświadczeń KFS. Founder wybrał jedną paletę na wszystko. Skutek: obowiązkowa etykieta słowna albo ikona przy każdym statusie jest teraz jedynym zabezpieczeniem czytelności w druku mono.
- **Poziom H3 - zatwierdzony (2026-09-02)**: Manrope 600 / 16 px / interlinia 1,3, czyli stopień leadu z podniesioną wagą. Kanwa nie definiowała tego poziomu. Wpisany do `03-pakiet-claude-design/format-paczki.md` wraz z pełną skalą typograficzną.

- **Paleta barw i siatka A4 - pierwsza decyzja (2026-09-02, rano)**: kierunek z `brandbook.dc.html` zaakceptowany i dopracowany — siatka 6 kolumn / moduł 25 mm / gutter 4 mm (poprawka błędu wymiarów oryginału), paleta 12 kolorów z Miedzią pogłębioną do `#8C5026` i Karminem `#AC151F`. Siatka obowiązuje w tej postaci do dziś. Paleta 12-kolorowa została tego samego dnia zastąpiona 14-kolorowym wariantem 2 (pozycja pierwsza tej listy); zapis zostaje jako historia. Obowiązujące specyfikacje: `01-baza-wiedzy/identyfikacja/`.
- **Logotyp - komplet zasad zatwierdzony**: minimalny rozmiar (18 mm / 90 px) i przestrzeń ochronna (x = wysokość liter sygnetu) potwierdzone wcześniej; **cztery zakazy modyfikacji** - zmiany koloru, obracania i odbijania, cienia i obrysu, nieproporcjonalnego rozciągania - potwierdzone 2026-09-02, wcześniej były tylko odczytem z kanwy. Specyfikacja przeniesiona do `01-baza-wiedzy/identyfikacja/logotyp.md`. Nadal niepotwierdzone dwie drobne pozycje z kanwy, opisane tam wprost: minimalny rozmiar samodzielnego sygnetu (10 mm / 44 px) i reguła o kontraście znaku na akcentach dziedzinowych (4,5:1).
- **Aplikacje dla przedstawicieli handlowych**: narzędzie wewnętrzne IRIN — CRM/aplikacja dla własnych handlowców (lead-y, prowizje, raportowanie sprzedaży szkoleń i pożyczek), nie produkt na sprzedaż zewnętrzną.
- **Usługi pozyskiwania pożyczek UE/BGK**: pośrednictwo finansowania rozwojowego dla firm (B2B) — doradztwo i pośrednictwo w pozyskiwaniu dotacji UE i pożyczek BGK dla małych i średnich przedsiębiorstw.
- **Portal sprzedaży szkoleń online**: model hybrydowy — portal sprzedaje miejsca na szkolenia (w tym dofinansowane KFS/BUR) i pozwala je zrealizować zdalnie (webinary, materiały do pobrania), bez pełnej platformy LMS.

- **Dane rejestrowe i forma prawna (2026-09-02, wieczór)**: founder potwierdził, że dane z `01-baza-wiedzy/firma/kontekst-firmy-sanitized.md` (Instytut Rozwoju i Nauki sp. z o.o., siedziba w Kielcach, KRS, NIP, REGON) są poprawne i zostają w publicznym repozytorium. Dane kontaktowe (e-mail, telefon, adres strony) zostały wcześniej usunięte zasadą minimalizacji (PR #4). Sprzeczność między `kontekst-firmy.md` (brak danych) a wersją sanitized rozstrzygnięta na rzecz sanitized; napis „Warszawa” z kanwy nie obowiązuje. Wpisane do `kontekst-firmy.md` i `02-szablony-dokumentow/papier-firmowy.md`.
- **Wariant zamknięcia projektu: B (2026-09-02)**: repozytorium plus jeden dokument pilotażowy (papier firmowy i wizytówka) przeprowadzony przez Claude Design, żeby sprawdzić cztery falsyfikatory identyfikacji na realnym dokumencie. Etapy i bramki: `MAPA-DROGOWA.md`.
- **Konwencja papieru firmowego i wizytówki (2026-09-02)**: papier zawiera e-mail, telefon i adres strony; wizytówka 85 × 55 mm, awers i rewers. Obserwacja z kanwy przyjęta w całości jako konwencja IRIN. Wpisane do `02-szablony-dokumentow/papier-firmowy.md`; pilot (zadanie 22) nie ma już blokad decyzyjnych.
- **Porządek w PR-ach (2026-09-02)**: PR #4 scalony, PR #6 zamknięty jako zastąpiony przez PR #5, gałęzie `copilot/irin-brandbook-os` i `claude/irin-color-palette-variants-tjjnza` do usunięcia ręcznie w GitHubie.

## Decyzje do potwierdzenia przez foundera

- Żadna nie blokuje pilota. Sześć pozycji odłożonych do pierwszego użycia dokumentu, którego dotyczą (viewbook, certyfikat, struktura zespołu i historia, aplikacja sprzedażowa, portal, sygnet): tabela w `MAPA-DROGOWA.md`, grupa II.


---

# Plan wykonawczy: bramka B i zlecenie certyfikatu

> **Dopisane 2026-09-03.** Ta sekcja nie zastępuje niczego wyżej: kolejka zadań 1-23 i lista
> decyzji foundera zostają źródłem prawdy. Tu jest rozpisana na kroki wyłącznie praca, która
> została po weryfikacji stanu z 2026-09-03.
>
> **Sprzeczność, którą trzeba nazwać:** skill `metoda-plan-pracy` każe zapisać plan do
> `PLAN.md` projektu, a `PLAN.md` tego repozytorium jest już kolejką zadań i dziennikiem decyzji
> (`CLAUDE.md`: „Kolejka zadań pozostaje w PLAN.md"). Rozstrzygnięcie: plan **dopisany** jako
> osobna sekcja, nie nadpisujący pliku. Cofnięcie: usunięcie tej sekcji albo `git revert`
> commitu, który ją dodał.
>
> **Dla wykonującego:** jedno zadanie na raz, w kolejności. Skończ, zweryfikuj podaną komendą,
> zatrzymaj się na przegląd, potem następne. Kroki mają `- [ ]` do odhaczania.

**Cel:** domknąć bramkę B (wyniki pomiarów pilota wpisane do warstwy 1) i wydać komplet zlecenia
certyfikatu dla Claude Design, bez wypełniania wzoru zmyślonymi danymi.

**Podejście:** repozytorium trzyma treść i wytyczne, layout powstaje w Claude Design. Każde
zadanie kończy się komendą, której wynik da się przeczytać - w tym projekcie „gotowe" znaczy
„pomiar wykonany", nie „plik istnieje".

**Specyfikacja, z której ten plan argumentuje:** `CLAUDE.md`, `MAPA-DROGOWA.md` (bramka B),
`01-baza-wiedzy/identyfikacja/` (cztery specyfikacje), `02-szablony-dokumentow/certyfikat.md`,
`01-baza-wiedzy/prawo/{bur,kfs,pozyczki-ue-bgk}.md`, oraz protokół weryfikacji stanu
`_robocze/sesje/2026-09-03-weryfikacja-stanu-i-kanwa-pilota.md`.

## Ograniczenia obowiązujące w każdym zadaniu

- Każdy commitowany plik po polsku: nazwa, nagłówki, treść.
- Layout, kompozycja i grafika **wyłącznie** w Claude Design. Claude Code nie pisze artboardów.
- Kontrast liczy się od nowa wzorem WCAG 2.1 i podaje oba hexy obok wyniku. Nigdy nie przepisuje
  się liczby ze starego pliku.
- Kolor nigdy nie jest jedynym nośnikiem statusu: każdy stan ma etykietę słowną albo ikonę.
- Jeden kolor dziedziny na dokument: Aksamit `#452430`, Miedź `#7A5638` albo Onyks `#33474F`.
- Na materiale IRIN **nie stawia się** znaku Funduszy Europejskich, znaku barw RP ani flagi UE.
- We wzorze zaświadczenia zero zmyślonych danych: placeholdery w nawiasach kwadratowych.
- Formatu kodu BUR nie odtwarza się. `2025/00817/PPUR` z kanwy jest formatem niepotwierdzonym.
- Do projektu w Claude Design **nie idą**: `brandbook.dc.html` ani `program-szkolenia.md`.
- Nazwy w projekcie w Claude Design są inne niż w repozytorium: `format-paczki.md` występuje tam
  jako `guidelines/zasady-uzycia.md`, katalog `tokeny/` jako `tokens/`.
- `_ds_manifest.json` nie jest dowodem o zawartości projektu. Dowodem jest `get_file`.
- W tekście wyłącznie dywiz `-`, nigdy `\u2014` ani `\u2013`, także w zakresach liczb i dat.
- Na `origin` nie idzie nic bez pytania właściciela.

---

## Strumień A: bramka B, pilot papieru firmowego

**Kolejność zmieniona polecaniem właściciela 2026-09-03: „później będziemy mierzyć na końcu",
„na razie poprowadź zadania aby design skończył pracę".** Najpierw A0, czyli tura poprawek
w Claude Design. Pomiary A2, A3 i A4 idą po jej zamknięciu, nie przed. A1 i A6 zostają
niezależne od tej kolejności, bo nie potrzebują ani właściciela, ani projektanta.

Zależność: A1 i A6 są niezależne od właściciela. A2-A5 wymagają jego oczu albo decyzji.

### Zadanie A0: tura poprawek w Claude Design - PIERWSZA W KOLEJNOŚCI

**Pliki:**
- Utworzone 2026-09-03: `03-pakiet-claude-design/zlecenia/pilot-poprawki-do-wyslania.md`
- Zapis wyników: `_robocze/pilot-papier-firmowy/protokol-pomiaru.md`

**Co brief zamawia, trzy rzeczy do zrobienia i jedna do zaraportowania:**

1. **Stopka strony pierwszej, defekt twardy.** `grid-template-columns: 54mm 54mm 62mm` plus
   `column-gap: 4mm` daje 178 mm w pojemniku 170 mm; `overflow:hidden` obcina 8 mm, a razem z nimi
   NIP, REGON, telefon i adres strony, czyli treść prawnie obowiązkową z art. 206 KSH. Naprawa
   podana wprost: 54 + 4 + 54 + 4 + 54 = 170 mm, trzy bloki po dwie kolumny.
2. **Trzy bloki nie siadają prawą krawędzią na kolumnie:** logo 20 .. 72 mm (do 54 mm), blok
   adresata 20 .. 99 mm (do 83 mm), kolumna tekstu `max-width:150mm` (do 141 albo 112 mm, wybór
   projektanta z uzasadnieniem, bo to długość wiersza).
3. **Znak: zero nowego przebarwienia** do decyzji właściciela; jeżeli przebarwienie zostaje, kolor
   wprost hexem z palety, nie łańcuchem `filter:`, który daje `#3D1922` i `#F6F3EB`, czyli barwy
   spoza palety.
4. **Do zaraportowania, nie do naprawy:** 15 z 22 stopni pisma jest poza skalą, czyli 68 procent.
   Przy takim udziale wniosek nie brzmi „dokument łamie regułę", tylko „skala nie ma poziomów
   poniżej 7,5 pt", a stopka i wizytówka ich potrzebują. Projektant ma zwrócić listę stopni,
   których faktycznie potrzebuje - to wejście do decyzji właściciela o rozszerzeniu
   `typografia.md`. Jedna wartość idzie w górę niezależnie od tej decyzji: etykiety na awersie
   wizytówki mają 1,90 mm, czyli 5,39 pt, poniżej progu czytelności druku.

- [ ] **Krok 1:** właściciel otwiera kanwę w Claude Design i wkleja tekst między znacznikami
      POCZĄTEK i KONIEC z `03-pakiet-claude-design/zlecenia/pilot-poprawki-do-wyslania.md`.
      Załączniki są już w projekcie, nie wgrywa się ich ponownie.
- [ ] **Krok 2:** Claude Code odczytuje kanwę po poprawkach i weryfikuje trzy naprawy rachunkiem.

```
DesignSync get_file projectId=1a22ce64-0e1c-43a6-bd60-eef9241ef73b \
  path=templates/papier-firmowy-wizytowka/PapierFirmowyWizytowka.dc.html
```

Oczekiwane po poprawce: suma kolumn stopki równa 170 mm; brak `62mm` w `grid-template-columns`;
logo w 54 mm; blok adresata w 83 mm; kolumna tekstu w 141 albo 112 mm.

- [ ] **Krok 3:** wpisać do formularza pomiaru, co projektant zmienił i jakie wartości wziął,
      wraz z jego listą potrzebnych stopni pisma.
- [ ] **Krok 4:** zadać właścicielowi decyzję o rozszerzeniu skali typograficznej - z listą
      od projektanta, nie z moją propozycją.
- [ ] **Krok 5: commit**

```bash
git add _robocze/pilot-papier-firmowy/protokol-pomiaru.md
git commit -m "Tura poprawek pilota: stopka, przyleganie do kolumn, lista stopni pisma"
```

### Zadanie A1: pomiar 2 (siatka z realną treścią) - wykonalny bez właściciela

**Pliki:**
- Odczyt: projekt Claude Design `1a22ce64-0e1c-43a6-bd60-eef9241ef73b`,
  `templates/papier-firmowy-wizytowka/PapierFirmowyWizytowka.dc.html`
- Zapis wyniku: `_robocze/pilot-papier-firmowy/protokol-pomiaru.md`, wiersz 2
- Zapis do warstwy 1: `01-baza-wiedzy/identyfikacja/siatka-a4.md`, nowa sekcja „Pierwsze użycie"

**Co już zmierzono 2026-09-03 i wchodzi do wyniku:**

| Element kanwy | Zakres w mm | Przyleganie do kolumn |
|---|---|---|
| logo poziome, strona 1 | 20 .. 72 | lewa siada, prawa nie (kolumna 2 kończy się na 74) |
| blok adresata | 20 .. 99 | lewa siada, prawa nie (kolumna 3 kończy się na 103) |
| lead i korpus, `max-width:150mm` | 20 .. 170 | lewa siada, prawa nie (kolumna 5 kończy się na 161) |
| pas kickera i H3 | 20 .. 190 | siada obustronnie |
| przełącznik `.siatka` | `repeat(6,25mm)` + `4mm` = 170 mm | zgodne z polem treści |
| **stopka strony pierwszej** | **54 + 54 + 62 + 2 × 4 = 178 mm w pojemniku 170 mm** | **przekroczenie 8 mm, obcinane przez `overflow:hidden`** |

- [ ] **Krok 1: odtworzyć pomiar**

```bash
python3 - <<'EOF'
edges=[(k+1, 20+k*29, 20+k*29+25) for k in range(6)]
print("kolumny:", edges)
print("stopka:", 54+54+62+2*4, "mm w pojemniku", 210-40, "mm")
EOF
```

Oczekiwane: kolumny `20..45, 49..74, 78..103, 107..132, 136..161, 165..190`; stopka `178 mm`
w pojemniku `170 mm`.

- [ ] **Krok 2: potwierdzić, że wartości nadal stoją w kanwie**

```
DesignSync get_file projectId=1a22ce64-0e1c-43a6-bd60-eef9241ef73b \
  path=templates/papier-firmowy-wizytowka/PapierFirmowyWizytowka.dc.html
```

Oczekiwane: w treści występuje `grid-template-columns:54mm 54mm 62mm` oraz `column-gap:4mm`.
Jeżeli nie występuje - kanwa została poprawiona, pomiar trzeba zrobić od nowa na nowych wartościach.

- [ ] **Krok 3: wpisać wynik do formularza pomiaru**

W `_robocze/pilot-papier-firmowy/protokol-pomiaru.md`, wiersz 2, kolumna „Co zobaczyłem":
tabela z kroku wyżej, z dopiskiem „odczytane z plików projektu, nie z renderu".

- [ ] **Krok 4: zadać właścicielowi jedno pytanie, nie rozstrzygać samemu**

Przekroczenie stopki o 8 mm obcina trzecią kolumnę: NIP, REGON, telefon i adres strony. Dane
z art. 206 KSH są w `02-szablony-dokumentow/papier-firmowy.md` **prawnie obowiązkowe**, więc to
nie jest kosmetyka. Pytanie: poprawiamy dokument (stopka na 54 + 54 + 54 + 2 × 4 = 170 mm), czy
zmieniamy pojemnik. **Nie wpisuj tego do warstwy 1 przed odpowiedzią** - formularz pomiaru wprost
zakazuje przenoszenia rozbieżności automatycznie.

- [ ] **Krok 5: commit**

```bash
git add _robocze/pilot-papier-firmowy/protokol-pomiaru.md
git commit -m "Pomiar 2 pilota: siatka zmierzona na plikach kanwy, stopka o 8 mm za szeroka"
```

### Zadanie A2: pomiary 1, 3 i 5 - właściciel na żywej kanwie

**Pliki:**
- Zapis wyniku: `_robocze/pilot-papier-firmowy/protokol-pomiaru.md`, wiersze 1, 3, 5
- Zapis do warstwy 1: `01-baza-wiedzy/identyfikacja/typografia.md` (sekcje „Alfabet polski" i o H3),
  `01-baza-wiedzy/identyfikacja/paleta-barw.md` (sekcja o regule 80/15/5)

**Warunek wejścia:** kanwa otwarta w przeglądarce. Kroje są w projekcie osadzone jako data URI
(zmierzone 2026-09-03: `sha256` `f80139aec8d4a268`, cztery bloki `data:font/woff2`, zero `url(http`),
więc **nie trzeba nic przygotowywać**. Pomiarów nie robi się na PDF - eksport idzie przez drukarkę
Chromium i wyciąga metryki systemowe.

- [ ] **Krok 1: pomiar 1** - powiększyć na kanwie zdanie „Żółć, gęś, źdźbło, ćma, łódź, ńandu, świt,
      żółw: ĄĆĘŁŃÓŚŹŻ ąćęłńóśźż" w każdym z trzech miejsc: korpus (Manrope 400), lead (500) i H3 (600).
      Szukać brakujących ogonków, kresek i zamienników z innego kroju. Zapisać, czy komplet 18
      diakrytyków stoi w każdej z trzech wag.
- [ ] **Krok 2: pomiar 3** - obejrzeć H3 „Źródła finansowania, o które występuje pracodawca"
      stojący bezpośrednio pod leadem. Oba mają stopień 4,2 mm (16 px), różni je wyłącznie waga
      500 wobec 600. Zapisać: widać różnicę bez kickera czy nie.
- [ ] **Krok 3: pomiar 5** - obejrzeć całość i odpowiedzieć, czy papier w samym Aksamicie, bez
      koloru dziedziny, czyta się jako spójny z regułą 80/15/5. Projektant zapisał w uwadze nr 1,
      że warstwa 15 % została pusta celowo - to jego zapis, nie odpowiedź właściciela.
- [ ] **Krok 4: Claude Code wpisuje trzy wyniki do formularza, z datą**
- [ ] **Krok 5: Claude Code przenosi wyniki do dwóch plików warstwy 1**

Weryfikacja: `grep -n "pokrycie potwierdzone w zakresie, w jakim je zmierzono" 01-baza-wiedzy/identyfikacja/typografia.md`
Oczekiwane po zadaniu: **zero trafień** - zdanie zastąpione wynikiem z datą.

- [ ] **Krok 6: commit**

```bash
git add _robocze/pilot-papier-firmowy/protokol-pomiaru.md 01-baza-wiedzy/identyfikacja/typografia.md 01-baza-wiedzy/identyfikacja/paleta-barw.md
git commit -m "Pomiary 1, 3 i 5 pilota wpisane do warstwy 1"
```

### Zadanie A3: pomiar 6 - wydruk na zwykłej drukarce

**Pliki:** `_robocze/pilot-papier-firmowy/protokol-pomiaru.md` wiersz 6,
potem `01-baza-wiedzy/identyfikacja/paleta-barw.md`, sekcja „Minimalna grubość linii".

- [ ] **Krok 1:** wyeksportować PDF w skali 1:1 i wydrukować stronę pierwszą oraz wizytówkę.
      Kroje na wydruku będą zastępcze i to nie przeszkadza - ten pomiar dotyczy grubości linii,
      nie liter.
- [ ] **Krok 2:** obejrzeć linię struktury 0,25 mm w Popiele `#7D7466` (linia stopki, dwie sztuki)
      i kreskę 0,5 mm w Złocie foliowym `#A8874E` (sygnatura na stronie pierwszej, kreska na
      awersie wizytówki). Zapisać: widoczne czy nie, i na jakim tle.
- [ ] **Krok 3:** wpisać wynik. Widoczne - obie wartości potwierdzone. Niewidoczne - wpisać
      zmierzone minimum, a nie „trzeba pogrubić".
- [ ] **Krok 4: commit**

```bash
git add _robocze/pilot-papier-firmowy/protokol-pomiaru.md 01-baza-wiedzy/identyfikacja/paleta-barw.md
git commit -m "Pomiar 6 pilota: minimalne grubosci linii sprawdzone na wydruku"
```

### Zadanie A4: pomiar 4 - decyzja właściciela, gdzie się przenosi

**Pliki:** `_robocze/pilot-papier-firmowy/protokol-pomiaru.md`, sekcja „Pomiar 4 stracił nośnik";
potem `01-baza-wiedzy/identyfikacja/logotyp.md` albo `MAPA-DROGOWA.md`, zależnie od wyjścia.

Trzy wyjścia są wypisane w formularzu. Zadanie polega na zadaniu pytania i wpisaniu odpowiedzi,
**nie** na wybraniu wyjścia za właściciela.

- [ ] **Krok 1:** zadać pytanie ankietą, z rekomendacją i jej uzasadnieniem.
- [ ] **Krok 2:** wpisać decyzję do `PLAN.md`, sekcja „Decyzje foundera - rozstrzygnięte".
- [ ] **Krok 3:** jeżeli wyjście 2 (przeniesienie na inny dokument) - poprawić `MAPA-DROGOWA.md`,
      wiersz etapu 4, tak jak zrobiono z falsyfikatorem „Karmin obok Aksamitu".
- [ ] **Krok 4: commit**

### Zadanie A5: zamknięcie bramki B

**Warunek wejścia:** A1-A4 zamknięte, każdy pomiar ma wpisany wynik albo jawnie przeniesiony nośnik.

**Pliki:**
- Modyfikacja: `MAPA-DROGOWA.md` (wiersz etapu 4 w tabeli bramek, plus diagram)
- Modyfikacja: `PLAN.md`, zadanie 22

- [ ] **Krok 1:** wpisać do `MAPA-DROGOWA.md`, że bramka B jest spełniona, z listą pomiarów
      i datą każdego.
- [ ] **Krok 2:** zamknąć zadanie 22 w `PLAN.md`.
- [ ] **Krok 3: weryfikacja**

```bash
grep -c "Etap czeka wyłącznie na przeprowadzenie pilota" MAPA-DROGOWA.md
```

Oczekiwane: `0`.

- [ ] **Krok 4: commit**

### Zadanie A6: higiena po weryfikacji z 2026-09-03

Trzy pliki twierdzą rzeczy, które pomiar obalił. Zadanie jest niezależne od właściciela.

**Pliki:**
- Modyfikacja: `_robocze/pilot-papier-firmowy/README.md` - zdanie „pomiar 4 dotyczyłby sygnetu
  12 mm, choć sporną wartością jest 10 mm" i „kanwę zasiewa się od nowa z paczki"
- Modyfikacja: `MAPA-DROGOWA.md`, wiersz etapu 4 - „Pomiarów nie robi się na żadnej z nich"
- Modyfikacja: `PLAN.md`, zadanie 22 - „sygnet na rewersie zmniejszony z 12 na 10 mm"

Wszystkie trzy powstały, gdy nie było wiadomo, że w projekcie w Claude Design leży gotowa kanwa
z 22 mm z polecenia właściciela.

- [ ] **Krok 1:** w każdym z trzech plików zastąpić nieaktualne zdanie wynikiem pomiaru, z odsyłaczem
      do `_robocze/sesje/2026-09-03-weryfikacja-stanu-i-kanwa-pilota.md`.
- [ ] **Krok 2:** dopisać do `_robocze/pilot-papier-firmowy/README.md` trzeci adres: projekt
      design-system `1a22ce64-0e1c-43a6-bd60-eef9241ef73b`, w nim
      `templates/papier-firmowy-wizytowka/PapierFirmowyWizytowka.dc.html` - **to jest kanwa,
      na której się mierzy**.
- [ ] **Krok 3: weryfikacja**

```bash
grep -rn "kanwę zasiewa się od nowa\|Pomiarów nie robi się na żadnej" MAPA-DROGOWA.md PLAN.md _robocze/pilot-papier-firmowy/README.md
```

Oczekiwane: `0` trafień.

- [ ] **Krok 4: commit**

---

## Strumień S: zestaw szablonów uniwersalnych - PRIORYTET WŁAŚCICIELA

**Wprowadzony polecaniem z 2026-09-03:** „narazie potrzebuję lekkich szablonów uniwersalnych,
żeby dało się je przygotować jako wzorce dla różnego rodzaju pierdoletów", „merytoryką będziemy
się martwić później", „niech już wszystko robi". Ten strumień **wyprzedza strumień B**: zamiast
zlecać sześć konkretnych dokumentów, zamawiamy osiem układów z miejscami na treść, a merytoryka
wchodzi w kolejnych turach.

### Zadanie S1: brief ośmiu szablonów - ZROBIONE 2026-09-03

**Plik:** `03-pakiet-claude-design/zlecenia/szablony-uniwersalne-do-wyslania.md`

Osiem artboardów: karta jednostronicowa, dokument z pieczęcią w dwóch odmianach, tabela danych
regulowanych, okładka, rozkładówka katalogowa, slajd 16:9 w trzech odmianach (jako **propozycja**
siatki, bo `siatka-a4.md` obowiązuje wyłącznie na A4 pion), notatka wewnętrzna, zestaw drobnych.
Wszystko na placeholderach, zero zmyślonych danych.

Inaczej niż zlecenie pilota ten plik **nie ma osobnej wersji projektowej** - nie zamawia treści
merytorycznej, więc nie ma czego trzymać w dwóch wersjach. Notatka dla właściciela ze ścieżkami
stoi w części A, przed znacznikiem POCZĄTEK; tekst do wklejenia jest za znacznikiem i ścieżek
nie ma (sprawdzone `grep` po czterech prefiksach katalogów: zero trafień).

- [x] Brief napisany i sprawdzony pod kątem ścieżek lokalnych oraz nazw z projektu.
- [ ] **Krok 2:** właściciel wkleja tekst między znacznikami do Claude Design.
- [ ] **Krok 3:** Claude Code odczytuje kanwę i weryfikuje rachunkiem przyleganie bloków do kolumn
      (szerokości 25, 54, 83, 112, 141, 170 mm; krawędzie prawe 45, 74, 103, 132, 161, 190 mm).
- [ ] **Krok 4:** wpisać trzy rzeczy zwrócone przez projektanta: listę stopni poniżej 7,5 pt,
      propozycję siatki slajdu 16:9, listę kandydatów na prymitywy.
- [ ] **Krok 5:** zadać właścicielowi dwie decyzje, które z tego wynikają: rozszerzenie skali
      typograficznej i zatwierdzenie siatki slajdu jako piątej specyfikacji identyfikacji.

### Zadanie S3: tury 2 i 3 briefu - lista rozszerzona 2026-09-03

**Plik:** ten sam, `03-pakiet-claude-design/zlecenia/szablony-uniwersalne-do-wyslania.md`,
rozszerzony o trzy bloki do wklejenia zamiast jednego. Powód podziału, do obalenia: jedna
wiadomość zamawiająca około sześćdziesięciu artboardów da sześćdziesiąt płytkich.

| Tura | Pozycje | Co zamawia |
|---|---|---|
| 1 | 1-8 | osiem szablonów dokumentów A4 |
| 2 | 9-12 | pakiet znaku, wersje kolorystyczne i favicon jako propozycja, cztery wizytówki, sześć formatów social media w pięciu typach treści |
| 3 | 13-16 | prezentacja w 24 wariantach slajdu, arkusz wzorcowy, wykresy plus zlecenie badawcze na paletę serii, pięć pozycji dołożonych z propozycji Claude Code |

- [x] Brief rozszerzony, trzy bloki sprawdzone pod kątem ścieżek lokalnych: zero trafień w każdym.
- [ ] **Krok 2:** właściciel wkleja turę 2, potem turę 3.
- [ ] **Krok 3:** Claude Code weryfikuje rachunkiem to, co da się policzyć z plików projektu.
- [ ] **Krok 4:** wpisać cztery rzeczy zwrócone przez projektanta: propozycje siatek dla trzech
      formatów bez zatwierdzonej siatki (slajd 16:9, kadry social media, wizytówka), propozycję
      palety serii, zmierzoną szerokość powiększonego sygnetu, obserwację o sygnecie poniżej 44 px.

### Zadanie S4: paleta serii do wykresów - zlecenie badawcze

**Właściciel poprosił, żeby spróbował Claude Design** („może Claude Design będzie potrafił, zleć
mu"), po tym jak pomiar pokazał, że z obecnych czternastu kolorów palety serii zbudować nie można.

Zmierzone walidatorem palet kategorialnych, tło Kaszmir `#FBF8F2`: trzy warianty, wszystkie FAIL.
Przyczyna jedna i nie do obejścia doborem - nasycenie każdego koloru IRIN leży między **0,016
a 0,085** w OKLCH przy podłodze **0,10**, a najciemniejsze mają jasność **0,226 - 0,406** przy
dolnej granicy pasma **0,43**. Kaszmir Wyciszony jest celowo odsycony, więc barwy czytają się
w wykresie jako szarości.

Progi przyjęcia wpisane do briefu, żeby propozycja była policzalna, nie estetyczna: jasność
0,43 - 0,77; nasycenie co najmniej 0,10; odróżnialność sąsiadów w wadach widzenia barw ΔE cel 8
i podłoga 6 tylko przy drugim nośniku tożsamości; odróżnialność w widzeniu prawidłowym ΔE co
najmniej 15; kontrast wobec tła co najmniej 3:1. Plus trzy ograniczenia z tożsamości IRIN:
kolejność stała i nigdy zapętlana, maksimum osiem pozycji, zakaz użycia trzech kolorów dziedziny
i trzech kolorów statusu.

- [ ] **Krok 1:** odebrać propozycję z hexami, jasnością, nasyceniem i kontrastem przy każdej pozycji.
- [ ] **Krok 2: weryfikacja tym samym walidatorem**, nie oceną wzrokową.

```
node scripts/validate_palette.js "<hexy z propozycji>" --mode light --surface "#FBF8F2"
```

Oczekiwane: `PASSED`. Każdy `FAIL` wraca do projektanta z nazwą sprawdzenia, nie z komentarzem
o gustach.

- [ ] **Krok 3:** przedstawić właścicielowi decyzję: czy identyfikacja dostaje **piątą
      specyfikację** - osobny zestaw odcieni wyłącznie do wykresów. Bez niej kolorowych pulpitów
      nie da się zrobić poprawnie, a wykresy zostają na sekwencji jednego odcienia, małych
      wielokrotnościach i fakturze.
- [ ] **Krok 4:** jeżeli tak - nowy plik `01-baza-wiedzy/identyfikacja/paleta-wykresow.md`
      z falsyfikatorem: ponowne uruchomienie walidatora dające inny wynik.

### Zadanie S5: trzy pliki, które nie powstają w Claude Design

Wszystkie trzy z listy właściciela z 2026-09-03. Szczegóły i uzasadnienie: część C briefu.

| Plik | Warunek wejścia | Uwaga |
|---|---|---|
| Arkusz `.xlsx` z tabelą, pasami wierszy i wykresami | pozycje 14 i 15 zamknięte na kanwie | **zrobione 2026-09-09**: `_robocze/arkusz-wzorcowy/`. Stare 1,054:1 i 1,247:1 dotyczyły Kaszmiru, Muślinu i Pergaminu, czyli barw wycofanych z paletą „Kaszmir Wyciszony" - przeliczone. Para pasów stoi na rekomendacji, nie na decyzji: patrz akapit pod listą |
| Szablon `.docx` do pisania pism | tura 1 zamknięta | **zrobione 2026-09-08**: `_robocze/pismo-firmowe/` - szablon, generator, symulacja układu i README z pomiarami |
| Podpis e-mail w HTML | tura 1 zamknięta | **zrobione 2026-09-08**: `_robocze/podpis-mailowy/` |

- [x] **Krok 1:** `.docx` i podpis e-mail - zrobione. Oba leżą w `_robocze/`, bo repozytorium
      nie ma warstwy gotowych plików; rekomendacja czwartej warstwy `04-materialy/` czeka na
      decyzję właściciela i nic nie jest przenoszone przed nią.
- [x] **Krok 2:** `.xlsx` zrobiony 2026-09-09, `_robocze/arkusz-wzorcowy/`. Barw wykresu **nie
      dobierano z palety na oko**: generator czyta stopnie z `tokeny/palette-irin.json`, a reguła
      „jedna barwa, cztery stopnie krycia" była już w `paleta-barw.md`. Przy tej okazji wyszło,
      że sama reguła nie wystarcza - stopień 30 % ma do tła 1,87:1 przy progu 3:1 z WCAG 1.4.11,
      a Bursztyn Wyciszony traci trzy stopnie z czterech. Domknięte obrysem Atramentem 0,25 mm
      i wyjątkiem dla wykresu liniowego (trzy serie). Pomiar w `paleta-barw.md`.
      **Otwarte:** para pasów wierszy stoi na rekomendacji, nie na decyzji - akapit pod listą.
- [x] **Krok 3: weryfikacja** dla `.docx` i podpisu e-mail - wykonana w granicach kontenera
      i jawnie ograniczona. Czego **nie** dało się zrobić: w tym kontenerze LibreOffice nie ma
      modułu Writer, a `pdftoppm` nie jest zainstalowany, więc `.docx` nie został otwarty
      w żadnym edytorze. Zamiast tego: odczyt geometrii wprost z OOXML plus symulacja układu
      w Chromium na prawdziwym Manrope. Pełna lista pomiarów i falsyfikatorów:
      `_robocze/pismo-firmowe/README.md`. **Dla `.xlsx` to samo ograniczenie i ta sama droga:**
      LibreOffice w tym kontenerze nie ma również modułu Calc, więc arkusz sprawdzono odczytem
      OOXML i odczytem zwrotnym przez openpyxl - formuły, barwy z kanałem alfa, `strRef`
      na kategoriach osi, `min val="0"`, obrys 9000 EMU, marginesy 20/20/18/28 mm i zero komórek
      bez polskich znaków. Lista w `_robocze/arkusz-wzorcowy/README.md`.

**Para pasów wierszy w Regalii - decyzja właściciela, jedna z dwóch.** Jasny koniec palety ma
trzy poziomy: Kość Słoniowa `#F7F3E9` (L* 95,90), Alabaster `#E4E1D8` (L* 89,53) i cztery tinty
12 % (L* około 87). Między 95,90 a 89,53 nie ma nic, więc nie da się mieć jednocześnie cichego
pasa i tekstu drugorzędnego w Grafcie Jedwabnym:

| Para | Kontrast pasów | ΔL* | Atrament | Grafit Jedwabny | Koszt |
|---|---|---|---|---|---|
| **Kość Słoniowa + Alabaster** (rekomendacja) | 1,180:1 | 6,36 | 15,25:1 | **4,61:1, AA trzymane** | pas jest wyraźny, czyta się jak jasnoszary blok, nie jak muśnięcie |
| Alabaster + Szafir 12 % | 1,068:1 | 2,46 | 14,27:1 | **4,31:1, AA złamane** | tekst drugorzędny musi zejść z Grafitu na Atrament albo Lapis Stonowany; tint przestaje być wolny dla kart dziedzinowych |

Rekomendacja: **Kość Słoniowa + Alabaster**, bo dostępność jest wymogiem, a cichość pasa
preferencją. Poprzednia sesja wybrała odwrotnie (para o ΔL* 2,08) - wybierała jednak wyłącznie
na oko odstępu pasów i nie liczyła tekstu na ciemniejszym pasie. Falsyfikator rekomendacji:
wydruk na drukarce biurowej, na którym ΔL* 6,36 wychodzi jako ciężka szara wstęga zamiast pasa;
wtedy wraca para cicha, a razem z nią zakaz Grafitu w wierszach.

Pomiar wszystkich sześciu barw tekstu na wszystkich jasnych tłach:
`01-baza-wiedzy/identyfikacja/paleta-barw.md`, sekcja „Jasne tła nie są wymienne".

### Zadanie S6: sprzeczność pozycji 1 z zakazem 1 - do rozstrzygnięcia przez właściciela

**Polecenie:** „pakiet logo do użycia i faviconów w różnych kolorach".
**Zakaz 1 z `01-baza-wiedzy/identyfikacja/logotyp.md`**, zatwierdzony przez właściciela
2026-09-02: znaku się nie przebarwia; na ciemnym tle wchodzi wersja odwrócona, nie przebarwiona.

Druga strona, niezależna od koloru: **favicon w 16 i 32 px stoi poniżej minimum 44 px** dla
samodzielnego sygnetu. Favicon nie mieści się w obowiązującej specyfikacji przy żadnej barwie.

Brief rozstrzyga to tak, że pakiet dopuszczony idzie jako zlecenie (pozycja 9), a wersje
kolorystyczne i favicon jako osobny artboard oznaczony jako propozycja, z policzonym kontrastem
każdej pary (pozycja 10). Liczby dla decyzji, przeliczone wzorem WCAG 2.1:

| Znak w kolorze | na Aksamicie | na Miedzi | na Onyksie | Próg 3:1 |
|---|---|---|---|---|
| Espresso `#221A15`, kolor źródłowy | **1,26:1** | **2,62:1** | **1,76:1** | zawodzi wszędzie |
| Kaszmir `#FBF8F2`, wersja odwrócona | 12,80:1 | 6,16:1 | 9,19:1 | przechodzi wszędzie |

Wniosek obowiązujący **niezależnie od decyzji o kolorach**: na każdym z trzech kolorów dziedziny
wchodzi wersja odwrócona znaku, nie źródłowa. To dotyczy wprost kolorowych wizytówek z pozycji 11.

- [ ] **Krok 1:** zadać właścicielowi dwie decyzje osobno: czy zakaz 1 zostaje, i czy favicon
      dostaje uproszczony znak jako utwór pochodny.
- [ ] **Krok 2:** wpisać rozstrzygnięcie do `PLAN.md` i do `logotyp.md`, wraz z datą.

### Zadanie S2: dwie luki w palecie, wykryte pomiarem

Obie policzone w tej sesji wzorem WCAG 2.1 i **już wpisane do briefu S1 jako zakazy**, bo bez nich
plakietka i pieczęć wyszłyby nieczytelne. Do decyzji właściciela, czy wchodzą do warstwy 1.

| Luka | Zmierzone | Czego `paleta-barw.md` nie mówi |
|---|---|---|
| Plakietka statusu na wypełnieniu koloru dziedziny | Karmin na Aksamicie 1,83:1, na Miedzi 1,13:1, na Onyksie 1,32:1 - wszystkie poniżej progu 3:1 | Plik nie zakazuje tego zestawienia w ogóle |
| Złoto foliowe zawodzi nie tylko na Pergaminie | na Miedzi 1,94:1, na Onyksie 2,90:1, przy progu 3:1; przechodzi na Aksamicie 4,03:1 i Kaszmirze 3,17:1 | Plik zakazuje mu wyłącznie tła Pergaminu (2,55:1) |

Skutek praktyczny drugiej luki: **pieczęć w Złocie foliowym nie działa w dokumencie dziedziny
Akademia AI ani Pożyczki UE/BGK.** To nie jest kosmetyka - pieczęć jest w `paleta-barw.md` jedną
z trzech dopuszczonych rol tego koloru.

- [ ] **Krok 1:** zadać właścicielowi decyzję: dopisujemy oba zakazy do `paleta-barw.md`
      czy zostają wyłącznie w zleceniach.
- [ ] **Krok 2:** jeżeli tak - dopisać do `01-baza-wiedzy/identyfikacja/paleta-barw.md`, sekcja
      „Dwie pary nadal pod progiem", i przeliczyć tabelę od nowa, nie kopiować tych liczb.
- [ ] **Krok 3: weryfikacja**

```bash
grep -c "1,13:1\|1,94:1" 01-baza-wiedzy/identyfikacja/paleta-barw.md
```

Oczekiwane po kroku 2: co najmniej `2`.

---

## Strumień B: zlecenie certyfikatu i zaświadczenia

Zależność: B1 nie ruszy bez B0. B0 to pytania, nie praca.

### Zadanie B0: pięć decyzji właściciela

Każda zmienia treść zlecenia, więc żadnej nie zgaduję. Pytane ankietą, po dwie albo trzy na raz,
z rekomendacją przy każdej.

- [ ] **Krok 1: orientacja strony.** A4 pion (siatka zatwierdzona, zero pracy) czy A4 poziom.
      Rekomendacja: **pion**. Uzasadnienie do obalenia: `siatka-a4.md` obowiązuje wyłącznie na
      pionie i sama mówi, że inna orientacja unieważnia całe sprawdzenie, a zaświadczenie jest
      w `02-szablony-dokumentow/certyfikat.md` opisane jako dowód rozliczeniowy wobec PUP i BUR,
      nie pamiątkowy dyplom - trafia do teczki obok dokumentów pionowych. Falsyfikator: jeżeli
      klienci albo operatorzy oczekują poziomego dyplomu, konwencja rynku wygrywa z wygodą siatki.
      Koszt poziomu, policzony: nowa para moduł/gutter (6 × 37 + 5 × 7 = 257 mm przy marginesach
      20 mm), rytm pionowy 27 jednostek plus 2 mm reszty zamiast 41 plus 5 mm, i **nowa
      specyfikacja do zatwierdzenia**, czyli piąta obok czterech istniejących.
- [ ] **Krok 2: dziedzina, czyli kolor warstwy 15 %.** Rekomendacja: **Aksamit (Pedagogika)**.
      Uzasadnienie: tylko wtedy na tym dokumencie zadziała falsyfikator „Karmin obok Aksamitu",
      który mapa drogowa przeniosła z pilota na pierwszy dokument ze statusami. Jeden kolor
      dziedziny na dokument, nigdy dwa.
- [ ] **Krok 3: osoba podpisująca.** Jedna sygnatura czy dwie. Imion z `brandbook.dc.html`
      użyć nie wolno - są zmyślone.
- [ ] **Krok 4: numeracja zaświadczeń.** Czy `IRIN/RRRR/D/NNNNN` z kanwy jest realną konwencją
      firmy. Jeżeli nie, we wzorze zostaje placeholder `[NUMER ZAŚWIADCZENIA]`.
- [ ] **Krok 5: PESEL.** Czy w ogóle na dokumencie i w jakim maskowaniu. Powód, dla którego to
      nie jest decyzja projektanta: zaświadczenie krąży jako skan między pracodawcą, urzędem pracy
      i operatorem, a `bur.md` wymaga „danych usługobiorcy" bez wskazania, że to musi być PESEL.
- [ ] **Krok 6:** wpisać pięć decyzji do `PLAN.md`, sekcja „Decyzje foundera - rozstrzygnięte",
      i zdjąć wiersz „Czy certyfikat ma dwie wersje wdrożeniowe" z `MAPA-DROGOWA.md`, grupa II.

### Zadanie B1: zlecenie certyfikatu, wersja projektowa

**Pliki:**
- Utworzenie: `03-pakiet-claude-design/zlecenia/certyfikat-zaswiadczenie.md`
- Wzór formy: `03-pakiet-claude-design/zlecenia/pilot-papier-firmowy.md` (cztery sekcje: skład
  paczki, treść sekcji „Zlecenie", protokół pomiaru, co blokuje wysłanie)

**Interfejsy:**
- Konsumuje: pięć decyzji z B0; listę ośmiu elementów zaświadczenia z
  `01-baza-wiedzy/prawo/bur.md`, sekcja „Zaświadczenie"; dwa wymogi KFS z
  `01-baza-wiedzy/prawo/kfs.md`, sekcja „Dokumentacja ukończenia szkolenia".
- Produkuje: listę plików paczki, której B2 i B4 muszą się trzymać co do nazw.

**Treść obowiązkowa zlecenia, wypisana, żeby nie było „uzupełnij":**

1. **Dwie wersje wdrożeniowe jako artboardy do porównania**, w tej samej dziedzinie i z tą samą
   treścią: kolumnowa i z pieczęcią (panel metryk jako blok kontrastowy). W zleceniu napisane
   wprost: **nie wybieraj wersji i nie sugeruj, która lepsza.** Powód: karta specyfikacji nie prosi
   o wybór, tylko o **regułę doboru wg kanału dystrybucji**, a reguła zakłada, że obie istnieją.
   Kryterium jest pomiarem, nie gustem: czy numer zaświadczenia i kod usługi zostają czytelne
   po kopii czarno-białej.
2. **Osiem elementów treści z Załącznika 4 do Regulaminu BUR**, Rozdział 2 pkt 3: tytuł usługi,
   numer identyfikacyjny usługi, data świadczenia, liczba godzin, informacja o nabytych efektach
   uczenia się, dane usługobiorcy, ID wsparcia, kod kwalifikacji z ZRK (tylko jeżeli nabyta).
   Wszystkie jako placeholdery w nawiasach kwadratowych.
3. **Dwa wymogi z KFS:** wzór dokumentu musi istnieć przed złożeniem wniosku (rozporządzenie
   o KFS, § 2 ust. 2 pkt 3), a wystawiony dokument wskazuje **tematykę kształcenia**
   (§ 6 ust. 3 pkt 5 lit. c). KFS nie narzuca ani pól, ani układu.
4. **Plakietka KOREKTA w Karminie `#9E2B2B`** jako stan błędu - jedyny legalny nośnik tego koloru
   na tym dokumencie. Podstawa nie jest wymysłem: Załącznik 4 nakłada obowiązek wydania korekty
   zaświadczenia w ciągu 7 dni od uzasadnionego wezwania usługobiorcy. Obok koloru obowiązkowa
   etykieta słowna - kolor nigdy nie jest jedynym nośnikiem statusu.
5. **Zakaz, który trzeba napisać wprost:** plakietka Karmin nie stoi na wypełnieniu Aksamitu ani
   Aksamit na Karminie. Kontrast przeliczony 2026-09-03 wzorem WCAG 2.1: `#9E2B2B` wobec `#452430`
   daje **1,83:1**. Dopuszczone: Karmin na papierze Kaszmir `#FBF8F2` (6,99:1), Pergamin
   `#E7DFD2` jako napis na wypełnieniu Karminu (5,60:1). Zakazane dodatkowo: Karmin na Espresso
   `#221A15` (2,31:1).
6. **Kodu usługi BUR nie odtwarzać.** Struktura numeru nie jest zdefiniowana w żadnym z sześciu
   przejrzanych dokumentów PARP. Na wzorze stoi `[NUMER IDENTYFIKACYJNY USŁUGI Z BUR]`.
7. **Zakaz znaków:** bez znaku Funduszy Europejskich, znaku barw RP i flagi UE. Podstawa:
   Podręcznik informacji i promocji FE, rozdz. 2 (s. 7) i 8.7 (s. 22). IRIN jest doradcą
   zewnętrznym, nie beneficjentem - to zakaz, nie brak obowiązku.
8. **Logotyp bez zmiany koloru**, dopóki decyzja o przebarwianiu filtrem jest odłożona. Na ciemnym
   tle wersja odwrócona, nie przebarwiona. Jeżeli projektant potrzebuje znaku w kolorze dziedziny,
   ma to **zapisać jako pytanie**, nie zrobić po cichu i nie łańcuchem `filter:` - ten na kanwie
   pilota daje `#3D1922`, czyli nie trafia w żaden kolor palety.
9. **Zdanie testowe z diakrytykami** do zachowania w każdej użytej wadze, jak w pilocie.
10. **Format wyniku:** żywa kanwa z przełącznikiem siatki nad każdym artboardem, potem PDF 1:1.
    Kolejność ma znaczenie - eksport nie osadza krojów.

- [ ] **Krok 1:** napisać plik według czterech sekcji wzoru pilota.
- [ ] **Krok 2: weryfikacja kompletności**

```bash
python3 - <<'EOF'
import re
s = open('03-pakiet-claude-design/zlecenia/certyfikat-zaswiadczenie.md', encoding='utf-8').read()
wymagane = ["1,83:1", "#9E2B2B", "#452430", "KOREKTA", "Załącznika 4", "§ 2 ust. 2 pkt 3",
            "§ 6 ust. 3 pkt 5", "nie wybieraj wersji", "Funduszy Europejskich",
            "NUMER IDENTYFIKACYJNY USŁUGI"]
brak = [w for w in wymagane if w not in s]
print("brakuje:", brak if brak else "nic")
print("mysliniki:", len(re.findall(r"[\u2014\u2013]", s)))
EOF
```

Oczekiwane: `brakuje: nic`, `mysliniki: 0`.

- [ ] **Krok 3: commit**

### Zadanie B2: przekład na wersję do wysłania

**Pliki:**
- Utworzenie: `03-pakiet-claude-design/zlecenia/certyfikat-zaswiadczenie-do-wyslania.md`
- Wzór: `03-pakiet-claude-design/zlecenia/pilot-papier-firmowy-do-wyslania.md`

Powód istnienia tego pliku: Claude Design nie widzi dysku, więc każda ścieżka lokalna jest tam
martwym adresem, który może zostać wzięty za zadanie do wykonania. Źródłem prawdy zostaje B1.

- [ ] **Krok 1:** przełożyć B1 na jeden ciągły tekst między znacznikami POCZĄTEK i KONIEC,
      bez ani jednej ścieżki lokalnej. Nazwy plików w paczce **w wersji z projektu Claude Design**:
      `zasady-uzycia.md` zamiast `format-paczki.md`, `tokens/palette-irin.json` zamiast `tokeny/`.
- [ ] **Krok 2: weryfikacja braku ścieżek lokalnych**

```bash
sed -n '/POCZĄTEK TEKSTU/,/KONIEC TEKSTU/p' 03-pakiet-claude-design/zlecenia/certyfikat-zaswiadczenie-do-wyslania.md | grep -n "01-baza-wiedzy/\|02-szablony-dokumentow/\|03-pakiet-claude-design/\|_robocze/\|format-paczki"
```

Oczekiwane: zero trafień.

- [ ] **Krok 3: commit**

### Zadanie B3: formularz pomiaru certyfikatu

**Pliki:** utworzenie `_robocze/certyfikat/protokol-pomiaru.md`, wzór:
`_robocze/pilot-papier-firmowy/protokol-pomiaru.md`.

**Pomiary, które ten dokument ma zamknąć** - każdy z nazwanym plikiem docelowym:

| Nr | Co sprawdzić | Gdzie ląduje wynik |
|---|---|---|
| 1 | **Karmin obok Aksamitu na realnym dokumencie** - falsyfikator przeniesiony z pilota. Czy plakietka KOREKTA jest odróżnialna od koloru dziedziny na papierze i po kopii mono | `paleta-barw.md`, sekcja o Karminie |
| 2 | Czy numer zaświadczenia i numer usługi BUR zostają czytelne **po kopii czarno-białej** w obu wersjach wdrożeniowych | `02-szablony-dokumentow/certyfikat.md`, sekcja „Konwencja organizacyjna IRIN" - to jest ta reguła doboru wersji |
| 3 | Czy osiem elementów z Załącznika 4 zmieściło się bez skracania i bez zmiany brzmienia | `02-szablony-dokumentow/certyfikat.md` |
| 4 | Objętość: ile stron zajmuje realne zaświadczenie w wariancie 1 „Kaszmir uporządkowany" - to pomiar zapowiedziany w `PLAN.md` przy wyborze układu księgi marki | `PLAN.md`, sekcja o wariancie 1 |
| 5 | Czy status ma etykietę słowną obok koloru w **każdym** miejscu, gdzie kolor niesie znaczenie | `paleta-barw.md`, sekcja „Kolor nigdy nie jest jedynym nośnikiem statusu" |

- [ ] **Krok 1:** napisać formularz z pustą kolumną „Co zobaczyłem" i kolumną „Na czym
      (kanwa / PDF / wydruk / kopia mono)".
- [ ] **Krok 2:** dopisać sekcję „Czego ten dokument nie sprawdzi", tak jak ma pilot.
- [ ] **Krok 3: commit**

### Zadanie B4: dołożyć cztery pliki do projektu w Claude Design

**Pliki w projekcie `1a22ce64-0e1c-43a6-bd60-eef9241ef73b`:**
- `guidelines/certyfikat.md` z `02-szablony-dokumentow/certyfikat.md`
- `guidelines/bur.md` z `01-baza-wiedzy/prawo/bur.md`
- `guidelines/kfs.md` z `01-baza-wiedzy/prawo/kfs.md`
- `guidelines/pozyczki-ue-bgk.md` z `01-baza-wiedzy/prawo/pozyczki-ue-bgk.md`

**To jest zapis do usługi zewnętrznej, więc wymaga zgody właściciela przed wykonaniem.**
Cofnięcie: `DesignSync delete_files` na tych czterech ścieżkach; żaden istniejący plik nie jest
nadpisywany, bo `guidelines/` ma dziś osiem plików i żadna z tych czterech nazw w nim nie występuje.

- [ ] **Krok 1:** skopiować cztery pliki do `_robocze/ds-bundle/guidelines/`, bo `write_files`
      czyta z katalogu zatwierdzonego w planie (`localDir`).
- [ ] **Krok 2:** `DesignSync finalize_plan` z `writes` na cztery ścieżki i `deletes: []`.
- [ ] **Krok 3:** `DesignSync write_files` z `planId` i `localPath` każdego pliku.
- [ ] **Krok 4: weryfikacja**

```
DesignSync list_files projectId=1a22ce64-0e1c-43a6-bd60-eef9241ef73b
```

Oczekiwane: `guidelines/` ma **dwanaście** plików, w tym cztery nowe.

- [ ] **Krok 5:** sprawdzić treść jednego z nich, żeby wykluczyć wysłanie pustego pliku.

```
DesignSync get_file projectId=1a22ce64-0e1c-43a6-bd60-eef9241ef73b path=guidelines/certyfikat.md
```

Oczekiwane: w treści występuje „Elementy prawnie obowiązkowe".

- [ ] **Krok 6: commit** kopii w `_robocze/ds-bundle/`.

---

## Kolejność i równoległości

- **A0 jest pierwsze.** Właściciel wkleja brief poprawek, projektant je wykonuje, ja weryfikuję
  rachunkiem. Dopóki A0 nie jest zamknięte, pomiarów nie robimy - mierzyłyby stan, który się
  jeszcze zmieni.
- **A1 i A6 ruszają natychmiast** - nie potrzebują właściciela ani Claude Design.
- **A2, A3 i A4 idą po A0**, nie przed. To praca na kanwie i wydruku plus jedna decyzja.
  **B0 nie czeka na A0** - pięć decyzji o certyfikacie jest od pilota niezależne.
- **Strumień S wyprzedza B.** Właściciel odłożył merytorykę, więc konkretne dokumenty (certyfikat,
  karta usługi, viewbook) czekają na zamknięcie szablonów uniwersalnych.
- **B1 zależy wyłącznie od B0.** Nie zależy od bramki B, więc oba strumienie idą równolegle.
- **B2 zależy od B1**, bo jest jego przekładem. **B3 i B4 są niezależne od B1** i mogą powstać
  wcześniej.
- **A5 jest ostatnie w strumieniu A**, po A1-A4.

Ryzyko blokujące jedno: jeżeli B0 krok 1 wyjdzie na A4 poziom, dochodzi zadanie nieujęte w tym
planie - przeliczenie i zatwierdzenie piątej specyfikacji identyfikacji. Wtedy B1 czeka na nią.

## Weryfikacja domknięcia planu

| Kryterium | Komenda | Oczekiwane |
|---|---|---|
| Stopka strony pierwszej mieści się w polu treści | `DesignSync get_file` na kanwie, potem suma kolumn stopki | `170 mm`, brak `62mm` |
| Każdy pomiar pilota ma wynik albo jawnie przeniesiony nośnik | `grep -c "| | |" _robocze/pilot-papier-firmowy/protokol-pomiaru.md` | `0` |
| Bramka B zamknięta | `grep -c "Etap czeka wyłącznie na przeprowadzenie pilota" MAPA-DROGOWA.md` | `0` |
| Nieaktualne zdania o kanwie usunięte | `grep -rn "kanwę zasiewa się od nowa" MAPA-DROGOWA.md PLAN.md _robocze/pilot-papier-firmowy/README.md` | zero trafień |
| Para plików zlecenia certyfikatu istnieje | `ls 03-pakiet-claude-design/zlecenia/certyfikat-zaswiadczenie*.md` | dwa pliki |
| Wersja do wysłania nie ma ścieżek lokalnych | komenda z B2 krok 2 | zero trafień |
| Formularz certyfikatu istnieje | `ls _robocze/certyfikat/protokol-pomiaru.md` | plik istnieje |
| Cztery pliki w projekcie Claude Design | `DesignSync list_files` | `guidelines/` ma dwanaście plików |
| Zero zmyślonych danych osobowych we wzorze | `grep -nE "PESEL [0-9]|[0-9]{11}" 03-pakiet-claude-design/zlecenia/certyfikat-zaswiadczenie*.md` | zero trafień |
| Zero myślników w nowych plikach | `grep -c "\u2014\|\u2013" 03-pakiet-claude-design/zlecenia/certyfikat-zaswiadczenie*.md _robocze/certyfikat/protokol-pomiaru.md` | `0` w każdym |

## Otwarte pytania

Sześć, wszystkie do właściciela. Pięć jest w zadaniu B0. Szóste w A4. Dodatkowo dwa, które wyszły
z pomiaru 2 i z weryfikacji stanu:

- **Stopka strony pierwszej jest o 8 mm szersza od pola treści** i obcina NIP, REGON, telefon oraz
  adres strony. Poprawiamy dokument czy pojemnik. Dane z art. 206 KSH są prawnie obowiązkowe,
  więc to nie jest kosmetyka.
- **Przebarwienie znaku łańcuchem `filter:`** - właściciel odłożył decyzję do obejrzenia pracy
  Claude Design. Do jej podjęcia w zleceniach obowiązuje `logotyp.md` bez zmian.
