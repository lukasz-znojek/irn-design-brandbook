# Protokół pomiaru pilota — formularz do wypełnienia po powrocie z Claude Design

Pilot ma wartość tylko wtedy, gdy jego wynik trafi do warstwy 1. Ten plik jest formularzem:
wypełnia się go po obejrzeniu wyniku, a potem Claude Code przenosi wyniki do plików wskazanych
w ostatniej kolumnie. Źródło pomiarów 1–5: `../../03-pakiet-claude-design/zlecenia/pilot-papier-firmowy.md`,
sekcja 3. Pomiar 6 jest nowy — dołożony 2026-09-03, po tym jak paleta dostała kontrasty
na trzech tłach zamiast jednego.

## Zanim zaczniesz mierzyć — trzy rzeczy

1. **Mierzysz na kanwie zasianej od nowa z paczki, nie na żadnej z istniejących.** Sprawdzone
   w przeglądarce 2026-09-03: adres z 2026-09-03 zwraca „Page not found", a kanwa z 2026-09-02
   działa, ale pokazuje wersję sprzed poprawek - jej notatka mówi „Sygnet na rewersie ma 12 mm",
   choć sporną wartością jest 10 mm. Pomiar na niej mierzyłby wartości, które repozytorium już
   poprawiło. Szczegóły: `README.md` obok.
2. **Pomiary 1, 3, 4 i 6 robi się na żywej kanwie, nie na wyeksportowanym PDF-ie.** Eksport podmienia
   Manrope i Inconsolatę na kroje zastępcze, więc mierzyłbyś czcionkę systemową, a nie swoją.
3. **Przełącznik `siatka` działa osobno na każdym artboardzie**, więc do pomiaru 2 trzeba go włączyć
   dwa razy: na stronie pierwszej i na stronie kolejnej.

## Formularz

| Nr | Co sprawdzić | Co zobaczyłem (wypełnij) | Na czym (kanwa / PDF / wydruk) | Gdzie ląduje wynik |
|---|---|---|---|---|
| 1 | Polskie znaki na wagach 400, 500 i 600 — komplet 18 diakrytyków w każdej wadze, bez brakujących ogonków, kresek i zamienników z innego kroju | | | `typografia.md`, sekcja „Alfabet polski”: zamienić „pokrycie potwierdzone w zakresie, w jakim je zmierzono” na wynik, z datą |
| 2 | Siatka 6 × 25 mm z realną treścią — czy blok danych rejestrowych, logotyp i kolumna tekstu siadają na kolumnach bez łamania modułu; czy margines prawy 22 mm nie wygląda na błąd | | | `siatka-a4.md`: dopisać sekcję „Pierwsze użycie” z wynikiem |
| 3 | H3 bezpośrednio pod leadem — czy różnica wagi 500 wobec 600 przy tym samym stopniu 16 px jest widoczna bez kickera | | | `typografia.md`, sekcja o H3. Jeśli niewidoczna, zasada 5 z `format-paczki.md` zostaje potwierdzona jako konieczna |
| 4 | Sygnet samodzielny na rewersie wizytówki — zmierzona szerokość w mm i ocena czytelności; sygnet stoi w 10 mm | | | `logotyp.md`, tabela minimalnych rozmiarów. Czytelny → wiersz „10 mm / 44 px” przechodzi z „nie potwierdzony osobno” na potwierdzony; nieczytelny → wpisać zmierzone minimum |
| 5 | Dokument bez koloru dziedzinowego — czy papier w samym Aksamicie jako `primary` czyta się jako spójny z systemem 80/15/5 | | | `paleta-barw.md`, sekcja o regule 80/15/5: dopisać zdanie o dokumentach ogólnofirmowych |
| 6 | **Linie włosowe Popiołu i Złota foliowego** — czy widać je na tle Muślinu; podać grubość w mm i tło | | wymaga **wydruku**, nie samego ekranu | `paleta-barw.md`, sekcja „Trzy pary poniżej progu”: dopisać wiersz o grubości linii na Muślinie |

## Skąd wziął się pomiar 6

Do 2026-09-03 `paleta-barw.md` podawała kontrasty wyłącznie na tle Kaszmiru i stwierdzała, że
w palecie nie ma ani jednej pozycji poniżej progu. Po przeliczeniu na trzech tłach okazało się,
że trzy pary spadają pod próg na Pergaminie. Kanwa pilota Pergaminu nie używa — jej tła to Kaszmir
`#FBF8F2` i Muślin `#F6F2E9` — więc reguły 7 nie łamie. Ale na Muślinie zapas nad progiem 3:1 jest
rzędu setnych:

| Para | na Kaszmirze | na Muślinie | Próg | Zapas na Muślinie |
|---|---|---|---|---|
| Popiół `#938978` | 3,25:1 | 3,09:1 | 3:1 dla grafiki | 0,09 |
| Złoto foliowe `#A8874E` | 3,17:1 | 3,01:1 | 3:1 dla grafiki | 0,01 |

Kanwa rysuje tymi kolorami linie 0,2 mm (Popiół, obrys stopki) i 0,3 mm (Złoto foliowe, kreska
nad blokiem treści). Przy zapasie 0,01 o widoczności decyduje grubość linii i druk, nie tabela
kontrastu — dlatego ten jeden pomiar wymaga wydruku, a nie ekranu.

## Czego ten pilot nie sprawdzi

Kontrastu Karminu obok Aksamitu na realnym dokumencie. Papier firmowy i wizytówka nie mają stanu
błędu, więc Karmin się na nich nie pojawia. Ten falsyfikator czeka na pierwszy dokument ze statusami
(certyfikat albo karta usługi BUR) i jest tak zapisany w mapie drogowej, bramka B.

## Po wypełnieniu

Claude Code przenosi wyniki do czterech plików warstwy 1 z ostatniej kolumny, a potem zamyka
zadanie 22 w `PLAN.md` i bramkę B w `MAPA-DROGOWA.md`. Rozbieżność „wyszło inaczej niż specyfikacja”
nie jest przenoszona automatycznie: idzie do właściciela jako pytanie, czy poprawiamy dokument,
czy specyfikację.
