# Krajowy Fundusz Szkoleniowy (KFS)

Status weryfikacji: sekcje „Podstawa prawna", „Kto może skorzystać", „Poziomy dofinansowania i limity kwotowe", „Wybór realizatora" i „Dokumentacja ukończenia szkolenia" są **odczytane u źródła** 2026-09-03, wprost z tekstów w Dzienniku Ustaw pobranych tego dnia i przechowywanych w `./zrodla/`. Każde twierdzenie ma podany artykuł albo paragraf. Sekcja „Co to jest KFS" jest streszczeniem mechanizmu, nie cytatem przepisu.

Trzy pliki źródłowe, wszystkie odczytane bezpośrednio:

| Akt | Plik | Uwaga |
|---|---|---|
| Ustawa z 20 marca 2025 r. o rynku pracy i służbach zatrudnienia, Dz.U. 2025 poz. 620 | `./zrodla/ustawa-o-rynku-pracy-i-sluzbach-zatrudnienia_dz-u-2025-poz-620.pdf` | 184 strony; KFS w art. 125-133, strony 59-62 |
| Rozporządzenie MRPiPS z 25 listopada 2025 r. w sprawie KFS, Dz.U. 2025 poz. 1641 | `./zrodla/rozporzadzenie-kfs_dz-u-2025-poz-1641.pdf` | 4 strony; weszło w życie 1 grudnia 2025 r. (§ 8) |
| Ustawa z 9 listopada 2000 r. o utworzeniu PARP, Dz.U. 2025 poz. 98 | `./zrodla/ustawa-o-utworzeniu-parp_dz-u-2025-poz-98.pdf` | potrzebna, żeby ustalić, o który rejestr chodzi w art. 128 ust. 2 |

**Falsyfikator całej tej sekcji:** nowelizacja któregokolwiek z tych trzech aktów ogłoszona po 2026-09-03. Sprawdzenie: `dziennikustaw.gov.pl/DU/2025/620`, `/DU/2025/1641`, `/DU/2025/98` — jeśli przy pozycji stoi odesłanie do tekstu jednolitego albo do zmiany późniejszej niż ta data, liczby i numery artykułów niżej trzeba przeliczyć od nowa.

## Co to jest KFS

Krajowy Fundusz Szkoleniowy to publiczny mechanizm dofinansowania kształcenia ustawicznego osób pracujących, finansowany z Funduszu Pracy. Podmiot (najczęściej pracodawca) składa wniosek do powiatowego urzędu pracy właściwego dla siedziby albo adresu prowadzenia działalności, w postaci elektronicznej przez indywidualne konto (art. 126 ust. 4). Po przyznaniu środków zawiera umowę ze starostą, a osobno umowę z realizatorem szkolenia — np. z IRIN — i rozlicza się z urzędem.

Cel ustawowy: „utrzymanie zatrudnienia i rozwój potencjału osób pracujących przez dostosowanie ich wiedzy, umiejętności lub kwalifikacji do wymagań zmieniającej się gospodarki" (art. 125 ust. 2).

## Podstawa prawna

- **Ustawa z 20 marca 2025 r. o rynku pracy i służbach zatrudnienia** (Dz.U. 2025 poz. 620) — KFS w art. 125-133.
- **Rozporządzenie MRPiPS z 25 listopada 2025 r. w sprawie KFS** (Dz.U. 2025 poz. 1641), wydane na podstawie art. 133 ustawy. Określa wyłącznie trzy rzeczy (§ 1): elementy wniosku i załączniki do niego, procedurę naboru, elementy umowy. **Nie zawiera żadnych wartości procentowych ani limitów kwotowych** — te są w ustawie.
- **Rozporządzenie Komisji (UE) 2023/2831** o pomocy de minimis — środki KFS przyznane podmiotowi prowadzącemu działalność gospodarczą stanowią pomoc de minimis (§ 7 rozporządzenia o KFS).
- Rozporządzenie z 25 listopada 2025 r. uchyliło rozporządzenie MPiPS z 14 maja 2014 r. (§ 8 wraz z przypisem 3).

