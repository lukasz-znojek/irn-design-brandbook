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

15. Zdefiniować format paczki wejściowej dla Claude Design → `03-pakiet-claude-design/format-paczki.md`. **[FOUNDER] — w pełni rozstrzygnięte (2026-09-02):** siatka A4 (6 kolumn, moduł 25 mm, gutter 4 mm — poprawka błędu wymiarów z kanwy) i paleta 12 kolorów (Miedź pogłębiona do `#8C5026`, Karmin zmieniony na `#AC151F`) zatwierdzone przez foundera i wpisane do `format-paczki.md`. Historia decyzji: `03-pakiet-claude-design/propozycja-palety-i-siatki-do-potwierdzenia.md`.
16. Napisać prompt bazowy dla Claude Design, odwołujący się do warstw 1 i 2 → `03-pakiet-claude-design/prompt-bazowy.md`.

## Decyzje foundera — rozstrzygnięte

- **Paleta barw - wybór wariantu (2026-09-02, decyzja późniejsza)**: automatyczne przyjęcie palety z 2026-09-02 zostało wstrzymane jako wymagające dopracowania. Powstało siedem wariantów z pomiarem kontrastu (`_robocze/paleta-v2/palette-options-v2.md`); founder wybrał **wariant 2 „Kaszmir Wyciszony”** - 14 kolorów, z których 12 to przesunięcia kolorów już nazwanych, a dwa są nowe (Popiół jako `border`, Patyna jako `link`; obie nazwy zatwierdzone przez foundera 2026-09-02). Powód wyboru: usuwa trzy zmierzone defekty poprzedniej palety (link i błąd w tym samym kolorze, `info` nieodróżnialny od tekstu korpusu, obramowanie w pełnym tuszu), nie zmieniając kierunku „ciepły papier plus bordo”. Obowiązująca specyfikacja: `01-baza-wiedzy/identyfikacja/paleta-barw.md` (przeniesiona do warstwy 1 decyzją foundera 2026-09-02; `format-paczki.md` już jej nie duplikuje, tylko się do niej odwołuje). Siatka A4 i typografia bez zmian.
- **Siatka i typografia przeniesione do warstwy 1 (2026-09-02)**: `01-baza-wiedzy/identyfikacja/siatka-a4.md` i `identyfikacja/typografia.md`, obok palety. `03-pakiet-claude-design/format-paczki.md` nie powtarza już żadnej z trzech specyfikacji - odsyła do nich i dokłada sześć zasad użycia, bez których same wartości są niekompletne. Zasady logotypu zostały w `format-paczki.md`; są tej samej kategorii i mogą pójść tą samą drogą.
- **Rozbieżność otwarta - jednostka bazowa 6 mm**: wysokość pola treści 251 mm nie dzieli się na 6 mm (41 jednostek i 5 mm reszty). Domknięcie rytmu wymagałoby marginesu dolnego 33 mm zamiast zatwierdzonych 28 mm. Zatwierdzonej wartości nie zmieniono; szczegóły w `01-baza-wiedzy/identyfikacja/siatka-a4.md`.
- **Tryb monochromatyczny - odrzucony (2026-09-02)**: rozważany był wariant 6 „Druk Ekonomiczny” jako osobny tryb mono dla zaświadczeń KFS. Founder wybrał jedną paletę na wszystko. Skutek: obowiązkowa etykieta słowna albo ikona przy każdym statusie jest teraz jedynym zabezpieczeniem czytelności w druku mono.
- **Poziom H3 - zatwierdzony (2026-09-02)**: Manrope 600 / 16 px / interlinia 1,3, czyli stopień leadu z podniesioną wagą. Kanwa nie definiowała tego poziomu. Wpisany do `03-pakiet-claude-design/format-paczki.md` wraz z pełną skalą typograficzną.

- **Paleta barw** (12 kolorów, "Colorbook Kaszmir Aksamit", reguła 80/15/5) i **siatka A4**: kierunek z `brandbook.dc.html` zaakceptowany, dopracowany i **w pełni zatwierdzony (2026-09-02)** — siatka 6 kolumn / moduł 25 mm / gutter 4 mm (poprawka błędu wymiarów oryginału), Miedź pogłębiona do `#8C5026`, Karmin zmieniony na `#AC151F`. Specyfikacja: `03-pakiet-claude-design/format-paczki.md`.
- **Minimalny rozmiar i przestrzeń ochronna logotypu** (18 mm / 90 px, x = wysokość liter sygnetu): **potwierdzone jako obowiązujące**.
- **Aplikacje dla przedstawicieli handlowych**: narzędzie wewnętrzne IRIN — CRM/aplikacja dla własnych handlowców (lead-y, prowizje, raportowanie sprzedaży szkoleń i pożyczek), nie produkt na sprzedaż zewnętrzną.
- **Usługi pozyskiwania pożyczek UE/BGK**: pośrednictwo finansowania rozwojowego dla firm (B2B) — doradztwo i pośrednictwo w pozyskiwaniu dotacji UE i pożyczek BGK dla małych i średnich przedsiębiorstw.
- **Portal sprzedaży szkoleń online**: model hybrydowy — portal sprzedaje miejsca na szkolenia (w tym dofinansowane KFS/BUR) i pozwala je zrealizować zdalnie (webinary, materiały do pobrania), bez pełnej platformy LMS.

## Decyzja do potwierdzenia przez foundera (nowa)

- Czy dane rejestrowe IRIN (KRS/NIP/REGON/adres/kontakt) w `01-baza-wiedzy/firma/kontekst-firmy-sanitized.md` mogą zostać w publicznym repozytorium — są jawne w KRS, ale to founder decyduje, czy mają trafić do publicznego repo.
