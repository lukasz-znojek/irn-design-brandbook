#!/usr/bin/env python3
"""Generator podglądu i pomiaru kontrastu dla wariantów palety IRIN (v2).

Wejście:  ../tokens/palette-options-v2.json
Wyjście:  ../palette-preview-v2.html            - jeden dokument HTML, 7 wariantów w identycznym układzie
          ../podglad/paleta-wariant-N.svg        - pasek próbek 15 tokenów (renderuje się na GitHubie)
          ../podglad/kontrast-pomiar.md          - pełny pomiar kontrastu WCAG 2.1 dla każdego wariantu
          ../palette-preview-v2.md               - dokument podglądowy (markdown) z paskami próbek
          ../palette-options-v2.md               - tabele kontrastu wstrzykiwane między znaczniki
                                                   <!-- kontrast:start:N --> ... <!-- kontrast:end:N -->
                                                   oraz <!-- tokeny:start:N --> ... <!-- tokeny:end:N -->

Typografia w HTML jest przepisana 1:1 z brandbook.dc.html (§ 04): Manrope 200-800 ładowany
z Google Fonts tym samym adresem, Inconsolata pomocniczo. Skrypt nie zmienia typografii -
jedyną zmienną między sekcjami są tokeny koloru.

Uruchomienie: python3 generuj-podglad-i-kontrast.py
"""
import json, re, html
from pathlib import Path

TU = Path(__file__).resolve().parent
KATALOG = TU.parent
JSON_WEJ = KATALOG / "tokens" / "palette-options-v2.json"
HTML_WYJ = KATALOG / "palette-preview-v2.html"
SVG_KAT = KATALOG / "podglad"
POMIAR_WYJ = SVG_KAT / "kontrast-pomiar.md"
OPCJE_MD = KATALOG / "palette-options-v2.md"
PREVIEW_MD = KATALOG / "palette-preview-v2.md"

# ---------- WCAG 2.1 ----------
def luminancja(h):
    h = h.lstrip("#")
    r, g, b = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)

def kontrast(a, b):
    la, lb = luminancja(a), luminancja(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)

def ocena(k, wymog):
    """wymog: 'normal' (4,5:1), 'duzy' (3:1), 'ui' (3:1, elementy nietekstowe), 'info' (bez progu)."""
    if wymog == "info":
        return "informacyjnie"
    if k >= 7:
        poziom = "AAA"
    elif k >= 4.5:
        poziom = "AA"
    elif k >= 3:
        poziom = "AA tylko duży tekst" if wymog == "normal" else "AA"
    else:
        poziom = "poniżej AA"
    prog = {"normal": 4.5, "duzy": 3.0, "ui": 3.0}[wymog]
    return poziom + (" ⚠" if k < prog else "")

def fmt(k):
    return f"{k:.2f}:1".replace(".", ",")

def tekst_na(tlo, kandydaci):
    """Wybiera kolor tekstu o najwyższym kontraście na danym tle."""
    return max(kandydaci, key=lambda c: kontrast(c, tlo))

def pary(t):
    """Kluczowe pary kolorów: (opis, pierwszy plan, tło, wymóg)."""
    cta_akcent_tekst = tekst_na(t["accent"], [t["background"], t["neutral-dark"]])
    warn_tekst = tekst_na(t["warning"], [t["text-primary"], t["background"]])
    return [
        ("Tekst korpusu (text-primary) na tle strony (background)", t["text-primary"], t["background"], "normal"),
        ("Tekst korpusu (text-primary) na karcie (surface)", t["text-primary"], t["surface"], "normal"),
        ("Tekst pomocniczy (text-secondary) na tle strony", t["text-secondary"], t["background"], "normal"),
        ("Tekst pomocniczy (text-secondary) na karcie (surface)", t["text-secondary"], t["surface"], "normal"),
        ("Link (link) na tle strony", t["link"], t["background"], "normal"),
        ("Link (link) na karcie (surface)", t["link"], t["surface"], "normal"),
        ("Nagłówek H1 (primary) na karcie - duży tekst", t["primary"], t["surface"], "duzy"),
        ("Nagłówek H2 (secondary) na karcie - duży tekst", t["secondary"], t["surface"], "duzy"),
        ("Nagłówek H3 / kicker (accent) na karcie - mały tekst wersalikowy", t["accent"], t["surface"], "normal"),
        ("CTA podstawowe: tekst w kolorze background na primary", t["background"], t["primary"], "normal"),
        (f"CTA akcentowe: tekst {cta_akcent_tekst} na accent", cta_akcent_tekst, t["accent"], "normal"),
        ("Info jako tekst na karcie", t["info"], t["surface"], "normal"),
        ("Success jako tekst na karcie", t["success"], t["surface"], "normal"),
        ("Warning jako tekst na karcie", t["warning"], t["surface"], "normal"),
        (f"Etykieta warning: tekst {warn_tekst} na warning", warn_tekst, t["warning"], "normal"),
        ("Error jako tekst na karcie", t["error"], t["surface"], "normal"),
        ("Etykieta success: tekst background na success", t["background"], t["success"], "normal"),
        ("Etykieta error: tekst background na error", t["background"], t["error"], "normal"),
        ("Etykieta info: tekst background na info", t["background"], t["info"], "normal"),
        ("Pas tytułowy: neutral-light na neutral-dark", t["neutral-light"], t["neutral-dark"], "normal"),
        ("Linia (border) na tle strony - element nietekstowy", t["border"], t["background"], "ui"),
        ("Rozróżnialność: link względem text-primary", t["link"], t["text-primary"], "info"),
        ("Rozróżnialność: primary względem error (ryzyko zlewania bordo/czerwień)", t["primary"], t["error"], "info"),
    ]

