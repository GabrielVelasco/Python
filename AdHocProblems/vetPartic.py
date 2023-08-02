def vetPartc(V, k):
    n = len(V)
    p = 0		# ponteiro inicio bloco dos iguais a k
    q = n - 1	# ponteiro final bloco dos iguais a k
    
    # coloca p no lugar correto
    while p < n and V[p] < k:
        p += 1

    # coloca q no lugar correto
    while q >= 0 and V[q] > k:
        q -= 1
    
    # ate aq: V[0...p-1] < k && V[q+1...fim] > K
    # oq fazer de V[p...q]
    i = p
    while i <= q:
        if V[i] < k:
            V[p], V[i] = V[i], V[p]
            p += 1
            i += 1
        elif V[i] > k:
            V[q], V[i] = V[i], V[q]
            q -= 1
        else:
            i += 1
    
    return p-1, q+1, V