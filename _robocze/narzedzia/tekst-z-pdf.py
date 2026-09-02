import re, zlib, sys
data = open(sys.argv[1],'rb').read()
# --- objects ---
objs = {}
for m in re.finditer(rb'(\d+)\s+(\d+)\s+obj\b(.*?)\bendobj', data, re.S):
    objs[int(m.group(1))] = m.group(3)
def stream_of(body):
    m = re.search(rb'stream\r?\n(.*?)\r?\nendstream', body, re.S)
    if not m: return None
    raw = m.group(1)
    if b'/FlateDecode' in body:
        try: return zlib.decompress(raw)
        except Exception:
            try: return zlib.decompressobj().decompress(raw)
            except Exception: return None
    return raw
def ref(body, key):
    m = re.search(rb'/'+key+rb'\s+(\d+)\s+\d+\s+R', body)
    return int(m.group(1)) if m else None
# --- fonts: ToUnicode maps ---
font_maps = {}
def parse_cmap(s):
    mp = {}
    for m in re.finditer(rb'beginbfchar(.*?)endbfchar', s, re.S):
        for a,b in re.findall(rb'<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>', m.group(1)):
            mp[int(a,16)] = bytes.fromhex(b.decode()).decode('utf-16-be','replace')
    for m in re.finditer(rb'beginbfrange(.*?)endbfrange', s, re.S):
        for lo,hi,dst in re.findall(rb'<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>', m.group(1)):
            lo,hi=int(lo,16),int(hi,16); d=int(dst,16)
            for c in range(lo,hi+1):
                mp[c]=chr(d+c-lo) if d+c-lo<0x110000 else '?'
    return mp
for n,b in objs.items():
    if b'/Font' in b and b'/ToUnicode' in b:
        tu = ref(b,b'ToUnicode')
        if tu in objs:
            s = stream_of(objs[tu])
            if s: font_maps[n] = parse_cmap(s)
# --- pages ---
pages = [n for n,b in objs.items() if re.search(rb'/Type\s*/Page\b', b)]
def parent_chain_order(n):
    return n
# order pages via Kids tree
def kids(n):
    b = objs.get(n,b''); m = re.search(rb'/Kids\s*\[(.*?)\]', b, re.S)
    return [int(x) for x in re.findall(rb'(\d+)\s+\d+\s+R', m.group(1))] if m else []
roots = [n for n,b in objs.items() if re.search(rb'/Type\s*/Pages\b', b) and b'/Parent' not in b]
ordered=[]
def walk(n):
    if re.search(rb'/Type\s*/Page\b', objs.get(n,b'')): ordered.append(n); return
    for k in kids(n): walk(k)
for r in roots: walk(r)
if not ordered: ordered = pages
def fonts_of_page(b):
    res = ref(b,b'Resources'); rb = objs.get(res,b'') if res else b
    m = re.search(rb'/Font\s*<<(.*?)>>', rb, re.S)
    fm = {}
    if m:
        for name,num in re.findall(rb'/(\w+)\s+(\d+)\s+\d+\s+R', m.group(1)): fm[name]=int(num)
    return fm
def decode_str(s, mp, two):
    out=[]
    if two:
        for i in range(0,len(s)-1,2):
            c=(s[i]<<8)|s[i+1]; out.append(mp.get(c, chr(c) if 32<=c<127 else chr(0xE000+c)))
    else:
        for c in s: out.append(mp.get(c, chr(c)) if mp else (chr(c) if c>=32 else chr(0xE000+c)))
    return ''.join(out)
def unescape_lit(s):
    return re.sub(rb'\\([nrtbf()\\]|\d{1,3})', lambda m: {b'n':b'\n',b'r':b'',b't':b' ',b'b':b'',b'f':b'',b'(':b'(',b')':b')',b'\\':b'\\'}.get(m.group(1), bytes([int(m.group(1),8)]) if m.group(1).isdigit() else b''), s)
out=[]
for pi,pn in enumerate(ordered,1):
    b = objs[pn]; fm = fonts_of_page(b)
    cont = ref(b,b'Contents')
    conts = [cont] if cont else []
    m = re.search(rb'/Contents\s*\[(.*?)\]', b, re.S)
    if m: conts = [int(x) for x in re.findall(rb'(\d+)\s+\d+\s+R', m.group(1))]
    stream = b''.join(stream_of(objs[c]) or b'' for c in conts if c in objs)
    mp={}; two=False; text=[]
    for tok in re.finditer(rb'/(\w+)\s+[\d.]+\s+Tf|\[(.*?)\]\s*TJ|\((?:[^()\\]|\\.)*\)\s*Tj|<([0-9A-Fa-f]+)>\s*Tj|(T\*|Td|TD|Tm|\')', stream, re.S):
        if tok.group(1):
            fn = fm.get(tok.group(1)); mp = font_maps.get(fn,{}); two = bool(mp) and max(mp.keys(),default=0)>255 or (fn and b'/Identity-H' in objs.get(fn,b''))
        elif tok.group(2) is not None:
            arr = tok.group(2)
            for p in re.finditer(rb'\((?:[^()\\]|\\.)*\)|<([0-9A-Fa-f]+)>|(-?[\d.]+)', arr):
                if p.group(1): text.append(decode_str(bytes.fromhex(p.group(1).decode()), mp, two))
                elif p.group(2):
                    try:
                        if float(p.group(2)) < -200: text.append(' ')
                    except: pass
                else: text.append(decode_str(unescape_lit(p.group(0)[1:-1]), mp, two))
        elif tok.group(3): text.append(decode_str(bytes.fromhex(tok.group(3).decode()), mp, two))
        elif tok.group(4): text.append('\n')
        else:
            s = tok.group(0)
            text.append(decode_str(unescape_lit(s[1:s.rfind(b')')]), mp, two))
    out.append(f'\n===== STRONA {pi} =====\n' + ''.join(text))
open(sys.argv[2],'w').write(''.join(out))
print(len(ordered),'stron;', len(font_maps),'fontów z ToUnicode')
