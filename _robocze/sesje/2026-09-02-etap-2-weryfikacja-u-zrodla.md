# Podsumowanie sesji 2026-09-02 (wieczór): Etap 2, weryfikacja u źródła

Sesja przerwana na prośbę foundera („wgrywaj pracę, kończy się sesja”). Stan zapisany w gałęzi `claude/project-roadmap-3cr739`.

## Co się udało

- Founder otworzył sieć środowiska; dziennikustaw.gov.pl, funduszeunijne.gov.pl, kielce.praca.gov.pl i it.kielce.pl odpowiadają.
- **Odczytane u źródła** (pozycje 4, 5, 6 listy z `01-baza-wiedzy/prawo/weryfikacja-u-zrodla.md`): rozporządzenie KFS Dz.U. 2025 poz. 1641, ustawa Dz.U. 2025 poz. 620 (art. 125-133, art. 461), ogłoszenie PUP Kielce o naborze KFS z sierpnia 2026. Kopie w `01-baza-wiedzy/prawo/zrodla/`.
- `kfs.md` przepisany na cytaty z numerami artykułów. Dwa błędy wcześniejszej wersji poprawione: krotności 4/8/12/14 zależą od wielkości podmiotu, nie od priorytetu; warunek „pracodawca zatrudniający co najmniej jednego pracownika” nie ma oparcia w art. 125.
- Nowe ustalenie ważne dla certyfikatu: rozporządzenie KFS § 2 ust. 2 pkt 3 każe pracodawcy dołączyć do wniosku **wzór dokumentu ukończenia wystawianego przez realizatora**. Wzór IRIN musi istnieć przed wnioskiem klienta.
- Pliki kanwy pilota papieru firmowego zabezpieczone w `_robocze/pilot-papier-firmowy/` (artboardy .dc.html i canvas.json). Opublikowana kanwa: https://claude.ai/code/artifact/3c6ee053-8041-4c1f-989a-c320941b156b
- Narzędzia w `_robocze/narzedzia/`: ekstraktor tekstu z PDF (czysty Python) i skrypt Chromium do stron za ochroną antybotową.

## Co się nie udało i dlaczego

- **Pozycje 1-3 (Regulamin BUR, załączniki nr 2 i 12, kod usługi):** serwery PARP odpowiadają stroną zabezpieczenia Incapsula; curl dostaje wyzwanie JavaScript, Chromium w sandboxie nie przechodzi przez proxy sesji (tunel zamykany po wysłaniu ClientHello), WebFetch zgłasza blokadę egress. Falsyfikator tej diagnozy: ten sam adres otwarty w zwykłej przeglądarce daje PDF.
- **Pozycja 7 (operator PSF):** operator zidentyfikowany (ŚCITT), aktualnego regulaminu FEŚ 2021-2027 nie znaleziono.
- **Pozycja 8 (podręcznik FE):** PDF pobrany, ale czcionka niestandardowa; odczyt rozdziału o adresatach obowiązków nie dokończony. Pozycja warunkowa.
- Z wyszukiwarki: PARP zmieniła Załączniki nr 2 od **6 lipca 2026 r.**; wersja z 5 maja 2026 r. przywołana w repozytorium jest nieaktualna.

## Następny krok dla foundera (jeden)

Pobrać w zwykłej przeglądarce trzy pliki z PARP (adresy w `weryfikacja-u-zrodla.md`, sekcja „Adresy plików PARP do pobrania ręcznie”) i wrzucić je do czatu albo do `01-baza-wiedzy/prawo/zrodla/`. Po tym pozycje 1-3 przechodzą na „odczytane”, a karty `karta-uslugi-bur.md` i `certyfikat.md` można zamknąć.

## Dla następnej sesji Claude

- Nie szukać grafik IRIN na dyskach Google; nie traktować dokumentów z dysku jako źródeł prawnych.
- Ścieżki w interfejsie podawać tylko po sprawdzeniu.
- Odczyt PDF: `python3 _robocze/narzedzia/tekst-z-pdf.py plik.pdf wynik.txt`; narzędzie Read nie renderuje PDF (brak poppler), pip i npm są zablokowane.
