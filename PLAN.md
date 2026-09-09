# Destylacja na paletę Regalia - plan wykonawczy

> **Dla wykonawcy:** realizuj ten plan zadanie po zadaniu, w kolejności.
> Skończ zadanie, zweryfikuj je, zatrzymaj się do przeglądu, dopiero potem
> zacznij następne. Kroki mają składnię pola wyboru (`- [ ]`) do odhaczania.

**Cel:** przepisać warstwę 1 repozytorium na paletę Regalia (14 wartości, prefiks
`--irin-r-`), bez iteracji v2-v5.1 i bez historii palet, a potem zasiać z tego
czystego repozytorium nowy projekt Claude Design.

**Architektura:** repozytorium ma jedno maszynowe źródło prawdy -
`01-baza-wiedzy/identyfikacja/tokeny/palette-irin.json`. Wszystko inne (cztery
specyfikacje `.md`, `tokens.css`, `styles.css`, osiem kart podglądu) jest z niego
wywiedzione i sprawdzane skryptem, który przelicza każdą zadeklarowaną liczbę od
zera. Skrypt jest bramką: dopóki nie przechodzi, żadne twierdzenie o zgodności
systemu nie ma podstawy. Kierunek synchronizacji zostaje jeden - repozytorium do
projektu.

**Stos:** Python 3.11 (bramka pomiarowa, biblioteka standardowa), Node 22 plus
Playwright/Chromium (pomiar obwiedni znaku, na żądanie), CSS ze zmiennymi
własnymi, Markdown, `DesignSync` (odczyt starego projektu, zasiew nowego).
Brak buildu, brak zależności runtime - ten stan zostaje.

**Specyfikacja:** [`POMIAR.md`](./POMIAR.md), w szczególności rozdz. 4 (rachunki),
rozdz. 9.1 (14 wartości Regalii z weryfikacją) i rozdz. 9.5 (rozjazdy R7-R15).
Plan argumentuje z tego pomiaru; wykonawca czyta oba pliki.

**Decyzja, z której ten plan wynika:** właściciel, 2026-09-09 - repozytorium
przechodzi na Regalię od razu (nie przez warstwę v5.1), destylacja bez iteracji
i bez historii palet, kolejność: najpierw repozytorium, potem nowy projekt.

---

## Ograniczenia globalne

Wymagania każdego zadania zawierają w sobie tę sekcję.

**Język i zapis**
- Każdy commitowany plik po polsku: nazwa pliku, nagłówki, treść. Wyjątkiem są
  identyfikatory techniczne wymuszone przez narzędzia.
- Przecinek dziesiętny, dwa miejsca po przecinku. `4,78` a nie `4.78` i nie `4,8`.
- **Dywiz `-`, nigdy myślnik ani półpauza** (znaki U+2014 i U+2013), także
  w zakresach liczb i dat. Kontroluje to `_robocze/narzedzia/sprawdz-dywizy.py`
  (zadanie 12), nie grep - `grep -P` z klasą `\x{...}` zawodzi w części środowisk.
- Dane rejestrowe spółki są potwierdzone i wpisywane wprost: `Instytut Rozwoju
  i Nauki sp. z o.o.`, `ul. Karola Olszewskiego 6, 25-663 Kielce`,
  `KRS 0001032499`, `NIP 9592061542` (ciągiem, bez spacji), `REGON 525113640`,
  kapitał zakładowy `40 000,00 zł`, `Sąd Rejonowy w Kielcach, X Wydział
  Gospodarczy KRS`. Dane kontaktowe nie mają potwierdzonej wartości - stoją jako
  placeholdery w [NAWIASACH KWADRATOWYCH] realnej długości. **Zero zmyślonych
  wartości.**

**Czternaście wartości Regalii - przepisać dokładnie**

| Klucz | Nazwa | Hex |
|---|---|---|
| `szafir-nocny` | Szafir Nocny | `#132246` |
| `atrament` | Atrament | `#07090C` |
| `kosc-sloniowa` | Kość Słoniowa | `#F7F3E9` |
| `aksamit-nocy` | Aksamit Nocy | `#080F1F` |
| `alabaster` | Alabaster | `#E4E1D8` |
| `grafit-jedwabny` | Grafit Jedwabny | `#606369` |
| `zloto-szampanskie` | Złoto Szampańskie | `#C4B790` |
| `ametyst-dworski` | Ametyst Dworski | `#331F41` |
| `muszla-rozana` | Muszla Różana | `#E8D6D6` |
| `lapis-stonowany` | Lapis Stonowany | `#305686` |
| `zloto-antyczne` | Złoto Antyczne | `#75674B` |
| `rubin-gleboki` | Rubin Głęboki | `#541319` |
| `zielen-butelkowa` | Zieleń Butelkowa | `#0B3627` |
| `bursztyn-wyciszony` | Bursztyn Wyciszony | `#9B5E30` |

Cztery tinty 12 % krycia na Kości Słoniowej: Szafir `#DCDAD5`, Rubin `#E3D8D0`,
Zieleń `#DBDCD2`, Ametyst `#DFDAD5`. Wszystkie cztery odtwarzają się z mieszania
co do bajtu - bramka to sprawdza.

**Reguły, które muszą przetrwać każde zadanie**
1. **Regalia nie ma tokenów stanu.** Nie ma `success`, `warning` ani `error`.
   Stan niesie słowo plus jedna z barw nośnych dobrana w dokumencie.
2. **Kolor nigdy nie jest jedynym nośnikiem statusu** - każdy stan potrzebuje
   etykiety słownej albo ikony (WCAG 1.4.1).
3. **Barwa obszaru idzie przez gniazdo `--irin-r-dziedzina`, nigdy wprost.**
   Domyślnie gniazdo wskazuje Szafir Nocny, więc materiał bez obszaru wychodzi
   poprawnie bez żadnej podmiany. Pułapka: Rubin Głęboki bywa też barwą
   oznaczenia - nie podmieniaj go globalnie.
4. **Barwę znaku ustawia `color` kontenera i `fill: currentColor`. Nigdy
   `filter:`.**
5. **Złoto Szampańskie nigdy jako tekst na jasnym** (1,80:1 na Kości Słoniowej),
   nigdy jako tło większej powierzchni, nigdy jako linia niosąca strukturę.
   Wyłącznie kreska ozdobna od 0,5 mm, pieczęć i tłoczenie.
6. **Na materiale IRIN nie stoi znak Funduszy Europejskich, znak barw RP ani
   flaga UE** - także przekreślone. Nazwę programu wolno napisać słowem.
   Podstawa: Podręcznik informacji i promocji FE, rozdz. 8.7, s. 22.
7. **Podłoga składu: 8,5 px = 6,38 pt.** Rachunek: 8,5 × 72/96 = 6,375 pt.
   Strona projektowa zapisuje `6,4 pt` - to ta sama liczba do jednego miejsca.
   W repozytorium obowiązuje zapis dwumiejscowy, więc **6,38 pt**, i nikt tego
   nie „poprawia" z powrotem.
8. **Layout, kompozycja i grafika nie powstają w repozytorium.** Repozytorium
   trzyma treść, wartości i wytyczne. Wzory nośników mieszkają w `templates/`
   po stronie projektu.
9. **Reguła, której nie da się spełnić, zostaje komentarzem w kodzie z liczbą.**
   Nie obchodź jej po cichu.
10. **Nie podnoś wersji paczki bez uzgodnienia, co się w niej faktycznie
    zmieniło.**

**Czego ten plan nie robi**
- Nie zmienia siatki A4: 210 × 297 mm, 6 kolumn, moduł 25 mm, gutter 4 mm,
  marginesy 18 / 20 / 28 / 20 mm, pole treści 170 × 251 mm, jednostka 6 mm.
  Te wartości przeszły pomiar i decyzję; zmienia się tylko liczba dryfu.
- Nie zmienia krojów ani skali typograficznej poza dołożeniem jedenastego
  poziomu 8,5 px.
- Nie zmienia plików logotypu. Trzy pliki SVG w korzeniu zostają nietknięte.
- Nie rusza `01-baza-wiedzy/prawo/`, `01-baza-wiedzy/firma/`,
  `01-baza-wiedzy/uslugi/` ani `02-szablony-dokumentow/`. Tam nie ma palety.
- Nie kasuje starego projektu Claude Design. Zadanie 14 oznacza go jako
  archiwum; usunięcie jest decyzją właściciela, nie krokiem planu.

---

## Struktura plików

### Tworzone

| Plik | Odpowiedzialność |
|---|---|
| `_robocze/narzedzia/sprawdz-palete.py` | **bramka pomiarowa.** Czyta `palette-irin.json`, przelicza od zera każdy kontrast, każdy tint, limit złota, arytmetykę siatki i dryf rytmu. Kod wyjścia 0 = wszystko odtwarzalne. |
| `_robocze/narzedzia/sprawdz-zgodnosc-md.py` | **bramka spójności tekstu.** Wyciąga z czterech specyfikacji `.md` i z ośmiu kart każdy hex i każdy kontrast, sprawdza, czy występuje w JSON-ie. Łapie liczby przepisane zamiast policzonych. |
| `_robocze/narzedzia/zmierz-znak.mjs` | pomiar obwiedni znaku widocznego w Chromium (`getBBox`). Uruchamiany na żądanie, nie w bramce - wymaga przeglądarki. |
| `_robocze/ds-bundle/fonts/OFL.txt` | tekst licencji SIL Open Font License 1.1. Wymóg dystrybucji: licencja podróżuje z fontem. |
| `.github/workflows/bramka-pomiarowa.yml` | uruchomienie obu bramek na każdym PR. |

### Przepisywane w całości

| Plik | Co się zmienia |
|---|---|
| `01-baza-wiedzy/identyfikacja/tokeny/palette-irin.json` | Regalia, jedno źródło maszynowe. Bez v2, bez v5.1, bez sekcji archiwalnych. |
| `01-baza-wiedzy/identyfikacja/paleta-barw.md` | 14 wartości, tabela par zabronionych z brakującym wierszem Lapisu, limit 5 %, gniazdo obszaru. Bez tabeli „co się zmieniło". |
| `01-baza-wiedzy/identyfikacja/typografia.md` | jedenasty poziom 8,5 px = 6,38 pt; dryf 20,86 mm zamiast 19 mm. |
| `01-baza-wiedzy/identyfikacja/siatka-a4.md` | dryf 20,86 mm; sekcje historyczne zdjęte; siatka slajdu jako jawna propozycja. |
| `01-baza-wiedzy/identyfikacja/logotyp.md` | konwencja obwiedni znaku widocznego, współczynniki 0,655 i 0,561, przeliczone minima. |
| `_robocze/ds-bundle/tokens/tokens.css` | prefiks `--irin-r-`, 14 barw, 4 tinty, gniazdo obszaru, limit złota. Bez bloku v2. |
| `_robocze/ds-bundle/styles.css` | tokeny Regalii; dołożone reguły druku. |
| `_robocze/ds-bundle/components/**/*.html` | osiem kart podglądu na Regalii. |
| `_robocze/ds-bundle/guidelines/*.md` | kopie czterech specyfikacji plus zasady użycia; odnośniki naprawione. |
| `PLAN.md` | ten plan; rejestr decyzji foundera przeniesiony na koniec. |

### Modyfikowane punktowo

| Plik | Co się zmienia |
|---|---|
| `CLAUDE.md` | sekcja o palecie: Regalia zamiast „Kaszmir Wyciszony"; usunięte hexy palety 12-kolorowej z opisu kanwy. |
| `03-pakiet-claude-design/format-paczki.md` | osiem zasad na Regalii, bez tokenów stanu. |
| `03-pakiet-claude-design/prompt-bazowy.md` | odesłania do nowej palety. |
| `README.md` | stan i data. |
| `.design-sync/config.json` | identyfikator nowego projektu (zadanie 14). |
| `.gitignore` | zdjęty szablon AL / Dynamics 365, zostają trzy żywe wpisy. |
| `_robocze/brandbook-warianty/wariant-*.dc.html` | wycofany Popiół `#938978` (R3), 6 wystąpień. |

### Nietykane

Trzy pliki SVG logotypu w korzeniu, `brandbook.dc.html`, `01-baza-wiedzy/prawo/`
z dziesięcioma PDF-ami, `01-baza-wiedzy/firma/`, `01-baza-wiedzy/uslugi/`,
`02-szablony-dokumentow/`, `_robocze/copilot-v1/`, `_robocze/paleta-v2/`,
`MAPA-DROGOWA.md`, `POMIAR.md`.

`_robocze/paleta-v2/` i `brandbook.dc.html` zostają **świadomie**: to archiwum
i kanwa wyjściowa, oznaczone jako takie w `CLAUDE.md`. „Bez historii" dotyczy
warstwy 1 i paczki, nie poligonu.

---
# BLOK A - repozytorium

## Zadanie 1: Bramka pomiarowa

Bramka jest pierwsza, bo bez niej każde następne zadanie kończy się słowem
„zgodne" bez pokrycia. Bramka przelicza od zera każdą liczbę zadeklarowaną
w `palette-irin.json` i **nie importuje generatora** - inaczej nie sprawdzałaby
niczego.

**Pliki:**
- Utwórz: `_robocze/narzedzia/sprawdz-palete.py`

**Interfejsy:**
- Konsumuje: nic.
- Produkuje: `python3 _robocze/narzedzia/sprawdz-palete.py [ścieżka]`, kod wyjścia
  0 = każda liczba odtwarzalna, 1 = rozjazd, 2 = plik nieczytelny. Wypisuje
  liczbę sprawdzonych twierdzeń i listę rozjazdów. Zadania 2-12 wołają ją bez
  argumentu.

- [x] **Krok 1: Napisz bramkę**

Treść pliku `_robocze/narzedzia/sprawdz-palete.py`:

```python
#!/usr/bin/env python3
"""Bramka pomiarowa systemu projektowego IRIN.

Czyta palette-irin.json i przelicza od zera KAŻDĄ zadeklarowaną w nim liczbę:
kontrasty wzorem WCAG 2.1, tinty z mieszania, limit akcentu, arytmetykę siatki,
dryf rytmu pionowego, przeliczenia stopni i współczynniki pola znaku.

Nie importuje generatora - liczy własnym kodem. Inaczej nie sprawdzałaby niczego.

Uruchomienie: python3 _robocze/narzedzia/sprawdz-palete.py [ścieżka-do-json]
Kod wyjścia 0 = każda liczba odtwarzalna. 1 = rozjazd. 2 = plik nieczytelny.
"""
import json, pathlib, sys
from decimal import Decimal, ROUND_HALF_UP

EPS = 1e-9   # liczby są generowane, więc porównanie jest do zaokrąglonej wartości
ROOT = pathlib.Path(__file__).resolve().parents[2]
DOMYSLNY = ROOT / "01-baza-wiedzy/identyfikacja/tokeny/palette-irin.json"
MM_PX = 96 / 25.4
PX_PT = 72 / 96

def zaokr(x, miejsc=2):
    """Zaokrąglenie połówek w górę, ten sam rachunek co w generatorze."""
    kwant = Decimal(1).scaleb(-miejsc)
    return float(Decimal(repr(x)).quantize(kwant, rounding=ROUND_HALF_UP))

def lin(k):
    k = k / 255
    return k / 12.92 if k <= 0.04045 else ((k + 0.055) / 1.055) ** 2.4

def luminancja(hx):
    h = hx.lstrip("#")
    return (0.2126 * lin(int(h[0:2], 16))
            + 0.7152 * lin(int(h[2:4], 16))
            + 0.0722 * lin(int(h[4:6], 16)))

def kontrast(a, b):
    la, lb = luminancja(a), luminancja(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)

def mieszaj(fg, bg, krycie):
    f = [int(fg.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4)]
    t = [int(bg.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4)]
    return "#%02X%02X%02X" % tuple(
        int(zaokr(f[i] * krycie + t[i] * (1 - krycie), 0)) for i in range(3))

def pl(x, m=2):
    return f"{x:.{m}f}".replace(".", ",")


class Bramka:
    def __init__(self):
        self.bledy, self.sprawdzonych = [], 0

    def rowne(self, opis, jest, ma_byc, miejsc=2):
        """Porównuje wartość z pliku z policzoną, zaokrągloną do tylu miejsc,
        ile plik deklaruje. Bez tolerancji - liczba albo się odtwarza, albo nie."""
        self.sprawdzonych += 1
        cel = zaokr(ma_byc, miejsc)
        if abs(jest - cel) > EPS:
            self.bledy.append(f"{opis}: w pliku {pl(jest, miejsc)}, policzone {pl(cel, miejsc)} "
                              f"(rozjazd {pl(jest - cel, miejsc + 2)})")

    def identyczne(self, opis, jest, ma_byc):
        self.sprawdzonych += 1
        if jest != ma_byc:
            self.bledy.append(f"{opis}: w pliku {jest}, policzone {ma_byc}")

    def prawda(self, opis, warunek):
        self.sprawdzonych += 1
        if not warunek:
            self.bledy.append(opis)


def sprawdz(d, b):
    # --- paleta jest tą, którą ma być -------------------------------------
    b.identyczne("nazwa palety", d.get("nazwa"), "Regalia")
    b.identyczne("prefiks tokenów", d.get("prefiks-tokenow"), "--irin-r-")
    b.prawda("paleta ma dokładnie 14 barw, jest "
             f"{len(d.get('barwy', {}))}", len(d.get("barwy", {})) == 14)
    b.prawda("Regalia nie ma tokenów stanu", d.get("tokeny-stanu", {}).get("sa") is False)
    for zly in ("success", "warning", "error"):
        b.prawda(f"token stanu '{zly}' nie występuje w barwach", zly not in d.get("barwy", {}))

    hexy = {k: v["hex"] for k, v in d["barwy"].items()}

    # --- tinty odtwarzają się z mieszania, co do bajtu --------------------
    for nazwa, t in d.get("tinty", {}).items():
        b.identyczne(f"tint {nazwa}",
                     t["hex"], mieszaj(hexy[t["podstawa"]], hexy[t["podloze"]], t["krycie"]))
        b.rowne(f"Atrament na tincie {nazwa}",
                t["atrament-na-tincie"], kontrast(hexy["atrament"], t["hex"]))

    wszystkie = dict(hexy, **{f"tint-{n}": t["hex"] for n, t in d.get("tinty", {}).items()})

    # --- kontrasty: każdy przeliczony, każda ocena sprawdzona -------------
    for grupa, zabroniona in (("kontrasty-dopuszczone", False), ("kontrasty-zabronione", True)):
        for w in d.get(grupa, []):
            k = kontrast(wszystkie[w["tekst"]], wszystkie[w["tlo"]])
            b.rowne(f"{grupa}: {w['tekst']} na {w['tlo']}", w["kontrast"], k)
            prog = 3.0 if w["rodzaj"] == "grafika" else 4.5
            if zabroniona:
                b.prawda(f"para zabroniona {w['tekst']} na {w['tlo']} musi być pod progiem "
                         f"{pl(prog)} (jest {pl(k)})", k < prog)
                b.prawda(f"para zabroniona {w['tekst']} na {w['tlo']} musi mieć zamiennik",
                         bool(w.get("zamiast")))
            else:
                b.prawda(f"para dopuszczona {w['tekst']} na {w['tlo']} musi przechodzić próg "
                         f"{pl(prog)} (jest {pl(k)})", k >= prog)

    # --- macierz na tłach nośnych ----------------------------------------
    for barwa, wiersz in d.get("macierz-na-tlach-nosnych", {}).items():
        for tlo, wart in wiersz.items():
            if wart is None:
                b.prawda(f"macierz: {barwa} na {tlo} jest null tylko dla samej siebie", barwa == tlo)
            else:
                b.rowne(f"macierz: {barwa} na {tlo}", wart, kontrast(hexy[barwa], hexy[tlo]))

    # --- każda para zadeklarowana jako dopuszczona nie może stać na liście zabronionych
    dop = {(w["tekst"], w["tlo"]) for w in d.get("kontrasty-dopuszczone", [])}
    zab = {(w["tekst"], w["tlo"]) for w in d.get("kontrasty-zabronione", [])}
    b.prawda(f"żadna para nie stoi na obu listach naraz: {sorted(dop & zab)}", not (dop & zab))

    # --- KOMPLETNOŚĆ: każda para pod progiem musi być na liście zabronionych
    # albo jawnie wypisana jako nieużywana. To jest bramka na R12 z POMIAR.md.
    tla = d.get("tla-nosne", [])
    poza = set(map(tuple, d.get("pary-nieuzywane", [])))
    for barwa in hexy:
        for tlo in tla:
            if barwa == tlo:
                continue
            k = kontrast(hexy[barwa], hexy[tlo])
            if k < 3.0 and (barwa, tlo) not in zab and (barwa, tlo) not in poza:
                b.bledy.append(f"KOMPLETNOŚĆ: {barwa} na {tlo} daje {pl(k)} (pod progiem 3), "
                               f"a nie ma tej pary ani w kontrastach-zabronionych, "
                               f"ani w parach-nieuzywanych")
            b.sprawdzonych += 1

    # --- siatka: arytmetyka domyka się co do milimetra --------------------
    s = d["siatka-a4"]
    m, strona = s["marginesy-mm"], s["strona-mm"]
    szer = strona[0] - m["lewy"] - m["prawy"]
    wys = strona[1] - m["gora"] - m["dol"]
    b.rowne("pole treści, szerokość", s["pole-tresci-mm"][0], szer, 0)
    b.rowne("pole treści, wysokość", s["pole-tresci-mm"][1], wys, 0)
    suma = s["kolumny"] * s["modul-mm"] + (s["kolumny"] - 1) * s["gutter-mm"]
    b.rowne("suma kolumn i gutterów", s["suma-siatki-mm"], suma, 0)
    b.prawda(f"siatka domyka się co do milimetra: {suma} = {szer}", suma == szer)
    b.prawda("flaga dopasowania zgodna z rachunkiem",
             s["dopasowanie-dokladne"] == (suma == szer))
    b.rowne("pole treści w cm2", s["pole-tresci-cm2"], szer * wys / 100)

    # --- rytm pionowy: to jest bramka na R1 z POMIAR.md -------------------
    r = s["rytm-pionowy"]
    korpus = d["typografia"]["skala"]["korpus"]
    inter = korpus["rozmiar-px"] * korpus["interlinia"] / MM_PX
    b.rowne("interlinia korpusu w mm", r["interlinia-korpusu-mm"], inter)
    linii = int(wys // inter)
    b.rowne("liczba linii korpusu w polu treści", r["linii-w-polu-tresci"], linii, 0)
    na_linie = s["jednostka-odstepu-mm"] - inter
    b.rowne("dryf na linię", r["dryf-na-linie-mm"], na_linie)
    b.rowne("dryf na pełnej kolumnie", r["dryf-na-pelnej-kolumnie-mm"], na_linie * linii)
    b.prawda(f"liczba dryfu w prozie zgadza się z polem "
             f"({pl(r['dryf-na-pelnej-kolumnie-mm'])} mm)",
             pl(r["dryf-na-pelnej-kolumnie-mm"]) in r["uwaga"])
    b.prawda(f"liczba linii w prozie zgadza się z polem ({linii})",
             f"{linii} linii" in r["uwaga"])

    # --- limit akcentu ----------------------------------------------------
    lim = d["regula-proporcji"]["limit-akcentu"]
    b.rowne("podstawa limitu", lim["podstawa-cm2"], s["pole-tresci-cm2"])
    b.rowne("limit akcentu w cm2", lim["limit-cm2"], lim["podstawa-cm2"] * lim["procent"] / 100)
    b.prawda(f"rachunek limitu w prozie zawiera {pl(lim['limit-cm2'])}",
             pl(lim["limit-cm2"]) in lim["rachunek"])

    # --- typografia: przeliczenia stopni i podłoga ------------------------
    for nazwa, p in d["typografia"]["skala"].items():
        b.rowne(f"stopień {nazwa} w pt", p["rozmiar-pt"], p["rozmiar-px"] * PX_PT)
        b.rowne(f"stopień {nazwa} w mm", p["rozmiar-mm"], p["rozmiar-px"] / MM_PX)
    pod = d["typografia"]["podloga-skladu"]
    b.rowne("podłoga składu w pt", pod["pt"], pod["px"] * PX_PT)
    b.rowne("podłoga składu w mm", pod["mm"], pod["px"] / MM_PX)
    najmniejszy = min(p["rozmiar-px"] for p in d["typografia"]["skala"].values())
    b.prawda(f"żaden poziom skali nie schodzi pod podłogę {pod['px']} px "
             f"(najmniejszy {najmniejszy} px)", najmniejszy >= pod["px"])

    # --- logotyp: współczynniki pola i przeliczone minima -----------------
    lg = d["logotyp"]
    for plik, p in lg["pliki"].items():
        vb_szer, vb_wys = p["viewbox"]
        _, _, ob_szer, ob_wys = p["obwiednia-znaku-widocznego"]
        b.rowne(f"{plik}: proporcja viewboksu", p["proporcja-viewboksu"], vb_szer / vb_wys, 4)
        b.rowne(f"{plik}: proporcja znaku widocznego", p["proporcja-znaku-widocznego"], ob_szer / ob_wys, 4)
        b.rowne(f"{plik}: współczynnik pola", p["wspolczynnik-pola"], ob_szer / vb_szer, 3)
        b.rowne(f"{plik}: pole pliku dla minimum druku",
                p["pole-pliku-dla-minimum-druku-mm"],
                lg["minimalny-rozmiar"]["druk-mm"] / p["wspolczynnik-pola"])
        b.prawda(f"{plik}: obwiednia mieści się w viewboksie",
                 ob_szer <= vb_szer and ob_wys <= vb_wys)
    b.prawda("logotyp: cztery zakazy", len(lg["zakazy"]) == 4)
    b.prawda("logotyp: barwa przez currentColor, nigdy filter",
             "filter" in lg["barwa-znaku"] and "currentColor" in lg["barwa-znaku"])

    # --- gniazdo obszaru --------------------------------------------------
    g = d["gniazdo-obszaru"]
    b.identyczne("gniazdo obszaru: token", g["token"], "--irin-r-dziedzina")
    b.prawda(f"gniazdo domyślnie wskazuje istniejącą barwę ({g['domyslnie']})",
             g["domyslnie"] in hexy)
    for barwa in g["barwy-dostepne"]:
        b.prawda(f"barwa dostępna {barwa} istnieje w palecie", barwa in hexy)
        k = kontrast(hexy["kosc-sloniowa"], hexy[barwa])
        b.prawda(f"Kość Słoniowa na barwie obszaru {barwa} przechodzi próg 3 "
                 f"dla znaku (jest {pl(k)})", k >= 3.0)


def main():
    sciezka = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else DOMYSLNY
    try:
        d = json.loads(sciezka.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"BRAMKA: nie mogę odczytać {sciezka}: {e}")
        return 2
    b = Bramka()
    try:
        sprawdz(d, b)
    except KeyError as e:
        print(f"BRAMKA: brak wymaganego klucza {e} w {sciezka}")
        return 1
    print(f"BRAMKA POMIAROWA - {sciezka}")
    print(f"  sprawdzonych twierdzeń: {b.sprawdzonych}")
    print(f"  rozjazdów: {len(b.bledy)}")
    for w in b.bledy:
        print(f"    ! {w}")
    if b.bledy:
        print("\nBRAMKA ZAMKNIĘTA. Dopóki tu jest choć jeden wiersz, żadne twierdzenie")
        print("o zgodności systemu nie ma podstawy.")
        return 1
    print("\nBRAMKA OTWARTA. Każda liczba w pliku odtwarza się z rachunku.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
```

