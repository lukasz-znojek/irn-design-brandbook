# Karta specyfikacji — papier firmowy i wizytówka

Ten plik opisuje treść i wymogi papieru firmowego oraz wizytówki IRIN. Nie opisuje layoutu ani grafiki — patrz `/03-pakiet-claude-design/`.

## Luka wejściowa — forma prawna IRIN

**Nie jest tu potwierdzone, jaką formę prawną ma IRIN** (spółka z o.o., spółka akcyjna, inna spółka handlowa, jednoosobowa działalność gospodarcza). To rozstrzyga, który dokładnie przepis i który dokładnie zestaw danych rejestrowych jest prawnie obowiązkowy na papierze firmowym — sekcja niżej opisuje regułę dla spółki kapitałowej (najbardziej rygorystyczny wariant), bo `brandbook.dc.html` (canvas foundera, materiał inspiracyjny, niepotwierdzony) używa w makietach pól "KRS" — co wskazuje na podmiot wpisany do Krajowego Rejestru Sądowego, a nie do CEIDG — ale same wartości w pliku są zerowym placeholderem (`KRS 0000000000`, `NIP 000-000-00-00`), więc nie stanowią rzeczywistych danych rejestrowych IRIN. **Do potwierdzenia przez foundera: forma prawna i rzeczywiste dane rejestrowe (KRS/NIP/adres siedziby), zanim ta karta zostanie użyta do wygenerowania gotowego wzoru z realnymi danymi.**

## Elementy prawnie obowiązkowe (przy założeniu spółki kapitałowej — do potwierdzenia)

Jeśli IRIN jest spółką z ograniczoną odpowiedzialnością, zastosowanie ma **art. 206 Kodeksu spółek handlowych** (dla spółki akcyjnej — analogicznie art. 374 KSH): pisma i zamówienia handlowe składane przez spółkę w formie papierowej i elektronicznej muszą zawierać:
1. firmę spółki, jej siedzibę i adres,
2. oznaczenie sądu rejestrowego, w którym przechowywana jest dokumentacja spółki, oraz numer, pod którym spółka jest wpisana do rejestru (KRS),
3. numer identyfikacji podatkowej (NIP),
4. wysokość kapitału zakładowego.

To dotyczy formalnie **pism i zamówień handlowych** — a więc wprost papieru firmowego. Niedopełnienie tego obowiązku jest zagrożone odpowiedzialnością (grzywna na podstawie KSH) — to nie jest kwestia estetyki, tylko wymóg ustawowy. **Jeśli forma prawna IRIN okaże się inna niż spółka kapitałowa, ta sekcja wymaga ponownego napisania od podstaw, nie tylko podmiany liczb.**

Wizytówka **nie jest** "pismem ani zamówieniem handlowym" w rozumieniu art. 206 KSH — nie podlega temu samemu rygorowi ustawowemu. W praktyce firmy powtarzają na wizytówce część tych danych (nazwa, adres, NIP) jako dobrą praktykę identyfikacyjną, nie jako obowiązek prawny — to należy do konwencji organizacyjnej, nie do tej sekcji.

## Konwencja organizacyjna IRIN

Z `brandbook.dc.html` (do potwierdzenia): papier firmowy zawiera dodatkowo dane kontaktowe (e-mail, telefon) i adres strony (`irin.pl`); wizytówka w formacie 85×55 mm, w wersji awers/rewers. **[do potwierdzenia przez foundera]** jako wiążąca konwencja, a nie tylko obserwacja z materiału inspiracyjnego.

## Swobodny wybór projektowy

Układ graficzny, typografia, kolorystyka w ramach palety IRIN, rozmieszczenie danych na stronie, materiał/gramatura papieru (poza zakresem treści tego repozytorium) — rozstrzyga się w Claude Design.

## Dane wejściowe wymagane przed przekazaniem do Claude Design

Forma prawna IRIN, rzeczywisty adres siedziby, numer KRS lub odpowiednik, NIP, wysokość kapitału zakładowego (jeśli dotyczy), dane kontaktowe do umieszczenia — żadne z nich nie są tu zgadywane.

## Źródła

- [Art. 206 KSH — Kodeks spółek handlowych — lexlege.pl](https://lexlege.pl/ksh/art-206/)
- [Jakie dane spółka z o.o. powinna ujawnić w pismach i umowach? — Infor.pl](https://mojafirma.infor.pl/spolki/213827,Jakie-dane-spolka-z-oo-powinna-ujawnic-w-pismach-i-umowach.html)
