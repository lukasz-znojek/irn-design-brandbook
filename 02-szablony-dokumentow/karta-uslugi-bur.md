# Karta specyfikacji — karta usługi BUR

Ten plik opisuje treść i wymogi drukowanej/PDF karty jednej usługi rozwojowej BUR (odrębny dokument dystrybucyjny, obok właściwej Karty Usługi publikowanej w systemie `uslugirozwojowe.parp.gov.pl`). Nie opisuje layoutu ani grafiki — patrz `/03-pakiet-claude-design/`.

## Cel i odbiorca

Materiał prezentujący jedną konkretną usługę szkoleniową zarejestrowaną w BUR — do wysyłki mailem lub dystrybucji klientowi (firmie rozważającej zakup, operatorowi dotacji), zgodnie z zastosowaniem pokazanym w `brandbook.dc.html` (materiał inspiracyjny foundera, nie specyfikacja układu). Treść tego dokumentu **musi być zgodna** z tym, co IRIN faktycznie opublikował w systemie BUR dla danej usługi — to nie jest niezależny opis marketingowy, tylko odbicie zarejestrowanych danych.

## Elementy prawnie obowiązkowe

Odczytane u źródła 2026-09-02 z Załącznika nr 2g do Regulaminu Bazy Usług Rozwojowych (wersja obowiązująca od 6 lipca 2026 r.) - pełna lista pól z numerami paragrafów i stron: `/01-baza-wiedzy/prawo/bur.md`, sekcja „Karta Usługi”. Skrót dla tej karty specyfikacji:

1. **Kod usługi BUR** (numer identyfikacyjny Usługi rozwojowej) - nadany przez system przy publikacji, musi być widoczny na dokumencie i zgodny z rzeczywistym wpisem. Regulamin BUR nie definiuje wewnętrznej struktury tego numeru - zapis `2025/00817/PPUR` z `brandbook.dc.html` pozostaje niepotwierdzonym formatem; nie zakładać żadnej struktury, wstawiać rzeczywisty numer wygenerowany przez system BUR.
2. **Rodzaj, podrodzaj i forma świadczenia usługi** (poz. 1.2-1.4) oraz **wariant zajęć** (poz. 1.5, nie występuje dla formy zdalnej).
3. **Tytuł, kategoria i podkategoria usługi** (poz. 2.1-2.3).
4. **Grupa docelowa** i minimalna/maksymalna liczba uczestników (poz. 2.6-2.8).
5. **Cel edukacyjny i efekty uczenia się** (poz. 3.1, 3.1.4) - muszą się pojawić w dokumencie w formie zgodnej z rejestracją, nie w wersji skróconej zmieniającej sens.
6. **Liczba godzin zegarowych usługi** (poz. 4.1) i pochodne pola dla wariantów mieszanych/z praktyką indywidualną (poz. 4.1.1-4.1.2).
7. **Lokalizacja usługi** (poz. 5).
8. **Osoby prowadzące** (poz. 6, nie występuje dla formy zdalnej) - imię i nazwisko, adres e-mail, opis doświadczenia dla każdej osoby.
9. **Program i harmonogram usługi** (poz. 7.1-7.2) - suma godzin harmonogramu musi być zgodna z liczbą godzin zegarowych z poz. 4.1.
10. **Dane kontaktowe** (poz. 8) i **warunki techniczne** (poz. 10, dla usług zdalnych/mieszanych).
11. **Informacja o materiałach dla uczestników** (poz. 9.1) - pole obowiązkowe formularza, więc dokument dystrybucyjny nie może go pomijać.

Trzy zastrzeżenia dopisane po odczycie Regulaminu i Załączników 1, 3, 5 (2026-09-06):

- **Wzór 2g dotyczy wyłącznie usługi szkoleniowej.** Regulamin BUR § 23 (s. 35) wymienia siedem wariantów Karty Usługi: coaching, doradztwo biznesowe, egzamin, mentoring, usługa o charakterze zawodowym, studia podyplomowe i usługa szkoleniowa. Lista pól wyżej jest odczytana z wariantu **2g - usługa szkoleniowa** i nie przenosi się na pozostałe sześć. Jeśli IRIN zacznie publikować usługę innego podrodzaju, ta karta specyfikacji wymaga osobnego odczytu właściwego załącznika; wariantów 2a-2f repozytorium nie ma.
- **Karta Usługi jest dokumentem publicznym.** Regulamin § 14 ust. 5 (s. 23): informacje z Karty Usługi są ogólnodostępne; wyjątkiem jest usługa zamknięta, gdzie widzi je tylko adresat i Administrator Regionalny BUR (ust. 6). Dokument dystrybucyjny powtarza więc treść, która i tak jest jawna - to obniża ryzyko rozbieżności, ale też znaczy, że każda nieścisłość jest publicznie sprawdzalna.
- **Usługi zdalne podlegają Standardowi SUZ.** Regulamin § 15 ust. 3 (s. 24). Dla karty usługi zdalnej oznacza to, że opis warunków technicznych (poz. 10) i informacja o materiałach (poz. 9.1) muszą odpowiadać wymaganiom SUZ-3, SUZ-8 i SUZ-11 - patrz `/01-baza-wiedzy/prawo/bur.md`, sekcja „Usługi zdalne”.

