# Baza Usług Rozwojowych (BUR) — wymogi certyfikacji

Status weryfikacji: ustalenia poniżej pochodzą z wyszukiwania w źródłach wtórnych (portale branżowe, strony certyfikujące) wykonanego 2026-09-02. Próba bezpośredniego pobrania oficjalnych dokumentów PARP (regulamin BUR, załączniki, wzór zaświadczenia) **nie powiodła się dwukrotnie**: rano domeny PARP były zablokowane przez proxy sesji; wieczorem, po otwarciu sieci przez foundera, serwery `serwis-uslugirozwojowe.parp.gov.pl` i `www.parp.gov.pl` odpowiadały stroną zabezpieczenia antybotowego (Incapsula), której narzędzia sesji nie przechodzą. Pliki trzeba pobrać w zwykłej przeglądarce i wrzucić do `./zrodla/` (lista w `./weryfikacja-u-zrodla.md`). Z wyszukiwarki wiadomo dodatkowo, że PARP opublikowała zmianę Załączników nr 2 do Regulaminu BUR **od 6 lipca 2026 r.**, więc wersja z 5 maja 2026 r. przywołana niżej nie jest już najnowsza. Poniższe ustalenia są więc podsumowaniami wtórnymi, nie odczytem pierwotnego tekstu regulaminu czy załączników. Falsyfikator: bezpośredni odczyt aktualnego Regulaminu BUR i jego załączników (linki niżej) różniący się od poniższego podsumowania — **do wykonania, gdy dostęp do domeny PARP będzie możliwy, przed uznaniem czegokolwiek poniżej za wiążącą specyfikację treści dokumentu**.

## Co to jest BUR

Baza Usług Rozwojowych to internetowy rejestr podmiotów świadczących usługi rozwojowe (szkoleniowe, doradcze, coachingowe, e-learningowe), współfinansowane ze środków publicznych, prowadzony przez Polską Agencję Rozwoju Przedsiębiorczości (PARP). Podstawa prawna rejestru: rozporządzenie Ministra Rozwoju i Finansów z dnia 29 sierpnia 2017 r. w sprawie rejestru podmiotów świadczących usługi rozwojowe. Bieżące zasady działania samej bazy (poza rejestrem) określa **Regulamin Bazy Usług Rozwojowych** — dokument aktualizowany kilkukrotnie w ciągu roku (znalezione wersje: obowiązująca od 1 stycznia 2026 r., zmieniona od 13 marca 2026 r. i od 5 maja 2026 r.) — co oznacza, że szczegóły proceduralne poniżej trzeba sprawdzać w wersji regulaminu obowiązującej w dniu tworzenia konkretnego dokumentu, nie zakładać, że pozostają stałe.

## Warunek wpisu do BUR

Aby zostać dostawcą usług w BUR, podmiot (IRIN) musi:
1. Uzyskać certyfikat jakości uznawany przez PARP — najczęściej wymieniane: **Standard Usług Szkoleniowo-Rozwojowych (SUS 2.0 lub nowszy SUS 3.0)** albo **ISO 9001**.
2. Założyć konto dostawcy w systemie BUR (`uslugirozwojowe.parp.gov.pl`).
3. Opublikować **Kartę Usługi** dla każdej oferowanej usługi rozwojowej — dopiero po publikacji usługa otrzymuje status widoczny w wyszukiwarce BUR.

Wpis do BUR jest bezpłatny; kosztem po stronie IRIN jest uzyskanie i utrzymanie certyfikatu jakości.

**Powiązanie z KFS:** od 1 stycznia 2026 r. wpis do BUR jest też warunkiem prowadzenia szkoleń finansowanych z Krajowego Funduszu Szkoleniowego — patrz `./kfs.md`. Dla IRIN oznacza to jeden wspólny wymóg rejestrowy dla obu ścieżek szkoleniowych, nie dwa osobne.

