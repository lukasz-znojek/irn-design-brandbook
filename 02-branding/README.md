# 02-branding - propozycje identyfikacji do wyboru

Ten katalog przechowuje **propozycje** elementów identyfikacji wizualnej IRIN, które czekają na decyzję foundera. Nie jest czwartą warstwą architektury z `/CLAUDE.md`: obowiązująca specyfikacja palety i siatki nadal mieszka w `/03-pakiet-claude-design/format-paczki.md`, a treści dokumentów w `/02-szablony-dokumentow/`. Gdy founder wybierze wariant, wynik trafia do plików docelowych osobnym commitem, a ten katalog zostaje jako zapis procesu wyboru.

- `kolorystyka/palette-options-v2.md` - siedem wariantów palety: tokeny, kontrasty WCAG, rekomendowane użycie, trade-offs, rekomendacja.
- `kolorystyka/palette-preview-v2.md` - dokument podglądowy: ten sam układ demonstracyjny dla wszystkich siedmiu wariantów, paski próbek SVG.
- `kolorystyka/palette-preview-v2.html` - podgląd wizualny z prawdziwą typografią repozytorium (Manrope, Inconsolata z Google Fonts); otwierać lokalnie.
- `kolorystyka/tokens/palette-options-v2.json` - struktura danych siedmiu wariantów (źródło dla generatora).
- `kolorystyka/narzedzia/generuj-podglad-i-kontrast.py` - generator podglądu HTML, pasków SVG i pomiaru kontrastu; jedyne źródło liczb kontrastu w tym katalogu.
- `kolorystyka/podglad/` - pliki generowane: paski próbek i pełny pomiar kontrastu.
