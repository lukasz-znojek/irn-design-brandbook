# Zaległe gałęzie w repozytorium - pomiar i rozstrzygnięcia

**Data pomiaru: 2026-09-09**, po wypchnięciu bloku A na `main` (`f9b6bd6`).
Metoda: `git rev-list --count`, `git diff --name-status` i **próbne scalenie**
`git merge-tree --write-tree` przeciw `origin/main` - konflikty niżej są
zmierzone, nie przewidziane.

## Stan wyjściowy

- Drzewo robocze: **czyste**, zero niescommitowanych plików.
- Gałąź `claude/irin-pomiar-raport-xsbs7j`: równa `main`, zdalna usunięta po scaleniu.
- Gałęzi zdalnych z commitami poza `main`: **sześć**, razem **24 commity**.
- `origin/copilot/sprawdz-stan-repo`: 0 commitów przed `main`, czyli w całości
  wchłonięta. Nie ma czego scalać; zostaje wyłącznie jako martwa gałąź.

## Co scalone w tej turze

**`copilot/help-advise-on-tasks`** - jedyna gałąź, która scala się **bez
konfliktu** (zmierzone: 0). Trzy pliki dokumentacji o delegowaniu etapów
agentom. Treść przeczytana przed scaleniem: zero wartości palety, zero tez
prawnych, zero kolizji z warstwą 1. Scalone jako `da9f2df`; obie bramki po
scaleniu bez zmiany (228/0 oraz 122).

## Pięć gałęzi, które konfliktują

| Gałąź | Commitów | Plików | Konfliktów | Konflikt w |
|---|---|---|---|---|
| `claude/irin-visual-identity-vq9ddw` | 14 | 33 | **5** | `logotyp.md`, `paleta-barw.md`, `palette-irin.json`, `PLAN.md`, `tokens.css` |
| `claude/etap-2-regulamin-bur` | 5 | 15 | 2 | `logotyp.md`, `typografia.md` |
| `claude/project-roadmap-3cr739` | 2 | 8 | 1 | `PLAN.md` |
| `claude/irin-color-palette-variants-dl9lge` | 1 | 16 | 1 | `PLAN.md` |
| `copilot/ankieta-uzupelniajaca` | 1 | 43 | 1 | `PLAN.md` |

**Wspólna przyczyna czterech z pięciu: `PLAN.md`.** Ten plik został dziś
zastąpiony w całości planem destylacji na Regalię, a tamte gałęzie niosą starą
kolejkę zadań. Rozstrzygnięcie jest tu mechaniczne: zostaje wersja z `main`.

**Osobny przypadek: `irin-visual-identity-vq9ddw`.** Konfliktuje w dwóch
plikach **generowanych** - `palette-irin.json` i `tokens.css`. Ręczne
rozwiązanie konfliktu w pliku generowanym jest bez sensu: jedyne poprawne
rozstrzygnięcie to wziąć wersję z `main`, złożyć paletę na nowo i przepuścić
przez bramkę. Ta gałąź niesie jednak rzeczy, których w `main` nie ma i które
wyglądają na realne wyniki: szablon pisma `.docx`, arkusz `.xlsx` z pięcioma
wykresami, podpis mailowy, cztery zlecenia do Claude Design oraz commit
„Tekst na jasnych tłach: policzona macierz, której w palecie nie było".

## Rekomendacja

**Nie scalać hurtem.** Jedna gałąź na raz, w kolejności rosnącego ryzyka,
z regułą rozstrzygania konfliktu podaną z góry: **w plikach przepisanych dziś
(warstwa 1, pliki generowane, `PLAN.md`) wygrywa `main`; w pozostałych wygrywa
gałąź.** Kolejność:

1. `claude/project-roadmap-3cr739` - 2 commity, jeden konflikt w `PLAN.md`,
   reszta to odczyt ogłoszenia PUP Kielce u źródła. Najmniejsze ryzyko.
2. `claude/etap-2-regulamin-bur` - 5 commitów, praca prawna wokół BUR;
   dwa konflikty w warstwie 1 wymagają sprawdzenia, co tamta gałąź tam
   dopisała poza paletą.
3. `claude/irin-visual-identity-vq9ddw` - 14 commitów, najwięcej wartości
   i najwięcej konfliktów; wymaga złożenia palety na nowo po scaleniu.
4. `copilot/ankieta-uzupelniajaca` - 43 pliki, w tym **usunięcia**
   (`_robocze/copilot-v1/`); wymaga osobnego przejrzenia, bo kasowanie
   plików nie jest scaleniem treści.

**`claude/irin-color-palette-variants-dl9lge` - rekomendacja: nie scalać.**
Dodaje katalog `02-branding/` z siedmioma wariantami palety v2, podglądami
i tokenami. To jest **paleta wycofana**, a katalog leży poza perymetrem bramki
spójności, więc te wartości nie zostałyby przez nic złapane. To samo
porównanie siedmiu wariantów leży już w `_robocze/paleta-v2/` i `CLAUDE.md`
wskazuje je jako archiwum. Falsyfikator: jeżeli w `02-branding/` jest coś,
czego nie ma w `_robocze/paleta-v2/`, wtedy trzeba przenieść tę różnicę,
a nie całą gałąź.

## Czego ten pomiar nie rozstrzyga

- **Co dokładnie tamte gałęzie dopisały w `logotyp.md` i `typografia.md`
  poza paletą** - nie czytałem tych różnic, więc reguła „wygrywa `main`"
  może wyrzucić treść, która nie ma nic wspólnego z kolorem. Do sprawdzenia
  przed scaleniem punktów 2 i 3.
- **Czy szablony `.docx` i `.xlsx` z gałęzi wizualnej są aktualne wobec
  Regalii** - powstały 2026-09-08, czyli przed dzisiejszą destylacją.
- **Czy któraś z tych gałęzi ma otwarty PR** - nie sprawdzałem.
