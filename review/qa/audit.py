import json,sys
from PIL import Image, ImageDraw
def lum(c):
    def f(v):
        v/=255
        return v/12.92 if v<=0.03928 else ((v+0.055)/1.055)**2.4
    r,g,b=c[:3]; return 0.2126*f(r)+0.7152*f(g)+0.0722*f(b)
TEXT={'head':(236,238,233),'sub':(221,226,229),'em':(245,188,65)}
name=sys.argv[1] if len(sys.argv)>1 else 'audit-1440x900.json'
audit=json.load(open(name))
worst={}
for a in audit:
    im=Image.open(a['file']).convert('RGB'); px=im.load()
    for bx in a['boxes']:
        x0,y0=int(max(0,bx['x'])),int(max(0,bx['y'])); x1,y1=int(min(im.width,bx['x']+bx['w'])),int(min(im.height,bx['y']+bx['h']))
        L=0; at=None
        for y in range(y0,y1):
            for x in range(x0,x1):
                l=lum(px[x,y])
                if l>L: L=l; at=(x,y)
        lt=lum(TEXT[bx['kind']]); cr=(max(lt,L)+.05)/(min(lt,L)+.05)
        key=(a['band'],bx['kind'])
        if key not in worst or cr<worst[key][0]: worst[key]=(cr,a['p'],bx.get('word',''),at,a['file'],px[at[0],at[1]] if at else None)
bad=0
for k,v in sorted(worst.items()):
    ok=v[0]>=3.5; bad+= not ok
    print('band %d %-4s worst %.2f:1 p=%.3f word=%-14s px=%s rgb=%s %s'%(k[0],k[1],v[0],v[1],v[2],v[3],v[5],'OK' if ok else 'FAIL'))
print('FAILS',bad)
