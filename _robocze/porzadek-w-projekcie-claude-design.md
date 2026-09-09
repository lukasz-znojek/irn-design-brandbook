# Porządek w projekcie Claude Design - pomiar i propozycja

**Data pomiaru: 2026-09-09.** Projekt: „System projektowy IRIN",
`1a22ce64-0e1c-43a6-bd60-eef9241ef73b`, typ `PROJECT_TYPE_DESIGN_SYSTEM`,
zapisywalny. Narzędzie: `DesignSync` (`list_files`, `get_file`, `get_project`).

Ten plik jest **danymi do sprawdzenia, nie ustaleniem**: liczby pochodzą z listy
plików zwróconej przez `list_files`, treść dwóch plików została odczytana,
resztę opisuję po ścieżkach.

## Uwaga metodologiczna: czego ten pomiar nie dowodzi

`list_projects` zwrócił **jeden** projekt („Modernist", cudzy system wzorcowy,
Archivo i akcent `#ec3013` - nie ma nic wspólnego z IRIN) i **nie zwrócił**
projektu IRIN. Nie wyciągam z tego wniosku o mechanizmie: projekt IRIN
sprawdzony wprost przez `get_project` po identyfikatorze
z `.design-sync/config.json` **istnieje i jest zapisywalny**. Dlaczego nie ma
go w liście - **nie zmierzone**. Falsyfikator: gdyby lista była kompletna,
`get_project` na tym identyfikatorze musiałby odmówić; nie odmówił.

## Ile tam czego jest

178 plików. Rozkład zmierzony, nie próbkowany; niesklasyfikowanych 0.

| Grupa | Plików | Udział |
|---|---|---|
| `_archiwum/**` | 68 | 38,2 % |
| `templates/**` (16 szablonów × 4 pliki) | 64 | 36,0 % |
| korzeń projektu | 16 | 9,0 % |
| `uploads/**` | 9 | 5,1 % |
| `components/**` (8 kart) | 8 | 4,5 % |
| `_robocze/**` | 5 | 2,8 % |
| `assets/**` | 3 | 1,7 % |
| `guidelines/**` | 2 | 1,1 % |
| `tokens/**` | 2 | 1,1 % |
| `fonts/**` | 1 | 0,6 % |
| **razem** | **178** | **100 %** |

**Archiwum jest większe od szablonów.** Na każdy plik, który coś w tym systemie
robi, przypada plik, który tylko pamięta, jak było.

## Sześć rzeczy, które są nie tak

### 1. `guidelines/` nie zawiera żadnych wytycznych projektowych

To nie jest bałagan, to defekt funkcjonalny. Katalog ma dwa pliki i oba mówią
o firmie, nie o projektowaniu:

- `guidelines/kontekst-firmy.md`
- `guidelines/kontekst-firmy-sanitized.md`

Cztery kopie specyfikacji (kolor, siatka, typografia, logotyp) i cztery inne
wytyczne leżą w `_archiwum/guidelines-zastapione/` - **osiem plików w archiwum,
zero w miejscu, w którym agent projektowy ich szuka.**

Skutek: zlecenie oparte na tym projekcie nie ma w `guidelines/` ani jednej
liczby o kolorze, siatce, typografii i znaku. Dostaje je wyłącznie przez
`tokens/` i przez cztery dokumenty `irn-design-*` w korzeniu, czyli przez
pliki, których nazwa nie mówi „to jest wytyczna".

Nie wiem, który z dwóch plików kontekstu firmy jest obowiązujący - **nie
zmierzone**, bo różnicy treści nie porównywałem.

### 2. Sprzeczność w `tokens/` - ta sama, którą opisuje `POMIAR.md`

Zmierzone 2026-09-09 (rozdz. 9 `POMIAR.md`): `tokens/palette-irin.json` niesie
paletę **v5.1**, a `tokens/tokens.css` ma **Regalię** w drugim bloku. Dwa pliki
w jednym katalogu, dwie różne palety, i to plik maszynowy jest ten starszy.

Do tego `tokens/tokens.css` wskazuje jako źródło prawdy
`01-baza-wiedzy/identyfikacja/paleta-barw.md` **w repozytorium** - a więc
odesłanie wychodzi z projektu do repozytorium, gdzie od dziś (zadanie 4) stoi
już Regalia. To odesłanie jest teraz poprawne; do 2026-09-09 wskazywało v2.

### 3. Procesu w korzeniu jest więcej niż systemu

W korzeniu projektu leżą pliki, które są zapisem pracy, nie systemem:

- `Prompt - Claude Code 1 pomiar stanu i plan.md`
- `_kontynuacja.md`
- `_robocze/audyt-zgodnosci-2026-09-09.md`
- `_robocze/poprawki-dokumentow-wzorcowych-2026-09-09.md`
- `_robocze/wykonanie-decyzji-2026-09-09.md`
- `_robocze/wykonanie-poprawek-2026-09-09.md`
- `_robocze/diakrytyki-probka.png`

Siedem plików. Każdy z nich był potrzebny w swoim oknie i żaden nie jest
potrzebny do złożenia dokumentu.

### 4. `uploads/` to trzy różne rzeczy w jednym katalogu

- **duplikat znaku:** `uploads/logo_irin_pion.svg`, `_poziom.svg`, `_sygnet.svg`
  wobec tych samych trzech nazw w `assets/`. Czy pliki są identyczne co do
  bajtu - **nie zmierzone**, porównywałem ścieżki, nie treść.
