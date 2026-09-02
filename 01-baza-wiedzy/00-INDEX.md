# 00-INDEX — baza wiedzy IRIN

Ten plik jest punktem wejścia do warstwy 1. Zawiera odnośniki do wszystkich plików w `firma/`, `prawo/` i `uslugi/`, wraz z jednozdaniowym opisem każdego z nich.

## _szablony/
Szablony do pisania kart tej warstwy, nie dokumentów wydawanych na zewnątrz.

- [`karta-produktu.md`](_szablony/karta-produktu.md) — szablon karty pojedynczego produktu/kanału finansowania albo wsparcia.

## identyfikacja/
Zatwierdzone specyfikacje identyfikacji wizualnej: wartości, nie kompozycja.

- [`identyfikacja/paleta-barw.md`](./identyfikacja/paleta-barw.md) - obowiązująca paleta „Kaszmir Wyciszony”: 14 kolorów z nazwami i tokenami semantycznymi, zmierzone kontrasty WCAG, reguła 80/15/5, przypisanie trzech dziedzin.
- [`identyfikacja/siatka-a4.md`](./identyfikacja/siatka-a4.md) - siatka A4: 6 kolumn, moduł 25 mm, gutter 4 mm; ze sprawdzeniem dopasowania do strony i rozstrzygnięciem roli jednostki bazowej 6 mm (jednostka odstępu między blokami, nie siatka linii bazowych tekstu).
- [`identyfikacja/typografia.md`](./identyfikacja/typografia.md) - Manrope 200-800 i Inconsolata, dziesięciopoziomowa skala, zasada różnicowania wagą zamiast rodziną.
- [`identyfikacja/logotyp.md`](./identyfikacja/logotyp.md) - logotyp: trzy warianty z proporcjami odczytanymi z plików źródłowych, minimalny rozmiar 18 mm / 90 px, przestrzeń ochronna x, cztery wiążące zakazy modyfikacji.
- [`identyfikacja/tokeny/palette-irin.json`](./identyfikacja/tokeny/palette-irin.json) - wszystkie cztery specyfikacje maszynowo.

## firma/

- [`firma/kontekst-firmy.md`](./firma/kontekst-firmy.md) — pełna nazwa i forma prawna IRIN, siedziba w Kielcach, rok założenia 2023, struktura zespołu, trzy linie biznesowe i planowany portal szkoleń.
- [`firma/kontekst-firmy-sanitized.md`](./firma/kontekst-firmy-sanitized.md) — uzupełnienie o mechanikę nieopisaną w karcie wyżej: dane rejestrowe dostawcy, modele rozliczenia dofinansowania, granica compliance dot. wkładu własnego.

## prawo/

- [`prawo/kfs.md`](./prawo/kfs.md) — Krajowy Fundusz Szkoleniowy: podstawa prawna po reformie 2026, wymóg wpisu realizatora do BUR, limity dofinansowania (zmienne rok do roku).
- [`prawo/bur.md`](./prawo/bur.md) — Baza Usług Rozwojowych: warunek wpisu (certyfikat jakości), obowiązkowe pola karty usługi, kod usługi, zaświadczenie ukończenia — część ustaleń oznaczona jako do potwierdzenia z powodu zablokowanego dostępu do domen PARP w tej sesji.
- [`prawo/pozyczki-ue-bgk.md`](./prawo/pozyczki-ue-bgk.md) — regulacje pośrednictwa w pozyskiwaniu dotacji UE i pożyczek BGK dla MŚP: dlaczego IRIN (jako doradca, nie strona umowy z BGK) nie podlega rejestrowi pośredników kredytowych KNF ani obowiązkowi znaku Fundusze Europejskie.
- [`prawo/psf.md`](./prawo/psf.md) — Podmiotowy System Finansowania (PSF): brak parametrów krajowych, wszystko ustala regulamin operatora regionalnego.
- [`prawo/kontekst-kfs-sanitized.md`](./prawo/kontekst-kfs-sanitized.md) — materiał źródłowy uzupełniający `kfs.md`: priorytety wydatkowania 2026, limity roczne wg wielkości firmy, checklista załączników wniosku.
- [`prawo/kontekst-psf-sanitized.md`](./prawo/kontekst-psf-sanitized.md) — materiał źródłowy, na którym oparta jest `psf.md`.
- [`prawo/weryfikacja-u-zrodla.md`](./prawo/weryfikacja-u-zrodla.md) - lista ośmiu dokumentów pierwotnych do dostarczenia przez foundera albo do odczytu po odblokowaniu domen PARP i Dziennika Ustaw; przy każdym: co odczytać i które zdanie się zmieni.

## uslugi/

- [`uslugi/aplikacje-sprzedazowe.md`](./uslugi/aplikacje-sprzedazowe.md) — aplikacja dla przedstawicieli handlowych: narzędzie wewnętrzne (lead-y, prowizje, raportowanie sprzedaży obu linii), nie produkt zewnętrzny.
- [`uslugi/portal-szkolen.md`](./uslugi/portal-szkolen.md) — planowany portal sprzedaży szkoleń online: model hybrydowy (sprzedaż miejsc + realizacja zdalna), bez pełnej platformy LMS; portal jeszcze nie istnieje.