**Konsekwencja dla IRIN, kluczowa dla tego repozytorium.** Art. 128 ust. 2 brzmi: „Instytucją realizującą szkolenie finansowane ze środków KFS jest realizator wpisany do rejestru, o którym mowa w art. 6 ust. 1 pkt 8 ustawy z dnia 9 listopada 2000 r. o utworzeniu Polskiej Agencji Rozwoju Przedsiębiorczości w zakresie świadczenia usług szkoleniowych" (s. 61). Ten rejestr to BUR: art. 6 ust. 1 pkt 8 ustawy o PARP mówi o „prowadzeniu rejestru podmiotów, które zapewniają należyte świadczenie usług doradczych i szkoleniowych, zwanych dalej «usługami rozwojowymi»" (Dz.U. 2025 poz. 98, s. 5). Obie ścieżki szkoleniowe IRIN, KFS i BUR, opierają się więc na jednym wpisie rejestrowym — **odczytane u źródła**, wcześniej był to wniosek ze źródeł wtórnych.

## Kto może skorzystać

**Korekta wobec wcześniejszej wersji tego pliku.** Poprzednio stało tu „Pracodawca zatrudniający co najmniej jednego pracownika". Ustawa tego nie wymaga: art. 126 ust. 2 wprost przewiduje finansowanie dla „podmiotów niezatrudniających pracowników". Warunkiem jest co innego.

Warunek wejścia (art. 125 ust. 8): ze środków KFS mogą korzystać podmioty, które **przez co najmniej 6 miesięcy bezpośrednio przed dniem złożenia wniosku opłacały składki na Fundusz Pracy** albo są z nich zwolnione z mocy prawa.

Wyłączenia (art. 125 ust. 9): publiczne służby zatrudnienia; podmioty z zaległościami podatkowymi, składkowymi albo wpłatami na PFRON, pod zarządem komisarycznym, w likwidacji lub upadłości, albo które rażąco naruszyły umowę o KFS w ciągu 3 lat; podmioty z zaległościami w KRUS lub ubezpieczeniu zdrowotnym; podmioty zbiorowe objęte sądowym zakazem korzystania z pomocy publicznej.

Krąg osób, na których kształcenie idą środki (art. 125 ust. 10): **pracownicy, pracodawcy, osoby fizyczne prowadzące działalność gospodarczą oraz osoby świadczące usługi na podstawie umów cywilnoprawnych.** To potwierdza rozszerzenie o zlecenia, dzieło i JDG — **odczytane u źródła**, wcześniej był to „kierunek zmiany potwierdzony w kilku źródłach".

Co można sfinansować (art. 125 ust. 11): należności dla instytucji realizującej szkolenia, dla instytucji potwierdzającej nabytą wiedzę i umiejętności albo wydającej dokument to potwierdzający, dla instytucji realizującej studia podyplomowe, za badania lekarskie i psychologiczne wymagane do podjęcia kształcenia lub zadań po nim, oraz ubezpieczenie NNW.

Czego nie można (art. 125 ust. 12): kształcenia sfinansowanego z innych środków publicznych; kształcenia, które pracodawca musi zapewnić z odrębnych przepisów; **działań rozpoczętych przed dniem podpisania umowy o finansowanie**. Ten trzeci punkt jest praktycznie najważniejszy dla IRIN: szkolenie nie może wystartować przed podpisaniem umowy klienta ze starostą.

## Poziomy dofinansowania i limity kwotowe

**Dwa limity działają jednocześnie, oba są ruchome.** Podstawa: art. 126 ust. 1-3 (s. 60-61).

| Kto | Udział KFS w kosztach | Podstawa |
|---|---|---|
| Podmiot niezatrudniający pracowników albo zatrudniający **nie więcej niż 9 osób** w przeliczeniu na pełny wymiar czasu pracy w dniu złożenia wniosku | **do 90 %** | art. 126 ust. 2 |
| Pozostałe podmioty | **do 70 %** | art. 126 ust. 1 |

Oba przepisy mówią „**do**" i oba dokładają ten sam pułap kwotowy: **nie więcej niż 200 % przeciętnego wynagrodzenia w danym roku kalendarzowym dla wskazanego we wniosku uczestnika**. Procent nie jest więc gwarantowany, tylko maksymalny — starosta ustala zakres finansowania w uzgodnieniu z wnioskodawcą (§ 5 ust. 4 rozporządzenia).

Drugi limit, roczny na wnioskodawcę (art. 126 ust. 3) — **zależy od zatrudnienia, nie od priorytetu**; wcześniejsza wersja tego pliku wiązała krotności z priorytetem, co jest nieprawdą:

