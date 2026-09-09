import sys,zlib,struct
def czytaj(p):
    d=open(p,'rb').read(); i=8; idat=b''
    while i<len(d):
        ln=struct.unpack('>I',d[i:i+4])[0]; typ=d[i+4:i+8]; dat=d[i+8:i+8+ln]
        if typ==b'IHDR': w,h,bd,ct=struct.unpack('>IIBB',dat[:10])
        elif typ==b'IDAT': idat+=dat
        i+=12+ln
    kan={0:1,2:3,3:1,4:2,6:4}[ct]; bpp=kan*bd//8
    raw=zlib.decompress(idat); st=w*bpp; out=bytearray(); prev=bytearray(st); o=0
    for y in range(h):
        ft=raw[o]; o+=1; line=bytearray(raw[o:o+st]); o+=st
        if ft==1:
            for x in range(bpp,st): line[x]=(line[x]+line[x-bpp])&255
        elif ft==2:
            for x in range(st): line[x]=(line[x]+prev[x])&255
        elif ft==3:
            for x in range(st): line[x]=(line[x]+((line[x-bpp] if x>=bpp else 0)+prev[x])//2)&255
        elif ft==4:
            for x in range(st):
                a=line[x-bpp] if x>=bpp else 0; b=prev[x]; cc=prev[x-bpp] if x>=bpp else 0
                pp=a+b-cc; pa,pb,pc=abs(pp-a),abs(pp-b),abs(pp-cc)
                pr=a if (pa<=pb and pa<=pc) else (b if pb<=pc else cc)
                line[x]=(line[x]+pr)&255
        out+=line; prev=line
    return w,h,bpp,bytes(out)
p=sys.argv[1]; skala=float(sys.argv[2])   # px na mm
w,h,bpp,px=czytaj(p)
print(f'{p}: {w}x{h} px, {skala} px/mm')
wier=[]
for y in range(h):
    row=px[y*w*bpp:(y+1)*w*bpp]
    wier.append(sum(1 for x in range(0,len(row),bpp) if row[x]<200))
pas=[]; st_=None
for y,c in enumerate(wier):
    if c>0 and st_ is None: st_=y
    elif c==0 and st_ is not None: pas.append((st_,y-1)); st_=None
if st_ is not None: pas.append((st_,h-1))
for a,b in pas:
    xs=[]
    for y in range(a,b+1):
        row=px[y*w*bpp:(y+1)*w*bpp]
        for x in range(0,w):
            if row[x*bpp]<200: xs.append(x); break
    l=min(xs)/skala if xs else 0
    r=0
    for y in range(a,b+1):
        row=px[y*w*bpp:(y+1)*w*bpp]
        for x in range(w-1,-1,-1):
            if row[x*bpp]<200: r=max(r,x); break
    print(f'  {a/skala:7.2f} - {b/skala:7.2f} mm  wys {(b-a+1)/skala:5.2f}  lewa {l:6.2f}  prawa {r/skala:6.2f}')
