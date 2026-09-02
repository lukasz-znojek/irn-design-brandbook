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
20. Etap 2, weryfikacja prawna u źródła: osiem dokumentów z `01-baza-wiedzy/prawo/weryfikacja-u-zrodla.md` (lista gotowa 2026-09-02) → pliki w `01-baza-wiedzy/prawo/` i karty w `02-szablony-dokumentow/`. **[FOUNDER]** dostarcza PDF-y albo fragmenty, bo domeny PARP i Dziennika Ustaw są z sesji Claude Code niedostępne (pomiar 2026-09-02).
21. Etap 3, karty warstwy 2: każde „do potwierdzenia przez foundera” zamienić na decyzję albo na status „otwarte do pierwszego użycia” z nazwą dokumentu → wszystkie pliki w `02-szablony-dokumentow/`. Zrealizowane 2026-09-02: zero znaczników, cztery pozycje otwarte do pierwszego zlecenia (viewbook: segmentacja i cykl; certyfikat: dwie wersje; karta usługi BUR: zapis dziedziny).
22. Etap 4, pilot: paczka i zlecenie gotowe w `03-pakiet-claude-design/zlecenia/pilot-papier-firmowy.md` (2026-09-02), z pięcioma polami do wypełnienia z odpisu KRS i danych kontaktowych. **[FOUNDER]** przeprowadza przez Claude Design; potem Claude Code wpisuje wyniki protokołu pomiaru (polskie znaki na wagach 400-600, siatka 25 mm z treścią, H3 obok leadu, sygnet na rewersie, dokument bez koloru dziedzinowego) → `01-baza-wiedzy/identyfikacja/`. Kontrast Karminu obok Aksamitu ten pilot nie sprawdzi; czeka na pierwszy dokument ze statusami.
23. Etap 5, zamknięcie: `PLAN.md` bez pozycji otwartych, `README.md` ze stanem „gotowe do użycia” i datą, tag `v1.0` na `main`.

## Decyzje foundera — rozstrzygnięte

- **Paleta barw - wybór wariantu (2026-09-02, decyzja późniejsza)**: automatyczne przyjęcie palety z 2026-09-02 zostało wstrzymane jako wymagające dopracowania. Powstało siedem wariantów z pomiarem kontrastu (`_robocze/paleta-v2/palette-options-v2.md`); founder wybrał **wariant 2 „Kaszmir Wyciszony”** - 14 kolorów, z których 12 to przesunięcia kolorów już nazwanych, a dwa są nowe (Popiół jako `border`, Patyna jako `link`; obie nazwy zatwierdzone przez foundera 2026-09-02). Powód wyboru: usuwa trzy zmierzone defekty poprzedniej palety (link i błąd w tym samym kolorze, `info` nieodróżnialny od tekstu korpusu, obramowanie w pełnym tuszu), nie zmieniając kierunku „ciepły papier plus bordo”. Obowiązująca specyfikacja: `01-baza-wiedzy/identyfikacja/paleta-barw.md` (przeniesiona do warstwy 1 decyzją foundera 2026-09-02; `format-paczki.md` już jej nie duplikuje, tylko się do niej odwołuje). Siatka A4 i typografia bez zmian.
- **Siatka, typografia i logotyp przeniesione do warstwy 1 (2026-09-02)**: `identyfikacja/siatka-a4.md`, `identyfikacja/typografia.md` i `identyfikacja/logotyp.md`, obok palety. `03-pakiet-claude-design/format-paczki.md` nie powtarza już żadnej z trzech specyfikacji - odsyła do nich i dokłada sześć zasad użycia, bez których same wartości są niekompletne. Zasady logotypu dołączyły tą samą drogą.
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

- Żadna nie blokuje pilota. Pozostają decyzje zależne od pierwszego użycia: historia kluczowych etapów firmy, nazwa i termin portalu, nazwy ekranów aplikacji oraz konkretne dane podpisującego. Ustalenia o strukturze zespołu, viewbooku, certyfikacie, modelu portalu, aplikacji i syg­necie wpisano 2026-09-02 do odpowiednich plików. Archiwum `_robocze/copilot-v1/` usunięto na prośbę foundera.
