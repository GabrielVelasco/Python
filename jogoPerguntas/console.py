import os
from time import sleep

TELA1 = '''
==================================
Trabalho 3 − Quiz Retro
==================================

A) Realizar o exame
B) Mostrar notas
S) Sair
'''.strip()

def exibir_menu():
    print(TELA1)
    opcao = input('Digite sua opcao: ')
    return opcao

def apagar_tela():
    print('Aguarde...')
    sleep(3)
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')