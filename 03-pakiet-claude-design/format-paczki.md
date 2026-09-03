# Format paczki wejściowej dla Claude Design

Ten plik definiuje, co powinna zawierać paczka wejściowa przekazywana do Claude Design dla dowolnego dokumentu IRIN. Sama kompozycja, layout i grafika powstają w Claude Design — ten plik tylko określa, jakie materiały i informacje muszą się tam znaleźć, żeby to było możliwe.

## Specyfikacje obowiązujące - wszystkie w warstwie 1

Kolor, siatka i typografia mają jedno miejsce każde, w `../01-baza-wiedzy/identyfikacja/`. Ten plik ich nie powtarza - jedna specyfikacja ma jedno źródło, żeby nie dało się rozjechać dwóch kopii.

| Co | Gdzie | Dane maszynowe |
|---|---|---|
| Paleta barw, 14 kolorów | [`paleta-barw.md`](../01-baza-wiedzy/identyfikacja/paleta-barw.md) | [`palette-irin.json`](../01-baza-wiedzy/identyfikacja/tokeny/palette-irin.json) |
| Siatka A4 | [`siatka-a4.md`](../01-baza-wiedzy/identyfikacja/siatka-a4.md) | ten sam plik, klucz `siatka-a4` |
| Typografia i skala | [`typografia.md`](../01-baza-wiedzy/identyfikacja/typografia.md) | ten sam plik, klucz `typografia` |
| Logotyp: rozmiary, przestrzeń ochronna, zakazy | [`logotyp.md`](../01-baza-wiedzy/identyfikacja/logotyp.md) | ten sam plik, klucz `logotyp` |

Trzymaj się dokładnie wartości z warstwy 1, nie przybliżaj ich „na oko”.

### Zasady, bez których same wartości są niekompletne

Poniższe **muszą** trafić do każdego zlecenia dla Claude Design razem z wartościami - to nie są szczegóły do wyczytania z tabel, a reguły, które te tabele interpretują.

1. **Jeden kolor dziedziny na dokument.** Aksamit (Pedagogika), Miedź (Akademia AI) albo Onyks (Pożyczki UE/BGK) - nigdy dwa naraz. To warstwa 15% reguły 80/15/5.
2. **Kolor etykiety na wypełnieniu nie jest wyborem projektowym.** Na każdym kolorze, który bywa tłem przycisku albo plakietki, kolor napisu jest przepisany w tabeli w warstwie 1. Nie dobieraj go „na oko”.
3. **Kolor nigdy nie jest jedynym nośnikiem statusu.** Każdy stan potrzebuje etykiety słownej albo ikony obok koloru. Po konwersji do skali szarości Werdykt, Rubryka, Karmin i Onyks mają zbliżoną jasność, a osobny tryb monochromatyczny został odrzucony - więc to jest jedyne zabezpieczenie czytelności, nie jedno z dwóch.

4. **Hierarchię buduje waga jednego kroju, nie zmiana rodziny.** Manrope na wszystko, Inconsolata wyłącznie na liczby, kody usług i metadane. Nie dobieraj trzeciego kroju.
5. **H3 odróżnia się od leadu wyłącznie wagą.** Te dwa poziomy nie powinny stać bezpośrednio obok siebie; jeśli muszą, użyj kickera.
6. **Siatka to sześć kolumn, zawsze.** Liczba kolumn jest wspólna dla wszystkich trzech dziedzin - to element tożsamości, nie parametr do dobierania per dokument.
7. **Na tle Pergaminu obowiązują inne kolory linii i ostrzeżeń niż na Kaszmirze.** Pergamin jest ciemniejszy o około 20 % luminancji i trzy pary spadają na nim pod próg: Popiół 2,61:1 i Złoto foliowe 2,55:1 (próg 3:1 dla grafiki), Rubryka jako tekst 4,18:1 (próg 4,5:1). Wewnątrz calloutu i na każdym polu o tle Pergaminu obrys prowadzi się Sepią, kreskę ozdobną Miedzią, a ostrzeżenie pisze Espresso z etykietą słowną. Tabela dla trzech teł: `/01-baza-wiedzy/identyfikacja/paleta-barw.md`, sekcja „Trzy pary poniżej progu”.
8. **Na materiale IRIN nie stawia się znaku Funduszy Europejskich, znaku barw RP ani flagi Unii Europejskiej.** Dotyczy każdego dokumentu dziedziny Pożyczki UE/BGK. To zakaz, nie brak obowiązku: Podręcznik informacji i promocji FE (rozdz. 8.7, s. 22) wprost nie pozwala umieszczać w zestawieniu znaków podmiotów, które nie są beneficjentami, a IRIN jest doradcą zewnętrznym. Nazwę programu wolno napisać w treści, oznaczyć nim materiału - nie. Uzasadnienie i falsyfikator: `/01-baza-wiedzy/prawo/pozyczki-ue-bgk.md`.

## Elementy paczki, potwierdzone i gotowe do użycia

### 1. Logotyp

Trzy pliki źródłowe leżą w korzeniu repozytorium i **wchodzą do paczki bez modyfikacji**: `logo_irin_poziom.svg` (podstawowy), `logo_irin_pion.svg` (pola wąskie i wysokie), `logo_irin_sygnet.svg` (znak samodzielny).

Pełna specyfikacja - proporcje, minimalne rozmiary, przestrzeń ochronna i zakazy - jest w warstwie 1: [`../01-baza-wiedzy/identyfikacja/logotyp.md`](../01-baza-wiedzy/identyfikacja/logotyp.md).

Trzy rzeczy, które muszą trafić do zlecenia razem z plikami:

- **Minimalny rozmiar: 18 mm w druku, 90 px na ekranie.** Poniżej znak nie wchodzi.
- **Przestrzeń ochronna x = wysokość liter sygnetu**, mierzona z każdej strony. Miara względna, skaluje się ze znakiem - nie da się jej zastąpić stałym marginesem strony.
- **Znaku się nie modyfikuje.** Bez zmiany koloru, bez obracania, pochylania i odbijania, bez cienia, poświaty i obrysu, bez nieproporcjonalnego rozciągania. Na ciemnym tle stosuje się wersję odwróconą, nie przebarwioną.

### 2. Treść merytoryczna — z warstwy 1 i 2

Dla każdego zlecenia do Claude Design paczka musi zawierać:
- **odpowiednią kartę specyfikacji z warstwy 2** (`/02-szablony-dokumentow/`) — określa, jakie elementy treści są prawnie obowiązkowe, konwencją organizacyjną i swobodnym wyborem projektowym dla danego typu dokumentu,
- **odpowiednie pliki z warstwy 1** (`/01-baza-wiedzy/`) wskazane przez tę kartę specyfikacji — fakty o firmie, przepisy prawne, wytyczne usługowe potrzebne do wypełnienia treści,
- **rzeczywiste dane wejściowe** dla konkretnego dokumentu (np. konkretne szkolenie, konkretny uczestnik, konkretne dane rejestrowe) — te nie są generowane w tym repozytorium i muszą przyjść od foundera przy każdym zleceniu.

## Czego paczka nie zawiera

Gotowego layoutu, kompozycji, wyboru konkretnych elementów graficznych poza logotypem — to wszystko rozstrzyga się w Claude Design, zgodnie z podziałem warstw z `/CLAUDE.md`.
