def forca (palavra):       
    acertos=0
    erros=0
    letras=[]
    erradas=[]
    acerto=[]
    tentativa=6
    if " " in palavra:
        k=str.split(palavra)
        for i in range(len(k)):
            k[i]=(len(k[i])*"-")
            j=str.join(" ",k)
        print(j) 
    else:
        print("-"*len(palavra))

    
        
    if palavra in palavras[0:5]:
        print("\n--------------------------")
        print("#País da África")
        print("--------------------------\n")

    if palavra in palavras[5:10]:
        print("\n--------------------------------")
        print("#País da América do Norte ou Central")
        print("--------------------------------\n")

    if palavra in palavras[10:15]:
        print("\n-------------------------------")
        print("#País da América do Sul")
        print("-------------------------------\n")

    if palavra in palavras[15:20]:
        print("\n------------------------------")
        print("#País da Ásia")
        print("------------------------------\n")

    if palavra in palavras[20:25]:
        print("\n--------------------------------------")
        print("#País da Europa")
        print("--------------------------------------\n")

    if palavra in palavras[25:30]:
        print("\n------------------------------------")
        print("#País da Oceania")
        print("------------------------------------\n")

    if " " in palavra:        
        list.append(letras," ")
        acertos=acertos + str.count(palavra," ")
        list.append(acerto," ")
    else:        
        acertos=0
  
    while tentativa>0:        
            
        print("_________________________________________________")
        x = input("\nAdivinhe uma letra ou digite um dos comandos: ")
        print("_________________________________________________\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

        if str.lower(x) == "novamente":
            print("------------------------------")
            print("Foi sorteada outro país")
            print("------------------------------\n")
            print("Seu novo país é:\n")
            l = palavras[randint(0,29)]
            forca(l)

        if x == "":
            print("\n******************************************")
            print("****Digite uma letra ou comando apenas****")
            print("******************************************\n")
       
        if str.lower(x) == "chutar":
            k=input("Chute um país: ")
            if str.lower(k) == palavra:
                acertos=acertos+len(palavra)
                print ("\n\n\n\t    VENCEU NO CHUTE!!!\n")
                break                
            else:
                print ("\n\n\n\t      VOCÊ PERDEU!\n")
                print("*******************************************\n")
                print(f"Seu personagem era: ->{str.upper(palavra)}<-")                
                tentativa=tentativa*0
                break 

        if x == " ":
            acertos= acertos -1
                                       
        if str.lower(x) in palavra:
            list.append(letras,str.lower(x))
            acertos=acertos + str.count(palavra,str.lower(x))
            list.append(acerto,str.lower(x))

        if " " in palavra:
            list.append(letras," ")            

        if list.count(acerto,str.lower(x))>1 and x != "" and x != " ":
            print("\n*******************************************")
            print("Essa letra esta na palavra mas ja foi usada")
            print("*******************************************\n")
            list.remove(acertadas,str.lower(x))
            acertos=acertos - str.count(palavra,str.lower(x))

               
        if str.lower(x) not in palavra and str.lower(x) != palavra:
            tentativa=tentativa-1
            erros=erros+1
            list.append(erradas,str.lower(x))        

        if list.count(erradas,str.lower(x))>1 and x != "" and x != " ":
            print("\n*********************************************")
            print("Essa letra não esta na palavra e ja foi usada")
            print("*********************************************\n")
            list.remove(erradas,x)
            erros=erros-1
            tentativa=tentativa +1
            

        if len(x)>1 and str.lower(x)!="chutar" and str.lower(x) != palavra:
            print("-Apenas uma letra por vez ou tente um chute-\n")
            erros=erros-1
            tentativa=tentativa +1
            list.remove(erradas,x)        

        if str.lower(x) == palavra:
            print("-Tente chutar ou apenas digite letra por letra-\n")
            tentativa=tentativa +1
            

        if erros == 5:
            print("\n--------------ULTIMA TENTATIVA!!!--------------\n")            
        
        for letra in palavra:
            if letra in letras:
                print(letra,end='')
            else:
                print('-',end='')

        if "chutar" in erradas:
            list.remove(erradas,"chutar")   
               
        print ('')
        errosl=str.join("-",erradas)
        print(f"\n*Quantidade de chances: {6-erros}")
        print(f"\n*Letras usadas que não pertencem a palavra: {errosl}")         
        
        if acertos == len(palavra):
             break
        
    if str.lower(x) != "chutar":
        if acertos == len(palavra):
            print ("\n\n\n\t  PARABÉNS, VOCÊ GANHOU!")
        else:
            print("\n*******************************************")
            print(f"Seu país era: ->{str.upper(palavra)}<-")
            print("*******************************************")
            print ("\n\n\n\tNÃO DEU, TENTE NOVAMENTE!")              

    print("\n-------------------------------------------")
    x = (input('Para jogar de novo digite sim: '))
    print("-------------------------------------------\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    if str.lower(x) == 'sim':
        print("\n-> Existem 3 comandos disponiveis para o jogo que são:\n")
        print("     -'chutar':caso deseje chutar uma palavra")
        print("       obs1: caso erre o chute o jogo acaba\n")
        print("     -'novamente':caso deseje jogar novamente com outra palavra\n")
        print("\nSeu país é:\n")
        y = palavras[(randint(0,29))]
        forca(y)
    else:
        print('\nAté a proxima')
        

    
if __name__ == "__main__":

    from random import randint

    print("\t\t\t\t\tJogo da Forca\t\t\t\t\t\t")
    print("\n-> Existem 3 comandos disponiveis para o jogo que são:\n")
    print("     -'chutar':caso deseje chutar uma palavra")
    print("       obs1: caso erre o chute o jogo acaba\n")
    print("     -'novamente':caso deseje jogar novamente com outra palavra\n")
    print("Seu país é:\n\n")
    
    with open('palavras.txt', 'r') as f:
        palavras = [linha.strip() for linha in f.readlines()]
               
    y = palavras[(randint(0,29))]
    forca(y)
   

