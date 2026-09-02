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
- `01-baza-wiedzy/prawo/psf.md` — karta produktu PSF (Podmiotowy System Finansowania). Zlecenie mówiło o karcie „PFS" — materiał źródłowy i terminologia urzędowa używają PSF, więc to nazwa kanoniczna; wyjaśnienie w nagłówku pliku.
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

15. Zdefiniować format paczki wejściowej dla Claude Design → `03-pakiet-claude-design/format-paczki.md`. **[FOUNDER]** (paleta barw i moduły siatki są zaakceptowanym kierunkiem, ale wymagają dopracowania — dokładnego pomiaru i zaplanowania kombinacji kolorów, zanim staną się wiążącą specyfikacją; patrz `CLAUDE.md`) — **format-paczki.md gotowy, świadomie bez wpisanej palety/siatki; dopracowana propozycja do zatwierdzenia czeka w `03-pakiet-claude-design/propozycja-palety-i-siatki-do-potwierdzenia.md`, w tym poprawka błędu wymiarów siatki A4 z kanwy.**
16. Napisać prompt bazowy dla Claude Design, odwołujący się do warstw 1 i 2 → `03-pakiet-claude-design/prompt-bazowy.md`.

## Decyzje foundera — rozstrzygnięte

- **Paleta barw** (12 kolorów, "Colorbook Kaszmir Aksamit", reguła 80/15/5) i **moduły siatki A4** (6 kolumn / 32 mm / gutter 4 mm) z `brandbook.dc.html`: zaakceptowany kierunek. Nie jest jeszcze wiążącą specyfikacją — wymaga dokładnego pomiaru i zaplanowania kombinacji kolorów przed wpisaniem do warstwy 1. Zadanie 15 pozostaje otwarte do tego czasu.
- **Minimalny rozmiar i przestrzeń ochronna logotypu** (18 mm / 90 px, x = wysokość liter sygnetu): **potwierdzone jako obowiązujące**.
- **Aplikacje dla przedstawicieli handlowych**: narzędzie wewnętrzne IRIN — CRM/aplikacja dla własnych handlowców (lead-y, prowizje, raportowanie sprzedaży szkoleń i pożyczek), nie produkt na sprzedaż zewnętrzną.
- **Usługi pozyskiwania pożyczek UE/BGK**: pośrednictwo finansowania rozwojowego dla firm (B2B) — doradztwo i pośrednictwo w pozyskiwaniu dotacji UE i pożyczek BGK dla małych i średnich przedsiębiorstw.
- **Portal sprzedaży szkoleń online**: model hybrydowy — portal sprzedaje miejsca na szkolenia (w tym dofinansowane KFS/BUR) i pozwala je zrealizować zdalnie (webinary, materiały do pobrania), bez pełnej platformy LMS.

## Decyzja do potwierdzenia przez foundera (nowa)

- Czy dane rejestrowe IRIN (KRS/NIP/REGON/adres/kontakt) w `01-baza-wiedzy/firma/kontekst-firmy-sanitized.md` mogą zostać w publicznym repozytorium — są jawne w KRS, ale to founder decyduje, czy mają trafić do publicznego repo.
