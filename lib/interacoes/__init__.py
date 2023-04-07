def leiaString(msg):
    """
    --> Impede que seja digitado um valor numérico
    :param msg: a mensagem que o usuário irá receber como pergunta
    :return: retorna a string digitada pelo usuário
    """
    while True:
        valor = input(msg).strip().upper()
        if valor.isalnum() == True:
            print('\033[31mInválido. Digite novamente!\033[m')
            continue
        return valor


def leiaqualquer(msg, qtdmin=1, qtdmax=50):
    """
    --> Permite que seja digitado qualquer valor no input
    :param msg: a mensagem que o usuário irá receber como pergunta
    :param qtdmin: a quantidade mínima de caracteres permitidas para resposta
    :param qtdmax: a quantidade máxima de caracteres permitidas para resposta
    :return: retorna a string digitada pelo usuário com a quantidade de caracteres configurados
    """
    while True:
        try:
            valor = input(msg).strip().upper()
            if len(valor) < qtdmin or len(valor) > qtdmax:
                print('\033[31mInválido. Digite novamente.\033[m')
                continue
        except (ValueError, TypeError, KeyboardInterrupt):
            print(
                '\033[31mO programa apresentou um erro inesperado. Tente Novamente.\033[m')
            continue
        else:
            return valor


def leiaNumero(msg, qtd=11):
    """
    --> Permite a digitação apenas de caracteres numéricos e limita a quantidade de caracteres
    :param msg: a mensagem que o usuário irá receber como pergunta
    :param qtd: a quantidade de caracteres aceitas para digitação
    :return: retorna a string 'numérica' digitada pelo usuário com a quantidade de caracteres definidas
    """
    while True:
        try:
            cpf = input(msg)
            if len(cpf) != qtd or cpf.isnumeric() == False:
                print('\033[31mInválido. Digite novamente.\033[m')
                continue
        except (ValueError, TypeError, KeyboardInterrupt):
            print('\033[31mVocê não digitou um valor válido. Repita!\033[m')
        else:
            return cpf


def leiaOptions(msg, opt1, opt2):
    """
    --> Permite fazer uma input com retorno de apenas um caractere definido previamente
    :param msg: a mensagem que o usuário irá receber como pergunta
    :param opt1: primeira opção que pode ser selecionada
    :param opt2: segunda opção que pode ser selecionada
    :return: retorna o valor digitado de uma string definida previamente
    """
    while True:
        try:
            valor = input(f'{msg} [{opt1}/{opt2}]: ').strip().upper()[0]
            if valor in [opt1, opt2]:
                return valor
            print('\033[31mInválido. Digite novamente.\033[m')
        except (ValueError, TypeError, KeyboardInterrupt):
            print('\033[31mInválido. Digite novamente.\033[m')
            continue


