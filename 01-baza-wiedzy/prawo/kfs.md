# Krajowy Fundusz Szkoleniowy (KFS)

Status weryfikacji: ustalenia poniżej są **niesprawdzone** u źródła. W dniu 2026-09-02 domena `dziennikustaw.gov.pl` była niedostępna z sesji Claude Code, a żaden dokument pierwotny nie został dostarczony do katalogu `01-baza-wiedzy/prawo/zrodla/`. Poniższe informacje mają charakter roboczy, nie są traktowane jako ostateczna interpretacja aktu prawnego i muszą zostać zweryfikowane przez bezpośredni odczyt rozporządzenia albo PDF dostarczony przez foundera.

## Co to jest KFS

Krajowy Fundusz Szkoleniowy to publiczny mechanizm dofinansowania kształcenia ustawicznego (szkoleń podnoszących kwalifikacje) pracowników i pracodawców, finansowany z Funduszu Pracy. Pracodawca składa wniosek o dofinansowanie do powiatowego urzędu pracy (PUP) właściwego dla siedziby lub miejsca prowadzenia działalności; po przyznaniu środków to on zawiera umowę z realizatorem szkolenia (np. z IRIN) i rozlicza się z PUP.

## Podstawa prawna — zmiana obowiązująca od 2026 roku

W 2026 roku (a więc już w momencie pisania tego pliku) obowiązuje **nowy** reżim prawny:

- **Ustawa z dnia 20 marca 2025 r. o rynku pracy i służbach zatrudnienia** — weszła w życie 1 czerwca 2025 r.; przepisy dotyczące KFS zaczęły obowiązywać od 1 stycznia 2026 r. Zastępuje wcześniejszą ustawę z 20 kwietnia 2004 r. o promocji zatrudnienia i instytucjach rynku pracy (na której KFS opierał się do końca 2025 r.).
- **Rozporządzenie Ministra Rodziny, Pracy i Polityki Społecznej z dnia 25 listopada 2025 r.** w sprawie Krajowego Funduszu Szkoleniowego — zastępuje rozporządzenie MPiPS z 14 maja 2014 r.
- **Rozporządzenie Komisji (UE) 2023/2831** w sprawie pomocy de minimis — dofinansowanie KFS dla pracodawcy jest pomocą de minimis i podlega jej limitom.

**Konsekwencja dla IRIN, kluczowa dla tego repozytorium:** od 1 stycznia 2026 r. zamknięto dotychczasowy Rejestr Instytucji Szkoleniowych (RIS, zamknięty 31 grudnia 2025 r.). Realizatorem szkolenia finansowanego z KFS może być **wyłącznie podmiot wpisany do Bazy Usług Rozwojowych (BUR)** prowadzonej przez PARP — ten sam rejestr, w którym IRIN musi figurować dla linii biznesowej BUR (patrz `./bur.md`). Innymi słowy: od 2026 roku obie ścieżki szkoleniowe IRIN (KFS i BUR) opierają się na tym samym wpisie rejestrowym, nie na dwóch osobnych rejestrach.

## Kto może skorzystać

Pracodawca zatrudniający co najmniej jednego pracownika. Ustawa z 2025 r. rozszerza od 2026 r. krąg osób, na których kształcenie można uzyskać dofinansowanie — o osoby na umowach zlecenia, umowach o dzieło oraz prowadzące jednoosobową działalność gospodarczą (dotąd KFS obejmował głównie pracowników etatowych). **Status: kierunek zmiany potwierdzony w kilku źródłach, szczegółowe warunki tego rozszerzenia — do zweryfikowania w treści rozporządzenia przed użyciem w konkretnym dokumencie.**

## Poziomy dofinansowania i limity kwotowe

Te wartości **zmieniają się corocznie** (a w 2026 r. dodatkowo w ramach reformy) — nie traktuj żadnej liczby niżej jako stałej specyfikacji do wpisania w dokument IRIN bez sprawdzenia aktualnych, obowiązujących w danym roku wytycznych:

- Dofinansowanie dla pracodawcy: najczęściej 90% kosztów kształcenia przy zatrudnieniu do 9 osób na umowę o pracę, 70% przy zatrudnieniu powyżej 9 osób (wcześniej, przed reformą: 100%/80%).
- Limit kwotowy na uczestnika: do 200% przeciętnego wynagrodzenia w danym roku kalendarzowym (wcześniej wyrażany też jako wielokrotność przeciętnego wynagrodzenia: 4×/8×/12×/14× w zależności od priorytetu).
- Priorytety wydatkowania KFS ustalane są **co roku** przez Radę Rynku Pracy i publikowane w wytycznych dla urzędów pracy — bez znajomości wytycznych na dany rok nie da się ocenić, czy konkretne szkolenie IRIN kwalifikuje się do dofinansowania.