def tabela_kontrastu(w):
    wiersze = ["| Para | Kolory | Kontrast | Ocena WCAG 2.1 |", "|---|---|---|---|"]
    for opis, fg, bg, wymog in pary(w["tokeny"]):
        k = kontrast(fg, bg)
        wiersze.append(f"| {opis} | `{fg}` na `{bg}` | {fmt(k)} | {ocena(k, wymog)} |")
    return "\n".join(wiersze)

def ponizej_aa(w):
    wynik = []
    for opis, fg, bg, wymog in pary(w["tokeny"]):
        if wymog == "info":
            continue
        k = kontrast(fg, bg)
        prog = {"normal": 4.5, "duzy": 3.0, "ui": 3.0}[wymog]
        if k < prog:
            wynik.append((opis, fmt(k)))
    return wynik

# ---------- SVG: pasek próbek ----------
KOLEJNOSC = ["primary", "secondary", "accent", "neutral-dark", "neutral-light", "success", "warning", "error",
             "info", "background", "surface", "border", "text-primary", "text-secondary", "link"]

def svg_pasek(w):
    t = w["tokeny"]
    szer, wys = 100, 150
    czesci = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{szer * 15}" height="{wys}" viewBox="0 0 {szer * 15} {wys}" '
              f'font-family="Manrope, system-ui, -apple-system, Segoe UI, sans-serif">',
              f'<title>Wariant {w["numer"]} - {html.escape(w["nazwa"])}</title>',
              f'<rect width="{szer * 15}" height="{wys}" fill="{t["background"]}"/>']
    for i, nazwa in enumerate(KOLEJNOSC):
        kolor = t[nazwa]
        x = i * szer
        tekst = tekst_na(kolor, ["#111111", "#FFFFFF"])
        czesci.append(f'<rect x="{x}" y="0" width="{szer}" height="{wys}" fill="{kolor}"/>')
        czesci.append(f'<rect x="{x}" y="0" width="{szer}" height="{wys}" fill="none" stroke="{t["border"]}" stroke-width="1"/>')
        czesci.append(f'<text x="{x + 8}" y="{wys - 30}" font-size="10" font-weight="700" fill="{tekst}">{nazwa}</text>')
        czesci.append(f'<text x="{x + 8}" y="{wys - 14}" font-size="10" font-family="Inconsolata, ui-monospace, monospace" fill="{tekst}">{kolor}</text>')
    czesci.append("</svg>")
    return "\n".join(czesci)

