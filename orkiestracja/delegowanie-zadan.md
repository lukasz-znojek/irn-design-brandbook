# Delegowanie zadań agentom

Ta karta opisuje sposób zlecania pozostałych prac. Agent wykonuje pracę
techniczną i redakcyjną, ale nie podejmuje decyzji foundera, nie zastępuje
źródeł prawnych i nie tworzy layoutu w tym repozytorium.

## Zasada zlecenia

Jedno podzadanie GitHub = jeden mierzalny rezultat = jeden PR. W treści
zlecenia zawsze podaj:

1. numer podzadania i plik docelowy;
2. dozwolone źródła wejściowe;
3. czego agent nie może założyć ani rozstrzygnąć;
4. kryterium odbioru;
5. wymaganie, aby nie kopiować treści issue do pliku.

Agent pracuje na osobnej gałęzi, pisze po polsku, wskazuje niepewności wraz
z plikiem i wierszem oraz zostawia decyzje oznaczone `czeka-na-foundera`.

## Kolejka pracy

### 1. Weryfikacja prawna — podzadania #30–#37

Uruchom niezależnie te podzadania, gdy founder dostarczy wskazane PDF-y lub
fragmenty z nazwą dokumentu i numerem strony:

- #30–#32: Regulamin BUR, załączniki 2 i 12 oraz numeracja usług;
- #33–#34: rozporządzenie KFS i ustawa o rynku pracy;
- #35: regulamin właściwego urzędu pracy;
- #36: zasady operatora regionalnego PSF;
- #37: Księga Tożsamości Wizualnej Funduszy Europejskich, tylko jeśli IRIN
  zamierza używać tego znaku.

Każdy agent może zmienić wyłącznie pliki wskazane w
`01-baza-wiedzy/prawo/weryfikacja-u-zrodla.md` i powiązane karty warstwy 2.
Wynik musi mieć jeden z dwóch statusów: **odczytane u źródła** z wersją i
stroną albo **niesprawdzone** z nazwanym powodem. Po zakończeniu #30–#32
zleć osobne sprawdzenie, czy karty BUR i certyfikatu nie zawierają już
tymczasowych zastrzeżeń.

Nie uruchamiaj tych zadań bez dokumentów wejściowych. Brak dostępu do źródła
nie jest podstawą do zgadywania treści prawnej.

### 2. Pilot — zadanie #39

Przed wysłaniem founder uzupełnia pięć pól w
`03-pakiet-claude-design/zlecenia/pilot-papier-firmowy.md`: sąd rejestrowy,
kapitał zakładowy oraz trzy dane kontaktowe. Agent sprawdza kompletność
paczki, ale nie wpisuje brakujących wartości.

Founder uruchamia kompozycję w Claude Design. Po otrzymaniu wyniku agent
uzupełnia protokół zadań #40–#45 wyłącznie na podstawie zmierzonego PDF-u,
podglądu z siatką i odpowiedzi foundera. Każdy wynik trafia do wskazanej
specyfikacji warstwy 1.

### 3. Zamknięcie — zadania #47–#51

Zleć dopiero po przejściu etapów 2 i 4:

1. sprawdzenie bramek w `MAPA-DROGOWA.md`;
2. usunięcie otwartych pozycji z `PLAN.md` albo pozostawienie ich z jawnym
   powodem blokady;
3. aktualizacja `README.md` ze stanem i datą;
4. kontrola linków, języka polskiego i statusów weryfikacji;
5. propozycja tagu `v1.0` do zatwierdzenia przez foundera.

Agent nie tworzy tagu na `main` i nie scala PR-a. Founder zatwierdza końcowy
stan oraz wykonuje czynności administracyjne w GitHubie.

## Checklista odbioru PR

- [ ] zmieniono tylko zakres podzadania;
- [ ] każda teza prawna ma źródło, stronę albo status „niesprawdzone”;
- [ ] nie dopisano decyzji foundera ani danych zastępczych;
- [ ] zachowano trzy kategorie w kartach warstwy 2;
- [ ] layout i grafika pozostały poza repozytorium;
- [ ] PR zawiera krótki opis wyniku, ryzyka i następnego kroku.

## Szablon zlecenia

> Wykonaj podzadanie #[NUMER] dla pliku `[ŚCIEŻKA]`. Użyj wyłącznie
> `[ŹRÓDŁA]`. Nie zgaduj brakujących danych i nie rozstrzygaj pozycji
> `czeka-na-foundera`. Zaktualizuj tylko wskazane pliki, zachowaj język
> polski, podaj wersję źródła oraz numer strony. Przygotuj osobną gałąź i
> PR. Kryterium odbioru: `[MIERZALNY WYNIK]`.
