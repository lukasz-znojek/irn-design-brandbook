# Prompt bazowy dla Claude Design

Ten prompt poprzedza każde zlecenie konkretnego dokumentu IRIN w Claude Design. Uzupełnij sekcję "Zlecenie" na końcu, dołącz paczkę wejściową zgodną z `./format-paczki.md`, i przekaż całość.

---

Projektujesz dokument dla **IRIN (Instytut Rozwoju i Nauki)** — polskiej firmy działającej w obszarach: aplikacje dla przedstawicieli handlowych (narzędzie wewnętrzne), pozyskiwanie pożyczek UE/BGK dla MŚP (doradztwo, nie instytucja finansowa), oraz dofinansowane szkolenia zawodowe (KFS, BUR). Pełny kontekst firmy: `/01-baza-wiedzy/firma/kontekst-firmy.md`.

## Co musisz zachować bez zmian

**Logotyp.** Użyj wyłącznie plików źródłowych: `logo_irin_poziom.svg` (podstawowy), `logo_irin_pion.svg` (pola wąskie i wysokie), `logo_irin_sygnet.svg` (znak samodzielny) - wszystkie jednokolorowe. Minimalny rozmiar 18 mm w druku, 90 px na ekranie. Przestrzeń ochronna: x = wysokość liter sygnetu, mierzona od krawędzi znaku we wszystkich kierunkach; to miara względna, skalująca się ze znakiem. Znaku się nie modyfikuje: bez zmiany koloru, bez obracania, pochylania i odbijania, bez cienia, poświaty i obrysu, bez nieproporcjonalnego rozciągania - na ciemnym tle stosuj wersję odwróconą, nie przebarwioną. Pełna specyfikacja: `../01-baza-wiedzy/identyfikacja/logotyp.md`.

**Typografia.** Krój **Manrope** (wagi 200-800) jako podstawowy; **Inconsolata** pomocniczo, do danych liczbowych, metadanych i kodów usług.

**Siatka, paleta i typografia.** Wszystkie trzy specyfikacje są zatwierdzone i leżą w warstwie 1: `../01-baza-wiedzy/identyfikacja/paleta-barw.md` (14 kolorów, tokeny semantyczne, przepisane kolory etykiet, reguła 80/15/5), `../01-baza-wiedzy/identyfikacja/siatka-a4.md` (6 kolumn, moduł 25 mm, gutter 4 mm) i `../01-baza-wiedzy/identyfikacja/typografia.md` (Manrope 200-800 plus Inconsolata, dziesięciopoziomowa skala). Dane maszynowe wszystkich trzech: `../01-baza-wiedzy/identyfikacja/tokeny/palette-irin.json`. Trzymaj się dokładnie tych wartości, nie przybliżaj ich „na oko”. Osiem zasad ich użycia - w `./format-paczki.md`; trzy najważniejsze: kolor nigdy nie jest jedynym nośnikiem statusu, hierarchię typograficzną buduje waga jednego kroju, a na tle Pergaminu obowiązują inne kolory linii i ostrzeżeń niż na Kaszmirze, bo trzy pary spadają tam pod próg kontrastu.

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