## Wybór realizatora przez pracodawcę

Pracodawca sam wybiera realizatora (może nim być IRIN), kierując się zasadami konkurencyjności, równego traktowania i przejrzystości, i musi wykazać rozeznanie rynku we wniosku do PUP. Wymagany jest brak powiązań osobowych i kapitałowych między wnioskodawcą (pracodawcą) a realizatorem szkolenia.

## Dokumentacja ukończenia szkolenia

PUP i starosta kontrolują realizację umowy, w tym w miejscu prowadzenia szkolenia. W rozliczeniu pracodawca przedstawia m.in.: kopię umowy z realizatorem, program szkolenia, dziennik zajęć/harmonogram, potwierdzenia obecności oraz **zaświadczenie lub inny dokument potwierdzający ukończenie szkolenia** wydany przez realizatora (IRIN) każdemu uczestnikowi. Skoro od 2026 r. realizator musi być wpisany do BUR, dokument ukończenia szkolenia z dużym prawdopodobieństwem będzie podlegał tym samym wymogom, co certyfikat/zaświadczenie BUR opisany w `./bur.md` — **status: wniosek prawdopodobny, nie potwierdzony wprost w źródłach przeszukanych w tej sesji; do zweryfikowania przed ostatecznym zamknięciem karty specyfikacji certyfikatu (zadanie 10 w `/PLAN.md`).**

## Co z tego jest prawnie wiążące dla dokumentów IRIN

Dla karty specyfikacji certyfikatu/zaświadczenia w warstwie 2 (`/02-szablony-dokumentow/certyfikat.md`) z powyższego wynika jako **prawnie obowiązkowe**:
- dokument musi jednoznacznie identyfikować uczestnika, szkolenie, realizatora (IRIN) i zakres/liczbę godzin szkolenia — to jest wymóg rozliczeniowy wobec PUP, nie wybór estetyczny.
- IRIN jako realizator musi mieć aktualny wpis do BUR — to warunek prawny prowadzenia tej linii biznesowej, nie treść samego dokumentu, ale warunek jego wiarygodności.

Cokolwiek poza tymi dwoma punktami (układ graficzny, kolejność pól, dodatkowe elementy wizualne) nie wynika z przepisów KFS i należy rozstrzygać jako konwencję organizacyjną IRIN lub swobodny wybór projektowy w karcie specyfikacji.

## Źródła

- [Ustawa z dnia 20 marca 2025 r. o rynku pracy i służbach zatrudnienia — Dziennik Ustaw](https://dziennikustaw.gov.pl/D2025000062001.pdf)
- [Krajowy Fundusz Szkoleniowy (KFS) w roku 2026 — Sądecki Urząd Pracy](https://supnowysacz.praca.gov.pl/strona-glowna/-/asset_publisher/Qat7ebECUfDp/content/krajowy-fundusz-szkoleniowy-kfs-w-roku-2026)
- [Krajowy Fundusz Szkoleniowy w roku 2026 — kierunkowe wytyczne dla urzędów pracy (WUP Szczecin, PDF)](https://wupszczecin.praca.gov.pl/documents/10240/6350314/KFS+2026+-+Wytyczne+dla+urz%C4%99d%C3%B3w+pracy_aktualizacja+Luty+2026.pdf)
- [Nowa ustawa o rynku pracy i służbach zatrudnienia — ważne zmiany od 1 czerwca 2025 r. — WUP Warszawa](https://wupwarszawa.praca.gov.pl/-/nowa-ustawa-o-rynku-pracy-i-sluzbach-zatrudnienia-wazne-zmiany-od-1-czerwca-2025-r.)
- [Krajowy Fundusz Szkoleniowy — Ministerstwo Rodziny, Pracy i Polityki Społecznej](https://www.gov.pl/web/rodzina/krajowy-fundusz-szkoleniowy-fundusz-pracy)
- [Zostały niemal 2 miesiące do zamknięcia Rejestru Instytucji Szkoleniowych — PARP](https://www.parp.gov.pl/component/content/article/89517:zostaly-niemal-2-miesiace-do-zamkniecia-rejestru-instytucji-szkoleniowych-nie-zwlekaj-wpisz-swoja-firme-do-bazy-uslug-rozwojowych)
- [Uzyskaj wpis do Bazy Usług Rozwojowych — biznes.gov.pl](https://www.biznes.gov.pl/pl/portal/ou712)