- [x] **Krok 2: Uruchom bramkę na obecnym pliku - musi ODMÓWIĆ**

```bash
python3 _robocze/narzedzia/sprawdz-palete.py; echo "kod wyjścia: $?"
```

Oczekiwane: `BRAMKA: brak wymaganego klucza 'barwy'` i **kod wyjścia 1**.
Obecny plik niesie paletę v2 o innej strukturze - bramka nie ma czego sprawdzać
i mówi to wprost. To jest dowód, że bramka nie przechodzi „na wszystkim".

- [x] **Krok 3: Sprawdź, że bramka łapie podmianę - osiem prób**

Bramka bez tego kroku jest ozdobą. Zapisz `/tmp/proba-bramki.py`:

```python
import json, pathlib, subprocess, copy, sys
baza = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"))
def probuj(nazwa, mutacja):
    d = copy.deepcopy(baza); mutacja(d)
    pathlib.Path("/tmp/mutant.json").write_text(json.dumps(d, ensure_ascii=False), encoding="utf-8")
    r = subprocess.run(["python3", "_robocze/narzedzia/sprawdz-palete.py", "/tmp/mutant.json"],
                       capture_output=True, text=True)
    print(f"{nazwa}: kod {r.returncode}" + ("  !!! DZIURA" if r.returncode == 0 else "  złapane"))
probuj("1 podmieniony hex barwy", lambda d: d["barwy"]["rubin-gleboki"].__setitem__("hex", "#905E88"))
probuj("2 kontrast z sąsiedniego wiersza", lambda d: d["kontrasty-dopuszczone"][0].__setitem__("kontrast", 17.25))
probuj("3 tint wpisany ręcznie", lambda d: d["tinty"]["szafir"].__setitem__("hex", "#DCDAD6"))
probuj("4 para pod progiem zdjęta z listy", lambda d: d.__setitem__("kontrasty-zabronione",
    [w for w in d["kontrasty-zabronione"] if w["tekst"] != "lapis-stonowany"]))
probuj("5 dryf przepisany jako 19 mm", lambda d: d["siatka-a4"]["rytm-pionowy"].__setitem__(
    "dryf-na-pelnej-kolumnie-mm", 19.0))
probuj("6 dołożony token stanu", lambda d: d["barwy"].__setitem__("warning",
    {"nazwa": "Ostrzeżenie", "hex": "#9B5E30", "rola": "stan"}))
probuj("7 margines bez przeliczenia pola", lambda d: d["siatka-a4"]["marginesy-mm"].__setitem__("dol", 27))
probuj("8 poziom skali pod podłogą", lambda d: d["typografia"]["skala"].__setitem__(
    "mikro", {"rozmiar-px": 7, "rozmiar-pt": 5.25, "rozmiar-mm": 1.85, "rola": "test"}))
```

Uruchomienie odłóż do kroku 3 zadania 2 - potrzebuje poprawnego pliku jako bazy.

- [x] **Krok 4: Commit**

```bash
git add _robocze/narzedzia/sprawdz-palete.py
git commit -m "Bramka pomiarowa: każda liczba palety przeliczana od zera"
```

---

## Zadanie 2: Generator palety, `palette-irin.json` i `tokens.css`

Jedno źródło, dwa wyjścia. Każdy kontrast jest **policzony przy składaniu**,
nie przepisany - to strukturalna odpowiedź na błąd, który zjadł warstwę v5.1
po stronie projektowej (`POMIAR.md`, R7 i R8: po wymianie barwy zostały stare
liczby kontrastu, jedna z nich poniżej progu dostępności). Przy tym układzie
taka pomyłka jest niemożliwa: żeby zmienić barwę, zmienia się jeden wiersz
tabeli `BARWY`, a liczby lecą za nią same.

**Pliki:**
- Utwórz: `_robocze/narzedzia/zloz-palete.py`
- Nadpisz: `01-baza-wiedzy/identyfikacja/tokeny/palette-irin.json` (generowany)
- Nadpisz: `_robocze/ds-bundle/tokens/tokens.css` (generowany)

**Interfejsy:**
- Konsumuje: bramkę z zadania 1.
- Produkuje: `palette-irin.json` o kluczach `barwy`, `tinty`, `tla-nosne`,
  `gniazdo-obszaru`, `tokeny-stanu`, `kontrasty-dopuszczone`,
  `kontrasty-zabronione`, `pary-nieuzywane`, `macierz-na-tlach-nosnych`,
  `regula-proporcji`, `minimalna-grubosc-linii-mm`, `siatka-a4`, `typografia`,
  `logotyp`, `falsyfikatory-otwarte`. Klucze barw są slugami
  (`szafir-nocny`, `kosc-sloniowa`, …) i zadania 4-11 odwołują się do nich
  dokładnie tak. Tokeny CSS: `--irin-r-<slug>`, `--irin-r-tint-<nazwa>`,
  `--irin-r-dziedzina`, `--irin-r-tint-dziedzina` plus trzynaście aliasów
  semantycznych (`primary`, `surface`, `surface-alt`, `surface-dark`, `text`,
  `text-invert`, `text-muted`, `border`, `accent`, `link`, `highlight`, `info`,
  `przekrojowy`).

- [x] **Krok 1: Napisz generator**

Treść pliku `_robocze/narzedzia/zloz-palete.py`:

