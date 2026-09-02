# 00-INDEX — baza wiedzy IRIN

Ten plik jest punktem wejścia do warstwy 1. Docelowo zawiera odnośniki do wszystkich plików w `firma/`, `prawo/` i `uslugi/`, wraz z jednozdaniowym opisem każdego z nich. Kolejność uzupełniania — patrz `/PLAN.md`.

## _szablony/
Szablony do pisania kart tej warstwy, nie dokumentów wydawanych na zewnątrz.

- [`karta-produktu.md`](_szablony/karta-produktu.md) — szablon karty pojedynczego produktu/kanału finansowania albo wsparcia.

## firma/
Kontekst działalności IRIN (linie biznesowe, model organizacyjny) — docelowa karta `kontekst-firmy.md` do uzupełnienia (patrz `/PLAN.md`, pozycja 1).

- [`kontekst-firmy-sanitized.md`](firma/kontekst-firmy-sanitized.md) — dane dostawcy, modele rozliczenia dofinansowania i granica compliance wkładu własnego; materiał wejściowy dla docelowej karty.

## prawo/
Przepisy i regulacje dotyczące KFS, PSF/BUR oraz usług pożyczkowych UE/BGK.

- [`psf.md`](prawo/psf.md) — karta produktu: Podmiotowy System Finansowania (PSF).
- [`kontekst-kfs-sanitized.md`](prawo/kontekst-kfs-sanitized.md) — materiał źródłowy o KFS (limity, priorytety 2026, ścieżka wniosku); wejście dla docelowej karty `kfs.md` (`/PLAN.md`, pozycja 2).
- [`kontekst-psf-sanitized.md`](prawo/kontekst-psf-sanitized.md) — materiał źródłowy o PSF (regionalna zmienność parametrów, mechanizmy regulaminowe); podstawa `psf.md`.
- `kfs.md`, `bur.md` — do uzupełnienia (`/PLAN.md`, pozycje 2-3).

## uslugi/
Wytyczne dotyczące poszczególnych usług IRIN (aplikacje sprzedażowe, portal szkoleń) — do uzupełnienia.
