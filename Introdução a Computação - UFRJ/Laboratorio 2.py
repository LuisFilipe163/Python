#Exercicio 1b
def media(x,y,z):
    """Essa função calcula a media de 3 numeros x,y e z"""
    """float/int,float/int,float/int -> float/int"""
    return round((x+y+z)/3,1)
    
#Exercicio 1c 
def submedia(x,y,z):
    """Essa função calcula a media de 3 numeros subtraindo o maior entre eles"""
    """float/int,float/int,float/int -> float/int"""
    return media(x,y,z) - max(x,y,z)

#Exercicio 1d
def submedia2(x,y,z):
    """Essa função calcula a media de 3 numeros somando o menor entre eles"""
    """float/int,float/int,float/int -> float/int"""
    return media(x,y,z) + min(x,y,z)

#Exercicio 2a
def delta(a,b,c):
    "Essa função calcula o descriminante(delta) de uma função do segundo grau"""
    """float/int,float/int,float/int -> float/int"""
    return b**2-4*a*c

#Exercicio 2b
def bhaska_pos(a,b,c):
    """Essa função calcula a raiz positiva de uma função do segundo grau usando
a formula de Bhaskara"""
    """float/int,float/int,float/int -> float/int"""
    return (-b + (delta(a,b,c)**1/2))/2*a

#Exercicio 2c
def bhaska_neg(a,b,c):
    """Essa função calcula a raiz negativa de uma função do segundo grau usando
a formula de Bhaskara"""
    """float/int,float/int,float/int -> float/int"""
    return (-b - (delta(a,b,c)**1/2))/2*a

#Exercicio 3b
def num_termos(a1,an,r):
    """Essa função calcula o numero de termos de uma PA"""
    """float/int,float/int -> float/int"""
    return 1 + (an-a1)/r

#Exercicio 3c
def soma_termos(a1s,ans,rs):
    """Essa função calcula a soma dos n termos de uma PA"""
    """float/int,float/int,float/int -> float/int"""
    return (a1s + ans)*(num_termos(a1s,ans,rs))/2

#Exercicio 4a
import math

def hipotenusa(a,b):
    """Essa função calcula a hipotenusa de um triangulo pelo quadrado de seus
catetos"""
    """float/int,float/int -> float/int"""
    return math.hypot(a,b)

#Exercicio 4b
def distanciap(x,y):
    """Essa função calcula a distancia de dois pontos em um plano"""
    """Ultilize x=(x1,y1) e y=(x2,y2)"""
    """float/int,float/int -> float/int"""
    return math.dist (x,y)

#Exercicio 4c
def perimetro_tri(a,b):
    """Essa função calcula o perimetro de um triangulo somando todos seus
lados"""
    """float/int,float/int -> float/int"""
    return hipotenusa(a,b)+a+b

#Função quadratica de um numero
def quadrado(x):
    """Essa função calcula o quadrado de um numero"""
    """float/int -> float/int"""
    return pow(x,2)

#Exercicio 4d
def seno(a):
    """Essa função calcula o seno de um angulo"""
    """float/int -> float"""
    return math.sin(a)

def cosseno(b):
    """Essa função calcula o cosseno de um angulo"""
    """float/int -> float"""
    return math.cos(b)

def soma_ang(a,b):
    """Essa função calcula a soma dos quadrados do seno e do cosseno aonde a e b
são angulos em radianos"""
    """float/int,float/int -> float"""
    return quadrado(seno(a))+ quadrado(cosseno(b))

#Exercicio 4e
def circunferencia(r):
    """Essa função calcula o comprimento de uma circunferencia"""
    """float -> float"""
    return 2*math.pi*r

#Exercicio 5
def Asetor(r,θ=360):
    """Essa função calcula um setor dado em angulos de uma circunferencia"""
    """Caso não informado o angulo sera usado 360º"""
    """float/int,int -> float"""
    return (θ*math.pi*quadrado(r))/360

#Exercicio 6
def quantidade(p,d):
    """Essa função calcula a quantidade de bombons que pedrinho consegue comprar
dependendo do dinheiro(d) e do preço(p)"""
    """int,int -> int"""
    return math.floor(d/p)

#Exercicio 7
def IMC(p,h):
    """Essa função calcula o indice de massa corporal dados peso(p) e altura(h)
de uma pessoa"""
    """float,float -> float"""
    return p/quadrado(h)

#Exercicio 8
def carros(p):
    """Essa função calcula a quantidade necessaria de veiculos para suportar
n pessoas(p)"""
    """int -> int"""
    return math.ceil(p/5)

#Exercicio 9
def distancia(d,r):
    """Essa função calcula quantas voltas a atleta da na pista dados
distancia(d) e raio(r)"""
    """float/int,float/int -> float"""
    return d/circunferencia(r)

#Exercicio 10
def bolos(a,b,c):
    """Essa função calcula a quantidade minuma de bolos que joão pode fazer com
a quantidade de ingredientes (A xicaras de farinha,B ovos e C colheres de sopa
de leite)"""
    """int,int -> int"""
    return min((a/2),(b/3),(c/5))
