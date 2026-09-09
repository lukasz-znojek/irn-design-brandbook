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
    ("kosc-sloniowa", "bursztyn-wyciszony", "tekst", "etykieta na wypełnieniu obszaru; najciaśniejsza z czterech barw gniazda"),
    ("muszla-rozana", "rubin-gleboki", "tekst", "etykieta na wypełnieniu"),
    ("atrament", "zloto-szampanskie", "tekst", "etykieta na wypełnieniu złotym"),
    ("zloto-szampanskie", "aksamit-nocy", "tekst", "kicker na tle ciemnym"),
    ("lapis-stonowany", "kosc-sloniowa", "tekst", "odnośniki i stan aktywny"),
    ("lapis-stonowany", "alabaster", "tekst", "odnośnik na karcie"),
    ("grafit-jedwabny", "kosc-sloniowa", "tekst", "tekst drugi na jasnym"),
    ("zloto-antyczne", "kosc-sloniowa", "tekst", "podpowiedzi, metadane"),
    ("bursztyn-wyciszony", "kosc-sloniowa", "tekst", "jedyne dopuszczone tło Bursztynu"),
    ("grafit-jedwabny", "kosc-sloniowa", "grafika", "linia struktury od 0,25 mm"),
    ("lapis-stonowany", "muszla-rozana", "tekst", "odnośnik w cytacie albo wyróżnieniu"),
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
    # Muszla Różana i Alabaster pełnią rolę tła (cytaty, wyróżnienia, karty),
    # a nie były sprawdzane wobec trzech barw tekstu drugiego. Dopisane 2026-09-09.
    ("grafit-jedwabny", "muszla-rozana", "tekst",
     "w cytacie tekst drugi idzie Atramentem albo Lapisem Stonowanym"),
    ("zloto-antyczne", "muszla-rozana", "tekst",
     "w cytacie metadane idą Atramentem albo Lapisem Stonowanym"),
    ("bursztyn-wyciszony", "muszla-rozana", "tekst",
     "Bursztyn ma jedno dopuszczone tło: Kość Słoniowa"),
    ("zloto-antyczne", "alabaster", "tekst",
     "na karcie metadane idą Grafitem Jedwabnym"),
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
    "logo_irin_pion.svg":   {"viewbox": [184.837, 162.834], "obwiednia": [40.555, 37.761, 103.728, 87.312],
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
    NAZWY_TINTOW = {"szafir": "Szafir", "rubin": "Rubin",
                    "zielen": "Zieleń", "ametyst": "Ametyst"}
    for n in tinty:
        dopuszczone.append(para("atrament", f"tint-{n}", "tekst",
                                f"karta i pas tabeli na tincie {NAZWY_TINTOW[n]} 12 %"))
        dopuszczone.append(para("lapis-stonowany", f"tint-{n}", "tekst",
                                f"odnośnik na karcie na tincie {NAZWY_TINTOW[n]} 12 %"))
        dopuszczone.append(para("szafir-nocny", f"tint-{n}", "tekst",
                                f"nagłówek karty na tincie {NAZWY_TINTOW[n]} 12 %"))
    zabronione = [para(a, b, r, "para zabroniona", z) for a, b, r, z in ZABRONIONE]
    # Tint jest tłem karty i pasa tabeli, więc trzy barwy tekstu drugiego muszą
    # mieć wobec niego wiersz. Wszystkie trzy są pod progiem 4,5. Dopisane 2026-09-09.
    for n in tinty:
        zabronione.append(para("grafit-jedwabny", f"tint-{n}", "tekst", "para zabroniona",
                               "na tincie tekst drugi idzie Atramentem albo Lapisem Stonowanym"))
        zabronione.append(para("zloto-antyczne", f"tint-{n}", "tekst", "para zabroniona",
                               "na tincie metadane idą Atramentem albo Lapisem Stonowanym"))
        zabronione.append(para("bursztyn-wyciszony", f"tint-{n}", "tekst", "para zabroniona",
                               "Bursztyn ma jedno dopuszczone tło: Kość Słoniowa"))

    # Stopnie serii wykresu: jedna barwa, cztery krycia, komponowane z tłem,
    # bo wypełnienie w arkuszu i w druku jest kryjące. Dopisane 2026-09-09,
    # bo arkusz z pięcioma wykresami leżał w repozytorium bez reguły w warstwie 1.
    KRYCIA_SERII = [1.0, 0.72, 0.50, 0.30]
    TLO_SERII = "kosc-sloniowa"
    OBRYS_SERII = "atrament"
    serie = {}
    for k in ("szafir-nocny", "rubin-gleboki", "zielen-butelkowa", "bursztyn-wyciszony"):
        stopnie = {}
        for kr in KRYCIA_SERII:
            h = mieszaj(hexy[k], hexy[TLO_SERII], kr)
            do_tla = kontrast(h, hexy[TLO_SERII])
            stopnie[f"{int(kr * 100)}"] = {
                "hex": h,
                "do-tla": do_tla,
                "nad-progiem-grafiki": do_tla >= 3.0,
                "obrys-na-wypelnieniu": kontrast(hexy[OBRYS_SERII], h),
                "grafit-na-wypelnieniu": kontrast(hexy["grafit-jedwabny"], h),
            }
        serie[k] = stopnie

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
        "rachunek-szerokosci": f"{SIATKA['kolumny']} × {SIATKA['modul-mm']} + "
                               f"{SIATKA['kolumny']-1} × {SIATKA['gutter-mm']} = {suma_siatki} mm "
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
            "decyzja-wlasciciela": "2026-09-09: barwy dostępne są DOBIERANE DO MATERIAŁU, nie przypisane "
                                   "do obszarów działalności. Rozstrzyga to sprzeczność między dwiema "
                                   "decyzjami po stronie projektowej i zamyka falsyfikator, który do tej "
                                   "pory stał otwarty.",
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
        "stopnie-serii-wykresu": {
            "tlo-kompozycji": TLO_SERII,
            "krycia": KRYCIA_SERII,
            "obrys": {"barwa": OBRYS_SERII, "grubosc-mm": 0.25},
            "prog-grafiki": 3.0,
            "serie": serie,
            "wyjatek-wykres-liniowy": {
                "serii-najwyzej": 3,
                "krycia": [1.0, 0.72, 0.50],
                "grubosc-linii-mm": 0.5,
                "powod": "linia nie ma wypełnienia, więc obrys nie ma czego obrysować; "
                         "stopień 30 % zostaje ze swoim kontrastem do tła pod progiem",
            },
        },
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
    def nazwa_barwy(klucz):
        # tło bywa tintem, a tinty nie mieszkają w "barwy"
        if klucz in d["barwy"]:
            return d["barwy"][klucz]["nazwa"]
        if klucz.startswith("tint-") and klucz[5:] in d["tinty"]:
            t = d["tinty"][klucz[5:]]
            return f"tint {t.get('nazwa') or d['barwy'][t['podstawa']]['nazwa']} 12 %"
        raise KeyError(f"nieznana barwa w parze zabronionej: {klucz}")

    L += ["/* PARY ZABRONIONE, każda z liczbą i zamiennikiem:"]
    for w in d["kontrasty-zabronione"]:
        L.append(f" *   {nazwa_barwy(w['tekst'])} na "
                 f"{nazwa_barwy(w['tlo'])}: {pl(w['kontrast'])} -> {w['zamiast']}")
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
