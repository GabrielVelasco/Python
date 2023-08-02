# avaliacao polinomios

def resolve_poli(P, x):
	# O(n)

	total = 0
	exp = len(P) - 1

	for i in range(0, len(P)):
		total += (P[i]*(pow(x, exp)))
		exp -= 1

	return total
