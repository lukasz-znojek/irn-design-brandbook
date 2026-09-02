# 00-INDEX — baza wiedzy IRIN

Ten plik jest punktem wejścia do warstwy 1. Zawiera odnośniki do wszystkich plików w `firma/`, `prawo/` i `uslugi/`, wraz z jednozdaniowym opisem każdego z nich.

## _szablony/
Szablony do pisania kart tej warstwy, nie dokumentów wydawanych na zewnątrz.

- [`karta-produktu.md`](_szablony/karta-produktu.md) — szablon karty pojedynczego produktu/kanału finansowania albo wsparcia.

## identyfikacja/
Zatwierdzone specyfikacje identyfikacji wizualnej: wartości, nie kompozycja.

- [`identyfikacja/paleta-barw.md`](./identyfikacja/paleta-barw.md) - obowiązująca paleta „Kaszmir Wyciszony”: 14 kolorów z nazwami i tokenami semantycznymi, zmierzone kontrasty WCAG, reguła 80/15/5, przypisanie trzech dziedzin.
- [`identyfikacja/tokeny/palette-irin.json`](./identyfikacja/tokeny/palette-irin.json) - te same dane maszynowo, wraz ze skalą typograficzną i siatką A4.

## firma/

- [`firma/kontekst-firmy.md`](./firma/kontekst-firmy.md) — pełna nazwa IRIN, trzy linie biznesowe i planowany portal szkoleń; model organizacyjny i historia firmy oznaczone jako brak danych, do potwierdzenia przez foundera.
- [`firma/kontekst-firmy-sanitized.md`](./firma/kontekst-firmy-sanitized.md) — uzupełnienie o mechanikę nieopisaną w karcie wyżej: dane rejestrowe dostawcy, modele rozliczenia dofinansowania, granica compliance dot. wkładu własnego.

## prawo/

- [`prawo/kfs.md`](./prawo/kfs.md) — Krajowy Fundusz Szkoleniowy: podstawa prawna po reformie 2026, wymóg wpisu realizatora do BUR, limity dofinansowania (zmienne rok do roku).
- [`prawo/bur.md`](./prawo/bur.md) — Baza Usług Rozwojowych: warunek wpisu (certyfikat jakości), obowiązkowe pola karty usługi, kod usługi, zaświadczenie ukończenia — część ustaleń oznaczona jako do potwierdzenia z powodu zablokowanego dostępu do domen PARP w tej sesji.
- [`prawo/pozyczki-ue-bgk.md`](./prawo/pozyczki-ue-bgk.md) — regulacje pośrednictwa w pozyskiwaniu dotacji UE i pożyczek BGK dla MŚP: dlaczego IRIN (jako doradca, nie strona umowy z BGK) nie podlega rejestrowi pośredników kredytowych KNF ani obowiązkowi znaku Fundusze Europejskie.
- [`prawo/psf.md`](./prawo/psf.md) — Podmiotowy System Finansowania (PSF): brak parametrów krajowych, wszystko ustala regulamin operatora regionalnego.
- [`prawo/kontekst-kfs-sanitized.md`](./prawo/kontekst-kfs-sanitized.md) — materiał źródłowy uzupełniający `kfs.md`: priorytety wydatkowania 2026, limity roczne wg wielkości firmy, checklista załączników wniosku.
- [`prawo/kontekst-psf-sanitized.md`](./prawo/kontekst-psf-sanitized.md) — materiał źródłowy, na którym oparta jest `psf.md`.

## uslugi/

- [`uslugi/aplikacje-sprzedazowe.md`](./uslugi/aplikacje-sprzedazowe.md) — aplikacja dla przedstawicieli handlowych: narzędzie wewnętrzne (lead-y, prowizje, raportowanie sprzedaży obu linii), nie produkt zewnętrzny.
- [`uslugi/portal-szkolen.md`](./uslugi/portal-szkolen.md) — planowany portal sprzedaży szkoleń online: model hybrydowy (sprzedaż miejsc + realizacja zdalna), bez pełnej platformy LMS; portal jeszcze nie istnieje.