| Zatrudnienie w przeliczeniu na pełny wymiar czasu pracy | Limit roczny |
|---|---|
| brak pracowników albo nie więcej niż 9 osób | 4-krotność przeciętnego wynagrodzenia |
| więcej niż 9, nie więcej niż 49 | 8-krotność |
| więcej niż 49, nie więcej niż 249 | 12-krotność |
| więcej niż 249 | 14-krotność |

Priorytety wydatkowania ustala się corocznie (art. 125 ust. 4); środki mogą pójść poza priorytety dopiero po rozpatrzeniu wniosków, które je spełniają (art. 125 ust. 5). Przy rozpatrywaniu wniosku starosta bierze pod uwagę zgodność z priorytetami, zgodność nabywanych kwalifikacji z potrzebami lokalnego lub regionalnego rynku pracy oraz porównanie kosztu usługi z podobnymi usługami na rynku (art. 125 ust. 13).

**Nie wpisuj kwoty złotowej do materiału zewnętrznego jako liczby stałej.** Przeciętne wynagrodzenie zmienia się z komunikatami Prezesa GUS; podawaj krotność i procent, z odesłaniem do aktualnego komunikatu.

## Wybór realizatora przez wnioskodawcę

Wnioskodawca sam wybiera realizatora, „mając na uwadze zasady konkurencyjności, równego traktowania i przejrzystości" (art. 128 ust. 1). Realizator musi mieć wpis do BUR w zakresie usług szkoleniowych (art. 128 ust. 2, wyżej).

Zakaz powiązań (art. 129): wnioskodawca nie może kupić usługi objętej umową od podmiotu powiązanego z nim osobowo lub kapitałowo — udział w spółce cywilnej lub osobowej, posiadanie udziałów albo co najmniej 5 % akcji, funkcja w organie nadzorczym lub zarządzającym, prokura, pełnomocnictwo, albo inny stosunek budzący uzasadnione wątpliwości co do bezstronności.

Wnioskodawca zobowiązuje się też utrzymać zatrudnienie osoby przeszkolonej przez co najmniej 3 miesiące od ukończenia kształcenia (art. 127 ust. 1); niedotrzymanie tego warunku odcina go od KFS na rok (art. 127 ust. 2).

## Dokumentacja ukończenia szkolenia

**Ustalenie kluczowe dla karty certyfikatu i wcześniej niepotwierdzone.** Przepisy KFS **nie określają treści ani wzoru** dokumentu potwierdzającego ukończenie kształcenia. Wymagają czego innego: żeby taki wzór istniał i został załączony do wniosku.

Rozporządzenie o KFS, § 2 ust. 2 pkt 3 (s. 3): do wniosku wnioskodawca dołącza „wzór dokumentu potwierdzającego ukończenie kształcenia ustawicznego, wystawianego przez realizatora usługi kształcenia ustawicznego, **o ile wzór takiego dokumentu nie jest określony w przepisach powszechnie obowiązujących**".

Rozporządzenie o KFS, § 6 ust. 3 pkt 5 lit. c (s. 4): umowa ze starostą określa dokumenty rozliczeniowe, wśród nich „dokumenty potwierdzające ukończenie kształcenia ustawicznego wystawione przez realizatora usługi kształcenia ustawicznego **oraz wskazanie tematyki tego kształcenia**".

Do wniosku idzie też program kształcenia (§ 2 ust. 2 pkt 2): nazwa kształcenia, liczba godzin na jednego uczestnika, cele kształcenia, plan nauczania i forma zaliczenia albo efekty uczenia się.

**Praktyczny wniosek dla IRIN.** IRIN jako realizator dostarcza klientowi wzór zaświadczenia **przed złożeniem wniosku**, nie po szkoleniu — to załącznik do wniosku, więc wzór musi istnieć zawczasu. Układ graficzny jest po stronie IRIN, bo KFS nie narzuca ani wzoru, ani listy pól.

**Czego to nie rozstrzyga.** Klauzula „o ile wzór nie jest określony w przepisach powszechnie obowiązujących" odsyła do innych przepisów. Dla usług prowadzonych jako Usługa rozwojowa w BUR obowiązuje lista ośmiu elementów treści z Załącznika 4 do Regulaminu BUR (patrz `./bur.md`). Czy szkolenie finansowane z KFS musi być opublikowane jako Usługa rozwojowa w BUR — a więc czy ta lista wiąże zawsze — **z tych trzech aktów nie wynika**: art. 128 ust. 2 wymaga wpisu **realizatora** do rejestru, a nie publikacji karty usługi. Bezpieczna reguła projektowa: zaświadczenie IRIN spełnia listę z Załącznika 4 BUR zawsze, bo wtedy jest poprawne w obu ścieżkach.

