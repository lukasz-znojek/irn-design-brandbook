#!/usr/bin/env python3
"""Wyciąga tekst z pliku PDF, z numerami stron, do porównania cytatu ze źródłem.

Użycie:
    python3 tekst-z-pdf.py sciezka/do/pliku.pdf > tekst.txt
    python3 tekst-z-pdf.py sciezka/do/pliku.pdf 5      # tylko strona 5 (liczona od 1)
    python3 tekst-z-pdf.py sciezka/do/pliku.pdf 5-8    # strony 5-8 (liczone od 1)

Zależność: biblioteka `pypdf`. W tym repozytorium narzędzia typu `poppler`
(`pdftotext`) nie są zainstalowane, a wcześniejszy brief tej sesji zakładał,
że `pip` też jest niedostępny — w praktyce (sesja 2026-09-02, Etap 2) `pip3`
działał, ale `import pypdf` sam z siebie zawodził, bo jego zależność
`cryptography` nie mogła znaleźć `_cffi_backend`. Skrypt instaluje `pypdf`
automatycznie, jeśli import się nie powiedzie, a jeśli to nie wystarczy,
naprawia brakujące `cffi`. Jeśli żadna z tych napraw nie pomoże (np.
środowisko bez dostępu do PyPI), zgłasza to jawnie zamiast cicho pomijać
stronę.

Każdy cytat wzięty z wyniku tego skryptu trzeba porównać z oryginałem PDF
(otwartym wizualnie, np. przez narzędzie Read) przed wpisaniem do repozytorium
— ekstrakcja tekstu z PDF czasem gubi łamanie wierszy, myli kolejność kolumn
w tabelach albo pomija tekst w polach formularza.
"""
import subprocess
import sys


def pip_install(*pakiety):
    return subprocess.run(
        [sys.executable, "-m", "pip", "install", *pakiety],
        capture_output=True, text=True,
    )


def upewnij_pypdf():
    """Importuje pypdf, naprawiając po drodze dwa znane problemy tego środowiska:
    brak pakietu (ImportError) i zepsuty import `cryptography` przez brakujący
    `_cffi_backend` (kończy się `pyo3_runtime.PanicException`, nie ImportError —
    stąd łapiemy tu Exception, nie tylko ImportError).
    """
    try:
        import pypdf  # noqa: F401
        return
    except Exception:
        pass

    print("pypdf niedostępny lub zepsuty — próbuję `pip3 install pypdf`...", file=sys.stderr)
    wynik = pip_install("pypdf")
    if wynik.returncode != 0:
        sys.exit(
            "Nie udało się zainstalować pypdf — pip niedostępny w tym środowisku.\n"
            f"stdout: {wynik.stdout}\nstderr: {wynik.stderr}\n"
            "Odczyt PDF wymaga ręcznego dostarczenia tekstu albo innego środowiska."
        )

    try:
        import pypdf  # noqa: F401
        return
    except Exception as e:
        # Typowy przypadek w tym środowisku: `cryptography` (zależność pypdf)
        # nie może zaimportować `_cffi_backend`, bo `cffi` brakuje albo jest
        # niespójny z zainstalowanym `cryptography`. Naprawia to reinstalacja `cffi`.
        print(f"Import pypdf nadal zawodzi ({e}) — próbuję `pip3 install --force-reinstall cffi`...", file=sys.stderr)
        wynik = pip_install("--force-reinstall", "cffi")
        if wynik.returncode != 0:
            sys.exit(
                "Naprawa importu pypdf się nie powiodła.\n"
                f"stdout: {wynik.stdout}\nstderr: {wynik.stderr}"
            )

    import pypdf  # noqa: F401  # jeśli i to zawiedzie, niech wyjątek poleci dalej


def zakres_stron(arg, liczba_stron):
    if arg is None:
        return range(liczba_stron)
    if "-" in arg:
        poczatek, koniec = arg.split("-", 1)
        return range(int(poczatek) - 1, int(koniec))
    return range(int(arg) - 1, int(arg))


def main():
    if len(sys.argv) < 2:
        sys.exit("Użycie: python3 tekst-z-pdf.py plik.pdf [numer-strony|zakres-stron]")

    upewnij_pypdf()
    from pypdf import PdfReader

    sciezka = sys.argv[1]
    arg_stron = sys.argv[2] if len(sys.argv) > 2 else None

    reader = PdfReader(sciezka)
    liczba_stron = len(reader.pages)

    for i in zakres_stron(arg_stron, liczba_stron):
        if i < 0 or i >= liczba_stron:
            continue
        tekst = reader.pages[i].extract_text() or "(brak tekstu na tej stronie — może być skan/obraz)"
        print(f"\n===== strona {i + 1} / {liczba_stron} =====")
        print(tekst)


if __name__ == "__main__":
    main()
