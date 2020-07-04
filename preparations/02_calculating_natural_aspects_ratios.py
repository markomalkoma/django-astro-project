import pandas as pd

astro=pd.read_csv('ephemeris.csv')

print('\n***CALCULATION OF ASPECTS PROBABILITY***\n')
print('List of celestial bodies: Sun, Moon, Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto, Tnode, Mnode, Lilit, Chiron\n')

planets=['Sun', 'Moon', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto', 'Tnode', 'Mnode', 'Lilit', 'Chiron']

for a in planets:
    for b in planets[planets.index(a)+1:]:
    
        con=0
        sex=0
        sqr=0
        trg=0
        ops=0

        loop=0

        for index, row in astro.iterrows():

            loop+=1
            
            d1=float(row[a])
            d2=float(row[b])

            l=d2-8
            h=d2+8
            sgn=l*h
            if l<0:
                l=l+360
            if h>360:
                h=h-360
            if sgn<0:
                if l<d1<360:
                    con+=1
                elif 0<d1<h:
                    con+=1
            elif l<d1<h:
                con+=1
                    
            l1=d2-30-3
            h1=d2-30+3
            sgn=l1*h1
            if l1<0:
                l1=l1+360
            if h1<0:
                h1=h1+360
            if sgn<0:
                if l1<d1<360:
                    sex+=1
                elif 0<d1<h1:
                    sex+=1 
            elif l1<d1<h1:
                sex+=1
                
            l2=d2+30-3
            h2=d2+30+3
            if l2>360:
                l2=l2-360
            if h2>360:
                h2=h2-360
            if l2>h2:
                if l2<d1<360:
                    sex+=1
                elif 0<d1<h2:
                    sex+=1 
            elif l2<d1<h2:
                sex+=1

            l1=d2-90-8
            h1=d2-90+8
            sgn=l1*h1
            if l1<0:
                l1=l1+360   
            if h1<0:
                h1=h1+360
            if sgn<0:
                if l1<d1<360:
                    sqr+=1
                elif 0<d1<h1:
                    sqr+=1
            elif l1<d1<h1:
                sqr+=1


            l2=d2+90-8
            h2=d2+90+8
            if l2>360:
                l2=l2-360
            if h2>360:
                h2=h2-360
            if l2>h2:
                if l2<d1<360:
                    sqr+=1
                elif 0<d1<h2:
                    sqr+=1 
            elif l2<d1<h2:
                sqr+=1

            l1=d2-120-8
            h1=d2-120+8
            sgn=l1*h1
            if l1<0:
                l1=l1+360
            if h1<0:
                h1=h1+360
            if sgn<0:
                if l1<d1<360:
                    trg+=1
                elif 0<d1<h1:
                    trg+=1
            elif l1<d1<h1:
                trg+=1
                    
            l2=d2+120-8
            h2=d2+120+8
            if l2>360:
                l2=l2-360
            if h2>360:
                h2=h2-360
            if l2>h2:
                if l2<d1<360:
                    trg+=1
                elif 0<d1<h2:
                    trg+=1 
            elif l2<d1<h2:
                trg+=1
                
            l=d2-180-8
            h=d2-180+8
            sgn=l*h
            if l<0:
                l=l+360
            if h<0:
                h=h+360
            if sgn<0:
                if l<d1<0:
                    ops+=1
                elif 0<d1<h:
                    ops+=1
            elif l<d1<h:
                ops+=1

                
        aspects_all=con+sex+sqr+trg+ops
        print('\nPROBABILITIES FOR '+a.upper()+' AND '+b.upper()+':\n')
        print('Conjuction:\t'+str(round(con/loop*100, 2))+'%')
        print('Sextile:\t'+str(round(sex/loop*100, 2))+'%')
        print('Square:\t\t'+str(round(sqr/loop*100, 2))+'%')
        print('Trine: \t\t'+str(round(trg/loop*100, 2))+'%')
        print('Opposition:\t'+str(round(ops/loop*100, 2))+'%')
        print('\nAll aspects:\t'+str(round(aspects_all/loop*100, 2))+'%')