**Powiązanie z PSF:** dla Podmiotowego Systemu Finansowania (PSF, patrz `./psf.md`) potwierdzone jest, że **usługa** musi być wybrana z BUR — warunek konieczny mechanizmu PSF niezależnie od regionu. Wpis **dostawcy** do BUR (konto + regulamin, jak w sekcji wyżej) jest tu wymagany pośrednio, tą samą drogą co dla każdej usługi w BUR — bo usługa nie może być opublikowana bez zarejestrowanego za nią dostawcy (Regulamin BUR, Załącznik nr 4 „Zasady funkcjonowania Dostawców usług"; źródła w `./psf.md`). To nie jest osobny, PSF-specyficzny przepis analogiczny do KFS — wynika z ogólnej mechaniki BUR. **Status: do potwierdzenia pozostaje** tylko węższe pytanie, czy poszczególni operatorzy regionalni PSF nakładają na dostawcę dodatkowe kryteria ponad ten bazowy wpis.

## Karta Usługi — obowiązkowe pola

Z podsumowań instrukcji PARP (Załącznik nr 2 do Regulaminu BUR) obowiązkowe elementy Karty Usługi obejmują co najmniej: tytuł usługi, opis usługi, efekty uczenia się, grupę docelową. Od zmiany regulaminu z 5 maja 2026 r. dochodzą dodatkowo: pole "Liczba godzin zegarowych usługi" (godzina zegarowa staje się jedyną obowiązującą miarą czasu trwania usługi w BUR), pola dot. liczby godzin praktycznych indywidualnych i godzin zdalnych w usługach mieszanych, dane osób prowadzących (uzupełniane już na etapie publikacji karty) oraz — dla większości podrodzajów usług poza doradztwem biznesowym i usługami zdalnymi — pole określające wariant zajęć. Suma godzin w harmonogramie musi być zgodna z liczbą godzin zegarowych zadeklarowaną w karcie.

**Status: lista pól potwierdzona w kilku niezależnych źródłach wtórnych, ale nie zweryfikowana wprost w treści Załącznika nr 2 — traktuj jako punkt wyjścia do karty specyfikacji w `/02-szablony-dokumentow/karta-uslugi-bur.md`, do potwierdzenia przy bezpośrednim dostępie do dokumentu PARP.**

## Kod usługi

System BUR nadaje każdej opublikowanej usłudze unikalny kod/numer. W pliku `brandbook.dc.html` (canvas foundera, materiał inspiracyjny — patrz `/CLAUDE.md`) pojawia się przykładowy zapis `2025/00817/PPUR` przy makiecie karty usługi BUR. **To jest obserwacja z materiału inspiracyjnego, nie potwierdzony oficjalny format kodu** — nie udało się zweryfikować struktury tego numeru (znaczenia segmentów) w źródłach dostępnych w tej sesji z powodu zablokowanego dostępu do domeny PARP. Do potwierdzenia przed wpisaniem jako wymóg do jakiejkolwiek karty specyfikacji.

## Ocena usługi po zakończeniu

Po zakończeniu usługi dostawca ma **7 dni** na oznaczenie statusu każdego uczestnika ("ukończył" / "nie ukończył" / "nie uczestniczył") w systemie BUR. Brak aktualizacji w tym terminie skutkuje automatycznym oznaczeniem uczestnika jako "nie uczestniczył", a system nie wygeneruje wtedy ankiety oceniającej usługę. Ankieta oceny obejmuje aspekty merytoryczne i organizacyjne (zgodność z opisem, przydatność treści).

## Zaświadczenie / certyfikat ukończenia usługi

Regulamin BUR przewiduje oficjalny wzór dokumentu — **Załącznik nr 12 do Regulaminu, "Zaświadczenie o zakończeniu udziału w usłudze rozwojowej"** (wersja obowiązująca od 1 kwietnia 2025 r., zgodnie ze znalezionym plikiem). **Nie udało się pobrać treści tego wzoru** w tej sesji (domena hostująca dokument jest zablokowana przez proxy) — dokładna lista pól wymaganych na zaświadczeniu nie jest tu potwierdzona. Z podsumowań wtórnych wynika, że dokument potwierdzający ukończenie usługi musi wskazywać osiągnięte efekty uczenia się (lub inne efekty usługi) i jednoznacznie identyfikować usługę oraz uczestnika; dokumentację potwierdzającą ukończenie stanowią też listy obecności potwierdzone przez osobę prowadzącą oraz — dla usług zdalnych — raporty logowań.

**Status: do potwierdzenia bezpośrednim odczytem Załącznika nr 12, zanim karta specyfikacji certyfikatu (`/02-szablony-dokumentow/certyfikat.md`, zadanie 10) uzna którekolwiek pole za prawnie obowiązkowe na tej podstawie.**

## Co z tego jest prawnie wiążące dla dokumentów IRIN

Prawnie obowiązkowe (na podstawie ustaleń powyżej, z zastrzeżeniem statusu weryfikacji):
- IRIN musi mieć aktualny wpis do BUR i certyfikat jakości (SUS lub ISO 9001), żeby w ogóle prowadzić tę linię biznesową.
- Karta usługi musi zawierać pola wymagane przez system BUR (tytuł, opis, efekty uczenia się, grupa docelowa, godziny zegarowe i pozostałe pola wymienione wyżej) — to są pola formularza w systemie PARP, nie materiał do zaprojektowania od nowa w warstwie 2, ale ich obecność w treści dokumentu (np. w karcie usługi drukowanej/PDF do dystrybucji, jeśli IRIN taką tworzy) jest wymogiem, nie wyborem.
- Zaświadczenie uczestnika musi identyfikować usługę, uczestnika i osiągnięte efekty uczenia się — dokładna forma pól czeka na potwierdzenie wzoru z Załącznika nr 12.

Wszystko poza tym (układ graficzny, kolejność elementów na drukowanej karcie usługi, dodatkowe elementy wizualne) to konwencja organizacyjna IRIN lub swobodny wybór projektowy — nie wynika z regulaminu BUR.

## Źródła

- [Baza Usług Rozwojowych (BUR) — co to jest i jak działa — StartujzBUR](https://startujzbur.pl/baza-uslug-rozwojowych-co-to-jest/)
- [Certyfikacja SUS 2.0 — DEKRA](https://www.dekra-certification.com.pl/pl/certyfikacja-sus-2-0/)
- [SUS 3.0 — Standard Usług Szkoleniowo-Rozwojowych — PIFS](https://sus.pifs.org.pl/)
- [Rejestracja w Bazie Usług Rozwojowych z certyfikatem ISO 9001 — Multicert](https://multicert.pl/blog/rejestracja-baza-uslug-rozwojowych-iso-9001/)
- [Standard usługi rozwojowej od 5 maja 2026 r. — najważniejsze zmiany — PARP](https://www.parp.gov.pl/component/content/article/90425:standard-uslugi-rozwojowej-od-5-maja-2026-r-najwazniejsze-zmiany) *(nie pobrano bezpośrednio — domena zablokowana w tej sesji)*
- [Usługa rozwojowa: definicja i co musi zawierać opis usługi w BUR — Scheelite](https://scheelite.eu/usluga-rozwojowa-definicja-bur/)
- [Ocena usługi w BUR: na czym polega i jak wpływa na rynek usług — Scheelite](https://scheelite.eu/ocena-uslugi-w-bur-czym-jest-jak-dziala/)
- [(WZÓR) Zaświadczenie o zakończeniu udziału w usłudze rozwojowej — Załącznik nr 12 do Regulaminu BUR](https://bur-subregion.pl/wp-content/uploads/2025/04/6.6_Zal.-nr-12-do-regulaminu_zaswiadczenie-o-zakonczeniu-udzialu-w-usludze_obowiazuje-od-1.04.2025-PDF.pdf) *(nie pobrano bezpośrednio — domena zablokowana w tej sesji, treść niezweryfikowana)*
