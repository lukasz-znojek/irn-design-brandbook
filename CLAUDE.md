# CLAUDE.md — kontekst dla pracy w tym repozytorium

## Czym jest IRIN

IRIN (Instytut Rozwoju i Nauki) to polska firma działająca w trzech obszarach: aplikacje dla przedstawicieli handlowych, usługi pozyskiwania pożyczek, oraz dofinansowane szkolenia zawodowe wydające zaświadczenia KFS (Krajowy Fundusz Szkoleniowy) i certyfikaty BUR (Baza Usług Rozwojowych, PARP). Planowany jest też portal sprzedaży szkoleń online.

## Architektura trójwarstwowa

1. **Warstwa 1 — baza wiedzy** (`01-baza-wiedzy/`): kontekst firmy, przepisy prawne, wytyczne usługowe. Punkt wejścia: `01-baza-wiedzy/00-INDEX.md`.
2. **Warstwa 2 — szablony dokumentów** (`02-szablony-dokumentow/`): pliki `.md` jako wytyczne co do treści i wymogów regulacyjnych — nigdy jako układ graficzny.
3. **Warstwa 3 — pakiet i prompt dla Claude Design** (`03-pakiet-claude-design/`): kompozycja, layout i grafika powstają w Claude Design, nie w tym repozytorium.

## Zasady obowiązujące w tym repozytorium

- Każdy commitowany plik jest napisany po polsku: nazwy plików, nagłówki, treść. Wyjątkiem są identyfikatory techniczne wymuszone przez narzędzia.
- Layout, kompozycja i grafika powstają wyłącznie w Claude Design — to repozytorium przechowuje treść i wytyczne merytoryczne, nie projekt graficzny.
- `_robocze/` to poligon roboczy/archiwum — nic stamtąd nie jest źródłem prawdy bez ponownej weryfikacji.
- Każda karta specyfikacji dokumentu w warstwie 2 musi jawnie rozróżniać trzy kategorie: elementy **prawnie obowiązkowe**, **konwencję organizacyjną** IRIN i **swobodny wybór projektowy**.
- **Znak łączący to dywiz (`-`), nie myślnik (`—`) ani półpauza (`–`)** - także w zakresach liczb i dat. Reguła obowiązuje w tekście pisanym w tym repozytorium.

  Zasięg reguły i pomiar stanu: nowa treść dopisywana od 2026-09-06 trzyma dywiz, ale w plikach `.md` poza `_robocze/` zostaje **465 myślników i półpauz w 35 plikach** (pomiar 2026-09-06). Masowej zamiany świadomie nie wykonano: część tych znaków stoi wewnątrz cytatów z dokumentów źródłowych, a to repozytorium wymaga, żeby cytat zgadzał się ze źródłem co do znaku - automat zamieniłby także je. Uporządkowanie starszej treści jest osobną decyzją właściciela, do wykonania cytat po cytacie.

  To jest **zapis, nie blokada**: nic technicznie nie wymusza dywizu i model może tę regułę pominąć. Wymuszałby ją dopiero krok w workflow recenzji PR, odrzucający myślnik i półpauzę w liniach dodanych poza cytatami - takiego kroku dziś nie ma.

## Co wynika z plików logotypu (`logo_irin_sygnet.svg`, `logo_irin_pion.svg`, `logo_irin_poziom.svg`)

- Ścieżki graficzne w każdym z trzech plików nie mają zdefiniowanego atrybutu `fill` — a więc renderują się domyślnym czarnym; jedyny jawny `fill="none"` dotyczy przezroczystego prostokąta tła. Wniosek: pliki źródłowe logotypu są jednokolorowe (czarne na przezroczystym tle) i same w sobie nie definiują żadnej palety barw.
- `logo_irin_sygnet.svg` i `logo_irin_pion.svg`: `viewBox="0 0 184.837 162.834"`; `logo_irin_poziom.svg`: `viewBox="0 0 281.333 158.667"`.
- **Proporcje odczytane z `viewBox` to proporcje pustej ramki, nie znaku - korekta 2026-09-04.** Obwiednia artworku zmierzona `getBBox` na złożonej kanwie: poziom 184,213 × 38,854 (**4,741:1**), pion 103,728 × 87,312 (**1,188:1**), sygnet 103,728 × 38,853 (**2,670:1**). Artwork zajmuje 16,0 / 30,1 / 13,4 procent powierzchni ramki. Skutek: `width:18mm` na kontenerze bez nadpisania `viewBox` daje znak o szerokości 11,8 mm, czyli poniżej minimum. Pełny wywód i dwa poprawne sposoby: `01-baza-wiedzy/identyfikacja/logotyp.md`.
- Trzy pliki odpowiadają trzem wariantom logotypu: poziomy (podstawowy), pionowy (pola wąskie/wysokie), sygnet (samodzielny).
- Minimalny rozmiar, przestrzeń ochronna i zakazy modyfikacji **nie wynikają z geometrii SVG** - nie da się ich zmierzyć w tych plikach. Pochodzą z `brandbook.dc.html` i **zostały potwierdzone przez foundera**: minimalny rozmiar i przestrzeń ochronna wcześniej, cztery zakazy modyfikacji 2026-09-02. Obowiązująca specyfikacja: `01-baza-wiedzy/identyfikacja/logotyp.md`.

