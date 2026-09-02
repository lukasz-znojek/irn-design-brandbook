# Mapa drogowa domknięcia projektu

Stan na 2026-09-02, po scaleniu PR #8 (logotyp w warstwie 1). Ten plik odpowiada na trzy pytania: co jest zrobione, co zostało, w jakiej kolejności to zamykać. Kolejka zadań pozostaje w `PLAN.md`; tutaj są etapy, bramki i zależności między nimi.

## Skąd wiadomo, że projekt jest gotowy

Repozytorium nie definiuje wprost, co znaczy „projekt zamknięty”. Z `CLAUDE.md` wynika, że repozytorium przechowuje treść i wytyczne, a kompozycja powstaje w Claude Design. Możliwe są więc dwa odczyty gotowości:

| Wariant | Co znaczy „gotowe” | Czego wymaga ponad stan obecny |
|---|---|---|
| **A. Repozytorium gotowe do użycia** | Trzy warstwy kompletne i spójne, żadna karta nie zawiera pozycji „do potwierdzenia przez foundera”, każde ustalenie prawne ma źródło pierwotne albo jawny status niesprawdzone. | Etapy 0-3 poniżej. |
| **B. Repozytorium sprawdzone w boju** | To, co w A, plus co najmniej jeden dokument przeprowadzony przez pełną ścieżkę: paczka wg `format-paczki.md`, prompt bazowy, wynik z Claude Design, wnioski wpisane z powrotem do warstwy 1. | Etapy 0-4 poniżej. |

**Rekomendacja: wariant B z jednym dokumentem pilotażowym.** Powód, który da się obalić: cztery specyfikacje identyfikacji mają wpisane falsyfikatory, których nie sprawdzi żaden przegląd plików, tylko realny dokument (polskie znaki na wagach 500 i 600, Karmin obok Aksamitu na papierze, sześć kolumn po 25 mm z realną treścią, H3 obok leadu). Zamknięcie bez pilota zostawia te cztery pozycje otwarte na zawsze. Jeżeli founder uzna, że pilot należy już do „użytkowania”, a nie do „budowy”, wariant A jest domknięciem poprawnym i o jeden etap krótszym.

## Co jest zrobione

| Warstwa | Zrealizowane | Dowód |
|---|---|---|
| 1 - baza wiedzy | Firma (2 pliki), prawo (6 plików: KFS, BUR, PSF, pożyczki UE/BGK plus dwa materiały źródłowe), usługi (2 pliki), szablon karty produktu, indeks. | `01-baza-wiedzy/00-INDEX.md` odsyła do każdego z nich. |
| 1 - identyfikacja | Paleta 14 kolorów „Kaszmir Wyciszony”, siatka A4, typografia z H3, logotyp z czterema zakazami. Wszystkie cztery zatwierdzone przez foundera. Tokeny maszynowe w jednym JSON. | `01-baza-wiedzy/identyfikacja/`, decyzje w `PLAN.md`, sekcja „Decyzje foundera - rozstrzygnięte”. |
| 2 - szablony | Siedem kart specyfikacji: viewbook, karta usługi BUR, certyfikat, papier firmowy i wizytówka, materiał sprzedażowy, program szkolenia, prezentacja sprzedażowa. Każda rozróżnia trzy kategorie elementów. | Pomiar w tej sesji: w każdym z siedmiu plików występują wszystkie trzy hasła („prawnie obowiązkowe”, „konwencja”, „swobodny wybór”). |
| 3 - pakiet | Format paczki z sześcioma zasadami użycia, prompt bazowy odsyłający do warstw 1 i 2, historia decyzji o palecie i siatce. | `03-pakiet-claude-design/`. |
| Zadania z `PLAN.md` | 16 z 16 ponumerowanych zadań ma plik docelowy. | Lista w `PLAN.md`; brak zadań 17+. |

## Co zostało

Cztery grupy pracy, różne co do tego, kto je może wykonać.

### Grupa I - higiena repozytorium (może zrobić Claude Code, bez decyzji foundera)

