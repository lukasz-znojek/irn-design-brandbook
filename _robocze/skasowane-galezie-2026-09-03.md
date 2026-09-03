# Gałęzie skasowane 2026-09-03

Zapis wykonany **przed** usunięciem, żeby każda pozycja dała się przywrócić. Decyzję podjął founder po pokazaniu listy; usunięcia dokonano z sesji Claude Code po scaleniu Etapu 2 do `main` (commit `9d4101e`).

**Jak przywrócić dowolną pozycję:**

```bash
git push git@github.com:lukasz-znojek/irn-design-brandbook.git <SHA>:refs/heads/<nazwa>
```

GitHub trzyma nieosiągalne commity jeszcze przez pewien czas po usunięciu gałęzi, ale nie w nieskończoność — poniższe SHA są jedynym pewnym adresem tej pracy.

## Gałęzie w całości zawarte w `main` (zero commitów poza `main`)

Usunięcie tych dwunastu nie kasuje żadnej pracy: każdy ich commit jest przodkiem `main`.

| SHA | Gałąź |
|---|---|
| `49d901529bf0d31e76022f2511c80b2843c77621` | `chore/post-merge-followups-psf-bur-kontekst` |
| `5d32eac0446b48be24ebd9e1e78f161ba1cb84c5` | `claude/irin-color-palette-variants-tjjnza` |
| `369322ced6802080634f183ee06a56140a7af0e0` | `claude/test-konto-rozliczeniowe-uzywasz` |
| `65af6c990c1c68cef24b0b7a533605371d7bbae3` | `copilot/co-o-mnie-wiesz` |
| `23aa871d7dbfb42858b37c94c3938b376fb671e5` | `copilot/explain-repository-structure` |
| `23aa871d7dbfb42858b37c94c3938b376fb671e5` | `copilot/explore-codebase-implementation-plan` |
| `eb2ccfba4cc3f192f737e7c74624d9137bdcec22` | `copilot/irin-brandbook-os` |
| `23aa871d7dbfb42858b37c94c3938b376fb671e5` | `copilot/review-session-history` |
| `23aa871d7dbfb42858b37c94c3938b376fb671e5` | `copilot/sprawdz-czy-caly-etap-2-jest-wykonany` |
| `23aa871d7dbfb42858b37c94c3938b376fb671e5` | `copilot/tworzylelismy-gdzie-roadmape` |
| `23aa871d7dbfb42858b37c94c3938b376fb671e5` | `copilot/wypchnij-wszystko-co-sie-nadaje` |
| `2fd78c7d9b5bd3fad9cf7adcbaf13d2519c3380a` | `lukasz-znojek-patch-1` |

## Gałęzie z własną, świadomie odrzuconą pracą

Te dwie miały commity poza `main`. Powód odrzucenia jest wpisany, bo bez niego przywrócenie ich za pół roku byłoby cofnięciem decyzji, nie naprawą pomyłki.

| SHA | Gałąź | Co niosła | Dlaczego odrzucona |
|---|---|---|---|
| `989a7219d21d5551824f82d36429cfc7e7284ebe` | `copilot/etap-2-weryfikacja-prawna` | 2 commity, 10 plików: zamykała wszystkie osiem pozycji `weryfikacja-u-zrodla.md` statusem „niesprawdzone”. | Siedem z tych ośmiu pozycji jest **odczytanych u źródła** (2026-09-02 i 2026-09-03), z cytatami i numerami stron. Scalenie zamieniłoby odczyt na deklarację braku odczytu. |
| `a84979c0612fb6770e4c8e657067928bc9150d46` | `claude/project-roadmap-3cr739` | 1 commit, 18 plików: równoległe podejście do Etapu 2 z wyciągiem art. 125-133 oraz kanwą pilota. | Oparta na `main` sprzed scalenia — jej scalenie **usunęłoby siedem PDF-ów źródłowych** z `01-baza-wiedzy/prawo/zrodla/` (`git diff` pokazywał je jako `Bin … -> 0 bytes`). To, co miała unikalnego, przeniesiono osobno: katalog `_robocze/pilot-papier-firmowy/` wszedł do `main` commitem `9d4101e`. |

## Druga tura, tego samego dnia: gałęzie bez własnej treści

Founder polecił usunąć to, co niepotrzebne. Usunięto dwie, obie sprawdzone pomiarem przed skasowaniem, nie na oko.

| SHA | Gałąź | Pomiar, na podstawie którego uznano ją za pustą |
|---|---|---|
| `47df8b7c` | `claude/agent-github` | `git diff main...` wskazywał cztery pliki, ale wszystkie trzy pliki w `.github/` mają w `main` **identyczne skróty obiektów**, a sekcja „Agent Claude w GitHub” jest w `CLAUDE.md` na `main`. Gałąź nie wnosiła nic. |
| `ee76082` | `copilot/pilot-papieru-firmowego` | Jeden commit „Initial plan”; `git diff --stat main...` zwraca pustkę. |

## Czego świadomie nie usunięto

- `copilot/ankieta-uzupelniajaca` (`3b4f098`) — usuwa 5110 wierszy w 43 plikach. Nie ustalono, co to miało być; **wymaga przejrzenia przed jakąkolwiek decyzją.**
- `claude/irin-color-palette-variants-dl9lge` (`e9b1569`) — 16 plików, siedem wariantów palety v2. Obowiązująca paleta to wariant 2, a jego kopia leży w `_robocze/paleta-v2/`; gałąź nie była jednak porównana plik po pliku, więc zostaje.
- `claude/zadanie-reczne` (`cc4728c`) — workflow „Claude – zadanie ręczne” na `workflow_dispatch`, nieobecny w `main`. To realna, niescalona funkcja, nie śmieć.
- `copilot/help-advise-on-tasks` (`33f023e`) — trzy pliki, dokumentacja delegowania etapów. Niescalona, nieprzejrzana.
