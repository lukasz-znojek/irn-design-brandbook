# -*- coding: utf-8 -*-
"""Arkusz wzorcowy IRIN. Kazda barwa i kazda liczba pochodzi z warstwy 1."""
import json, os
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side, Protection
from openpyxl.utils import get_column_letter
from openpyxl.chart import BarChart, LineChart, Reference
from openpyxl.chart.label import DataLabelList
from openpyxl.drawing.line import LineProperties
from openpyxl.chart.shapes import GraphicalProperties
from openpyxl.chart.data_source import AxDataSource, StrRef

TOK = json.load(open(os.environ['TOKENY'], encoding='utf-8'))

# ---- barwy z palety (bez kratki, tak chce openpyxl) -----------------------
def A(h): return 'FF' + h          # Excel chce aRGB; openpyxl dopisuje '00', czyli alfa zero
ATRAMENT   = '07090C'
KOSC       = 'F7F3E9'
ALABASTER  = 'E4E1D8'
GRAFIT     = '606369'
SZAFIR     = '132246'
LAPIS      = '305686'
MUSZLA     = 'E8D6D6'
ZLOTO_SZ   = 'C4B790'

KROJ, MONO = 'Manrope', 'Inconsolata'
PT_KORPUS, PT_META, PT_NAGL, PT_TEMAT = 10, 7.5, 10, 18
WYS_WIERSZA = 15.7          # 10 pt x 1,55 z typografia.md
OBRYS_EMU  = round(0.25/25.4*72*12700)  # 0,25 mm, linia niosaca strukture
GRUB_LINII = round(0.50/25.4*72*12700)  # 0,50 mm, dwukrotnosc minimum

cienka = Side(style='thin', color=A(GRAFIT))
def f(sz=PT_KORPUS, kolor=ATRAMENT, bold=False, mono=False, italic=False):
    return Font(name=MONO if mono else KROJ, size=sz, color=A(kolor), bold=bold, italic=italic)
def tlo(hexs): return PatternFill('solid', fgColor=A(hexs))

wb = Workbook()

# =========================== ARKUSZ 1: TABELA ==============================
ws = wb.active
ws.title = 'Tabela'
ws.sheet_view.showGridLines = False
ws.sheet_properties.tabColor = SZAFIR

ws['B2'] = 'ARKUSZ WZORCOWY'
ws['B2'].font = f(PT_META, SZAFIR, bold=True)
ws['B3'] = '[Tytuł tabeli w jednym zdaniu]'
ws['B3'].font = f(PT_TEMAT, SZAFIR, bold=True)
ws['B4'] = 'Liczby poniżej są wypełnieniem przykładowym, nie danymi IRIN.'
ws['B4'].font = f(PT_META, GRAFIT)
for r in (2,3,4): ws.row_dimensions[r].height = {2:12.6, 3:24, 4:12.6}[r]
ws.row_dimensions[5].height = 12

NAGL = ['Kod', 'Pozycja', 'Okres', 'Wartość netto', 'Stawka', 'Wartość brutto', 'Uwaga']
TYPY = ['kod', 'tekst', 'data', 'wpis', 'wpis', 'formula', 'tekst']
SZER = [12, 30, 12, 15, 9, 16, 26]
R0 = 6
for i, (n, s) in enumerate(zip(NAGL, SZER)):
    c = ws.cell(row=R0, column=2+i, value=n)
    c.font = f(PT_NAGL, KOSC, bold=True)
    c.fill = tlo(SZAFIR)
    c.alignment = Alignment(horizontal='right' if i in (3,4,5) else 'left',
                            vertical='center', wrap_text=False)
    ws.column_dimensions[get_column_letter(2+i)].width = s
ws.row_dimensions[R0].height = 21

