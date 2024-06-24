def busca(setor,lista_funcionarios):
    pessoas=[]
    for i in range(len(lista_funcionarios)):
        for j in range(len(lista_funcionarios[i])):
            if setor == lista_funcionarios[i][j]:
                list.append(pessoas,lista_funcionarios[i])

    for k in range(len(pessoas)):
        for l in range(len(pessoas[0])):
            if setor in pessoas[k]:
                del pessoas[k][2]

    return pessoas 


def main():

    print("----------Procurar funcionarios pelo setor----------")
    setor=input("Digite o setor:\n")
    lista_funcionarios=[['Adalberto Ferreira', '566', 'Contabilidade', '(21)84564-5248'], ['Juliana Vasconcelos', '465', 'RH', '(21)3555-4552'], ['Flavia Amorim', '565', 'Contabilidade', '(21)2134-4845']]

    pessoas=busca(setor,lista_funcionarios)

    if pessoas == []:
        print("\nNenhum registro encontrado")

    else:
        print("\nEstes são os funcionario encontrados nesse setor:\n")

    for i in range(len(pessoas)):                
        print(str.format("{}",pessoas[i]))


main()    