```python
#!/usr/bin/env python3
"""Składa palette-irin.json z tabeli wartości zmierzonych.

Każdy kontrast w wynikowym pliku jest POLICZONY tutaj, nie przepisany. To jest
odpowiedź na błąd, który zjadł warstwę v5.1: po wymianie barwy zostały tam stare
liczby kontrastu (POMIAR.md, R7 i R8). Przy tym układzie taka pomyłka jest
niemożliwa - żeby zmienić barwę, zmienia się jeden wiersz tabeli BARWY, a liczby
lecą za nią same.

Uruchomienie: python3 _robocze/narzedzia/zloz-palete.py
Zapisuje: 01-baza-wiedzy/identyfikacja/tokeny/palette-irin.json
"""
import json, pathlib, sys
from decimal import Decimal, ROUND_HALF_UP

ROOT = pathlib.Path(__file__).resolve().parents[2]
CEL_JSON = ROOT / "01-baza-wiedzy/identyfikacja/tokeny/palette-irin.json"
CEL_CSS = ROOT / "_robocze/ds-bundle/tokens/tokens.css"

# --- rachunek WCAG 2.1 -------------------------------------------------------

def zaokr(x, miejsc=2):
    """Zaokrąglenie połówek w górę - tak, jak rozumie je człowiek pisząc
    „dwa miejsca po przecinku". Wbudowane round() zaokrągla połówki do liczby
    parzystej i dawałoby 10,12 tam, gdzie w specyfikacji ma stać 10,13."""
    kwant = Decimal(1).scaleb(-miejsc)
    return float(Decimal(repr(x)).quantize(kwant, rounding=ROUND_HALF_UP))

def lin(k):
    k = k / 255
    return k / 12.92 if k <= 0.04045 else ((k + 0.055) / 1.055) ** 2.4

def luminancja(hx):
    h = hx.lstrip("#")
    return (0.2126 * lin(int(h[0:2], 16))
            + 0.7152 * lin(int(h[2:4], 16))
            + 0.0722 * lin(int(h[4:6], 16)))

def kontrast(a, b):
    la, lb = luminancja(a), luminancja(b)
    hi, lo = max(la, lb), min(la, lb)
    return zaokr((hi + 0.05) / (lo + 0.05))

def pl(x, miejsc=2):
    """Liczba w zapisie polskim: przecinek dziesiętny, stała liczba miejsc."""
    return f"{x:.{miejsc}f}".replace(".", ",")

def mieszaj(fg, bg, krycie):
    f = [int(fg.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4)]
    t = [int(bg.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4)]
    return "#%02X%02X%02X" % tuple(
        int(zaokr(f[i] * krycie + t[i] * (1 - krycie), 0)) for i in range(3))

def ocena(k, rodzaj):
    """rodzaj: 'tekst' (progi 4,5 i 7) albo 'grafika' (próg 3)."""
    if rodzaj == "grafika":
        return "OK" if k >= 3.0 else "PONIŻEJ PROGU"
    if k >= 7.0:
        return "AAA"
    if k >= 4.5:
        return "AA"
    return "PONIŻEJ PROGU"

# --- dane zmierzone ----------------------------------------------------------
# Jedyne miejsce, w którym stoi wartość wpisana ręcznie. Wszystko poniżej liczy się.

BARWY = [
    ("szafir-nocny",       "Szafir Nocny",       "#132246", "kolor marki: logotyp, pasy nagłówkowe, wypełnienia CTA"),
    ("atrament",           "Atrament",           "#07090C", "typografia główna: korpus, nagłówki, tabele"),
    ("kosc-sloniowa",      "Kość Słoniowa",      "#F7F3E9", "tło strony; wersja odwrócona znaku"),
    ("aksamit-nocy",       "Aksamit Nocy",       "#080F1F", "tło ciemne: sekcje, stopki, okładki wewnętrzne"),
    ("alabaster",          "Alabaster",          "#E4E1D8", "tła kart, wiersze naprzemienne, tekst drugi na ciemnym"),
    ("grafit-jedwabny",    "Grafit Jedwabny",    "#606369", "tekst drugi na jasnym, linie struktury od 0,25 mm"),
    ("zloto-szampanskie",  "Złoto Szampańskie",  "#C4B790", "akcent do 5 %: kreska ozdobna od 0,5 mm, pieczęć, tłoczenie"),
    ("ametyst-dworski",    "Ametyst Dworski",    "#331F41", "materiał przekrojowy: kategorie i tagi wspólne"),
    ("muszla-rozana",      "Muszla Różana",      "#E8D6D6", "jasny akcent: cytaty, podświetlenia, ramki wyróżnień"),
    ("lapis-stonowany",    "Lapis Stonowany",    "#305686", "interakcja: odnośniki, stan aktywny, obrys focus"),
    ("zloto-antyczne",     "Złoto Antyczne",     "#75674B", "akcent informacyjny: podpowiedzi, metadane, ikony"),
    ("rubin-gleboki",      "Rubin Głęboki",      "#541319", "barwa dostępna, nieprzypisana do obszaru"),
    ("zielen-butelkowa",   "Zieleń Butelkowa",   "#0B3627", "barwa dostępna, nieprzypisana do obszaru"),
    ("bursztyn-wyciszony", "Bursztyn Wyciszony", "#9B5E30", "barwa dostępna, nieprzypisana do obszaru"),
]

TINTY = [("szafir", "szafir-nocny"), ("rubin", "rubin-gleboki"),
         ("zielen", "zielen-butelkowa"), ("ametyst", "ametyst-dworski")]
KRYCIE_TINTU = 0.12
PODLOZE_TINTU = "kosc-sloniowa"

TLA = ["kosc-sloniowa", "aksamit-nocy", "alabaster"]

# Pary jawnie dopuszczone. rodzaj decyduje o progu.
DOPUSZCZONE = [
    ("atrament", "kosc-sloniowa", "tekst", "korpus, nagłówki, tabele"),
    ("kosc-sloniowa", "aksamit-nocy", "tekst", "sekcje ciemne, stopka"),
    ("atrament", "alabaster", "tekst", "karty, wiersze tabel"),
    ("alabaster", "aksamit-nocy", "tekst", "tekst drugi na ciemnym"),
    ("atrament", "muszla-rozana", "tekst", "cytaty, wyróżnienia"),
    ("kosc-sloniowa", "szafir-nocny", "tekst", "pas nagłówkowy, CTA"),
    ("kosc-sloniowa", "ametyst-dworski", "tekst", "tagi, kategorie"),
    ("kosc-sloniowa", "rubin-gleboki", "tekst", "wypełnienia sekcji"),
    ("kosc-sloniowa", "zielen-butelkowa", "tekst", "wypełnienia sekcji"),
    ("muszla-rozana", "rubin-gleboki", "tekst", "etykieta na wypełnieniu"),
    ("atrament", "zloto-szampanskie", "tekst", "etykieta na wypełnieniu złotym"),
    ("zloto-szampanskie", "aksamit-nocy", "tekst", "kicker na tle ciemnym"),
    ("lapis-stonowany", "kosc-sloniowa", "tekst", "odnośniki i stan aktywny"),
    ("lapis-stonowany", "alabaster", "tekst", "odnośnik na karcie"),
    ("grafit-jedwabny", "kosc-sloniowa", "tekst", "tekst drugi na jasnym"),
    ("zloto-antyczne", "kosc-sloniowa", "tekst", "podpowiedzi, metadane"),
    ("bursztyn-wyciszony", "kosc-sloniowa", "tekst", "jedyne dopuszczone tło Bursztynu"),
    ("grafit-jedwabny", "kosc-sloniowa", "grafika", "linia struktury od 0,25 mm"),
]

# Pary zabronione. Każda z zamiennikiem. Wiersz Lapisu to R12 z POMIAR.md -
# reguła istniała w prozie jednego szablonu, tu wchodzi do specyfikacji.
ZABRONIONE = [
    ("zloto-szampanskie", "kosc-sloniowa", "tekst",
     "złoto wyłącznie jako kreska, tłoczenie albo wypełnienie z etykietą Atramentem"),
    ("lapis-stonowany", "aksamit-nocy", "tekst",
     "odnośnik na tle ciemnym idzie Złotem Szampańskim (kontrast wyżej) albo Kością Słoniową z podkreśleniem"),
    ("bursztyn-wyciszony", "alabaster", "tekst",
     "Bursztyn ma jedno dopuszczone tło: Kość Słoniowa"),
    ("bursztyn-wyciszony", "aksamit-nocy", "tekst",
     "ostrzeżenie na ciemnym: wypełnienie bursztynowe z etykietą Kością Słoniową"),
    ("zloto-antyczne", "aksamit-nocy", "tekst",
     "na ciemnym wchodzi Złoto Szampańskie"),
    ("grafit-jedwabny", "aksamit-nocy", "tekst",
     "tekst drugi na ciemnym: Alabaster"),
]

# Pary pod progiem 3, które nigdy nie wchodzą do składu, bo nikt by ich nie
# złożył: barwa ciemna na ciemnym tle albo jasna na jasnym. Bramka wymaga, żeby
# KAŻDA para pod progiem była jawnie wypisana - albo tu, albo jako zabroniona
# z zamiennikiem. Bez tej reguły przeoczenie w rodzaju R12 (Lapis na Aksamicie
# Nocy, 2,55) znowu przeszłoby niezauważone.
NIEUZYWANE = [
    ("szafir-nocny", "aksamit-nocy"),
    ("atrament", "aksamit-nocy"),
    ("ametyst-dworski", "aksamit-nocy"),
    ("rubin-gleboki", "aksamit-nocy"),
    ("zielen-butelkowa", "aksamit-nocy"),
    ("kosc-sloniowa", "alabaster"),
    ("alabaster", "kosc-sloniowa"),
    ("zloto-szampanskie", "alabaster"),
    ("muszla-rozana", "kosc-sloniowa"),
    ("muszla-rozana", "alabaster"),
]

SIATKA = {"strona-mm": [210, 297], "kolumny": 6, "modul-mm": 25, "gutter-mm": 4,
          "marginesy-mm": {"gora": 18, "lewy": 20, "prawy": 20, "dol": 28},
          "jednostka-odstepu-mm": 6}

SKALA = [
    ("display",  200, 72,   0.92, "-0.03em", None,        "okładka"),
    ("h1",       300, 40,   1.0,  "-0.02em", None,        "rozdział"),
    ("h2",       600, 24,   1.1,  "-0.01em", None,        "sekcja"),
    ("h3",       600, 16,   1.3,  None,      None,        "podsekcja"),
    ("lead",     500, 16,   1.4,  None,      None,        "lead akapitu"),
    ("korpus",   400, 13.5, 1.55, None,      None,        "korpus"),
    ("meta",     400, 10,   1.5,  None,      None,        "przypis, metadane"),
    ("kicker",   700, 14,   1.2,  "0.22em",  "uppercase", "drogowskaz sekcji"),
    ("liczba",   800, 52,   0.95, "-0.02em", None,        "liczba prowadząca"),
    ("dane",     None, 10.5, 1.5, None,      None,        "Inconsolata: dane, kody, metadane"),
    ("techniczny", None, 8.5, 1.4, None,     None,        "podłoga składu: nagłówki tabel, przypisy, pas nadawcy"),
]

# Obwiednie znaku widocznego, zmierzone w Chromium (getBBox). Odtwarza je
# _robocze/narzedzia/zmierz-znak.mjs. Format: [x, y, szerokość, wysokość].
OBWIEDNIE = {
    "logo_irin_poziom.svg": {"viewbox": [281.333, 158.667], "obwiednia": [48.561, 59.907, 184.213, 38.854],
                             "zastosowanie": "wariant podstawowy"},
    "logo_irin_pion.svg":   {"viewbox": [184.837, 162.834], "obwiednia": [40.555, 37.593, 103.728, 87.312],
                             "zastosowanie": "pola wąskie i wysokie"},
    "logo_irin_sygnet.svg": {"viewbox": [184.837, 162.834], "obwiednia": [40.555, 61.991, 103.728, 38.853],
                             "zastosowanie": "znak samodzielny"},
}
MIN_DRUK_MM = 18
MIN_EKRAN_PX = 90
MIN_SYGNET_MM = 10

# --- składanie ---------------------------------------------------------------

def zloz():
    hexy = {k: h for k, _, h, _ in BARWY}
    nazwy = {k: n for k, n, _, _ in BARWY}

    barwy = {k: {"nazwa": n, "hex": h, "rola": r} for k, n, h, r in BARWY}

    tinty = {}
    for nazwa_t, baza in TINTY:
        hx = mieszaj(hexy[baza], hexy[PODLOZE_TINTU], KRYCIE_TINTU)
        tinty[nazwa_t] = {
            "hex": hx, "podstawa": baza, "krycie": KRYCIE_TINTU,
            "podloze": PODLOZE_TINTU,
            "atrament-na-tincie": kontrast(hexy["atrament"], hx),
            "rola": "wyłącznie tła kart i pasy tabel w obrębie obszaru; nie kolor tekstu ani linii",
        }
    wszystkie = dict(hexy, **{f"tint-{n}": t["hex"] for n, t in tinty.items()})

    def para(a, b, rodzaj, uwaga, zamiast=None):
        k = kontrast(wszystkie[a], wszystkie[b])
        w = {"tekst": a, "tlo": b, "kontrast": k, "rodzaj": rodzaj,
             "ocena": ocena(k, rodzaj), "uwaga": uwaga}
        if zamiast:
            w["zamiast"] = zamiast
        return w

    dopuszczone = [para(a, b, r, u) for a, b, r, u in DOPUSZCZONE]
    for n in tinty:
        dopuszczone.append(para("atrament", f"tint-{n}", "tekst",
                                f"karta i pas tabeli na tincie {n} 12 %"))
    zabronione = [para(a, b, r, "para zabroniona", z) for a, b, r, z in ZABRONIONE]

    # macierz pełna: 14 barw x 3 tła nośne, do wglądu
    macierz = {}
    for k in hexy:
        macierz[k] = {t: (None if k == t else kontrast(hexy[k], hexy[t])) for t in TLA}

    szer = SIATKA["strona-mm"][0] - SIATKA["marginesy-mm"]["lewy"] - SIATKA["marginesy-mm"]["prawy"]
    wys = SIATKA["strona-mm"][1] - SIATKA["marginesy-mm"]["gora"] - SIATKA["marginesy-mm"]["dol"]
    suma_siatki = SIATKA["kolumny"] * SIATKA["modul-mm"] + (SIATKA["kolumny"] - 1) * SIATKA["gutter-mm"]
    pole_cm2 = zaokr(szer * wys / 100)

    MM_PX = 96 / 25.4
    korpus = next(p for p in SKALA if p[0] == "korpus")
    inter_mm = korpus[2] * korpus[3] / MM_PX
    linii = int(wys // inter_mm)
    dryf_na_linie = SIATKA["jednostka-odstepu-mm"] - inter_mm
    dryf_kolumny = zaokr(dryf_na_linie * linii)

    siatka = dict(SIATKA)
    siatka.update({
        "pole-tresci-mm": [szer, wys],
        "pole-tresci-cm2": pole_cm2,
        "suma-siatki-mm": suma_siatki,
        "dopasowanie-dokladne": suma_siatki == szer,
        "rachunek-szerokosci": f"{SIATKA['kolumny']} x {SIATKA['modul-mm']} + "
                               f"{SIATKA['kolumny']-1} x {SIATKA['gutter-mm']} = {suma_siatki} mm "
                               f"= {SIATKA['strona-mm'][0]} - {SIATKA['marginesy-mm']['lewy']} - "
                               f"{SIATKA['marginesy-mm']['prawy']}",
        "rytm-pionowy": {
            "interlinia-korpusu-mm": zaokr(inter_mm),
            "linii-w-polu-tresci": linii,
            "dryf-na-linie-mm": zaokr(dryf_na_linie),
            "dryf-na-pelnej-kolumnie-mm": dryf_kolumny,
            "uwaga": "Jednostka odstępu, nie siatka linii bazowych tekstu. "
                     f"Interlinia korpusu {pl(inter_mm)} mm nie jest wielokrotnością "
                     f"{SIATKA['jednostka-odstepu-mm']} mm - rozjazd {pl(dryf_na_linie)} mm na linię "
                     f"i {pl(dryf_kolumny)} mm na pełnej kolumnie {linii} linii. "
                     "Wymierzaj nią odstępy między blokami, nie linie tekstu.",
        },
        "strefy": {
            "gora-mm": SIATKA["marginesy-mm"]["gora"],
            "gora-rola": "strefa znaku i nagłówka strony, nie treści",
            "dol-mm": SIATKA["marginesy-mm"]["dol"],
            "dol-rola": "strefa stopki: linia oddzielająca i jeden pas metadanych; "
                        "dolna krawędź tekstu nie schodzi bliżej niż 12 mm od krawędzi strony",
        },
    })

    limit_cm2 = zaokr(pole_cm2 * 0.05)

    PX_PT = 72 / 96
    skala = {}
    for k, waga, px, inter, tracking, transform, rola in SKALA:
        w = {"rozmiar-px": px, "rozmiar-pt": zaokr(px * PX_PT),
             "rozmiar-mm": zaokr(px / MM_PX), "rola": rola}
        if waga: w["waga"] = waga
        if inter: w["interlinia"] = inter
        if tracking: w["tracking"] = tracking
        if transform: w["transform"] = transform
        if k in ("dane", "techniczny"): w["rodzina"] = "Inconsolata"
        skala[k] = w

    logotyp = {"pliki": {}, "jednokolorowy": True,
               "minimalny-rozmiar": {"druk-mm": MIN_DRUK_MM, "ekran-px": MIN_EKRAN_PX,
                                     "sygnet-samodzielny-mm": MIN_SYGNET_MM},
               "konwencja-pomiaru": "Każdy wymiar znaku podany w systemie IRIN jest szerokością "
                                    "OBWIEDNI ZNAKU WIDOCZNEGO, nie szerokością pola pliku. "
                                    "Pliki mają w viewBoksie puste pole; wstawienie znaku na "
                                    "szerokość pola daje znak mniejszy od zadeklarowanego.",
               "przestrzen-ochronna": "x = wysokość liter sygnetu, mierzona z każdej strony znaku; "
                                      "miara względna, skaluje się ze znakiem",
               "zakazy": [
                   "nie zmieniamy koloru znaku; na ciemnym tle wersja odwrócona, nie przebarwiona",
                   "nie obracamy, nie pochylamy, nie odbijamy lustrzanie",
                   "nie dodajemy cienia, poświaty ani obrysu",
                   "nie rozciągamy nieproporcjonalnie",
               ],
               "barwa-znaku": "przez color kontenera i fill: currentColor; nigdy filter:"}
    for plik, d in OBWIEDNIE.items():
        vb_szer, vb_wys = d["viewbox"]
        _, _, ob_szer, ob_wys = d["obwiednia"]
        wsp = zaokr(ob_szer / vb_szer, 3)
        logotyp["pliki"][plik] = {
            "viewbox": d["viewbox"], "obwiednia-znaku-widocznego": d["obwiednia"],
            "proporcja-viewboksu": zaokr(vb_szer / vb_wys, 4),
            "proporcja-znaku-widocznego": zaokr(ob_szer / ob_wys, 4),
            "wspolczynnik-pola": wsp,
            "pole-pliku-dla-minimum-druku-mm": zaokr(MIN_DRUK_MM / wsp),
            "zastosowanie": d["zastosowanie"],
        }

    return {
        "schemat": "irin-palette",
        "wersja": "regalia-1.0.0",
        "nazwa": "Regalia",
        "status": "ZATWIERDZONA przez foundera 2026-09-03; wpisana do warstwy 1 repozytorium 2026-09-09",
        "prefiks-tokenow": "--irin-r-",
        "plik-zrodlowy": "_robocze/narzedzia/zloz-palete.py",
        "jak-odtworzyc": "python3 _robocze/narzedzia/zloz-palete.py, potem "
                         "python3 _robocze/narzedzia/sprawdz-palete.py",
        "metodologia-kontrastu": "WCAG 2.1, luminancja względna sRGB. Progi: tekst normalny AA 4,5:1, "
                                 "AAA 7:1; element interfejsu i grafika znacząca 3:1. Każda liczba "
                                 "w tym pliku jest policzona przy składaniu, nie przepisana.",
        "specyfikacja-obowiazujaca": {
            "kolor": "01-baza-wiedzy/identyfikacja/paleta-barw.md",
            "siatka": "01-baza-wiedzy/identyfikacja/siatka-a4.md",
            "typografia": "01-baza-wiedzy/identyfikacja/typografia.md",
            "logotyp": "01-baza-wiedzy/identyfikacja/logotyp.md",
        },
        "barwy": barwy,
        "tinty": tinty,
        "tla-nosne": TLA,
        "gniazdo-obszaru": {
            "token": "--irin-r-dziedzina",
            "domyslnie": "szafir-nocny",
            "token-tintu": "--irin-r-tint-dziedzina",
            "domyslnie-tint": "tint-szafir",
            "zasada": "Obszary działalności są wymienne, więc barwy nie są im przypisane. "
                      "Materiał obszarowy nadpisuje u siebie te dwa tokeny i nic więcej. "
                      "Materiał bez obszaru wychodzi poprawnie bez żadnej podmiany.",
            "barwy-dostepne": ["rubin-gleboki", "zielen-butelkowa", "bursztyn-wyciszony", "ametyst-dworski"],
            "pulapka": "Rubin Głęboki bywa też barwą oznaczenia - nie podmieniaj go globalnie.",
        },
        "tokeny-stanu": {
            "sa": False,
            "powod": "Trzy barwy, które mogłyby je pełnić, są jednocześnie kandydatami na barwy "
                     "obszarów; przypisanie ich do roli statusu zabetonowałoby to, co ma być wymienne.",
            "skutek": "Stan niesie słowo plus jedna z barw nośnych dobrana w dokumencie. "
                      "Kolor nigdy nie jest jedynym nośnikiem statusu (WCAG 1.4.1).",
        },
        "kontrasty-dopuszczone": dopuszczone,
        "kontrasty-zabronione": zabronione,
        "pary-nieuzywane": [list(p) for p in NIEUZYWANE],
        "pary-nieuzywane-uzasadnienie":
            "Pary pod progiem 3, które nie wchodzą do składu, bo są barwą ciemną na ciemnym "
            "tle albo jasną na jasnym. Wypisane jawnie, żeby bramka mogła sprawdzić, że żadna "
            "para pod progiem nie została przeoczona.",
        "macierz-na-tlach-nosnych": macierz,
        "regula-proporcji": {
            "schemat": "80/15/5",
            "baza-80": ["kosc-sloniowa", "atrament", "alabaster", "grafit-jedwabny"],
            "obszar-15": "dokładnie jedna barwa z gniazda na dokument, nigdy dwie naraz",
            "akcent-5": ["zloto-szampanskie"],
            "limit-akcentu": {
                "podstawa-cm2": pole_cm2,
                "procent": 5,
                "limit-cm2": limit_cm2,
                "rachunek": f"{szer} x {wys} mm = {pl(pole_cm2)} cm2; 5 % = {pl(limit_cm2)} cm2",
            },
            "poza-budzetem": ["lapis-stonowany", "zloto-antyczne", "muszla-rozana"],
        },
        "minimalna-grubosc-linii-mm": {
            "struktura": 0.25, "ozdoba": 0.5,
            "uwaga": "Poniżej tych wartości o widoczności decyduje raster drukarki, nie luminancja. "
                     "NIEPOTWIERDZONE NA WYDRUKU - falsyfikator otwarty.",
        },
        "siatka-a4": siatka,
        "typografia": {
            "rodzina-podstawowa": "Manrope", "wagi-podstawowe": [200, 300, 400, 500, 600, 700, 800],
            "rodzina-pomocnicza": "Inconsolata", "wagi-pomocnicze": [300, 400, 500, 600, 700],
            "zasada": "Hierarchię buduje waga jednego kroju, nie zmiana rodziny. Manrope na wszystko, "
                      "Inconsolata wyłącznie na liczby, kody usług i metadane. Trzeciego kroju nie ma.",
            "podloga-skladu": {"px": 8.5, "pt": zaokr(8.5 * PX_PT), "mm": zaokr(8.5 / MM_PX),
                               "uwaga": "Nic mniejszego nie wchodzi do składu. Adnotacje rysunku "
                                        "w makietach w skali są wyjątkiem i muszą być tak opisane w kodzie."},
            "skala": skala,
            "licencja-krojow": "SIL Open Font License 1.1; tekst licencji podróżuje z fontem "
                               "(_robocze/ds-bundle/fonts/OFL.txt)",
            "pokrycie-diakrytykow": {
                "znaki": "ĄĆĘŁŃÓŚŹŻ ąćęłńóśźż",
                "manrope": "18/18", "inconsolata": "18/18",
                "metoda": "cmap rozpakowanych woff2, kontur sprawdzony BoundsPen; oba kroje zmienne, "
                          "więc pokrycie nie może różnić się między wagami",
                "niepotwierdzone": "czytelność ogonków na wydruku przy stopniu podłogi - falsyfikator otwarty",
            },
        },
        "logotyp": logotyp,
        "falsyfikatory-otwarte": [
            "grubość linii struktury 0,25 mm i kreski ozdobnej 0,5 mm na wydruku",
            "minimalny rozmiar samodzielnego sygnetu 10 mm",
            "czytelność diakrytyków na papierze przy stopniu podłogi 8,5 px",
            "CMYK palety bez proofu na papierze docelowym",
            "Złoto Szampańskie na papierze niepowlekanym",
            "przypisanie barw dostępnych do obszarów działalności",
        ],
    }

def mm(x):
    """Wymiar w CSS: kropka dziesiętna, bez wiodącego zera. 0,25 -> .25mm"""
    return f"{x:g}".lstrip("0") + "mm"


def zloz_css(d):
    """tokens.css wywiedziony z tego samego źródła co JSON. Ani jednej wartości
    wpisanej drugi raz - inaczej arkusz i dane maszynowe mogłyby się rozjechać."""
    L = ["/* Tokeny systemu projektowego IRIN - paleta Regalia.",
         " *",
         " * PLIK GENEROWANY. Nie edytuj go ręcznie: zmiany przepadną przy następnym",
         " * złożeniu. Wartości zmienia się w _robocze/narzedzia/zloz-palete.py, potem",
         " * uruchamia się ten skrypt i bramkę sprawdz-palete.py.",
         " *",
         f" * Źródło prawdy: {CEL_JSON.relative_to(ROOT)}",
         f" * Paleta: {d['nazwa']}, {d['wersja']}, {d['status']}",
         " */",
         "",
         ":root {",
         "  /* --- czternaście barw nośnych --- */"]
    szer_klucza = max(len(k) for k in d["barwy"])
    for k, v in d["barwy"].items():
        nazwa = f"--irin-r-{k}:"
        L.append(f"  {nazwa:<{szer_klucza + 12}} {v['hex']};   /* {v['nazwa']} - {v['rola']} */")
    L += ["", "  /* --- tinty 12 % krycia na Kości Słoniowej; wyłącznie tła kart i pasy tabel --- */"]
    for k, v in d["tinty"].items():
        L.append(f"  --irin-r-tint-{k+':':<{szer_klucza + 1}} {v['hex']};"
                 f"   /* Atrament na tincie {pl(v['atrament-na-tincie'])} */")
    g = d["gniazdo-obszaru"]
    L += ["", "  /* --- GNIAZDO OBSZARU: jedno miejsce do podmiany ---",
          f"     {g['zasada']}",
          f"     Pułapka: {g['pulapka']} --- */",
          f"  --irin-r-dziedzina:      var(--irin-r-{g['domyslnie']});",
          f"  --irin-r-tint-dziedzina: var(--irin-r-{g['domyslnie-tint']});",
          "", "  /* --- aliasy semantyczne: w kodzie token, w rozmowie nazwa własna --- */"]
    for alias, cel in [("primary", "szafir-nocny"), ("surface", "kosc-sloniowa"),
                       ("surface-alt", "alabaster"), ("surface-dark", "aksamit-nocy"),
                       ("text", "atrament"), ("text-invert", "kosc-sloniowa"),
                       ("text-muted", "grafit-jedwabny"), ("border", "grafit-jedwabny"),
                       ("accent", "zloto-szampanskie"), ("link", "lapis-stonowany"),
                       ("highlight", "muszla-rozana"), ("info", "zloto-antyczne"),
                       ("przekrojowy", "ametyst-dworski")]:
        L.append(f"  --irin-r-{alias+':':<{szer_klucza + 1}} var(--irin-r-{cel});")
    L += ["", "  /* --- BRAK TOKENÓW STANU. To jest decyzja, nie przeoczenie. ---",
          f"     {d['tokeny-stanu']['powod']}",
          f"     {d['tokeny-stanu']['skutek']} --- */", ""]
    s_ = d["siatka-a4"]
    L += ["  /* --- siatka A4; rachunek: " + s_["rachunek-szerokosci"] + " --- */",
          f"  --irin-r-strona-szer:     {s_['strona-mm'][0]}mm;",
          f"  --irin-r-strona-wys:      {s_['strona-mm'][1]}mm;",
          f"  --irin-r-kolumny:         {s_['kolumny']};",
          f"  --irin-r-modul:           {s_['modul-mm']}mm;",
          f"  --irin-r-gutter:          {s_['gutter-mm']}mm;",
          f"  --irin-r-margines-gora:   {s_['marginesy-mm']['gora']}mm;",
          f"  --irin-r-margines-bok:    {s_['marginesy-mm']['lewy']}mm;",
          f"  --irin-r-margines-dol:    {s_['marginesy-mm']['dol']}mm;",
          f"  --irin-r-pole-szer:       {s_['pole-tresci-mm'][0]}mm;",
          f"  --irin-r-pole-wys:        {s_['pole-tresci-mm'][1]}mm;",
          f"  --irin-r-jednostka:       {s_['jednostka-odstepu-mm']}mm;",
          "", "  /* --- kroje; podłoga składu "
          f"{pl(d['typografia']['podloga-skladu']['px'])} px = "
          f"{pl(d['typografia']['podloga-skladu']['pt'])} pt --- */",
          "  --irin-r-kroj:      'Manrope', system-ui, -apple-system, 'Segoe UI', sans-serif;",
          "  --irin-r-kroj-mono: 'Inconsolata', 'SFMono-Regular', Consolas, monospace;",
          "", "  /* --- grubości linii; NIEPOTWIERDZONE NA WYDRUKU --- */",
          f"  --irin-r-linia-struktury: {mm(d['minimalna-grubosc-linii-mm']['struktura'])};",
          f"  --irin-r-linia-ozdobna:   {mm(d['minimalna-grubosc-linii-mm']['ozdoba'])};",
          "", "  /* --- limit akcentu: " + d["regula-proporcji"]["limit-akcentu"]["rachunek"] + " --- */",
          f"  --irin-r-limit-zlota-cm2: {d['regula-proporcji']['limit-akcentu']['limit-cm2']};",
          "}", ""]
    L += ["/* PARY ZABRONIONE, każda z liczbą i zamiennikiem:"]
    for w in d["kontrasty-zabronione"]:
        L.append(f" *   {d['barwy'][w['tekst']]['nazwa']} na "
                 f"{d['barwy'][w['tlo']]['nazwa']}: {pl(w['kontrast'])} -> {w['zamiast']}")
    L += [" */", ""]
    return "\n".join(L)


if __name__ == "__main__":
    dane = zloz()
    tekst = json.dumps(dane, ensure_ascii=False, indent=2) + "\n"
    css = zloz_css(dane)
    if "--dry-run" in sys.argv:
        print(tekst if "--css" not in sys.argv else css)
    else:
        for cel, tresc in ((CEL_JSON, tekst), (CEL_CSS, css)):
            cel.parent.mkdir(parents=True, exist_ok=True)
            cel.write_text(tresc, encoding="utf-8")
            print(f"zapisane: {cel.relative_to(ROOT)}  ({len(tresc)} znaków)")
```

- [x] **Krok 2: Złóż paletę i otwórz bramkę**

```bash
python3 _robocze/narzedzia/zloz-palete.py
python3 _robocze/narzedzia/sprawdz-palete.py; echo "kod wyjścia: $?"
```

Oczekiwane: `sprawdzonych twierdzeń: 226`, `rozjazdów: 0`,
`BRAMKA OTWARTA`, **kod wyjścia 0**.

Liczby, które muszą się w wyniku pojawić - jeżeli którejś nie ma, coś jest nie tak:
pole treści `426,70 cm2`, limit akcentu `21,34 cm2`, dryf rytmu `20,86 mm`
przy `45` liniach, podłoga składu `6,38 pt`, współczynniki pola znaku
`0,655` i `0,561`, tinty `#DCDAD5 · #E3D8D0 · #DBDCD2 · #DFDAD5`.

- [x] **Krok 3: Uruchom osiem prób podmiany z zadania 1**

```bash
python3 /tmp/proba-bramki.py 01-baza-wiedzy/identyfikacja/tokeny/palette-irin.json
```

Oczekiwane: osiem wierszy, każdy `kod 1  złapane`. Ani jednego `!!! DZIURA`.

- [x] **Krok 4: Sprawdź, że `tokens.css` rozwiązuje się w przeglądarce**

```bash
python3 - <<'PY'
import pathlib, re
css = pathlib.Path("_robocze/ds-bundle/tokens/tokens.css").read_text(encoding="utf-8")
zmienne = re.findall(r"^\s*(--irin-r-[a-z0-9-]+):", css, re.M)
print("tokenów:", len(zmienne))
for zly in ("--irin-r-success", "--irin-r-warning", "--irin-r-error"):
    assert zly not in zmienne, f"token stanu w arkuszu: {zly}"
assert "--irin-r-dziedzina" in zmienne and "--irin-r-tint-dziedzina" in zmienne
print("brak tokenów stanu: potwierdzone")
print("gniazdo obszaru: obecne")
PY
```

Oczekiwane: `tokenów: 49`, oba potwierdzenia.

**Uwaga do zapisania, nie do obejścia:** linia struktury `.25mm` renderuje się
na ekranie jako `1px` (0,25 mm = 0,94 px przy 96 dpi, przeglądarka zaokrągla
obramowanie w górę). Wartość drukarska jest w pliku poprawna; ekran jej nie
odwzorowuje i nie jest miejscem pomiaru grubości linii.

- [x] **Krok 5: Commit**

```bash
git add _robocze/narzedzia/zloz-palete.py \
        01-baza-wiedzy/identyfikacja/tokeny/palette-irin.json \
        _robocze/ds-bundle/tokens/tokens.css
git commit -m "Paleta Regalia w warstwie 1: JSON i tokeny składane z jednego źródła"
```

---

## Zadanie 3: Bramka spójności tekstu z danymi

Bramka z zadania 1 pilnuje spójności **wewnątrz** JSON-a. Ta pilnuje, żeby
proza specyfikacji i karty podglądu nie niosły liczb ani hexów, których w JSON-ie
nie ma. To bramka na R11 z `POMIAR.md`: karta `Paleta` po stronie projektowej
wypisuje czternaście hexów wprost i sześć z nich nie zgadza się z tokenem, który
ta sama karta rozwiązuje.

**Pliki:**
- Utwórz: `_robocze/narzedzia/sprawdz-zgodnosc-md.py`

**Interfejsy:**
- Konsumuje: `palette-irin.json` z zadania 2.
- Produkuje: `python3 _robocze/narzedzia/sprawdz-zgodnosc-md.py`, kod wyjścia
  0 albo 1. Sprawdza cztery specyfikacje warstwy 1, pięć plików `guidelines/`,
  osiem kart, `styles.css`, `format-paczki.md` i `prompt-bazowy.md`.

- [x] **Krok 1: Napisz bramkę spójności**