## Co wynika z `brandbook.dc.html`

To jest **wstępne canvas foundera** — punkt inspiracji i dowód zamierzonego kierunku, nie specyfikacja do odtworzenia. Wyekstrahowane fakty:

- Pełna nazwa firmy w pliku: "Instytut Rozwoju i Nauki". Trzy dziedziny nazwane wprost: Pedagogika, Akademia AI, Pożyczki UE/BGK. **Rozbieżność otwarta 2026-09-04:** dokumenty wzorcowe `irn-design-*` nazywają pierwszą dziedzinę **Szkolenia zawodowe**, nie Pedagogika, a `tokens/tokens.css` opisuje **sześć** obszarów przy trzech barwach dziedzinowych w palecie. Czeka na decyzję właściciela; do jej podjęcia obowiązują trzy barwy z `paleta-barw.md`, a obszar bez własnej barwy dostaje Szafir Nocny plus podpis słowem.
- Krój pisma: **Manrope**, wagi 200–800; pomocniczo Inconsolata.
- Najczęstsze wartości hex w pliku: `#1E1611` (tusz/tekst), `#5B4837`, `#F2ECE1` (papier/tło), `#3A2C1E`, `#4A1D26`, `#D9A75B`, `#B58540`, `#E4DACB`, `#1B2B26`, `#A15C2C`, `#8B2E3A` — plik nazywa tę paletę "Colorbook Kaszmir Aksamit" i opisuje regułę proporcji 80/15/5 (baza / akcent dziedzinowy / akcja).
- Siatka dokumentu A4 w pliku: 6 kolumn, moduł 32 mm, gutter 4 mm, jednostka bazowa 6 mm.
- Przestrzeń ochronna logotypu opisana jako "x = wysokość liter sygnetu" — jednostka względna, nie stała miara. Minimalna szerokość podana w pliku: 18 mm / 90 px.
- Przykładowe zastosowania pokazane w pliku: okładka viewbooka, karta usługi BUR, dwie wersje certyfikatu (kolumnowa, pieczęć), papier firmowy, wizytówka.
- **Rozbieżność do potwierdzenia z founderem**: 12-barwna paleta i moduły siatki w pliku to jego robocza propozycja, a nie coś zmierzonego z geometrii logotypu — każda z tych wartości musi zostać przez niego świadomie zatwierdzona, zanim stanie się obowiązującą specyfikacją w `01-baza-wiedzy/`.

## Paleta barw - stan obowiązujący

Wartości hex wypisane wyżej opisują **plik `brandbook.dc.html`**, a nie obowiązującą paletę - to zapis tego, co jest w kanwie foundera, i pozostaje prawdziwy jako opis tego pliku.

Obowiązująca paleta to **Regalia (wariant B)**, zatwierdzona przez właściciela 2026-09-03: siedem barw nośnych, siedem funkcjonalnych i cztery tinty dziedzinowe 12 procent. **Zastąpiła w całości paletę „Kaszmir Wyciszony” (14 kolorów, 2026-09-02) - żadna nazwa i żaden hex tamtej palety nie obowiązuje.** Wypadły: Kaszmir, Muślin, Pergamin, Espresso, Sepia, Popiół, Miedź, Onyks, Karmin, Patyna, Werdykt, Rubryka, dawny Aksamit `#452430` i Złoto foliowe. Jedyne źródło prawdy: `01-baza-wiedzy/identyfikacja/paleta-barw.md`. Tam też, od 2026-09-02, siatka A4 (`siatka-a4.md`), typografia (`typografia.md`) i logotyp (`logotyp.md`) - `03-pakiet-claude-design/format-paczki.md` już żadnej z tych czterech nie powtarza, tylko odsyła i dokłada zasady ich użycia w zleceniu. Dane maszynowe: `01-baza-wiedzy/identyfikacja/tokeny/palette-irin.json`. Porównanie siedmiu wariantów i uzasadnienie wyboru (archiwum): `_robocze/paleta-v2/palette-options-v2.md`. Historia pierwszej decyzji: `03-pakiet-claude-design/propozycja-palety-i-siatki-do-potwierdzenia.md`.

