const fs = require('fs');
const P = process.env.DOCX || __dirname + '/node_modules/docx';
const { Document, Packer, Paragraph, TextRun, ImageRun, Header, Footer, PageNumber,
        AlignmentType, BorderStyle, TabStopType, LineRuleType,
        convertMillimetersToTwip } = require(P);

// ---- stale z warstwy 1 ------------------------------------------------------
const KROJ = 'Manrope';                 // typografia.md
const MONO = 'Inconsolata';             // typografia.md
const ATRAMENT = '07090C';              // paleta-barw.md, wersja znaku 01
const KOSC     = 'F7F3E9';
const GRAFIT   = '606369';
const SZAFIR   = '132246';              // wersja znaku 03, barwa markowa

const mm = convertMillimetersToTwip;

// skala z typografia.md: px -> pt (96 dpi, 1 px = 0,75 pt) -> polpunkty
const px = (v) => Math.round(v * 0.75 * 2);          // stopien pisma
const li = (pxStopien, mnoznik) => Math.round(pxStopien * 0.75 * mnoznik * 20); // interlinia w twipach
const tr = (em, pxStopien) => Math.round(em * pxStopien * 0.75 * 20);           // tracking w twipach

const S = {
  h2:        { size: px(24),   line: li(24, 1.10),   spacing: tr(-0.01, 24) },
  h3:        { size: px(16),   line: li(16, 1.30),   spacing: 0 },
  lead:      { size: px(16),   line: li(16, 1.40),   spacing: 0 },
  korpus:    { size: px(13.5), line: li(13.5, 1.55), spacing: 0 },
  meta:      { size: px(10),   line: li(10, 1.50),   spacing: 0 },
  kicker:    { size: px(14),   line: li(14, 1.20),   spacing: tr(0.22, 14) },
  mono:      { size: px(10.5), line: li(10.5, 1.50), spacing: 0 },
};

// ---- siatka z siatka-a4.md -------------------------------------------------
const KOL = (n) => 29 * n - 4;          // szerokosc n kolumn w mm
const POLE = KOL(6);                    // 170 mm
const KORPUS_SZER = KOL(4);             // 112 mm - swobodny wybor projektowy
const SYGN_START  = 29 * 3;             // 87 mm, blok sygnatury = 3 kolumny
const ADRES_SZER  = KOL(3);             // 83 mm - 54 mm lamalo nazwe adresata na dwie linie

// ---- znak: logotyp.md ------------------------------------------------------
// 40 mm to jedna z trzech szerokosci, dla ktorych logotyp.md podaje x wprost (8,44 mm).
const ZNAK_MM = 40;
const znak = fs.readFileSync(__dirname + '/znak-poziom.png');
const PROP = 1572 / 332;                             // proporcja pliku PNG
const znakW = ZNAK_MM / 25.4 * 96;
const znakH = znakW / PROP;

const naglowek = new Header({ children: [
  new Paragraph({ spacing: { before: 0, after: 0 }, children: [
    new ImageRun({ type: 'png', data: znak, altText: {
        title: 'IRIN', description: 'Logotyp Instytutu Rozwoju i Nauki, wariant poziomy', name: 'IRIN' },
      transformation: { width: znakW, height: znakH } })
  ]})
]});

const meta = (text, o={}) => new TextRun(Object.assign(
  { text, font: KROJ, size: S.meta.size, color: GRAFIT }, o));
const metaMono = (text) => new TextRun(
  { text, font: MONO, size: S.mono.size, color: GRAFIT });

const LINIA = { top: { style: BorderStyle.SINGLE, size: 6, space: 6, color: GRAFIT } };

const TAB = [{ type: TabStopType.RIGHT, position: mm(POLE) }];

