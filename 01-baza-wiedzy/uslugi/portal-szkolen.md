# Wytyczne usługowe — portal sprzedaży szkoleń online

Status: portal **jeszcze nie istnieje** — jest w fazie planowania (potwierdzone w `/PLAN.md`, zadanie 6, i w `/CLAUDE.md`). Ten plik opisuje ustalony dotąd kierunek, nie gotowy produkt — każda karta specyfikacji dokumentu odwołująca się do portalu (np. materiały promocyjne) powinna to jawnie zaznaczać jako zapowiedź, nie ofertę istniejącej usługi.

## Model — rozstrzygnięty przez foundera

Model **hybrydowy** (`/PLAN.md`, sekcja "Decyzje foundera — rozstrzygnięte"):
- portal **sprzedaje miejsca** na szkolenia, w tym szkolenia dofinansowane w ramach KFS i BUR (patrz `../prawo/kfs.md`, `../prawo/bur.md`),
- pozwala je **zrealizować zdalnie** — webinary i materiały do pobrania,
- **bez pełnej platformy LMS** (systemu do zarządzania nauczaniem z odtwarzaniem kursów, testami i śledzeniem postępu kursanta) — ten element świadomie pozostaje poza zakresem portalu.

## Konsekwencje dla treści dokumentów

- Portal **nie jest** platformą e-learningową z automatyczną walidacją postępu ani systemem testów — treści opisujące portal nie powinny sugerować funkcji LMS (np. "śledzenie Twojego postępu w kursie", "automatyczne testy końcowe"), bo to wykraczałoby poza ustalony zakres.
- Skoro portal sprzedaje też miejsca na szkolenia dofinansowane (KFS/BUR), materiały portalu będą musiały jasno rozróżniać ścieżkę **pełnopłatną** od ścieżki **dofinansowanej** — z odrębnymi wymogami formalnymi tej drugiej (patrz `../prawo/kfs.md` i `../prawo/bur.md`), np. co do dokumentów, które uczestnik musi dostarczyć, żeby skorzystać z dofinansowania.
- Realizacja zdalna (webinary + materiały do pobrania) oznacza, że opis usługi na portalu powinien od razu precyzować format zajęć (na żywo vs. samodzielna nauka z materiałów) — to rozróżnienie jest też wymogiem formalnym karty usługi BUR od 5 maja 2026 r. (pole "wariant zajęć", patrz `../prawo/bur.md`), więc dobrze zaprojektowany opis usługi na portalu może od razu zbierać dane potrzebne też do karty usługi BUR.

## Wymóg prawny dla realizacji zdalnej: Standard SUZ

Odczytane u źródła 2026-09-06. Regulamin BUR § 15 ust. 3 (`../prawo/zrodla/regulamin-bazy-uslug-rozwojowych_wersja-2026-05-05.pdf`, s. 24): „W przypadku realizacji Usług rozwojowych realizowanych w formie zdalnej Dostawca Usług jest zobowiązany do jej świadczenia zgodnie ze Standardem Usług Zdalnego Uczenia się (SUZ), stanowiącym Załącznik 5 do Regulaminu.”

Skutek dla portalu: **każde szkolenie sprzedane przez portal i zrealizowane zdalnie w ramach BUR podlega czternastu wymaganiom SUZ-1 do SUZ-14** - to nie jest zbiór dobrych praktyk, tylko warunek zgodności usługi. Pełny odczyt: `../prawo/bur.md`, sekcja „Usługi zdalne - Standard SUZ jest wiążący”. Cztery wymagania, które trzeba rozstrzygnąć **zanim** portal ruszy, bo dotyczą jego treści i konstrukcji, a nie samej organizacji szkolenia:

- **SUZ-1** (s. 6): zakres walidacji obejmuje wprost pytanie „Czy Dostawca Usług stosuje zasady ustawy o dostępności cyfrowej, stron internetowych i aplikacji mobilnych.” Portal jest serwisem internetowym, więc dotyczy go to bezpośrednio. **Niesprawdzone:** czy IRIN jako spółka prywatna jest podmiotem tej ustawy z mocy prawa, czy dopiero ten zapis SUZ czyni z niej wymóg umowny wobec PARP - repozytorium nie ma treści tej ustawy (domena `isap.sejm.gov.pl` zablokowana, patrz `../prawo/weryfikacja-u-zrodla.md`). Do rozstrzygnięcia przed budową portalu, bo zmienia zakres prac.
- **SUZ-2** (s. 7): „Dostawca Usług publikuje rzetelne informacje dotyczące swojej działalności”, a jako źródła dowodów standard wymienia stronę internetową dostawcy, dokumenty ofertowe i publikacje w kanałach marketingowych. Teksty na portalu są objęte tym wymaganiem tak samo jak karta usługi.
- **SUZ-3** (s. 7-8): dostawca „jasno komunikuje zakres licencji i dozwolony sposób użytkowania” produktów cyfrowych. Materiały do pobrania z portalu potrzebują jawnej informacji o licencji - to nowy element treści, którego dotychczasowy opis portalu nie przewidywał.
- **SUZ-8** (s. 10): funkcjonalności, narzędzia i materiały „zgodnie z określonymi standardami technicznymi zapewniającymi ich dostępność i kompatybilność, również w kontekście urządzeń mobilnych”, z przywołaniem SCORM i xAPI. Uwaga: to nie unieważnia decyzji o braku LMS - SCORM i xAPI są wymienione jako przykłady standardów, a wymaganie dotyczy dostępności i kompatybilności materiałów, nie posiadania platformy.

Czego SUZ **nie** narzuca: żadnego poziomu WCAG, wartości kontrastu ani wymogów typograficznych (przejrzano wszystkie 15 stron). Reguły kontrastu z `../identyfikacja/paleta-barw.md` pozostają konwencją IRIN.

## Braki — do potwierdzenia przez foundera

Repozytorium nie zawiera: nazwy/marki portalu, planowanego terminu uruchomienia, wybranej technologii webinarów, zakresu materiałów do pobrania (pliki, nagrania, inne), ani modelu cenowego. Te decyzje nie są tu zgadywane — karta specyfikacji dowolnego dokumentu odwołującego się do portalu powinna je traktować jako otwarte, nie domyślne.
