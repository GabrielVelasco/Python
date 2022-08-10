import os
import sys
import time

TELA1 = '''
===================================
Controle de Entrada de Funcionários
===================================

C) Cadastrar funcionário
B) Buscar Funcionário
R) Registrar entrada/saída
S) Sair
'''.strip()

def apagar_tela():
    """Limpa o conteúdo do console (Windows ou Linux)."""
    if sys.platform == 'linux':
        os.system('clear')
    else:
        os.system('cls')


def ler_funcionarios():
    """Lê a lista de funcionários a partir do arquivo CSV."""
    funcionarios = [] # array de objcs | func = [{'nome': nome, 'email': email}, {...}, {...}]
    if not os.path.exists('funcionarios.csv'):
        return funcionarios

    arq = open('funcionarios.csv')
    while True:
        linha = arq.readline()
        if linha == '':
            break

        partes = linha.split(',')
        nome = partes[0].strip()
        email = partes[1].strip()

        funcionarios.append( {'nome': nome, 'email': email} )

    # arq.readlines() == array strs com todas as linhas
    # with open('funcionarios.csv') as arq:
    #     for i, linha in enumerate(arq.readlines()):
    #         partes = linha.split(',') # cria um array a partir da string, com base no carac ',' | partes == array
    #         nome = partes[0].strip() # strip == apaga espacos das bordas
    #         email = partes[1].strip()
    #         funcionarios.append( {'nome': nome, 'email': email} )

    return funcionarios


def cadastrar_funcionario(funcionarios, nome, email):
    """Cadastra um novo funcionário e salva o arquivo."""

    obj = {}
    obj['nome'] = nome
    obj['email'] = email + '\n'
    funcionarios.append(obj)

    arq = open('funcionarios.csv', mode="a+")
    arq.write(f'{nome},{email}')
    arq.close()

    # funcionarios.append({'nome': nome, 'email': email})
    # with open('funcionarios.csv', 'a') as arq:
    #     arq.write(f'{nome},{email}\n')

    return len(funcionarios)


def exibir_form_cadastro(funcionarios):
    """Exibe e processa o formulário de cadastro"""
    nome = input('Digite o nome do novo funcionário: ')
    email = input('Digite o e-mail do novo funcionário: ')
    print(f'  Nome: {nome}')
    print(f'E-mail: {email}')
    confirmar = input('Está correto? [S/N] ')
    if confirmar.lower() == 's':
        codigo = cadastrar_funcionario(funcionarios, nome, email)
        print(f'Funcionário cadastrado com código {codigo}')
    time.sleep(3)


def exibir_form_busca(funcionarios):
    """Exibe e processa o formulário de busca."""
    nome = input('Digite o nome do funcionário: ')

    for i, funcionario in enumerate(funcionarios):
        if funcionario['nome'].strip().lower() == nome.lower().strip():
            codigo = i + 1
            nome = funcionario['nome']
            email = funcionario['email']
            print('Funcionário Encontrado')
            print('Dados:')
            print('=========================')
            print(f'Código: {codigo}')
            print(f'  Nome: {nome}')
            print(f'E-mail: {email}')
            time.sleep(3)
            return

    print('Funcionário não encontrado!')
    time.sleep(3)


funcionarios = ler_funcionarios()

while True:
    apagar_tela()
    print(TELA1)
    opcao = input('Digite uma opção: ').lower()
    if opcao == 'c':
        exibir_form_cadastro(funcionarios)
    elif opcao == 'b':
        exibir_form_busca(funcionarios)
    elif opcao == 'r':
        # Aula que vem!
        pass
    elif opcao == 's':
        sys.exit()
    else:
        print('Opção inválida!')
        time.sleep(3)