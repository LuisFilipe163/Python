#Laboratorio 10

#Exercicio 1
def serie (dados):
    series = 0
    anterior = -1
    contador = 1
    for n in dados:
        if n == anterior:
            contador=contador + 1
        else:
            if contador > 1:
                series=series + 1
            anterior = n
            contador = 1
    if contador > 1:
        series=series + 1
    return series
            

if __name__ == "__main__":
    y = input('defina uma serie: ')
    z = serie(y)
    print (z)


