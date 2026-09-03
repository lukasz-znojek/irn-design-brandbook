# PSF — Podmiotowy System Finansowania

> Karta produktu wg `01-baza-wiedzy/_szablony/karta-produktu.md`. Materiał źródłowy: `01-baza-wiedzy/prawo/kontekst-psf-sanitized.md`.
>
> Nazwa mechanizmu: **PSF — Podmiotowy System Finansowania**, zgodnie z terminologią wytycznych dla programów regionalnych EFS+.

## Krótki opis

PSF to popytowy mechanizm dofinansowania usług rozwojowych (m.in. szkoleń) ze środków Europejskiego Funduszu Społecznego Plus, wdrażany regionalnie przez programy wojewódzkie. Uczestnik albo pracodawca wybiera usługę z Bazy Usług Rozwojowych (BUR), a operator wybrany w konkursie przez samorząd województwa rozlicza dofinansowanie.

## Dla kogo

Pracodawcy i przedsiębiorcy oraz — w większości regionów jako osobny strumień — osoby dorosłe uczące się z własnej inicjatywy. Dokładne kryteria kwalifikowalności ustala regulamin naboru właściwego operatora, nie ma tu jednolitej definicji krajowej.

## Zakres wsparcia / co obejmuje

Dofinansowanie usług rozwojowych wpisanych do BUR — w praktyce najczęściej szkoleń, ale zakres usługi w BUR jest szerszy niż samo szkolenie. Konkretny zakres kwalifikowalnych usług i formy świadczenia (stacjonarna/zdalna) zależą od regulaminu operatora.

## Kluczowe warunki i ograniczenia

**PSF nie ma jednolitych parametrów krajowych** — to jest ustalenie z samych wytycznych EFS+, nie luka w tej karcie. Poziom refundacji, limit na uczestnika, limit firmowy i model wypłaty różnią się między regionami kilkukrotnie naraz, w każdym parametrze osobno.

| Warunek | Wartość | Źródło i data odczytu |
|---|---|---|
| Poziom dofinansowania krajowy | brak — ustala regulamin operatora regionalnego | wytyczne EFS+ dla programów regionalnych, https://www.gov.pl/web/fundusze-regiony/wytyczne-na-lata-2021-2027, odczyt 2026-08-10 |
| Limit na uczestnika / na firmę | brak wartości krajowej — regionalna, zmienna | jw. |
| Wybór usługi z BUR | obowiązkowy | jw. |
| Liczba operatorów w regionie | od 1-2 do kilkudziesięciu, zależnie od województwa | jw. |

Do wyceny konkretnej oferty **wymagana jest karta parametrów właściwego operatora regionalnego** — ta karta produktu nie zastępuje jej i nie podaje wartości, których nie ma w wytycznych krajowych.

## Proces / jak skorzystać

1. Ustalenie właściwego operatora dla regionu i strumienia (pracodawcy/przedsiębiorcy albo osoby dorosłe).
2. Sprawdzenie regulaminu naboru danego operatora — w tym limitów, okresu ich liczenia, wymogu karty usługi opublikowanej w BUR w dniu składania wniosku i dopuszczalnych form świadczenia.
3. Złożenie wniosku u operatora, zgodnie z jego trybem (terminy naborów ustala operator, nie ma jednego trybu krajowego).
4. Realizacja usługi wybranej z BUR i rozliczenie wg modelu wypłaty wskazanego przez operatora (dopłata do dostawcy albo refundacja uczestnikowi).

## Aspekty prawne i compliance

