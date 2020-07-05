from django.shortcuts import render, redirect
from . models import Nata, Tipo, Position
from math import factorial
from . aspects_prob import p_aspects
import pandas as pd
from itertools import combinations
from django.contrib import messages
import sigfig

types=Tipo.objects.all()

maping_planets={
0:'sun',
1:'moon',
2:'mercury',
3:'venus',
4:'mars',
5:'jupiter',
6:'saturn',
7:'uranus',
8:'neptune',
9:'pluto',
10:'tnode',
11:'mnode',
12:'lilit',
13:'chiron',
}


planets_order={
'sun':0,
'moon':1,
'mercury':2,
'venus':3,
'mars':4,
'jupiter':5,
'saturn':6,
'uranus':7,
'neptune':8,
'pluto':9,
'tnode':10,
'mnode':11,
'lilit':12,
'chiron':13,
}

def ordering(x):
    return planets_order(x)


planets=['sun','moon','mercury','venus','mars','jupiter','saturn','uranus','neptune','pluto','tnode','mnode','lilit','chiron']


maping_aspects={0:'conjuction',1:'sextile',2:'square',3:'trine',4:'opposition',5:'aspect'}
maping_symbols={0:chr(9740),1:chr(8727),2:chr(9723),3:chr(9651),4:chr(9741)}


