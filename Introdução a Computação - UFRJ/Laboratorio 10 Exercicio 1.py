#Laboratorio 10

#Exercicio 1
def serie(sequencia):
    """Essa função retorna a quantidade de vezes que um numero se repede na sequencia em uma serie"""
    """int->int"""
    s = 0
    anterior = -1
    contador = 1
    for n in sequencia:
        if n == anterior:
            contador= contador + 1
        else:
            if contador > 1:
                s=s + 1
            anterior = n
            contador = 1
    if contador > 1:
        s=s + 1
    return s
            

def main():

    print("------Contador de numeros consecutivos iguais------\n")

    sequencia = input('Defina uma serie: ')
    s=serie(sequencia)
    print(str.format("\n\nO numeros de repetições em sequencia é: {}",s))
    
main()
