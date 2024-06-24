#Laboratorio 9 parte 2

#1
def MxN(matriz,numero):
    resultado=[]
    c=list.copy(matriz)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            resultado=resultado+[matriz[i][j]*numero]
            for k in range(len(resultado)):
                c[i][j]=resultado[k]
    return c


#2
def chamada(telefone,contatos):
    lista=[]
    for i in range(len(contatos)):
        if telefone in contatos[i]:
                list.append(lista,contatos[i])
    return lista

