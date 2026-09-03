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

**Czego nie sprawdzono:** to nie jest pełny audyt glifów. Znak ź nie wystąpił w renderowanej treści na żadnym kroju, a poszczególne wagi nie były sprawdzane glif po glifie. Falsyfikator: pierwszy realny dokument z pełnym zakresem diakrytyków na wagach 500 i 600 - jeśli tam wszystko się złoży, sprawa jest zamknięta. Do tego czasu wniosek brzmi: **pokrycie potwierdzone w zakresie, w jakim je zmierzono**, a nie „pełne pokrycie na wszystkich wagach".
