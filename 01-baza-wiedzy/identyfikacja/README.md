# identyfikacja/

Zatwierdzone specyfikacje identyfikacji wizualnej IRIN - wartości, nie kompozycja.

- [`paleta-barw.md`](./paleta-barw.md) - obowiązująca paleta „Kaszmir Wyciszony”: 14 kolorów z nazwami, tokenami semantycznymi, zmierzonymi kontrastami WCAG i regułą 80/15/5.
- [`siatka-a4.md`](./siatka-a4.md) - siatka dokumentu A4: 6 kolumn, moduł 25 mm, gutter 4 mm, marginesy i pole treści, wraz ze sprawdzeniem, że siatka fizycznie mieści się na stronie.
- [`typografia.md`](./typografia.md) - Manrope i Inconsolata, dziesięciopoziomowa skala, zasada różnicowania wagą, stan sprawdzenia alfabetu polskiego.
- [`tokeny/palette-irin.json`](./tokeny/palette-irin.json) - wszystkie trzy powyższe w formie maszynowej: kolory, skala typograficzna, siatka.

Granica wobec warstwy 3: tutaj żyją **wartości** (który hex, jaki stopień, jaki moduł), a w `../../03-pakiet-claude-design/` **kompozycja** - jak z tych wartości zbudować stronę. Layout, grafika i dobór elementów nadal powstają wyłącznie w Claude Design.

Czego tu jeszcze nie ma: zasady użycia logotypu (minimalny rozmiar, przestrzeń ochronna, zakazane użycia) leżą nadal w `../../03-pakiet-claude-design/format-paczki.md`, w sekcji „Logotyp”. Są tej samej kategorii co pliki wyżej i tą samą logiką mogłyby tu trafić.

Materiał odrzucony przy wyborze palety leży w `../../_robocze/paleta-v2/` i nie jest źródłem prawdy.
