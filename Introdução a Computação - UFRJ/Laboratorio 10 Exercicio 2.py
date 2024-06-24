#Laboratorio 10

#Exercicio 2
def igual1(a,b,c):
    """Essa função retorna a area do trapezio e os numeros escolhidos"""
    """int,int,int->list"""
    i1=[((a+b)*c)/2,[a,b,c]]
    if a<b:
        return i1
    else:
        print("\n(a precisa ser menor que b)")
       
def igual2(a,b,c):
    """Essa função retorna a multiplicação de cada numero escolhido por ele mesmos e os proprio numeros"""
    """int,int,int->list"""
    i2=[a*a,b*b,c*c,[a,b,c]]
    if a<b:
        return i2
    else:
        print("\n(a precisa ser menor que b)")

def igual3(a,b,c):
    """Essa função retorna a soma aritimetica dos numeros escolhidos"""
    """int,int,int->list"""
    i3=[(a+b+c)/3,[a,b,c]]
    if a<b:
        return i3
    else:
        print("\n(a precisa ser menor que b)")

def igual4(a,b,c):
    """Essa função retorna a soma de todos os numeros entre a e b mas pulando de a+c ate chegar em b"""
    """int,int,int->list"""
    if a<b:
        soma=list(range(a,b+1,c))
        return [sum(soma),[a,b,c]]
    else:
        print("\n(a precisa ser menor que b)")


def main():

    print("------Codigo de '\'i'\'------\n")

    i=int(input("Digite um valor de 1 a 4 para i:"))

    if i>4:
        print("\nAPENAS NUMEROS ENTRE 1 E 4 PARA I")
        

    print("\n-Defina um valor para as incognitas")
    
    a=int(input("\nDigite um valor para a:"))
    b=int(input("Digite um valor para b:"))
    c=int(input("Digite um valor para c:"))

    
    if i == 1:
        i1=igual1(a,b,c)
        print(i1)

    if i == 2:
        i2=igual2(a,b,c)
        print(i2)

    if i == 3:
        i3=igual3(a,b,c)
        print(i3)

    if i == 4:
        i4=igual4(a,b,c)
        print(i4)

    
main()
    



    
    
