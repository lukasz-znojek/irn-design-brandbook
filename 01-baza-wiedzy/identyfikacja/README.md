# identyfikacja/

Zatwierdzone specyfikacje identyfikacji wizualnej IRIN - wartości, nie kompozycja.

- [`paleta-barw.md`](./paleta-barw.md) - obowiązująca paleta **„Regalia”**: siedem barw nośnych, siedem funkcjonalnych, cztery tinty 12 procent, kontrasty przeliczone 2026-09-04, reguła 80/15/5. Zastąpiła paletę „Kaszmir Wyciszony” 2026-09-03.
- [`siatka-a4.md`](./siatka-a4.md) - siatka dokumentu A4: 6 kolumn, moduł 25 mm, gutter 4 mm, marginesy i pole treści, wraz ze sprawdzeniem, że siatka fizycznie mieści się na stronie.
- [`typografia.md`](./typografia.md) - Manrope i Inconsolata, dziesięciopoziomowa skala, zasada różnicowania wagą, stan sprawdzenia alfabetu polskiego.
- [`logotyp.md`](./logotyp.md) - trzy pliki źródłowe z proporcjami, minimalne rozmiary, przestrzeń ochronna i cztery wiążące zakazy modyfikacji znaku.
- [`tokeny/palette-irin.json`](./tokeny/palette-irin.json) - wszystkie powyższe w formie maszynowej: kolory, skala typograficzna, siatka, logotyp.

Granica wobec warstwy 3: tutaj żyją **wartości** (który hex, jaki stopień, jaki moduł), a w `../../03-pakiet-claude-design/` **kompozycja** - jak z tych wartości zbudować stronę. Layout, grafika i dobór elementów nadal powstają wyłącznie w Claude Design.

Komplet: kolor, siatka, typografia i logotyp. Wszystkie cztery są zatwierdzone i żadnej z nich nie powtarza już `../../03-pakiet-claude-design/format-paczki.md`.

Materiał odrzucony przy wyborze palety leży w `../../_robocze/paleta-v2/` i nie jest źródłem prawdy.
