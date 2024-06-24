def altera_frase(x,y,z):
    l1=str.split(x)
    l2=list.copy(l1)
    if (y in l1) == True:
        l2[list.index(l1,y)]=str.upper(l1[list.index(l1,y)])
        return str.join(" ",l2)
    else:
        l1.insert(z,y)
        l3= str.join(" ",l1)
        return l3


def insere(lista, n):
    ordem=lista + [n]
    list.sort(ordem)
    return ordem[(list.index(ordem,n)+1):]

def eh_ordenada(lista):
    lista2=list.copy(lista)
    lista3=list.copy(lista)
    if lista==list.sort(lista2):
        return (True,"crescente")
    elif lista==list.reverse(list.sort(lista3)):
        return (True,"decrescente")
    else:
        return (False,"desordenada")
    
    

def acima_da_media(lista):
    ordem=lista
    list.sort(ordem)
    return ordem[(len(ordem)//2):]
