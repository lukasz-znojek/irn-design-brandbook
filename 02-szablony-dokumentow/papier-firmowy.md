# Karta specyfikacji — papier firmowy i wizytówka

Ten plik opisuje treść i wymogi papieru firmowego oraz wizytówki IRIN. Nie opisuje layoutu ani grafiki — patrz `/03-pakiet-claude-design/`.

## Forma prawna IRIN - rozstrzygnięta

IRIN to **spółka z ograniczoną odpowiedzialnością** (Instytut Rozwoju i Nauki sp. z o.o.) z siedzibą w Kielcach. Potwierdzone przez foundera 2026-09-02; numery KRS, NIP, REGON i adres siedziby są w `/01-baza-wiedzy/firma/kontekst-firmy-sanitized.md`, sekcja „Kto jest dostawcą”, i mogą wejść do gotowego wzoru. Wartości z `brandbook.dc.html` (`KRS 0000000000`, `NIP 000-000-00-00`) były zerowym placeholderem kanwy i nie są danymi IRIN.

Dwie pozycje wymagane przez przepis niżej - oznaczenie sądu rejestrowego i wysokość kapitału zakładowego - **zostały odczytane 2026-09-03 z rejestru KRS** (`api-krs.ms.gov.pl`, odpis pełny, stan z dnia 15.07.2026): **Sąd Rejonowy w Kielcach, X Wydział Gospodarczy Krajowego Rejestru Sądowego**, kapitał zakładowy **40 000,00 zł**. Obie są jawne w KRS, więc ich miejsce w publicznym repozytorium jest tym samym, co KRS, NIP i REGON.

**Falsyfikator:** ponowny odczyt tego samego odpisu pokazujący inną kwotę albo inny wydział - kapitał zakładowy zmienia się uchwałą i wpisem, więc przed każdym zleceniem papieru sprawdza się datę „stan z dnia" w odpisie, a nie datę tego pliku.

## Elementy prawnie obowiązkowe

Skoro IRIN jest spółką z ograniczoną odpowiedzialnością, zastosowanie ma **art. 206 Kodeksu spółek handlowych** (dla spółki akcyjnej — analogicznie art. 374 KSH): pisma i zamówienia handlowe składane przez spółkę w formie papierowej i elektronicznej muszą zawierać:
1. firmę spółki, jej siedzibę i adres,
2. oznaczenie sądu rejestrowego, w którym przechowywana jest dokumentacja spółki, oraz numer, pod którym spółka jest wpisana do rejestru (KRS),
3. numer identyfikacji podatkowej (NIP),
4. wysokość kapitału zakładowego.

To dotyczy formalnie **pism i zamówień handlowych** — a więc wprost papieru firmowego. Niedopełnienie tego obowiązku jest zagrożone odpowiedzialnością (grzywna na podstawie KSH) — to nie jest kwestia estetyki, tylko wymóg ustawowy. **Falsyfikator tej sekcji:** zmiana formy prawnej spółki. Wtedy sekcja wymaga ponownego napisania od podstaw, nie tylko podmiany liczb.

Wizytówka **nie jest** "pismem ani zamówieniem handlowym" w rozumieniu art. 206 KSH — nie podlega temu samemu rygorowi ustawowemu. W praktyce firmy powtarzają na wizytówce część tych danych (nazwa, adres, NIP) jako dobrą praktykę identyfikacyjną, nie jako obowiązek prawny — to należy do konwencji organizacyjnej, nie do tej sekcji.

## Konwencja organizacyjna IRIN

**Zatwierdzone przez foundera 2026-09-02** jako wiążąca konwencja IRIN (wcześniej obserwacja z `brandbook.dc.html`):

- papier firmowy zawiera, poza danymi z art. 206 KSH, dane kontaktowe: adres e-mail, numer telefonu i adres strony internetowej; konkretne wartości przychodzą od foundera przy zleceniu, nie są powielane w warstwie 1;
- wizytówka ma format 85 × 55 mm i dwie strony: awers i rewers; podział treści między strony pozostaje swobodnym wyborem projektowym.

Zmiana tej konwencji wymaga zgody foundera i wpisu tutaj, nie decyzji w Claude Design.

## Swobodny wybór projektowy

Układ graficzny, typografia, kolorystyka w ramach palety IRIN, rozmieszczenie danych na stronie, materiał/gramatura papieru (poza zakresem treści tego repozytorium) — rozstrzyga się w Claude Design.

## Dane wejściowe wymagane przed przekazaniem do Claude Design

Z repozytorium: forma prawna, adres siedziby, KRS, NIP, REGON (`/01-baza-wiedzy/firma/kontekst-firmy-sanitized.md`) oraz - od 2026-09-03 - oznaczenie sądu rejestrowego i wysokość kapitału zakładowego, odczytane z KRS (sekcja wyżej). Od foundera przy zleceniu zostają wyłącznie wartości danych kontaktowych: e-mail, telefon, adres strony - celowo niepowielane w warstwie 1. Żadne z nich nie są tu zgadywane.

## Źródła

- [Art. 206 KSH — Kodeks spółek handlowych — lexlege.pl](https://lexlege.pl/ksh/art-206/)
- [Jakie dane spółka z o.o. powinna ujawnić w pismach i umowach? — Infor.pl](https://mojafirma.infor.pl/spolki/213827,Jakie-dane-spolka-z-oo-powinna-ujawnic-w-pismach-i-umowach.html)
