#Laboratorio 4 part 2

#Exercicio 1
def SIGA(boletim):
    """Essa função retorna a situação de um aluno em realção a suas notas com a mensagem de aprovação ou reprovação"""
    """string,int,int,int->tuple"""
    b=tuple(boletim)
    media=(b[1]+b[2]+b[3])/3
    if media>=7:
        return str(b[0]),media,'Aprovado','Parabens'
    elif media>5 and media<7:
        return str(b[0]),media,'Aprovado'
    else:
        return str(b[0]),media,'Reprovado'

#Exercicio 2
import math

def quadrante(angulo,graus):
    """Essa função retorna em qual quadrante dado angulo se encontra tanto em radianos quanto em graus"""
    """int,bool->int"""
    if graus==False:
        angulo=math.degrees(angulo)
    if angulo<0:
        angulo=abs(360+angulo)
    if graus==True and angulo<=90 or angulo%360<=90:
        return 1
    elif graus==True and angulo<=180 or angulo%360<=180:
        return 2
    elif graus==True and angulo<=270 or angulo%360<=270:
        return 3
    else:
        return 4
        
