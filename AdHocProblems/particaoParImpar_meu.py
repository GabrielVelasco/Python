# Ex slide 5 
# 15 Carnazinga
# algo. in place (sem mem adc) particaoParImpar(A)

# pensamento: os caras q sao iguais ao 'bloco' tenho que trazer eles para a frente desse bloco...
# P I P I
# P P I I

def eh_par(n):
	return n % 2  == 0

def sao_dois_iguais(a, b):
	# True, se a e b tem a mesma 'paridade?'

	if eh_par(a) and eh_par(b):
		return True
	elif not eh_par(a) and not eh_par(b):
		return True

	return False # um eh par outro eh impar

def particaoParImpar(A):
 	# O(n)
 	# sem custo adc de mem

	inicio_bloco = fim_bloco = 0
	n = len(A)

	for i in range(1, n):
		if sao_dois_iguais(A[fim_bloco], A[i]): # A[i] deve ir para a frente do bloco
			tmp = A[fim_bloco + 1]
			A[fim_bloco + 1] = A[i]
			A[i] = tmp

			fim_bloco += 1

	return A