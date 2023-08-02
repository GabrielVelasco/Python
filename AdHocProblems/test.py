contador = []

V = [...]


# usando mapping?
# O(n + m)?

for i in V: # n
	contador[i] += 1

for j in range(0, len(contador)): # m
	if contador[j] >= ((n/2)+1):
		print(f'V possui elemento maioria == {contador[i]}')
		break

# sem mapping ==> O(n²)?

# 0 <= f(n) <= c*g(n)	
# 'g' limita o cresciemnto de 'f'		

# exemplo algort. O(n*log n)
for i in range(0, n): # O(n)
	for j in range(0, n, j = j*2) # O(lg n)


###############################

# ex slide aula 3

# algoritmo: O(M*n) ?? sendo M qntd de vezes q a funcao vetor_ordenado() foi chamada.
def sort_with_sort5(V):
	n = len(V)
	i = 0

	while not vetor_ordenado(V): # O(n)
		sort5(V, i)	# O(1)
		i += 1

		if i+5 >= n:
			i = 0

# OU

# complex? 
def sort_with_sort5_v2(V): # O( n + (2n/5) * X ) ==> O( (2n/5) * X ) ==> O( (2n/5) * n ) ==> O(n²)
	# forma X grupos, cada um ordenado por sort5(), vetor para cada grupo?, vetor de vetores? == grupos.append([1...5]) ...
	for i in range(0, n-5, i += 6):# O(n)
		sort5(V, i) # O(1)

	# * ...O( (2n/5) * X )?? .... X == len(V) == n??
		# pega o menor de cada grupo e forma um conjunto M com os menores, O(n/5)?
		# a = min(M) // menor valor de M, O(|M| == n/5)?
		# arr_resposta += a
		# remove 'a' do vetor principal/respectivo grupo, O(1) com tecnica de indexacao??

		# se arr_resposta.len == V.len: 
			# break ORDENADO!
	# repete *

	#obs..
	grupos[0] = {....}
	grupos[1] = {....}
	...
	grupos[i][0] == prim element -> menor do grupo
	# qntd grupos?? depende de |V|

	# algoirthm in place == sem mem adicional


###############################

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    print(arr)

    return i

def merge_3_parts(V):
	tam_grup = int(len(V) / 3)
	pivot = partition(V, 0, len(V)-1)

	merge_3_parts(V[0:tam_grup])
	merge_3_parts(V[tam_grup:2*tam_grup])
	merge_3_parts(V[2*tam_grup:len(V)])

	return V

###############################

def bin_search_bimodal(V, l = 0, r = len(V)-1):
	 if r-l == 0:
	 	return V[r]

	 m = (l+r)/2

	 if V[m] > V[m-1] and V[m] > V[m+1]:
	 	return V[m]

	 if V[m] < V[m+1]:
	 	bin_search_bimodal(V, m+1, r)
	 elif V[m] > V[m+1]:
	 	bin_search_bimodal(V, l, m)