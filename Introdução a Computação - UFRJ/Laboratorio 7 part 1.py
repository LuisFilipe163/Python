def uppCons(string):
    """Essa função retorna uma frase com todas suas consuantes em letra maiusculas"""
    """string->string"""
    vogais=""
    i=0
    proximo=0
    while proximo<len(string):
        if string[i] in 'bcdfghjklmnpqrstvwxzç':
            vogais=vogais+str.upper(string[i])
        else:
            vogais=vogais+(string[i])
        i=i+1
        proximo=proximo+1
    return vogais
