import datetime

def idaded (dia,mes,ano):
    diad= datetime.datetime.now().day
    mesd= datetime.datetime.now().month
    anod= datetime.datetime.now().year
    if diad==dia and mesd==mes:
        return str(anod - ano)+ ' anos. Parabens pelo aniversario'
    elif ((mes<mesd) or mes==mesd and dia<diad):
        return str(anod-ano)+' anos'
    else:
        return str(anod-ano-1)+' anos'

def soma(a,b):
    a= ~result
    b= x1
    return ~result+x1
