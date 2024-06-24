def msg(media):
    mensagem = 'O aluno foi '
    if(media<5):
        mensagem = mensagem + 'reprovado'
    else:
        mensagem = mensagem + 'aprovado'
    return mensagem    

        
def meia(carteira, idade):
    if carteira == True:
        return True
    else:
        if idade>65 or idade<21:
            return True

def meia2(carteira, idade):
    if carteira == True:
        return True
    elif idade>=65 and idade<=21:
        return True
    else:
        return False

def meia3(carteira, idade):
    if not carteira:
        return idade>=65 or idade<=21
    else:
        False

def meia4(carteira, idade):
    if not carteira:
        return idade>=65 or idade<=21
    else:
        return carteira

def meia5(carteira, idade):
    if not (idade>=65 or idade<=21):
        return carteira
    else:
        return True

def meia6(carteira, idade):
    return idade>=65 or idade<=21 or carteira
