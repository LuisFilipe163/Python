#Exercicio 1
def area(x,y):
    """Essa função calcula a area de um retangulo dado os seus 2 lado x e y"""
    return x*y

#Exercicio 2
def area_cubo(x):
    """Essa função calcula a area de um quadrado dado um lado x"""
    return x**2

#Exercicio 3
def anel(r1,r2):
    """Essa função calcula a diferença de dois raios de circunferencias
concentricas que formam um anel e considera pi=3,14"""
    return 3,14*r1**2 - 3,14*r2**2

#Exercicio 4
def media(x,y):
    """Essa função calcula a media de dois numeros inteiros x e y"""
    return (x+y)/2

#Exercicio 5
def grau2(a,b,c,x):
    """Essa função calcula o valor de y em uma função do segundo grau ax²+bx+c"""
    return a*x**2+b*x+c

#Exercicio 6
def mediap(x,y,a,b):
    """A e B são os pesos da media e x e y são os numeros que seram calculados"""
    return (x*a+y*b)/(a+b)

#Exercicio 7
def formula(n,q):
    """Essa função calcula erro de aproximação da pg aonde n é o numero de termos
e q a razão"""
    return 1/(1-q) - 1*((q**n)-1)/(q-1)

#Exercicio 8
def gorjeta(x):
    """Essa função calcula o valor de 10% da gorjeta de uma conta"""
    return x*(10/100)

#Exercicio 9
def conta(valor,gorjeta):
    """Essa função calcula o valor total da conta do restaurante"""
    return valor*(gorjeta/100)+valor

#Exercicio 10
def saldo(inicial,juros,meses):
    """Essa função calcula o saldo final de uma conta ultilizando a porcentagem
dos juros representada como x/100"""
    return inicial*(1+juros*meses)

#Exercicio 11
def arrasto(L,Vb,Vr):
    """Essa função calcula o arrasto que o braco sofre usando a
largura do rio,velocidade do barco e velociade da correnteza"""
    return Vr*L/Vb