1. Cztery zdania, które opisują stan nieaktualny:
   - `01-baza-wiedzy/00-INDEX.md`, wiersz o siatce: „jedną otwartą rozbieżnością co do jednostki bazowej 6 mm”, a `siatka-a4.md` ma tę sprawę rozstrzygniętą.
   - `01-baza-wiedzy/README.md`: „na razie paletę barw”, a w `identyfikacja/` są cztery specyfikacje.
   - `PLAN.md`, zadanie 15: „paleta 12 kolorów (...) wpisane do `format-paczki.md`”, a obowiązuje 14 kolorów w warstwie 1 i `format-paczki.md` już palety nie zawiera.
   - `PLAN.md`, wiersz „Paleta barw (12 kolorów, Colorbook Kaszmir Aksamit) (...) Specyfikacja: `format-paczki.md`”: ta sama nieaktualność co wyżej.
2. `PLAN.md` nie ma zadań 17+; kolejka kończy się na promptcie bazowym, choć praca trwa. Do dopisania zadania z tej mapy.
3. Dwa otwarte PR-y i trzy martwe gałęzie (rozstrzygnięcie niżej, w grupie IV).

### Grupa II - decyzje foundera (blokują karty warstwy 2 i pilota)

Każda pozycja to jedno zdanie, z plikiem, który na nią czeka. Podział na to, co blokuje pilota, i to, co można odłożyć.

**Blokujące pilota (papier firmowy i wizytówka):**

| Decyzja | Czeka plik | Co się zmieni po decyzji |
|---|---|---|
| Czy dane rejestrowe (KRS, NIP, REGON, adres) zostają w publicznym repozytorium. | `01-baza-wiedzy/firma/kontekst-firmy-sanitized.md`, `PLAN.md` | Tak: dane wchodzą do paczki papieru firmowego. Nie: paczka dostaje placeholder, a dane przychodzą przy każdym zleceniu. |
| Forma prawna i siedziba IRIN. | `02-szablony-dokumentow/papier-firmowy.md`, `01-baza-wiedzy/firma/kontekst-firmy.md` | Rozstrzyga, który zestaw danych jest prawnie obowiązkowy na papierze firmowym. |
| Czy papier firmowy zawiera e-mail, telefon i adres strony, a wizytówka ma format 85 × 55 mm, awers i rewers. | `02-szablony-dokumentow/papier-firmowy.md` | Z obserwacji z kanwy staje się konwencją IRIN albo zostaje swobodnym wyborem projektowym. |

**Sprzeczność do nazwania obiema stronami, zanim founder odpowie:** `kontekst-firmy.md` mówi, że siedziba i forma prawna to brak danych, a napis „Warszawa” z kanwy nie jest przyjmowany. `kontekst-firmy-sanitized.md` podaje „Instytut Rozwoju i Nauki sp. z o.o.” i adres w Kielcach z numerem KRS. `papier-firmowy.md` opiera się na pierwszym z tych plików. Po decyzji foundera ma zostać jedna wersja we wszystkich trzech miejscach.

**Do odłożenia, aż powstanie dokument, którego dotyczą:**

| Decyzja | Czeka plik |
|---|---|
| Czy viewbook wychodzi osobno per dziedzina (Pedagogika, Akademia AI, Pożyczki UE/BGK) i w cyklu rocznym. | `02-szablony-dokumentow/viewbook.md`, `karta-uslugi-bur.md` |
| Czy certyfikat ma dwie wersje wdrożeniowe (kolumnowa, z pieczęcią) i regułę doboru wg kanału dystrybucji. | `02-szablony-dokumentow/certyfikat.md` |
| Model organizacyjny i historia firmy. | `01-baza-wiedzy/firma/kontekst-firmy.md` |
| Aplikacja sprzedażowa: platforma (web, mobile) i stan wdrożenia. | `01-baza-wiedzy/uslugi/aplikacje-sprzedazowe.md`, `02-szablony-dokumentow/material-sprzedazowy.md` |
| Portal szkoleń: nazwa, termin, technologia webinarów, model cenowy. | `01-baza-wiedzy/uslugi/portal-szkolen.md` |
| Minimalny rozmiar samodzielnego sygnetu (10 mm / 44 px) i kontrast znaku na akcentach dziedzinowych 4,5:1. | `01-baza-wiedzy/identyfikacja/logotyp.md` (plik sam odkłada to do pierwszego użycia sygnetu) |

### Grupa III - weryfikacja prawna u źródła pierwotnego

Wszystkie ustalenia prawne w warstwie 1 pochodzą ze źródeł wtórnych, bo w sesjach, w których powstały, dostęp do domen PARP i Dziennika Ustaw był zablokowany. Każda pozycja ma wpisany falsyfikator; zamknięcie oznacza odczyt dokumentu i wpisanie wyniku.