const stopka = new Footer({ children: [
  new Paragraph({ border: LINIA, style: 'irinMeta', spacing: { before: 0, after: 40 },
    tabStops: TAB, children: [
      meta('Instytut Rozwoju i Nauki sp. z o.o., ul. Karola Olszewskiego 6, 25-663 Kielce'),
      meta('\t'), meta('[e-mail firmowy]') ]}),
  new Paragraph({ style: 'irinMeta', spacing: { after: 40 }, tabStops: TAB, children: [
    meta('Sąd Rejonowy w Kielcach, X Wydział Gospodarczy Krajowego Rejestru Sądowego, KRS '),
    metaMono('0001032499'),
    meta('\t'), meta('[telefon]') ]}),
  new Paragraph({ style: 'irinMeta', tabStops: TAB, children: [
    meta('NIP '), metaMono('9592061542'),
    meta('  ·  kapitał zakładowy '), metaMono('40 000,00 zł'),
    meta('  ·  www.irin.pl'),
    meta('\t'),
    new TextRun({ children: ['strona ', PageNumber.CURRENT, ' z ', PageNumber.TOTAL_PAGES],
      font: MONO, size: S.mono.size, color: GRAFIT })
  ]})
]});

// ---- styl akapitu ----------------------------------------------------------
const styl = (id, name, s, extra={}) => Object.assign({
  id, name, basedOn: 'irinKorpus', next: 'irinKorpus', quickFormat: true,
  run: { font: KROJ, size: s.size, color: ATRAMENT, characterSpacing: s.spacing },
  paragraph: { spacing: { line: s.line, lineRule: LineRuleType.EXACT, after: mm(6) },
               indent: { right: mm(POLE - KORPUS_SZER) } }
}, extra);

const style = {
  default: { document: {
    run: { font: KROJ, size: S.korpus.size, color: ATRAMENT },
    paragraph: { spacing: { line: S.korpus.line, lineRule: LineRuleType.EXACT, after: mm(6) } }
  }},
  paragraphStyles: [
    styl('irinKorpus', 'IRIN Korpus', S.korpus, { basedOn: 'Normal', next: 'irinKorpus' }),
    styl('irinLead', 'IRIN Lead', S.lead, { run: {
        font: KROJ, size: S.lead.size, color: ATRAMENT } }),
    styl('irinTemat', 'IRIN Temat', S.h2, {
      run: { font: KROJ, size: S.h2.size, bold: true, color: SZAFIR,
             characterSpacing: S.h2.spacing },
      paragraph: { spacing: { line: S.h2.line, lineRule: LineRuleType.EXACT, after: mm(12) },
                   indent: { right: mm(POLE - KORPUS_SZER) }, outlineLevel: 1,
                   keepNext: true } }),
    styl('irinPodsekcja', 'IRIN Podsekcja', S.h3, {
      run: { font: KROJ, size: S.h3.size, bold: true, color: SZAFIR },
      paragraph: { spacing: { before: mm(12), line: S.h3.line, lineRule: LineRuleType.EXACT,
                              after: mm(6) },
                   indent: { right: mm(POLE - KORPUS_SZER) }, outlineLevel: 2,
                   keepNext: true } }),
    styl('irinKicker', 'IRIN Kicker', S.kicker, {
      next: 'irinTemat',
      run: { font: KROJ, size: S.kicker.size, bold: true, color: SZAFIR,
             characterSpacing: S.kicker.spacing, allCaps: true },
      paragraph: { spacing: { line: S.kicker.line, lineRule: LineRuleType.EXACT, after: mm(6) },
                   indent: { right: mm(POLE - KORPUS_SZER) }, keepNext: true } }),
    styl('irinMeta', 'IRIN Metadane', S.meta, {
      run: { font: KROJ, size: S.meta.size, color: GRAFIT } }),
    styl('irinAdresat', 'IRIN Adresat', S.korpus, {
      paragraph: { spacing: { line: S.korpus.line, lineRule: LineRuleType.EXACT, after: 0 },
                   indent: { right: mm(POLE - ADRES_SZER) } } }),
    styl('irinSygnatura', 'IRIN Sygnatura', S.korpus, {
      paragraph: { alignment: AlignmentType.RIGHT,
                   spacing: { line: S.korpus.line, lineRule: LineRuleType.EXACT, after: 0 },
                   indent: { left: mm(SYGN_START) } } }),
  ],
  characterStyles: [
    { id: 'irinKod', name: 'IRIN Kod', quickFormat: true,
      run: { font: MONO, size: S.mono.size, color: ATRAMENT } }
  ]
};

// ---- tresc: wylacznie placeholdery -----------------------------------------
const t = (text, o={}) => new TextRun(Object.assign({ text }, o));

