# Typografia IRIN - specyfikacja obowiązująca

**Status: ZATWIERDZONA.** Kroje i skala pochodzą z `brandbook.dc.html` (sekcja 04) i nie były na liście rozbieżności wymagających potwierdzenia; poziom H3 został dodany i zatwierdzony przez foundera 2026-09-02. To jest jedyne źródło prawdy dla typografii dokumentów IRIN.

Dane maszynowe: [`tokeny/palette-irin.json`](./tokeny/palette-irin.json), klucz `typografia`.
Kolor: [`paleta-barw.md`](./paleta-barw.md). Siatka: [`siatka-a4.md`](./siatka-a4.md).
Jak typografia wchodzi do zlecenia dla Claude Design: [`../../03-pakiet-claude-design/format-paczki.md`](../../03-pakiet-claude-design/format-paczki.md).

## Kroje

- **Manrope**, wagi 200-800 - krój podstawowy. Nagłówki, korpus, etykiety, nawigacja, liczby prowadzące.
- **Inconsolata**, wagi 300-700 - krój pomocniczy. Wyłącznie dane liczbowe, metadane, kody usług, numery dokumentów.

Oba są darmowe i dostępne przez Google Fonts.

## Zasada systemu: hierarchię buduje waga, nie rodzina

Cała hierarchia powstaje przez zmianę wagi jednego kroju - ExtraLight na display, Bold na drogowskazy wersalikowe, Regular i Medium na korpus. To nie szczegół, a zasada: jedna rodzina eliminuje ryzyko niedopasowania metryk przy tłumaczeniach i przy przelewaniu tekstu. Nie dobieraj trzeciego kroju do żadnego zastosowania.

## Skala obowiązująca

| Poziom | Krój | Waga | Stopień | Interlinia | Tracking |
|---|---|---|---|---|---|
| Display (okładka) | Manrope | 200 | 72 px | 0,92 | -0,03em |
| H1 - rozdział | Manrope | 300 | 40 px | 1,0 | -0,02em |
| H2 - sekcja | Manrope | 600 | 24 px | 1,1 | -0,01em |
| **H3 - podsekcja** | Manrope | 600 | 16 px | 1,3 | 0 |
| Lead akapitu | Manrope | 500 | 16 px | 1,4 | 0 |
| Korpus | Manrope | 400 | 13,5 px | 1,55 | 0 |
| Przypis, metadane | Manrope | 400 | 10 px | 1,5 | 0 |
| Kicker - drogowskaz sekcji | Manrope | 700 | 14 px | 1,2 | 0,22em, wersaliki |
| Liczba prowadząca | Manrope | 800 | 52 px | 0,95 | -0,02em |
| Dane techniczne, kody usług | Inconsolata | 300-700 | 10,5 px | 1,5 | 0 |

Tracking jest ujemny na display i nagłówkach, dodatni na wersalikach. Stopnie podane w pikselach zgodnie z zapisem w kanwie; przy druku przelicz je na punkty w jednym miejscu i konsekwentnie, nie poziom po poziomie.

## Interlinia korpusu a jednostka odstępu 6 mm

Interlinia korpusu wynosi 13,5 px × 1,55 = 20,93 px, czyli **5,54 mm**. Jednostka odstępu z siatki to 6 mm. Te dwie wielkości **nie są ze sobą powiązane i nie muszą być** - jednostka 6 mm wymierza odstępy między blokami, a nie linie bazowe tekstu (patrz [`siatka-a4.md`](./siatka-a4.md), sekcja o jednostce bazowej).

Konsekwencja praktyczna: nie próbuj układać akapitów na siatce 6 mm. Rozjazd wynosi 0,46 mm na linię i narasta do 19 mm na pełnej kolumnie, więc pogoń za wyrównaniem skończy się rozstrzelonymi odstępami między akapitami. Odstępy między blokami wymierzaj jednostką 6 mm, tekst wewnątrz bloku zostaw jego własnej interlinii.

## H3 - jedyny poziom dodany po kanwie

**Zatwierdzony przez foundera 2026-09-02.** Kanwa nie definiowała tego poziomu; H3 to stopień leadu (16 px) z wagą podniesioną z 500 do 600. Ruch zgodny z własną logiką systemu - różnicuje wagą, nie wprowadza nowego stopnia do skali.

Konsekwencja do zapamiętania: **H3 odróżnia się od leadu wyłącznie wagą**, więc te dwa poziomy nigdy nie powinny stać bezpośrednio obok siebie. Jeśli podsekcja musi sąsiadować z leadem, użyj kickera (700 / 14 px / wersaliki), który różni się także rozmiarem i trackingiem.

## Alfabet polski - co zostało sprawdzone, a co nie

