# [ID] — [Nazwa programu szkolenia]

> Poziom orientacyjny — nie wklejać wprost do formularza BUR. Przed publikacją wymaga przejścia wewnętrznych bramek jakości IRIN (kontrola limitów dofinansowania, treści programowej i kadry).

Plik programu jest jedynym źródłem prawdy dla liczb usługi: nazwy modułów, godzin, efektów uczenia się i limitów. Karta usługi BUR i materiały sprzedażowe (np. `prezentacja-sprzedazowa.md`) są z niego generowane — żadna liczba usługi nie powinna żyć w dwóch miejscach niezależnie. Limity i poziomy dofinansowania pochodzą dodatkowo z karty produktu właściwego kanału (`01-baza-wiedzy/prawo/kfs.md`, `01-baza-wiedzy/prawo/psf.md`) — to liczby kanału, nie usługi. Sekcję 1 wypełnia się tylko dla programów pod klienta; w programach katalogowych usuń ją.

Inaczej niż pozostałe pliki tej warstwy (np. `karta-uslugi-bur.md`, `certyfikat.md`) — to nie karta specyfikacji, tylko roboczy szablon do wypełnienia dla konkretnego programu; stąd nagłówek z polami do uzupełnienia zamiast nazwy dokumentu.

## Legenda kategorii

