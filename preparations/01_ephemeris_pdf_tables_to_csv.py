import pdfplumber
import re
from collections import namedtuple as nt
import pandas as pd
import os

mesecnik=re.compile(r'(\w+)\s*(\d{4})\s*(\w*)\s+00:00')
moment=re.compile(r'''
([WTFSM])\s*(\d+)\s*
(\d\d?)\s*(\d\d?)\s*(\d\d?)\s*
(\d+)([abcdefghijkl]|\D)[RD]?\s?(\d+)\'(\d+)\s*
(\d+)([abcdefghijkl]|\D)[RD]?\s?(\d+)\s*
(\d+)([abcdefghijkl]|\D)[RD]?\s?(\d+)\s*
(\d+)([abcdefghijkl]|\D)[RD]?\s?(\d+)\s*
(\d+)([abcdefghijkl]|\D)[RD]?\s?(\d+)\s*
(\d+)([abcdefghijkl]|\D)[RD]?\s?(\d+)\s*
(\d+)([abcdefghijkl]|\D)[RD]?\s?(\d+)\s*
(\d+)([abcdefghijkl]|\D)[RD]?\s?(\d+)\s*
(\d+)([abcdefghijkl]|\D)[RD]?\s?(\d+)\s*
(\d+)([abcdefghijkl]|\D)[RD]?\s?(\d+)\s*
(\d+)([abcdefghijkl]|\D)[RD]?\s?(\d+)\s*
(\d+)([abcdefghijkl]|\D)[RD]?\s?(\d+)\s*
(\d+)([abcdefghijkl]|\D)[RD]?\s?(\d+)\s*
(\d+)([abcdefghijkl]|\D)[RD]?\s?(\d+)\s*
''', re.X) 


sign={
'a':'Aries',
'b':'Taurus',
'c':'Gemini',
'd':'Cancer',
'e':'Leo',
'f':'Virgo',
'g':'Libra',
'h':'Scorpio',
'i':'Sagitarius',
'j':'Capricorn',
'k':'Aquarius',
'l':'Pisces'
}


sign_start={
'Aries':0,
'Taurus':30,
'Gemini':60,
'Cancer':90,
'Leo':120,
'Virgo':150,
'Libra':180,
'Scorpio':210,
'Sagitarius':240,
'Capricorn':270,
'Aquarius':300,
'Pisces':330
}


month_num={
'JANUARY':1,
'FEBRUARY':2,
'MARCH':3,
'APRIL':4,
'MAY':5,
'JUNE':6,
'JULY':7,
'AUGUST':8,
'SEPTEMBER':9,
'OCTOBER':10,
'NOVEMBER':11,
'DECEMBER':12,
}

files=[1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750, 1800, 1850, 1900, 1950, 2000]


Line=nt('Line', 'Year Month Day Sun Moon Mercury Venus Mars Jupiter Saturn Uranus Neptune Pluto Tnode Mnode Lilit Chiron')


