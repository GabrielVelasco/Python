# import math

# x1 = float(input("Digite o valor x1: "))
# x2 = float(input("Digite o valor x2: "))
# n = int(input("Digite o numero de pontos: "))

# r = (x2 - x1)/(n-1)
# print("Funcao tabelada:")
# for i in range(n):
# 	print("{:.2f}".format(x1), "{:.2f}".format(math.sin(x1)))
# 	x1 = x1 + r

##############################################################
# nome = input("Nome: ")
# diaVenc = int(input("Dia vencimento: "))
# mesVenc = int(input("Mes vencimento: "))
# valor = float(input("Valor fatura: "))

# print("Ola", nome)
# print("A sua fatura com vencimento em", 
# 	diaVenc, "de", mesVenc, "no valor R$", 
# 	valor, "está fechada, o pagamento mínimo é de R$", 
# 	"{:.2f}".format(valor*0.75))

##############################################################
# n1 = int(input("Nota 1: "))
# n2 = int(input("Nota 2: "))
# n3 = int(input("Nota 3: "))
# n4 = int(input("Nota 4: "))

# print((n1+n2+n3+n4)/4)

##############################################################
# seg = int(input("Segundos: "))

# print(int(seg/86400))
# tmp = seg % 86400

# print(int(tmp/3600))
# tmp = tmp % 3600

# print(int(tmp/60))
# tmp = tmp % 60

# print(tmp)

##############################################################
# def primeTest(n):
# 	if n < 2:
# 		return False

# 	if n == 2:
# 		return True

# # procura possiveis divisores de N em (2 .... n-1) 
# 	for i in range(2, n):
# 		if n % i == 0:
# 			return False

# 	return True

# # for i in range(50):
# # 	if primeTest(i):
# # 		print(i)

# def maiorPmenorIgualN(N):
# 	if N < 2:
# 		return False

# 	if N == 2:
# 		print("Ans: ", 2)

# 	for i in range(N, 2, -1):
# 		if primeTest(i):
# 			print("Ans: ", i)
# 			return


# maiorPmenorIgualN(23)

##############################################################
# n1 = int(input("Num: "))
# n2 = int(input("Num: "))
# n3 = int(input("Num: "))

# print(min(n1, n2, n3))
# print(max(n1, n2, n3))

##############################################################
#URI 1272

# n =  int(input())

# for i in range(n):
# 	s = input()
# 	ans = ""
# 	isFirst = True
# 	for j in s:
# 		if (j >= 'a') and (j <= 'z') and isFirst:
# 			ans = ans + j
# 			isFirst = False

# 		elif j == " " and not isFirst:
# 			isFirst = True

# 	print(ans)

##############################################################
# prodCar = 2
# total = 0

# for i in range(prodCar):
#     prec = float(input("digite o preco: "))
#     qntd = int(input("digite a quantidade: "))

#     ttmp = prec * qntd
#     total = total + ttmp

# if total > 200:
#     total = total * 0.95

# if prodCar <= 20:
#     total = total + 15

# print(total)

##############################################################
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1025
# def binary_search(arr, low, high, x):
 
#     # Check base case
#     if high >= low:
 
#         mid = (high + low) // 2
 
#         # If element is present at the middle itself
#         if arr[mid] == x:
#             return mid
 
#         # If element is smaller than mid, then it can only
#         # be present in left subarray
#         elif arr[mid] > x:
#             return binary_search(arr, low, mid - 1, x)
 
#         # Else the element can only be present in right subarray
#         else:
#             return binary_search(arr, mid + 1, high, x)
 
#     else:
#         # Element is not present in the array
#         return -1

# case = 1

# while True:
#     n = int(input())
#     q = int(input())

#     if n == 0 and q == 0:
#         break

#     arr = []
#     for i in range(n):
#         mar = int(input())
#         arr.append(mar)

#     arr.sort()
#     print(f'CASE# {case}')
#     for i in range(q):
#         cons = int(input())
#         ans = binary_search(arr, 0, len(arr), cons)
#         if ans != -1:
#             print(f'{cons} found at {ans+1}')
#         else:
#             print(f'{cons} not found')

#     case = case + 1


##############################################################
# caso a = b menor sera b (indiferente)
# if a < b:
#     m = a 
# else:
#     m = b

#######

# a = [20,3,12,8,13,3,17,9]

# for i in range(len(a)-2):
#     if a[i] < a[i+2]:
#         b = a[i]
#         a[i] = a[i+2]
#         a[i+2] = b

# print(a)

######
# # from math import sqrt

# def raiz_do_menor(n1, n2, n3):
#     menor_numero = min(n1, n2, n3)
#     a = sqrt(menor_numero)
#     return a

# print(raiz_do_menor(4,6,9))


# import math

# def raiz(num1, num2, num3):
#     m = min(num1, num2, num3)
#     r = math.sqrt(m)
#     return r

# print(raiz(9,6,4))



#####

# if 'idade' in {'idade': 18}:
#     print(10, end=' ')
#     print(20, end=' ')
#     if 'a' in 'limão':
#         print(30, end=' ')

# print(40)


# def elemento(pos):
#     if not pos:
#         return 2
#     elif pos > 1:
#         return elemento(pos - 1) + elemento(pos - 2)
#     else:
#         return pos

# print(elemento(3))


##########

# def f(x):
#     x += 2
# x = 10
# f(x)
# x += 10
# print(x + 1)

def f(a, b):
    r = a % b
    while r != 0:
        a = b 
        b = r 
        r = a % b 

    return b

print(f(60, 18))