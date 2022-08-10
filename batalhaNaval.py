
# converte para uma cordenada na matriz: A == 0, B == 1 ...
def converteCordenadaLinha(palpiteLinhaColuna):
    linhaPalpite = palpiteLinhaColuna[0]

    return int(ord(linhaPalpite) - 65)

def converteCordenadaColuna(palpiteLinhaColuna):
    colunaPalpite = int(palpiteLinhaColuna[1])

    return colunaPalpite - 1

# esta entre A e Z?
def ehCaractere(c):
    return c >= 'A' and c <= 'Z'

# transforma a linha = ". . . A A A" em vetor = [., ., ., A, A, A, A] de caracteres
# para contruir a matriz
def transformaLinha(linha, contaPecasNavio):
    vetor = []
    for c in linha:
        if c != ' ':
            vetor.append(c)
            if ehCaractere(c):
                if c in contaPecasNavio:
                    contaPecasNavio[c] += 1
                else:
                    contaPecasNavio[c] = 1

    return vetor

def main():
    # conta qnts peças cada navio tem
    # Ex: se contaPecasNavio['X'] = 3 -> navio X tem 3 peças
    contaPecasNavio = {}

    tabuleiro = []
    linhasTabuleiro = 10
    for i in range(0, linhasTabuleiro):
        linha = input()
        linhaDoTabuleiro = transformaLinha(linha, contaPecasNavio)
        tabuleiro.append(linhaDoTabuleiro)
    
    palpites = input()
    for i in range(0, int(palpites)):
        palpiteLinhaColua = input()
        l = converteCordenadaLinha(palpiteLinhaColua.split(' '))
        c = converteCordenadaColuna(palpiteLinhaColua.split(' '))

        localAtingido = tabuleiro[l][c]
        tabuleiro[l][c] = '.';

        if localAtingido == '.':
            print("agua")
        elif localAtingido in contaPecasNavio: 
            contaPecasNavio[localAtingido] -= 1 # navio atingido tem menos uma parte
            if contaPecasNavio[localAtingido] == 0:
                print(f'afundou o navio {localAtingido}')
            else:
                print(f'atingiu o navio {localAtingido}')
            
if __name__ == '__main__':
    main()