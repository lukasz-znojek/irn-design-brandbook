# Baza Usług Rozwojowych (BUR) — wymogi certyfikacji

Status weryfikacji: sekcje „Karta Usługi”, „Kod usługi” i „Zaświadczenie” poniżej są **odczytane u źródła** - z sześciu plików PDF dostarczonych bezpośrednio przez foundera 2026-09-02 (domeny PARP pozostają zablokowane przez politykę sieciową środowiska Claude Code; szczegóły pomiaru: `./weryfikacja-u-zrodla.md`). Pliki źródłowe: `./zrodla/`. Pozostałe sekcje tego pliku („Warunek wpisu do BUR”, „Ocena usługi po zakończeniu”) nie były przedmiotem tej weryfikacji i nadal pochodzą z wyszukiwania w źródłach wtórnych wykonanego wcześniej - traktuj je z tym samym zastrzeżeniem co dotychczas, dopóki nie zostaną odczytane wprost.

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

## Karta Usługi - obowiązkowe pola

Źródło: **Załącznik nr 2g do Regulaminu Bazy Usług Rozwojowych, „Wzór formularza Karty Usługi wraz z instrukcją jej wypełniania - usługa szkoleniowa”, wersja obowiązująca od 6 lipca 2026 r.** (`./zrodla/zalacznik-2g-karta-uslugi-szkoleniowa_wersja-2026-07-06.pdf`, 76 stron). Regulamin przewiduje siedem wariantów Karty Usługi wg podrodzaju usługi (2a coaching, 2b doradztwo biznesowe, 2c egzamin, 2d mentoring, 2e o charakterze zawodowym, 2f studia podyplomowe, **2g usługa szkoleniowa** - Regulamin BUR § 23, `./zrodla/regulamin-bazy-uslug-rozwojowych_wersja-2026-05-05.pdf`, s. 35); IRIN świadczy usługi szkoleniowe, więc 2g jest właściwym wzorem.

Pola oznaczone w formularzu jako „Pole obowiązkowe” (numeracja jak w załączniku; strony w nawiasie odnoszą się do pliku 2g):
- **1.2 Rodzaj świadczonej usługi**, **1.3 Podrodzaj świadczonej usługi**, **1.4 Forma świadczenia usługi** (s. 2).
- **1.5 Wariant zajęć** - jeden z trzech: zajęcia indywidualne / zajęcia grupowe / zajęcia grupowe z praktyką indywidualną; nie występuje dla formy zdalnej; blokowane do edycji po publikacji usługi (s. 9-10).
- **1.6 Podstawa uzyskania wpisu do BUR**, **1.7 Usługa zamknięta** (s. 11-12).
- **2.1 Tytuł usługi**, **2.2 Kategoria usługi**, **2.3 Podkategoria usługi** (s. 12-13).
- **2.6 Grupa docelowa**, **2.7 Minimalna liczba Uczestników**, **2.8 Maksymalna liczba Uczestników** (s. 16-18).
- **3.1 Cel edukacyjny** wraz z **3.1.4 Efekty uczenia się** (s. 19-37).
- **3.2.1 Efekt usługi oraz kryteria jego weryfikacji**, **3.2.2 Metoda potwierdzenia** (dla celu biznesowego, jeśli wskazany).
- **4.1 Liczba godzin zegarowych usługi** - faktyczna liczba godzin uwzględniająca proces kształcenia i walidację, łącznie z przerwami zgodnie z harmonogramem; blokowane do edycji po publikacji (s. 49).
  - **4.1.1 w tym liczba godzin zajęć praktycznych indywidualnych** - obowiązkowe tylko dla wariantu „zajęcia grupowe z praktyką indywidualną” (s. 50).
  - **4.1.2 w tym liczba godzin zdalnych** - obowiązkowe tylko dla form mieszanych (stacjonarna/zdalna w czasie rzeczywistym połączona ze zdalną) (s. 50).
