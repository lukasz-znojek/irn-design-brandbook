# Archiwum plików z projektu Claude Design - OSTRZEŻENIE O WIERNOŚCI

**Zawartość tego katalogu to transkrypcje, nie kopie co do bajtu.**

Mechanizm: `DesignSync.get_file` zwraca treść pliku do sesji modelu, a zapis na
dysk jest przepisaniem tej treści. Nie ma tu ścieżki, która przenosiłaby bajty
bez pośrednictwa modelu, i nie ma sposobu policzenia sumy kontrolnej pliku
źródłowego po stronie projektu. **Wierności tych kopii nie da się wykazać.**

Co z tego wynika dla korzystania:

- plik `.json` przechodzi walidację składni, więc wiadomo, że jest poprawnym
  JSON-em - ale nie wiadomo, czy każda liczba w nim jest tą, która była
  w oryginale;
- plik `.html` i `.md` nie przechodzi żadnej walidacji, więc jego zgodność
  z oryginałem jest **niesprawdzona**;
- żadna wartość z tego katalogu nie wchodzi do warstwy 1 repozytorium ani do
  żadnej specyfikacji bez ponownego pomiaru u źródła.

To archiwum jest zapisem tego, że coś istniało i mniej więcej co zawierało.
Nie jest dowodem na konkretną wartość.

Data założenia: 2026-09-09. Projekt źródłowy: „System projektowy IRIN",
`1a22ce64-0e1c-43a6-bd60-eef9241ef73b`.

## Stan przenoszenia

| Plik | Status |
|---|---|
| `iteracje-palety/paleta-v7/pomiary-v70.json` | transkrypcja, JSON zwalidowany, 3 138 bajtów |

Pozostałe 42 pliki z paletami czekają na rozstrzygnięcie, którą drogą je
przenieść - patrz `_robocze/porzadek-w-projekcie-claude-design.md`.
