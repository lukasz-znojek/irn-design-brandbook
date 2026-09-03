# Pilot papieru firmowego: pliki źródłowe kanwy

Artboardy `.dc.html` i `canvas.json` pilota papieru firmowego IRIN. Źródło do zasiania kanwy skillem `design`, nie źródło prawdy o layoucie: zgodnie z `/CLAUDE.md` layout powstaje w Claude Design, a wyniki pięciu pomiarów z `03-pakiet-claude-design/zlecenia/pilot-papier-firmowy.md` trafiają do warstwy 1, nie tutaj. Logotypy do ponownego zasiania: `logo_irin_poziom.svg` i `logo_irin_sygnet.svg` z korzenia repozytorium.

**Uzupełnione 2026-09-03:** kapitał zakładowy 40 000,00 zł wpisany do `Main.dc.html` po odczycie odpisu pełnego z rejestru KRS. Ten sam odpis potwierdził niezależnie zapis sądu rejestrowego, który wcześniej pochodził z dokumentów foundera - dwa źródła zgodne. **Uzupełnione 2026-09-03, druga tura:** telefon firmowy `+48 453 049 912` wpisany do bloku kontaktowego w `Main.dc.html`. Zapis z prefiksem kierunkowym i w grupach po trzy cyfry jest wyborem tej sesji, nie regułą repozytorium - `02-szablony-dokumentow/papier-firmowy.md` formatu nie narzuca, więc zmiana na `453 049 912` albo `+48 453 04 99 12` niczego nie łamie.

**Placeholder `[TELEFON]` w `WizytowkaAwers.dc.html` zostaje celowo** - obok `[IMIĘ I NAZWISKO]`, `[STANOWISKO]` i `[E-MAIL]` to pole osoby, nie firmy, a zlecenie wprost zakazuje wypełniania ich zmyślonymi danymi.

## Kanwa nie została dotąd opublikowana - korekta z 2026-09-03

Wcześniejsza wersja tego pliku podawała, że 2026-09-02 zasiano kanwę pod adresem `https://claude.ai/code/artifact/3c6ee053-8041-4c1f-989a-c320941b156b`. **Lista artefaktów konta tego nie potwierdza:** `Artifact action:list` w zakresie `mine` i `all` zwraca trzy artefakty, najnowszy z 2026-08-29, i tego identyfikatora wśród nich nie ma. Zapis był nieprawdziwy i został usunięty; to będzie pierwsza publikacja, nie ponowna.

**Po publikacji wpisz tu adres artefaktu.** Bez tego powtórzy się dokładnie ta sytuacja: plik twierdzi, że kanwa istnieje, a nikt nie potrafi jej znaleźć.

## Jak zasiać

Logotypy zostają w korzeniu repozytorium - **nie kopiuj ich do tego katalogu**. Przy zasiewie przekazuje się je jako obrazy, a seeder zapisuje je pod samą nazwą pliku; dlatego `<img src="logo_irin_poziom.svg">` bez prefiksu katalogu jest zapisem poprawnym. Prefiks `uploads/`, jak w `brandbook.dc.html` w korzeniu, pochodzi z innego mechanizmu i tutaj **zepsułby render** - obraz wyszedłby jako pusta ramka, bez ostrzeżenia.

Używane są dokładnie dwa pliki: `logo_irin_poziom.svg` (strona 1, strona kolejna, awers wizytówki) i `logo_irin_sygnet.svg` (rewers wizytówki).