for years in files:
        
    #file='ae__50_'+str(years)+'.pdf'
    
    big={}   
    checker=0

    with pdfplumber.open(file) as pdf:
        pages=pdf.pages
        for page in pages:
            text=page.extract_text()
            for line in text.split('\n'):
                x=mesecnik.search(line)
                
                if x:
                    if x.group(1)=='JANUARY':
                        checker=1
                        k=0
                        small={
                        'sun':0,
                        'moon':0,
                        'mercury':0,
                        'venus':0,
                        'mars':0,
                        'jupiter':0,
                        'saturn':0,
                        'uranus':0,
                        'neptune':0,
                        'pluto':0,
                        'true':0,
                        'mean':0,
                        'lilit':0,
                        'chiron':0,
                            }
                        year=x.group(2)
                y=moment.search(line)        
                if checker and y:
                    k+=1
                    p=y.group(7)                   
                    if not small['sun'] and p in 'abcdefghijkl':
                        small['sun']=sign[p]
                    p=y.group(11)
                    if not small['moon'] and p in 'abcdefghijkl':
                        small['moon']=sign[p]
                    p=y.group(14)
                    if not small['mercury'] and p in 'abcdefghijkl':
                        small['mercury']=sign[p]
                    p=y.group(17)
                    if not small['venus'] and p in 'abcdefghijkl':
                        small['venus']=sign[p]
                    p=y.group(20)
                    if not small['mars'] and p in 'abcdefghijkl':
                        small['mars']=sign[p]
                    p=y.group(23)
                    if not small['jupiter'] and p in 'abcdefghijkl':
                        small['jupiter']=sign[p]
                    p=y.group(26)
                    if not small['saturn'] and p in 'abcdefghijkl':
                        small['saturn']=sign[p]
                    p=y.group(29)
                    if not small['uranus'] and p in 'abcdefghijkl':
                        small['uranus']=sign[p]
                    p=y.group(32)
                    if not small['neptune'] and p in 'abcdefghijkl':
                        small['neptune']=sign[p]
                    p=y.group(35)
                    if not small['pluto'] and p in 'abcdefghijkl':
                        small['pluto']=sign[p]
                    p=y.group(38)
                    if not small['true'] and p in 'abcdefghijkl':
                        small['true']=sign[p]
                    p=y.group(41)
                    if not small['mean'] and p in 'abcdefghijkl':
                        small['mean']=sign[p]
                    p=y.group(44)
                    if not small['lilit'] and p in 'abcdefghijkl':
                        small['lilit']=sign[p]
                    p=y.group(47)
                    if not small['chiron'] and p in 'abcdefghijkl':
                        small['chiron']=sign[p]
                    if k==4:
                        checker=0
                        big[year]=small

    
    Data=[]
    
    with pdfplumber.open(file) as pdf:
        pages=pdf.pages
        for page in pages:
            text=page.extract_text()
            for line in text.split('\n'):
                x=mesecnik.search(line)
                if x:
                    year=x.group(2)
                    month=x.group(1)
                    
                    if month=='JANUARY':
                    	sun=big[year]['sun']
                    	moon=big[year]['moon']
                    	mercury=big[year]['mercury']
                    	venus=big[year]['venus']
                    	mars=big[year]['mars']
                    	jupiter=big[year]['jupiter']
                    	saturn=big[year]['saturn']
                    	uranus=big[year]['uranus']
                    	neptune=big[year]['neptune']
                    	pluto=big[year]['pluto']
                    	true=big[year]['true']
                    	mean=big[year]['mean']
                    	lilit=big[year]['lilit']
                    	chiron=big[year]['chiron']
                    
                y=moment.search(line)
                if y:
                    day=y.group(2)
                    p_1=y.group(7)
                    if p_1 in 'abcdefghijkl':
                        sun=sign[p_1]
                    sun_deg=round(sign_start[sun]+int(y.group(6))+int(y.group(8))/60,2)
                    p_2=y.group(11)
                    if p_2 in 'abcdefghijkl':
                        moon=sign[p_2]
                    moo_deg=round(sign_start[moon]+int(y.group(10))+int(y.group(12))/60,2)
                    p_3=y.group(14)
                    if p_3 in 'abcdefghijkl':
                        mercury=sign[p_3]
                    mer_deg=round(sign_start[mercury]+int(y.group(13))+int(y.group(15))/60,2)
                    p_4=y.group(17)
                    if p_4 in 'abcdefghijkl':
                        venus=sign[p_4]
                    ven_deg=round(sign_start[venus]+int(y.group(16))+int(y.group(18))/60,2)
                    p_5=y.group(20)
                    if p_5 in 'abcdefghijkl':
                        mars=sign[p_5]
                    mar_deg=round(sign_start[mars]+int(y.group(19))+int(y.group(21))/60,2)
                    p_6=y.group(23)
                    if p_6 in 'abcdefghijkl':
                        jupiter=sign[p_6]
                    jup_deg=round(sign_start[jupiter]+int(y.group(22))+int(y.group(24))/60,2)
                    p_7=y.group(26)
                    if p_7 in 'abcdefghijkl':
                        saturn=sign[p_7]
                    sat_deg=round(sign_start[saturn]+int(y.group(25))+int(y.group(27))/60,2)
                    p_8=y.group(29)
                    if p_8 in 'abcdefghijkl':
                        uranus=sign[p_8]
                    ura_deg=round(sign_start[uranus]+int(y.group(28))+int(y.group(30))/60,2)
                    p_9=y.group(32)
                    if p_9 in 'abcdefghijkl':
                        neptune=sign[p_9]
                    nep_deg=round(sign_start[neptune]+int(y.group(31))+int(y.group(33))/60,2)
                    p_10=y.group(35)
                    if p_10 in 'abcdefghijkl':
                        pluto=sign[p_10]
                    plu_deg=round(sign_start[pluto]+int(y.group(34))+int(y.group(36))/60,2)
                    p_11=y.group(38)
                    if p_11 in 'abcdefghijkl':
                        true=sign[p_11]
                    tru_deg=round(sign_start[true]+int(y.group(37))+int(y.group(39))/60,2)
                    p_12=y.group(41)
                    if p_12 in 'abcdefghijkl':
                        mean=sign[p_12]
                    men_deg=round(sign_start[mean]+int(y.group(40))+int(y.group(42))/60,2)
                    p_13=y.group(44)
                    if p_13 in 'abcdefghijkl':
                        lilit=sign[p_13]
                    lil_deg=round(sign_start[lilit]+int(y.group(43))+int(y.group(45))/60,2)
                    p_14=y.group(47)
                    if p_14 in 'abcdefghijkl':
                        chiron=sign[p_14]
                    chi_deg=round(sign_start[chiron]+int(y.group(46))+int(y.group(48))/60,2)
                    t=(year, month_num[month], day, sun_deg, moo_deg, mer_deg, ven_deg, mar_deg, jup_deg, sat_deg, ura_deg, nep_deg, plu_deg, tru_deg, men_deg, lil_deg, chi_deg)
                    Row=Line(*t)
                    Data.append(Row)

    df=pd.DataFrame(Data)

    if not os.path.isfile('ephemeris.csv'):
        df.to_csv('ephemeris.csv', index=False)
    else:
        df.to_csv('ephemeris.csv', mode = 'a', header=False, index=False)


                  