**Manrope.** `brandbook.dc.html` pokazuje pełny zestaw ą ć ę ł ń ó ś ź ż wraz z wersalikami, ale tylko na dwóch wagach: 200 i 700. Dodatkowo w renderze wykonanym przy okazji wyboru palety (Chromium, Manrope z Google Fonts) znaki ą ć ę ł ń ó ś ż oraz wersaliki Ł i Ą wyświetliły się poprawnie na wszystkich wagach od 200 do 800.

**Inconsolata.** Kanwa używa tego kroju do opisów zawierających polskie znaki („wąskie", „odwrócona", „pieczęć"), a w renderze tej sesji poprawnie wyświetlił ł, ę i ą. To wystarczające potwierdzenie dla zastosowań, jakie krój ma w systemie - liczby, kody usług, metadane.

**Czego nie sprawdzono w tamtym pomiarze:** nie był to pełny audyt glifów. Znak ź nie wystąpił w renderowanej treści na żadnym kroju, a poszczególne wagi nie były sprawdzane glif po glifie.

### Pomiar maszynowy z 2026-09-06 - pokrycie zamknięte, wygląd nie

Narzędzie: `/_robocze/narzedzia/pokrycie-diakrytykow.py`, uruchomione na `/_robocze/ds-bundle/fonts/fonts.css` (paczka systemu projektowego wgrywana do Claude Design, z fontami osadzonymi jako data URI). Pomiar do powtórzenia jednym poleceniem po każdej zmianie tego pliku.

| Krój | Podzbiory | Oś zmienności `wght` | Pokrycie 18 diakrytyków | Puste glify |
|---|---|---|---|---|
| Manrope | 2 pliki (`latin`, `latin-ext`), razem 39 816 B | 200-800 | **18/18** | brak |
| Inconsolata | 2 pliki (`latin`, `latin-ext`), razem 54 576 B | 200-900 (CSS udostępnia 300-700) | **18/18** | brak |

Trzy wnioski, każdy z osobnym zakresem:

1. **Podstawienie z innego kroju jest w tej paczce niemożliwe.** Każdy z osiemnastu znaków ma odwzorowanie w tablicy `cmap` i realny kontur, więc przeglądarka nie ma powodu sięgać po krój zastępczy. To była główna obawa stojąca za pomiarem 1 z protokołu pilota.
2. **Glify nie mogą się różnić między wagami 400, 500 i 600.** Oba kroje to fonty zmienne z ciągłą osią `wght` - jeden plik na podzbiór, a nie osobny plik na wagę. Nie istnieje więc plik dla wagi 500, w którym mogłoby czegoś brakować, choć jest w wadze 400. Pytanie „czy komplet diakrytyków jest w każdej wadze” dla tej paczki nie jest już pytaniem empirycznym.
3. **Ó i ó są w podzbiorze `latin`, pozostałe szesnaście znaków w `latin-ext`.** Żaden pojedynczy plik nie ma kompletu i tak ma być - przeglądarka składa je po `unicode-range`. Kto zmierzy jeden plik osobno, zobaczy „brakuje 16 znaków” i wyciągnie fałszywy wniosek.

**Czego ten pomiar nie rozstrzyga:** jak glif wygląda przy danej wadze. Czy ogonek przy ą nie ginie w wadze 600, czy kreska nad ź nie zlewa się z literą przy 16 px - to pytania o rysunek, nie o obecność glifu, i odpowiada na nie tylko obejrzenie złożonego tekstu. Pomiar 1 z `/_robocze/pilot-papier-firmowy/protokol-pomiaru.md` zostaje więc otwarty w tej części.

**Falsyfikator:** to samo narzędzie uruchomione na `fonts.css` po zmianie paczki, zwracające „SĄ BRAKI”. Drugi falsyfikator, poza zasięgiem tego pomiaru: kanwa w Claude Design pobierająca font z innego źródła niż ta paczka - wtedy mierzony plik nie jest tym, który się renderuje.

**Uwaga metodyczna z tego pomiaru.** Pierwsze podejście pokazało, że szesnaście glifów Inconsolaty jest pustych. To był artefakt narzędzia, nie wada fontu: Ą, Ć, ż i pozostałe są glifami złożonymi (baza plus znak diakrytyczny), a użyty licznik zapisywał wtedy operację `addComponent` zamiast `moveTo` i liczył zero konturów. Po rozłożeniu składników wynik brzmi 18/18 z konturami. Wniosek ogólny: liczba konturów bez rozkładu glifów złożonych nie jest miarą tego, czy glif jest pusty.

Wniosek zbiorczy dla tego pliku: **pokrycie diakrytyków w paczce systemu projektowego jest kompletne i zmierzone maszynowo (2026-09-06); otwarta zostaje wyłącznie ocena wizualna rysunku znaków przy wagach 500 i 600.**