## Czy karta usługi w BUR jest wymagana na etapie wniosku KFS

**Nie, na poziomie przepisów krajowych — odczytane u źródła 2026-09-03.** Rozporządzenie o KFS wylicza zamkniętą listę tego, co zawiera wniosek (§ 2 ust. 1) i co się do niego dołącza (§ 2 ust. 2). O realizatorze wniosek podaje nazwę, adres, NIP albo REGON, informację o **wpisie do rejestru PARP w zakresie usług szkoleniowych**, nazwę i liczbę godzin usługi, miejsce przeprowadzenia, koszt na osobę wraz z porównaniem rynkowym oraz brak powiązań z art. 129 (§ 2 ust. 1 pkt 6). **Karta usługi w BUR nie występuje w tej liście ani razu.**

Zastrzeżenie, które zostaje: to ustalenie dotyczy przepisów powszechnie obowiązujących. Poszczególne urzędy pracy publikują własne zasady naboru i ogłaszają w nich „zasady i kryteria wyboru" (§ 3 ust. 1 rozporządzenia), więc konkretny urząd może poprosić o więcej. Sprawdzenie przy pierwszym realnym kliencie: regulamin naboru PUP właściwego dla siedziby tego klienta.

## Co z tego jest prawnie wiążące dla dokumentów IRIN

Dla karty specyfikacji zaświadczenia w warstwie 2 (`/02-szablony-dokumentow/certyfikat.md`):

- **Prawnie obowiązkowe z KFS:** istnienie wzoru dokumentu ukończenia, wystawianego przez realizatora, gotowego przed złożeniem wniosku (§ 2 ust. 2 pkt 3), oraz to, że wystawiony dokument wskazuje tematykę kształcenia (§ 6 ust. 3 pkt 5 lit. c). Nic ponadto — KFS nie narzuca ani pól, ani układu.
- **Prawnie obowiązkowe z BUR** (patrz `./bur.md`): osiem elementów treści z Załącznika 4, Rozdział 2 pkt 3.
- **Warunek prowadzenia linii biznesowej, nie treść dokumentu:** aktualny wpis IRIN do BUR w zakresie usług szkoleniowych (art. 128 ust. 2).

Wszystko poza tym — układ graficzny, kolejność pól, elementy wizualne — jest konwencją organizacyjną IRIN albo swobodnym wyborem projektowym.

## Źródła

Pierwotne, odczytane bezpośrednio 2026-09-03, pliki w `./zrodla/`:

- Ustawa z 20 marca 2025 r. o rynku pracy i służbach zatrudnienia, Dz.U. 2025 poz. 620 — https://dziennikustaw.gov.pl/D2025000062001.pdf
- Rozporządzenie MRPiPS z 25 listopada 2025 r. w sprawie KFS, Dz.U. 2025 poz. 1641 — https://dziennikustaw.gov.pl/D2025000164101.pdf
- Ustawa z 9 listopada 2000 r. o utworzeniu PARP, Dz.U. 2025 poz. 98 — https://dziennikustaw.gov.pl/D2025000009801.pdf

Wtórne, zachowane jako kontekst operacyjny (priorytety i wytyczne roczne, których ustawa nie zawiera):

- [Krajowy Fundusz Szkoleniowy w roku 2026 — kierunkowe wytyczne dla urzędów pracy (WUP Szczecin, PDF)](https://wupszczecin.praca.gov.pl/documents/10240/6350314/KFS+2026+-+Wytyczne+dla+urz%C4%99d%C3%B3w+pracy_aktualizacja+Luty+2026.pdf)
- [Krajowy Fundusz Szkoleniowy — Ministerstwo Rodziny, Pracy i Polityki Społecznej](https://www.gov.pl/web/rodzina/krajowy-fundusz-szkoleniowy-fundusz-pracy)
- [Zostały niemal 2 miesiące do zamknięcia Rejestru Instytucji Szkoleniowych — PARP](https://www.parp.gov.pl/component/content/article/89517:zostaly-niemal-2-miesiace-do-zamkniecia-rejestru-instytucji-szkoleniowych-nie-zwlekaj-wpisz-swoja-firme-do-bazy-uslug-rozwojowych)
- [Uzyskaj wpis do Bazy Usług Rozwojowych — biznes.gov.pl](https://www.biznes.gov.pl/pl/portal/ou712)
