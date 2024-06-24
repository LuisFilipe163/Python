from random import *

def dados(quantidade):
    y=int(input("\n\nQuantos lados tem o dado\n-->"))
    w=input("\n\nSomar/Multiplicar/Nada[s,m,n]\n-->")
    numeros_sorteados=[]

    if quantidade == 0:
        print("\n---------------------------------\n")
        print(str.format("{}d0 = 0",y))
        print("\n---------------------------------\n")
   

#Sem Soma nos dados
    if w == "n":

    #Mais de 1 dado        
        if quantidade >1:        
            for i in range(quantidade):
                list.append(numeros_sorteados,randint(1,y))
                numeros_sorteados2 = list.copy(numeros_sorteados)
            for j in range(len(numeros_sorteados)):
                numeros_sorteados2[j] = str(numeros_sorteados[j])
            todos_numeros = str.join("+",numeros_sorteados2)
            print("\n---------------------------------\n")
            print(str.format("{}d{} = ({}) = {}",quantidade,y,todos_numeros,sum(numeros_sorteados)))
            print(str.format("\n{} Critico(s)",list.count(numeros_sorteados,y)))
            print(str.format("\n{} Erro(s) Critico(s)",list.count(numeros_sorteados,1)))
            print("\n---------------------------------\n")

    #Apenas 1 dado            
        if quantidade == 1:
            list.append(numeros_sorteados,randint(1,y))
            print("\n---------------------------------\n")
            if numeros_sorteados[0] == y:
                print("CRITICO!\n")                
                print(str.format("d{} = {}\n",y,numeros_sorteados[0]))
                print("\n---------------------------------\n")
            if numeros_sorteados[0] == 1:
                print("ERRO CRITICO!\n")                
                print(str.format("d{} = {}",y,numeros_sorteados[0]))
                print("\n---------------------------------\n")
            if numeros_sorteados[0] > 1 and numeros_sorteados[0] <y:
                print(str.format("d{} = {}",y,numeros_sorteados[0]))
                print("\n---------------------------------\n")

#Com Somo nos dados            
    if w == "s":

    #Com Soma Positiva nos dados
        z=int(input("\n\nSomado/Multiplicado a quanto\n-->"))
        if z > 0:

        #Mais de 1 dado 
            if quantidade >1:
                for i in range(quantidade):
                    list.append(numeros_sorteados,randint(1,y))
                    numeros_sorteados2 = list.copy(numeros_sorteados)
                for j in range(len(numeros_sorteados)):
                    numeros_sorteados2[j] = str(numeros_sorteados[j])
                todos_numeros = str.join("+",numeros_sorteados2)
                print("\n---------------------------------\n")
                print(str.format("{}d{} + {} = ({}) + {} = {}",quantidade,y,z,todos_numeros,z,sum(numeros_sorteados)+z))
                print(str.format("\n{} Critico(s)",list.count(numeros_sorteados,y)))
                print(str.format("\n{} Erro(s) Critico(s)",list.count(numeros_sorteados,1)))
                print("\n---------------------------------\n")

        #Apenas 1 dado
            if quantidade == 1:
                
                list.append(numeros_sorteados,randint(1,y))
                print("\n---------------------------------\n")
                if numeros_sorteados[0] == y:
                    print("CRITICO!\n")                
                    print(str.format("d{} + {} = ({}) + {} = {}",y,z,y,z,numeros_sorteados[0]+z))
                    print("\n---------------------------------\n")
                if numeros_sorteados[0] == 1:
                    print("ERRO CRITICO!\n")                
                    print(str.format("d{} + {} = (1) + {} = {}",y,z,z,numeros_sorteados[0]+z))
                    print("\n---------------------------------\n")
                if numeros_sorteados[0] > 1 and numeros_sorteados[0] <y:
                    print(str.format("d{} + {} = ({}) + {} = {}",y,z,numeros_sorteados[0],z,numeros_sorteados[0]+z))
                    print("\n---------------------------------\n")

    #Com Soma Negativa nos Dados
        if z < 0:

        #Mais de 1 dado 
            if quantidade >1:
                for i in range(quantidade):
                    list.append(numeros_sorteados,randint(1,y))
                    numeros_sorteados2 = list.copy(numeros_sorteados)
                for j in range(len(numeros_sorteados)):
                    numeros_sorteados2[j] = str(numeros_sorteados[j])
                todos_numeros = str.join("+",numeros_sorteados2)
                print("\n---------------------------------\n")
                print(str.format("{}d{} - {} = ({}) - {} = {}",quantidade,y,-(z),todos_numeros,-(z),sum(numeros_sorteados)+z))
                print(str.format("\n{} Critico(s)",list.count(numeros_sorteados,y)))
                print(str.format("\n{} Erro(s) Critico(s)",list.count(numeros_sorteados,1)))
                print("\n---------------------------------\n")

        #Apenas 1 dado
            if quantidade == 1:
                
                list.append(numeros_sorteados,randint(1,y))
                print("\n---------------------------------\n")
                if numeros_sorteados[0] == y:
                    print("CRITICO!\n")                
                    print(str.format("d{} - {} = ({}) - {} = {}",y,-(z),y,-(z),numeros_sorteados[0]+z))
                    print("\n---------------------------------\n")
                if numeros_sorteados[0] == 1:
                    print("ERRO CRITICO!\n")                
                    print(str.format("d{} - {} = (1) - {} = {}",y,-(z),-(z),numeros_sorteados[0]+z))
                    print("\n---------------------------------\n")
                if numeros_sorteados[0] > 1 and numeros_sorteados[0] <y:
                    print(str.format("d{} - {} = ({}) - {} = {}",y,-(z),numeros_sorteados[0],-(z),numeros_sorteados[0] + z))
                    print("\n---------------------------------\n")