```python
#!/usr/bin/env python3
"""Bramka spójności: proza i karty nie mogą nieść wartości, których nie ma
w palette-irin.json.

Łapie dwie klasy błędów, obie zmierzone w POMIAR.md:
  - hex palety wycofanej, który przeżył podmianę (R3, R11);
  - liczbę kontrastu przepisaną zamiast policzonej (R9, R11).

Uruchomienie: python3 _robocze/narzedzia/sprawdz-zgodnosc-md.py
Kod wyjścia 0 = zgodne. 1 = rozjazd.
"""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
JSON = ROOT / "01-baza-wiedzy/identyfikacja/tokeny/palette-irin.json"

SPRAWDZANE = [
    "01-baza-wiedzy/identyfikacja/paleta-barw.md",
    "01-baza-wiedzy/identyfikacja/siatka-a4.md",
    "01-baza-wiedzy/identyfikacja/typografia.md",
    "01-baza-wiedzy/identyfikacja/logotyp.md",
    "01-baza-wiedzy/identyfikacja/README.md",
    "03-pakiet-claude-design/format-paczki.md",
    "03-pakiet-claude-design/prompt-bazowy.md",
    "_robocze/ds-bundle/README.md",
    "_robocze/ds-bundle/styles.css",
]
KATALOGI = ["_robocze/ds-bundle/guidelines", "_robocze/ds-bundle/components"]

# Hexy palet wycofanych. Żaden nie ma prawa stać w plikach wyżej.
WYCOFANE = {
    "#452430": "Aksamit v2", "#7A5638": "Miedź v2", "#33474F": "Onyks v2",
    "#2E5241": "Werdykt v2", "#8A6110": "Rubryka v2", "#2F5A63": "Patyna v2",
    "#FBF8F2": "Kaszmir v2", "#F6F2E9": "Muślin v2", "#E7DFD2": "Pergamin v2",
    "#221A15": "Espresso v2", "#5E4E40": "Sepia v2", "#A8874E": "Złoto foliowe v2",
    "#7D7466": "Popiół v2", "#9E2B2B": "Karmin v2", "#938978": "Popiół sprzed poprawki",
    "#752F3F": "Aksamit v5.1", "#9F6631": "Bursztyn v5.1", "#005A80": "Onyks v5.1",
    "#004D49": "Werdykt v5.1", "#803700": "Rubryka v5.1", "#007987": "Patyna v5.1",
    "#191647": "Ultramaryna v5.1", "#905E88": "Rubin v5.1", "#2D795C": "Szmaragd v5.1",
    "#3D3D00": "Oliwin v5.0", "#F2ECE1": "Kaszmir v1", "#1E1611": "Espresso v1",
}

def pliki():
    for s in SPRAWDZANE:
        p = ROOT / s
        if p.exists():
            yield p
    for k in KATALOGI:
        d = ROOT / k
        if d.exists():
            for p in sorted(d.rglob("*")):
                if p.is_file() and p.suffix in (".md", ".html", ".css"):
                    yield p

def main():
    d = json.loads(JSON.read_text(encoding="utf-8"))
    hexy = {v["hex"].upper() for v in d["barwy"].values()}
    hexy |= {t["hex"].upper() for t in d["tinty"].values()}
    hexy |= {"#FFFFFF", "#000000"}
    liczby = {f"{w['kontrast']:.2f}".replace(".", ",")
              for grupa in ("kontrasty-dopuszczone", "kontrasty-zabronione")
              for w in d[grupa]}
    liczby |= {f"{t['atrament-na-tincie']:.2f}".replace(".", ",") for t in d["tinty"].values()}
    liczby |= {f"{k:.2f}".replace(".", ",")
               for wiersz in d["macierz-na-tlach-nosnych"].values()
               for k in wiersz.values() if k is not None}

    bledy, sprawdzonych = [], 0
    for p in pliki():
        tresc = p.read_text(encoding="utf-8", errors="replace")
        rel = p.relative_to(ROOT)
        for nr, wiersz in enumerate(tresc.splitlines(), 1):
            for hx in re.findall(r"#[0-9A-Fa-f]{6}\b", wiersz):
                sprawdzonych += 1
                g = hx.upper()
                if g in WYCOFANE:
                    bledy.append(f"{rel}:{nr}  {hx} - {WYCOFANE[g]}, paleta wycofana")
                elif g not in hexy:
                    bledy.append(f"{rel}:{nr}  {hx} - nie ma tej wartości w palette-irin.json")
            for kontr in re.findall(r"\b(\d{1,2},\d{2})\s*:\s*1\b", wiersz):
                sprawdzonych += 1
                if kontr not in liczby:
                    bledy.append(f"{rel}:{nr}  kontrast {kontr}:1 - "
                                 f"nie ma tej liczby w palette-irin.json")

    print("BRAMKA SPÓJNOŚCI TEKSTU Z DANYMI")
    print(f"  sprawdzonych wartości: {sprawdzonych}")
    print(f"  rozjazdów: {len(bledy)}")
    for w in bledy:
        print(f"    ! {w}")
    if bledy:
        print("\nBRAMKA ZAMKNIĘTA. Proza niesie wartość, której nie ma w danych maszynowych.")
        return 1
    print("\nBRAMKA OTWARTA. Każdy hex i każdy kontrast w prozie ma pokrycie w danych.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
```

- [x] **Krok 2: Uruchom - musi ODMÓWIĆ**

```bash
python3 _robocze/narzedzia/sprawdz-zgodnosc-md.py; echo "kod wyjścia: $?"
```

Oczekiwane: **kod wyjścia 1** i kilkadziesiąt wierszy z hexami palety v2
w czterech specyfikacjach, w `guidelines/`, w ośmiu kartach i w `styles.css`.
To jest lista roboty na zadania 4-11. Zapisz ją:

```bash
python3 _robocze/narzedzia/sprawdz-zgodnosc-md.py > /tmp/roboty.txt 2>&1
awk '/^    !/{print $2}' /tmp/roboty.txt | cut -d: -f1 | sort | uniq -c | sort -rn
```

- [x] **Krok 3: Commit**

```bash
git add _robocze/narzedzia/sprawdz-zgodnosc-md.py
git commit -m "Bramka spójności: proza nie może nieść wartości spoza danych maszynowych"
```

---

## Zadanie 4: `paleta-barw.md` na Regalii

**Pliki:**
- Nadpisz: `01-baza-wiedzy/identyfikacja/paleta-barw.md`

**Interfejsy:**
- Konsumuje: `palette-irin.json` (klucze `barwy`, `tinty`, `kontrasty-*`,
  `pary-nieuzywane`, `gniazdo-obszaru`, `tokeny-stanu`, `regula-proporcji`,
  `minimalna-grubosc-linii-mm`).
- Produkuje: plik, na który odsyłają `format-paczki.md`, `CLAUDE.md`,
  `guidelines/paleta-barw.md` i `tokens.css`.

- [x] **Krok 1: Napisz plik**

Struktura, w tej kolejności. Każda liczba przepisana z JSON-a, **żadna
policzona ręcznie** - bramka z zadania 3 sprawdzi zgodność.

1. Nagłówek: `# Paleta barw IRIN - specyfikacja obowiązująca`, status
   `ZATWIERDZONA przez foundera 2026-09-03`, nazwa `Regalia`, odesłanie do
   `tokeny/palette-irin.json` jako danych maszynowych i do `siatka-a4.md`,
   `typografia.md`, `logotyp.md`.
2. Zdanie o tym, że plik jest **wywiedziony**: „Wartości w tym pliku pochodzą
   z `tokeny/palette-irin.json`. Ten plik nie jest miejscem, w którym się je
   zmienia - zmiana idzie przez `_robocze/narzedzia/zloz-palete.py` i bramkę
   `sprawdz-palete.py`."
3. `## Czternaście barw` - tabela: Nazwa · Token · Hex · Rola · na Kości
   Słoniowej · na Aksamicie Nocy · na Alabastrze. Wartości z
   `macierz-na-tlach-nosnych`.
4. `## Dwa układy, nie czternaście barw na stronie` - para bazowa Atrament na
   Kości Słoniowej `17,99:1` jako układ jasny, Kość Słoniowa na Aksamicie Nocy
   `17,25:1` jako odwrócenie. Zdanie: **maksymalnie dwa tła na dokument.**
5. `## Gniazdo obszaru` - treść z `gniazdo-obszaru`: token, domyślna barwa,
   zasada, cztery barwy dostępne, pułapka Rubinu. Wprost: **barwy nie są
   przypisane do obszarów, bo obszary są wymienne.**
6. `## Regalia nie ma tokenów stanu` - powód i skutek z `tokeny-stanu`. Wprost:
   stan niesie słowo plus barwa nośna dobrana w dokumencie; kolor nigdy nie jest
   jedynym nośnikiem statusu (WCAG 1.4.1).
7. `## Tinty 12 procent` - cztery tinty z `tinty`, z kontrastem Atramentu i
   zdaniem o roli: wyłącznie tła kart i pasy tabel, nigdy kolor tekstu ani linii.
8. `## Pary dopuszczone` - tabela z `kontrasty-dopuszczone`.
9. `## Pary zabronione` - tabela z `kontrasty-zabronione`, kolumna „zamiast
   tego" z pola `zamiast`. **Wiersz Lapisu na Aksamicie Nocy musi tu być** -
   to R12 z `POMIAR.md`: reguła istniała w prozie jednego szablonu i nie było
   jej w żadnej specyfikacji.
10. `## Pary, które nie wchodzą do składu` - lista z `pary-nieuzywane`
    z uzasadnieniem. Zdanie o tym, po co ta lista istnieje: żeby bramka mogła
    sprawdzić, że **żadna** para pod progiem nie została przeoczona.
11. `## Reguła proporcji 80/15/5` - z `regula-proporcji`, z rachunkiem limitu
    akcentu (`426,70 cm2`, `21,34 cm2`) i listą barw poza budżetem.
12. `## Minimalna grubość linii` - `0,25 mm` struktura, `0,5 mm` ozdoba,
    z jawnym `NIEPOTWIERDZONE NA WYDRUKU`.
13. `## Falsyfikatory otwarte` - lista z `falsyfikatory-otwarte`.

**Czego w tym pliku nie ma:** tabeli „co zmieniło się względem palety z…",
hexów v2 i v5.1, historii iteracji. To jest destylacja - historia palet została
w gicie i w `POMIAR.md`.

- [x] **Krok 2: Uruchom bramkę spójności**

```bash
python3 _robocze/narzedzia/sprawdz-zgodnosc-md.py 2>&1 | grep "paleta-barw" || echo "paleta-barw.md: czysto"
```

Oczekiwane: `paleta-barw.md: czysto`.

- [x] **Krok 3: Sprawdź, że nie ma myślników i że liczby mają przecinek**

```bash
python3 _robocze/narzedzia/sprawdz-dywizy.py 01-baza-wiedzy/identyfikacja/paleta-barw.md
grep -nE '[0-9]\.[0-9]{2}\s*:\s*1' 01-baza-wiedzy/identyfikacja/paleta-barw.md && echo "KROPKA - popraw" || echo "przecinki: OK"
```

- [x] **Krok 4: Commit**

```bash
git add 01-baza-wiedzy/identyfikacja/paleta-barw.md
git commit -m "Specyfikacja koloru na Regalii, z parą Lapisu w tabeli par zabronionych"
```

---

## Zadanie 5: `typografia.md` z jedenastym poziomem

**Pliki:**
- Nadpisz: `01-baza-wiedzy/identyfikacja/typografia.md`

**Interfejsy:**
- Konsumuje: `palette-irin.json`, klucz `typografia`.
- Produkuje: plik, na który odsyłają `format-paczki.md` i `guidelines/`.

- [x] **Krok 1: Napisz plik**

1. Nagłówek i to samo zdanie o wywiedzeniu z JSON-a co w zadaniu 4.
2. `## Kroje` - Manrope 200-800 podstawowy, Inconsolata 300-700 pomocniczy,
   licencja SIL OFL 1.1 z odesłaniem do `_robocze/ds-bundle/fonts/OFL.txt`.
3. `## Zasada systemu` - hierarchię buduje waga jednego kroju, nie zmiana
   rodziny. Trzeciego kroju nie ma.
4. `## Skala obowiązująca` - **jedenaście** poziomów z `typografia.skala`,
   kolumny: Poziom · Krój · Waga · Stopień px · Stopień pt · Interlinia ·
   Tracking · Rola. Jedenasty wiersz to `techniczny`: **8,5 px = 6,38 pt**,
   Inconsolata, rola „nagłówki tabel, przypisy, pas nadawcy".
5. `## Podłoga składu: 8,5 px = 6,38 pt` - osobna sekcja, bo to reguła, nie
   tylko wiersz tabeli. Treść: nic mniejszego nie wchodzi do składu; adnotacje
   rysunku w makietach w skali są wyjątkiem i **muszą być tak opisane w kodzie**.
   Rachunek wypisany: `8,5 × 72/96 = 6,375 pt`, w zapisie dwumiejscowym
   `6,38 pt`. Zdanie, które musi tam stać dosłownie: „Strona projektowa zapisuje
   `6,4 pt` - to ta sama liczba do jednego miejsca po przecinku. W repozytorium
   obowiązuje zapis dwumiejscowy."
6. `## Interlinia korpusu a jednostka odstępu 6 mm` - **dryf 20,86 mm na pełnej
   kolumnie 45 linii**, nie 19 mm. Pełny rachunek: interlinia `13,5 × 1,55
   = 20,93 px = 5,54 mm`, jednostka `6 mm = 22,68 px`, różnica `0,46 mm` na
   linię, `251 / 5,54 = 45,34`, więc 45 linii, `45 × 0,46 = 20,86 mm`.
   Zdanie o tym, co ta poprawka obala i czego nie: obala liczbę 19 mm
   (to dryf na 41 jednostkach siatki, nie na 45 liniach tekstu); **nie obala**
   rozstrzygnięcia, że jednostka 6 mm jest jednostką odstępu, a nie siatką
   linii bazowych - poprawiona liczba jest większa, więc wniosek stoi mocniej.
7. `## Alfabet polski - pokrycie zmierzone` - z `typografia.pokrycie-diakrytykow`:
   18/18 dla oba kroje, metoda (cmap rozpakowanych woff2, kontur sprawdzony,
   oba kroje zmienne, więc pokrycie nie może różnić się między wagami) oraz
   **co pozostaje niepotwierdzone**: czytelność ogonków na wydruku przy stopniu
   podłogi.

- [x] **Krok 2: Bramka spójności i kontrola dryfu**

```bash
python3 _robocze/narzedzia/sprawdz-zgodnosc-md.py 2>&1 | grep "typografia" || echo "typografia.md: czysto"
grep -c "20,86" 01-baza-wiedzy/identyfikacja/typografia.md
grep -n "19 mm" 01-baza-wiedzy/identyfikacja/typografia.md && echo "STARA LICZBA - popraw" || echo "dryf: OK"
grep -c "6,38 pt" 01-baza-wiedzy/identyfikacja/typografia.md
```

Oczekiwane: `czysto`, co najmniej jedno `20,86`, brak `19 mm`, co najmniej
jedno `6,38 pt`.

- [x] **Krok 3: Commit**

```bash
git add 01-baza-wiedzy/identyfikacja/typografia.md
git commit -m "Typografia: jedenasty poziom 8,5 px i poprawiony dryf 20,86 mm"
```

---

## Zadanie 6: `siatka-a4.md` po destylacji

**Pliki:**
- Nadpisz: `01-baza-wiedzy/identyfikacja/siatka-a4.md`

**Interfejsy:**
- Konsumuje: `palette-irin.json`, klucz `siatka-a4`.
- Produkuje: plik, na który odsyłają `format-paczki.md` i `guidelines/`.

- [x] **Krok 1: Napisz plik**

1. Nagłówek, status, zdanie o wywiedzeniu z JSON-a.
2. `## Parametry` - tabela z `siatka-a4`: format, kolumny, moduł, gutter,
   cztery marginesy, pole treści `170 × 251 mm` i `426,70 cm2`.
3. `## Rachunek, który musi się zgadzać co do milimetra` - z
   `rachunek-szerokosci`: `6 × 25 + 5 × 4 = 170 mm = 210 - 20 - 20`,
   dopasowanie dokładne. Zdanie: każda zmiana modułu albo gutteru pociąga
   zmianę marginesu i odwrotnie.
4. `## Dlaczego 25 i 4` - pięć rozwiązań całkowitych równania `6c + 5g = 170`
   (25/4, 20/10, 15/16, 10/22, 5/28) i powód wyboru pierwszego: gutter jest
   szóstą częścią modułu, więc kolumna czyta się jako kolumna. **To zostaje** -
   nie jest historią palety, tylko uzasadnieniem obowiązującej wartości.
5. `## Rytm pionowy` - dopuszczone odstępy między blokami 6, 12, 18, 24 i 48 mm;
   granica „wnętrze komponentu nie podlega jednostce"; reszta 5 mm zostaje
   światłem pod ostatnim blokiem i nigdy nie jest odstępem.
6. `## Dryf rytmu - 20,86 mm` - ta sama liczba i ten sam rachunek co w zadaniu 5,
   z odesłaniem do `typografia.md`, żeby nie było dwóch źródeł.
7. `## Dwie strefy marginesów` - z `siatka-a4.strefy`: górne 18 mm to strefa
   znaku i nagłówka, dolne 28 mm to strefa stopki, dolna krawędź tekstu stopki
   nie schodzi bliżej niż 12 mm od krawędzi strony.
8. `## Siatka slajdu 16:9 - PROPOZYCJA, nie specyfikacja` - jawnie oznaczona
   jako czekająca na decyzję właściciela. Rachunek: kanwa `1920 × 1080 px`,
   marginesy `96 px`, pole `1728 × 888 px`, `6 × 253 + 5 × 42 = 1728 px`,
   jednostka pionowa `24 px` (`888 = 37 × 24`), proporcja gutteru do modułu
   `42/253 = 16,6 %` wobec `4/25 = 16,0 %` na A4. Zdanie o tym, co ta propozycja
   obala: rozdz. 17 brandbooka podaje gutter `32 px` przy marginesie `96 px`,
   a `(1728 - 5 × 32) / 6 = 261,33 px` nie jest liczbą całkowitą. Wariant
   alternatywny przy utrzymaniu 32 px: marginesy `100 px`, pole `1720 px`,
   moduł `260 px`.

**Czego w tym pliku nie ma:** sekcji „Dlaczego moduł to 25 mm, a nie 32 mm
z kanwy", „Marginesy boczne wyrównane - poprawka 2026-09-03" i „Jednostka
bazowa 6 mm - rozstrzygnięte". To historia poprawek, nie specyfikacja.
Zostaje w gicie.

- [x] **Krok 2: Bramka i kontrola**

```bash
python3 _robocze/narzedzia/sprawdz-zgodnosc-md.py 2>&1 | grep "siatka-a4" || echo "siatka-a4.md: czysto"
grep -c "PROPOZYCJA" 01-baza-wiedzy/identyfikacja/siatka-a4.md
python3 -c "print('kontrola rachunku slajdu:', 6*253 + 5*42, '== 1728 ->', 6*253+5*42==1728)"
python3 -c "print('kontrola jednostki pionowej: 888 / 24 =', 888/24)"
```

- [x] **Krok 3: Commit**

```bash
git add 01-baza-wiedzy/identyfikacja/siatka-a4.md
git commit -m "Siatka A4 po destylacji; siatka slajdu jako jawna propozycja"
```

---

## Zadanie 7: `logotyp.md` z konwencją obwiedni znaku widocznego

To zadanie zamyka R12-sąsiada z `POMIAR.md` rozdz. 4.3: dziś specyfikacja mówi
„minimum 18 mm" i nie mówi, czy chodzi o szerokość pliku, czy o szerokość znaku.
Przy odczycie „pole pliku" znak poziomy wstawiony w 18 mm ma faktycznie
`11,79 mm`, czyli o 35 procent mniej, niż sugeruje liczba.

**Pliki:**
- Nadpisz: `01-baza-wiedzy/identyfikacja/logotyp.md`
- Utwórz: `_robocze/narzedzia/zmierz-znak.mjs`

**Interfejsy:**
- Konsumuje: `palette-irin.json`, klucz `logotyp`; trzy pliki SVG w korzeniu.
- Produkuje: plik specyfikacji plus skrypt odtwarzający obwiednie.

- [ ] **Krok 1: Napisz skrypt pomiaru obwiedni**

`_robocze/narzedzia/zmierz-znak.mjs`. Pomiar wymaga przeglądarki, więc **nie
wchodzi do bramki** - odtwarza wartości wpisane do generatora, na żądanie.

```javascript
// Pomiar obwiedni znaku widocznego w trzech plikach SVG.
// Odtwarza tablicę OBWIEDNIE z _robocze/narzedzia/zloz-palete.py.
// Uruchomienie: node _robocze/narzedzia/zmierz-znak.mjs
import pw from 'playwright';
const { chromium } = pw;
import fs from 'node:fs';
import path from 'node:path';

const ROOT = path.resolve(import.meta.dirname, '../..');
const PLIKI = ['logo_irin_poziom.svg', 'logo_irin_pion.svg', 'logo_irin_sygnet.svg'];

const b = await chromium.launch();
const p = await b.newPage();
for (const nazwa of PLIKI) {
  await p.setContent('<body style="margin:0">' +
    fs.readFileSync(path.join(ROOT, nazwa), 'utf8') + '</body>');
  const w = await p.evaluate(() => {
    const svg = document.querySelector('svg');
    const vb = svg.viewBox.baseVal;
    let x0 = Infinity, y0 = Infinity, x1 = -Infinity, y1 = -Infinity, n = 0;
    for (const el of svg.querySelectorAll('path,polygon,rect,circle,ellipse,polyline,line')) {
      const cs = getComputedStyle(el);
      if (cs.fill === 'none' && cs.stroke === 'none') continue;  // przezroczysty prostokąt tła
      const bb = el.getBBox();
      if (bb.width === 0 && bb.height === 0) continue;
      x0 = Math.min(x0, bb.x); y0 = Math.min(y0, bb.y);
      x1 = Math.max(x1, bb.x + bb.width); y1 = Math.max(y1, bb.y + bb.height); n++;
    }
    return { vbW: vb.width, vbH: vb.height, x0, y0, x1, y1, n };
  });
  const szer = w.x1 - w.x0, wys = w.y1 - w.y0;
  console.log(`${nazwa}:`);
  console.log(`  viewBox   ${w.vbW} x ${w.vbH}`);
  console.log(`  obwiednia [${w.x0.toFixed(3)}, ${w.y0.toFixed(3)}, ` +
              `${szer.toFixed(3)}, ${wys.toFixed(3)}]  (${w.n} kształtów)`);
  console.log(`  współczynnik pola ${(szer / w.vbW).toFixed(3)}`);
}
await b.close();
```

- [ ] **Krok 2: Uruchom pomiar i porównaj z generatorem**

```bash
NODE_PATH=/opt/node22/lib/node_modules node _robocze/narzedzia/zmierz-znak.mjs
```

Oczekiwane, co do trzeciego miejsca:

```
logo_irin_poziom.svg: obwiednia [48.561, 59.907, 184.213, 38.854]  współczynnik 0.655
logo_irin_pion.svg:   obwiednia [40.555, 37.593, 103.728, 87.312]  współczynnik 0.561
logo_irin_sygnet.svg: obwiednia [40.555, 61.991, 103.728, 38.853]  współczynnik 0.561
```

Jeżeli którakolwiek liczba się różni, **nie poprawiaj skryptu** - popraw tablicę
`OBWIEDNIE` w generatorze i złóż paletę na nowo. Pomiar jest źródłem, wpisana
wartość jest kopią.

- [ ] **Krok 3: Napisz `logotyp.md`**

1. Nagłówek, status, zdanie o wywiedzeniu z JSON-a.
2. `## Trzy pliki źródłowe` - tabela: plik · viewBox · obwiednia znaku
   widocznego · proporcja znaku · współczynnik pola · zastosowanie.
3. `## Konwencja pomiaru - obwiednia znaku widocznego` - sekcja pierwsza po
   tabeli, bo bez niej wszystkie liczby niżej są dwuznaczne. Treść z
   `logotyp.konwencja-pomiaru`, plus skutek liczbowy wypisany wprost:
   pole pliku `18 mm` daje znak widoczny `11,79 mm` (poziomy) i `10,10 mm`
   (pionowy, sygnet); żeby znak widoczny miał `18 mm`, pole pliku musi mieć
   `27,48 mm` (poziomy) albo `32,09 mm` (pionowy, sygnet) - wartości
   z `pole-pliku-dla-minimum-druku-mm`.
4. `## Minimalny rozmiar` - `18 mm` druk, `90 px` ekran, `10 mm` sygnet
   samodzielny, wszystko **w obwiedni znaku widocznego**. Wiersz sygnetu nadal
   oznaczony jako niepotwierdzony na wydruku.
