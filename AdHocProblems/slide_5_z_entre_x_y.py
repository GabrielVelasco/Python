# ex slide 5
# 6;19 de manber

# x < z < y, logo...

# condicao de busca == A[0] < z < A[len(A)-1], sendo A[0] < A[len(A)-1]

# ...

# A[1] == A[0]+1 	ou
# A[1] == A[0]	ou
# A[1] == A[0]-1	


def manber_x_meno_y(A):
	# solucao facil
	# O(n)

	i = 1
	while i < len(A):
		print(f'verf pos == {i}')

		if A[i] > A[0] and A[i] < A[len(A) - 1]:
			return i # achou, caso base p/ terminar

		if A[i] < A[0]:
			i += abs(A[0] - A[i])

		i += 1

	return -1