- Podstawa: Wytyczne dotyczące realizacji projektów z udziałem środków Europejskiego Funduszu Społecznego Plus w programach regionalnych na lata 2021-2027 (wersja z lipca 2025, obowiązuje od 30.06.2025) — rozdział o PSF nie określa parametrów finansowych, odsyła do instytucji zarządzającej programem regionalnym.
- Decyzja o przyznaniu dofinansowania i jego poziomie należy do operatora regionalnego — komunikacja zewnętrzna nie powinna sugerować gwarancji dofinansowania.
- Wybór usługi z BUR jest warunkiem koniecznym, niezależnie od regionu.
- **Dostawca usługi musi mieć aktywny profil „Dostawcy Usług" w BUR** (konto dostawcy + akceptacja regulaminu — ten sam wymóg, co opisany w `./bur.md`, sekcja „Warunek wpisu do BUR"). To nie jest wymóg specyficzny dla PSF: usługa nie może zostać opublikowana w BUR bez zarejestrowanego za nią dostawcy, więc skoro PSF wymaga usługi z BUR, wymaga też pośrednio dostawcy z BUR. Wpis jest warunkiem **koniecznym, ale niewystarczającym** — możliwość finansowania w konkretnym naborze zależy dodatkowo od kryteriów projektowych i regulaminu operatora regionalnego.
- **Odczytane u źródła 2026-09-03, na przykładzie jednego operatora.** Regulamin wsparcia operatora PSF w województwie świętokrzyskim (Wojewódzki Urząd Pracy w Kielcach, nabór BUR-I/2.1/2026, działanie 10.06, wersja z 29.07.2026, 40 stron, `./zrodla/regulamin-psf-swietokrzyskie-dzialanie-10-06_wersja-2026-07-29.pdf`) **nie wprowadza akredytacji regionalnej ani listy uznanych realizatorów**: słowo „akredytac" nie występuje w nim ani razu (pomiar: `grep -c "akredytac"` na wyciągu tekstowym zwraca 0), a Dostawcę Usług definiuje wyłącznie przez rejestrację w BUR Kartą Dostawcy Usług „w trybie określonym w Regulaminie BUR" (s. 4). Nakłada natomiast cztery obowiązki operacyjne opisane niżej.

## Co operator PSF nakłada na Dostawcę Usług ponad wpis do BUR

Odczytane 2026-09-03 z regulaminu WUP w Kielcach (nabór BUR-I/2.1/2026, działanie 10.06, wersja z 29.07.2026); plik w `./zrodla/`. Numery stron odnoszą się do tego pliku.

| Nr | Obowiązek | Strona | Czym różni się od KFS |
|---|---|---|---|
| 1 | **Karta Usługi wydrukowana z BUR jest załącznikiem do wniosku.** „Przedsiębiorca przedkłada wraz z wnioskiem o dofinansowanie usługi rozwojowej w całości uzupełnioną Kartę Usługi (wydruk z systemu BUR)". | s. 18 | W KFS karta usługi **nie jest** wymagana na etapie wniosku (`./kfs.md`). To jest ta różnica, dla której warto trzymać oba pliki osobno. |
| 2 | **Dostęp monitoringowy do usług zdalnych.** Dostawca „jest zobowiązany do umożliwienia Operatorowi prowadzenia monitoringu usług rozwojowych w formie zdalnej poprzez udzielenie mu dostępu do usługi w terminie nie później niż na 1 dzień przed planowanym terminem jej realizacji", obok Standardu Usług Zdalnego Uczenia się (Zał. 5 do Regulaminu BUR) i załącznika nr 4 do regulaminu operatora. | s. 13 | KFS nie zna analogicznego obowiązku wobec realizatora. |
| 3 | **Uzasadnienie ceny na żądanie.** WUP „ma prawo zażądać dodatkowych uzupełnień i wyjaśnień (…) od Dostawcy Usługi w zakresie racjonalności i wysokości kosztów usługi rozwojowej"; przy cenie powyżej III kwartyla dla podkategorii wnioskodawca dołącza uzasadnienie, a kalkulację „może sporządzić Dostawca Usług" - z porównaniem do co najmniej trzech usług o zbliżonym zakresie. | s. 20, 24 | KFS wymaga porównania rynkowego od wnioskodawcy (§ 2 ust. 1 pkt 6 lit. f rozporządzenia), nie od realizatora. |
| 4 | **Szerszy zakaz powiązań, z wyższym progiem udziałowym.** Niekwalifikowalna jest usługa świadczona przez Dostawcę na rzecz własnych pracowników, przez Dostawcę powiązanego z pracodawcą kapitałowo lub osobowo (**co najmniej 10 % udziałów lub akcji**, funkcje w organach, prokura, pełnomocnictwo, pokrewieństwo i powinowactwo), przez Operatora lub podmiot z nim powiązany, a także wzajemne świadczenie usług o zbliżonej tematyce między Dostawcami. | s. 25-26 | KFS stawia próg na **co najmniej 5 %** akcji (art. 129 pkt 2 ustawy o rynku pracy) i nie wymienia wzajemnego świadczenia usług. **Progi się różnią - nie przenoś jednego na drugi.** |

