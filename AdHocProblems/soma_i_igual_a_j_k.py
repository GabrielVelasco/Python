
# ex 6) p1 antiga

def soma_i_igual_a_j_k(V):
	# Complexidade: sempre O(n³)?

	for i in range(0, len(V)):
		for j in range(i+1, len(V)):
			for k in range(j+1, len(V)):

				if V[i] == V[j] + V[k]:
					return (i, j, k)

	V.reverse()

	for i in range(0, len(V)):
		for j in range(i+1, len(V)):
			for k in range(j+1, len(V)):

				if V[i] == V[j] + V[k]:
					return (len(V)-1-i, len(V)-1-j, len(V)-1-k)

	return -1
