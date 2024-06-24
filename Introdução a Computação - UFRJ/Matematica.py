import math

def hipotenusada(a,b):
    return math.hypot(a,b)
def distancia(p,q):
    return math.dist (p,q)

def quadrado(x):
    """Essa função calcula o quadrado de um numero"""
    return pow(x,2)

def raiz(y):
    """Essa função calcula a raiz quadrada de um numero"""
    return math.sqrt(y)

def somaquadrados(a,b):
    """Essa função calcula a soma dos quadrados de dois numeros"""
    return quadrado(a)+quadrado(b)