def positions(human):

    positions_list=[]
        
    planets=['Sun', 'Moon', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto', 'Tnode', 'Mnode', 'Lilit', 'Chiron']
    f=pd.read_csv('astrology/static/modeling/ephemeris.csv')    
    i=f.loc[(f.Year==human.year) & (f.Month==human.month) & (f.Day==human.day)].index[0]
    today=f.iloc[i]
    tomorow=f.iloc[i+1]

        
    for planet in planets:
        if abs(tomorow[planet]-today[planet])<30:           
            if tomorow[planet]-today[planet]<0:
                pos=today[planet]-(today[planet]-tomorow[planet])*(human.hour*60+human.minutes)/1440
            else:
                pos=(tomorow[planet]-today[planet])*(human.hour*60+human.minutes)/1440+today[planet]
        else:
            if tomorow[planet]-today[planet]<0:
                pos=(tomorow[planet]+360-today[planet])*(human.hour*60+human.minutes)/1440+today[planet]
            else:
                pos=today[planet]+360-(today[planet]+360-tomorow[planet])*(human.hour*60+human.minutes)/1440
        if pos>360:
            pos=pos-360
        pos=round(pos,3)
        positions_list.append(pos)
            
    planet_set=Position(natus=human) 

    human.position.sun=positions_list[0]
    human.position.moon=positions_list[1]
    human.position.mercury=positions_list[2]
    human.position.venus=positions_list[3]
    human.position.mars=positions_list[4]
    human.position.jupiter=positions_list[5]
    human.position.saturn=positions_list[6]
    human.position.uranus=positions_list[7]
    human.position.neptune=positions_list[8]
    human.position.pluto=positions_list[9]
    human.position.tnode=positions_list[10]
    human.position.mnode=positions_list[11]
    human.position.lilit=positions_list[12]
    human.position.chiron=positions_list[13]

    planet_set.save()


def refresh(request):
    for human in Nata.objects.all():    
        try:
            positions(human)
        except:
            pass
    context={}
    context['types']=types
    context['planets']=planets
    context['results']=list(range(1,101))

    return render(request, 'modeling/blanco.html', context)    


def complete(request, **kwargs):

    categories=[]

    for tip, cat in kwargs.items():
        categories.append(cat)

    
    people=[]

    for human in Nata.objects.all():
        for cat in human.category.all():
            if cat.name in categories:
                if human not in people:
                    people.append(human)
                

    
    context={'people':people}
    context['planets']=planets
    context['categories']=categories
    context['types']=types
    context['results']=list(range(1,101))

    planetarium=[]
    
    for a in range(0,13):
        for b in range(a+1,14):

            p_lister=[]
            p_lister.append('1')
            p_lister.append(maping_planets[a])
            p_lister.append(maping_planets[b])
        
            con=0
            sex=0
            sqr=0
            trg=0
            ops=0

            loop=0
       
            for row in people:
                if 1 in (a,b) and row.precise==0:
                    continue

                loop+=1

                maping_functions={
                0:row.position.sun,
                1:row.position.moon,
                2:row.position.mercury,
                3:row.position.venus,
                4:row.position.mars,
                5:row.position.jupiter,
                6:row.position.saturn,
                7:row.position.uranus,
                8:row.position.neptune,
                9:row.position.pluto,
                10:row.position.tnode,
                11:row.position.mnode,
                12:row.position.lilit,
                13:row.position.chiron,
                }
                
                d1=maping_functions[a]
                d2=maping_functions[b]

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
                    
                l1=d2-60-4
                h1=d2-60+4
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
                
                l2=d2+60-4
                h2=d2+60+4
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
            
            probas=p_aspects[maping_planets[a]][maping_planets[b]]

            p_lister.extend(probas)

            frequency=[round(con/loop, 4), round(sex/loop, 4),round(sqr/loop, 4),round(trg/loop, 4),round(ops/loop, 4), round(aspects_all/loop, 4),] 
            p_lister.extend(frequency)
            
            present=[]
            absent=[]
            counter=0
        
            for hits in [con,sex,sqr,trg,ops,aspects_all]:
                suma_pr=0
                for hit in range(hits,loop+1):
                    p=(((probas[counter])**hit)*((1-probas[counter])**(loop-hit)))*(factorial(loop))/(factorial(loop-hit)*factorial(hit))
                    suma_pr+=p
                present.append(round(suma_pr, 4))
                suma_ab=0
                for hit in range(0, hits+1):
                    p=(((probas[counter])**hit)*((1-probas[counter])**(loop-hit)))*(factorial(loop))/(factorial(loop-hit)*factorial(hit))
                    suma_ab+=p
                absent.append(round(suma_ab, 4))
                counter+=1
               
            p_lister.extend(present)       
            p_lister.extend(absent)

            planetarium.append(p_lister)
            
        context['planetarium']=planetarium
        


    return render(request, 'modeling/complete.html', context)
    



def group(request, **kwargs):
    categories=[]

    for tip, cat in kwargs.items():
        categories.append(cat)

    people=[]

    for human in Nata.objects.all():
        for cat in human.category.all():
            if cat.name in categories:
                if human not in people:
                    people.append(human)
                  
    def sorter(x):
        return x.name
    
    people.sort(key=sorter)

    
    context={'people':people}
    context['planets']=planets
    context['types']=types
    context['categories']=categories
    context['results']=list(range(1,101))

    return render(request, 'modeling/group.html', context)



def detail(request, hid):

    month_mapper={1:"January",2:"February",3:"March",4:"April",5:"May",6:"Jun",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
    
    human=Nata.objects.get(id=hid)

    context={'human':human}
    context['month']=month_mapper[human.month]

    aspects_tuple=[]
    
    for a in range(0,13):
        for b in range(a+1,14):
            
            con=0
            sex=0
            sqr=0
            trg=0
            ops=0
            
            if 1 in (a,b) and human.precise==0:
                continue

            maping_functions={
            0:human.position.sun,
            1:human.position.moon,
            2:human.position.mercury,
            3:human.position.venus,
            4:human.position.mars,
            5:human.position.jupiter,
            6:human.position.saturn,
            7:human.position.uranus,
            8:human.position.neptune,
            9:human.position.pluto,
            10:human.position.tnode,
            11:human.position.mnode,
            12:human.position.lilit,
            13:human.position.chiron,
            }
                
            d1=maping_functions[a]
            d2=maping_functions[b]

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

            if con:
                r=(max(d1,d2)-min(d1,d2))
                if r > 10:
                    d3=min(d1,d2)+360
                    r=d3-max(d1,d2)
                    
            l1=d2-60-4
            h1=d2-60+4
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
                
            l2=d2+60-4
            h2=d2+60+4
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
                
            if sex:
                r=abs((max(d1,d2)-min(d1,d2)-60))
                if r > 5:
                    d3=min(d1,d2)+360
                    r=abs(d3-max(d1,d2)-60)
                
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

            if sqr:
                r=abs((max(d1,d2)-min(d1,d2)-90))
                if r > 10:
                    d3=min(d1,d2)+360
                    r=abs(d3-max(d1,d2)-90)

                
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


            if trg:
                r=abs((max(d1,d2)-min(d1,d2)-120))
                if r > 10:
                    d3=min(d1,d2)+360
                    r=abs(d3-max(d1,d2)-120)

                
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

            if ops:
                r=abs((max(d1,d2)-min(d1,d2)-180))

            
            maping_aspect_functions={0:con,1:sex,2:sqr,3:trg,4:ops}
            
            for hit in range(5):
                if maping_aspect_functions[hit]:
                    aspects_tuple.append((r,maping_symbols[hit], maping_planets[a]+' '+maping_aspects[hit]+' '+maping_planets[b]))
                

            aspects_tuple.sort()

            aspects=[]
            for num, symbol, text in aspects_tuple:
                r=int(round(num,0))
                aspects.append((symbol, text,' orb '+str(r)))
                
                
                
    context['aspects']=aspects
    context['planets']=planets
    context['types']=types
    context['results']=list(range(1,101))
    
    return render(request, 'modeling/detail.html', context)




def dominant(request, planet1, planet2, planet3, planet4, aspect1, aspect2, **kwargs):

    categories=[]

    for tip, cat in kwargs.items():
        categories.append(cat)

    if planets_order[planet1] > planets_order[planet2]:
        planet1, planet2 = planet2, planet1

    if planets_order[planet3] > planets_order[planet4]:
        planet3, planet4 = planet4, planet3
    
    p1=p_aspects[planet1][planet2][aspect1]
    p2=p_aspects[planet3][planet4][aspect2]

    try:
        p_1=p1/(p1+p2)
        p_2=p2/(p1+p2)
    except:
        p_1=0
        p_2=0
        

    asp=[aspect1, aspect2]
    
    mooner=0
    for planet in [planet1, planet2, planet3, planet4]:
        if 'moon' in planet:
            mooner=1
        
    loop=0
    first=0
    second=0

    first_group=[]
    second_group=[]

    for human in Nata.objects.all():
        if mooner and not human.precise:
            continue
        
        
        par=[]
        combo=[(planet1, planet2), (planet3, planet4)]
        for member in combo:

            con=0
            sex=0
            sqr=0
            trg=0
            ops=0

            
            maping_functions={
            'sun':human.position.sun,
            'moon':human.position.moon,
            'mercury':human.position.mercury,
            'venus':human.position.venus,
            'mars':human.position.mars,
            'jupiter':human.position.jupiter,
            'saturn':human.position.saturn,
            'uranus':human.position.uranus,
            'neptune':human.position.neptune,
            'pluto':human.position.pluto,
            'tnode':human.position.tnode,
            'mnode':human.position.mnode,
            'lilit':human.position.lilit,
            'chiron':human.position.chiron,
            }
                
            d1=maping_functions[member[0]]
            d2=maping_functions[member[1]]

            l=d2-10
            h=d2+10
            sgn=l*h
            if l<0:
                l=l+360
            if h>360:
                h=h-360
            if sgn<0:
                if l<d1<360:
                    con=1
                elif 0<d1<h:
                    con=1
            elif l<d1<h:
                con=1

            if con:
                r=(max(d1,d2)-min(d1,d2))
                if r > 10:
                    d3=min(d1,d2)+360
                    r=d3-max(d1,d2)
                    
                    
            l1=d2-60-5
            h1=d2-60+5
            sgn=l1*h1
            if l1<0:
                l1=l1+360
            if h1<0:
                h1=h1+360
            if sgn<0:
                if l1<d1<360:
                    sex=1
                elif 0<d1<h1:
                    sex=1 
            elif l1<d1<h1:
                sex=1
                              
            l2=d2+60-5
            h2=d2+60+5
            if l2>360:
                l2=l2-360
            if h2>360:
                h2=h2-360
            if l2>h2:
                if l2<d1<360:
                    sex=1
                elif 0<d1<h2:
                    sex=1 
            elif l2<d1<h2:
                sex=1

            if sex:
                r=abs((max(d1,d2)-min(d1,d2)-60))
                if r > 5:
                    d3=min(d1,d2)+360
                    r=abs(d3-max(d1,d2)-60)

            l1=d2-90-10
            h1=d2-90+10
            sgn=l1*h1
            if l1<0:
                l1=l1+360   
            if h1<0:
                h1=h1+360
            if sgn<0:
                if l1<d1<360:
                    sqr=1
                elif 0<d1<h1:
                    sqr=1
            elif l1<d1<h1:
                sqr=1

            l2=d2+90-10
            h2=d2+90+10
            if l2>360:
                l2=l2-360
            if h2>360:
                h2=h2-360
            if l2>h2:
                if l2<d1<360:
                    sqr=1
                elif 0<d1<h2:
                    sqr=1 
            elif l2<d1<h2:
                sqr=1

            if sqr:
                r=abs((max(d1,d2)-min(d1,d2)-90))
                if r > 10:
                    d3=min(d1,d2)+360
                    r=abs(d3-max(d1,d2)-90)
            
            l1=d2-120-10
            h1=d2-120+10
            sgn=l1*h1
            if l1<0:
                l1=l1+360
            if h1<0:
                h1=h1+360
            if sgn<0:
                if l1<d1<360:
                    trg=1
                elif 0<d1<h1:
                    trg=1
            elif l1<d1<h1:
                trg=1
                        
            l2=d2+120-10
            h2=d2+120+10
            if l2>360:
                l2=l2-360
            if h2>360:
                h2=h2-360
            if l2>h2:
                if l2<d1<360:
                    trg=1
                elif 0<d1<h2:
                    trg=1 
            elif l2<d1<h2:
                trg=1

            if trg:
                r=abs((max(d1,d2)-min(d1,d2)-120))
                if r > 10:
                    d3=min(d1,d2)+360
                    r=abs(d3-max(d1,d2)-120)

                    
            l=d2-180-10
            h=d2-180+10
            sgn=l*h
            if l<0:
                l=l+360
            if h<0:
                h=h+360
            if sgn<0:
                if l<d1<0:
                    ops=1
                elif 0<d1<h:
                    ops=1
            elif l<d1<h:
                ops=1

            if ops:
                r=abs((max(d1,d2)-min(d1,d2)-180))
            
            present=con+sex+sqr+trg+ops
            maping_aspects_f={0:con,1:sex,2:sqr,3:trg,4:ops,5:present}
            
            if maping_aspects_f[asp[combo.index(member)]]:
                par.append(r)
            else:
                par.append(False)
                

        if all(par):
            if abs(par[0]-par[1])>4:
                loop+=1
                if par[0]==min(par[0],par[1]):
                    first+=1
                    first_group.append(human)
                else:
                    second+=1
                    second_group.append(human)
                    
        elif any(par):
            loop+=1
            if par[0]:
                first+=1
                first_group.append(human)
            else:
                second+=1
                second_group.append(human)

    if loop==0:
        r_1=0
        r_2=0
    else:
        r_1=round(first/loop, 4)
        r_2=round(second/loop, 4)
      
    suma_1=0
    for hit in range(first,loop+1):
        prb=(((p_1)**hit)*((p_2)**(loop-hit)))*(factorial(loop))/(factorial(loop-hit)*factorial(hit))
        suma_1+=prb

    suma_2=0
    for hit in range(second,loop+1):
        prb=(((p_2)**hit)*((p_1)**(loop-hit)))*(factorial(loop))/(factorial(loop-hit)*factorial(hit))
        suma_2+=prb
                   

    p_1=round(p_1, 4)
    p_2=round(p_2, 4)
    suma_1=round(suma_1, 4)
    suma_2=round(suma_2, 4)

    context={'planetas':[[planet1, planet2],[planet3, planet4]]}
    context['aspects']=[maping_aspects[aspect1], maping_aspects[aspect2]]
    context['categories']=categories
    context['rates']=[p_1, p_2, first, second, loop, r_1, r_2]
    context['probas']=[suma_1, suma_2]
    context['humans']=[first_group, second_group, first_group+second_group]
    context['planets']=planets
    context['types']=types
    context['results']=list(range(1,101))


    
    return render(request, 'modeling/dominant.html', context)
        

def combined(request, results, **kwargs):

    categories=[]
    planetas=[]

    for tip, cat in kwargs.items():
        if tip[0]=='c':
            categories.append(cat)
        if tip[0]=='p':
            planetas.append(cat)

            
    def ordering(x):
        return planets_order[x]

    planetas.sort(key=ordering)
    
    number_of_planets=len(planetas)


    if 'moon' in planetas:
        moonless=False
    else:
        moonless=True

    
    people=[]

    for human in Nata.objects.all():
        for cat in human.category.all():
            if cat.name in categories:
                if human not in people:
                    if moonless:
                        people.append(human)
                    else:
                        if human.precise:
                            people.append(human)


    aspects=[]
    humans_aspects=[]
    humans_names=[]

    for a in planetas[:-1]:
        for b in planetas[planetas.index(a)+1:]:
            aspects.append((a,b))


    for human in people:      
        humans_names.append((human.name, human.surname))
        human_aspects=[]
                        
        for a in planetas[:-1]:
            for b in planetas[planetas.index(a)+1:]:
                                
                con=0
                sex=0
                sqr=0
                trg=0
                ops=0
                
                maping_functions={
                'sun':human.position.sun,
                'moon':human.position.moon,
                'mercury':human.position.mercury,
                'venus':human.position.venus,
                'mars':human.position.mars,
                'jupiter':human.position.jupiter,
                'saturn':human.position.saturn,
                'uranus':human.position.uranus,
                'neptune':human.position.neptune,
                'pluto':human.position.pluto,
                'tnode':human.position.tnode,
                'mnode':human.position.mnode,
                'lilit':human.position.lilit,
                'chiron':human.position.chiron,
                }
                    
                d1=maping_functions[a]
                d2=maping_functions[b]

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
                        
                l1=d2-60-4
                h1=d2-60+4
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
                    
                l2=d2+60-4
                h2=d2+60+4
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


                aspects_any=con+sex+sqr+trg+ops
                if aspects_any:
                    human_aspects.append(1)
                else:
                    human_aspects.append(0)
                    
        humans_aspects.append(human_aspects)



    combos=[]

    for group_num in range(2,len(aspects)+1):
        combo_object=combinations(aspects,group_num)
        combo=list(combo_object)
        combos+=combo


    combos_indexes=[]

    for combo in combos:
        box=[]
        for aspect in combo:
            box.append(aspects.index(aspect))
        combos_indexes.append(box)



    hits_01_aspects=[]    
    for combo in combos_indexes:
        human_hits=[]
        group_hiter=[]
        for i in range(2**(len(combo))):
            temp=[]
            for loop in range(len(combo)):
                combo_combo=[]
                m=2**(len(combo)-loop-1)
                if i >= m:
                    i=i-m
                    temp.append(1)
                else:
                    temp.append(0)
            hits=0
            hum_index=0
            small_group_of_people=[]
            for human in humans_aspects:
                hiter=[]
                for member in combo:
                    if human[member]:
                        hiter.append(1)
                    else:
                        hiter.append(0)
                if temp==hiter:
                    hits+=1
                    small_group_of_people.append(people[hum_index])
                hum_index+=1
            combo_planet_aspects=[]
            for member in combo:
                combo_planet_aspects.append(aspects[member])
            combo_combo=[(hits,temp,combo_planet_aspects,small_group_of_people)]
            hits_01_aspects.append(combo_combo)



    people_len=len(people)
    complete=[]
    for combo in hits_01_aspects:
        prob=1
        for pair in combo[0][2]:
            a=pair[0]
            b=pair[1]
            if combo[0][1][combo[0][2].index(pair)]==1:
                prob*=p_aspects[a][b][5]
            else:
                prob*=(1-p_aspects[a][b][5]) 
        P=0
        for hit in range(combo[0][0],people_len+1):
            p=(prob**(hit)*((1-prob)**(people_len-hit)))*(factorial(people_len))/(factorial(hit)*factorial(people_len-hit))
            P+=p
        combo_t=combo
        P=sigfig.round(P,3)
        combo_t.append(P)
        complete.append(combo_t)

    def sorter(x):
        return x[1]

    complete.sort(key=sorter)

    context={'complete':complete[:results]}
    context['planetas']=planetas
    context['types']=types
    context['planets']=planets
    context['results']=list(range(1,101))
    context['categories']=categories

    return render(request, 'modeling/combined.html', context)
         
    
def redirector(request):
    if request.method =='POST':
        categories = request.POST.getlist('categories')
        if len(categories)==0:
            messages.error(request,'Choose at least one category!')
            return redirect('/')
        category_sum=''
        for category in categories:
            category_sum+='/'+category

        if request.POST.get("complete"):
            url=category_sum+'/complete/'
            return redirect(url)
            
        if request.POST.get("dominant"):
            planet1=request.POST['planet1']
            aspect1=request.POST['aspect1']
            planet2=request.POST['planet2']
            if planet1==planet2:
                messages.error(request,'Astro object cannot be in aspect with itself!')
                return redirect('/')
            
            planet3=request.POST['planet3']
            aspect2=request.POST['aspect2']
            planet4=request.POST['planet4']
            if planet3==planet4:
                messages.error(request,'Astro object cannot be in aspect with itself!')
                return redirect('/')

            if (planet1,planet2) == (planet3,planet4):
                messages.error(request,'Cannot compare identical pairs of astro objects!')
                return redirect('/')
                
            url=category_sum+'/dominant/'+planet1+'/'+aspect1+'/'+planet2+'/'+planet3+'/'+aspect2+'/'+planet4+'/'
            return redirect(url)

        if request.POST.get("combined"):
            planets = request.POST.getlist('planets')
            if len(planets)<3:
                messages.error(request,'Choose at least three astro objects!')
                return redirect('/')
            if len(planets)>5:
                messages.error(request,'Cannot choose more than five astro objects!')
                return redirect('/')
            planet_sum=''
            for planet in planets:
                planet_sum+='/'+planet
            number=request.POST['numbers']
            
            url=category_sum+'/combined/'+number+planet_sum+'/'
            return redirect(url)
        
    
def blanco(request):
    context={}
    context['types']=types
    context['planets']=planets
    context['results']=list(range(1,101))

    return render(request, 'modeling/blanco.html', context)

def handler(request):
    context={}
    context['types']=types
    context['planets']=planets
    context['results']=list(range(1,101))

    return render(request, 'modeling/how_to_use.html', context)

def about(request):
    context={}
    context['types']=types
    context['planets']=planets
    context['results']=list(range(1,101))

    return render(request, 'modeling/about.html', context)
