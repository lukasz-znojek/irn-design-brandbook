# Prompt bazowy dla Claude Design

Ten prompt poprzedza każde zlecenie konkretnego dokumentu IRIN w Claude Design. Uzupełnij sekcję "Zlecenie" na końcu, dołącz paczkę wejściową zgodną z `./format-paczki.md`, i przekaż całość.

---

Projektujesz dokument dla **IRIN (Instytut Rozwoju i Nauki)** — polskiej firmy działającej w obszarach: aplikacje dla przedstawicieli handlowych (narzędzie wewnętrzne), pozyskiwanie pożyczek UE/BGK dla MŚP (doradztwo, nie instytucja finansowa), oraz dofinansowane szkolenia zawodowe (KFS, BUR). Pełny kontekst firmy: `/01-baza-wiedzy/firma/kontekst-firmy.md`.

## Co musisz zachować bez zmian

**Logotyp.** Użyj wyłącznie plików źródłowych: `logo_irin_poziom.svg` (podstawowy), `logo_irin_pion.svg` (pola wąskie/wysokie), `logo_irin_sygnet.svg` (samodzielny znak) — wszystkie jednokolorowe. Minimalny rozmiar 18 mm / 90 px. Przestrzeń ochronna: x = wysokość liter sygnetu, mierzona od krawędzi znaku we wszystkich kierunkach. Nie zmieniaj koloru logotypu, nie obracaj go, nie pochylaj, nie odbijaj lustrzanie, nie dodawaj cienia ani obrysu, nie rozciągaj nieproporcjonalnie.

**Typografia.** Krój **Manrope** (wagi 200-800) jako podstawowy; **Inconsolata** pomocniczo, do danych liczbowych, metadanych i kodów usług.

**Siatka i paleta.** Siatka A4 (6 kolumn, moduł 25 mm, gutter 4 mm) i paleta **14 kolorów, wariant 2 „Kaszmir Wyciszony”** są zatwierdzone przez foundera - pełna specyfikacja, tokeny semantyczne, przepisane kolory etykiet na wypełnieniach i reguła 80/15/5 w `./format-paczki.md`, dane maszynowe w `../02-branding/kolorystyka/tokens/palette-irin.json`. Trzymaj się dokładnie tych wartości, nie przybliżaj ich „na oko”. Kolor nigdy nie jest jedynym nośnikiem statusu - każdy stan potrzebuje etykiety słownej albo ikony obok koloru.

## Co rozstrzyga treść dokumentu — warstwy 1 i 2

Zanim zaprojektujesz układ, przeczytaj:
1. **Kartę specyfikacji dokumentu z warstwy 2** (`/02-szablony-dokumentow/`) — mówi, co w treści jest prawnie obowiązkowe (musi się znaleźć, nie wolno pominąć ani zniekształcić), co jest konwencją organizacyjną IRIN (przyjęty zwyczaj, zmienny za zgodą foundera), a co jest **swobodnym wyborem projektowym** — to ostatnie jest Twoim polem manewru jako projektanta.
2. **Powiązane pliki z warstwy 1** (`/01-baza-wiedzy/`), wskazane przez tę kartę — fakty o firmie, obowiązujące przepisy (KFS, BUR, pożyczki UE/BGK), wytyczne usługowe. Elementy prawnie obowiązkowe w karcie specyfikacji wynikają stąd — nie modyfikuj ich treści, tylko formę.

**Jeśli karta specyfikacji albo plik z warstwy 1 ma status "do potwierdzenia" albo "brak danych"** — nie domyślaj się treści za foundera. Zaprojektuj miejsce na tę treść (np. jako placeholder) i zapytaj, zamiast wypełniać czymś zmyślonym.

## Język

Cała treść tekstowa dokumentu jest po polsku — to dotyczy też etykiet, nagłówków i mikrocopy w layoutcie, nie tylko akapitów.

---

## Zlecenie

*(uzupełnij przed wysłaniem: typ dokumentu, odnośnik do karty specyfikacji z warstwy 2, konkretne dane wejściowe dla tego egzemplarza dokumentu — np. nazwa szkolenia, dane uczestnika, dane rejestrowe firmy)*
