dic = {}

while True:
    modalidade = input("Digite o nome da modalidade ou sair: ")
    if modalidade == "sair" or modalidade == "Sair":
        break

    medOuro = input("Informe o país associado à medalha de Ouro: ")
    if dic.get(medOuro) == None: # se pais lido n existir no dicionario
        dic[medOuro] = {"ouro": 0, "prata" :0, "bronze": 0, "total": 0} # cria

    dic[medOuro]["ouro"] += 1 # incrementa
    dic[medOuro]["total"] += 1

    medPrata = input("Informe o país associado à medalha de Prata: ")
    if dic.get(medPrata) == None: # se pais n existir
        dic[medPrata] = {"ouro": 0, "prata" :0, "bronze": 0, "total": 0} # cria

    dic[medPrata]["prata"] += 1
    dic[medPrata]["total"] += 1

    medBronze = input("Informe o país associado à medalha de Bronze: ")
    if dic.get(medBronze) == None: # se pais n existir
        dic[medBronze] = {"ouro": 0, "prata" :0, "bronze": 0, "total": 0} # cria

    dic[medBronze]["bronze"] += 1
    dic[medBronze]["total"] += 1

print("Sumário: ")
for x in dic:
    if x == "ROC":
        continue
    print(x, ':', "Ouro =", dic[x]["ouro"], ", Prata =", dic[x]["prata"], ", Bronze =", dic[x]["bronze"], "Total =", dic[x]["total"])