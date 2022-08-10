import random

perguntas = [
    {
        'enunciado': 'De quem é a famosa frase “Penso, logo existo”?',
        'alternativas': [
            'Platão',
            'Galileu Galilei',
            '_Descartes',
            'Sócrates',
            'Francis Bacon'         
        ]
    },
    {
        'enunciado': 'De onde é a invenção do chuveiro elétrico?',
        'alternativas': [
            'França',
            'Inglaterra',
            '_Brasil',
            'Austrália',
            'Itália'
        ]
    },
    {
        'enunciado': 'Quais o menor e o maior país do mundo?',
        'alternativas': [
            '_Vaticano e Rússia',
            'Nauru e China',
            'Mônaco e Canadá',
            'Malta e Estados Unidos',
            'São Marino e Índia'

        ]
    },
    {
        'enunciado': 'Qual o nome do presidente do Brasil que ficou conhecido como Jango?',
        'alternativas': [
            'Jânio Quadros',
            'Jacinto Anjos',
            'Getúlio Vargas',
            'João Figueiredo',
            '_João Goulart'
        ]
    },
    {
        'enunciado': 'Qual o grupo em que todas as palavras foram escritas corretamente?',
        'alternativas': [

            'Asterístico, beneficiente, meteorologia, entertido',
            '_Asterisco, beneficente, meteorologia, entretido',
            'Asterisco, beneficente, metereologia, entretido',
            'Asterístico, beneficiente, metereologia, entretido',
            'Asterisco, beneficiente, metereologia, entretido'
        ]
    },
    {
        'enunciado': 'Qual o livro mais vendido no mundo a seguir à Bíblia?',
        'alternativas': [
            'O Senhor dos Anéis',
            '_Dom Quixote',
            'O Pequeno Príncipe',
            'Ela, a Feiticeira',
            'Um Conto de Duas Cidades'
        ]
    },
    {
        'enunciado': 'Quantas casas decimais tem o número pi?',
        'alternativas': [
            'Duas',
            'Centenas',
            '_Infinitas',
            'Vinte',
            'Milhares'
        ]
    },
    {
        'enunciado': 'Atualmente, quantos elementos químicos a tabela periódica possui?',
        'alternativas': [
            '113',
            '109',
            '108',
            '_118',
            '92'
        ]
    },
    {
        'enunciado': 'Quais os países que têm a maior e a menor expectativa de vida do mundo?',
        'alternativas': [
            '_Japão e Serra Leoa',
            'Austrália e Afeganistão',
            'Itália e Chade',
            'Brasil e Congo',
            'Estados Unidos e Angola'
        ]
    },
    {
        'enunciado': 'Qual a altura da rede de vôlei nos jogos masculino e feminino?',
        'alternativas': [
            '2,4 para ambos',
            '2,5 m e 2,0 m',
            '1,8 m e 1,5 m',
            '2,45 m e 2,15 m',
            '_2,43 m e 2,24 m'
        ]
    },
]

random.shuffle(perguntas)

print('==================')
print('Jogo das Perguntas')
print('==================')

acertos = 0

for i in range(len(perguntas)):
    # Enunciado
    enunciado = perguntas[i]['enunciado']
    print(f'{i + 1}) {enunciado}')
    # Alternativas
    alternativas = perguntas[i]['alternativas']
    random.shuffle(alternativas)
    for j in range(len(alternativas)):
        letra = chr(ord('a') + j)
        alternativa = alternativas[j]
        if alternativa[0] == '_':
            resposta_correta = letra
            alternativa = alternativa[1:]
        print(f'  {letra}    {alternativa}')
    resposta_informada = input('Qual é a opção correta? ')
    resposta_informada = resposta_informada.strip().lower()
    if resposta_correta == resposta_informada:
        acertos += 1  # mesma coisa que acertos = acertos + 1
        print('Certa resposta!\n')
    else:
        print('Resposta está errada!\n')
    if input('Pressione S para continuar...').strip().lower() != 's':
        break
print('\n')
percentual = acertos / len(perguntas) * 100
print('Você tirou ' + str(percentual) + '%')