# ---------- HTML: podgląd ----------
CSS_WSPOLNY = """
  html, body { margin:0; padding:0; background:#EDEBE6; color:#1E1611; font-family:'Manrope', system-ui, sans-serif; -webkit-font-smoothing:antialiased; }
  .spis { max-width:1000px; margin:0 auto; padding:32px 24px 8px; font-size:13px; line-height:1.6; }
  .spis .kicker { font-weight:700; font-size:10.5px; letter-spacing:0.24em; text-transform:uppercase; color:#5B4837; margin-bottom:10px; }
  .spis a { color:#1E1611; margin-right:16px; }
  .wariant { max-width:1000px; margin:32px auto; padding:24px; background:var(--background); color:var(--text-primary); }
  .wariant a { color:var(--link); text-decoration:underline; text-underline-offset:2px; }
  .wariant a:hover { color:var(--primary); }
  .naglowek-wariantu { display:flex; justify-content:space-between; align-items:baseline; gap:16px; padding:0 0 12px; border-bottom:1px solid var(--neutral-dark); margin-bottom:24px; }
  .naglowek-wariantu .nr { font-weight:800; font-size:52px; line-height:0.95; letter-spacing:-0.02em; font-variant-numeric:tabular-nums; color:var(--primary); }
  .naglowek-wariantu .nazwa { font-weight:600; font-size:24px; line-height:1.1; letter-spacing:-0.01em; }
  .naglowek-wariantu .kierunek { font-weight:400; font-size:13.5px; line-height:1.55; color:var(--text-secondary); max-width:560px; }
  .probki { display:grid; grid-template-columns:repeat(15,1fr); gap:4px; margin-bottom:24px; }
  .probki div { height:64px; padding:6px; display:flex; flex-direction:column; justify-content:flex-end; font-family:'Inconsolata', ui-monospace, monospace; font-size:9px; line-height:1.3; border:1px solid var(--border); overflow:hidden; }
  .probki b { font-family:'Manrope'; font-weight:700; font-size:8.5px; letter-spacing:0.02em; }

  /* Komponenty przepisane z brandbook.dc.html */
  .sekcja { background:var(--surface); border:1px solid var(--neutral-dark); padding:48px; margin-top:16px; }
  .kicker { font-family:'Manrope'; font-weight:700; font-size:10.5px; letter-spacing:0.24em; text-transform:uppercase; color:var(--text-secondary); }
  .pas { background:var(--neutral-dark); color:var(--neutral-light); padding:22px 40px 26px; }
  .pas .siatka { display:grid; grid-template-columns:auto 1fr auto; gap:24px; align-items:center; }
  .pas img { height:20px; width:auto; filter:invert(1) brightness(1.6); }
  .pas .linia { height:1px; background:var(--accent); opacity:0.55; }
  .pas .meta { font-weight:700; font-size:10.5px; letter-spacing:0.26em; text-transform:uppercase; color:var(--accent); }
  .pasy { margin-top:20px; display:grid; grid-template-columns:repeat(5,1fr); gap:10px; height:12px; }
  .okladka { padding:56px 48px 40px; display:grid; grid-template-columns:1.4fr 1fr; gap:56px; }
  .display { font-weight:200; font-size:72px; line-height:0.92; letter-spacing:-0.03em; margin:0; color:var(--primary); }
  .lead { font-weight:500; font-size:16px; line-height:1.4; margin:20px 0 0; color:var(--text-secondary); }
  .okladka .prawa { border-left:1px solid var(--neutral-dark); padding-left:32px; }
  .okladka ol { list-style:none; margin:0; padding:0; font-weight:400; font-size:15px; line-height:1.5; }
  .okladka li { display:grid; grid-template-columns:minmax(130px,auto) 1fr; gap:12px; padding:9px 0; border-bottom:1px solid var(--border); }
  .okladka li span { color:var(--secondary); font-weight:600; }
  .okladka li a { color:var(--text-primary); text-decoration:none; }
  .stopka { padding:12px 28px; border-top:1px solid var(--neutral-dark); display:grid; grid-template-columns:1fr auto; font-size:8.5px; color:var(--text-secondary); }

  h1.h1 { font-weight:300; font-size:40px; line-height:1.0; letter-spacing:-0.02em; margin:0 0 16px; color:var(--primary); }
  h2.h2 { font-weight:600; font-size:24px; line-height:1.1; letter-spacing:-0.01em; margin:28px 0 12px; color:var(--secondary); }
  h3.h3 { font-weight:700; font-size:9.5px; letter-spacing:0.2em; text-transform:uppercase; margin:20px 0 10px; color:var(--accent); }
  p.korpus { font-weight:400; font-size:13.5px; line-height:1.55; margin:0 0 12px; max-width:720px; color:var(--text-primary); }
  p.przypis { font-weight:400; font-size:10px; line-height:1.5; margin:8px 0 0; color:var(--text-secondary); }
  .mono { font-family:'Inconsolata', ui-monospace, monospace; }

  .box { border:1px solid var(--border); border-left:3px solid var(--info); background:var(--background); padding:16px 20px; margin:20px 0; max-width:720px; }
  .box .kicker { color:var(--info); margin-bottom:8px; }
  .box p { font-size:12.5px; line-height:1.55; margin:0; }
  .box.ostrzezenie { border-left-color:var(--warning); }
  .box.ostrzezenie .kicker { color:var(--text-primary); }

  table.tab { width:100%; border-collapse:collapse; font-size:13px; margin:12px 0 4px; }
  table.tab th { text-align:left; padding:8px 10px 8px 0; font-weight:700; font-size:9.5px; letter-spacing:0.2em; text-transform:uppercase; color:var(--secondary); border-bottom:1px solid var(--neutral-dark); }
  table.tab td { padding:9px 10px 9px 0; border-top:1px solid var(--border); vertical-align:top; }
  table.tab tr:nth-child(even) td { background:var(--neutral-light); }
  table.tab td.l { text-align:right; font-family:'Inconsolata', ui-monospace, monospace; font-weight:600; }
  .etykieta { display:inline-block; padding:3px 8px; font-weight:700; font-size:8.5px; letter-spacing:0.14em; text-transform:uppercase; }

  .cta { display:inline-block; padding:12px 20px; font-weight:700; font-size:11px; letter-spacing:0.16em; text-transform:uppercase; text-decoration:none !important; margin:0 10px 10px 0; }
  .cta.podstawowy { background:var(--primary); color:var(--background) !important; }
  .cta.drugi { background:transparent; color:var(--primary) !important; border:1px solid var(--primary); }
  .cta.akcent { background:var(--accent); }

  .compliance { border-top:1px solid var(--neutral-dark); margin-top:32px; padding-top:20px; }
  .compliance ul { margin:8px 0 0; padding-left:0; list-style:none; font-size:12.5px; line-height:1.6; max-width:720px; }
  .compliance li { display:grid; grid-template-columns:1fr auto; gap:12px; padding:6px 0; border-top:1px solid var(--border); }
  .cyfra { font-weight:800; font-size:52px; line-height:0.95; letter-spacing:-0.02em; font-variant-numeric:tabular-nums; color:var(--accent); }
  @media (max-width:760px) { .okladka { grid-template-columns:1fr; } .probki { grid-template-columns:repeat(5,1fr); } .display { font-size:52px; } }
"""

