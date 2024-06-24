#Laboratorio 8 parte 2

#Exercicio 1a
def somatorio(n):
    """Essa função retorna o somatorio da função em questão"""
    """int->float"""
    soma=0
    for i in range(0,n):
        soma=soma+(((-1)**n)/(2*n+1))
    return soma


#Exercicio 1b

    

#Exercicio 2
def contatinhosApp(contatos,palavra):
    """Essa função procura um nome em uma lista de contato e retorna os resultados encontrados"""
    """list,str->list"""
    lista=[]
    minusculo = str.lower(palavra)
    for i in range(0,len(contatos)):
        if minusculo in str.lower(contatos[i][0]):
            list.append(lista,contatos[i])
    return lista

def main():

    print("Procurar funcionarios pelo setor")
    palavra=input("Digite o setor: \n")
    contatos=input("Digite a fixa dos funcionarios:\n")

    lista=contatinhosApp(contatos,palavra)

    print("Resultados encontrados:")
    print(str.format("O funcionario {} tranalha no setor {}",lista,palavra))

main()
                         
