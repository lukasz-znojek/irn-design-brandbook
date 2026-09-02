# PLAN.md — kolejka zadań

Zadania w kolejności wykonania, jedno zdanie każde, z docelowym plikiem. Pozycje oznaczone **[FOUNDER]** wymagają decyzji foundera, zanim można je zacząć.

## Warstwa 1 — baza wiedzy

1. Spisać kontekst firmy IRIN (trzy linie biznesowe, model organizacyjny, historia) → `01-baza-wiedzy/firma/kontekst-firmy.md`. **[FOUNDER]** (materiał wejściowy gotowy: `01-baza-wiedzy/firma/kontekst-firmy-sanitized.md`)
2. Zebrać obowiązujące przepisy dot. Krajowego Funduszu Szkoleniowego (KFS) → `01-baza-wiedzy/prawo/kfs.md`. (materiał wejściowy gotowy: `01-baza-wiedzy/prawo/kontekst-kfs-sanitized.md`)
3. Zebrać wymogi certyfikacji BUR (Baza Usług Rozwojowych, PARP) → `01-baza-wiedzy/prawo/bur.md`.
4. Opisać regulacje dot. usług pożyczkowych UE/BGK → `01-baza-wiedzy/prawo/pozyczki-ue-bgk.md`. **[FOUNDER]** (zakres usługi do potwierdzenia)
5. Spisać wytyczne usługowe dla aplikacji przedstawicieli handlowych → `01-baza-wiedzy/uslugi/aplikacje-sprzedazowe.md`. **[FOUNDER]**
6. Spisać wytyczne dot. planowanego portalu sprzedaży szkoleń online → `01-baza-wiedzy/uslugi/portal-szkolen.md`. **[FOUNDER]** (portal jeszcze nie istnieje)
7. Uzupełnić `01-baza-wiedzy/00-INDEX.md` o odnośniki do wszystkich powyższych plików. (zrobione dla plików istniejących na dziś — patrz sekcja niżej; do dokończenia po pozycjach 1, 3-6)

## Warstwa 1 — zrealizowane poza pierwotną kolejnością

Zrobione w ramach sanitizacji materiałów wewnętrznych i karty PSF (nie były ponumerowane wyżej, bo PLAN.md nie przewidywał jeszcze tych plików):

- `01-baza-wiedzy/_szablony/karta-produktu.md` — szablon karty produktu/kanału dla warstwy 1.
- `01-baza-wiedzy/prawo/psf.md` — karta produktu PSF (Podmiotowy System Finansowania). Zlecenie mówiło o karcie „PFS" — materiał źródłowy i terminologia urzędowa używają PSF, więc to nazwa kanoniczna; wyjaśnienie w nagłówku pliku.
- `01-baza-wiedzy/prawo/kontekst-kfs-sanitized.md`, `01-baza-wiedzy/prawo/kontekst-psf-sanitized.md`, `01-baza-wiedzy/firma/kontekst-firmy-sanitized.md` — bezpieczne wersje robocze materiałów wewnętrznych, każda z notatką o sanitizacji.

## Warstwa 2 — szablony dokumentów

8. Karta specyfikacji viewbooka szkoleniowego → `02-szablony-dokumentow/viewbook.md`.
9. Karta specyfikacji karty usługi BUR → `02-szablony-dokumentow/karta-uslugi-bur.md`. (osobny dokument od `program-szkolenia.md` i `prezentacja-sprzedazowa.md` poniżej — karta usługi BUR to formalny dokument publikowany w BUR, nie program ani prezentacja)
10. Karta specyfikacji certyfikatu/zaświadczenia ukończenia szkolenia → `02-szablony-dokumentow/certyfikat.md`.
11. Karta specyfikacji papieru firmowego i wizytówki → `02-szablony-dokumentow/papier-firmowy.md`.
12. Karta specyfikacji materiałów aplikacji sprzedażowej → `02-szablony-dokumentow/material-sprzedazowy.md`. **[FOUNDER]** (zakres aplikacji do doprecyzowania)
13. ~~Karta specyfikacji programu szkolenia~~ → zrobione: `02-szablony-dokumentow/program-szkolenia.md`.
14. ~~Karta specyfikacji prezentacji produktowo-sprzedażowej~~ → zrobione: `02-szablony-dokumentow/prezentacja-sprzedazowa.md`.

## Warstwa 3 — pakiet Claude Design

15. Zdefiniować format paczki wejściowej dla Claude Design → `03-pakiet-claude-design/format-paczki.md`. **[FOUNDER]** (paleta barw i moduły siatki wymagają zatwierdzenia — patrz `CLAUDE.md`)
16. Napisać prompt bazowy dla Claude Design, odwołujący się do warstw 1 i 2 → `03-pakiet-claude-design/prompt-bazowy.md`.

## Decyzje foundera zebrane w jednym miejscu

- Czy 12-barwna paleta z `brandbook.dc.html` obowiązuje, czy to tylko robocza propozycja?
- Czy moduły siatki A4 (6 kolumn / 32 mm / gutter 4 mm) obowiązują, czy wymagają zmiany?
- Minimalny rozmiar i przestrzeń ochronna logotypu — potwierdzić wartości z `brandbook.dc.html` jako obowiązujące.
- Zakres usługi pożyczek UE/BGK, aplikacji sprzedażowej i portalu szkoleń — potrzebny opis od foundera, nie da się go wywnioskować z posiadanych plików.
