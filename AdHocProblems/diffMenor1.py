# achar j, tal que V[j] = z

def diff(V, i, f, z):
	if f < i:
		return -1

	m = int((i+f)/2)

	if V[m] == z:
		return m

	d = abs(V[m] - z)

	j1 = diff(V, i, m-d, z)
	if j1 == -1:					# reposta nao esta na parte da esquerda
		return diff(V, m+d, f, z)
	else:
		return j1