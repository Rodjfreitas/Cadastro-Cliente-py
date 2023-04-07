def leiaInt(msg):
    """
    --> Realiza um input esperando receber um número inteiro
    :param msg: a mensagem que o usuário irá receber como pergunta
    :return: retorna um int digitado pelo usuário
    """
    while True:
        try:
            valor = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mInválido. Digite novamente.\033[m')
        except (KeyboardInterrupt):
            print('\033[1;31mUsuário não digitou valor.\033[m')
            valor = 0
            return valor
        else:
            return valor


def leiaFloat(msg):
    """
    --> Realiza um input esperando receber um número real
    :param msg: a mensagem que o usuário irá receber como pergunta
    :return: retorna um float digitado pelo usuário
    """
    while True:
        try:
            valor = float(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mInválido. Digite novamente.\033[m')
        except (KeyboardInterrupt):
            print('\033[1;31mUsuário não digitou valor.\033[m')
            valor = 0
            return valor
        else:
            return valor


def linha(tam=42):
    return '=' * tam


def cabeçalho(msg, tam=42):
    print(linha(tam))
    print(msg.center(tam))
    print(linha(tam))


def menu(lista):
    """
    --> Imprime conteúdo de uma lista em forma de opções
    :param lista: conteúdo de uma lista que será apresentado no mural de opções
    :return: retorna o valor referente a opção desejada
    """
    cabeçalho('SISTEMA DE CLIENTES v1.0')
    c = 1
    for item in lista:
        print(f'\033[33m{c:>4}\033[m - \033[34m{item:<20}\033[m')
        c += 1
    print(linha())
    opcao = leiaInt('\033[1;32mOpção: \033[m')
    return opcao


def arquivoExiste(nome):
    """
    --> Realiza uma verificação de existencia de arquivo
    :param nome: nome do arquivo
    :return: False para arquivo inexistente, True para arquivo existente
    """
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    return True


def criarArquivo(nome):
    """
    --> Cria um novo arquivo
    :param nome: nome do arquivo
    :return: não possui
    """
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('\033[1;32mHouve um ERRO na criação do arquivo.\033[m')
    else:
        print(f'Arquivo \033[42m{nome}\033[m criado com sucesso.')


def verificarnoArquivo(nome, dado):
    """
    --> Realiza uma verificação de informações no arquivo
    :param nome: nome do arquivo
    :param dado: informação que deseja buscar no arquivo
    :return: False para dado inexistente no arquivo, True para dado existente no arquivo
    """
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo.')
    else:
        for linha in a:
            dados = linha.split(';')
            if dados[0] == dado:
                return True
        return False
    finally:
        a.close()


def cadastrar(arq, dado1, dado2, dado3, dado4, dado5, dado6, dado7):
    try:
        a = open(arq, 'at')
    except:
        print('\033[31mHouve um ERRO na abertura do arquivo\033[m')
    else:
        try:
            a.write(f'{dado1};{dado2};{dado3};{dado4};{dado5};{dado6};{dado7}\n')
        except:
            print('\033[31mHouve um ERRO na hora de escrever os dados\033[m')
        else:
            print(f'\033[32mNovo Registro de {dado2} adicionado.\033[m')


def lerArquivo(nome):
    try:
        a = open(nome)
    except:
        print('\033[31mErro ao ler arquivo.\033[m')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        print(
            f'\033[32;44m{"CPF":<13}{"NOME":<30}{"IDADE":<8}{"SEXO":<8}{"ENDEREÇO":<45}{"CIDADE":<25}{"UF":<6}\033[m')
        for linha in a:
            dado = linha.split(';')
            dado[6] = dado[6].replace('\n', '')
            print(
                f'{dado[0]:<13}{dado[1]:<30}{dado[2]:<8}{dado[3]:<8}{dado[4]:<45}{dado[5]:<25}{dado[6]:<3}')
    finally:
        a.close()