| Co sprawdzić | Dokument źródłowy | Który plik czeka |
|---|---|---|
| Lista obowiązkowych pól karty usługi. | Regulamin BUR, Załącznik nr 2 | `prawo/bur.md`, `02-szablony-dokumentow/karta-uslugi-bur.md` |
| Pola zaświadczenia o ukończeniu usługi. | Regulamin BUR, Załącznik nr 12 | `prawo/bur.md`, `02-szablony-dokumentow/certyfikat.md` |
| Format kodu usługi (`2025/00817/PPUR` z kanwy to obserwacja, nie wymóg). | Regulamin BUR | `prawo/bur.md` |
| Treść rozporządzenia o KFS z 25 listopada 2025. | Dziennik Ustaw | `prawo/kfs.md` |
| Czy operatorzy regionalni PSF nakładają na dostawcę kryteria ponad wpis do BUR. | Regionalne „Zasady udzielania wsparcia” | `prawo/psf.md`, `prawo/bur.md` |
| Czy karta usługi w BUR jest wymagana na etapie wniosku KFS. | Regulamin konkretnego urzędu pracy | `prawo/kontekst-kfs-sanitized.md` |
| Rozdział beneficjent a doradca zewnętrzny w Księdze Tożsamości Wizualnej Funduszy Europejskich. | Księga Tożsamości Wizualnej FE | `prawo/pozyczki-ue-bgk.md`; tylko jeśli IRIN zechce użyć znaku FE |

Jeśli dostęp do tych domen nadal będzie zablokowany, dokumenty musi dostarczyć founder (PDF do repozytorium albo wklejony fragment). To jedyna grupa, której Claude Code nie domknie samodzielnie bez zmiany dostępu sieciowego.

### Grupa IV - porządek w gałęziach i PR-ach

| Pozycja | Stan zmierzony w tej sesji | Rekomendacja |
|---|---|---|
| PR #4 „finalize post-merge follow-ups” (`chore/post-merge-followups-psf-bur-kontekst`) | 1 commit, 3 pliki, 11 commitów za `main`, scalenie bez konfliktów (sprawdzone `git merge-tree`). Rozstrzyga pośrednio wymóg wpisu dostawcy do BUR dla PSF i usuwa e-mail, telefon i adres strony z karty kontekstu firmy. | **Scalić**, bo zawęża otwarte pytanie o PSF i realizuje zasadę minimalizacji danych. Uwaga: usunięcie danych kontaktowych to część decyzji foundera o danych rejestrowych; scalenie nie zamyka tej decyzji, tylko zmniejsza jej zakres do KRS, NIP, REGON i adresu. |
| PR #6 „Siedem wariantów palety v2” (`claude/irin-color-palette-variants-dl9lge`) | Dodaje katalog `02-branding/` z siedmioma wariantami. Ta sama treść trafiła już do `main` przez PR #5, w katalogu `_robocze/paleta-v2/`. | **Zamknąć bez scalenia** jako zastąpiony; scalenie stworzyłoby drugą kopię wariantów w katalogu, którego architektura trzech warstw nie przewiduje. |
| Gałęzie `copilot/irin-brandbook-os`, `claude/irin-color-palette-variants-tjjnza` | 0 commitów przed `main`. | Usunąć (odwracalne: `git push origin <gałąź>` z lokalnej kopii przywraca). Usunięcie czeka na decyzję foundera. |

## Etapy i bramki

