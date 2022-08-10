import console
import glob

def ler_pergunta(nome_arquivo):
    per_dicionario = {}
    arq = open(nome_arquivo)
    linhas = arq.readlines()
    per_dicionario["enuciado"] = linhas[0]
    per_dicionario["alternativas"] = linhas[2:6]
    if linhas[-1] != '\n':
        per_dicionario["resposta"] = int(linhas[-1]) # ultimo nao pode ser o '\n'
    else:
        per_dicionario["resposta"] = int(linhas[-2])
    arq.close()
    return per_dicionario 

def exibir_notas():
    print('Printar resultados:')
    arq = open('resultados.txt')
    print(arq.read())
    arq.close()

# INICIO
perguntas = []
arquivos = glob.glob('pergunta*.txt') 
for nome_arquivo in arquivos:
    perguntas.append( ler_pergunta(nome_arquivo) )

while True:
    opc = console.exibir_menu()
    console.apagar_tela()
    certas = 0
    if opc.upper() == 'A':
        arq_res = open('resultados.txt', mode='a+')
        print('Responder questionario:')
        usuario = input('Nome de usuario: ')
        for pergunta in perguntas:
            print(pergunta['enuciado'])
            for i, p in enumerate(pergunta['alternativas']):
                print(f'{i+1} {p}\n')
 
            opc = int(input('Resposta correta: '))
            if opc == pergunta['resposta']:
                certas = certas + 1
        arq_res.write(f'{usuario} {certas}\n')
        arq_res.close()
    elif opc.upper() == "B":
        exibir_notas()
    elif opc.upper() == "S":
        break;
    else:
        print('Opcao invalida')