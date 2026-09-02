# Weryfikacja u źródła: wyniki odczytu dokumentów

Wszystkie ustalenia prawne w tym katalogu miały w dniu 2026-09-02 status roboczy, bo domeny `parp.gov.pl`, `uslugirozwojowe.parp.gov.pl`, `dziennikustaw.gov.pl` i `isap.sejm.gov.pl` były niedostępne z sesji Claude Code. Zgodnie z wymaganiem issue, wynik dla każdej pozycji musi być jawnie wpisany jako **odczytane u źródła** z datą wersji i numerem strony albo **niesprawdzone** z nazwanym powodem. W tej chwili żaden z dokumentów z listy nie został dostarczony do repozytorium jako PDF ani jako fragment z numerem strony, więc wszystkie osiem pozycji pozostają `niesprawdzone`.

**Jak dostarczyć:** PDF do katalogu `01-baza-wiedzy/prawo/zrodla/` (nazwa po polsku, z datą wersji w nazwie) albo wklejony fragment z podaniem nazwy dokumentu i numeru strony. Dokumenty urzędowe są informacją publiczną, więc mogą leżeć w repozytorium. Alternatywa: dopuszczenie tych domen w polityce sieciowej środowiska Claude Code; wtedy odczyt wykona Claude Code sam.

## Lista, w kolejności wpływu na dokumenty IRIN

| Nr | Dokument | Skąd | Status | Powód / wpływ |
|---|---|---|---|---|
| 1 | **Regulamin Bazy Usług Rozwojowych, Załącznik nr 2** (Karta Usługi), wersja obowiązująca w dniu odczytu | `uslugirozwojowe.parp.gov.pl`, sekcja Regulamin i załączniki | **niesprawdzone** | Brak dostępu do domeny PARP i braku dostarczonego PDF/fragmentu; nie zebrano oficjalnie potwierdzonej listy pól obowiązkowych. |
| 2 | **Regulamin BUR, Załącznik nr 12** (Zaświadczenie o zakończeniu udziału w usłudze rozwojowej), wersja od 1 kwietnia 2025 albo nowsza | to samo miejsce; kopia lustrzana wskazana w `bur.md` | **niesprawdzone** | Brak dostępu do wzoru zaświadczenia i brak dostarczonego źródła; nie potwierdzono listy pól dokumentu. |
| 3 | **Regulamin BUR, część o numeracji usług** (albo instrukcja publikacji karty) | to samo miejsce | **niesprawdzone** | Brak dostępu do regulaminu i braku źródła; oficjalny format kodu usługi pozostaje niezweryfikowany. |
| 4 | **Rozporządzenie Ministra Rodziny, Pracy i Polityki Społecznej z 25 listopada 2025 r. w sprawie Krajowego Funduszu Szkoleniowego**, Dz.U. 2025 poz. 1641 | `dziennikustaw.gov.pl/DU/2025/1641` | **niesprawdzone** | Domena Dz.U. niedostępna i brak dostarczonego PDF; wartości 90 % / 70 % oraz warunki rozszerzenia kręgu osób nie zostały zweryfikowane. |
| 5 | **Ustawa z 20 marca 2025 r. o rynku pracy i służbach zatrudnienia**, Dz.U. 2025 poz. 620, rozdział o KFS | `dziennikustaw.gov.pl/D2025000062001.pdf` | **niesprawdzone** | Brak bezpośredniego dostępu do aktu i brak wersji źródłowej; przepis o limicie dofinansowania nie został odczytany wprost. |
| 6 | **Regulamin naboru KFS jednego powiatowego urzędu pracy** (właściwego dla Kielc albo dla pierwszego klienta) | strona PUP | **niesprawdzone** | Brak dostępu do regulaminu właściwego urzędu; nie ustalono, czy karta usługi w BUR jest wymagana na etapie wniosku. |
| 7 | **„Zasady udzielania wsparcia” jednego operatora regionalnego PSF** (region pierwszego klienta) | strona operatora, lista operatorów w serwisie BUR | **niesprawdzone** | Brak dostępu do regionalnych dokumentów i brak źródła; nie potwierdzono dodatkowych kryteriów operatora ponad wpis do BUR. |
| 8 | **Księga Tożsamości Wizualnej marki Fundusze Europejskie 2021-2027**, rozdział o obowiązkach informacyjnych | `gov.pl/web/fundusze-regiony`, promocja | **niesprawdzone** | Brak dostarczonego dokumentu źródłowego; ta pozycja pozostaje warunkowa i nie ma wpływu na dokumenty IRIN, jeśli nie używa się znaku FE. |

Pozycje 1-3 blokują domknięcie dwóch kart warstwy 2 (karta usługi BUR, certyfikat). Pozycje 4-5 nie zamykają kart, ale zmieniają status `kfs.md` na odczyt pierwotny dopiero po dostarczeniu źródła. Pozycje 6-7 dotyczą pierwszego realnego klienta, nie repozytorium. Pozycja 8 jest warunkowa.

## Co się dzieje po odczycie

Dla każdej pozycji Claude Code wpisuje do wskazanego pliku jedno z dwojga: **odczytane u źródła** z datą wersji dokumentu i numerem strony, albo **niesprawdzone** z nazwanym powodem, jeśli dokument okaże się niedostępny także dla foundera. Nie ma trzeciego statusu. Po przejściu pozycji 1-3 sekcje „Status weryfikacji” w `karta-uslugi-bur.md` i `certyfikat.md` przestają być potrzebne i znikają.