def zmienne(t):
    return " ".join(f"--{k}:{v};" for k, v in t.items())

def sekcja_html(w, logo):
    t = w["tokeny"]
    n = w["numer"]
    cta_akcent_tekst = tekst_na(t["accent"], [t["background"], t["neutral-dark"]])
    warn_tekst = tekst_na(t["warning"], [t["text-primary"], t["background"]])
    ok_tekst = t["background"]
    probki = "".join(
        f'<div style="background:{t[k]}; color:{tekst_na(t[k], ["#111111", "#FFFFFF"])}"><b>{k}</b>{t[k]}</div>' for k in KOLEJNOSC)
    dziedziny = "".join(f"<li><span>{html.escape(k)}</span><span style='color:var(--text-primary); font-weight:400'>{html.escape(v)}</span></li>" for k, v in w["mapowanie_dziedzin"].items())
    return f"""
<article class="wariant" id="wariant-{n}" style="{zmienne(t)}">
  <div class="naglowek-wariantu">
    <div style="display:flex; gap:20px; align-items:baseline;">
      <div class="nr">{n}</div>
      <div><div class="nazwa">{html.escape(w["nazwa"])}</div></div>
    </div>
    <div class="kierunek">{html.escape(w["kierunek"])}</div>
  </div>
  <div class="probki">{probki}</div>

  <!-- 1. Strona tytułowa (komponent okładki z brandbook.dc.html, § 00) -->
  <section class="sekcja" style="padding:0;">
    <div class="pas">
      <div class="siatka">
        <img src="{logo}" alt="IRIN">
        <div class="linia"></div>
        <div class="meta">Brandbook · wariant palety {n}</div>
      </div>
      <div class="pasy">
        <div style="background:var(--accent)"></div><div style="background:var(--accent); opacity:0.3"></div><div style="background:var(--accent)"></div><div style="background:var(--accent); opacity:0.3"></div><div style="background:var(--accent)"></div>
      </div>
    </div>
    <div class="okladka">
      <div>
        <div class="kicker" style="margin-bottom:20px;">Instytut Rozwoju i Nauki · księga marki</div>
        <h1 class="display">Brandbook.</h1>
        <div class="lead">Manrope × siatka sześciokolumnowa × paleta „{html.escape(w["nazwa"].split(" (")[0])}” - jeden system dla trzech dziedzin.</div>
        <div style="margin-top:32px; height:1px; background:var(--neutral-dark);"></div>
        <p class="korpus" style="margin-top:20px;">Ta strona pokazuje wariant {n} palety na identycznym układzie co pozostałe sześć. Typografia, siatka i komponenty są wspólne - jedyną zmienną jest kolor i jego zastosowanie.</p>
      </div>
      <div class="prawa">
        <div class="kicker" style="margin-bottom:16px;">§ Mapowanie dziedzin (propozycja)</div>
        <ol>{dziedziny}</ol>
      </div>
    </div>
    <div class="stopka"><div>Instytut Rozwoju i Nauki</div><div>podgląd palety v2 · wariant {n}</div></div>
  </section>

  <!-- 2. Hierarchia nagłówków (skala z brandbook.dc.html, § 04) -->
  <section class="sekcja">
    <div class="kicker" style="margin-bottom:20px; padding-bottom:20px; border-bottom:1px solid var(--neutral-dark);">§ 01 · Hierarchia nagłówków i akapit</div>
    <h1 class="h1">Nagłówek H1 - rozdział dokumentu</h1>
    <h2 class="h2">Nagłówek H2 - sekcja</h2>
    <h3 class="h3">Nagłówek H3 · drogowskaz sekcji</h3>
    <p class="korpus">IRIN mówi z pozycji doradcy biznesowego, nie urzędu i nie startupu. Ten sam dokument czyta dział HR korporacji, zarząd firmy i pracownik operatora dotacji, bez zmiany rejestru. Pedagogika, Akademia AI i Pożyczki UE/BGK są rozróżniane kolorem dziedziny, struktura i krój pozostają identyczne. Więcej: <a href="#wariant-{n}">karta usługi w Bazie Usług Rozwojowych</a>.</p>
    <p class="przypis">Przypis i metadane: Manrope Regular 10 pt, kolor text-secondary. Kod usługi <span class="mono">2026/00000/PPUR</span> [do potwierdzenia].</p>

    <!-- 3. Box informacyjny -->
    <div class="box">
      <div class="kicker">Informacja</div>
      <p>Szkolenie może być dofinansowane ze środków Krajowego Funduszu Szkoleniowego (KFS) lub przez Bazę Usług Rozwojowych (BUR). Wysokość dofinansowania zależy od wielkości firmy i regulaminu operatora - patrz <a href="#wariant-{n}">01-baza-wiedzy/prawo/kfs.md</a>.</p>
    </div>

    <!-- 4. Tabela -->
    <h2 class="h2">Tabela - program i rozliczenie</h2>
    <table class="tab">
      <thead><tr><th>Moduł szkolenia</th><th>Forma</th><th style="text-align:right">Godziny</th><th>Status</th></tr></thead>
      <tbody>
        <tr><td>Diagnoza potrzeb rozwojowych</td><td>warsztat</td><td class="l">8</td><td><span class="etykieta" style="background:var(--success); color:{ok_tekst}">potwierdzone</span></td></tr>
        <tr><td>Wniosek KFS i dokumentacja</td><td>ćwiczenia</td><td class="l">6</td><td><span class="etykieta" style="background:var(--warning); color:{warn_tekst}">do potwierdzenia</span></td></tr>
        <tr><td>Walidacja efektów uczenia się</td><td>test</td><td class="l">2</td><td><span class="etykieta" style="background:var(--error); color:{ok_tekst}">brak danych</span></td></tr>
        <tr><td>Konsultacja poszkoleniowa</td><td>zdalnie</td><td class="l">2</td><td><span class="etykieta" style="background:var(--info); color:{ok_tekst}">informacja</span></td></tr>
      </tbody>
    </table>
    <p class="przypis">Wiersze naprzemienne: neutral-light. Linie: border. Nagłówki kolumn: secondary, styl drogowskazu (700, wersaliki, tracking 0,2 em).</p>

    <!-- 5. CTA i link -->
    <h2 class="h2">Przycisk / CTA i link</h2>
    <div style="margin:12px 0 4px;">
      <a class="cta podstawowy" href="#wariant-{n}">Zapisz się na szkolenie</a>
      <a class="cta drugi" href="#wariant-{n}">Pobierz program</a>
      <a class="cta akcent" href="#wariant-{n}" style="color:{cta_akcent_tekst} !important">Sprawdź dofinansowanie</a>
    </div>
    <p class="korpus">Link w tekście: <a href="#wariant-{n}">regulamin Bazy Usług Rozwojowych</a> oraz <a href="#wariant-{n}">limity KFS na rok bieżący</a>. Podkreślenie z odsunięciem 2 px jak w brandbook.dc.html; kolor: link, po najechaniu: primary.</p>
    <div style="display:flex; gap:32px; align-items:baseline; margin-top:16px;">
      <div><div class="cyfra">3 128</div><div class="przypis">liczba prowadząca · Manrope 800 · accent</div></div>
      <div><div class="cyfra" style="color:var(--primary)">80%</div><div class="przypis">liczba prowadząca · primary</div></div>
    </div>

    <!-- 6. Sekcja prawo / compliance -->
    <div class="compliance">
      <div class="kicker" style="margin-bottom:8px;">§ 02 · Prawo i zgodność - elementy obowiązkowe zaświadczenia</div>
      <h2 class="h2" style="margin-top:8px;">Wymogi formalne wobec PUP i BUR</h2>
      <p class="korpus">Lista pól wynika z karty specyfikacji <a href="#wariant-{n}">02-szablony-dokumentow/certyfikat.md</a>. Status każdego pola pokazuje, jak paleta oznacza stan potwierdzony, do potwierdzenia i brak danych.</p>
      <ul>
        <li><span>Identyfikacja uczestnika, szkolenia, realizatora (IRIN) i liczby godzin - wymóg rozliczeniowy wobec PUP (ścieżka KFS)</span><span class="etykieta" style="background:var(--success); color:{ok_tekst}">potwierdzone</span></li>
        <li><span>Osiągnięte efekty uczenia się - wymóg BUR</span><span class="etykieta" style="background:var(--success); color:{ok_tekst}">potwierdzone</span></li>
        <li><span>Kod usługi BUR w formie zgodnej z rejestracją</span><span class="etykieta" style="background:var(--warning); color:{warn_tekst}">do potwierdzenia</span></li>
        <li><span>Komplet pól wzoru z Załącznika nr 12 do Regulaminu BUR - treść wzoru nie została odczytana</span><span class="etykieta" style="background:var(--error); color:{ok_tekst}">brak danych</span></li>
      </ul>
      <div class="box ostrzezenie">
        <div class="kicker">Zastrzeżenie</div>
        <p>Oficjalny wzór zaświadczenia BUR istnieje, ale jego treści nie udało się pobrać w sesji, w której powstała baza wiedzy. Zanim karta specyfikacji zostanie uznana za zamkniętą, należy odczytać załącznik wprost.</p>
      </div>
      <p class="przypis mono">Podstawa: ustawa o promocji zatrudnienia i instytucjach rynku pracy (KFS) · Regulamin BUR (PARP) · dane rejestrowe realizatora [do potwierdzenia]</p>
    </div>
  </section>
</article>
"""

