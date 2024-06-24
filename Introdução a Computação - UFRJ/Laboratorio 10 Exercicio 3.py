#Laboratorio 10

#Exercicio 3
def busca(setor,func):
    """Essa função agrupa e procura por um setor em uma ficha de funcionarios"""
    """str,list->list"""
    pessoas=[]

    for i in range(len(func)):
        for j in range(len(func[i])):
            if setor == func[i][j]:
                list.append(pessoas,func[i])

    for k in range(len(pessoas)):
        for l in range(len(pessoas[0])):
            if setor in pessoas[k]:
                del pessoas[k][2]

    return pessoas 


def main():

    
    print("----------Procurar funcionarios pelo setor----------")
    setor=input("Digite o setor:\n")

    import ast

    x="..."
    print("Escreva a ficha de um funcionario por vez:\n")
    print("-Quando terminar aperte enter")
    print("O formato da fixa deve ser ['\'Nome'\','\'Registro'\','\'Setor'\','\'Telefone'\']!")
    func=[]
    while x != '':        
        x=input(str.format("Ficha: "))
        if x != '':
            ficha = ast.literal_eval(x)

            ficha = [n.strip() for n in ficha]

        list.append(func,ficha)
                       
    pessoas=busca(setor,func)

    if len(pessoas)>1 and pessoas[-2] == pessoas[-1]:
        del pessoas[-1]

    if pessoas == []:
        print("\nNenhum registro encontrado")

    else:
        print("\nEstes são os funcionarios encontrados nesse setor:\n")

    for i in range(len(pessoas)):
        print(str.format("O(A) funcionario(a) {} de registo ({}) e numero de telefone {} trabalha neste setor",pessoas[i][0],pessoas[i][1],pessoas[i][2]))


main()   


