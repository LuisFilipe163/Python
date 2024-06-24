def main():

    import ast

    for i in range(2):
        x=input(str.format("Escreva a ficha do {}º funcionario",i+1))

    l = ast.literal_eval(x)

    l = [i.strip() for i in l]

    k=[]

    for j in range(2):
        list.append(k,l)

    print(k)

main()