def html_podglad(dane, logo="../../logo_irin_poziom.svg"):
    spis = " ".join(f'<a href="#wariant-{w["numer"]}">{w["numer"]} · {html.escape(w["nazwa"].split(" (")[0])}</a>' for w in dane["warianty"])
    sekcje = "".join(sekcja_html(w, logo) for w in dane["warianty"])
    return f"""<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>IRIN - podgląd wariantów palety v2</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@200..800&family=Inconsolata:wght@300..700&display=swap" rel="stylesheet">
<style>{CSS_WSPOLNY}</style>
</head>
<body>
<div class="spis">
  <div class="kicker">IRIN · podgląd 7 wariantów palety v2 · typografia bez zmian (Manrope 200-800, Inconsolata)</div>
  <div>{spis}</div>
  <div style="margin-top:8px; font-size:11px; color:#5B4837;">Wygenerowano z <span style="font-family:'Inconsolata', monospace">tokens/palette-options-v2.json</span>. Status: propozycja do wyboru, żaden wariant nie jest finalny. Krój ładuje się z Google Fonts - bez połączenia z internetem zobaczysz krój zastępczy.</div>
</div>
{sekcje}
</body>
</html>
"""

# ---------- Podgląd (markdown) ----------
ELEMENTY = [
    ("Strona tytułowa - pas górny", "neutral-dark (tło), neutral-light (tekst), accent (linia i pasy)", "Manrope 700 · 10,5 px · wersaliki · tracking 0,26 em"),
    ("Strona tytułowa - tytuł display", "primary", "Manrope 200 · 72 px · interlinia 0,92 · tracking -0,03 em"),
    ("Strona tytułowa - lead", "text-secondary", "Manrope 500 · 16 px · interlinia 1,4"),
    ("Nagłówek H1", "primary", "Manrope 300 · 40 px · interlinia 1,0 · tracking -0,02 em"),
    ("Nagłówek H2", "secondary", "Manrope 600 · 24 px · interlinia 1,1 · tracking -0,01 em"),
    ("Nagłówek H3 (drogowskaz)", "accent", "Manrope 700 · 9,5 px · wersaliki · tracking 0,2 em"),
    ("Akapit korpusu", "text-primary na surface", "Manrope 400 · 13,5 px · interlinia 1,55"),
    ("Przypis / metadane", "text-secondary; kody w Inconsolata", "Manrope 400 · 10 px · interlinia 1,5"),
    ("Box informacyjny", "border (ramka), info (lewa krawędź 3 px i tytuł), background (tło)", "tytuł: drogowskaz 700; treść: Manrope 400 · 12,5 px"),
    ("Tabela - nagłówki kolumn", "secondary; linia dolna neutral-dark", "Manrope 700 · 9,5 px · wersaliki · tracking 0,2 em"),
    ("Tabela - wiersze", "text-primary; linie border; wiersze parzyste neutral-light; liczby w Inconsolata 600", "Manrope 400 · 13 px"),
    ("Tabela - etykiety stanu", "success / warning / error / info (tło) z tekstem o najwyższym kontraście", "Manrope 700 · 8,5 px · wersaliki · tracking 0,14 em"),
    ("CTA podstawowe", "primary (tło), background (tekst)", "Manrope 700 · 11 px · wersaliki · tracking 0,16 em"),
    ("CTA drugie", "primary (obrys i tekst), bez tła", "jak wyżej"),
    ("CTA akcentowe", "accent (tło), tekst background albo neutral-dark - wybór wg kontrastu", "jak wyżej"),
    ("Link w tekście", "link; po najechaniu primary; podkreślenie z odsunięciem 2 px", "dziedziczy z akapitu"),
    ("Liczba prowadząca", "accent / primary", "Manrope 800 · 52 px · tabular · tracking -0,02 em"),
    ("Sekcja prawo / compliance", "neutral-dark (linia górna), etykiety stanu, box ostrzegawczy z krawędzią warning", "H2 600 · 24 px; lista 400 · 12,5 px; podstawa prawna Inconsolata 10 px"),
]