**Dostępność - element prawnie obowiązkowy, wcześniej nieujęty w tej karcie.** Regulamin BUR § 11 ust. 1 pkt 3 (s. 18): na wniosek osoby ze szczególnymi potrzebami dostawca zapewnia materiały dydaktyczne dostosowane do jej potrzeb. Regulamin § 15 ust. 1 (s. 24) dodaje, że **potrzeba takiego dostosowania nie może być powodem odmowy usługi**. Karta usługi w wersji dystrybucyjnej powinna więc zawierać informację, jak zgłosić taką potrzebę - inaczej dokument opisuje usługę, do której formalnie nie da się zgłosić wniosku o dostosowanie. Sam kształt dostosowania nie jest w dokumentach PARP określony; odsyłają do art. 6 ustawy z 19 lipca 2019 r., którego treści repozytorium nie ma (**niesprawdzone**, patrz `/01-baza-wiedzy/prawo/weryfikacja-u-zrodla.md`).

## Konwencja organizacyjna IRIN

- Przypisanie usługi do jednej z trzech dziedzin IRIN: Pedagogika, Akademia AI, Pożyczki UE/BGK. Same dziedziny i ich kolory są zatwierdzone (`/01-baza-wiedzy/identyfikacja/paleta-barw.md`, reguła jednego koloru dziedzinowego na dokument), więc karta usługi zawsze niesie dokładnie jedną dziedzinę. **Otwarte do pierwszego zlecenia:** czy przypisanie ma być także wypisane słownie na karcie, czy wystarczy kolor plus nazwa usługi (obserwacja z `brandbook.dc.html`, patrz też `./viewbook.md`); rozstrzyga founder przy pierwszym zleceniu.
- Informacja o powiązaniu z KFS, jeśli usługa kwalifikuje się też do tej ścieżki dofinansowania (patrz `/01-baza-wiedzy/prawo/kfs.md`) — to nie jest pole systemu BUR, tylko dodatkowa informacja, którą IRIN może chcieć umieścić dla klienta.
- **Ocena usługi z BUR na dokumencie: jeśli się ją podaje, to razem z liczbą ankiet.** Załącznik 3 do Regulaminu BUR (wersja od 8 lipca 2025 r.) nie zakazuje powoływania się na oceny we własnych materiałach - przejrzano wszystkie 5 stron, takiego zapisu tam nie ma. Sam system prezentuje jednak uśrednioną ocenę zawsze wraz z liczbą ankiet, na podstawie których ją wyliczono (cz. II pkt 12, s. 5). Podawanie średniej bez tej liczby jest więc dopuszczalne prawnie, a mimo to zabronione jako konwencja IRIN - średnia bez licznika ankiet jest liczbą, której odbiorca nie może zweryfikować. Ocena liczona jest wzorem `0,5*P1 + 0,3*P2 + 0,2*P3`; szczegóły w `/01-baza-wiedzy/prawo/bur.md`, sekcja „Ocena usługi po zakończeniu”.
- Informacja o kwalifikowalności do PSF (Podmiotowy System Finansowania), jeśli usługa jest dostępna w regionie klienta u właściwego operatora (patrz `/01-baza-wiedzy/prawo/psf.md`) — podobnie jak przy KFS, to dodatkowa informacja dla klienta, nie pole systemu BUR. Poziom dofinansowania i limity PSF są regionalne, więc karta nie powinna podawać ich jako liczby stałej — patrz karta produktu PSF.

## Swobodny wybór projektowy

Układ karty, kolejność prezentacji pól, elementy graficzne, sposób wyróżnienia kodu usługi czy efektów uczenia się — rozstrzyga się w Claude Design.

## Dane wejściowe wymagane przed przekazaniem do Claude Design

Konkretna usługa do zaprezentowania (nazwa, kod BUR, opis, efekty uczenia się, grupa docelowa, liczba godzin, wariant zajęć, prowadzący) — dane od foundera / z systemu BUR, nie generowane w tym repozytorium.