5. `## Przestrzeń ochronna` - `x = wysokość liter sygnetu`, miara względna.
   Przeliczenie z obwiedni: dla sygnetu wysokość to `37,5 %` szerokości znaku,
   dla wersji poziomej `21,1 %`.
6. `## Cztery zakazy` - z `logotyp.zakazy`, wszystkie wiążące, plus akapit
   o tym, dlaczego zakaz koloru jest najważniejszy.
7. `## Barwa znaku w kodzie` - z `logotyp.barwa-znaku`: `color` kontenera plus
   `fill: currentColor`, **nigdy `filter:`**. Przykład:

   ```css
   .znak { color: var(--irin-r-atrament); }
   .znak svg path, .znak svg polygon, .znak svg rect:not([fill="none"]) { fill: currentColor; }
   ```

8. `## Dobór barwy znaku` - Atrament na Kości Słoniowej `17,99:1` jako
   domyślny; Kość Słoniowa na tle ciemnym jako wersja odwrócona
   (`17,25:1` na Aksamicie Nocy, `14,09:1` na Szafirze). Zdanie: **na
   fotografii żadna liczba z macierzy nie obowiązuje** - kontrast lokalny
   zdjęcia jest niepoliczalny, więc znak siada na plamie neutralnej.
9. `## Falsyfikator otwarty` - minimalny rozmiar samodzielnego sygnetu czeka
   na wydruk.

- [ ] **Krok 4: Bramka i kontrola**

```bash
python3 _robocze/narzedzia/sprawdz-zgodnosc-md.py; echo "kod wyjścia: $?"
```

Oczekiwane po zadaniach 4-7: **kod wyjścia 0** dla czterech specyfikacji
warstwy 1. Pliki `guidelines/`, karty i `styles.css` nadal będą zgłaszane -
to zadania 8, 9 i 10.

- [ ] **Krok 5: Commit**

```bash
git add 01-baza-wiedzy/identyfikacja/logotyp.md _robocze/narzedzia/zmierz-znak.mjs
git commit -m "Logotyp: konwencja obwiedni znaku widocznego, ze skryptem pomiaru"
```

---

## Zadanie 8: `styles.css`, reguły druku i licencja krojów

Trzy rzeczy w jednym zadaniu, bo dotyczą jednego pliku i jednego katalogu i mają
jeden cykl sprawdzenia. Reguły druku to luka zmierzona w `POMIAR.md` rozdz. 5:
w całym repozytorium jest **zero** wystąpień `@media print`, `@page`
i `print-color-adjust`, a system opisuje siebie jako służący dokumentom
drukowanym. Bez tego bloku przeglądarka wygasza tła przy `Ctrl+P`.

Brak pliku licencji jest drugą taką luką: oba kroje niosą w tablicy `name`
adres `http://scripts.sil.org/OFL`, ale SIL OFL wymaga, żeby **tekst** licencji
podróżował z fontem, a `find -iname 'license*' -o -iname 'OFL*'` zwraca pusto.

**Pliki:**
- Nadpisz: `_robocze/ds-bundle/styles.css`
- Utwórz: `_robocze/ds-bundle/fonts/OFL.txt`

**Interfejsy:**
- Konsumuje: `tokens.css` z zadania 2 (tokeny `--irin-r-*`).
- Produkuje: klasy `.irin-display`, `.irin-h1`, `.irin-h2`, `.irin-h3`,
  `.irin-lead`, `.irin-korpus`, `.irin-meta`, `.irin-kicker`, `.irin-liczba`,
  `.irin-dane`, **`.irin-techniczny`** (nowa, podłoga składu),
  `.irin-linia-struktury`, `.irin-kreska-ozdobna`, `.irin-odstep-1|2|4`,
  `.irin-siatka`, **`.irin-arkusz`** (nowa), **`.irin-odwrocony`** (nowa),
  `.karta` z potomkami. Osiem kart z zadania 9 używa dokładnie tych nazw.

- [ ] **Krok 1: Napisz `styles.css`**

```css
@import url('./fonts/fonts.css');
@import url('./tokens/tokens.css');

/* Warstwa bazowa systemu IRIN, paleta Regalia. Wszystko, co widzi projekt
   renderowany w Claude Design, przechodzi przez domknięcie @import tego pliku.

   Ten plik NIE jest generowany - klasy pisze się tu ręcznie. Generowany jest
   tokens.css; tu wolno używać wyłącznie zmiennych --irin-r-*, nigdy wartości
   wpisanej wprost. Bramka sprawdz-zgodnosc-md.py to pilnuje. */

body { background: var(--irin-r-surface); color: var(--irin-r-text);
       font-family: var(--irin-r-kroj); margin: 0; }

/* Skala typograficzna - jedenaście poziomów. Hierarchię buduje waga jednego
   kroju, nie zmiana rodziny. Podłoga składu: .irin-techniczny, 8,5 px = 6,38 pt. */
.irin-display    { font-weight: 200; font-size: 72px;   line-height: .92; letter-spacing: -.03em; }
.irin-h1         { font-weight: 300; font-size: 40px;   line-height: 1;   letter-spacing: -.02em; }
.irin-h2         { font-weight: 600; font-size: 24px;   line-height: 1.1; letter-spacing: -.01em; }
.irin-h3         { font-weight: 600; font-size: 16px;   line-height: 1.3; }
.irin-lead       { font-weight: 500; font-size: 16px;   line-height: 1.4; }
.irin-korpus     { font-weight: 400; font-size: 13.5px; line-height: 1.55; }
.irin-meta       { font-weight: 400; font-size: 10px;   line-height: 1.5; color: var(--irin-r-text-muted); }
.irin-kicker     { font-weight: 700; font-size: 14px;   line-height: 1.2; letter-spacing: .22em;
                   text-transform: uppercase; color: var(--irin-r-dziedzina); }
.irin-liczba     { font-weight: 800; font-size: 52px;   line-height: .95; letter-spacing: -.02em; }
.irin-dane       { font-family: var(--irin-r-kroj-mono); font-size: 10.5px; line-height: 1.5; }
.irin-techniczny { font-family: var(--irin-r-kroj-mono); font-size: 8.5px;  line-height: 1.4;
                   color: var(--irin-r-text-muted); }

/* Linie. Grubości NIEPOTWIERDZONE NA WYDRUKU - falsyfikator otwarty.
   Na ekranie .25mm zaokrągla się do 1px; ekran nie jest miejscem pomiaru. */
.irin-linia-struktury { border: 0; border-top: var(--irin-r-linia-struktury) solid var(--irin-r-border); }
.irin-kreska-ozdobna  { border: 0; height: var(--irin-r-linia-ozdobna); background: var(--irin-r-accent); }

/* Odstęp pionowy między blokami: wielokrotność jednostki 6 mm.
   Wnętrze komponentu tej jednostce nie podlega - patrz siatka-a4.md. */
.irin-odstep-1 { margin-block: var(--irin-r-jednostka); }
.irin-odstep-2 { margin-block: calc(var(--irin-r-jednostka) * 2); }
.irin-odstep-4 { margin-block: calc(var(--irin-r-jednostka) * 4); }

/* Sześć kolumn zawsze. Liczba kolumn jest elementem tożsamości, nie parametrem. */
.irin-siatka { display: grid; grid-template-columns: repeat(var(--irin-r-kolumny), minmax(0, 1fr));
               gap: var(--irin-r-gutter); }

/* Arkusz A4: pole treści i dwie strefy marginesów. */
.irin-arkusz { width: var(--irin-r-strona-szer); height: var(--irin-r-strona-wys);
               box-sizing: border-box; background: var(--irin-r-surface);
               padding: var(--irin-r-margines-gora) var(--irin-r-margines-bok)
                        var(--irin-r-margines-dol); position: relative; overflow: hidden; }

/* Układ odwrócony: para bazowa na ciemnym tle, nie nowe barwy. */
.irin-odwrocony { background: var(--irin-r-surface-dark); color: var(--irin-r-text-invert); }
.irin-odwrocony .irin-meta, .irin-odwrocony .irin-techniczny { color: var(--irin-r-surface-alt); }

/* Karta podglądu w panelu Design System. */
.karta { background: var(--irin-r-surface); color: var(--irin-r-text);
         font-family: var(--irin-r-kroj); padding: 28px 32px; box-sizing: border-box; }
.karta h2 { font-weight: 600; font-size: 24px; letter-spacing: -.01em; margin: 0 0 4px; }
.karta .podtytul { font-weight: 400; font-size: 13.5px; line-height: 1.55;
                   color: var(--irin-r-text-muted); margin: 0 0 20px; max-width: 62ch; }
.karta table { border-collapse: collapse; width: 100%; font-size: 12px; }
.karta th { text-align: left; font-weight: 600; font-size: 10px; text-transform: uppercase;
            letter-spacing: .08em; color: var(--irin-r-text-muted);
            border-bottom: var(--irin-r-linia-struktury) solid var(--irin-r-border);
            padding: 6px 10px 6px 0; }
.karta td { padding: 7px 10px 7px 0; vertical-align: middle;
            border-bottom: var(--irin-r-linia-struktury) solid var(--irin-r-border); }
.karta .uwaga { margin-top: 18px; padding: 12px 14px; background: var(--irin-r-surface-alt);
                font-size: 11.5px; line-height: 1.5; }
.karta code { font-family: var(--irin-r-kroj-mono); font-size: 11px; }

/* ================================================================
   DRUK. Bez tego bloku przeglądarka wygasza tła przy Ctrl+P i Pergamin
   calloutu oraz papier arkusza znikają. System opisuje siebie jako służący
   dokumentom drukowanym, więc to nie jest szczegół.
   ================================================================ */
@page { size: A4 portrait; margin: 0; }

@media print {
  html, body { background: var(--irin-r-surface); margin: 0; }
  * { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  .irin-arkusz { box-shadow: none; page-break-after: always; break-after: page; }
  .irin-arkusz:last-child { page-break-after: auto; break-after: auto; }
  .karta, .karta .uwaga { box-shadow: none; }
  a { text-decoration: underline; }              /* odnośnik bez barwy ekranu nadal widoczny */
  .irin-siatka, table, tr, td, th { break-inside: avoid; }
}
```

- [ ] **Krok 2: Sprawdź w przeglądarce, że druk zachowuje tła**

Zapisz `/tmp/sprawdz-druk.mjs`:

```javascript
import pw from 'playwright';
const { chromium } = pw;
import http from 'node:http'; import fs from 'node:fs'; import path from 'node:path';
const ROOT = process.argv[2];
const typy = {'.css':'text/css','.html':'text/html; charset=utf-8','.woff2':'font/woff2'};
const srv = http.createServer((q,s)=>{ const f=path.join(ROOT,decodeURIComponent(q.url.split('?')[0]));
  if(!fs.existsSync(f)){s.writeHead(404);return s.end();}
  s.writeHead(200,{'content-type':typy[path.extname(f)]||'text/plain'});
  fs.createReadStream(f).pipe(s); });
await new Promise(r=>srv.listen(8102,r));
fs.writeFileSync(path.join(ROOT,'_druk.html'),
`<!doctype html><html lang="pl"><head><meta charset="utf-8">
<link rel="stylesheet" href="styles.css"></head><body>
<div class="irin-arkusz"><p class="irin-korpus">Żółć, gęś, źdźbło: ĄĆĘŁŃÓŚŹŻ</p>
<div class="karta"><div class="uwaga">callout</div></div>
<hr class="irin-linia-struktury"><hr class="irin-kreska-ozdobna">
<p class="irin-techniczny">podłoga składu</p></div>
<div class="irin-arkusz irin-odwrocony"><p class="irin-korpus">układ odwrócony</p></div>
</body></html>`);
const b = await chromium.launch(); const p = await b.newPage(); const bledy = [];
p.on('console', m => { if (m.type()==='error') bledy.push(m.text()); });
p.on('response', r => { if (r.status()>=400) bledy.push('HTTP '+r.status()+' '+r.url()); });
await p.goto('http://127.0.0.1:8102/_druk.html', {waitUntil:'networkidle'});
const zmierz = async (media) => { await p.emulateMedia({media});
  return p.evaluate(() => { const cs = e => getComputedStyle(e);
    const a=document.querySelector('.irin-arkusz'), u=document.querySelector('.uwaga'),
          o=document.querySelector('.irin-odwrocony'), t=document.querySelector('.irin-techniczny');
    return { arkuszTlo: cs(a).backgroundColor, arkusz: cs(a).width+' x '+cs(a).height,
      paddingGora: cs(a).paddingTop, calloutTlo: cs(u).backgroundColor,
      odwroconyTlo: cs(o).backgroundColor, odwroconyTekst: cs(o).color,
      technicznyPx: cs(t).fontSize,
      adjust: cs(a).printColorAdjust || cs(a).webkitPrintColorAdjust }; }); };
console.log('EKRAN:', JSON.stringify(await zmierz('screen')));
console.log('DRUK :', JSON.stringify(await zmierz('print')));
console.log('błędy:', bledy.length ? bledy : 'brak');
fs.unlinkSync(path.join(ROOT,'_druk.html'));
await b.close(); srv.close();
```

```bash
NODE_PATH=/opt/node22/lib/node_modules node /tmp/sprawdz-druk.mjs _robocze/ds-bundle
```

Oczekiwane - te wartości muszą wyjść dokładnie tak:

| Pomiar | Ekran | Druk |
|---|---|---|
| `adjust` | `economy` | **`exact`** |
| `arkuszTlo` | `rgb(247, 243, 233)` | `rgb(247, 243, 233)` |
| `calloutTlo` | `rgb(228, 225, 216)` | `rgb(228, 225, 216)` |
| `odwroconyTlo` | `rgb(8, 15, 31)` | `rgb(8, 15, 31)` |
| `arkusz` | `793.688px x 1122.52px` | to samo |
| `paddingGora` | `68.0315px` | to samo |
| `technicznyPx` | `8.5px` | to samo |
| `błędy` | `brak` | `brak` |

`793,688 px` to `210 mm` przy 96 dpi, `1122,52 px` to `297 mm`, `68,0315 px`
to `18 mm`. Jeżeli `adjust` w druku pokazuje `economy`, blok `@media print`
nie zadziałał i **tła znikną na wydruku** - to jest ta luka, którą to zadanie
zamyka.

- [ ] **Krok 3: Dołóż tekst licencji krojów**

```bash
python3 - <<'PY'
import re, base64, io, pathlib
css = pathlib.Path("_robocze/ds-bundle/fonts/fonts.css").read_text(encoding="utf-8")
print("Kroje osadzone w fonts.css i ich metryka licencji:")
for blok in re.findall(r"@font-face\s*\{(.*?)\}", css, re.S):
    fam = re.search(r"font-family:\s*'([^']+)'", blok).group(1)
    print(f"  {fam}: licencja z tablicy name -> http://scripts.sil.org/OFL")
PY
```

Zapisz do `_robocze/ds-bundle/fonts/OFL.txt` pełny tekst **SIL Open Font
License, Version 1.1** wraz z nagłówkiem wymienionym w niej `Copyright`
dla obu krojów:

```
Copyright 2019 The Manrope Project Authors (https://github.com/sharanda/manrope)
Copyright 2006 The Inconsolata Project Authors (https://github.com/cyrealtype/Inconsolata)

This Font Software is licensed under the SIL Open Font License, Version 1.1.
[dalej pełny tekst licencji OFL 1.1 - pobrany z https://openfontlicense.org
 albo z repozytoriów obu krojów; nie streszczaj go i nie tłumacz]
```

To jedyny plik w repozytorium po angielsku - tekst licencji jest identyfikatorem
prawnym i tłumaczenie go byłoby zmianą treści, nie przekładem.

Dopisz na końcu `_robocze/ds-bundle/README.md` sekcję `## Licencja krojów`
z jednym zdaniem: kroje są objęte SIL OFL 1.1, tekst licencji leży w
`fonts/OFL.txt` i podróżuje z paczką.

- [ ] **Krok 4: Bramka**

```bash
python3 _robocze/narzedzia/sprawdz-zgodnosc-md.py 2>&1 | grep "styles.css" || echo "styles.css: czysto"
ls -l _robocze/ds-bundle/fonts/OFL.txt
grep -c "print-color-adjust" _robocze/ds-bundle/styles.css
```

Oczekiwane: `styles.css: czysto`, plik OFL istnieje, `print-color-adjust`
występuje co najmniej raz.

- [ ] **Krok 5: Commit**

```bash
git add _robocze/ds-bundle/styles.css _robocze/ds-bundle/fonts/OFL.txt _robocze/ds-bundle/README.md
git commit -m "Arkusz na Regalii, reguły druku i tekst licencji OFL przy fontach"
```

---

## Zadanie 9: Osiem kart podglądu

Karty są dziś jedynym miejscem w paczce, które wpisuje wartości wprost obok
tokenów - i dokładnie tam po stronie projektowej powstał rozjazd R11: karta
`Paleta` wypisuje czternaście hexów, a sześć z nich nie zgadza się z tokenem,
który ta sama karta rozwiązuje. Rozwiązanie jest strukturalne: **karta nie
wpisuje żadnej wartości wprost.** Próbki barw też idą przez `var()`.

**Pliki:**
- Nadpisz: `_robocze/ds-bundle/components/fundamenty/Paleta/Paleta.html`
- Nadpisz: `_robocze/ds-bundle/components/fundamenty/Typografia/Typografia.html`
- Nadpisz: `_robocze/ds-bundle/components/fundamenty/SiatkaA4/SiatkaA4.html`
- Nadpisz: `_robocze/ds-bundle/components/fundamenty/Logotyp/Logotyp.html`
- Nadpisz: `_robocze/ds-bundle/components/prymitywy/HierarchiaTekstu/HierarchiaTekstu.html`
- Nadpisz: `_robocze/ds-bundle/components/prymitywy/BlokDanychRejestrowych/BlokDanychRejestrowych.html`
- Nadpisz: `_robocze/ds-bundle/components/prymitywy/StopkaFirmowa/StopkaFirmowa.html`
- Zmień nazwę i przepisz: `components/prymitywy/PlakietkaStatusu/` →
  `components/prymitywy/PlakietkaStanu/PlakietkaStanu.html`

**Interfejsy:**
- Konsumuje: klasy z zadania 8, tokeny z zadania 2.
- Produkuje: osiem kart z adnotacją pierwszego wiersza
  `<!-- @dsCard group="Fundamenty" -->` albo `group="Prymitywy"`. Z tej
  adnotacji panel Design System buduje indeks - zadanie 15 na tym stoi.

- [ ] **Krok 1: Przepisz siedem kart**

Wspólne reguły dla każdej z nich:
- `<link rel="stylesheet" href="../../../styles.css">` - ścieżka bez zmian.
- **Zero literalnych hexów.** Próbka barwy to
  `<span style="background:var(--irin-r-szafir-nocny)">`, nie `background:#132246`.
- Zero liczb kontrastu wpisanych w treść, o ile nie stoją w
  `palette-irin.json` - bramka z zadania 3 to sprawdza.
- Karta `Paleta`: czternaście wierszy, kolumny Nazwa · Token · Rola ·
  na Kości Słoniowej · na Aksamicie Nocy · na Alabastrze. Pod tabelą dwa
  calloutuy: tabela par zabronionych z zamiennikami i akapit o braku tokenów stanu.
- Karta `Typografia`: **jedenaście** wierszy, ostatni to `.irin-techniczny`
  z podpisem `8,5 px = 6,38 pt - podłoga składu`.
- Karta `SiatkaA4`: rysunek w skali plus tabela parametrów plus callout
  z rachunkiem `6 × 25 + 5 × 4 = 170 mm`. Rysunek buduj na
  `var(--irin-r-*)`, nie na `rgba()` z wpisanymi składowymi.
- Karta `Logotyp`: trzy warianty, tabela obwiedni i współczynników pola,
  callout o konwencji obwiedni znaku widocznego i cztery zakazy. Barwa znaku
  przez `color` kontenera i `fill: currentColor` - **w karcie też, nie tylko
  w specyfikacji.**
- Karta `HierarchiaTekstu`: kicker, lead, H3, korpus, dane, techniczny
  w jednym bloku, z odstępami `.irin-odstep-*`.
- Karta `BlokDanychRejestrowych`: dane rejestrowe wprost (są potwierdzone),
  dane kontaktowe jako placeholdery. Callout o art. 206 KSH.
- Karta `StopkaFirmowa`: linia `.irin-linia-struktury` plus jeden pas
  metadanych na `.irin-siatka`, callout o strefie stopki 28 mm i granicy 12 mm.

- [ ] **Krok 2: Przepisz kartę stanu - to nie jest zmiana kosmetyczna**

Stara karta nazywa się `PlakietkaStatusu` i pokazuje cztery plakietki
**na wypełnieniu barwnym**, po jednej na token stanu. Regalia nie ma tokenów
stanu, więc taka karta nie ma czym rysować czterech wypełnień.

Nowa karta `PlakietkaStanu` pokazuje **jedno wykonanie i cztery słowa**:
etykieta Atramentem, obrys Grafit Jedwabny `0,25 mm`, tło Kość Słoniowa albo
tint obszaru. Cztery stany: `POTWIERDZONE`, `WYMAGA UWAGI`, `BŁĄD I KOREKTA`,
`INFORMACJA`. Callout musi zawierać zdanie: „Stan niesie słowo, nie barwa.
Regalia nie ma tokenów stanu - i to jest decyzja, nie przeoczenie."

```bash
git mv _robocze/ds-bundle/components/prymitywy/PlakietkaStatusu \
       _robocze/ds-bundle/components/prymitywy/PlakietkaStanu
git mv _robocze/ds-bundle/components/prymitywy/PlakietkaStanu/PlakietkaStatusu.html \
       _robocze/ds-bundle/components/prymitywy/PlakietkaStanu/PlakietkaStanu.html
```

- [ ] **Krok 3: Sprawdź, że żadna karta nie wpisuje wartości wprost**

```bash
grep -rn -E '#[0-9A-Fa-f]{6}' _robocze/ds-bundle/components/ && echo "LITERALNY HEX - popraw" || echo "karty: zero literalnych hexów"
python3 _robocze/narzedzia/sprawdz-zgodnosc-md.py; echo "kod wyjścia: $?"
```

Oczekiwane: `karty: zero literalnych hexów` i **kod wyjścia 0** dla całej
bramki spójności, o ile zadanie 10 (`guidelines/`) też jest już zrobione;
jeżeli nie - zgłaszane mają być wyłącznie pliki z `guidelines/`.

- [ ] **Krok 4: Otwórz osiem kart w przeglądarce**

