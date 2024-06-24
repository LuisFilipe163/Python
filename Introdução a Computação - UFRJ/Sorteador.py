from random import randint

def dados(n,x):
    jogadas=[]
    while len(jogadas)<n:
        rolagem = randint(1,x)
        list.append(jogadas,rolagem)

    return jogadas

def main():

    print("----------- Programa Sorteador -----------")
    n=int(input("Quantos numeros deverao ser sorteados?\n"))
    x=int(input("Ate que numero pode ser sorteado (De 1 a ...)? \n"))

    jogadas = dados(n,x)

    print("---------- Resultado do sorteio ---------")
    print(str.format("Foram sorteados {} numeros", len(jogadas)))

    for i in range(len(jogadas)):
        print(str.format("O {}o numero soteado foi: {}", i+1,jogadas[i]))

main()