WIERSZE = 10
for k in range(WIERSZE):
    r = R0 + 1 + k
    pas = KOSC if k % 2 == 0 else ALABASTER
    ws.row_dimensions[r].height = WYS_WIERSZA
    netto = 1200 + k * 385.5
    ws.cell(row=r, column=2, value=f'IRN-{k+1:03d}').font = f(PT_KORPUS, ATRAMENT, mono=True)
    ws.cell(row=r, column=3, value=f'[pozycja {k+1}]').font = f()
    ws.cell(row=r, column=4, value=f'Okres {k % 4 + 1}').font = f(PT_KORPUS, GRAFIT)
    ws.cell(row=r, column=5, value=netto).font = f()
    ws.cell(row=r, column=6, value=0.23).font = f()
    ws.cell(row=r, column=7, value=f'=E{r}*(1+F{r})').font = f(PT_KORPUS, GRAFIT, italic=True)
    ws.cell(row=r, column=8, value='[uwaga]').font = f(PT_META, GRAFIT)
    for col in range(2, 9):
        c = ws.cell(row=r, column=col)
        c.fill = tlo(MUSZLA if col in (5,6) else pas)
        c.border = Border(bottom=cienka) if k == WIERSZE-1 else Border()
        c.alignment = Alignment(horizontal='right' if col in (5,6,7) else 'left',
                                vertical='center')
        if col in (5,6):                       # pola do wpisania
            c.border = Border(left=Side(style='thin', color=A(LAPIS)),
                              right=Side(style='thin', color=A(LAPIS)),
                              top=c.border.top, bottom=c.border.bottom)
            c.protection = Protection(locked=False)
        else:
            c.protection = Protection(locked=True)
    ws.cell(row=r, column=5).number_format = '#,##0.00'
    ws.cell(row=r, column=6).number_format = '0 %'
    ws.cell(row=r, column=7).number_format = '#,##0.00'

RS = R0 + WIERSZE + 1
ws.row_dimensions[RS].height = WYS_WIERSZA
ws.cell(row=RS, column=3, value='Razem').font = f(bold=True)
ws.cell(row=RS, column=5, value=f'=SUM(E{R0+1}:E{R0+WIERSZE})').font = f(bold=True)
ws.cell(row=RS, column=7, value=f'=SUM(G{R0+1}:G{R0+WIERSZE})').font = f(bold=True)
for col in range(2, 9):
    c = ws.cell(row=RS, column=col)
    c.fill = tlo(ALABASTER)
    c.border = Border(top=Side(style='medium', color=A(GRAFIT)))
    c.alignment = Alignment(horizontal='right' if col in (5,6,7) else 'left', vertical='center')
ws.cell(row=RS, column=5).number_format = '#,##0.00'
ws.cell(row=RS, column=7).number_format = '#,##0.00'

RL = RS + 2
ws.cell(row=RL, column=2, value='RODZAJE PÓL').font = f(PT_META, SZAFIR, bold=True)
LEG = [('do wpisania',  MUSZLA,   'ramka Lapis Stonowany po bokach; komórka odblokowana'),
       ('policzone formułą', None,'kursywa i Grafit Jedwabny; komórka zablokowana'),
       ('stałe, tylko do czytania', None, 'pismo proste Atramentem; komórka zablokowana'),
       ('suma', ALABASTER,        'linia górna Grafitem, pismo pogrubione')]
for i, (n, tl, opis) in enumerate(LEG):
    r = RL + 1 + i
    ws.row_dimensions[r].height = WYS_WIERSZA
    c = ws.cell(row=r, column=2, value=n); c.font = f(PT_META)
    if tl: c.fill = tlo(tl)
    ws.cell(row=r, column=3, value=opis).font = f(PT_META, GRAFIT)
ws.cell(row=RL+len(LEG)+1, column=2,
        value='Kolor nigdy nie jest jedynym nośnikiem: każdy rodzaj pola ma obok koloru '
              'sygnał nie-kolorowy (ramka, kursywa, linia albo brak).').font = f(PT_META, GRAFIT)

ws.freeze_panes = f'A{R0+1}'
ws.print_area = f'A1:I{RL+len(LEG)+2}'
ws.page_setup.orientation = 'landscape'
ws.page_margins.left = ws.page_margins.right = 20/25.4
ws.page_margins.top = 18/25.4
ws.page_margins.bottom = 28/25.4

# =========================== ARKUSZ 2: WYKRESY =============================
wk = wb.create_sheet('Wykresy')
wk.sheet_view.showGridLines = False
wk['B2'] = 'WYKRESY'
wk['B2'].font = f(PT_META, SZAFIR, bold=True)
wk['B3'] = 'Jedna barwa, cztery stopnie krycia'
wk['B3'].font = f(PT_TEMAT, SZAFIR, bold=True)
wk['B4'] = ('Stopnie i obrys z paleta-barw.md, sekcja „Wykresy". Oś Y zawsze od zera, '
            'każda oś podpisana słowem, najwyżej cztery serie.')
wk['B4'].font = f(PT_META, GRAFIT)
wk.row_dimensions[3].height = 24

DR = 6
wk.cell(row=DR, column=2, value='Okres').font = f(PT_NAGL, KOSC, bold=True)
wk.cell(row=DR, column=2).fill = tlo(SZAFIR)
SERIE = ['Seria A', 'Seria B', 'Seria C', 'Seria D']
for i, s in enumerate(SERIE):
    c = wk.cell(row=DR, column=3+i, value=s)
    c.font = f(PT_NAGL, KOSC, bold=True); c.fill = tlo(SZAFIR)
    c.alignment = Alignment(horizontal='right')
