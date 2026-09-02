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

## Konwencja organizacyjna IRIN

- Przypisanie usługi do jednej z trzech dziedzin IRIN: Pedagogika, Akademia AI, Pożyczki UE/BGK. Same dziedziny i ich kolory są zatwierdzone (`/01-baza-wiedzy/identyfikacja/paleta-barw.md`, reguła jednego koloru dziedzinowego na dokument), więc karta usługi zawsze niesie dokładnie jedną dziedzinę. **Otwarte do pierwszego zlecenia:** czy przypisanie ma być także wypisane słownie na karcie, czy wystarczy kolor plus nazwa usługi (obserwacja z `brandbook.dc.html`, patrz też `./viewbook.md`); rozstrzyga founder przy pierwszym zleceniu.
- Informacja o powiązaniu z KFS, jeśli usługa kwalifikuje się też do tej ścieżki dofinansowania (patrz `/01-baza-wiedzy/prawo/kfs.md`) — to nie jest pole systemu BUR, tylko dodatkowa informacja, którą IRIN może chcieć umieścić dla klienta.
- Informacja o kwalifikowalności do PSF (Podmiotowy System Finansowania), jeśli usługa jest dostępna w regionie klienta u właściwego operatora (patrz `/01-baza-wiedzy/prawo/psf.md`) — podobnie jak przy KFS, to dodatkowa informacja dla klienta, nie pole systemu BUR. Poziom dofinansowania i limity PSF są regionalne, więc karta nie powinna podawać ich jako liczby stałej — patrz karta produktu PSF.

## Swobodny wybór projektowy

Układ karty, kolejność prezentacji pól, elementy graficzne, sposób wyróżnienia kodu usługi czy efektów uczenia się — rozstrzyga się w Claude Design.

## Dane wejściowe wymagane przed przekazaniem do Claude Design

Konkretna usługa do zaprezentowania (nazwa, kod BUR, opis, efekty uczenia się, grupa docelowa, liczba godzin, wariant zajęć, prowadzący) — dane od foundera / z systemu BUR, nie generowane w tym repozytorium.
