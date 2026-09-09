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