- **4.2-4.10 Stawka VAT i koszty** (netto/brutto, w tym walidacji i certyfikowania osobno, jeśli dotyczy).
- **5 Lokalizacja usługi** (s. 55).
- **6 Osoby prowadzące** - obowiązkowe, poza formą zdalną; dla osoby prowadzącej usługę: imię i nazwisko, adres e-mail, opis doświadczenia - każde obligatoryjne; dla osoby walidującej analogicznie, z zastrzeżeniem rozdzielności funkcji kształcenia i walidacji (s. 57-61).
- **7 Program i harmonogram usługi**, w tym **7.1 Ramowy program** i **7.2 Harmonogram usługi** (s. 61-65).
- **8 Dane kontaktowe** (s. 68).
- **9 Informacje dodatkowe** jako tytuł sekcji i **9.1 Informacja o materiałach dla uczestników** (s. 69).
- **10 Warunki techniczne** jako tytuł sekcji i **10.1 Warunki techniczne - opis**, **10.2 Kody dostępowe do usługi** (s. 71-72).

Suma godzin w harmonogramie musi być zgodna z liczbą godzin zegarowych zadeklarowaną w karcie (4.1, s. 49). **Status: odczytane u źródła**, `./zrodla/zalacznik-2g-karta-uslugi-szkoleniowa_wersja-2026-07-06.pdf`, 2026-09-02.

## Kod usługi

Regulamin BUR i Załącznik 4 („Zasady funkcjonowania Dostawców Usług”, wersja od 31 marca 2026 r., `./zrodla/zalacznik-4-zasady-funkcjonowania-dostawcow-uslug_wersja-2026-03-31.pdf`) potwierdzają, że każda usługa ma **„numer identyfikacyjny Usługi rozwojowej”** - nadawany przez system BUR i wymagany m.in. na dokumencie księgowym (Zał. 4, Rozdział 2, pkt 2) oraz na zaświadczeniu uczestnika (Zał. 4, Rozdział 2, pkt 3, s. 6-7 - patrz sekcja „Zaświadczenie” niżej). **Żaden z sześciu przejrzanych dokumentów PARP (Regulamin i Załączniki 1, 2g, 3, 4, 5) nie definiuje wewnętrznej struktury tego numeru** - czy i jak dzieli się na segmenty, co oznacza rok/kolejność/typ usługi. Zapis `2025/00817/PPUR` z `brandbook.dc.html` (canvas foundera, materiał inspiracyjny - patrz `/CLAUDE.md`) pozostaje więc **niepotwierdzonym formatem** - nie z powodu braku dostępu do źródła (jak poprzednio), tylko dlatego, że przejrzane dokumenty nie precyzują tej struktury. Praktyczny wniosek jest taki sam jak wcześniej: karta usługi BUR w warstwie 2 nie powinna zakładać żadnej konkretnej struktury numeru - ma wstawiać rzeczywisty numer nadany przez system dla danej usługi, bez próby jego rekonstrukcji czy formatowania.

**Status: odczytane u źródła** - struktura numeru nie jest zdefiniowana w przejrzanych dokumentach, 2026-09-02.

## Ocena usługi po zakończeniu

Po zakończeniu usługi dostawca ma **7 dni** na oznaczenie statusu każdego uczestnika ("ukończył" / "nie ukończył" / "nie uczestniczył") w systemie BUR. Brak aktualizacji w tym terminie skutkuje automatycznym oznaczeniem uczestnika jako "nie uczestniczył", a system nie wygeneruje wtedy ankiety oceniającej usługę. Ankieta oceny obejmuje aspekty merytoryczne i organizacyjne (zgodność z opisem, przydatność treści).

## Zaświadczenie / certyfikat ukończenia usługi