```bash
NODE_PATH=/opt/node22/lib/node_modules node - <<'JS'
import pw from 'playwright'; const { chromium } = pw;
import http from 'node:http'; import fs from 'node:fs'; import path from 'node:path';
const ROOT='_robocze/ds-bundle';
const typy={'.css':'text/css','.html':'text/html; charset=utf-8','.svg':'image/svg+xml'};
const srv=http.createServer((q,s)=>{const f=path.join(ROOT,decodeURIComponent(q.url.split('?')[0]));
 if(!fs.existsSync(f)||fs.statSync(f).isDirectory()){s.writeHead(404);return s.end();}
 s.writeHead(200,{'content-type':typy[path.extname(f)]||'text/plain'});
 fs.createReadStream(f).pipe(s);});
await new Promise(r=>srv.listen(8103,r));
const karty=[]; (function chodz(d){ for(const e of fs.readdirSync(path.join(ROOT,d),{withFileTypes:true})){
  const s=path.posix.join(d,e.name); if(e.isDirectory())chodz(s); else if(e.name.endsWith('.html'))karty.push(s);}})('components');
const b=await chromium.launch(); const p=await b.newPage(); let zle=0;
for(const k of karty.sort()){ const bledy=[];
  const onC=m=>{if(m.type()==='error')bledy.push(m.text())}, onR=r=>{if(r.status()>=400)bledy.push('HTTP '+r.status())};
  p.on('console',onC); p.on('response',onR);
  await p.goto('http://127.0.0.1:8103/'+k,{waitUntil:'networkidle'});
  const w=await p.evaluate(async()=>{ await document.fonts.ready;
    const cs=getComputedStyle(document.documentElement);
    return {surface:cs.getPropertyValue('--irin-r-surface').trim(),
      dziedzina:cs.getPropertyValue('--irin-r-dziedzina').trim(),
      stan:['--irin-r-success','--irin-r-warning','--irin-r-error']
        .map(n=>cs.getPropertyValue(n).trim()).filter(Boolean).length,
      karta:getComputedStyle(document.querySelector('.karta')||document.body).backgroundColor};});
  p.off('console',onC); p.off('response',onR);
  const ok = w.surface==='#F7F3E9' && w.dziedzina==='#132246' && w.stan===0 && bledy.length===0;
  if(!ok) zle++;
  console.log(`${ok?'OK  ':'ZŁE '} ${k.split('/').pop().padEnd(28)} surface=${w.surface} dziedzina=${w.dziedzina} tokenów-stanu=${w.stan} błędy=${bledy.length}`);
}
console.log(`\nkart: ${karty.length}, złych: ${zle}`);
await b.close(); srv.close(); process.exit(zle?1:0);
JS
```

Oczekiwane: osiem wierszy `OK`, `kart: 8, złych: 0`.

- [ ] **Krok 5: Commit**

```bash
git add -A _robocze/ds-bundle/components/
git commit -m "Osiem kart podglądu na Regalii; plakietka stanu bez barwy stanu"
```

---

## Zadanie 10: `guidelines/` i naprawa siedemnastu odnośników

`guidelines/` to kopie specyfikacji warstwy 1, przenoszone do paczki. Dziś
niosą **siedemnaście martwych odnośników** (R4 z `POMIAR.md`): pliki są bajt
w bajt kopiami warstwy 1, przeniesionymi na inną głębokość, więc ścieżki
względne się urwały. Dla czytelnika po stronie projektowej te ścieżki prowadzą
donikąd.

**Pliki:**
- Nadpisz: `_robocze/ds-bundle/guidelines/{paleta-barw,siatka-a4,typografia,logotyp}.md`
- Nadpisz: `_robocze/ds-bundle/guidelines/zasady-uzycia.md`
- Utwórz: `_robocze/narzedzia/zloz-paczke.py`

**Interfejsy:**
- Konsumuje: cztery specyfikacje z zadań 4-7.
- Produkuje: `python3 _robocze/narzedzia/zloz-paczke.py` - kopiuje cztery
  specyfikacje do `guidelines/` i **przepisuje w nich odnośniki względne** na
  ścieżki obowiązujące wewnątrz paczki. Kopiowanie ręczne odpada: właśnie ono
  wygenerowało siedemnaście martwych odnośników.

- [ ] **Krok 1: Napisz składacz paczki**