Rozbieżność opisana w punkcie wyżej jest **rozstrzygnięta**: paleta i siatka przeszły pomiar i świadomą decyzję foundera. Zapis zostaje jako historia, nie jako otwarta sprawa.

**Uwaga o projekcie w Claude Design, zmierzona 2026-09-04.** W projekcie `1a22ce64-0e1c-43a6-bd60-eef9241ef73b` żyją równolegle **trzy zestawy barw**: `guidelines/paleta-barw.md` (kopia sprzed wymiany), `tokens/tokens.css` w wersji v5 z sześcioma obszarami i wartościami spoza obu palet (`--irin-aksamit: #752F3F`, `--irin-onyks: #005A80`), oraz dokumenty `irn-design-*` na Regalii. Osiem szablonów w `templates/` i cztery dokumenty wzorcowe **nie korzystają z tokenów** - wpisują hexy Regalii wprost - więc renderują się poprawnie; wydanie 01 brandbooka i księgi znaku korzysta z `--irin-*` i renderuje się w barwach v5. Synchronizacja `tokens/` jest po stronie repozytorium kodu (`/design-sync`) i jest pozycją otwartą.

Dwie zasady, które muszą przetrwać każdą przyszłą zmianę palety: kontrast liczy się na nowo wzorem WCAG 2.1, nigdy nie kopiuje się starych liczb; kolor nigdy nie jest jedynym nośnikiem statusu - każdy stan potrzebuje etykiety słownej albo ikony obok koloru.

## Agent Claude w GitHub (rola i granice)

Dwa kanały o różnym rozliczeniu:

- **Workflow** `anthropics/claude-code-action` w `.github/workflows/` – rozliczane w subskrypcji Claude (sekret `CLAUDE_CODE_OAUTH_TOKEN`). Kanał podstawowy.
- **Karta „Agents”** w GitHub – agent `brandbook-irin` z pliku `.github/agents/brandbook-irin.agent.md`, do zadań zlecanych ręcznie z panelu. Rozliczany w GitHub AI credits i minutach Actions; własnego klucza Anthropic nie przyjmuje.

Cztery wyzwalacze workflow:

- `claude.yml` – wzmianka `@claude` w issue, komentarzu albo recenzji: odpowiedź na pytanie, wyjaśnienie repozytorium, plan pracy, propozycja zmiany w osobnej gałęzi.
- `claude-recenzja-pr.yml` – każde otwarcie lub aktualizacja PR: recenzja zgodności z tym plikiem i ze specyfikacjami w `01-baza-wiedzy/identyfikacja/`.
- `claude-triaz-issue.yml` – każde nowe issue bez `@claude`: etykiety `warstwa-1`, `warstwa-2`, `czeka-na-foundera`, wykrycie duplikatu, jeden komentarz z następnym krokiem.
- `claude-zadanie.yml` – ręczne uruchomienie z zakładki Actions („Run workflow”) z polem na zadanie i numerem issue/PR na wynik; zamiennik panelu „Agents” na subskrypcji Claude. Zmiany plików tylko przez gałąź `claude/zadanie-<run_id>` i PR.

Granice obowiązujące agenta w każdym trybie:

- Nie modyfikuje `main` bezpośrednio. Każda zmiana plików to gałąź i PR do akceptacji właściciela; poza tym wyłącznie komentarze.
- Nie zamyka issues ani PR-ów, nie scala, nie tworzy nowych etykiet, nie usuwa gałęzi.
- Pisze po polsku, krótko i formalnie. Ryzyko nazywa przed pochwałą. Każda uwaga wskazuje plik i wiersz.
- Nie rozstrzyga spraw oznaczonych `czeka-na-foundera` – może je streścić i wskazać, jaka decyzja jest potrzebna.
- Limity: `--max-turns` w każdym workflow; brak wyzwalaczy cyklicznych (cron), dopóki właściciel ich nie doda świadomie.
