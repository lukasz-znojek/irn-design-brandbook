# Dostęp do projektu Claude Design i dwie równoległe linie palety

Notatka z 2026-09-09. Powstała przy sprawdzaniu, czy sesja może poprawiać pliki w projekcie
Claude Design. Zawiera dwa ustalenia: zmierzone uprawnienia i znalezioną przy tym linię
palety, której `CLAUDE.md` opisuje niepoprawnie.

## Uprawnienia sesji do projektu `1a22ce64-0e1c-43a6-bd60-eef9241ef73b`

Zmierzone komendami, nie wywnioskowane. Projekt nazywa się „System projektowy IRIN",
typ `PROJECT_TYPE_DESIGN_SYSTEM`.

| Operacja | Wynik | Dowód |
|---|---|---|
| `DesignSync get_project` | `canEdit: true` | odpowiedź metody |
| `DesignSync list_files` | 180 ścieżek | pełna lista |
| `DesignSync get_file` | pełna treść | `guidelines/paleta-barw.md`, `tokens/tokens.css` |
| `DesignSync finalize_plan` | `planId` zwrócony | dla ścieżki nieistniejącej |
| `DesignSync write_files` | **`written: 1`** | plik odczytany zwrotnie |
| `DesignSync delete_files` | **HTTP 403** `permission_denied` | „bulk delete requires project ownership when called without a turn fence; **this project is owned by another user**" |
| `DesignSync list_projects` | **nie pokazuje tego projektu** | zwraca wyłącznie „Modernist" (`66a4f3af-84eb-46b9-a152-2395994856ea`) |

**Wniosek: zapis i nadpisywanie działa, usuwanie nie.** Projekt należy do innego konta niż
to, z którego działa sesja.

**Pomyłka, którą to sprostowało.** Na podstawie samego `list_projects` napisałem w rozmowie,
że zapisu prawdopodobnie nie mam. `list_projects` jest filtrowane do projektów własnych,
więc jego milczenie nic nie mówi o prawie zapisu do projektu współdzielonego. Próba zapisu
to obaliła. Reguła do zapamiętania: **brak pozycji na liście nie jest dowodem braku
uprawnienia** - dowodem jest próba.

**Konsekwencja operacyjna, ważniejsza od samego wyniku.** Nadpisanie pliku w tym projekcie
jest **nieodwracalne ze strony sesji**: nie ma usuwania i nie ma dostępu do historii wersji.
Każde nadpisanie wymaga wcześniejszej kopii w repozytorium.

**Zostawiony ślad.** `_robocze/proba-zapisu.md` w projekcie to plik testowy z tej próby.
Sesja nie może go usunąć; do skasowania w interfejsie Claude Design.

## Dwie linie palety, oba zestawy ze stemplem z 2026-09-03

`CLAUDE.md` opisuje dziś `guidelines/paleta-barw.md` w projekcie jako „kopię sprzed wymiany"
14-kolorowej palety. **Odczyt pokazuje coś innego.** To osobna, znacznie dalej rozwinięta
linia: **Kaszmir Wyciszony v5.1.0**, z architekturą jeden kolor uniwersalny plus **sześć
dziedzin** po trzy stopnie, macierzami ΔE2000 dla piętnastu par i progiem akceptacji
podniesionym przez foundera z 20 na 25.

Wartości bazowe tej linii, przepisane z odczytu, żeby zapis przetrwał ewentualne nadpisanie
pliku w projekcie:

| Kolor | Token | Dziedzina | Hex |
|---|---|---|---|
| Aksamit | `primary` | Pedagogika | `#752F3F` |
| Bursztyn | `secondary` | Akademia AI | `#9F6631` |
| Onyks | `info` | Pożyczki UE/BGK | `#005A80` |
| Ultramaryna | `tertiary` | Aplikacje sprzedażowe | `#191647` |
| Rubin | `quaternary` | Portal sprzedaży online | `#905E88` |
| Szmaragd | `quinary` | szósta, linia do wskazania | `#2D795C` |

Baza: Espresso `#221A15`, Kaszmir `#FBF8F2`, Muślin `#F6F2E9`, Pergamin `#E7DFD2`,
Sepia `#5E4E40`, Popiół `#7D7466`. Stany: Patyna `#007987`, Werdykt `#004D49`,
Rubryka `#803700`, Karmin `#9E2B2B`, Złoto foliowe `#A8874E`. Reguła proporcji 70/25/5,
dokładnie jedna dziedzina na dokument.