def preview_md(dane):
    cz = ["# Podgląd wariantów palety v2 - jeden układ, siedem kolorystyk",
          "",
          "**Status: propozycja do wyboru przez foundera. Żaden wariant nie jest finalny; obowiązująca paleta w `03-pakiet-claude-design/format-paczki.md` pozostaje bez zmian do decyzji.**",
          "",
          "Ten plik jest generowany skryptem `narzedzia/generuj-podglad-i-kontrast.py` z `tokens/palette-options-v2.json`. Pełna specyfikacja, kontrasty i trade-offs: [`palette-options-v2.md`](./palette-options-v2.md).",
          "",
          "## Jak obejrzeć podgląd z prawdziwą typografią",
          "",
          "Właściwy podgląd wizualny to plik [`palette-preview-v2.html`](./palette-preview-v2.html): jeden dokument, siedem sekcji o identycznym układzie, różniących się wyłącznie tokenami koloru. Krój Manrope (wagi 200-800) i Inconsolata są ładowane z Google Fonts tym samym adresem, którego używa `brandbook.dc.html`, więc do poprawnego renderu potrzebne jest połączenie z internetem. GitHub nie renderuje plików HTML w podglądzie repozytorium - pobierz gałąź i otwórz plik lokalnie w przeglądarce (logotyp wczytuje się z korzenia repozytorium ścieżką względną).",
          "",
          "Paski próbek poniżej (SVG) renderują się bezpośrednio na GitHubie i pokazują same kolory; etykiety na nich nie są demonstracją typografii.",
          "",
          "## Wspólny układ demonstracyjny",
          "",
          "Każdy wariant pokazuje tę samą sekwencję komponentów, przepisanych z `brandbook.dc.html` (§ 00 okładka, § 04 skala typograficzna, tabele i drogowskazy z § 02-§ 06):",
          "",
          "1. strona tytułowa (pas górny z logotypem, pasy akcentu, tytuł display, lead, mapowanie dziedzin),",
          "2. hierarchia nagłówków H1 / H2 / H3,",
          "3. akapit korpusu z przypisem,",
          "4. box informacyjny,",
          "5. tabela z etykietami stanu,",
          "6. przyciski CTA (podstawowy, drugi, akcentowy),",
          "7. link w tekście i liczby prowadzące,",
          "8. sekcja „prawo / compliance” z listą elementów obowiązkowych zaświadczenia (treść z `02-szablony-dokumentow/certyfikat.md`) i boxem ostrzegawczym.",
          "",
          "Typografia jest identyczna we wszystkich siedmiu sekcjach i nie była przedmiotem zmian - tabela poniżej podaje ją raz, a przy każdym wariancie zmienia się tylko kolumna z kolorem.",
          "",
          "| Element układu | Token koloru | Typografia (bez zmian, z brandbook.dc.html) |",
          "|---|---|---|"]
    for el, tok, typ in ELEMENTY:
        cz.append(f"| {el} | {tok} | {typ} |")
    cz.append("")
    for w in dane["warianty"]:
        t = w["tokeny"]
        n = w["numer"]
        cz += [f"## Wariant {n} - {w['nazwa']}", "",
               f"![Wariant {n} - pasek 15 tokenów](./podglad/paleta-wariant-{n}.svg)", "",
               w["kierunek"], "",
               f"Sekcja w podglądzie HTML: `palette-preview-v2.html#wariant-{n}`.", "",
               "| Element układu | Kolor w tym wariancie |", "|---|---|",
               f"| Strona tytułowa: pas górny / tekst pasa / pasy akcentu | `{t['neutral-dark']}` / `{t['neutral-light']}` / `{t['accent']}` |",
               f"| Tytuł display i H1 | `{t['primary']}` |",
               f"| Lead i przypisy (text-secondary) | `{t['text-secondary']}` |",
               f"| H2 i nagłówki kolumn tabeli (secondary) | `{t['secondary']}` |",
               f"| H3 drogowskaz, liczba prowadząca, CTA akcentowe (accent) | `{t['accent']}` (tekst CTA: `{tekst_na(t['accent'], [t['background'], t['neutral-dark']])}`) |",
               f"| Akapit (text-primary) na karcie (surface) na tle strony (background) | `{t['text-primary']}` na `{t['surface']}` na `{t['background']}` |",
               f"| Box informacyjny: krawędź i tytuł (info), ramka (border) | `{t['info']}`, `{t['border']}` |",
               f"| Tabela: linie (border), wiersze parzyste (neutral-light) | `{t['border']}`, `{t['neutral-light']}` |",
               f"| Etykiety stanu: success / warning / error / info | `{t['success']}` / `{t['warning']}` (tekst `{tekst_na(t['warning'], [t['text-primary'], t['background']])}`) / `{t['error']}` / `{t['info']}` |",
               f"| CTA podstawowe: tło / tekst | `{t['primary']}` / `{t['background']}` |",
               f"| Link (po najechaniu: primary) | `{t['link']}` |",
               ""]
        cz.append("Mapowanie dziedzin (propozycja, poza 15 tokenami): " + "; ".join(f"{k} - {v}" for k, v in w["mapowanie_dziedzin"].items()) + ".")
        cz.append("")
    return "\n".join(cz)