```python
#!/usr/bin/env python3
"""Kopiuje specyfikacje warstwy 1 do guidelines/ paczki i naprawia odnośniki.

Powód istnienia: kopiowanie ręczne dało 17 martwych odnośników (POMIAR.md, R4).
Pliki w warstwie 1 odsyłają do siebie ścieżkami względnymi, a w paczce leżą
na innej głębokości i bez katalogu 01-baza-wiedzy nad sobą.

Uruchomienie: python3 _robocze/narzedzia/zloz-paczke.py
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
ZRODLO = ROOT / "01-baza-wiedzy/identyfikacja"
PACZKA = ROOT / "_robocze/ds-bundle/guidelines"
SPECYFIKACJE = ["paleta-barw.md", "siatka-a4.md", "typografia.md", "logotyp.md"]

# Ścieżka w warstwie 1 -> ścieżka wewnątrz paczki. Cel, którego w paczce nie ma,
# zamienia się na nazwę w nawiasie ostrym, żeby odnośnik nie prowadził donikąd.
MAPA = {
    "./tokeny/palette-irin.json": "../tokens/palette-irin.json",
    "tokeny/palette-irin.json": "../tokens/palette-irin.json",
    "./paleta-barw.md": "./paleta-barw.md",
    "./siatka-a4.md": "./siatka-a4.md",
    "./typografia.md": "./typografia.md",
    "./logotyp.md": "./logotyp.md",
}
POZA_PACZKA = re.compile(r"\.\./\.\./|\.\./01-baza-wiedzy|/01-baza-wiedzy")

def napraw(tekst, nazwa):
    zmian, poza = 0, []
    def zamien(m):
        nonlocal zmian
        etykieta, cel = m.group(1), m.group(2)
        if cel.startswith(("http://", "https://", "mailto:", "#")):
            return m.group(0)
        if cel in MAPA:
            zmian += 1
            return f"[{etykieta}]({MAPA[cel]})"
        if POZA_PACZKA.search(cel):
            poza.append(cel)
            zmian += 1
            return f"{etykieta} (poza paczką: `{cel}`)"
        return m.group(0)
    wynik = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", zamien, tekst)
    return wynik, zmian, poza

def main():
    PACZKA.mkdir(parents=True, exist_ok=True)
    razem = 0
    for nazwa in SPECYFIKACJE:
        zr = ZRODLO / nazwa
        if not zr.exists():
            print(f"BŁĄD: brak {zr.relative_to(ROOT)}")
            return 1
        tekst, zmian, poza = napraw(zr.read_text(encoding="utf-8"), nazwa)
        naglowek = (f"<!-- Kopia {zr.relative_to(ROOT)} złożona przez "
                    f"_robocze/narzedzia/zloz-paczke.py. Nie edytuj tu - "
                    f"zmiana idzie w warstwie 1. -->\n")
        (PACZKA / nazwa).write_text(naglowek + tekst, encoding="utf-8")
        print(f"  {nazwa}: odnośników przepisanych {zmian}" +
              (f", poza paczką {len(poza)}" if poza else ""))
        razem += zmian
    print(f"złożone: {len(SPECYFIKACJE)} plików, {razem} odnośników przepisanych")
    return 0

if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Krok 2: Złóż paczkę i sprawdź, że nie ma martwych odnośników**

```bash
python3 _robocze/narzedzia/zloz-paczke.py
python3 - <<'PY'
import os, re, pathlib
ROOT = pathlib.Path(".")
wzor = re.compile(r"\]\(([^)\s#]+)(?:\s+\"[^\"]*\")?\)")
martwe = ile = 0
for p in sorted(ROOT.rglob("*.md")):
    if ".git" in p.parts: continue
    for nr, w in enumerate(p.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
        for m in wzor.finditer(w):
            t = m.group(1)
            if t.startswith(("http://","https://","mailto:","#")): continue
            ile += 1
            if not (p.parent / t).resolve().exists():
                martwe += 1
                print(f"  ! {p}:{nr} -> {t}")
print(f"odnośników względnych: {ile}, martwych: {martwe}")
PY
```

Oczekiwane: `martwych: 0`. Przed tym zadaniem było ich siedemnaście.

- [ ] **Krok 3: Napisz `zasady-uzycia.md`**

Osiem reguł, bez których same wartości są niekompletne. Ten plik **nie jest
kopią** - powstaje ręcznie i jest jedynym plikiem w `guidelines/` bez nagłówka
o złożeniu. Treść to osiem punktów z sekcji `Ograniczenia globalne` tego planu,
każdy z liczbą albo z odesłaniem do specyfikacji. Reguła ósma (zakaz znaków
Funduszy Europejskich) z podstawą: Podręcznik informacji i promocji FE,
rozdz. 8.7, s. 22, i odesłaniem do `01-baza-wiedzy/prawo/pozyczki-ue-bgk.md`.

- [ ] **Krok 4: Bramka**

```bash
python3 _robocze/narzedzia/sprawdz-palete.py && python3 _robocze/narzedzia/sprawdz-zgodnosc-md.py
echo "obie bramki, kod wyjścia: $?"
```

Oczekiwane: **kod wyjścia 0**. To pierwszy moment w tym planie, w którym cała
paczka i cała warstwa 1 przechodzą oba sprawdzenia.

- [ ] **Krok 5: Commit**

```bash
git add _robocze/narzedzia/zloz-paczke.py _robocze/ds-bundle/guidelines/
git commit -m "Guidelines składane skryptem; siedemnaście martwych odnośników zamknięte"
```

---

## Zadanie 11: Pliki towarzyszące i sprzątanie

**Pliki:**
- Modyfikuj: `CLAUDE.md` - sekcje o palecie
- Modyfikuj: `03-pakiet-claude-design/format-paczki.md`
- Modyfikuj: `03-pakiet-claude-design/prompt-bazowy.md`
- Modyfikuj: `01-baza-wiedzy/identyfikacja/README.md`
- Modyfikuj: `README.md`
- Modyfikuj: `.gitignore`
- Modyfikuj: `_robocze/brandbook-warianty/wariant-{1,2,3}-*.dc.html`
- Usuń: `_robocze/skasowane-galezie-2026-09-03.md`

- [ ] **Krok 1: `CLAUDE.md`**

Zamień sekcje `## Paleta barw - stan obowiązujący` i akapit o `brandbook.dc.html`:
- Obowiązująca paleta to **Regalia, 14 wartości, prefiks `--irin-r-`**,
  zatwierdzona 2026-09-03, wpisana do warstwy 1 2026-09-09.
- Jedyne źródło maszynowe: `01-baza-wiedzy/identyfikacja/tokeny/palette-irin.json`,
  **generowane** przez `_robocze/narzedzia/zloz-palete.py`.
- Zdanie, które musi tam stać: „Wartości palety nie zmienia się w żadnym pliku
  `.md` ani `.css` - zmiana idzie przez generator i przez bramkę
  `sprawdz-palete.py`. Plik, którego bramka nie przepuszcza, nie jest gotowy."
- Z opisu `brandbook.dc.html` **usuń listę jedenastu hexów palety kanwy**.
  Zostaw zdanie, że kanwa jest punktem wyjścia i że jej palety nie stosuje się.
- Dopisz do sekcji o zasadach: reguły druku i licencja krojów są częścią paczki.

- [ ] **Krok 2: `format-paczki.md` i `prompt-bazowy.md`**

Osiem zasad przepisz na Regalię. Zmiany merytoryczne, nie kosmetyczne:
- zasada o jednym kolorze dziedziny → **gniazdo `--irin-r-dziedzina`**, barwy
  nie są przypisane do obszarów;
- zasada o etykiecie na wypełnieniu → tabela par dopuszczonych z
  `paleta-barw.md`;
- zasada o kolorze jako nośniku statusu → **Regalia nie ma tokenów stanu**;
- zasada o linii → Grafit Jedwabny od `0,25 mm`, Złoto Szampańskie od `0,5 mm`
  i **nigdy jako tekst na jasnym** (`1,80:1`);
- dopisz zasadę o barwie znaku: `color` plus `fill: currentColor`, nigdy `filter:`;
- dopisz zasadę o podłodze składu `8,5 px = 6,38 pt`.

- [ ] **Krok 3: Usuń wycofany Popiół z trzech wariantów księgi marki**

To R3 z `POMIAR.md`: wariant 1 jest **wybrany przez foundera**, a niesie
`#938978` - wartość sprzed poprawki, dającą `2,61:1` na tle calloutu przy
progu `3:1`. Pliki są o 45 minut starsze od poprawki koloru.

```bash
grep -c "938978" _robocze/brandbook-warianty/wariant-*.dc.html
```

Oczekiwane przed: po `2` w każdym z trzech plików.

Te trzy pliki są na palecie v2 w całości, nie tylko w Popiele. Skoro warstwa 1
przechodzi na Regalię, warianty księgi marki są materiałem do złożenia od nowa
po stronie projektowej - nie do łatania tu. **Oznacz je, nie poprawiaj:**
dopisz na początku każdego z trzech plików komentarz HTML:

```html
<!-- ARCHIWUM. Ten wariant powstał na palecie v2 „Kaszmir Wyciszony" (2026-09-03)
     i nie jest zgodny z obowiązującą paletą Regalia. Niesie m.in. Popiół #938978,
     wartość sprzed poprawki kontrastu (2,61:1 na tle calloutu przy progu 3:1).
     Wybór wariantu 1 przez foundera dotyczył UKŁADU, nie barw - układ zostaje,
     barwy składa się od nowa na Regalii po stronie projektu Claude Design.
     Podstawa: POMIAR.md, R3. -->
```

Dopisz to samo rozstrzygnięcie jednym zdaniem do
`_robocze/brandbook-warianty/notatka-warianty.md`.

- [ ] **Krok 4: `.gitignore` i plik martwy**

```bash
cat > .gitignore <<'GITIGNORE'
# macOS
.DS_Store

# Konfiguracja narzędzi, nie kod projektu
.mcp.json

# Katalog roboczy AgentsRoom - stan aplikacji, nie kod projektu
.agentsroom/
GITIGNORE
git rm _robocze/skasowane-galezie-2026-09-03.md
```

Powód: dwadzieścia sześć z trzydziestu dwóch wierszy starego `.gitignore` to
szablon dla projektów AL / Dynamics 365 Business Central (`.alcache/`,
`*.bclicense`, `rad.json`) - do tego repozytorium nie ma nic.
`skasowane-galezie-2026-09-03.md` to zapis jednorazowej operacji, do którego
nic się nie odwołuje.

- [ ] **Krok 5: Oznacz pilota papieru firmowego jako archiwum**

`_robocze/pilot-papier-firmowy/` niesie trzy zmierzone rozjazdy i wszystkie
trzy są skutkiem tego, że pilot powstał na palecie v2:

| # | Rozjazd | Gdzie |
|---|---|---|
| R2 | etykieta „marginesy 18 / 22 / 28 / 18 mm" obok kodu ustawiającego `18mm 20mm 28mm 20mm` | `Main.dc.html:29` wobec `Main.dc.html:17` |
| R5 | zero `var(--irin-*)`, fonty z `fonts.googleapis.com`, brak `styles.css` - zmiana palety nie przejdzie na nośnik | cztery artboardy |
| R6 | `<script src="./support.js">` w czterech plikach, pliku nie ma w repozytorium | cztery artboardy |

Pilot jest **unieważniony w części barwnej** (rejestr decyzji na końcu tego
planu), a jego wzory nośników zostały po stronie projektowej złożone od nowa
na Regalii - `templates/papier-firmowy` i `templates/wizytowka`, oba zmierzone
w `POMIAR.md` rozdz. 9.2. Łatanie pilota tutaj byłoby pracą nad materiałem,
który już ma następcę.

Dopisz na początku `_robocze/pilot-papier-firmowy/README.md`:

```markdown
> **ARCHIWUM.** Pilot powstał na palecie v2 „Kaszmir Wyciszony" i nie jest
> zgodny z obowiązującą paletą Regalia. Trzy znane rozjazdy: etykieta siatki
> podaje marginesy 18 / 22 zamiast 20 / 20 (Main.dc.html:29 wobec :17),
> artboardy nie czytają tokenów ani arkusza paczki, `support.js` nie istnieje
> w repozytorium. Następcy tych wzorów stoją po stronie projektu Claude Design:
> `templates/papier-firmowy` i `templates/wizytowka`, oba na Regalii.
> Sześć pomiarów z `protokol-pomiaru.md`: cztery wykonane po stronie projektowej
> i wpisane do warstwy 1 razem z Regalią, dwa otwarte i wymagające papieru
> (grubości linii, minimum sygnetu). Podstawa: POMIAR.md, R2, R5, R6.
```

To samo zdanie jednym akapitem na początku `protokol-pomiaru.md`.

- [ ] **Krok 6: Zapis w czterech plikach perymetru, których plan nie przepisuje**

Zadania 4-10 przepisują większość plików perymetru i myślniki znikają tam same.
Zostają cztery, których plan nie dotyka merytorycznie, a które w perymetrze są:

| Plik | Myślników | Co zrobić |
|---|---|---|
| `03-pakiet-claude-design/README.md` | 2 | zamień na dywiz |
| `.github/workflows/claude-recenzja-pr.yml` | 2 | zamień na dywiz |
| `.github/workflows/claude-triaz-issue.yml` | 2 | zamień na dywiz |
| `.github/workflows/claude-zadanie.yml` | 2 | zamień na dywiz |

Osobno dwa pliki z epoki palety v2, w sumie **87** myślników, które nie są
zapisem do poprawienia, tylko materiałem do rozstrzygnięcia:

| Plik | Myślników | Co to jest |
|---|---|---|
| `03-pakiet-claude-design/propozycja-palety-i-siatki-do-potwierdzenia.md` | 57 | historia pierwszej decyzji o palecie, zastąpionej dwa razy |
| `03-pakiet-claude-design/zlecenia/pilot-papier-firmowy*.md` | 30 | zlecenie pilota złożone na palecie v2 |

**Oba oznacz, nie poprawiaj.** Sama decyzja jest już w rejestrze na końcu
`PLAN.md`, a pilot jest unieważniony w części barwnej (zadanie 22 z poprzedniej
kolejki). Dopisz na początku każdego z nich:

```markdown
> **ARCHIWUM.** Ten plik opisuje stan z epoki palety v2 „Kaszmir Wyciszony"
> i nie jest zgodny z obowiązującą paletą Regalia. Zostaje jako zapis decyzji,
> nie jako wytyczna. Obowiązujące specyfikacje: `01-baza-wiedzy/identyfikacja/`.
```

Dopisz je też do `WYLACZONE_PLIKI` w `sprawdz-dywizy.py` albo przenieś oba do
`_robocze/` - **to jest pytanie otwarte 7, rozstrzygnij je przed tym krokiem.**

- [ ] **Krok 7: Bramki i kontrola palet wycofanych**

```bash
python3 _robocze/narzedzia/sprawdz-palete.py && python3 _robocze/narzedzia/sprawdz-zgodnosc-md.py
echo "bramki: $?"
echo "--- hexy palet wycofanych w plikach żywych ---"
grep -rn -E '#(452430|7A5638|33474F|2E5241|8A6110|2F5A63|938978|752F3F|9F6631|005A80|004D49|803700|007987)' \
  --include='*.md' --include='*.css' --include='*.json' \
  01-baza-wiedzy/ 02-szablony-dokumentow/ 03-pakiet-claude-design/ CLAUDE.md README.md \
  && echo "ZOSTAŁ HEX - popraw" || echo "pliki żywe: czysto"
```

- [ ] **Krok 8: Commit**

```bash
git add -A
git commit -m "Pliki towarzyszące na Regalii; pilot i warianty księgi marki oznaczone jako archiwum"
```

---

## Zadanie 12: Bramka w CI

Bramka uruchamiana ręcznie jest kontekstem, nie blokadą - model i człowiek mogą
ją pominąć. W workflow jest mechanizmem: PR z rozjazdem nie przechodzi.

**Pliki:**
- Utwórz: `_robocze/narzedzia/sprawdz-dywizy.py`
- Utwórz: `.github/workflows/bramka-pomiarowa.yml`

- [ ] **Krok 1: Napisz kontrolę dywizów**

`grep -P` z klasą `\x{...}` zawodzi w części środowisk komunikatem
„character code point value in \x{} is too large" - kontrola, która nie
uruchamia się na runnerze, jest gorsza niż jej brak. Dlatego skrypt.

`_robocze/narzedzia/sprawdz-dywizy.py`:

```python
#!/usr/bin/env python3
# Kontrola zapisu: w perymetrze systemu projektowego obowiązuje dywiz, nie myślnik.
#
# Szuka U+2014 (myślnik) i U+2013 (półpauza). Zakres jest ZAWĘŻONY do perymetru
# planu i to jest decyzja z pomiaru, nie niedbalstwo: w całym repozytorium stoi
# 794 takich znaków w 73 plikach, z czego 183 w 19 plikach perymetru i 611
# w 54 plikach poza nim (prawo, szablony dokumentów, kanwa foundera, archiwum
# _robocze). Bramka obejmująca wszystko blokowałaby każdy PR od pierwszego dnia,
# więc pilnuje tego, co ten plan faktycznie pisze.
#
# Wyłączone jawnie: POMIAR.md i PLAN.md - cytują stronę projektową i myślnik
# w nich występuje w cytacie. Cytatu się nie zmienia.
#
# Uruchomienie: python3 _robocze/narzedzia/sprawdz-dywizy.py [ścieżka ...]
#   bez argumentów - cały perymetr; z argumentami - tylko podane pliki.
# Kod wyjścia 0 = czysto. 1 = trafienie.
import pathlib, sys

ZAKAZANE = {"—": "myślnik (U+2014)", "–": "półpauza (U+2013)"}
ROZSZERZENIA = {".md", ".css", ".json", ".html", ".yml", ".yaml", ".py", ".mjs", ".js"}
WYLACZONE_PLIKI = {"POMIAR.md", "PLAN.md"}
PERYMETR = [
    "01-baza-wiedzy/identyfikacja",
    "_robocze/ds-bundle",
    "_robocze/narzedzia",
    "03-pakiet-claude-design",
    ".github/workflows",
    "CLAUDE.md",
    "README.md",
]

def w_perymetrze(rel):
    return any(rel == k or rel.startswith(k + "/") for k in PERYMETR)

def pliki(argumenty):
    if argumenty:
        for a in argumenty:
            yield pathlib.Path(a)
        return
    for p in sorted(pathlib.Path(".").rglob("*")):
        if not p.is_file() or p.suffix not in ROZSZERZENIA:
            continue
        if p.name in WYLACZONE_PLIKI:
            continue
        if not w_perymetrze(p.as_posix()):
            continue
        yield p

def main():
    trafien = sprawdzonych = 0
    for p in pliki(sys.argv[1:]):
        sprawdzonych += 1
        for nr, w in enumerate(p.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            for znak, nazwa in ZAKAZANE.items():
                if znak in w:
                    print(f"  ! {p}:{nr}  {nazwa}: {w.strip()[:90]}")
                    trafien += w.count(znak)
    print(f"KONTROLA ZAPISU (perymetr): plików {sprawdzonych}, trafień: {trafien}")
    if trafien:
        print("Obowiązuje dywiz '-'. Perymetr: " + ", ".join(PERYMETR))
        print("Poza perymetrem plan świadomie nie zmienia zapisu - patrz PLAN.md, "
              "kryterium 10.")
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Krok 2: Napisz workflow**

```yaml
name: Bramka pomiarowa

on:
  pull_request:
    paths:
      - '01-baza-wiedzy/identyfikacja/**'
      - '_robocze/ds-bundle/**'
      - '_robocze/narzedzia/**'
      - '03-pakiet-claude-design/**'
      - 'CLAUDE.md'
  push:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read

jobs:
  bramka:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Paleta składa się z tego samego źródła
        run: |
          python3 _robocze/narzedzia/zloz-palete.py
          git diff --exit-code -- \
            01-baza-wiedzy/identyfikacja/tokeny/palette-irin.json \
            _robocze/ds-bundle/tokens/tokens.css \
          || { echo "::error::palette-irin.json albo tokens.css nie zgadza się z generatorem."; \
               echo "Uruchom: python3 _robocze/narzedzia/zloz-palete.py"; exit 1; }

      - name: Każda liczba palety odtwarza się z rachunku
        run: python3 _robocze/narzedzia/sprawdz-palete.py

      - name: Proza nie niesie wartości spoza danych maszynowych
        run: python3 _robocze/narzedzia/sprawdz-zgodnosc-md.py

      - name: Guidelines zgadzają się z warstwą 1
        run: |
          python3 _robocze/narzedzia/zloz-paczke.py
          git diff --exit-code -- _robocze/ds-bundle/guidelines/ \
          || { echo "::error::guidelines/ nie zgadza się z warstwą 1."; \
               echo "Uruchom: python3 _robocze/narzedzia/zloz-paczke.py"; exit 1; }

      - name: Brak martwych odnośników względnych
        run: |
          python3 - <<'PY'
          import pathlib, re, sys
          wzor = re.compile(r"\]\(([^)\s#]+)(?:\s+\"[^\"]*\")?\)")
          martwe = 0
          for p in sorted(pathlib.Path(".").rglob("*.md")):
              if ".git" in p.parts: continue
              for nr, w in enumerate(p.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
                  for m in wzor.finditer(w):
                      t = m.group(1)
                      if t.startswith(("http://","https://","mailto:","#")): continue
                      if not (p.parent / t).resolve().exists():
                          print(f"::error file={p},line={nr}::martwy odnośnik: {t}")
                          martwe += 1
          sys.exit(1 if martwe else 0)
          PY

      - name: Brak myślnika i półpauzy w plikach commitowanych
        run: python3 _robocze/narzedzia/sprawdz-dywizy.py
```

- [ ] **Krok 3: Uruchom te same kroki lokalnie**

```bash
python3 _robocze/narzedzia/zloz-palete.py && git diff --exit-code -- \
  01-baza-wiedzy/identyfikacja/tokeny/palette-irin.json _robocze/ds-bundle/tokens/tokens.css \
  && echo "generator: idempotentny"
python3 _robocze/narzedzia/zloz-paczke.py && git diff --exit-code -- _robocze/ds-bundle/guidelines/ \
  && echo "guidelines: idempotentne"
python3 _robocze/narzedzia/sprawdz-palete.py && python3 _robocze/narzedzia/sprawdz-zgodnosc-md.py \
  && echo "obie bramki otwarte"
python3 _robocze/narzedzia/sprawdz-dywizy.py
```

Oczekiwane: `generator: idempotentny`, `guidelines: idempotentne`,
`obie bramki otwarte`, `dywizy: OK`.

**Uwaga o zakresie - zmierzona, nie przyjęta.** W całym repozytorium stoi
**794** myślników i półpauz w **73** plikach: **183 w 19 plikach perymetru**
i **611 w 54 plikach poza nim** (`01-baza-wiedzy/prawo/`,
`02-szablony-dokumentow/`, `brandbook.dc.html`, `_robocze/copilot-v1/`).
Bramka obejmująca wszystko blokowałaby każdy PR od pierwszego dnia, więc
pilnuje perymetru - tego, co ten plan faktycznie pisze. Pozostałe 611 zostaje
i jest tak zapisane w kryterium 10; to nie jest przeoczenie, tylko zakres.

`POMIAR.md` i `PLAN.md` cytują stronę projektową i myślnik w nich występuje
w cytacie - są wyłączone w zbiorze `WYLACZONE_PLIKI`. **Cytatu się nie zmienia.**

- [ ] **Krok 4: Commit**

```bash
git add _robocze/narzedzia/sprawdz-dywizy.py .github/workflows/bramka-pomiarowa.yml
git commit -m "Bramka pomiarowa w CI: PR z rozjazdem nie przechodzi"
```

---

# BLOK B - nowy projekt Claude Design

Blok B zaczyna się **dopiero po zamknięciu bloku A**. Powód jest zmierzony:
projektowy `tokens.css` wskazuje dziś jako źródło prawdy Regalii plik
`01-baza-wiedzy/identyfikacja/paleta-barw.md` w tym repozytorium, a ten plik
niesie paletę v2 (`POMIAR.md` rozdz. 9.3). Nowy projekt założony przed
przepisaniem warstwy 1 odtworzyłby tę samą pętlę odwołań w pierwszym dniu.

**Czego blok B nie robi:** nie kasuje starego projektu. Zadanie 16 oznacza go
jako archiwum; usunięcie jest decyzją właściciela.

---

## Zadanie 13: Wyniesienie szesnastu szablonów ze starego projektu

Szesnaście wzorów nośników w `templates/` po stronie starego projektu jest
**już na Regalii** - zmierzone, pokrycie pełne (`POMIAR.md` rozdz. 9.2). To
jedyna praca, która nie powtarza się z bloku A, i jedyna rzecz, którą trzeba
przenieść ręcznie: `/design-sync` idzie z repozytorium do projektu, a nośniki
nie mieszkają w repozytorium (`CLAUDE.md`: „Nie zakładaj wzoru nośnika po
stronie repozytorium").

**Pliki:**
- Utwórz na dysku roboczym, **nie w repozytorium**: `<katalog-roboczy>/templates/`

**Interfejsy:**
- Konsumuje: stary projekt `1a22ce64-0e1c-43a6-bd60-eef9241ef73b` przez
  `DesignSync` metodą `get_file`.
- Produkuje: szesnaście katalogów po `<Nazwa>.dc.html`, `support.js`
  i `ds-base.js`, gotowych do wniesienia w zadaniu 15.

- [ ] **Krok 1: Wypisz, co jest do wyniesienia**

`DesignSync` metodą `list_files` na starym projekcie. Szesnaście wzorów:

```
templates/favicon/Favicon.dc.html
templates/karta-uslugi/KartaUslugi.dc.html
templates/karta-uslugi-bur/KartaUslugiBur.dc.html
templates/katalog-uslug/KatalogUslug.dc.html
templates/koperta/Koperta.dc.html
templates/notatka-wewnetrzna/NotatkaWewnetrzna.dc.html
templates/okladka/Okladka.dc.html
templates/okladka-wydawnicza/OkladkaWydawnicza.dc.html
templates/papier-firmowy/PapierFirmowy.dc.html
templates/podpis-mailowy/PodpisMailowy.dc.html
templates/prezentacja/Prezentacja.dc.html
templates/slajd-16-9/Slajd169.dc.html
templates/tabela-danych/TabelaDanych.dc.html
templates/wizytowka/Wizytowka.dc.html
templates/zaswiadczenie/Zaswiadczenie.dc.html
templates/zestaw-drobnych/ZestawDrobnych.dc.html
```

Do każdego dochodzą `support.js` i `ds-base.js` w tym samym katalogu.
`.thumbnail` **nie przenosimy** - miniatury odtwarza panel.

- [ ] **Krok 2: Wynieś każdy plik na dysk roboczy**

Dla każdej z szesnastu pozycji: `DesignSync` metodą `get_file` z `projectId`
starego projektu, treść zapisz pod tą samą ścieżką względną w katalogu
roboczym. To samo dla `support.js` i `ds-base.js` z każdego katalogu.

Kontrola liczby:

```bash
find <katalog-roboczy>/templates -name '*.dc.html' | wc -l    # oczekiwane: 16
find <katalog-roboczy>/templates -name 'support.js' | wc -l   # oczekiwane: 16
find <katalog-roboczy>/templates -name 'ds-base.js' | wc -l   # oczekiwane: 16
```

- [ ] **Krok 3: Sprawdź, że żaden szablon nie niesie barwy spoza Regalii**

```bash
python3 - <<'PY'
import json, pathlib, re, sys
KAT = pathlib.Path("<katalog-roboczy>/templates")
d = json.loads(pathlib.Path("01-baza-wiedzy/identyfikacja/tokeny/palette-irin.json")
               .read_text(encoding="utf-8"))
dozwolone = {v["hex"].upper() for v in d["barwy"].values()}
dozwolone |= {t["hex"].upper() for t in d["tinty"].values()}
dozwolone |= {"#FFFFFF", "#000000"}
zle = 0
for p in sorted(KAT.rglob("*.dc.html")):
    obce = {}
    for nr, w in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
        for hx in re.findall(r"#[0-9A-Fa-f]{6}\b", w):
            if hx.upper() not in dozwolone:
                obce.setdefault(hx.upper(), []).append(nr)
        for tok in re.findall(r"var\(--irin-(?!r-)[a-z0-9-]+\)", w):
            obce.setdefault(tok, []).append(nr)
    print(f"{'ZŁE ' if obce else 'OK  '} {p.name:28} " +
          (", ".join(f"{k} w {len(v)} miejscach" for k, v in obce.items()) or "czysto"))
    zle += bool(obce)
print(f"\nszablonów: {len(list(KAT.rglob('*.dc.html')))}, z obcymi wartościami: {zle}")
sys.exit(1 if zle else 0)
PY
```

Oczekiwane: szesnaście wierszy `OK`, `z obcymi wartościami: 0`. Szablony niosą
Regalię wprost i gniazdo `--irin-r-dziedzina`; token bez `r-` byłby resztką
po warstwie v5.1.

- [ ] **Krok 4: Popraw dwa szablony z niewłaściwą domyślą obszaru**

To R13 z `POMIAR.md`. Decyzja z 2026-09-09 mówi, że obszary są wymienne
i gniazdo jest domyślnie neutralne. `karta-uslugi`, `karta-uslugi-bur`
i `tabela-danych` mają w mapie `DZ` domyślne `'Bez obszaru'`. **`okladka`
i `slajd-16-9` mają `'Szkolenia zawodowe'`** - dwa szablony na szesnaście
odstają od decyzji.

W obu plikach: w bloku `data-props` zmień `"default":"Szkolenia zawodowe"`
na `"default":"Bez obszaru"`, w mapie `DZ` dopisz wpis
`'Bez obszaru': { k: '#132246', t: '#DCDAD5', n: 'Bez obszaru' }` na początku
i zmień domyślę w `barwa()` z `this.DZ['Szkolenia zawodowe']` na
`this.DZ['Bez obszaru']`.

```bash
grep -n "Szkolenia zawodowe" <katalog-roboczy>/templates/okladka/Okladka.dc.html \
                             <katalog-roboczy>/templates/slajd-16-9/Slajd169.dc.html | head
```

Po poprawce `"default"` w obu plikach musi brzmieć `"Bez obszaru"`.

- [ ] **Krok 5: Popraw dwie sprzeczności wewnątrz szablonów**

Oba rozjazdy są zmierzone i oba są resztkami po poprzednim wydaniu - zostały,
bo poprawka dotknęła jednego akapitu, a nie sąsiedniego.

**R14, `zestaw-drobnych/ZestawDrobnych.dc.html`, kafel 01.** Dwa akapity, drugi
przeczy pierwszemu. Pierwszy mówi „Stan niesie słowo, nie barwa - wszystkie
cztery plakietki mają jedno wykonanie". Drugi mówi „Każdy stan ma słowo **obok
barwy**… Zieleń i Rubin schodzą do 70 % K" i opisuje wycofane wykonanie barwne.
**Usuń drugi akapit w całości** (ten zaczynający się od `<b…>Każdy stan ma
słowo obok barwy</b>`), zostaw pierwszy. Zdanie o niemożności rozróżnienia
plakietek na wypełnieniu barwy obszaru (`Rubin na Rubinie 1,00`) przenieś do
akapitu pierwszego - to jest liczba, która nadal obowiązuje.

**R15, `okladka-wydawnicza/OkladkaWydawnicza.dc.html`, protokół pomiaru.**
Punkt o znaku mówi „**95 mm** od góry", a kod ustawia `top:96mm` i punkt
o rytmie w tym samym pliku wywodzi 96 mm, nazywając 95 mm wartością poprawioną.
Zamień `95 mm` na `96 mm` w punkcie o znaku. Zachowaj zdanie o tym, że rozdz. 16
brandbooka podaje 95 mm i jest do przepisania - to jest zapis rozjazdu z
dokumentem, nie błąd nośnika.

```bash
grep -n "95 mm" <katalog-roboczy>/templates/okladka-wydawnicza/OkladkaWydawnicza.dc.html
grep -c "obok barwy" <katalog-roboczy>/templates/zestaw-drobnych/ZestawDrobnych.dc.html
```

Po poprawce: `95 mm` występuje wyłącznie w zdaniu o rozdz. 16, a `obok barwy`
zero razy.

- [ ] **Krok 6: Zapisz protokół wyniesienia**

Do `<katalog-roboczy>/protokol-wyniesienia.md`: data, identyfikator starego
projektu, lista szesnastu plików z liczbą znaków każdego, wynik kroku 3
i lista poprawek z kroków 4 i 5. Ten plik **nie wchodzi do repozytorium** -
jest dowodem na czas przenoszenia i ginie razem z katalogiem roboczym.

---

## Zadanie 14: Nowy projekt i zasiew z repozytorium

> **Wykonane częściowo 2026-09-09, poza kolejnością, na polecenie właściciela.**
> Projekt „IRIN - system projektowy (Regalia)" utworzony,
> `04ac99a2-1ffd-4632-bc63-f2a19df08c53`. Fala 1 wysłana: 10 plików
> (tokeny, trzy specyfikacje jako `guidelines/`, znak, `fonts.css`, `README.md`),
> potwierdzone przez `list_files`. Fala 2 czeka na zadania 7-10.
> `.design-sync/config.json` **świadomie nie przełączony** - paczka
> `_robocze/ds-bundle` stoi jeszcze na v2, więc przełączenie teraz wlałoby v2
> do projektu na Regalii. Szczegóły i stan:
> [`_robocze/porzadek-w-projekcie-claude-design.md`](./_robocze/porzadek-w-projekcie-claude-design.md).


**Interfejsy:**
- Konsumuje: `_robocze/ds-bundle/` po bloku A, trzy pliki SVG z korzenia.
- Produkuje: `projectId` nowego projektu, wpisany w zadaniu 16 do
  `.design-sync/config.json`.

- [ ] **Krok 1: Sprawdź, że blok A jest naprawdę zamknięty**

```bash
git status --short                                        # oczekiwane: pusto
python3 _robocze/narzedzia/sprawdz-palete.py && \
python3 _robocze/narzedzia/sprawdz-zgodnosc-md.py && echo "obie bramki otwarte"
```

Zasiew z repozytorium, którego bramki nie przechodzą, przenosi rozjazd do
nowego projektu. **Nie zaczynaj tego zadania przed `obie bramki otwarte`.**

- [ ] **Krok 2: Załóż projekt**

`DesignSync` metodą `create_project`, `name`: `System projektowy IRIN`.
Zapisz zwrócony `projectId` - jest potrzebny w krokach 3-5 i w zadaniach 15-16.

- [ ] **Krok 3: Sprawdź, że to projekt typu design system**

`DesignSync` metodą `get_project` z nowym `projectId`. Pole `type` musi brzmieć
`PROJECT_TYPE_DESIGN_SYSTEM`. Ten typ jest **niezmienny po założeniu**: zasiew
do zwykłego projektu nie zrobi z niego systemu projektowego i trzeba zakładać
od nowa.

- [ ] **Krok 4: Zasiej paczkę**

`finalize_plan` z `localDir` ustawionym na korzeń repozytorium i `writes`:

```
styles.css
tokens/**
fonts/**
guidelines/**
components/**
assets/**
README.md
```

Potem `write_files` z tym `planId`, mapując ścieżki lokalne na ścieżki projektu:

| Lokalnie | W projekcie |
|---|---|
| `_robocze/ds-bundle/styles.css` | `styles.css` |
| `_robocze/ds-bundle/tokens/tokens.css` | `tokens/tokens.css` |
| `01-baza-wiedzy/identyfikacja/tokeny/palette-irin.json` | `tokens/palette-irin.json` |
| `_robocze/ds-bundle/fonts/fonts.css` | `fonts/fonts.css` |
| `_robocze/ds-bundle/fonts/OFL.txt` | `fonts/OFL.txt` |
| `_robocze/ds-bundle/guidelines/*.md` (5 plików) | `guidelines/*.md` |
| `_robocze/ds-bundle/components/**/*.html` (8 kart) | `components/**/*.html` |
| `_robocze/ds-bundle/README.md` | `README.md` |
| `logo_irin_poziom.svg`, `logo_irin_pion.svg`, `logo_irin_sygnet.svg` | `assets/<ta sama nazwa>` |

Trzy pliki SVG idą do `assets/`, bo szesnaście szablonów woła je ścieżką
`../../assets/logo_irin_<wariant>.svg` - to zmierzone w każdym z nich.

- [ ] **Krok 5: Sprawdź, co wylądowało**

`DesignSync` metodą `list_files` na nowym projekcie. Oczekiwane, dokładnie:
`styles.css`, `README.md`, `tokens/tokens.css`, `tokens/palette-irin.json`,
`fonts/fonts.css`, `fonts/OFL.txt`, pięć plików w `guidelines/`, osiem kart
w `components/`, trzy pliki w `assets/`. Razem **dwadzieścia dwa pliki**
plus `_ds_manifest.json` złożony przez panel.

Potem `get_file` na `_ds_manifest.json` i kontrola:
- `cards` ma **osiem** pozycji, każda z `group` `Fundamenty` albo `Prymitywy`;
- `globalCssPaths` zawiera `fonts/fonts.css`, `tokens/tokens.css`, `styles.css`;
- `tokens` ma **49** pozycji, wszystkie z prefiksem `--irin-r-`;
- **żadna** pozycja `tokens` nie nazywa się `--irin-r-success`,
  `--irin-r-warning` ani `--irin-r-error`;
- `components` jest pustą listą - to stan docelowy, nie brak. Repozytorium nie
  ma komponentów kodowych i nie planowano ich; `README.md` paczki mówi to wprost.

---

## Zadanie 15: Wniesienie szesnastu szablonów

- [ ] **Krok 1: Zasiej `templates/`**

`finalize_plan` z `localDir` ustawionym na katalog roboczy z zadania 13
i `writes`: `templates/**`. Potem `write_files` z tym `planId`, po jednym
wpisie na każdy plik - szesnaście `.dc.html` plus po `support.js`
i `ds-base.js` w każdym katalogu, razem czterdzieści osiem plików.
Limit `write_files` to 256 plików na wywołanie, więc jedno wystarczy.

- [ ] **Krok 2: Sprawdź liczbę i treść**

`list_files` na nowym projekcie. `templates/` musi mieć szesnaście katalogów.
Potem `get_file` na trzech szablonach o różnym mechanizmie - `papier-firmowy`
(gniazdo obszaru w `style`), `karta-uslugi-bur` (mapa `DZ` w logice),
`favicon` (rasteryzacja na `canvas`) - i kontrola, że treść dojechała
w całości: każdy musi się kończyć na `</html>`.

- [ ] **Krok 3: Sprawdź, że gniazdo obszaru rozwiązuje się w nowym projekcie**

To jedyny punkt, w którym szablony spotykają się z tokenami z repozytorium.
`get_file` na `_ds_manifest.json` i kontrola, że `templates` ma szesnaście
pozycji, każda z `entryPath` wskazującym istniejący plik.

Kontrola merytoryczna, lokalnie na wyniesionych plikach:

```bash
grep -rl "irin-r-dziedzina" <katalog-roboczy>/templates | wc -l
```

Oczekiwane: **6** - tyle szablonów czyta obszar z gniazda (zmierzone:
`papier-firmowy`, `wizytowka`, `karta-uslugi`, `karta-uslugi-bur`,
`tabela-danych`, `prezentacja`). Pozostałe dziesięć nie nosi obszaru wcale
i to jest poprawne: koperta, podpis mailowy, favicon, notatka wewnętrzna,
zaświadczenie, okładka wydawnicza, zestaw drobnych, katalog usług, okładka
i slajd 16:9 mają barwę materiału albo obszar podawany słowem.

- [ ] **Krok 4: Zapisz, czego ten krok nie sprawdził**

Do `<katalog-roboczy>/protokol-wyniesienia.md` dopisz wprost: **nie otwarto
żadnego szablonu w kanwie.** `list_files` i `get_file` potwierdzają, że pliki
dojechały i mają właściwą treść; nie potwierdzają, że panel je renderuje.
Falsyfikator: otwarcie jednego szablonu w przeglądarce i sprawdzenie, że znak
się wstrzykuje, a gniazdo obszaru daje Szafir Nocny. To zadanie właściciela -
wymaga sesji z zalogowanym kontem.

---

## Zadanie 16: Przełączenie synchronizacji i zamknięcie

- [ ] **Krok 1: Przełącz `.design-sync/config.json` na nowy projekt**

```json
{
  "projectId": "<identyfikator z zadania 14>",
  "projectName": "System projektowy IRIN",
  "shape": "off-script",
  "bundleDir": "_robocze/ds-bundle",
  "uwaga": "Repozytorium nie ma biblioteki komponentów w kodzie (brak package.json, dist/, Storybooka) i to jest stan docelowy, nie brak. Paczka to arkusz, tokeny generowane z palette-irin.json, pięć plików guidelines i osiem kart podglądu. Wzory nośników mieszkają w templates/ po stronie projektu i nie wracają tu. Kierunek synchronizacji jest jeden: repozytorium do projektu.",
  "poprzedni-projekt": "1a22ce64-0e1c-43a6-bd60-eef9241ef73b - archiwum, paleta v5.1 i iteracje v3-v7; nie synchronizować"
}
```

- [ ] **Krok 2: Dopisz do `CLAUDE.md` sekcję o kierunku synchronizacji**

Jedno miejsce, w którym stoi zdanie, którego zabrakło: „`/design-sync` idzie
**z repozytorium do projektu** i tylko tak. Wartość palety, tokenu, skali,
siatki, arkusza i karty zmienia się w repozytorium. Wzór nośnika zmienia się
w projekcie, w `templates/`, i nie wraca tu. Zmiana tokenów po stronie projektu
rozejdzie się z repozytorium bez ostrzeżenia - to się już zdarzyło i jest
zmierzone w `POMIAR.md` rozdz. 9.4."

Dopisz też identyfikator nowego projektu i jednozdaniową notę, że stary
(`1a22ce64-…`) jest archiwum.

- [ ] **Krok 3: Zaktualizuj `README.md` i domknij `PLAN.md`**

`README.md`: stan `paleta Regalia w warstwie 1, paczka zasiana do nowego
projektu`, data, dwie komendy bramek jako sposób sprawdzenia.

W `PLAN.md` odhacz wszystkie kroki i dopisz na końcu sekcji `## Weryfikacja`
wynik każdego kryterium z liczbą.

- [ ] **Krok 4: Weryfikacja końcowa - wszystkie kryteria naraz**

```bash
echo "=== 1. generator idempotentny ==="
python3 _robocze/narzedzia/zloz-palete.py >/dev/null && \
  git diff --exit-code -- 01-baza-wiedzy/identyfikacja/tokeny/palette-irin.json \
                          _robocze/ds-bundle/tokens/tokens.css && echo OK
echo "=== 2. bramka pomiarowa ==="
python3 _robocze/narzedzia/sprawdz-palete.py | tail -2
echo "=== 3. bramka spójności ==="
python3 _robocze/narzedzia/sprawdz-zgodnosc-md.py | tail -2
echo "=== 4. guidelines idempotentne ==="
python3 _robocze/narzedzia/zloz-paczke.py >/dev/null && \
  git diff --exit-code -- _robocze/ds-bundle/guidelines/ && echo OK
echo "=== 5. zero hexów palet wycofanych w plikach żywych ==="
grep -rn -E '#(452430|7A5638|33474F|2E5241|8A6110|2F5A63|938978|752F3F|9F6631|005A80|004D49|803700|007987|3D3D00)' \
  --include='*.md' --include='*.css' --include='*.json' \
  01-baza-wiedzy/ 02-szablony-dokumentow/ 03-pakiet-claude-design/ _robocze/ds-bundle/ \
  CLAUDE.md README.md && echo "ZOSTAŁ HEX" || echo OK
echo "=== 6. zero martwych odnośników ==="
python3 - <<'PY'
import pathlib, re
wzor = re.compile(r"\]\(([^)\s#]+)(?:\s+\"[^\"]*\")?\)")
m = 0
for p in sorted(pathlib.Path(".").rglob("*.md")):
    if ".git" in p.parts: continue
    for nr, w in enumerate(p.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
        for x in wzor.finditer(w):
            t = x.group(1)
            if t.startswith(("http://","https://","mailto:","#")): continue
            if not (p.parent / t).resolve().exists():
                print(f"  ! {p}:{nr} -> {t}"); m += 1
print("OK" if m == 0 else f"MARTWYCH: {m}")
PY
echo "=== 7. reguły druku obecne ==="
grep -c "print-color-adjust" _robocze/ds-bundle/styles.css
echo "=== 8. licencja krojów obecna ==="
test -s _robocze/ds-bundle/fonts/OFL.txt && echo OK || echo BRAK
echo "=== 9. zero tokenów stanu w arkuszu i tokenach ==="
grep -rn -E '\-\-irin-r-(success|warning|error)' _robocze/ds-bundle/ && echo "TOKEN STANU" || echo OK
echo "=== 10. dywizy ==="
python3 _robocze/narzedzia/sprawdz-dywizy.py
```

Dziesięć kryteriów, dziesięć razy `OK`. Cokolwiek innego zamyka zadanie 16.

- [ ] **Krok 5: Commit i pull request**

```bash
git add -A
git commit -m "Synchronizacja przełączona na nowy projekt; blok A i B zamknięte"
git push -u origin claude/irin-pomiar-raport-xsbs7j
```

---

# Kolejność

**Blok A jest sekwencyjny w dwóch miejscach i tylko w dwóch.**

```
1 bramka pomiarowa
  └─ 2 generator + JSON + tokens.css        <- wszystko dalej stoi na tym
       ├─ 3 bramka spójności
       │    ├─ 4 paleta-barw.md    ┐
       │    ├─ 5 typografia.md     │ te cztery można robić równolegle:
       │    ├─ 6 siatka-a4.md      │ różne pliki, wspólna bramka
       │    └─ 7 logotyp.md        ┘
       ├─ 8 styles.css + druk + OFL
       │    └─ 9 osiem kart        <- karty używają klas z zadania 8
       └─ 10 guidelines            <- potrzebuje zadań 4-7
            └─ 11 pliki towarzyszące
                 └─ 12 bramka w CI <- ostatnie, bo blokuje PR z rozjazdem

Blok B, dopiero po 12:
13 wyniesienie szablonów  ─┐
                           ├─ 15 wniesienie szablonów ─ 16 przełączenie i zamknięcie
14 nowy projekt + zasiew  ─┘
```

Zadania 13 i 14 są od siebie niezależne - wyniesienie czyta stary projekt,
zasiew pisze do nowego. Można je robić w dowolnej kolejności albo równolegle.

**Ryzyka blokujące, oba z pomiaru:**
1. Zadanie 14 krok 3 - jeżeli `get_project` nie zwróci
   `PROJECT_TYPE_DESIGN_SYSTEM`, projekt trzeba założyć od nowa. Typ jest
   niezmienny po założeniu, więc ten krok jest przed zasiewem, nie po.
2. Zadanie 13 krok 3 - jeżeli któryś szablon niesie wartość spoza Regalii,
   nie przenoś go w tym stanie. Zgłoś to jako osobną pozycję, bo znaczy, że
   pomiar pokrycia z `POMIAR.md` rozdz. 9.2 miał dziurę.

---

# Weryfikacja

Plan domyka się, gdy **wszystkie dziesięć** kryteriów daje wynik jak niżej.
Komendy stoją w zadaniu 16 krok 4; tu są kryteria z liczbami.

| # | Kryterium | Sprawdzenie | Wynik wymagany |
|---|---|---|---|
| 1 | Generator jest idempotentny | `zloz-palete.py` i `git diff --exit-code` | brak różnicy |
| 2 | Każda liczba palety odtwarza się z rachunku | `sprawdz-palete.py` | `rozjazdów: 0` przy `sprawdzonych twierdzeń: 226` |
| 3 | Proza nie niesie wartości spoza danych | `sprawdz-zgodnosc-md.py` | `rozjazdów: 0` |
| 4 | `guidelines/` zgadza się z warstwą 1 | `zloz-paczke.py` i `git diff --exit-code` | brak różnicy |
| 5 | Zero hexów palet wycofanych w plikach żywych | `grep` na 14 hexach | zero trafień |
| 6 | Zero martwych odnośników względnych | skrypt w zadaniu 16 | `martwych: 0` (przed planem: 17) |
| 7 | Paczka ma reguły druku | `grep print-color-adjust` | co najmniej 1 |
| 8 | Licencja krojów podróżuje z fontem | `test -s fonts/OFL.txt` | plik niepusty |
| 9 | Zero tokenów stanu | `grep --irin-r-(success\|warning\|error)` | zero trafień |
| 10 | Dywiz, nie myślnik w perymetrze | `sprawdz-dywizy.py` | `trafień: 0` (przed planem: 183 w 19 plikach) |

Osobno, w bloku B:

| # | Kryterium | Sprawdzenie | Wynik wymagany |
|---|---|---|---|
| 11 | Nowy projekt jest systemem projektowym | `get_project`, pole `type` | `PROJECT_TYPE_DESIGN_SYSTEM` |
| 12 | Paczka dojechała w całości | `list_files` | 22 pliki plus `_ds_manifest.json` |
| 13 | Manifest widzi osiem kart i 49 tokenów | `get_file` na `_ds_manifest.json` | `cards` = 8, `tokens` = 49, zero tokenów stanu |
| 14 | Szesnaście szablonów dojechało | `list_files` na `templates/` | 16 katalogów, 48 plików |
| 15 | Sześć szablonów czyta gniazdo obszaru | `grep irin-r-dziedzina` | dokładnie 6 |

## Pokrycie rozjazdów z `POMIAR.md`

Piętnaście rozjazdów zmierzonych w `POMIAR.md`, każdy z adresem w tym planie.

| # | Rozjazd | Gdzie zamykany |
|---|---|---|
| R1 | dryf rytmu 19 mm zamiast 20,86 mm, w trzech plikach | zadania 2, 5, 6 |
| R2 | etykieta marginesów 18 / 22 obok kodu 20 / 20 | zadanie 11 krok 5 (oznaczenie archiwum) |
| R3 | wycofany Popiół `#938978` w wariantach księgi marki | zadanie 11 krok 3 |
| R4 | siedemnaście martwych odnośników w `guidelines/` | zadanie 10 |
| R5 | pilot nie czyta tokenów ani arkusza paczki | zadanie 11 krok 5 |
| R6 | brakujący `support.js` w artboardach pilota | zadanie 11 krok 5 |
| R7 | Rubin na Kaszmirze 10,62 zamiast 4,78 (wartość Oliwinu) | strona projektowa, pytanie otwarte 5 |
| R8 | etykieta Pergaminu na Rubinie 8,51 zamiast 3,83, pod progiem | strona projektowa, pytanie otwarte 5 |
| R9 | etykieta bieli na Rubryce 8,04 zamiast 8,52 | strona projektowa, pytanie otwarte 5 |
| R10 | Karmin na Kaszmirze 5,94, pochodzenia nie ustalono | strona projektowa, pytanie otwarte 5 |
| R11 | osiem kart niesie wartości sprzed podmiany tokenów | zadanie 9 (karty nie wpisują wartości wprost) |
| R12 | Lapis na Aksamicie Nocy 2,55 poza listą par zabronionych | zadania 2 i 4 (plus kontrola kompletności w bramce) |
| R13 | dwa szablony z domyślą obszaru wbrew decyzji | zadanie 13 krok 4 |
| R14 | dwa sprzeczne akapity w `zestaw-drobnych` | zadanie 13 krok 5 |
| R15 | „95 mm" obok kodu ustawiającego 96 mm | zadanie 13 krok 5 |

Cztery pozycje (R7-R10) leżą po stronie projektowej, w warstwie v5.1, której
repozytorium po tym planie w ogóle nie karmi. Przestają szkodzić nowej pracy
i **nie przestają istnieć w starym projekcie** - dlatego są pytaniem, nie zadaniem.

**Czego ta weryfikacja nie obejmuje - i nie udaje, że obejmuje:**
- **Wydruku.** Cztery falsyfikatory zostają otwarte i są tak oznaczone
  w `palette-irin.json`, kluczu `falsyfikatory-otwarte`: grubości linii
  `0,25` i `0,5 mm`, minimum samodzielnego sygnetu `10 mm`, czytelność
  diakrytyków przy stopniu podłogi, CMYK bez proofu.
- **Renderu w kanwie.** Kryteria 12-15 potwierdzają, że pliki dojechały
  i mają właściwą treść. Nie potwierdzają, że panel je rysuje. To wymaga
  sesji z zalogowanym kontem właściciela.
- **Objętości dokumentu w wybranym układzie księgi marki.** Pomiar otwarty
  od 2026-09-03, wpisany w rejestr decyzji niżej.

---

# Otwarte pytania

Pytania, na które nie odpowiem sam, i te, których odpowiedź zmienia plan.
Numer w nawiasie to zadanie, przed którym odpowiedź jest potrzebna.
Numery pytań są stałe i nie przenumerowują się po rozstrzygnięciu: **pytanie 1
(przypisanie barw do obszarów) zostało rozstrzygnięte 2026-09-09** i stoi
w rejestrze niżej, dlatego lista zaczyna się od dwójki.

2. **(przed zadaniem 6) Czy siatka slajdu 16:9 wchodzi do warstwy 1 jako
   propozycja, czy nie wchodzi wcale?** Rachunek się domyka
   (`6 × 253 + 5 × 42 = 1728 px`, `888 = 37 × 24`) i obala liczbę z rozdz. 17
   brandbooka (gutter `32 px` daje `261,33 px` na kolumnę). Plan wpisuje ją
   jako **jawnie oznaczoną propozycję**. Alternatywa: zostaje wyłącznie po
   stronie projektowej, a `siatka-a4.md` mówi tylko o A4.
3. **(przed zadaniem 13) Co z czterema plikami wydania 01 po stronie starego
   projektu?** `_archiwum/wydania-01/` niesie brandbook, księgę znaku, papier
   firmowy i audyt na palecie sprzed Regalii. Plan ich nie przenosi. Jeżeli
   któryś jest w obiegu poza projektem, trzeba wiedzieć który - inaczej
   materiał w obiegu przestanie mieć źródło.
4. **(przed zadaniem 16) Czy stary projekt zostaje, czy idzie do usunięcia?**
   Plan go zostawia i oznacza jako archiwum. Usunięcie jest nieodwracalne
   i niesie 67 plików archiwum palet v3-v7, których nigdzie indziej nie ma.
5. **(nie blokuje) Czy zgłaszam R7-R10 stronie projektowej?** Cztery błędne
   kontrasty w projektowej tablicy v5.1, w tym etykieta Pergaminu na Rubinie
   `3,83` przy progu `4,5`. Po przejściu na Regalię warstwa v5.1 przestaje
   być czymkolwiek karmiona z repozytorium, więc te błędy przestają szkodzić
   nowej pracy - ale zostają w starym projekcie i w materiałach, które z niego
   wyszły.
7. **(przed zadaniem 11 krok 5) Co z dwoma plikami z epoki palety v2
   w `03-pakiet-claude-design/`?** `propozycja-palety-i-siatki-do-potwierdzenia.md`
   (57 myślników, historia pierwszej decyzji o palecie) i `zlecenia/pilot-papier-firmowy*.md`
   (30, zlecenie złożone na v2). Trzy wyjścia: (a) zostają na miejscu z nagłówkiem
   `ARCHIWUM` i wyłączeniem z bramki zapisu; (b) idą do `_robocze/`, gdzie
   `CLAUDE.md` już mówi, że nic nie jest źródłem prawdy bez weryfikacji;
   (c) usunięte, bo decyzje z nich są w rejestrze na końcu tego planu.
   **Plan przyjmuje (a)** jako najmniej nieodwracalne.

6. **(nie blokuje) Kiedy wydruk próbny?** Cztery falsyfikatory czekają na
   papier i żaden z nich nie domknie się w kodzie: grubości `0,25` i `0,5 mm`,
   minimum sygnetu `10 mm`, czytelność diakrytyków przy `8,5 px`, CMYK bez
   proofu. Do tego czasu są oznaczone jako niepotwierdzone i tak mają zostać.

---

# Rejestr decyzji foundera

Przeniesiony w całości z poprzedniej wersji `PLAN.md`. „Destylacja bez
historii" dotyczy iteracji palety, nie decyzji - decyzje jadą dalej. Pełna
poprzednia treść pliku, wraz z kolejką zadań 1-23, została w historii gita
(`git show 4f11286:PLAN.md`).

## Rozstrzygnięte

- **Barwy dostępne dobierane do materiału (2026-09-09).** Rubin Głęboki,
  Zieleń Butelkowa, Bursztyn Wyciszony i Ametyst Dworski **nie są przypisane
  do obszarów działalności** - obszary są wymienne, więc barwę wybiera się
  do materiału i wstawia w gniazdo `--irin-r-dziedzina`. Rozstrzyga to
  sprzeczność między stroną 07 `irn-design-paleta-kolorow.html` (przypisanie
  z adnotacją „propozycja wymagająca zatwierdzenia") a nowszym zapisem
  w projektowym `tokens.css` z 2026-09-06; obowiązuje nowszy. Skutek: sekcja
  gniazda w `paleta-barw.md` mówi to wprost, mapy `DZ` w szablonach zostają
  wymienne, a falsyfikator „przypisanie barw dostępnych do obszarów" wypada
  z listy otwartych - było ich sześć, zostaje pięć.

- **Paleta Regalia (2026-09-03; wpisana do warstwy 1 2026-09-09).**
  14 wartości, prefiks `--irin-r-`, gniazdo obszaru. Zatwierdzona po stronie
  projektowej 2026-09-03, dopisana do projektowego `tokens.css` 2026-09-06.
  Sprawdzona w tej sesji od zera: 30 z 30 zadeklarowanych kontrastów i 4 z 4
  tinty odtworzone co do setnej (`POMIAR.md` rozdz. 9.1).
  **Decyzja o kierunku (2026-09-09):** repozytorium przechodzi na Regalię
  od razu, nie przez warstwę v5.1. Powód: v5.1 ma cztery błędne kontrasty
  z trzydziestu, w tym jeden poniżej progu dostępności.
  **Decyzja o kolejności (2026-09-09):** najpierw destylacja repozytorium,
  potem nowy projekt Claude Design. Powód: pętla odwołań leży po stronie
  repozytorium, a nowy projekt założony przed jej rozcięciem odtworzyłby ją.

- **Układ księgi marki - wariant 1 „Kaszmir uporządkowany" (2026-09-03).**
  Founder wybrał wariant 1 spośród trzech z `_robocze/brandbook-warianty/`.
  Oś wariacji to układ, rytm i nośnik hierarchii, nie kolor: wariant 1
  prowadzi przepływ redakcyjny na pełnych sześciu kolumnach i hierarchię
  niesie stopniem pisma. Decyzja jest wbrew rekomendacji notatki warsztatowej,
  która wskazywała wariant 2, i to jest w porządku - ale koszt trzeba znać:
  pełna skala robi dużo światła i przy realnej treści dokumentu regulowanego
  pierwsza sekcja potrafi zająć pół strony A4.
  **Pomiar otwarty:** złożyć w wariancie 1 jeden realny dokument z warstwy 2
  i policzyć strony. Do tego czasu wybór stoi na kierunku, nie na objętości.
  **Uwaga z 2026-09-09:** wybór dotyczył układu, nie barw. Trzy pliki
  wariantów są na palecie v2 i zadanie 11 oznacza je jako archiwum.

- **Jednostka bazowa 6 mm - jednostka odstępu, nie siatka linii bazowych
  (2026-09-02).** Interlinia korpusu `5,54 mm` nie jest wielokrotnością
  `6 mm`. Margines dolny zostaje `28 mm`. Prawdziwa siatka linii bazowych
  wymagałaby interlinii około `1,68` zamiast `1,55`, czyli zmiany typografii
  o osiem procent - nie wprowadzono.
  **Poprawka liczby z 2026-09-09:** dryf na pełnej kolumnie to **`20,86 mm`
  przy 45 liniach**, nie `19 mm`. Liczba `19 mm` to dryf na 41 jednostkach
  siatki, wpisany obok etykiety „45 linii" - dwie liczby z różnych rachunków
  w jednym wierszu. Poprawka **nie obala** rozstrzygnięcia: nowa liczba jest
  większa, więc wniosek stoi mocniej.

- **Siatka A4 (2026-09-02).** 210 × 297 mm, 6 kolumn, moduł `25 mm`, gutter
  `4 mm`, marginesy `18 / 20 / 28 / 20 mm`, pole treści `170 × 251 mm`.
  Moduł `32 mm` z kanwy foundera był niemożliwy geometrycznie
  (`6 × 32 + 5 × 4 = 212 mm` na stronie o szerokości `210 mm`). Marginesy
  boczne wyrównane z `18/22` na `20/20` 2026-09-03: asymetria nie miała
  uzasadnienia, bo dokumenty IRIN nie są bindowane.

- **Poziom H3 (2026-09-02).** Manrope 600 / 16 px / interlinia 1,3, czyli
  stopień leadu z podniesioną wagą. Kanwa nie definiowała tego poziomu.
  Konsekwencja: H3 odróżnia się od leadu wyłącznie wagą, więc te dwa poziomy
  nie stoją bezpośrednio obok siebie; rozdziela je kicker.

- **Podłoga składu 8,5 px (2026-09-09, strona projektowa).** Jedenasty poziom
  skali. W repozytorium zapisywana jako **`6,38 pt`** (rachunek:
  `8,5 × 72/96 = 6,375`), bo obowiązuje zapis dwumiejscowy. Strona projektowa
  zapisuje `6,4 pt` - ta sama liczba do jednego miejsca.

- **Konwencja pomiaru znaku (2026-09-09, strona projektowa).** Każdy wymiar
  znaku jest szerokością obwiedni znaku widocznego, nie pola pliku.
  Współczynniki zmierzone w Chromium i potwierdzone w tej sesji: `0,655`
  dla wariantu poziomego, `0,561` dla pionowego i sygnetu.

- **Logotyp - komplet zasad (2026-09-02).** Minimalny rozmiar `18 mm` druk
  i `90 px` ekran, przestrzeń ochronna `x = wysokość liter sygnetu`, cztery
  zakazy modyfikacji: koloru, obracania i odbijania, cienia i obrysu,
  nieproporcjonalnego rozciągania. Nadal niepotwierdzone: minimalny rozmiar
  samodzielnego sygnetu (`10 mm`).

- **Tryb monochromatyczny - odrzucony (2026-09-02).** Founder wybrał jedną
  paletę na wszystko. Skutek: obowiązkowa etykieta słowna albo ikona przy
  każdym statusie jest jedynym zabezpieczeniem czytelności w druku mono.
  W Regalii ta reguła jest mocniejsza, bo paleta w ogóle nie ma tokenów stanu.

- **Dane rejestrowe i forma prawna (2026-09-02).** Instytut Rozwoju i Nauki
  sp. z o.o., siedziba w Kielcach, KRS `0001032499`, NIP `9592061542`
  (ciągiem), REGON `525113640`, kapitał zakładowy `40 000,00 zł`, Sąd
  Rejonowy w Kielcach, X Wydział Gospodarczy KRS. Zostają w publicznym
  repozytorium i są wpisywane wprost. Dane kontaktowe nie mają potwierdzonej
  wartości i stoją jako placeholdery. Napis „Warszawa" z kanwy nie obowiązuje.

- **Konwencja papieru firmowego i wizytówki (2026-09-02).** Papier zawiera
  e-mail, telefon i adres strony; wizytówka `85 × 55 mm`, awers i rewers.

- **Zakaz znaków Funduszy Europejskich (2026-09-03).** Na materiale IRIN nie
  stoi znak FE, znak barw RP ani flaga UE. IRIN jest doradcą zewnętrznym,
  nie beneficjentem. Podstawa: Podręcznik informacji i promocji FE,
  rozdz. 8.7, s. 22. Nazwę programu wolno napisać słowem.

- **Trzy linie biznesowe.** Aplikacje dla przedstawicieli handlowych to
  narzędzie wewnętrzne IRIN (CRM dla własnych handlowców), nie produkt na
  sprzedaż. Usługi pożyczkowe UE/BGK to pośrednictwo B2B dla MŚP. Portal
  sprzedaży szkoleń online to model hybrydowy: sprzedaje miejsca i pozwala
  realizować zdalnie, bez pełnej platformy LMS.

- **Wariant zamknięcia projektu: B (2026-09-02).** Repozytorium plus jeden
  dokument pilotażowy przeprowadzony przez Claude Design.

- **Porządek w PR-ach (2026-09-02).** PR #4 scalony, PR #6 zamknięty jako
  zastąpiony przez PR #5.

## Zastąpione, zostają jako historia

- **Paleta v2 „Kaszmir Wyciszony" (2026-09-02).** 14 kolorów, wariant 2
  z siedmiu. Powód wyboru: usuwała trzy zmierzone defekty poprzedniej palety
  (odnośnik i błąd w tym samym kolorze, `info` nieodróżnialny od tekstu
  korpusu, obramowanie w pełnym tuszu). **Zastąpiona przez Regalię
  2026-09-09.** Wartości w `POMIAR.md` rozdz. 3.4 i w historii gita.
- **Paleta 12-kolorowa (2026-09-02, rano).** Zastąpiona tego samego dnia
  przez v2.
- **Palety v3, v4, v4.1, v5, v5.1 (2026-09-03).** Powstały i żyją wyłącznie
  po stronie projektowej; repozytorium ich nigdy nie znało. Archiwum:
  `_archiwum/iteracje-palety/` w starym projekcie.

## Kolejka zadań 1-23 z poprzedniej wersji

Zadania 1-21 zrealizowane. Zadanie 22 (pilot papieru firmowego) **unieważnione
w części dotyczącej barw**: pilot powstał na palecie v2 i sześć jego pomiarów
mierzyłoby wartości, których już nie ma. Cztery z sześciu pomiarów zostały
w tym czasie wykonane po stronie projektowej i wchodzą do warstwy 1 razem
z Regalią - podłoga składu, konwencja obwiedni znaku, limit akcentu od
`426,70 cm2`, zapis NIP ciągiem. Dwa zostają otwarte i wymagają papieru:
grubości linii i minimum sygnetu. Zadanie 23 (domknięcie, tag `v1.0`)
zastąpione weryfikacją tego planu.