Ta linia niesie własny rachunek i własne świadome ustępstwo: najsłabsza para całej macierzy
to **Aksamit × Rubin ΔE2000 19,0**, poniżej progu 25, przyjęta przez foundera po odrzuceniu
bezpieczniejszej alternatywy (hue 319°, ΔE 24,0), żeby zachować charakter bordo.

**Obowiązująca w repozytorium jest Regalia**, zatwierdzona przez właściciela 2026-09-03 -
ta sama data. Dokumenty `irn-design-*` w projekcie stoją na Regalii.

### Czego ta notatka NIE rozstrzyga

Która linia obowiązuje. Oba zestawy noszą datę zatwierdzenia 2026-09-03 i oba mają
uzasadnienie. To pozycja **czekająca na właściciela**; rozstrzyga ją audyt czterech
dokumentów wzorcowych przekazanych 2026-09-09 jako najaktualniejsze wytyczne.

**Czego nie wolno zrobić przed tym rozstrzygnięciem:** nadpisać `guidelines/paleta-barw.md`
w projekcie. To zapis decyzji z rachunkiem, a nadpisania nie da się z sesji odwrócić.

## Co faktycznie zawiera `tokens/tokens.css` w projekcie

Sprawdzone odczytem. Plik niesie **dwa bloki naraz**:

1. Stary blok `--irin-*` w wartościach linii Kaszmir Wyciszony v5, wraz z sześcioma
   dziedzinami po trzy stopnie i trzema wariantami `dark-*`.
2. Dopisany 2026-09-06 blok `--irin-r-*` w Regalii: czternaście barw, cztery tinty, gniazdo
   dziedziny (`--irin-r-dziedzina`, `--irin-r-tint-dziedzina`) domyślnie neutralne, aliasy
   semantyczne, limit złota `21.34` cm², lista par zabronionych z liczbami i komentarz
   wyjaśniający brak tokenów `success` / `warning` / `error`.

Blok Regalii jest w projekcie zgodnie z zamiarem, więc synchronizacja z 2026-09-06 nie
wymaga powtórzenia. Otwarte zostaje pytanie, **które pliki czytają który blok** - podejrzenie
z `CLAUDE.md` (wydanie 01 brandbooka i księgi znaku czyta `--irin-*`, więc renderuje się
w barwach v5) nie zostało w tej sesji zweryfikowane odczytem tych plików.

## Poprawki do wprowadzenia w `CLAUDE.md`

Nie wprowadzone w tej turze, bo plik czytały równolegle audyty. Do zrobienia:

1. Akapit „Uwaga o projekcie w Claude Design, zmierzona 2026-09-04" nazywa
   `guidelines/paleta-barw.md` „kopią sprzed wymiany". Jest to **Kaszmir Wyciszony v5.1.0**,
   osobna linia z sześcioma dziedzinami, nie kopia poprzedniej wersji Regalii.
2. Ten sam akapit mówi o „trzech zestawach barw" w projekcie. Po dopisaniu bloku Regalii
   do `tokens/tokens.css` 2026-09-06 opis wymaga przeliczenia: `tokens.css` niesie dwa
   bloki w jednym pliku.
3. Rozbieżność nazw obszarów („Pedagogika" wobec „Szkolenia zawodowe", trzy obszary wobec
   sześciu) ma w `CLAUDE.md` status otwarty od 2026-09-04. Cztery dokumenty wzorcowe
   przekazane 2026-09-09 nazywają obszary „Szkolenia zawodowe", „Pożyczki UE / BGK"
   i „Akademia AI"; to kandydat na rozstrzygnięcie, ale wymaga potwierdzenia audytem,
   nie jednym odczytem.

## Falsyfikatory

- **Uprawnień:** ponowna próba `delete_files` kończąca się sukcesem oznaczałaby, że projekt
  zmienił właściciela albo że uprawnienia sesji się zmieniły.
- **Dwóch linii:** dokument z datą późniejszą niż 2026-09-03, który jawnie wycofuje jedną
  z linii. Do jego znalezienia oba zestawy trzeba traktować jako równoległe, nie jako nowszy
  i starszy.
- **Zawartości `tokens.css`:** ponowny odczyt pokazujący jeden blok zamiast dwóch.
