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
    # stopnie serii wykresu: hexy komponowane z tłem i ich dwa kontrasty
    for seria in d.get("stopnie-serii-wykresu", {}).get("serie", {}).values():
        for st in seria.values():
            hexy.add(st["hex"].upper())
            liczby |= {f"{st['do-tla']:.2f}".replace(".", ","),
                       f"{st['obrys-na-wypelnieniu']:.2f}".replace(".", ","),
                       f"{st['grafit-na-wypelnieniu']:.2f}".replace(".", ",")}

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
