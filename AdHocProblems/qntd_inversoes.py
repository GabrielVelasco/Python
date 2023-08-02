# problema da inversao slide aula 2
arr = [3,2,1,4, 1,6]
inversoes = 0
n = len(arr)

for i in range(0, n):
	for j in range(i+1, n):
		if arr[i] > arr[j]:
			inversoes = inversoes + 1

print(f'Num de inversoes = {inversoes}')



