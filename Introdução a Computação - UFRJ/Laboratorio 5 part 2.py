def SignoC(ano):
    """Essa função retorna o signo chines com base no ano de nascimento"""
    """int->string"""
    signo=ano%12
    l=["Macaco","Galo","Cão","Porco","Rato","Boi","Tigre","Coelho","Dragão","Serpente","Cavalo","Carneiro"]
    return l[signo]
