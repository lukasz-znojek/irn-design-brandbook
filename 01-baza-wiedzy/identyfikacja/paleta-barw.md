# Paleta barw IRIN - specyfikacja obowiązująca

**Status: ZATWIERDZONA przez foundera (2026-09-02).** To jest jedyne źródło prawdy dla kolorów IRIN. Nazwa systemu: **Kaszmir Wyciszony** (wariant 2 z siedmiu przedstawionych do wyboru).

Dane maszynowe: [`tokeny/palette-irin.json`](./tokeny/palette-irin.json).
Jak paleta wchodzi do zlecenia dla Claude Design: [`../../03-pakiet-claude-design/format-paczki.md`](../../03-pakiet-claude-design/format-paczki.md).
Siatka A4: [`siatka-a4.md`](./siatka-a4.md). Typografia: [`typografia.md`](./typografia.md). Ten plik opisuje wyłącznie kolor.
Porównanie siedmiu wariantów, pomiar i uzasadnienie wyboru (archiwum, nie źródło prawdy): [`../../_robocze/paleta-v2/palette-options-v2.md`](../../_robocze/paleta-v2/palette-options-v2.md).
Historia pierwszej decyzji z 2026-09-02, zastąpionej tą: [`../../03-pakiet-claude-design/propozycja-palety-i-siatki-do-potwierdzenia.md`](../../03-pakiet-claude-design/propozycja-palety-i-siatki-do-potwierdzenia.md).

## 14 kolorów

System ma dwie warstwy i obie obowiązują naraz: **nazwa koloru** (tożsamość marki, reguła 80/15/5, przypisanie dziedzin) i **token semantyczny** (rola w dokumencie i w interfejsie). Ten sam kolor ma zawsze obie etykiety - Aksamit *jest* tokenem `primary`, nie ma osobnego koloru wiodącego obok Aksamitu.

| Kolor | Token | Hex | Rola | na Kaszmirze | na Muślinie | na Pergaminie |
|---|---|---|---|---|---|---|
| Kaszmir | `surface` | `#FBF8F2` | papier, tło karty i tabeli | nie dotyczy (tło) | - | - |
| Muślin | `background` | `#F6F2E9` | tło strony | - | nie dotyczy (tło) | - |
| Pergamin | `neutral-light` | `#E7DFD2` | tło calloutu, pas nagłówka, etykieta na ciemnym wypełnieniu | - | - | nie dotyczy (tło) |
| Espresso | `neutral-dark`, `text-primary` | `#221A15` | tusz uniwersalny, tekst korpusu, tło sekcji odwróconej | 16,15:1 | 15,32:1 | 12,95:1 |
| Sepia | `text-secondary` | `#5E4E40` | tekst pomocniczy, metadane, przypisy, nagłówki kolumn | 7,50:1 | 7,12:1 | 6,02:1 |
| **Aksamit** | `primary` | `#452430` | kolor wiodący: nagłówki H1/H2, wypełnienie CTA; akcent dziedziny **Pedagogika** | 12,80:1 | 12,14:1 | 10,26:1 |
| **Miedź** | `secondary` | `#7A5638` | kolor wspierający: H3, podtytuły; akcent dziedziny **Akademia AI** | 6,16:1 | 5,85:1 | 4,94:1 |
| **Onyks** | `info` | `#33474F` | nota informacyjna, boks „podstawa prawna”; akcent dziedziny **Pożyczki UE/BGK** | 9,19:1 | 8,72:1 | 7,37:1 |
| Złoto foliowe | `accent` | `#A8874E` | pieczęć, sygnatura, cienka linia ozdobna | 3,17:1 | 3,01:1 | **2,55:1** |
| Werdykt | `success` | `#2E5241` | stan potwierdzony: zatwierdzona karta usługi, zdany egzamin | 8,26:1 | 7,83:1 | 6,62:1 |
| Rubryka | `warning` | `#8A6110` | stan wymagający uwagi: termin naboru, brakujący załącznik | 5,22:1 | 4,95:1 | **4,18:1** |
| Karmin | `error` | `#9E2B2B` | stan błędu: odrzucony wniosek, niespełniony wymóg | 6,99:1 | 6,63:1 | 5,60:1 |
| **Popiół** | `border` | `#938978` | linie tabeli, obrys karty i pola formularza | 3,25:1 | 3,09:1 | **2,61:1** |
| **Patyna** | `link` | `#2F5A63` | odnośnik w treści i w interfejsie | 7,17:1 | 6,80:1 | 5,75:1 |

