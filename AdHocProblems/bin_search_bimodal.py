def bin_search_bimodal(V, l, r): # T(n)
	 if r-l == 0:
	 	return V[r]

	 m = int((l+r)/2)

	 if V[m] > V[m-1] and V[m] > V[m+1]:
	 	return V[m]

	 if V[m] < V[m+1]:
	 	return bin_search_bimodal(V, m+1, r) # T(n/2)
	 elif V[m] > V[m+1]:
	 	return bin_search_bimodal(V, l, m) # T(n/2)

# T(n) = 2*T(n/2) + 1 ==> O(n*lgn), chutando n*lgn