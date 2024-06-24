#Laboratorio 4 part 1
import math


#Exercicio 1
def concatenacao(x,y):
    """string,string->string"""
    return x+y+y+x

#Exercicio 2
def substitui(s, x, i):
    """string,string,int->string"""
    return s[0:i]+str(x)+s[(i+1):]

#Exercicio 3
def recursiva(s):
    return s[0:math.floor(len(s)/2)]+s+s[(math.floor(len(s)/2)):]

#Exercicio 4
def hashtag(s):
    
    return "#"+s[0:math.floor(len(s)/2)]+"#"+s[math.floor(len(s)/2):]+"#"

#Exercicio 5
def diff_datas(data1,data2):
    d1 = int(data1[0:2])
    m1 = int(data1[3:5])
    a1 = int(data1[6:])
    d2 = int(data2[0:2])
    m2 = int(data2[3:5])
    a2 = int(data2[6:])

    if m2 > m1 and d1 > d2:
        return 365*(a2-a1)+30*(m2-m1)-abs(d2-d1)
    elif m2 < m1 and d1 > d2:
        return 365*(a2-a1)-30*(m1-m2)-(d1-d2)
    elif m2 > m1 and d1 < d2:
        return 365*(a2-a1)+30*(m2-m1)+abs(d2-d1)
    else: 
        return 365*(a2-a1)+30*(m2-m1)+(d2-d1)

def filtra_pares(e1,e2,e3,e4):
    """..."""
    tup=(e1,e2,e3,e4)
    pares = ()

    if tup[0]%2 == 0:
    if tup[1]%2 == 0:
    if tup[2]%2 == 0:    
    if tup[3]%2 == 0:
        return pares + (tup[0],tup[1],tup[2],tup[3])
        
    
    


