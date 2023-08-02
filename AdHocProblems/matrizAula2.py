# problema da matriz slide aula 2

# O(n²) ou O(n*m)?

def acha_menor_maior_de_linha(linha):
	mai_tmp = men_tmp = linha[0]
	
	for i in range(0, len(linha)):
		if linha[i] > mai_tmp:
			mai_tmp = linha[i]

		elif linha[i] < men_tmp:
			men_tmp = linha[i]

	return (men_tmp, mai_tmp)

def main():
	M = [[11,2,3],
		 [4,5,6],
		 [7,8,9]]

	l = len(M)

	maior_da_linha = 0
	menor_geral = float('+inf')

	for i in range(0, l): # O(n)
		(men_tmp, mai_tmp) = acha_menor_maior_de_linha(M[i]) # O(n)

		if men_tmp < menor_geral:
			menor_geral = men_tmp
			maior_da_linha = mai_tmp

	print(f'Menor de M = {menor_geral} | maior dessa linha = {maior_da_linha}')

main()