const tresc = [
  new Paragraph({ style: 'irinMeta', spacing: { before: mm(24), after: 0 },
    children: [ t('ADRESAT', { font: KROJ, size: S.meta.size, color: GRAFIT,
                               characterSpacing: tr(0.22, 10), allCaps: true }) ]}),
  new Paragraph({ style: 'irinAdresat',
    children: [ t('[Imię i nazwisko albo nazwa firmy]') ]}),
  new Paragraph({ style: 'irinAdresat', children: [ t('[ulica i numer]') ]}),
  new Paragraph({ style: 'irinAdresat', spacing: { after: mm(12) },
    children: [ t('[kod pocztowy i miejscowość]') ]}),

  new Paragraph({ style: 'irinKorpus', alignment: AlignmentType.RIGHT,
    indent: { right: 0 }, spacing: { after: mm(12) }, children: [
      t('Kielce, ', { color: GRAFIT }),
      t('[RRRR-MM-DD]', { font: MONO, size: S.mono.size, color: GRAFIT }) ]}),

  new Paragraph({ style: 'irinKicker', children: [ t('[KATEGORIA PISMA]') ]}),
  new Paragraph({ style: 'irinTemat', children: [ t('[Temat pisma w jednym zdaniu]') ]}),
  new Paragraph({ style: 'irinLead', spacing: { after: mm(12) }, children: [
    t('[Lead: jedno albo dwa zdania, które mówią, po co jest to pismo i czego dotyczy.]') ]}),

  new Paragraph({ style: 'irinPodsekcja', children: [ t('[Podsekcja]') ]}),
  new Paragraph({ style: 'irinKorpus', children: [
    t('[Akapit korpusu. Zdanie kontrolne z pełnym zestawem polskich znaków: żółć, gęś, źdźbło, ćma, łódź, świt, żółw - ĄĆĘŁŃÓŚŹŻ ąćęłńóśźż.]') ]}),
  new Paragraph({ style: 'irinKorpus', spacing: { after: mm(24) }, children: [
    t('[Akapit drugi. Odstęp między akapitami to 6 mm, czyli jedna jednostka rytmu pionowego.]') ]}),

  new Paragraph({ style: 'irinMeta', spacing: { after: mm(24) }, children: [
    meta('Nr pisma: '), metaMono('[numer pisma]'),
    meta('   ·   Numer usługi w BUR: '), metaMono('[numer usługi]') ]}),

  new Paragraph({ style: 'irinSygnatura', border: {
      top: { style: BorderStyle.SINGLE, size: 6, space: 8, color: GRAFIT } },
    children: [ t('[Imię i Nazwisko]') ]}),
  new Paragraph({ style: 'irinSygnatura', children: [
    t('[stanowisko osoby upoważnionej]', { size: S.meta.size, color: GRAFIT }) ]}),
];

const doc = new Document({
  creator: 'Instytut Rozwoju i Nauki sp. z o.o.',
  title: 'Pismo firmowe IRIN - szablon',
  description: 'Szablon pisma firmowego. Paleta Regalia, siatka A4 i skala z warstwy 1.',
  styles: style,
  sections: [{
    properties: { page: {
      margin: { top: mm(18), right: mm(20), bottom: mm(28), left: mm(20),
                header: mm(9), footer: mm(12) } } },
    headers: { default: naglowek },
    footers: { default: stopka },
    children: tresc
  }]
});

Packer.toBuffer(doc).then(b => {
  fs.writeFileSync(__dirname + '/pismo-irin.docx', b);
  console.log('zapisane pismo-irin.docx,', b.length, 'bajtow');
  console.log('znak:', znakW.toFixed(3), 'x', znakH.toFixed(3), 'px =',
              (znakW/96*25.4).toFixed(3), 'x', (znakH/96*25.4).toFixed(3), 'mm');
  console.log('stopnie (polpunkty):', JSON.stringify(
    Object.fromEntries(Object.entries(S).map(([k,v]) => [k, [v.size, v.line, v.spacing]]))));
  console.log('pole tresci', POLE, 'mm; korpus', KORPUS_SZER, 'mm; prawy wciecie',
              POLE - KORPUS_SZER, 'mm =', mm(POLE - KORPUS_SZER), 'tw');
});