**Rozbieżność wobec wcześniejszego zapisu w tym pliku - rozstrzygnięta źródłem pierwotnym.** Wcześniejsza wersja tej sekcji zakładała istnienie osobnego „Załącznika nr 12 do Regulaminu - wzór Zaświadczenia” (wersja z 1 kwietnia 2025 r., z kopii lustrzanej na `bur-subregion.pl`). W aktualnym Regulaminie BUR (wersja od 5 maja 2026 r.) § 23 „Załączniki” wymienia jako integralną część Regulaminu wyłącznie Załączniki 1-5 - **Załącznika nr 12 już nie ma** (`./zrodla/regulamin-bazy-uslug-rozwojowych_wersja-2026-05-05.pdf`, s. 35). Nowszy dokument wygrywa: obowiązek wystawienia zaświadczenia i jego minimalna treść są dziś częścią **Załącznika 4 „Zasady funkcjonowania Dostawców Usług”, Rozdział 2 „Standardy świadczenia Usług rozwojowych”, pkt 3** (wersja obowiązująca od 31 marca 2026 r., `./zrodla/zalacznik-4-zasady-funkcjonowania-dostawcow-uslug_wersja-2026-03-31.pdf`, s. 6-7) - nie osobnego wzoru graficznego, tylko listy obowiązkowych elementów treści.

Zgodnie z tym przepisem Dostawca Usług **wydaje usługobiorcy zaświadczenie o skorzystaniu z Usługi rozwojowej, zawierające co najmniej**:
1. tytuł Usługi rozwojowej,
2. numer identyfikacyjny Usługi rozwojowej (patrz sekcja „Kod usługi” wyżej - struktura numeru nieokreślona, wstawić rzeczywisty numer z systemu),
3. datę świadczenia Usługi rozwojowej,
4. liczbę godzin Usługi rozwojowej,
5. informację na temat nabytych przez usługobiorcę efektów uczenia się lub innych osiągniętych efektów Usługi rozwojowej,
6. dane usługobiorcy,
7. numer identyfikacyjny wsparcia nadany w systemie teleinformatycznym (ID wsparcia) - dotyczy usług z dofinansowaniem, np. PSF/KFS,
8. kod kwalifikacji w Zintegrowanym Rejestrze Kwalifikacji zgodny z kodem wskazanym w opublikowanej informacji o usłudze - **tylko jeżeli usługobiorca nabył tę kwalifikację**.

Dostawca Usług ma też obowiązek wystawić korektę zaświadczenia w ciągu 7 dni od uzasadnionego wezwania usługobiorcy (ten sam punkt). Żaden z przejrzanych dokumentów nie narzuca układu graficznego zaświadczenia - to lista treści minimalnej, nie wzór wizualny; forma dokumentu (`/02-szablony-dokumentow/certyfikat.md`) pozostaje swobodnym wyborem projektowym w Claude Design.

**Status: odczytane u źródła**, `./zrodla/zalacznik-4-zasady-funkcjonowania-dostawcow-uslug_wersja-2026-03-31.pdf`, s. 6-7, 2026-09-02.

## Co z tego jest prawnie wiążące dla dokumentów IRIN

Prawnie obowiązkowe (sekcje „Karta Usługi”, „Kod usługi”, „Zaświadczenie” - odczytane u źródła 2026-09-02; sekcja „Warunek wpisu do BUR” - nadal ze źródeł wtórnych):
- IRIN musi mieć aktualny wpis do BUR i certyfikat jakości (SUS lub ISO 9001), żeby w ogóle prowadzić tę linię biznesową.
- Karta usługi (wzór 2g - usługa szkoleniowa) musi zawierać wszystkie pola oznaczone jako obowiązkowe w Załączniku nr 2g - pełna lista wyżej. To są pola formularza w systemie PARP, nie materiał do zaprojektowania od nowa w warstwie 2, ale ich obecność w treści dokumentu (np. w karcie usługi drukowanej/PDF do dystrybucji, jeśli IRIN taką tworzy) jest wymogiem, nie wyborem.
- Zaświadczenie uczestnika musi zawierać co najmniej osiem elementów z Załącznika 4, Rozdział 2, pkt 3 - pełna lista wyżej.
- Numer identyfikacyjny usługi na obu dokumentach musi być rzeczywistym numerem nadanym przez system BUR - jego wewnętrzna struktura nie jest nigdzie zdefiniowana, więc nie wolno jej zakładać ani formatować od nowa.

Wszystko poza tym (układ graficzny, kolejność elementów na drukowanej karcie usługi, dodatkowe elementy wizualne) to konwencja organizacyjna IRIN lub swobodny wybór projektowy - nie wynika z regulaminu BUR.

