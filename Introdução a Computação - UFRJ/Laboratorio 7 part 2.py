#Laboratorio 7 Parte 2

#Exercicio 1
import random

def iguais():
    """Essa função retorna a quantidade de vezes que dois dados são lançados e não dão o mesmo numero"""
    """sem entrada"""
    i=0
    while random.randint(1,6) != random.randint(1,6):
        i=i+1
    return i

#Exercicio 2
def busca_contatos(contatos,nome):
    """Essa função retorna todos os contatos iguais ao nome procurado"""
    """list,string->list"""
    i=0
    cont=[]
    indice=0
    name=str.upper(nome)
    while i<=len(contatos):
        if name in str.upper(contatos[indice][0]):
            cont= cont + [contatos[indice]]
        i=i+1
        indice=indice+1
        return cont
        
        
        