#Com Multiplicação nos dados
    if w == "m":

        #Mais de 1 dado
        z=int(input("\n\nSomado/Multiplicado a quanto\n-->"))
        if quantidade >1:
            for i in range(quantidade):
                list.append(numeros_sorteados,randint(1,y))
                numeros_sorteados2 = list.copy(numeros_sorteados)
            for j in range(len(numeros_sorteados)):
                numeros_sorteados2[j] = str(numeros_sorteados[j])
            todos_numeros = str.join("+",numeros_sorteados2)
            print("\n---------------------------------\n")
            print(str.format("{}d{} * {} = ({}) * {} = {}",quantidade,y,z,todos_numeros,z,sum(numeros_sorteados)*z))
            print(str.format("\n{} Critico(s)",list.count(numeros_sorteados,y)))
            print(str.format("\n{} Erro(s) Critico(s)",list.count(numeros_sorteados,1)))
            print("\n---------------------------------\n")

        #Apenas 1 dado
        if quantidade == 1:
                
            list.append(numeros_sorteados,randint(1,y))
            print("\n---------------------------------\n")
            if numeros_sorteados[0] == y:
                print("CRITICO!\n")                
                print(str.format("d{} * {} = ({}) * {} = {}",y,z,y,z,numeros_sorteados[0]*z))
                print("\n---------------------------------\n")
            if numeros_sorteados[0] == 1:
                print("ERRO CRITICO!\n")                
                print(str.format("d{} * {} = (1) * {} = {}",y,z,z,numeros_sorteados[0]*z))
                print("\n---------------------------------\n")
            if numeros_sorteados[0] > 1 and numeros_sorteados[0] <y:
                print(str.format("d{} * {} = ({}) * {} = {}",y,z,numeros_sorteados[0],z,numeros_sorteados[0]*z))
                print("\n---------------------------------\n")

        
            
#Repetir Rolagem
    print("\n-Role Novamente")
    x=int(input("\nQuantos dados\n-->"))    
    dados(x)

if __name__ == "__main__":

    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=Rolador de dados=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    x=int(input("\n\nQuantos dados\n-->"))    
    dados(x)