Wszystkie kontrasty policzone wzorem WCAG 2.1 na luminancji względnej sRGB, przeliczone od nowa 2026-09-03 dla wszystkich trzech teł. Progi: tekst normalny AA 4,5:1, AAA 7:1; element interfejsu i grafika znacząca 3:1.

## Trzy pary poniżej progu - na Pergaminie, nie na Kaszmirze

**Poprzednia wersja tego pliku podawała kontrasty wyłącznie na Kaszmirze i stwierdzała, że w palecie nie ma ani jednej pozycji poniżej progu. To było prawdziwe dla Kaszmiru i nieprawdziwe dla Pergaminu.** Pergamin jest ciemniejszy od Kaszmiru o około 20 % luminancji, więc trzy pary spadają pod próg dokładnie tam, gdzie Pergamin bywa tłem: **wewnątrz calloutu i pod pasem nagłówka**.

| Para | Kontrast na Pergaminie | Próg | Co przestaje działać |
|---|---|---|---|
| Popiół `#938978` | **2,61:1** | 3:1 dla grafiki | linia tabeli i obrys karty wewnątrz calloutu są niewidoczne |
| Złoto foliowe `#A8874E` | **2,55:1** | 3:1 dla grafiki | cienka linia ozdobna na tle calloutu nie przechodzi |
| Rubryka `#8A6110` jako tekst | **4,18:1** | 4,5:1 dla tekstu | ostrzeżenie pisane Rubryką w calloucie nie przechodzi AA |

**Zasada wiążąca, wynikająca z tych trzech liczb:** wewnątrz calloutu i na każdym innym polu, którego tłem jest Pergamin, **nie stosuje się Popiołu jako linii ani Złota foliowego jako kreski ozdobnej, a Rubryki nie używa się jako koloru tekstu**. Obrys wewnątrz calloutu prowadzi się Sepią (6,02:1), kreskę ozdobną Miedzią (4,94:1), a ostrzeżenie pisze się Espresso (12,95:1) z etykietą słowną, bo kolor i tak nigdy nie jest jedynym nośnikiem statusu.

**Czego ta tabela nie rozstrzyga:** kontrastów na tłach spoza palety - na kolorowym zdjęciu, na skanie, na papierze innym niż biały maszynowy. Tam liczy się od nowa, nie przenosi tych liczb.

**Falsyfikator:** ponowne przeliczenie wzorem WCAG 2.1 na `tokeny/palette-irin.json` dające inną wartość niż w tabeli wyżej. Rachunek odtwarza się skryptem liczącym luminancję względną sRGB dla par (token, tło); kolumna „na Kaszmirze” jest w tym pliku od 2026-09-02 i przeliczenie z 2026-09-03 odtworzyło ją co do setnej, co jest kontrolą samej metody.

## Etykieta na wypełnieniu - kolor przepisany, nie dowolny

Kiedy kolor jest tłem przycisku, plakietki albo pieczęci, kolor napisu na nim **nie jest wyborem projektowym**. Obowiązuje ta tabela:

| Wypełnienie | Kolor etykiety | Kontrast |
|---|---|---|
| Aksamit `#452430` | Pergamin `#E7DFD2` | 10,26:1 |
| Miedź `#7A5638` | Pergamin `#E7DFD2` | 4,94:1 |
| Onyks `#33474F` | Pergamin `#E7DFD2` | 7,37:1 |
| Złoto foliowe `#A8874E` | Espresso `#221A15` | 5,09:1 |
| Werdykt `#2E5241` | Pergamin `#E7DFD2` | 6,62:1 |
| Rubryka `#8A6110` | biel `#FFFFFF` | 5,53:1 |
| Karmin `#9E2B2B` | Pergamin `#E7DFD2` | 5,60:1 |

## Reguła proporcji 80/15/5 - obowiązuje bez zmian

- **80% - baza:** Kaszmir (tło karty), Muślin (tło strony), Pergamin (drugie tło neutralne), Espresso (tekst korpusu), Sepia (tekst pomocniczy), Popiół (linie). Wszystko, co nie niesie znaczenia kategoryzującego.
- **15% - sygnał dziedziny:** dokładnie jeden z trzech - Aksamit (Pedagogika), Miedź (Akademia AI), Onyks (Pożyczki UE/BGK) - na dokument. Nie mieszać dwóch kolorów dziedzinowych na jednej stronie.
- **5% - aktywność i honor:** Patyna wyłącznie do odnośników i stanów aktywnych, Werdykt do stanu potwierdzonego, Rubryka do stanu wymagającego uwagi, Karmin do stanu błędu, Złoto foliowe **wyłącznie** jako pieczęć, sygnatura albo cienka linia - nigdy jako tło większej powierzchni.

## Kolor nigdy nie jest jedynym nośnikiem statusu