Zgodnie z `/CLAUDE.md` każda karta specyfikacji w tej warstwie rozróżnia jawnie trzy kategorie elementów. Pozostałe pliki warstwy 2 robią to osobnymi nagłówkami („Elementy prawnie obowiązkowe" / „Konwencja organizacyjna IRIN" / „Swobodny wybór projektowy"); ten plik, żeby nie przerywać pól do wypełnienia, oznacza je inline tymi samymi trzema kategoriami:

- **[PRAWO]** — element prawnie obowiązkowy: wynika z przepisu albo z regulaminu instytucji finansującej (KFS/PSF/BUR).
- **[IRIN]** — konwencja organizacyjna IRIN: obecnie obowiązująca praktyka firmy, zmienialna decyzją firmy, nie przepisem.
- **[WYBÓR]** — swobodny wybór projektowy albo redakcyjny, bez wymogu formalnego.

## Metryczka **[IRIN]**

| Pole | Wartość |
|---|---|
| ID / wersja | |
| Typ | katalogowy / pod klienta |
| Klient | tylko programy pod klienta |
| Program bazowy | jeśli powstaje z programu katalogowego |
| Dziedzina tematyczna | jedna |
| Status | szkic / w opracowaniu / zatwierdzony / archiwalny |
| Autor / właściciel | |
| Data utworzenia / zmiany | |
| Źródło wejścia | brief, notatka z analizy potrzeb, pomysł własny |

## 1. Kontekst klienta *(tylko programy pod klienta)* **[IRIN]**

- Czym firma się zajmuje, skala, specyfika:
- Zdiagnozowane potrzeby i problemy do rozwiązania:
- Kto ma być szkolony — stanowiska, liczebność, poziom wejściowy:
- Oczekiwania i ograniczenia — terminy, forma, lokalizacja, budżet:
- Cel biznesowy klienta, mierzalny: co ma się zmienić i po czym to poznamy
- Metoda potwierdzenia efektu biznesowego:

## 2. Kanały i finansowanie **[PRAWO]**

| Kanał | Status | Karta produktu / źródło |
|---|---|---|
| PSF — operator, strumień, działanie | | `01-baza-wiedzy/prawo/psf.md` |
| KFS | | `01-baza-wiedzy/prawo/kfs.md` |
| Komercyjny | | — |

Wszystkie ceny w tym dokumencie są **[netto / brutto]**. Podstawa klasyfikacji podatkowej: [wskaż; potwierdza księgowość — patrz `01-baza-wiedzy/firma/kontekst-firmy-sanitized.md`, sekcja o VAT].

### 2a. Parametry wiążące, z których wynika cena **[PRAWO]**

| Parametr | Wartość | Źródło i data odczytu |
|---|---|---|
| Poziom refundacji — bazowy i preferencyjny | | |
| Limit dofinansowania na osobę | | |
| Limit dofinansowania na pojedynczą usługę | | |
| Limity firmowe po wielkościach | | |
| Pułap ceny za osobogodzinę — forma 1 | | |
| Pułap ceny za osobogodzinę — forma 2 | | |

Wkład własny klienta liczony przy poziomie [najniższym, jaki instytucja finansująca dopuszcza], komunikowany jako [widełki].

### 2b. Cennik **[IRIN]**

Godziny w karcie usługi: **[X] godzin zegarowych** — rozpisane w przeliczniku w sekcji 6, nie tutaj.

| Pozycja | Godziny zegarowe | Cena / os. | Cena za osobogodzinę |
|---|---|---|---|
| | | | |
| **Razem** | | | |

Uzasadnienie ceny — dlaczego dokładnie ta liczba, a nie inna:

### 2c. Pakiety **[IRIN]**

| Pakiet | Skład | Wartość | Dofinansowanie | % limitu | Wkład własny |
|---|---|---|---|---|---|
| | | | | | |

Kontrola limitów: dofinansowanie na osobę [ ] wobec limitu [ ] · dofinansowanie za najdroższą pojedynczą usługę [ ] wobec limitu [ ] · pakiet wobec limitu firmowego [ ].

### 2d. Liczebność grupy **[IRIN]**

**Ten plik nie nosi części kosztowej.** Cel przychodowy, budżet trenerski, koszt obsługi terminu, marża i próg rentowności są liczone w wewnętrznych narzędziach finansowych IRIN i nie są częścią tego pliku ani żadnego dokumentu wychodzącego na zewnątrz.

**Minimum do karty usługi: [ ]** — z wewnętrznych parametrów firmy, nie z progu rentowności. Karta z wysokim minimum blokuje realizację mniejszych grup.

Maksimum — najniższa z tych, które występują:

| Źródło | Wartość | Czy wiąże |
|---|---|---|
| limit BUR — 30 uczestników; **nie dotyczy formy „zdalna"** **[PRAWO]** | | |
| regulamin operatora albo naboru **[PRAWO]** | | |
| miejsce i wyposażenie — sala, stanowiska, licencje **[WYBÓR]** | | |
| prowadzący przy tej metodzie pracy **[WYBÓR]** | | |

Brak któregokolwiek twardego źródła zapisz jako `—`. Gdy wszystkie są puste: `brak limitu twardego`, a planowaną liczebność bierz z realnej zapełnialności porównywalnych terminów.

## 3. Cel edukacyjny **[PRAWO]**

Usługa przygotowuje do samodzielnego […]

*(Wariant z egzaminem: „Usługa potwierdza przygotowanie do…". Musi wskazywać działania, do których uczestnik będzie przygotowany.)*

## 4. Grupa docelowa **[PRAWO]**

Konkretnie: funkcje albo stanowiska, doświadczenie, zakres zadań, wymagana wiedza i umiejętności wejściowe.

Warunki uczestnictwa:

## 5. Efekty uczenia się **[PRAWO]**

Czasowniki operacyjne. Każde kryterium z co najmniej jedną metodą z listy zamkniętej.

| # | Efekt uczenia się (uczestnik…) | Kryteria weryfikacji | Metoda walidacji |
|---|---|---|---|
| 1 | | | |
| 2 | | | |

## 6. Ramowy program **[PRAWO]**

Godzina dydaktyczna: 45 minut. Godziny zegarowe w karcie obejmują zajęcia, przerwy i walidację. Układ przerw: [ ].

Moduły sumuj w godzinach dydaktycznych. Walidacji nie dopisuj do tej sumy — ma inną jednostkę i osobny wiersz w przeliczniku poniżej.

| Moduł | Zagadnienia | → efekt nr | T / P | Godz. dyd. |
|---|---|---|---|---|
| 1. | | | | |
| **Zajęcia razem** | | | | |

Walidacja *(odrębna pozycja harmonogramu, koniec ostatniego dnia zajęć — nigdy osobny termin)*: metody z sekcji 5, [ ] godzin zegarowych, prowadzi [osoba z sekcji 9].

### Przelicznik godzin — do pola liczby godzin w karcie **[IRIN]**

| Składnik | Godziny zegarowe |
|---|---|
| Dzień 1 zajęć: [ ] godz. dyd. + [ ] przerw | |
| Dzień [n] | |
| Walidacja | |
| **Razem — do karty** | |

## 7. Metody pracy i warunki organizacyjne **[WYBÓR]**

Formy pracy, podział na grupy, wymagania wobec stanowiska uczestnika, sprzęt, oprogramowanie, kto pokrywa koszt licencji.

## 8. Warianty programu **[WYBÓR]** / **[IRIN]**

| | Wariant 1 | Wariant 2 |
|---|---|---|
| Forma świadczenia w karcie | | |
| Miejsce albo platforma | | |
| Zakres, godziny, dni | | |
| Cena | | |
| Sekcje karty specyficzne dla wariantu | | |

Zakres i efekty uczenia się identyczne we wszystkich wariantach. Odstępstwo wymaga osobnego programu, nie wariantu.

## 9. Kadra **[PRAWO]**

| Rola | Osoba | Doświadczenie lub kwalifikacje z datami | Dokumenty |
|---|---|---|---|
| Prowadzący kształcenie | | | |
| Prowadzący kształcenie — drugi *(jeśli metoda tego wymaga)* | | | |
| Prowadzący walidację *(inna osoba)* | | | |

**Stawek ani budżetu trenerskiego w tej tabeli nie ma i nie dopisuj ich** — to dane finansowe, prowadzone w wewnętrznych narzędziach IRIN, nigdy w dokumencie programowym.

Karta usługi wymaga **dwóch różnych osób**: prowadzącej kształcenie i prowadzącej walidację. Wymyślanie danych osoby, która nie potwierdziła swojego doświadczenia, jest zakazane bez wyjątków — karta jest dokumentem publicznym w usłudze finansowanej ze środków publicznych. Dane robocze kadry (dane kontaktowe, warunki współpracy) trzymaj poza tym plikiem i poza dokumentami wychodzącymi na zewnątrz.

## 10. Materiały dla uczestników **[WYBÓR]**

Wyłącznie materiały odnoszące się do tej usługi.

## 11. Karty usług **[PRAWO]** / **[IRIN]**

Liczba kart: [liczba usług × liczba form świadczenia]. Program jednomodułowy w jednej formie to jedna karta. Plik kart: [ścieżka].

Siatka terminów *(tylko programy wielousługowe)*: [rytm publikacji terminów; terminy jednej osoby nie mogą nachodzić na siebie]. Jeżeli operator dopuszcza jeden wniosek na klienta w naborze, wszystkie terminy potrzebne klientowi muszą być widoczne w BUR w dniu składania wniosku.

## 12. Ryzyka i pozycje otwarte

**Blokujące publikację karty:**

**Do potwierdzenia u źródła:**

## Elementy wizualne

Elementy wizualne i formatowanie tego dokumentu należy stosować zgodnie z aktualnym brandbookiem IRIN.
