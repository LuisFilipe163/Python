def velocidade_esperada (v0, a, t):
    '''função que, dadas a velocidade inicial do veículo, a aceleração e o instante,
    devolve a velocidade esperada naquele instante, com até 2 casas decimais.
    float, float, float --> float'''
    return round(v0 + a*t,2)

def calcula_esperadas (v0, a, tempos):
    '''função que, dadas a velocidade inicial do veículo, a aceleração e uma lista de instantes,
    devolve uma lista com as velocidades esperadas em cada instante da lista.
    float, float, list --> list'''
    esperadas = []
    for i in range(len(tempos)):
        list.append(esperadas, velocidade_esperada (v0, a, tempos[i]))
    return esperadas

def erro_do_experimento (v_esperada, v_observada):
    '''função que, dadas a velocidade esperada e a observada, devolve a porcentagem de
    erro da observação, com até 2 casas decimais.
    float, float --> float'''
    return round((v_esperada - v_observada)*100/v_esperada, 2)

def erro_ao_longo_do_tempo(v_esperadas, v_observadas, tempos):
    ''' função que, dadas três listas contendo respectivamente as velocidades esperadas em cada instante,
    as velocidades observadas em cada instante e  os instantes considerados, devolve uma lista contendo
    os erros entre os valores observados e os esperados, pareados com os instantes correspondentes.
    ASSUME QUE as 3 listas recebidas possuem o mesmo tamanho.
    list, list --> list'''
    erros = []
    for i in range(len(v_esperadas)):
        erro = (erro_do_experimento (v_esperadas[i], v_observadas[i]), tempos[i])
        list.append (erros, erro)
    return erros

def main():

    velocidade_inicial = 10.00
    aceleracao= 0.50
    tempos = [0.00, 1.00, 2.00, 5.00, 10.00, 15.00, 30.00]
    velocidades_esperadas = calcula_esperadas(velocidade_inicial, aceleraacao, tempos)

    velocidades_observadas = [10.00, 11.10, 12.00, 13.05, 14.00, 15.76, 16.00]

    erros = erro_ao_longo_do_tempo(velocidade_esperadas, velocidades_observadas, tempos)

    return erros
