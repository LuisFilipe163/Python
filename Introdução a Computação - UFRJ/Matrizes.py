def a(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j]=float(input("Valor de a("+str(i)+","+str(j)+") = )")

def imprime(matriz):
    for linha in matriz:
        print("|",end="\t")
        for aij in linha:
            print(str.format("{:.2f}" , aij),end="\t")
        print("|")

def cria(linhas,colunas):
    matriz=[]
    for i in range(linhas):
        list.append(matriz,colunas*[0])
    return matriz
                            
