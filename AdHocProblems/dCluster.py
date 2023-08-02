# d-Cluster e um subconjunto de inteiros tal que adiferenca entre seus membros (par a par) e menor ouigual a d.  
# Dado um vetor V e o parˆametro d desenvolvaum algoritmo para determinar o maior d-cluster quepode ser obtido de V

def maiorDcluster(V, d):
	# diff par a par menor igual a d
	# maior (tamanho conjunto) d-cluster

	# para cada subconjunto S de V, ordenar V? (evita ter q olhar par-par de S)
	tamMaiorDCluster = 0
	maiorDcluster = []

	for i in range(0, len(V)): 				# n
		for j in range(i, len(V)):			# n
				# testa todos subconjuntos

				S = V[i:j+1]				# n
				tamS = j-i+1
				S.sort()					# n lgn

				maiorDist = abs(S[0] - S[tamS-1])
				if maiorDist <= d:
					# S eh possivel resposta (d-cluster)
					if tamS > tamMaiorDCluster:
						tamMaiorDCluster = tamS
						maiorDcluster = S
				else:
					break

	return (tamMaiorDCluster, maiorDcluster)