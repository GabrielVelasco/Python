# problema escada
# de quantas formas eu consigo subir uma escada até o ultimo degrau? 
# sair do '0' e chegar no 'fimEscada'
# subir 1 ou 2 degraus por vez... 0>1 ou 0>2 ... i>i+1 ou i>i+2

################################################
####### QNTDE DE FORMAS DO 'i' ATE O FIM #######
################################################
def climb(degrau_atual, fim_escada, memo):
	# retorna qntd de FORMAS q vou de 'degrau_atual' para 'fim_escada'
	# no max X formas...

	if degrau_atual > fim_escada:	# 0 formas
		return 0

	if degrau_atual == fim_escada:	# pisou no fim da escada
		return 1

	if memo[degrau_atual] != -1:
		# ja foi calculado
		return memo[degrau_atual]
	
	else:
		memo[degrau_atual] = climb(degrau_atual + 1, fim_escada, memo) + climb(degrau_atual + 2, fim_escada, memo)

	return memo[degrau_atual]

def climb_bottom_up(degrau_atual, fim_escada, memo_bttm_up):
	memo_bttm_up[fim_escada] = 1 			# por def, 1 jeito de sair do ultimo e chegar no ultimo

	for i in range(fim_escada-1, -1, -1):	# de fim-1 ... 0
		memo_bttm_up[i] = memo_bttm_up[i+1] + memo_bttm_up[i+2]

	return memo_bttm_up[0]					# memo_bttm[i] == qnts formas de subir de i ... fim

def escadaQntdFormas(qntdDegraus):

	# usando call stack (recurcao) + memoization
	memo = [-1] * qntdDegraus
	return climb(0, qntdDegraus-1, memo)	# nao calcula pra n ≳ 1000

	# usando bottom up
	memo_bttm_up = [0] * (qntdDegraus+1)
	return climb_bottom_up(0, qntdDegraus-1, memo_bttm_up)		# calcula pra n ≳ 3000 ...

##########################################
####### CUSTO MIN DO 'i' ATE O FIM #######
##########################################
def climb_com_custo_min(escada, i):
	# retorna CUSTO MIN de escada[i] ate escada[n-1]
	# i>i+1 ou i>i+2
	# escada == array == ex: [1,2,3,4,5]

	# if memo[i] != -1 .... 

	if i >= len(escada) - 1:	# ultimo degrau
		return escada[-1]

	sub_prob_1 = climb_com_custo_min(escada, i+1)
	sub_prob_2 = climb_com_custo_min(escada, i+2)

	return min(sub_prob_1, sub_prob_2) + escada[i]

def climb_com_custo_min_bottom_up(escada, inicio):
	# escada[i] == custo min de 'i' ate o 'fim'
	n = len(escada)

	for i in range(n-1, -1, -1):
		if i == n-1:
			continue

		if i+2 == n:
			escada[i] = escada[i] + escada[i+1]

		else:
			escada[i] = escada[i] + min(escada[i+1], escada[i+2])

	return escada[inicio]