Żaden z tych czterech obowiązków nie dotyczy wyglądu dokumentu, więc **na karty specyfikacji w warstwie 2 nie wpływa**. Wpływa na to, co IRIN musi umieć dostarczyć klientowi obok samego szkolenia: aktualną Kartę Usługi, dostęp monitoringowy przy zajęciach zdalnych i kalkulację ceny.

## Powiązane dokumenty

- `01-baza-wiedzy/prawo/kontekst-psf-sanitized.md` — pełny materiał źródłowy, w tym lista powtarzalnych mechanizmów regulaminowych do sprawdzenia u operatora.
- `01-baza-wiedzy/prawo/kfs.md` — kanał porównawczy (KFS), z krajowymi, a nie regionalnymi parametrami.
- `01-baza-wiedzy/_szablony/karta-produktu.md` — szablon, wg którego powstała ta karta.

## FAQ

**Czy PSF ma taki sam poziom dofinansowania w całej Polsce?**
Nie. Poziom dofinansowania, limity i model wypłaty ustala każdy operator regionalny osobno — różnice między regionami są kilkukrotne.

**Czy uczestnik może wybrać dowolną usługę rozwojową?**
Tylko usługę wpisaną do BUR, spełniającą dodatkowo wymogi regulaminu konkretnego operatora (np. dopuszczalną formę świadczenia).

**Kto rozlicza dofinansowanie — urząd pracy czy inny podmiot?**
W większości regionów operator to podmiot wybrany w konkursie (agencja rozwoju, izba gospodarcza, fundacja itp.), nie urząd pracy — choć wojewódzki urząd pracy pełni tę rolę w części regionów.

## Źródła (publiczne lub sanitized)

- Wytyczne dotyczące realizacji projektów z udziałem środków EFS+ w programach regionalnych: https://www.gov.pl/web/fundusze-regiony/wytyczne-na-lata-2021-2027
- Regulamin Bazy Usług Rozwojowych, Załącznik nr 4 „Zasady funkcjonowania Dostawców usług": https://www.parp.gov.pl/storage/site/files/1319/Za.-4--Zasady-funkcjonowania-Dostawcw-usug.pdf — podstawa wymogu profilu dostawcy w BUR; treść niezweryfikowana bezpośrednim odczytem (dostęp do domeny zablokowany w sesji, w której powstał ten zapis), ustalenie oparte na syntezie wyników wyszukiwania.
- „Dostawca usług w BUR: definicja, odpowiedzialność i zasady działania" — Scheelite: https://scheelite.eu/dostawca-uslug-bur-definicja/ (źródło wtórne, potwierdza: wpis do BUR jest warunkiem koniecznym, ale niewystarczającym do świadczenia usług współfinansowanych).
- `01-baza-wiedzy/prawo/kontekst-psf-sanitized.md` (materiał źródłowy sanitized, ten sam katalog).

## Notatka o niepewności

- Podstawa ogólnego wymogu wpisu dostawcy do BUR jest ustalona (Regulamin BUR i jego Załącznik nr 4 — patrz Źródła) i nie jest specyficzna dla PSF, tylko wynika z mechaniki samego BUR. **Rozstrzygnięte 2026-09-03 dla jednego operatora** (WUP w Kielcach, województwo świętokrzyskie): bez akredytacji regionalnej, ale z czterema obowiązkami ponad wpis — patrz sekcja „Co operator PSF nakłada na Dostawcę Usług ponad wpis do BUR". **Granica tego ustalenia:** przeczytano regulamin jednego operatora z jednego naboru. Szesnaście województw ma własne regulaminy i własne progi; przed pierwszym klientem z innego regionu ten sam pomiar trzeba powtórzyć na jego regulaminie.
- Aktualność listy operatorów PSF w serwisie BUR — data w nazwie pliku źródłowego jest niepotwierdzona (nie występuje w treści dokumentu); każdy konkretny operator wymaga weryfikacji przy pierwszym kontakcie.
