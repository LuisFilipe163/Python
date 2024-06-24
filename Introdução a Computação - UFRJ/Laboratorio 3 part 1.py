#Exercicio 1
def absoluto(x):
    """Essa função retorna o modulo de um numero"""
    """int/float->int/float"""
    if x>0:
        return x
    else:
        return x*-1
    
    
#Exercicio 2
def delta(a,b,c):
    "Essa função calcula o descriminante(delta) de uma função do segundo grau"""
    """float/int,float/int,float/int -> float/int"""
    return b**2-4*a*c

def bhaskara(a,b,c):
    "Essa função calcula as raizes de uma equação do segundo grau"""
    """float/int,float/int,float/int -> float/int,float/int"""
    return (-b + (delta(a,b,c))**1/2)/2*a,(-b - delta(a,b,c)**1/2)/2*a

#Exercicio 3
def mensagem(texto,n):
    """Retorna um texto multiplicado por n vezes"""
    """string,int -> string"""
    return str(texto)*int(n)

#Exercicio 4
def data(d,m,a):
    """Retorna a data com padrão DD/MM/AAAA"""
    """int,int,int -> string"""
    return str(d)+'/'+str(m)+'/'+str(a)

#Exercicio 5
def equação(x):
    """Essa formula o resultado com base na equação apresentada na questão"""
    """int/float -> int/float"""
    if x<2:
        return x
    elif x>=2 and x<=3.5:
        return 2
    elif x>3.5 and x<=5:
        return 3
    else:
        return x**2-10*x+28

#Exercício 6a
def inss(s1):
    """Essa função calcula a taxa de desconto de imposto de INSS"""
    """int/float -> int/float"""
    if s1 <= 2000:
        return 6/100*s1
    elif s1 > 2000 and s1 <= 3000:
        return 8/100*s1
    else:
        return 10/100*s1

#Exercício 6b
def IR(s2):
    """Essa função calcula a taxa de desconto de IR"""
    """int/float -> int/float"""
    if s2 <= 2500:
        return 11/100*s2
    elif s2 > 2500 and s2 <= 5000:
        return 15/100*s2
    else:
        return 22/100*s2

#Exercício 6c
def saldoL(s3):
    """Essa função calcula o salario liquido"""
    """int/float -> int/float"""
    return s3 - (inss(s3)+IR(s3))

    




