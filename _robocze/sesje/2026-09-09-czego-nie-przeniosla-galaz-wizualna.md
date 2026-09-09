# Czego nie przeniosło scalenie gałęzi `claude/irin-visual-identity-vq9ddw`

**Data: 2026-09-09.** Gałąź scalona w całości poza pięcioma plikami, w których
konflikt rozstrzygnięto na rzecz `main`. Ten plik wypisuje **imiennie**, co
zostało po tamtej stronie, żeby nie zginęło po cichu. Treść jest odzyskiwalna
jednym poleceniem:

```bash
git show 961011d:01-baza-wiedzy/identyfikacja/paleta-barw.md
git show 961011d:01-baza-wiedzy/identyfikacja/logotyp.md
```

**Poprawka 2026-09-09, druga tura.** Pierwotnie stało tu odwołanie przez nazwę gałęzi,
`git show origin/claude/irin-visual-identity-vq9ddw:...`. Ta ścieżka **cicho zwraca zły
plik**: gałąź została po scaleniu skasowana, a potem założona od nowa pod tą samą nazwą,
więc polecenie oddaje dzisiejszy stan zamiast odzyskiwanego. Trwałym adresem jest drugi
rodzic scalenia, `961011d` (czyli `7a7fa3d^2`) - commit nie zmienia treści przy żadnym
przełożeniu gałęzi.

## Dlaczego wygrał `main`

Tamta gałąź niesie **równoległą wersję Regalii z 2026-09-04**, nie starą paletę.
Nie jest to więc wybór między aktualnym a nieaktualnym, tylko między dwiema
liniami tej samej palety. Rozstrzygnęły trzy rzeczy:

1. Wersja z `main` jest **wywiedziona z generatora i sprawdzana bramką**
   (228 twierdzeń, 0 rozjazdów); tamta jest pisana ręcznie.
2. Tamta wersja niesie hexy **spoza czternastu barw** oraz wycofany
   `#452430` z palety v2.
3. Dwa z pięciu konfliktów były w plikach **generowanych**
   (`palette-irin.json`, `tokens.css`) - tam ręczne rozstrzyganie konfliktu nie
   ma sensu, poprawne jest wzięcie wersji z `main` i złożenie na nowo.

## Cztery rzeczy warte odzyskania, wypisane imiennie

Żadna z nich nie jest w `main` i żadna nie jest błędem tamtej gałęzi.

1. **`## Osiem dopuszczonych wersji kolorystycznych` znaku** wraz z
   `## Matryca teł · osiem wersji × sześć podłoży` (`logotyp.md`). Dzisiejszy
   `logotyp.md` mówi o wersji domyślnej i odwróconej, czyli o dwóch, i odsyła
   dobór barwy do trzech wierszy tabeli. Osiem wersji na sześciu podłożach to
   rozstrzygnięcie szersze.
2. **`## Przestrzeń ochronna - miara x, teraz policzona`** (`logotyp.md`).
   Dzisiejszy plik podaje `x` jako miarę względną z przeliczeniem na procenty
   szerokości; tamten deklaruje policzoną wartość.
3. **`## Jasne tła nie są wymienne - policzone 2026-09-08`** (`paleta-barw.md`).
   Dzisiejsza specyfikacja mówi „maksymalnie dwa tła na dokument" i traktuje
   Alabaster jako tło karty; tamta ma osobny pomiar różnicy między jasnymi tłami.
4. **`## Wykresy - jedna barwa, cztery stopnie krycia`** (`paleta-barw.md`).
   W `main` nie ma nic o wykresach, a arkusz `_robocze/arkusz-wzorcowy/arkusz-irin.xlsx`
   z pięcioma wykresami **wszedł** tym scaleniem - czyli mamy nośnik bez reguły.

## Co weszło i wymaga sprawdzenia

Dwadzieścia jeden nowych plików, w tym cztery realne nośniki:
`_robocze/pismo-firmowe/pismo-irin.docx`, `_robocze/arkusz-wzorcowy/arkusz-irin.xlsx`,
`_robocze/podpis-mailowy/podpis-mailowy.html` i podgląd układu w PNG.

**Powstały 2026-09-08, czyli przed destylacją z 2026-09-09** - nie sprawdzałem,
czy ich wartości zgadzają się z obowiązującym `palette-irin.json`. Trzy pliki
tekstowe w tych katalogach mają zero hexów spoza palety; **plików binarnych nie
mierzyłem** i to jest pozycja niesprawdzona, nie ustalenie.

Jeden hex do wyjaśnienia: `#1B1B1B` w `_robocze/podpis-mailowy/README.md` -
prawdopodobnie wartość zastępcza dla klientów pocztowych, ale nie sprawdziłem.

## Czego nie wziąłem świadomie

`_robocze/ds-bundle/tokens/tokens-regalia.css` - drugi plik tokenów obok
`tokens.css`. Architektura systemu ma **jedno** źródło maszynowe i jeden arkusz
z niego wywiedziony; drugi plik tokenów jest z tą zasadą sprzeczny niezależnie
od tego, co w nim stoi.
