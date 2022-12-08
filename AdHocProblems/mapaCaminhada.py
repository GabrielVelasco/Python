def printaMatriz(matriz, linhas, colunas):

	for i in range(linhas):
		for j in range(colunas):
			if j != colunas - 1: # enquanto n estiver na ultima coluna
				print(matriz[i][j], end=' ')
			else:
				print(matriz[i][j], end='') # ultima coluna, printa sem o espaco no final
		print()

def preencheMatriz(matriz, numLinhas, numColunas):
	for linha in range(numLinhas):
		matriz.append(['.']*numColunas)

def fimCaminho(instrucao):
	return (instrucao == 'F')

def arvoreEncontrada(instrucao):
	return (instrucao == 'A')

def naoVisitado(posicao):
	return posicao == '.'

def caminhaNorte(matriz, qntdCaminhada, posicaoAtual):
	# Subir na matriz == diminuir o valor da linha

	linhaAtual = posicaoAtual[0]
	colunaAtual = posicaoAtual[1]

	# marcar '+' em cada posicao no caminho
	for linha in range(linhaAtual, linhaAtual-qntdCaminhada-1, -1):
		conteudoPosicao = matriz[linha][colunaAtual]

		if naoVisitado(conteudoPosicao):
			matriz[linha][colunaAtual] = '+'

def caminhaSul(matriz, qntdCaminhada, posicaoAtual):
	# Descer na matriz == aumentar valor da linha
	# marca com '+' de linhaAtual ate linhaAtual+qntdCaminhada

	linhaAtual = posicaoAtual[0]
	colunaAtual = posicaoAtual[1]

	# marcar '+' em cada posicao no caminho
	for linha in range(linhaAtual, linhaAtual+qntdCaminhada+1):
		conteudoPosicao = matriz[linha][colunaAtual]

		if naoVisitado(conteudoPosicao):
			matriz[linha][colunaAtual] = '+'

def caminhaLeste(matriz, qntdCaminhada, posicaoAtual):
	# Ir para direita na matriz == aumentar valor da coluna
	# marca '+' de colunaAtual ate colunaAtual+qntdCaminhada
	# linha fica constante (n se move na linha)

	linhaAtual = posicaoAtual[0]
	colunaAtual = posicaoAtual[1]

	# marcar '+' em cada posicao no caminho
	for coluna in range(colunaAtual, colunaAtual+qntdCaminhada+1):
		conteudoPosicao = matriz[linhaAtual][coluna]

		if naoVisitado(conteudoPosicao):
			matriz[linhaAtual][coluna] = '+'

def caminhaOeste(matriz, qntdCaminhada, posicaoAtual):
	# Ir para esquerda na matriz == diminuir valor da coluna
	# marca '+' de colunaAtual ate colunaAtuasl-qntdCaminhada

	linhaAtual = posicaoAtual[0]
	colunaAtual = posicaoAtual[1]

	# marcar '+' em cada posicao no caminho
	for coluna in range(colunaAtual, colunaAtual-qntdCaminhada-1, -1):
		conteudoPosicao = matriz[linhaAtual][coluna]

		if naoVisitado(conteudoPosicao):
			matriz[linhaAtual][coluna] = '+'

def fazCaminhada(matriz, sentidoCaminhada, qntdCaminhada, posicaoAtual):
	# identificar o sentido da caminhada

	if sentidoCaminhada == 'N':
		caminhaNorte(matriz, qntdCaminhada, posicaoAtual)
		posicaoAtual[0] = posicaoAtual[0] - qntdCaminhada # apenas cordenada da linha se altera

	elif sentidoCaminhada == 'S':
		caminhaSul(matriz, qntdCaminhada, posicaoAtual)
		posicaoAtual[0] = posicaoAtual[0] + qntdCaminhada
	
	elif sentidoCaminhada == 'L':
		caminhaLeste(matriz, qntdCaminhada, posicaoAtual)
		posicaoAtual[1] = posicaoAtual[1] + qntdCaminhada
	
	else:
		caminhaOeste(matriz, qntdCaminhada, posicaoAtual)
		posicaoAtual[1] = posicaoAtual[1] - qntdCaminhada

	# funcao que traça a caminhada na matriz de acordo com o sentido e quantidade

def marcaPosicaoAtual(matriz, posicaoAtual):
	# marca posAtual na matriz com '#'

	linhaAtual = posicaoAtual[0]
	colunaAtual = posicaoAtual[1]

	matriz[linhaAtual][colunaAtual] = '#'

def main():
	# contruindo a matriz (lista de listas)
	linhasColunas = input().split(); # le numero de linhas e colunas em uma linha
	numLinhas = int(linhasColunas[0])
	numColunas = int(linhasColunas[1])

	# ['.']*10 => resulta em uma lista de 10 '.' = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']

	matriz = []
	preencheMatriz(matriz, numLinhas, numColunas)
	posicaoAtual = [int(x) for x in input().split()] # posicaoInicial[0] == i | posicaoInicial[1] == j

	while True:
		novaInstrucao = input().split() # le string com 'N/S/L/O k' ou 'A' ou 'F'

		if fimCaminho(novaInstrucao[0]):
			break

		elif arvoreEncontrada(novaInstrucao[0]):
			marcaPosicaoAtual(matriz, posicaoAtual)

		else:
			# temos instrucao do tipo 'X N' sendo X = sentido e N = unidades a caminhar nesse sentido
			sentidoCaminhada = novaInstrucao[0]
			qntdCaminhada = int(novaInstrucao[1])
			fazCaminhada(matriz, sentidoCaminhada, qntdCaminhada, posicaoAtual)


	printaMatriz(matriz, numLinhas, numColunas)

main()