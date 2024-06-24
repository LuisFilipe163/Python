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
    ''' programa principal para realização dos cálculos do laboratório de cinemática'''

    # dados do experimento
    # pedir para o usuário fornecer os dados do experimento
	
    #Fornecimento da velocidade inicial
    velocidade_inicial_string = input('Velocidade inicial (m/s): ')
    velocidade_inicial = float(velocidade_inicial_string)
	
    #Fornecimento da aceleração
    #INCLUA A SEGUIR O CODIGO NECESSARIO PARA PEDIR E RECEBER DO USUARIO
    # O VALOR DA ACELERACAO DO VEICULO NO EXPERIMENTO

    #Fornecimento da lista de instantes a serem considerados no experimento
    tempos = []
    tempo_str = '...'
    print('Tempos (Digite enter quando terminar):')
    while tempo_str != '':
        tempo_str = input(' - Tempo (s): ')
        if tempo_str:
            list.append(tempos, float(tempo_str))

    # Calcula a velocidade esperada
    velocidades_esperadas = calcula_esperadas(velocidade_inicial, aceleracao, tempos)
    qtd_velocidades_esperadas = len(velocidades_esperadas)

    # resultados observados
    # pedir para o usuário fornecer os resultados observados	
	
    velocidades_observadas = []
    print(str.format('Velocidades observadas (Espera-se {} velocidades):', qtd_velocidades_esperadas))
    i = 0
    while i < len(tempos):
	# * INCLUA A SEGUIR O CODIGO NECESSARIO PARA PEDIR E RECEBER DO USUARIO
        # O VALOR DAS VELOCIDADES OBSERVADAS DO VEICULO NO EXPERIMENTO
        # * PEDIR UMA VELOCIDADE DE CADA VEZ
        # * GARANTIR QUE O USUARIO FORNECE A QUANTIDADE CERTA DE DADOS 

    # cálculo dos erros
    erros = erro_ao_longo_do_tempo(velocidades_esperadas, velocidades_observadas, tempos)

    # Saída para o usuário
    strings_velocidades_esperadas = []
    for velocidade in velocidades_esperadas:
        string_velocidade_esperada = str.format('{:8.2f}', velocidade)
        list.append(strings_velocidades_esperadas, string_velocidade_esperada)

    strings_velocidades_observadas = []
    for velocidade in velocidades_observadas:
        string_velocidade_observada = str.format('{:8.2f}', velocidade)
        list.append(strings_velocidades_observadas, string_velocidade_observada)

    strings_erros_em_porcentagem = []
    for erro in erros:
        erro_em_porcentagem, tempo = erro
        string_erro_em_porcentagem = str.format('{:7.2f}%', erro_em_porcentagem)
        list.append(strings_erros_em_porcentagem, string_erro_em_porcentagem)

    print(str.format('\n\nComparação de velocidades (v0 = {} m/s; a = {} m/s²):', velocidade_inicial, aceleracao))
    print(str.format(' - Velocidades esperadas  (m/s): [{}]', str.join(', ', strings_velocidades_esperadas)))
    print(str.format(' - Velocidades observadas  (m/s): [{}]', str.join(', ', strings_velocidades_observadas)))
    print(str.format(' - Erros  (%): [{}]', str.join(', ', strings_erros_em_porcentagem)))
    # * CONCLUA A IMPRESSAO DE RESULTADOS COM A IMPRESSAO DAS VELOCIDADES OBSERVADAS E OS ERROS
    # MANTENDO O FORMATO ANTERIOR

main()
