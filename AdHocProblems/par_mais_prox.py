# pseudo cod
# ParMaixProximo(V):
#    Vx = V ordenado no eixo x 
#    Vy = V ordenado no eixo y 
   
#    m = INFINITO

#    Para i de 0 a n-1:
#		d1 = d(Vx[i],Vx[i+1]) # dist no 1D?d
# 		d2 = d(Vy[i],Vy[i+1])

#       m = menor(m, d1, d2)

#    retorna m

# Para tal algoritmo, produzir uma entrada V tal que o o valor retornado esteja errado. Destacar o erro no algoritmo ^
# algoritmo certo?

# erro: 

import math
import random
import time

def cria_vetor_de_pts_tamanho(n):
	# peguei do cod do teams
	# cria array de pts (x, y) == tupla com cordenadas aleatorias

    prob = []
    x=-1
    for i in range(n):
        x += random.randint(5,20)
        y = random.randint(0,100000000)
        prob.append((x,y))

    return prob

def dist1D(a, b):
	return abs(b - a)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def par_mais_prox_incorreto(V):
	# V == [(x1, y1), (x2, y2), ... (Xn, Yn)] == lista de tuplas

	# extraindo eixo X
	X = []
	for i in range(len(V)):
		X.append(V[i][0])

	# extraindo eixo Y
	Y = []
	for i in range(len(V)):
		Y.append(V[i][1])

	# Até aqui... Pi = (X[i], Y[i]) ==> ponto i

	# ordenar os eixos c/ Insertion Sort
	X = insertion_sort(X)
	Y = insertion_sort(Y)

	# aqui baguncou tudo... Pi = (X[i], Y[i]) eh um pt que provavelmente n existia no inicio
	# seguindo o codigo que ta no teams...

	menor_dist = float('inf')
	par_errado = ()

	for i in range(len(V) - 1):
		d1 = dist1D(X[i], X[i+1])
		d2 = dist1D(Y[i], Y[i+1])
		menor_tmp = min(d1, d2)
		if menor_tmp < menor_dist:
			menor_dist = menor_tmp
			par_errado = (X[i], Y[i])

	return (menor_dist, par_errado)

##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################

def dist(p1,p2):
	# pi == tupla --> ponto == (p[0], p[1])

    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2) # p[0] ==  cord X | p[1] == cord y

def parProximoDireto(V,i,f):
	# V == [ (x1, y1), (x2, y2) ,... ] == lista de tuplas

    d=dist(V[i],V[i+1])
    par=(V[i],V[i+1])
    for j in range(i,f-1):
        for k in range(j+1,f):
            if dist(V[j],V[k])<d:
                d= dist(V[j],V[k])
                par=(V[j],V[k]) # nova menor dist

    return (d,par) # retorna a dist e o respectivo par com essa dist

def parProximoDC(V,i,f):
    if f-i<1000: # qntd de elemntos em V?
        return parProximoDireto(V,i,f)

    # dividindo
    m = int((f+i)/2)

    # conquistando
    r1 = parProximoDC(V,i,m)
    r2 = parProximoDC(V,m+1,f)

    # combinnando
    delta = r1[0]
    par = r1[1]
    if r2[0]<r1[0]:
        delta = r2[0]
        par = r2[1]

    faixa = []

    for k in range(i,f):
        if V[k][0] > V[m][0]-delta and V[k][0] < V[m][0]+delta: # linha do meio - delta	&& 	linha do meio + delta
            faixa.append(V[k]) # add os pts do intervalo [m - delta ... m + delta] ao array faixa

    #faixa = sorted(faixa, key= lambda x:x[1])
    # usar o sorted (implementado em C) contra um merge sort em python nao e muito honesto

    faixa = merge_sort(faixa)
    for k in range(len(faixa)-1):
        for l in range(1,8):
            if k+l < len(faixa):
                if dist(faixa[k],faixa[k+l]) < delta: # nova menor distancia?
                    delta = dist(faixa[k],faixa[k+l]) 
                    par = (faixa[k],faixa[k+l])

    return (delta,par) # resp final



def merge_sort(V):
	# ordena pro eixo Y?

    if len(V)<=1:
        return V
    if len(V)==2:
        if V[0][1]<=V[1][1]:
            return V
        return [V[1],V[0]]
        
    m = int(len(V)/2)
    s1 = merge_sort(V[:m])
    s2 = merge_sort(V[m:])
    return merge(s1,s2)
    
    
def merge(V1,V2):
    i1=0
    i2=0
    ret = [[0,0]]*(len(V1)+len(V2))
    j=0
    while (i1<len(V1) and i2<len(V2)):
        if V1[i1][1]<V2[i2][1]:
            ret[j]=V1[i1]
            i1+=1
            j+=1
        else:
            ret[j]=V2[i2]
            i2+=1
            j+=1
            
    while (i1<len(V1)):
        ret[j]=V1[i1]
        i1+=1
        j+=1
    while (i2<len(V2)):
        ret[j]=V2[i2]
        j+=1
        i2+=1
    return ret


def parProximoDCPig(V,i,f):
    if f-i<1000:
        s = sorted(V[i:f], key= lambda x:x[1])
        t = parProximoDireto(V,i,f)
        return (t[0],t[1],s)
    m = int((f+i)/2)
    gm = V[m][0]
    r1 = parProximoDCPig(V,i,m)
    r2 = parProximoDCPig(V,m+1,f)
    delta = r1[0]
    par = r1[1]
    if r2[0]<r1[0]:
        delta = r2[0]
        par = r2[1]
    ordenado = merge(r1[2],r2[2])
    lmin = gm-delta
    lmax = gm+delta
    
    for k in range(len(ordenado)-9):
        ok =  ordenado[k]
        if ok[0]>lmin and ok[0]<lmax:
            for l in range(1,8):
                if dist(ok,ordenado[k+l])<delta:
                    delta = dist(ok,ordenado[k+l])
                    par = (ok,ordenado[k+l])
                    lmin = gm-delta
                    lmax = gm+delta
    return (delta,par,ordenado)