# ---------- Pomiar (markdown) ----------
def pomiar_md(dane):
    czesci = ["# Pomiar kontrastu WCAG 2.1 - warianty palety v2",
              "",
              "Plik generowany skryptem `../narzedzia/generuj-podglad-i-kontrast.py` z `../tokens/palette-options-v2.json`. "
              "Kontrast liczony wzorem na luminancję względną sRGB (WCAG 2.1), nie przepisany z żadnego źródła. "
              "Progi: AA tekst normalny 4,5:1, AA duży tekst 3:1, AAA 7:1, elementy nietekstowe 3:1. Znak ⚠ oznacza wynik poniżej progu wymaganego dla danej pary.",
              ""]
    for w in dane["warianty"]:
        czesci.append(f"## Wariant {w['numer']} - {w['nazwa']}")
        czesci.append("")
        czesci.append(tabela_kontrastu(w))
        czesci.append("")
        p = ponizej_aa(w)
        if p:
            czesci.append("**Poniżej progu:** " + "; ".join(f"{o} ({k})" for o, k in p) + ".")
        else:
            czesci.append("**Poniżej progu:** brak.")
        czesci.append("")
    return "\n".join(czesci)

ROLE_TOKENOW = {
    "primary": "H1, tytuł display, CTA podstawowe, pas dziedzinowy",
    "secondary": "H2, nagłówki kolumn tabel, numeracja",
    "accent": "H3 drogowskaz, liczby prowadzące, CTA akcentowe, pasy na okładce",
    "neutral-dark": "pas tytułowy, stopka odwrócona, linie główne",
    "neutral-light": "wiersze parzyste tabel, tła wtórne",
    "success": "etykieta „potwierdzone”",
    "warning": "etykieta „do potwierdzenia”, krawędź boxu ostrzegawczego (tylko tło / linia, nie tekst)",
    "error": "etykieta „brak danych”, komunikat błędu",
    "info": "box informacyjny, etykieta neutralna",
    "background": "tło strony",
    "surface": "tło karty / sekcji",
    "border": "linie tabel i ramek (hairline dekoracyjny)",
    "text-primary": "korpus, przypisy w tabeli",
    "text-secondary": "lead, przypisy, metadane",
    "link": "odsyłacze, stany aktywne",
}

