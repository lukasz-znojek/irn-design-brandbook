#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mierzy pokrycie polskich diakrytyków w fontach osadzonych w pliku CSS jako data URI.

Użycie:
    python3 pokrycie-diakrytykow.py [sciezka/do/fonts.css]

Domyślnie sprawdza `_robocze/ds-bundle/fonts/fonts.css` (paczka systemu projektowego
wgrywana do Claude Design). Dla każdego bloku `@font-face` dekoduje font z data URI
i sprawdza dwie rzeczy naraz:

1. czy każdy z osiemnastu polskich znaków diakrytyzowanych (ĄĆĘŁŃÓŚŹŻ ąćęłńóśźż)
   ma odwzorowanie w tablicy `cmap`, czyli czy przeglądarka w ogóle znajdzie glif
   w tym foncie, zamiast podstawić znak z innego kroju;
2. czy ten glif ma realne kontury, a nie jest pusty.

Dwie pułapki, na które ten skrypt uważa - obie potrafią dać fałszywy wynik:

- **Podzbiory.** Google Fonts dzieli krój na podzbiory `latin` i `latin-ext`
  z rozłącznymi zakresami `unicode-range`. Ó i ó leżą w Latin-1, więc są
  w podzbiorze `latin`; pozostałe szesnaście znaków jest w `latin-ext`.
  Żaden pojedynczy plik nie ma kompletu i to jest poprawne - przeglądarka
  składa je po `unicode-range`. Dlatego wynik sumuje się w obrębie rodziny,
  a nie liczy osobno dla każdego pliku.
- **Glify złożone.** Ą to zwykle glif złożony z „A" i ogonka, a nie osobny
  rysunek. Zwykły `RecordingPen` zapisuje wtedy operację `addComponent`,
  nie `moveTo`, więc licznik konturów pokazuje zero i można z tego błędnie
  wywnioskować, że glif jest pusty. `DecomposingRecordingPen` rozkłada
  składniki na kontury i daje prawdziwą odpowiedź.

Zależności: `fonttools` i `brotli` (drugie jest potrzebne do rozpakowania woff2).
Skrypt instaluje je sam, jeśli brakuje.

Czego ten pomiar NIE rozstrzyga: jak glif wygląda przy konkretnej wadze - czy
ogonek nie ginie, czy kreska nad ź nie zlewa się z literą. To pytanie o rysunek,
nie o obecność glifu, i odpowiada na nie tylko obejrzenie złożonego tekstu.
"""
import base64
import io
import re
import subprocess
import sys

POLSKIE = "ĄĆĘŁŃÓŚŹŻąćęłńóśźż"
DOMYSLNY_CSS = "_robocze/ds-bundle/fonts/fonts.css"


def upewnij_zaleznosci():
    try:
        from fontTools.ttLib import TTFont  # noqa: F401
        import brotli  # noqa: F401
        return
    except Exception:
        pass
    subprocess.run([sys.executable, "-m", "pip", "install", "--quiet", "fonttools", "brotli"],
                   capture_output=True, text=True)
    try:
        from fontTools.ttLib import TTFont  # noqa: F401
        import brotli  # noqa: F401
    except Exception as e:
        sys.exit("Nie udało się przygotować zależności (fonttools, brotli): %s" % e)


def zmierz(sciezka_css):
    from fontTools.ttLib import TTFont
    from fontTools.pens.recordingPen import DecomposingRecordingPen

    tekst = io.open(sciezka_css, encoding="utf-8").read()
    bloki = re.findall(r"@font-face\s*\{(.*?)\}", tekst, re.S)
    if not bloki:
        sys.exit("W pliku %s nie ma ani jednego bloku @font-face." % sciezka_css)

    rodziny = {}
    for blok in bloki:
        m_rodzina = re.search(r"font-family:\s*'([^']+)'", blok)
        m_dane = re.search(r"base64,([A-Za-z0-9+/=]+)\)", blok)
        if not m_rodzina or not m_dane:
            continue
        rodzina = m_rodzina.group(1)
        m_waga = re.search(r"font-weight:\s*([^;]+);", blok)
        surowe = base64.b64decode(m_dane.group(1))
        font = TTFont(io.BytesIO(surowe))

        cmap = {}
        for tabela in font["cmap"].tables:
            cmap.update(tabela.cmap)
        zestaw_glifow = font.getGlyphSet()

        wpis = rodziny.setdefault(rodzina, {
            "waga_css": m_waga.group(1).strip() if m_waga else "?",
            "osie": [],
            "znaki": {},
            "plikow": 0,
            "bajtow": 0,
        })
        wpis["plikow"] += 1
        wpis["bajtow"] += len(surowe)
        if "fvar" in font and not wpis["osie"]:
            wpis["osie"] = [(o.axisTag, o.minValue, o.maxValue) for o in font["fvar"].axes]

        for znak in POLSKIE:
            nazwa = cmap.get(ord(znak))
            if not nazwa:
                continue
            pioro = DecomposingRecordingPen(zestaw_glifow)
            zestaw_glifow[nazwa].draw(pioro)
            kontury = sum(1 for operacja, _ in pioro.value if operacja == "moveTo")
            wpis["znaki"][znak] = (nazwa, kontury)

    return rodziny


def main():
    upewnij_zaleznosci()
    sciezka = sys.argv[1] if len(sys.argv) > 1 else DOMYSLNY_CSS
    rodziny = zmierz(sciezka)

    print("Plik: %s" % sciezka)
    wszystko_ok = True
    for rodzina, w in sorted(rodziny.items()):
        brakujace = [z for z in POLSKIE if z not in w["znaki"]]
        puste = [z for z, (_, k) in w["znaki"].items() if k == 0]
        if brakujace or puste:
            wszystko_ok = False
        print("\n%s" % rodzina)
        print("  plików (podzbiorów): %d, razem %d B" % (w["plikow"], w["bajtow"]))
        print("  font-weight w CSS: %s" % w["waga_css"])
        print("  oś zmienności: %s" % (w["osie"] if w["osie"] else "brak - font statyczny"))
        print("  pokrycie: %d/18" % len(w["znaki"]))
        print("  brakujące: %s" % ("".join(brakujace) if brakujace else "brak"))
        print("  puste glify: %s" % ("".join(puste) if puste else "brak"))
    print("\nWynik zbiorczy: %s" % ("komplet 18/18 z konturami w każdej rodzinie"
                                    if wszystko_ok else "SĄ BRAKI - patrz wyżej"))
    return 0 if wszystko_ok else 1


if __name__ == "__main__":
    sys.exit(main())