```mermaid
flowchart TD
    S0["Etap 0 - higiena<br/>4 nieaktualne zdania, PLAN 17+,<br/>PR #4 scalić, PR #6 zamknąć"]
    S1["Etap 1 - decyzje foundera<br/>3 blokujące pilota + 6 do odłożenia"]
    S2["Etap 2 - weryfikacja prawna<br/>BUR zał. 2 i 12, kod usługi,<br/>KFS z Dz.U., operatorzy PSF"]
    S3["Etap 3 - domknięcie kart warstwy 2<br/>każde „do potwierdzenia” zamienione<br/>na decyzję albo status niesprawdzone"]
    S4["Etap 4 - pilot w Claude Design<br/>papier firmowy i wizytówka:<br/>paczka, prompt, wynik, wnioski do warstwy 1"]
    S5["Etap 5 - zamknięcie<br/>PLAN.md domknięty, README ze stanem,<br/>tag v1.0, procedura domknięcia okna"]

    G1{"Bramka A<br/>brak „do potwierdzenia”<br/>w kartach warstwy 2"}
    G2{"Bramka B<br/>4 falsyfikatory identyfikacji<br/>sprawdzone na realnym dokumencie"}

    S0 --> S1
    S0 --> S2
    S1 --> S3
    S2 --> S3
    S3 --> G1
    G1 -->|wariant A| S5
    G1 -->|wariant B| S4
    S4 --> G2
    G2 --> S5

    style S0 fill:#F2ECE1,stroke:#1E1611,color:#1E1611
    style S1 fill:#F2ECE1,stroke:#1E1611,color:#1E1611
    style S2 fill:#F2ECE1,stroke:#1E1611,color:#1E1611
    style S3 fill:#F2ECE1,stroke:#1E1611,color:#1E1611
    style S4 fill:#F2ECE1,stroke:#1E1611,color:#1E1611
    style S5 fill:#F2ECE1,stroke:#1E1611,color:#1E1611
    style G1 fill:#E4DACB,stroke:#1E1611,color:#1E1611
    style G2 fill:#E4DACB,stroke:#1E1611,color:#1E1611
```

Etapy 1 i 2 są niezależne i mogą iść równolegle: pierwszy wymaga foundera, drugi dostępu do dokumentów źródłowych. Etap 3 czeka na oba.

| Etap | Kto wykonuje | Warunek wyjścia (mierzalny) |
|---|---|---|
| 0 - higiena | Claude Code | `grep` po czterech nieaktualnych zdaniach zwraca zero trafień; `PLAN.md` ma zadania 17+; na GitHubie nie ma otwartego PR poza bieżącym. |
| 1 - decyzje foundera | Founder, Claude Code wpisuje | Trzy decyzje blokujące pilota wpisane do `PLAN.md` w sekcji „rozstrzygnięte”; sprzeczność o siedzibę i formę prawną ma jedną wersję w trzech plikach. |
| 2 - weryfikacja prawna | Claude Code przy dostępie do PARP i Dz.U., inaczej founder dostarcza dokumenty | Każde z siedmiu ustaleń ma wpisane: odczytane u źródła albo status niesprawdzone z nazwanym powodem. Zero pozycji „do potwierdzenia przy dostępie do PARP”. |
| 3 - karty warstwy 2 | Claude Code | `grep -i "do potwierdzenia przez foundera" 02-szablony-dokumentow/` zwraca zero trafień; pozycje odłożone mają status „otwarte do pierwszego użycia” z nazwą dokumentu. |
| 4 - pilot | Founder w Claude Design, Claude Code buduje paczkę i spisuje wnioski | Cztery falsyfikatory z warstwy 1 (polskie znaki na 500 i 600, Karmin obok Aksamitu, siatka 25 mm z treścią, H3 obok leadu) mają wpisany wynik pomiaru w swoich plikach. |
| 5 - zamknięcie | Claude Code, founder zatwierdza | `PLAN.md` bez pozycji otwartych, `README.md` podaje stan „gotowe do użycia” z datą, tag `v1.0` na `main`. |

## Dlaczego pilotem jest papier firmowy, a nie certyfikat

Papier firmowy i wizytówka wymagają wszystkich czterech specyfikacji identyfikacji (logotyp, paleta, siatka, typografia) i mają najmniej zależności prawnych: jedyny wymóg to komplet danych rejestrowych, który zależy od jednej decyzji foundera. Certyfikat i karta usługi BUR zależą od Załączników 2 i 12 Regulaminu BUR, których odczyt jest w grupie III i może się przeciągnąć. Falsyfikator tego wyboru: jeśli founder potrzebuje pilnie zaświadczenia KFS na najbliższe szkolenie, pilotem staje się certyfikat, a papier firmowy idzie jako drugi.

## Czego ta mapa nie rozstrzyga

- Czy repozytorium ma zostać publiczne. Od tego zależy decyzja o danych rejestrowych, nie odwrotnie.
- Czy `_robocze/copilot-v1/` (30 plików po angielsku) ma zostać w repozytorium jako archiwum, czy wyjść do osobnego archiwum poza nim. Nie blokuje żadnego etapu.
- Terminy. Etapy są ułożone wg zależności, nie wg kalendarza; czas etapu 1 zależy od foundera, etapu 2 od dostępu do dokumentów.