DANE = [[120, 96, 74, 48], [145, 110, 85, 52], [138, 128, 91, 61], [172, 141, 103, 70]]
for k, row in enumerate(DANE):
    r = DR + 1 + k
    wk.row_dimensions[r].height = WYS_WIERSZA
    c = wk.cell(row=r, column=2, value=f'Okres {k+1}'); c.font = f()
    c.fill = tlo(KOSC if k % 2 == 0 else ALABASTER)
    for i, v in enumerate(row):
        c = wk.cell(row=r, column=3+i, value=v)
        c.font = f(); c.number_format = '#,##0'
        c.fill = tlo(KOSC if k % 2 == 0 else ALABASTER)
        c.alignment = Alignment(horizontal='right')
wk.column_dimensions['B'].width = 14
for col in 'CDEF': wk.column_dimensions[col].width = 11

ST = TOK['stopnie-serii-wykresu']['serie']['szafir-nocny']
STOPNIE = [ST[k]['hex'].lstrip('#') for k in ('100','72','50','30')]

KAT_REF = None   # ustawiane po zbudowaniu bloku danych

def kategorie_tekstem(ch):
    for s_ in ch.series:
        s_.cat = AxDataSource(strRef=StrRef(f=KAT_REF))

def ubierz(ch, tytul, os_x, os_y):
    ch.title = tytul
    ch.x_axis.title = os_x
    ch.y_axis.title = os_y
    ch.y_axis.scaling.min = 0
    ch.height, ch.width = 8.5, 15.5
    ch.style = None
    for i, s in enumerate(ch.series):
        gp = GraphicalProperties(solidFill=STOPNIE[i % 4])
        gp.line = LineProperties(solidFill=ATRAMENT, w=OBRYS_EMU)
        s.graphicalProperties = gp
    kategorie_tekstem(ch)
    return ch

dane = Reference(wk, min_col=3, max_col=6, min_row=DR, max_row=DR+len(DANE))
kat  = Reference(wk, min_col=2, min_row=DR+1, max_row=DR+len(DANE))
KAT_REF = f"'Wykresy'!$B${DR+1}:$B${DR+len(DANE)}"

k1 = BarChart(); k1.type='col'; k1.grouping='clustered'
k1.add_data(dane, titles_from_data=True); k1.set_categories(kat)
wk.add_chart(ubierz(k1,'Słupki grupowane - cztery serie','Okres','Wartość'), 'H6')

k2 = BarChart(); k2.type='col'; k2.grouping='stacked'; k2.overlap=100
k2.add_data(dane, titles_from_data=True); k2.set_categories(kat)
wk.add_chart(ubierz(k2,'Słupki skumulowane','Okres','Wartość'), 'H24')

k3 = BarChart(); k3.type='bar'; k3.grouping='clustered'
k3.add_data(dane, titles_from_data=True); k3.set_categories(kat)
wk.add_chart(ubierz(k3,'Słupki poziome','Okres','Wartość'), 'R6')

# Linia nie ma wypelnienia, wiec obrys Atramentem nie ma czego obrysowac.
# Stopien 30 % ma do tla 1,87:1 i wypada; zostaja trzy serie nad progiem 3:1.
dane3 = Reference(wk, min_col=3, max_col=5, min_row=DR, max_row=DR+len(DANE))
k4 = LineChart()
k4.add_data(dane3, titles_from_data=True); k4.set_categories(kat)
ubierz(k4,'Linie - trzy serie, bo stopień 30 % nie przechodzi','Okres','Wartość')
for i, s in enumerate(k4.series):
    s.graphicalProperties = GraphicalProperties()
    s.graphicalProperties.line = LineProperties(solidFill=STOPNIE[i % 3], w=GRUB_LINII)
    s.smooth = False
wk.add_chart(k4, 'R24')

jedna = Reference(wk, min_col=3, max_col=3, min_row=DR, max_row=DR+len(DANE))
k5 = BarChart(); k5.type='col'
k5.add_data(jedna, titles_from_data=True); k5.set_categories(kat)
k5.dLbls = DataLabelList(); k5.dLbls.showVal = True
wk.add_chart(ubierz(k5,'Jedna seria - pełne krycie','Okres','Wartość'), 'H42')

# =========================== ARKUSZ 3: LEGENDA =============================
lg = wb.create_sheet('Legenda')
lg.sheet_view.showGridLines = False
lg['B2'] = 'CO JEST W TYM PLIKU I SKĄD'
lg['B2'].font = f(PT_META, SZAFIR, bold=True)
lg['B3'] = 'Legenda barw i reguł'
lg['B3'].font = f(PT_TEMAT, SZAFIR, bold=True)
lg.row_dimensions[3].height = 24
lg.column_dimensions['B'].width = 26
lg.column_dimensions['C'].width = 12
lg.column_dimensions['D'].width = 14
lg.column_dimensions['E'].width = 62

