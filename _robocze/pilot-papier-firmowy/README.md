# Pilot papieru firmowego: pliki źródłowe kanwy

Artboardy `.dc.html` i `canvas.json` pilota papieru firmowego IRIN. Źródło do zasiania kanwy skillem `design`, nie źródło prawdy o layoucie: zgodnie z `/CLAUDE.md` layout powstaje w Claude Design, a wyniki pięciu pomiarów z `03-pakiet-claude-design/zlecenia/pilot-papier-firmowy.md` trafiają do warstwy 1, nie tutaj. Logotypy do ponownego zasiania: `logo_irin_poziom.svg` i `logo_irin_sygnet.svg` z korzenia repozytorium.

**Uzupełnione 2026-09-03:** kapitał zakładowy 40 000,00 zł wpisany do `Main.dc.html` po odczycie odpisu pełnego z rejestru KRS. Ten sam odpis potwierdził niezależnie zapis sądu rejestrowego, który wcześniej pochodził z dokumentów foundera - dwa źródła zgodne. **Uzupełnione 2026-09-03, druga tura:** telefon firmowy `+48 453 049 912` wpisany do bloku kontaktowego w `Main.dc.html`. Zapis z prefiksem kierunkowym i w grupach po trzy cyfry jest wyborem tej sesji, nie regułą repozytorium - `02-szablony-dokumentow/papier-firmowy.md` formatu nie narzuca, więc zmiana na `453 049 912` albo `+48 453 04 99 12` niczego nie łamie.

**Placeholder `[TELEFON]` w `WizytowkaAwers.dc.html` zostaje celowo** - obok `[IMIĘ I NAZWISKO]`, `[STANOWISKO]` i `[E-MAIL]` to pole osoby, nie firmy, a zlecenie wprost zakazuje wypełniania ich zmyślonymi danymi.

## Dwa adresy kanwy, żadnego nie potwierdzono z sesji - stan na 2026-09-03

| Adres | Skąd |
|---|---|
| `https://claude.ai/code/artifact/3c6ee053-8041-4c1f-989a-c320941b156b` | zapisany przez sesję z 2026-09-02 |
| `https://claude.ai/code/artifact/191cf137-7c7c-4bec-a074-f9c53780ae9d` | publikacja z 2026-09-03, zwróciła sukces i ten adres |

**Wcześniejsza wersja tego akapitu twierdziła, że pierwszy adres nie istnieje, i powoływała się na `Artifact action:list`. To twierdzenie zostało wycofane, bo dowód go nie utrzymuje.** Ten sam mechanizm, użyty później w tej samej sesji, zwrócił zero artefaktów, a `Artifact action:status` odpowiedział „no such artifact for this account" **na kanwę opublikowaną godzinę wcześniej z tej sesji**. Listowanie artefaktów jest zależne od profilu konta, na którym akurat pracuje sesja, i nie rozstrzyga, czy artefakt istnieje.

Co z tego wynika: **nie wiadomo, czy któryś z dwóch adresów działa** - nie wiadomo też, że nie działa. Rozstrzyga jedno i nie da się tego zrobić z sesji: otworzyć oba w przeglądarce zalogowanej na właściwy profil.

## Jak zasiać

Logotypy zostają w korzeniu repozytorium - **nie kopiuj ich do tego katalogu**. Przy zasiewie przekazuje się je jako obrazy, a seeder zapisuje je pod samą nazwą pliku; dlatego `<img src="logo_irin_poziom.svg">` bez prefiksu katalogu jest zapisem poprawnym. Prefiks `uploads/`, jak w `brandbook.dc.html` w korzeniu, pochodzi z innego mechanizmu i tutaj **zepsułby render** - obraz wyszedłby jako pusta ramka, bez ostrzeżenia.

Używane są dokładnie dwa pliki: `logo_irin_poziom.svg` (strona 1, strona kolejna, awers wizytówki) i `logo_irin_sygnet.svg` (rewers wizytówki).

## Zanim wykonasz pomiary

Dwie rzeczy, bez których wynik będzie fałszywy:

1. **Pomiary liter i wag robi się na kanwie, nie na wyeksportowanym PDF-ie.** Eksport nie osadza krojów z Google Fonts — w pliku PDF zobaczysz krój zastępczy (`Segoe UI`/`Arial` zamiast Manrope, `Courier New` zamiast Inconsolaty). PDF służy do sprawdzenia proporcji i skali 1:1.
2. **Przełącznik `siatka` działa osobno na każdym artboardzie.** Do pomiaru siatki trzeba go włączyć dwa razy: na stronie pierwszej i na stronie kolejnej.
