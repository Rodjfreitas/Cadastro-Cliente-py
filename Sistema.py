from lib.dados import *
from lib.interacoes import *
from time import sleep

# nomeia o arquivo txt
arquivo = 'relacaofuncionarios.txt'
# verifica se já existe um arquivo com este nome, caso não, cria-se um
if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resposta = menu(['Novo Registro', 'Consultar', 'Sair'])
    if resposta == 1:
        cabeçalho('CADASTRAR FUNCIONÁRIO')
        while True:
            cpf = leiaNumero('CPF: ')
            if not verificarnoArquivo(arquivo, cpf):
                break
            print('\033[31mCPF já cadastrado!\033[m')
        nome = leiaString('Nome Completo: ')
        idade = leiaNumero('Idade: ', 2)
        sexo = leiaOptions('Sexo: ', 'M', 'F')
        endereco = leiaqualquer('Endereço: ')
        cidade = leiaqualquer('Cidade: ')
        estado = leiaqualquer('Estado: ', 2, 2)
        cadastrar(arquivo, cpf, nome, idade, sexo, endereco, cidade, estado)
    elif resposta == 2:
        lerArquivo(arquivo)
    elif resposta == 3:
        cabeçalho('Obrigado por Usar nosso Sistema...\nVolte logo!')
        break
    else:
        cabeçalho('\033[1;31mOpção Inválida\033[m')
    sleep(1)