Po konwersji do skali szarości Werdykt, Rubryka, Karmin i Onyks mają zbliżoną jasność. Każdy status w dokumencie IRIN **musi** mieć etykietę słowną albo ikonę obok koloru. To wymóg dostępności (WCAG 1.4.1 „Użycie koloru”), nie preferencja - i dotyczy tak samo zaświadczeń drukowanych mono, jak ekranu.

## Co dokładnie zmieniło się względem palety z 2026-09-02

Poprzednia paleta miała 12 kolorów; ta ma 14. Żaden kolor nie został usunięty, żadna nazwa nie zniknęła, dwa kolory doszły. Wszystkie hexy są nowe, ale dwanaście z nich to przesunięcia w obrębie tego samego koloru, a nie inne barwy.

| Kolor | Było | Jest | Na czym polega zmiana |
|---|---|---|---|
| Kaszmir | `#F2ECE1` | `#FBF8F2` | papier rozjaśniony i odsycony, żeby karta wyraźniej odcinała się od strony |
| Muślin | `#F7F3EA` | `#F6F2E9` | tło strony przygaszone o włos, w parze ze zmianą wyżej |
| Pergamin | `#E4DACB` | `#E7DFD2` | rozjaśniony, mniej żółty |
| Espresso | `#1E1611` | `#221A15` | minimalnie rozjaśniony; nadal najciemniejszy kolor palety |
| Sepia | `#5B4837` | `#5E4E40` | odsycona, mniej rudy |
| Aksamit | `#4A1D26` | `#452430` | odsycony i przesunięty od bordo ku śliwce; spokojniejszy |
| Miedź | `#8C5026` | `#7A5638` | odsycona, bardziej brązowa niż rudo-pomarańczowa |
| **Onyks** | `#1B2B26` | `#33474F` | **istotna zmiana**: z prawie-czerni na łupkowy błękit. Powód: stary Onyks miał wobec Espresso kontrast 1,05:1, czyli był nieodróżnialny od zwykłego tekstu i nie niósł żadnego sygnału. Nowy ma 1,76:1 wobec Espresso - to nadal niewiele w luminancji, ale barwa jest teraz jawnie inna (chłodny łupek wobec ciepłej czerni), więc różnicę widać okiem. |
| Złoto foliowe | `#B58540` | `#A8874E` | pogłębione. Powód: stare złoto dawało 2,79:1 na papierze, czyli **nie przechodziło progu 3:1** dla linii i ikon. Nowe daje 3,17:1, więc wolno go użyć jako cienkiej kreski, a nie tylko plamy. |
| Werdykt | `#2F4A32` | `#2E5241` | przesunięty od zieleni butelkowej ku morskiej |
| **Rubryka** | `#D9AC4A` | `#8A6110` | **zmiana roli, nie tylko odcienia**: było jasne złoto używane jako tło z ciemnym tekstem, jest ciemny bursztyn używany jako tło z tekstem białym albo jako kolor tekstu na papierze. Powód: stara Rubryka nie nadawała się na tekst (kontrast 1,7:1 na papierze), więc token `warning` nie miał czym pisać. |
| Karmin | `#AC151F` | `#9E2B2B` | przygaszony, mniej sygnalizacyjny |
| **Popiół** | *nie istniał* | `#938978` | **kolor nowy**. Powód: wcześniej linie tabeli rysowało się pełnym Espresso, więc każda kreska miała wagę ramki i tabela nie miała hierarchii linii cienkiej i grubej. |
| **Patyna** | *nie istniał* | `#2F5A63` | **kolor nowy**. Powód: wcześniej odnośnik i komunikat błędu były fizycznie tym samym kolorem (Karmin, kontrast wzajemny 1,00:1), więc czytelnik nie mógł ich odróżnić inaczej niż z kontekstu zdania. |

**Dwie nazwy nowe, zatwierdzone przez foundera (2026-09-02):** „Popiół” (`border`) i „Patyna” (`link`). Trzymają się konwencji pozostałych dwunastu - materiał albo barwnik, jak Kaszmir, Aksamit, Sepia, Karmin, Miedź, Onyks - a „Patyna” wiąże się dodatkowo znaczeniowo z Miedzią. Obie nazwy są obowiązujące na równi z pozostałymi dwunastoma.

**Jedno ryzyko, które zostaje w tej palecie:** Patyna (`#2F5A63`) i Onyks (`#33474F`) mają kontrast wzajemny 1,28:1. Jeśli odnośnik trafi do wnętrza boksu informacyjnego rysowanego Onyksem, oba kolory się zleją. Zabezpieczenie: odnośnik wewnątrz boksu `info` zawsze z podkreśleniem.
