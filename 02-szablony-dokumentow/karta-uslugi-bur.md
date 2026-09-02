# Karta specyfikacji — karta usługi BUR

Ten plik opisuje treść i wymogi drukowanej/PDF karty jednej usługi rozwojowej BUR (odrębny dokument dystrybucyjny, obok właściwej Karty Usługi publikowanej w systemie `uslugirozwojowe.parp.gov.pl`). Nie opisuje layoutu ani grafiki — patrz `/03-pakiet-claude-design/`.

## Cel i odbiorca

Materiał prezentujący jedną konkretną usługę szkoleniową zarejestrowaną w BUR — do wysyłki mailem lub dystrybucji klientowi (firmie rozważającej zakup, operatorowi dotacji), zgodnie z zastosowaniem pokazanym w `brandbook.dc.html` (materiał inspiracyjny foundera, nie specyfikacja układu). Treść tego dokumentu **musi być zgodna** z tym, co IRIN faktycznie opublikował w systemie BUR dla danej usługi — to nie jest niezależny opis marketingowy, tylko odbicie zarejestrowanych danych.

## Elementy prawnie obowiązkowe

Wynikają z `/01-baza-wiedzy/prawo/bur.md` — z zastrzeżeniem, że część z nich ma tam status "do potwierdzenia bezpośrednim odczytem regulaminu BUR" (dostęp do domen PARP był zablokowany; lista dokumentów do dostarczenia: `/01-baza-wiedzy/prawo/weryfikacja-u-zrodla.md`, pozycje 1 i 3):

1. **Kod usługi BUR** — unikalny numer nadany usłudze przez system przy publikacji, musi być widoczny na dokumencie i zgodny z rzeczywistym wpisem. Format zaobserwowany w `brandbook.dc.html` (`2025/00817/PPUR`) jest niepotwierdzony — nie zakładać tej struktury jako reguły, wstawiać rzeczywisty kod usługi wygenerowany przez system BUR.
2. **Tytuł i opis usługi** — zgodne z opublikowaną Kartą Usługi.
3. **Efekty uczenia się** — obowiązkowe pole Karty Usługi; muszą się pojawić w dokumencie w formie zgodnej z rejestracją, nie w wersji skróconej zmieniającej sens.
4. **Grupa docelowa** — do kogo kierowana jest usługa; obowiązkowe pole Karty Usługi.
5. **Liczba godzin zegarowych usługi** i — od zmiany Regulaminu BUR z 5 maja 2026 r. — **wariant zajęć** (tam gdzie dotyczy) oraz dane **osób prowadzących** — jeśli dokument podaje wymiar godzinowy czy prowadzącego, musi być zgodny z tym, co zadeklarowano w systemie.

**Status weryfikacji:** lista wynika z `/01-baza-wiedzy/prawo/bur.md`, gdzie jest oznaczona jako oparta na źródłach wtórnych. Przed uznaniem tej karty za zamkniętą specyfikację, warto zweryfikować bezpośrednio w Załączniku nr 2 do Regulaminu BUR, czy nie ma dodatkowych pól obowiązkowych pominiętych tutaj.

## Konwencja organizacyjna IRIN

- Przypisanie usługi do jednej z trzech dziedzin IRIN: Pedagogika, Akademia AI, Pożyczki UE/BGK. Same dziedziny i ich kolory są zatwierdzone (`/01-baza-wiedzy/identyfikacja/paleta-barw.md`, reguła jednego koloru dziedzinowego na dokument), więc karta usługi zawsze niesie dokładnie jedną dziedzinę. **Otwarte do pierwszego zlecenia:** czy przypisanie ma być także wypisane słownie na karcie, czy wystarczy kolor plus nazwa usługi (obserwacja z `brandbook.dc.html`, patrz też `./viewbook.md`); rozstrzyga founder przy pierwszym zleceniu.
- Informacja o powiązaniu z KFS, jeśli usługa kwalifikuje się też do tej ścieżki dofinansowania (patrz `/01-baza-wiedzy/prawo/kfs.md`) — to nie jest pole systemu BUR, tylko dodatkowa informacja, którą IRIN może chcieć umieścić dla klienta.
- Informacja o kwalifikowalności do PSF (Podmiotowy System Finansowania), jeśli usługa jest dostępna w regionie klienta u właściwego operatora (patrz `/01-baza-wiedzy/prawo/psf.md`) — podobnie jak przy KFS, to dodatkowa informacja dla klienta, nie pole systemu BUR. Poziom dofinansowania i limity PSF są regionalne, więc karta nie powinna podawać ich jako liczby stałej — patrz karta produktu PSF.

## Swobodny wybór projektowy

Układ karty, kolejność prezentacji pól, elementy graficzne, sposób wyróżnienia kodu usługi czy efektów uczenia się — rozstrzyga się w Claude Design.

## Dane wejściowe wymagane przed przekazaniem do Claude Design

Konkretna usługa do zaprezentowania (nazwa, kod BUR, opis, efekty uczenia się, grupa docelowa, liczba godzin, wariant zajęć, prowadzący) — dane od foundera / z systemu BUR, nie generowane w tym repozytorium.