## Źródła

Pierwotne (odczytane bezpośrednio, pliki dostarczone przez foundera 2026-09-02, przechowywane w `./zrodla/`):
- Regulamin Bazy Usług Rozwojowych, wersja obowiązująca od 5 maja 2026 r. - `zrodla/regulamin-bazy-uslug-rozwojowych_wersja-2026-05-05.pdf`
- Załącznik nr 2g do Regulaminu BUR - Karta Usługi, usługa szkoleniowa, wersja obowiązująca od 6 lipca 2026 r. - `zrodla/zalacznik-2g-karta-uslugi-szkoleniowa_wersja-2026-07-06.pdf`
- Załącznik 4 do Regulaminu BUR - Zasady funkcjonowania Dostawców Usług, wersja obowiązująca od 31 marca 2026 r. - `zrodla/zalacznik-4-zasady-funkcjonowania-dostawcow-uslug_wersja-2026-03-31.pdf`
- Załącznik 1 do Regulaminu BUR - Karta Dostawcy Usług, wersja obowiązująca od 1 stycznia 2026 r. - `zrodla/zalacznik-1-karta-dostawcy-uslug_wersja-2026-01-01.pdf` *(dostarczony, nieprzeczytany w tej sesji - poza zakresem pozycji 1-3)*
- Załącznik 3 do Regulaminu BUR - System Oceny Usług Rozwojowych, wersja obowiązująca od 8 lipca 2025 r. - `zrodla/zalacznik-3-system-oceny-uslug-rozwojowych_wersja-2025-07-08.pdf` *(dostarczony, nieprzeczytany w tej sesji)*
- Załącznik 5 do Regulaminu BUR - Standard Usług Zdalnego Uczenia się (SUZ), luty 2021 - `zrodla/zalacznik-5-standard-uslug-zdalnego-uczenia-sie-suz_wersja-2021-02.pdf` *(dostarczony, nieprzeczytany w tej sesji)*

Falsyfikator na przyszłość: żaden z powyższych plików nie jest datowany później niż 6 lipca 2026 r., a odczyt nastąpił 2026-09-02 - sieć PARP pozostała zablokowana przez cały czas trwania sesji (`./weryfikacja-u-zrodla.md`), więc nie sprawdzono, czy między 6 lipca a dniem odczytu PARP opublikowała nowszą wersję Regulaminu lub Załącznika 2g. Publikacja nowszej wersji na `uslugirozwojowe.parp.gov.pl` obala datowanie użyte wyżej.

Wtórne (kontekst ogólny, sekcja „Warunek wpisu do BUR” wyżej - nieodczytane wprost):
- [Baza Usług Rozwojowych (BUR) — co to jest i jak działa — StartujzBUR](https://startujzbur.pl/baza-uslug-rozwojowych-co-to-jest/)
- [Certyfikacja SUS 2.0 — DEKRA](https://www.dekra-certification.com.pl/pl/certyfikacja-sus-2-0/)
- [SUS 3.0 — Standard Usług Szkoleniowo-Rozwojowych — PIFS](https://sus.pifs.org.pl/)
- [Rejestracja w Bazie Usług Rozwojowych z certyfikatem ISO 9001 — Multicert](https://multicert.pl/blog/rejestracja-baza-uslug-rozwojowych-iso-9001/)
- [Standard usługi rozwojowej od 5 maja 2026 r. — najważniejsze zmiany — PARP](https://www.parp.gov.pl/component/content/article/90425:standard-uslugi-rozwojowej-od-5-maja-2026-r-najwazniejsze-zmiany) *(nie pobrano bezpośrednio — domena zablokowana)*
- [Usługa rozwojowa: definicja i co musi zawierać opis usługi w BUR — Scheelite](https://scheelite.eu/usluga-rozwojowa-definicja-bur/)
- [Ocena usługi w BUR: na czym polega i jak wpływa na rynek usług — Scheelite](https://scheelite.eu/ocena-uslugi-w-bur-czym-jest-jak-dziala/)