def tabela_tokenow(w):
    t = w["tokeny"]
    wiersze = ["| Token | Hex | Zastosowanie w podglądzie |", "|---|---|---|"]
    for k in KOLEJNOSC:
        wiersze.append(f"| `{k}` | `{t[k]}` | {ROLE_TOKENOW[k]} |")
    wiersze.append("")
    wiersze.append("Mapowanie dziedzin (propozycja, poza 15 tokenami): " + "; ".join(f"{k} - {v}" for k, v in w["mapowanie_dziedzin"].items()) + ". " + w["poza_tokenami"])
    return "\n".join(wiersze)

def wstrzyknij_do_opcji(dane):
    if not OPCJE_MD.exists():
        return False
    tekst = OPCJE_MD.read_text(encoding="utf-8")
    for w in dane["warianty"]:
        n = w["numer"]
        for znacznik, fn in (("kontrast", tabela_kontrastu), ("tokeny", tabela_tokenow)):
            wzor = re.compile(rf"(<!-- {znacznik}:start:{n} -->)(.*?)(<!-- {znacznik}:end:{n} -->)", re.S)
            if wzor.search(tekst):
                tekst = wzor.sub(lambda m, w=w, fn=fn: m.group(1) + "\n" + fn(w) + "\n" + m.group(3), tekst)
    OPCJE_MD.write_text(tekst, encoding="utf-8")
    return True

def main():
    dane = json.loads(JSON_WEJ.read_text(encoding="utf-8"))
    assert len(dane["warianty"]) == 7, f"oczekiwano 7 wariantów, jest {len(dane['warianty'])}"
    for w in dane["warianty"]:
        brak = set(KOLEJNOSC) - set(w["tokeny"])
        nadmiar = set(w["tokeny"]) - set(KOLEJNOSC)
        assert not brak and not nadmiar, f"wariant {w['numer']}: brak {brak}, nadmiar {nadmiar}"
        for k, v in w["tokeny"].items():
            assert re.fullmatch(r"#[0-9A-F]{6}", v), f"wariant {w['numer']}: zły hex {k}={v}"
    SVG_KAT.mkdir(exist_ok=True)
    HTML_WYJ.write_text(html_podglad(dane), encoding="utf-8")
    for w in dane["warianty"]:
        (SVG_KAT / f"paleta-wariant-{w['numer']}.svg").write_text(svg_pasek(w), encoding="utf-8")
    POMIAR_WYJ.write_text(pomiar_md(dane), encoding="utf-8")
    PREVIEW_MD.write_text(preview_md(dane), encoding="utf-8")
    wstrzyknieto = wstrzyknij_do_opcji(dane)
    print(f"OK: {HTML_WYJ.name}, 7 × SVG, {POMIAR_WYJ.name}, tabele w palette-options-v2.md: {'tak' if wstrzyknieto else 'plik jeszcze nie istnieje'}")
    for w in dane["warianty"]:
        p = ponizej_aa(w)
        print(f"  wariant {w['numer']}: poniżej progu {len(p)}" + (": " + "; ".join(o for o, _ in p) if p else ""))

if __name__ == "__main__":
    main()
