def menor_conj_intervalos(pontos_reta):
	inicio_intervalos = []
	n = len(pontos_reta)

	for i in range(0, n):
		# pergunta: a cada iteracao, devo INICIAR um novo intervalo?

		if i == 0:
			inicio_intervalos.append(pontos_reta[i])	# definido primeiro intervalo
			fim_ultimo_interv = pontos_reta[i] + 1

		elif pontos_reta[i] > fim_ultimo_interv:
			inicio_intervalos.append(pontos_reta[i])	# inicia um novo intervalo em ponto_reta[i]
			fim_ultimo_interv = pontos_reta[i] + 1

	return inicio_intervalos