POZ = [
 ('Nagłówek tabeli', SZAFIR, '14,09:1', 'Szafir Nocny jako wypełnienie, Kość Słoniowa jako tekst'),
 ('Pas wiersza nieparzysty', KOSC, '17,99:1', 'Kość Słoniowa, tło strony; Atrament na niej'),
 ('Pas wiersza parzysty', ALABASTER, '15,25:1', 'Alabaster; Grafit Jedwabny na niej trzyma 4,61:1'),
 ('Pole do wpisania', MUSZLA, '14,26:1', 'Muszla Różana, rola „podświetlenia”; ramka Lapis Stonowany'),
 ('Tekst drugorzędny', GRAFIT, '5,44 / 4,61:1', 'Grafit Jedwabny; na tincie 12 % spada do 4,31 i łamie AA'),
 ('Linia tabeli', GRAFIT, '5,44:1', 'Grafit Jedwabny, minimum 0,25 mm'),
 ('Obrys serii wykresu', ATRAMENT, '17,99:1', 'Atrament 0,25 mm; Grafit na stopniu 72 % znika (1,09:1)'),
]
for i, (n, hexs, kon, opis) in enumerate(POZ):
    r = 5 + i
    lg.row_dimensions[r].height = WYS_WIERSZA
    lg.cell(row=r, column=2, value=n).font = f(PT_META)
    c = lg.cell(row=r, column=3, value='#'+hexs)
    c.font = f(PT_META, KOSC if hexs in (SZAFIR, ATRAMENT, GRAFIT) else ATRAMENT, mono=True)
    c.fill = tlo(hexs); c.alignment = Alignment(horizontal='center')
    lg.cell(row=r, column=4, value=kon).font = f(PT_META, GRAFIT, mono=True)
    lg.cell(row=r, column=5, value=opis).font = f(PT_META, GRAFIT)

r = 5 + len(POZ) + 1
lg.cell(row=r, column=2, value='STOPNIE SERII WYKRESU').font = f(PT_META, SZAFIR, bold=True)
for i, k in enumerate(('100','72','50','30')):
    rr = r + 1 + i
    lg.row_dimensions[rr].height = WYS_WIERSZA
    lg.cell(row=rr, column=2, value=f'Szafir Nocny {k} %').font = f(PT_META)
    c = lg.cell(row=rr, column=3, value=ST[k]['hex'])
    c.font = f(PT_META, KOSC if k in ('100','72') else ATRAMENT, mono=True)
    c.fill = tlo(ST[k]['hex'].lstrip('#')); c.alignment = Alignment(horizontal='center')
    lg.cell(row=rr, column=4, value=f"{ST[k]['do-tla']:.2f}:1".replace('.', ',')).font = f(PT_META, GRAFIT, mono=True)
    lg.cell(row=rr, column=5,
            value=('nad progiem 3:1 dla grafiki' if ST[k]['nad-progiem-3']
                   else 'PONIŻEJ 3:1 - granicę niesie obrys Atramentem i podpis serii')
            ).font = f(PT_META, GRAFIT)

r = r + 6
UWAGI = [
 'Źródła: 01-baza-wiedzy/identyfikacja/paleta-barw.md, siatka-a4.md, typografia.md.',
 'Kroje: Manrope i Inconsolata. Bez nich zainstalowanych Excel podstawi krój systemowy',
 'i cała skala się przesunie - to ograniczenie Excela, nie błąd w pliku.',
 'Marginesy wydruku 18 / 20 / 28 / 20 mm, orientacja pozioma, siatka arkusza wyłączona.',
 'Liczby w tabeli i na wykresach są wypełnieniem przykładowym, nie danymi IRIN.',
 'Każda oś wykresu jest podpisana słowem, oś Y zaczyna się od zera, serii jest najwyżej cztery.',
]
for i, t in enumerate(UWAGI):
    lg.cell(row=r+i, column=2, value=t).font = f(PT_META, GRAFIT)

WY = os.environ['WYNIK']
wb.save(WY)
print('zapisane', WY, os.path.getsize(WY), 'bajtow')
print('arkusze:', wb.sheetnames)
print('stopnie serii:', STOPNIE)
print('obrys:', OBRYS_EMU, 'EMU =', round(OBRYS_EMU/12700, 4), 'pt =', round(OBRYS_EMU/12700/72*25.4, 3), 'mm')
