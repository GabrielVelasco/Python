# NAO FUNCIONA

V = [5,2,8,1,3,6,23,7,9,10,11]
k = 6
faltam = k-1

n = len(V)

for i in range(0, n-k):-
	for u in range(1, n-i):
		ultimo_encontrado = V[i]
		faltam = k-1
		s = []
		s.append(ultimo_encontrado)

		for j in range(i+u, n):
			if ultimo_encontrado <= V[j]:
				faltam = faltam - 1
				ultimo_encontrado = V[j]
				s.append(ultimo_encontrado)

				if faltam == 0:
					break

		if faltam == 0:
			break
	
	if faltam == 0:
		break


if len(s) == k:
	print(f'Existe S em V == {s}')
else:
	print('Não existe S em V')