# PSF — Podmiotowy System Finansowania — materiał źródłowy, wersja sanitized

> Wersja bezpieczna do publicznego repozytorium, opracowana z wewnętrznego materiału roboczego. To jest **materiał źródłowy do dalszej pracy**, nie ostateczna karta prawna. Zobacz też `01-baza-wiedzy/prawo/psf.md` — kartę produktu opartą na tym materiale.

> **Uwaga o nazwie:** zlecenie tego zadania posługiwało się skrótem „PFS". Materiał źródłowy i terminologia urzędowa używają skrótu **PSF (Podmiotowy System Finansowania)** — to prawidłowa nazwa mechanizmu. Ten plik i powiązana karta produktu przyjmują PSF jako rozstrzygnięcie tej rozbieżności.

## Dlaczego parametrów nie ma w tym pliku

**PSF nie ma parametrów krajowych.** Wytyczne dotyczące realizacji projektów z udziałem środków Europejskiego Funduszu Społecznego Plus w programach regionalnych (wersja z lipca 2025, obowiązuje od 30.06.2025, odczyt 2026-08-10) poświęcają PSF jeden rozdział o dwóch podrozdziałach: zasady ogólne i kontrole projektów. Rozdział ten **nie określa** ani maksymalnego poziomu dofinansowania, ani minimalnego wkładu własnego, ani limitów kwotowych, ani sposobu liczenia pułapu ceny. Wytyczne zawierają klauzulę, że za zasady wykraczające poza ich zakres odpowiada właściwa instytucja zarządzająca programem regionalnym.

Krajowego podręcznika PSF nie ma. Funkcję tę pełnią regionalne zasady udzielania wsparcia i regulaminy naborów.

Adres wytycznych: https://www.gov.pl/web/fundusze-regiony/wytyczne-na-lata-2021-2027

Rozpiętość między regionami jest kilkukrotna w każdym z parametrów naraz — w poziomie refundacji, limicie na uczestnika, limicie firmowym i modelu wypłaty. Żadnej z tych wartości nie da się przyjąć z innego województwa: każda pochodzi z regulaminu operatora właściwego dla regionu.

## Co jest wspólne dla wszystkich regionów

Tylko konstrukcja: podejście popytowe z obowiązkowym wyborem usługi z BUR, dystrybucja przez operatora, adresaci (pracodawcy, przedsiębiorcy, pracownicy, osoby dorosłe uczące się z własnej inicjatywy), reguły kontroli projektów. Narzędziem quasi-wspólnym jest porównywarka cen w BUR.

## Kto jest operatorem

Operatorami są w przeważającej większości **podmioty wybrane w konkursach**, nie urzędy pracy: agencje rozwoju regionalnego, izby gospodarcze, fundacje, parki technologiczne, spółki szkoleniowe. Wojewódzki urząd pracy występuje jako operator w mniejszości regionów, czasem tylko dla jednego strumienia wsparcia.

Liczba operatorów różni się skrajnie: w części regionów jeden lub dwa, w innych kilkadziesiąt.

**W większości regionów PSF jest rozdzielony na dwa strumienie** — dla pracodawców i przedsiębiorców oraz dla osób dorosłych uczących się z własnej inicjatywy — z osobnymi operatorami, osobnymi regulaminami i osobnymi parametrami.

Punkty startu do znalezienia operatora dla regionu:
- lista operatorów i partnerów PSF w serwisie informacyjnym BUR (plik PDF; jego nazwa wskazuje datę, ale w treści dokumentu daty nie ma — traktować jako niepotwierdzoną i weryfikować aktualność u operatora przy pierwszym kontakcie),
- strony regionalne PARP dotyczące PSF w poszczególnych województwach,
- portal funduszy europejskich właściwy dla województwa.

Adres listy odczytany 2026-08-10: https://serwis-uslugirozwojowe.parp.gov.pl/images/BUR_serwis_info/LISTY%20OPERATOROW/LISTA%20OPERATOROW_PARTNEROW_SERWIS%20BUR_23_03_2026.pdf

## Powtarzalne mechanizmy warte sprawdzenia w regulaminie operatora

Nie są wspólne dla wszystkich operatorów, ale powtarzają się na tyle często, że warto ich szukać wprost.

- **Limit na pojedynczą usługę** obok limitu na osobę — wyznacza maksymalną cenę jednej usługi.
- **Okres liczenia limitów** — nabór czy cały okres projektu; różnica decyduje o tym, czy uczestnik może wrócić po kolejne usługi.
- **Liczba wniosków na jeden numer identyfikacji podatkowej w naborze** — jeśli jeden, cały pakiet usług musi wejść do wniosku od razu, z terminami wszystkich usług wskazanymi z góry.
- **Minimalne wyprzedzenie startu usługi wobec złożenia wniosku**, czas weryfikacji wniosku i okno realizacji od umowy wsparcia — te trzy liczby razem określają, jakie terminy w ogóle mają sens.
- **Wymóg karty usługi opublikowanej w dniu składania wniosku** — jeśli występuje, nabór bez gotowej karty jest poza zasięgiem niezależnie od dostępnej alokacji.
- **Dopuszczalne formy świadczenia** — część operatorów wyklucza formy asynchroniczne i wymaga dostępu do zajęć na żywo z wyprzedzeniem.
- **Podstawy poziomu preferencyjnego** — zwykle więcej niż jedna (charakter usługi, cecha uczestnika, branża albo specjalizacja regionalna) i zwykle się nie sumują.
- **Model wypłaty** — refundacja oznacza, że uczestnik wykłada całość i czeka na zwrot; suma terminów rozliczenia, weryfikacji i wypłaty jest realnym kosztem finansowym po jego stronie.
- **Wykluczenia** — szkolenia obowiązkowe z mocy prawa są zwykle niekwalifikowalne.
- **Wymogi dokumentu wydawanego uczestnikowi** — bywają szersze niż minimum wymagane przez BUR.

## Notatka o sanitizacji

Źródło: wewnętrzny materiał roboczy o PSF, przetworzony 2026-09-02.

Usunięto lub uogólniono:
- **odwołania do wewnętrznego systemu/skilla** — ścieżki takie jak `../assets/szablon-karty-operatora.md`, `przed-publikacja.md`, `cena-pulap.md`, `wymogi-bur.md`, `../SKILL.md` — to elementy innego, wewnętrznego narzędzia sprzedażowego, którego nie ma w tym repozytorium,
- **wzorzec rejestru operatorów** — usunięto pustą tabelę do wewnętrznego prowadzenia listy operatorów po regionach; to narzędzie robocze firmy, nie wiedza merytoryczna o PSF, i nie wnosiło treści do dokumentu publicznego,
- **wskazówkę „architektura jednej karty usługi na poziom"** — to wewnętrzna konwencja tworzenia dokumentów sprzedażowych IRIN, nie cecha samego mechanizmu PSF.

Zachowano w całości: opis konstrukcji PSF, źródła rządowe, adresy stron i mechanizmy regulaminowe — są to informacje publiczne albo ogólnobranżowe, nie zawierają nazw klientów, kwot ani warunków handlowych.

Poprawiono nazwę skrótu z „PFS" (błędnie użytego w zleceniu) na **PSF**, zgodnie z materiałem źródłowym i terminologią urzędową (Podmiotowy System Finansowania).