- **zrzuty ekranu:** dwa `draw-*.png` i dwa `pasted-*.png`.
- **robocze markdowny:** `pilotpoprawkidowyslania.md`,
  `szablonyuniwersalnedowyslania.md` - nazwy bez separatorów, treść roboczą.

### 5. Cztery dokumenty, siedem plików, dwa formaty bez reguły

| Dokument | `.html` | `.md` |
|---|---|---|
| `irn-design-brandbook` | jest | jest |
| `irn-design-ksiega-znaku` | jest | jest |
| `irn-design-paleta-kolorow` | jest | jest |
| `irn-design-ksiega-koloru` | jest | **nie ma** |

Trzy dokumenty mają wersję `.md`, czwarty nie. Nie wiem, czy `.md` jest
źródłem, czy odpadem po składaniu `.html` - **nie zmierzone**. Dopóki to nie
jest rozstrzygnięte, przy każdej poprawce trzeba pamiętać o dwóch plikach
i nie ma reguły, która by o tym przypominała.

### 6. Znak niesie 7-8 kB podpisu na 2 kB geometrii

`assets/logo_irin_sygnet.svg` odczytany wprost: zawiera osadzony manifest C2PA
w base64. To samo w repozytorium - `logo_irin_sygnet.svg` ma 9 594 bajty
i jedno wystąpienie `c2pa`, `logo_irin_pion.svg` 15 814, `logo_irin_poziom.svg`
15 725. Geometria to kilkaset bajtów ścieżek; reszta to metadane podpisu.

Nie jest to błąd i nie proponuję tu zmiany: `CLAUDE.md` mówi, że pliki SVG
logotypu są nietykane, a manifest nie zmienia renderu. Zapisuję, bo przy
osadzaniu znaku w każdym z 16 szablonów te bajty jadą razem z nim.

## Trzy drogi do porządku

### A. Porządek na miejscu, pełny

Usunąć albo przenieść 82 pliki (68 archiwum + 5 `_robocze` + 7 procesu
w korzeniu i `uploads`), przywrócić `guidelines/` z repozytorium, złożyć
`tokens/` z jednego źródła, ujednolicić dokumenty do jednego formatu.
Szablony zostają na miejscu.

**Za:** projekt, którego dziś się używa, robi się czysty od razu.
**Przeciw:** to praca w projekcie, który plan i tak zastępuje (zadania 13-16),
czyli w dużej części do wyrzucenia. Usunięcie 68 plików archiwum jest
nieodwracalne, a w nich siedzi pomiar palet v3-v7, którego nie ma nigdzie
indziej.

### B. Nowy projekt, zgodnie z planem (zadania 13-16)

Zasiać nowy projekt z czystego repozytorium, przenieść 16 szablonów, stary
oznaczyć jako archiwum i nie kasować.

**Za:** jedna paleta, jeden kierunek synchronizacji, zero historii; archiwum
przestaje ciążyć, bo zostaje po starej stronie.
**Przeciw:** 64 pliki szablonów trzeba przenieść ręcznie, a to jest ta część
planu, w której najłatwiej coś zgubić. Do momentu zasiewu bałagan zostaje.

### C. Minimum na miejscu teraz, reszta przy zasiewie (rekomendacja)

Trzy ruchy, wszystkie odwracalne, żaden nie kasuje archiwum:

1. **Przywrócić `guidelines/`** - cztery kopie specyfikacji z repozytorium
   (po zadaniach 4-7, czyli po Regalii) plus zasady użycia. To zamyka defekt
   z punktu 1, jedyny, który psuje wynik pracy agenta, a nie tylko wygląd
   drzewa.
2. **Złożyć `tokens/` z jednego źródła** - `palette-irin.json` i `tokens.css`
   wprost z repozytorium, gdzie oba są generowane i sprawdzane bramką. To
   zamyka punkt 2 i znosi sprzeczność v5.1 wobec Regalii.
3. **Zsunąć proces w jedno miejsce** - siedem plików z punktu 3 i dwa robocze
   markdowny z `uploads/` przenieść do `_archiwum/`, bez kasowania.

**Dlaczego to, a nie A:** kasowanie 68 plików w projekcie, który zastępujemy,
to praca do wyrzucenia; a trzy ruchy wyżej mają wartość niezależnie od tego,
czy nowy projekt powstanie za tydzień, czy za miesiąc.

**Falsyfikator tej rekomendacji:** jeżeli zadania 13-16 nie mają się wykonać
(nowy projekt odpada), to A jest całą robotą i trzeba ją zrobić w całości -
wtedy C jest połowicznością, nie oszczędnością.

**Czego C nie robi:** nie rusza 16 szablonów, nie kasuje ani jednego pliku,
nie rozstrzyga formatu dokumentów (`.md` obok `.html`) i nie wybiera między
dwoma plikami kontekstu firmy. To są decyzje, nie porządki.

## Co wymaga Twojej decyzji

1. **Która droga: A, B czy C?** Rekomendacja C.
2. **Który plik kontekstu firmy jest obowiązujący** - `kontekst-firmy.md` czy
   `kontekst-firmy-sanitized.md`? Bez tego nie wiem, który ma jechać dalej,
   a drugi jest wtedy do archiwum.
3. **Czy `.md` obok `.html` w czterech dokumentach jest źródłem, czy odpadem?**
   Jeżeli odpadem, cztery pliki idą do archiwum; jeżeli źródłem, brakuje
   piątego (`irn-design-ksiega-koloru.md`) i trzeba go dopisać.
