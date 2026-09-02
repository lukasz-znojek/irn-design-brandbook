# PLAN.md — kolejka zadań

Zadania w kolejności wykonania, jedno zdanie każde, z docelowym plikiem. Pozycje oznaczone **[FOUNDER]** wymagają decyzji foundera, zanim można je zacząć.

## Warstwa 1 — baza wiedzy

1. Spisać kontekst firmy IRIN (trzy linie biznesowe, model organizacyjny, historia) → `01-baza-wiedzy/firma/kontekst-firmy.md`.
2. Zebrać obowiązujące przepisy dot. Krajowego Funduszu Szkoleniowego (KFS) → `01-baza-wiedzy/prawo/kfs.md`.
3. Zebrać wymogi certyfikacji BUR (Baza Usług Rozwojowych, PARP) → `01-baza-wiedzy/prawo/bur.md`.
4. Opisać regulacje dot. usług pożyczkowych UE/BGK → `01-baza-wiedzy/prawo/pozyczki-ue-bgk.md`.
5. Spisać wytyczne usługowe dla aplikacji przedstawicieli handlowych → `01-baza-wiedzy/uslugi/aplikacje-sprzedazowe.md`.
6. Spisać wytyczne dot. planowanego portalu sprzedaży szkoleń online → `01-baza-wiedzy/uslugi/portal-szkolen.md`. (portal jeszcze nie istnieje)
7. Uzupełnić `01-baza-wiedzy/00-INDEX.md` o odnośniki do wszystkich powyższych plików.

## Warstwa 2 — szablony dokumentów

8. Karta specyfikacji viewbooka szkoleniowego → `02-szablony-dokumentow/viewbook.md`.
9. Karta specyfikacji karty usługi BUR → `02-szablony-dokumentow/karta-uslugi-bur.md`.
10. Karta specyfikacji certyfikatu/zaświadczenia ukończenia szkolenia → `02-szablony-dokumentow/certyfikat.md`.
11. Karta specyfikacji papieru firmowego i wizytówki → `02-szablony-dokumentow/papier-firmowy.md`.
12. Karta specyfikacji materiałów aplikacji sprzedażowej → `02-szablony-dokumentow/material-sprzedazowy.md`.

## Warstwa 3 — pakiet Claude Design

13. Zdefiniować format paczki wejściowej dla Claude Design → `03-pakiet-claude-design/format-paczki.md`. **[FOUNDER] — w pełni rozstrzygnięte (2026-09-02):** siatka A4 (6 kolumn, moduł 25 mm, gutter 4 mm — poprawka błędu wymiarów z kanwy) i paleta 12 kolorów (Miedź pogłębiona do `#8C5026`, Karmin zmieniony na `#AC151F`) zatwierdzone przez foundera i wpisane do `format-paczki.md`. Historia decyzji: `03-pakiet-claude-design/propozycja-palety-i-siatki-do-potwierdzenia.md`.
14. Napisać prompt bazowy dla Claude Design, odwołujący się do warstw 1 i 2 → `03-pakiet-claude-design/prompt-bazowy.md`.

## Decyzje foundera — rozstrzygnięte

- **Paleta barw** (12 kolorów, "Colorbook Kaszmir Aksamit", reguła 80/15/5) i **siatka A4**: kierunek z `brandbook.dc.html` zaakceptowany, dopracowany i **w pełni zatwierdzony (2026-09-02)** — siatka 6 kolumn / moduł 25 mm / gutter 4 mm (poprawka błędu wymiarów oryginału), Miedź pogłębiona do `#8C5026`, Karmin zmieniony na `#AC151F`. Specyfikacja: `03-pakiet-claude-design/format-paczki.md`.
- **Minimalny rozmiar i przestrzeń ochronna logotypu** (18 mm / 90 px, x = wysokość liter sygnetu): **potwierdzone jako obowiązujące**.
- **Aplikacje dla przedstawicieli handlowych**: narzędzie wewnętrzne IRIN — CRM/aplikacja dla własnych handlowców (lead-y, prowizje, raportowanie sprzedaży szkoleń i pożyczek), nie produkt na sprzedaż zewnętrzną.
- **Usługi pozyskiwania pożyczek UE/BGK**: pośrednictwo finansowania rozwojowego dla firm (B2B) — doradztwo i pośrednictwo w pozyskiwaniu dotacji UE i pożyczek BGK dla małych i średnich przedsiębiorstw.
- **Portal sprzedaży szkoleń online**: model hybrydowy — portal sprzedaje miejsca na szkolenia (w tym dofinansowane KFS/BUR) i pozwala je zrealizować zdalnie (webinary, materiały do pobrania), bez pełnej platformy LMS.
