# transforma a linha = "1 0 1 0 0 ..." em vetor = [1 0 1 0 0 ...]
def transformaEmVetor(linha):
    vetor = []
    for c in linha:
        if c != ' ':
            vetor.append(int(c))

    return vetor


def calcPontuacaoMax(quadMaior, quadMenor, m, n):
    # agora quadMaior e quadMenor são matrizes de inteiros
    # percorrer todos os quadMenor dentro da quadMaior possíveis
    # e calcular a pontuacao de cada um

    contaIguais = 0
    maiorAteAqui = 0
    similaridadeMax = 0
    respostas = ""

    for i in range(0, n-m+1):
        for j in range(0, n-m+1):
            contaIguais = 0

            for k in range(i, i+m):
                for l in range(j, j+m):
                    if quadMaior[k][l] == quadMenor[k-i][l-j]:
                        contaIguais += 1
            
            if contaIguais > maiorAteAqui:
                maiorAteAqui = contaIguais
                similaridadeMax = contaIguais / (m*m)
                respostas = f'({i},{j})'
            
            elif contaIguais == maiorAteAqui and contaIguais != 0:
                linhaMaiorAnterior = int(respostas[1])
                colMaiorAnterior = int(respostas[3])

                # nova linha, coluna está mais superior a esquerda
                if (i+j) <= (linhaMaiorAnterior + colMaiorAnterior):
                    respostas = f'({i},{j})'

    print("Posição: ", end="")
    for p in respostas:
        print(p, end="")

    formatSimilaridade = "{:.2f}".format(similaridadeMax*100)
    print(f'\nSimilaridade máxima: {formatSimilaridade}%')  

def main():
    #  le quadrado maior
    quadMaior = []

    n = int(input())
    for i in range(0, n):
        linha = input()
        vetor = transformaEmVetor(linha)
        quadMaior.append(vetor)
        
    #  le quadrado menor
    quadMenor = []
    m = int(input())
    for i in range(0, m):
        linha = input()
        vetor = transformaEmVetor(linha)        
        quadMenor.append(vetor)

    calcPontuacaoMax(quadMaior, quadMenor, m, n)            


main()