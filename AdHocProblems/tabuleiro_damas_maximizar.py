# [5, 3, 2, 4]
# [7, 5, 7, 2]
# [8, 1, 2, 6]
# [6, 2, 8, 3] n=4

tabuleiro = [[5, 13, 2, 14], 
             [7, 5, 7, 2], 
             [6, 8, 2, 6], 
             [6, 2, 8, 3]] #37, 2? certo

def resolve_damas_maxi(tabuleiro, n, i, j):
    # retorna valor do caminho com mais pontuacao, partindo de [i][j] ate o topo (considerando restricoes de movimento)

    # Caso base
    if j == -1 or j == n:
        return 0

    if i == 0:
        return tabuleiro[0][j]
        
    max_diagonal_esq = resolve_damas_maxi(tabuleiro, n, i-1, j-1)
    max_cima = resolve_damas_maxi(tabuleiro, n, i-1, j)
    max_diagonal_dir = resolve_damas_maxi(tabuleiro, n, i-1, j+1)

    return max(max_diagonal_esq, max_cima, max_diagonal_dir) + tabuleiro[i][j]

def resolve_damas_maxi_memo(tabuleiro, n, i, j, memo):
    # retorna valor do caminho com mais pontuacao, partindo de [i][j] ate o topo (considerando restricoes de movimento)

    # Caso base
    if j == -1 or j == n:
        return 0
    
    if memo[i][j] != -1:    # partindo da pos [i][j] ja foi calculado
        return memo[i][j]

    if i == 0:
        return tabuleiro[0][j]
        
    max_diagonal_esq = resolve_damas_maxi(tabuleiro, n, i-1, j-1)
    max_cima = resolve_damas_maxi(tabuleiro, n, i-1, j)
    max_diagonal_dir = resolve_damas_maxi(tabuleiro, n, i-1, j+1)

    memo[i][j] = max(max_diagonal_esq, max_cima, max_diagonal_dir) + tabuleiro[i][j]    # valor partindo da pos [i][j]

    return memo[i][j]

def solve_no_memo():
    n = len(tabuleiro)
    ultima_linha = n-1

    valor_maximo = 0
    col_pos_inicio = 0
    for col in range(n):
        solucao_parcial = resolve_damas_maxi(tabuleiro, n, ultima_linha, col)   # partindo de tab[ultima_linha][col]
        valor_maximo = max(solucao_parcial, valor_maximo)

        if valor_maximo == solucao_parcial:
            col_pos_inicio = col

    return valor_maximo, col_pos_inicio

def solve_with_memo():
    n = len(tabuleiro)
    ultima_linha = n-1

    memo = [[-1] * n for _ in range(n)] # cria matriz memorizacao

    valor_maximo = 0
    col_pos_inicio = 0
    for col in range(n):
        solucao_parcial = resolve_damas_maxi_memo(tabuleiro, n, ultima_linha, col, memo)   # partindo de tab[ultima_linha][col]
        valor_maximo = max(solucao_parcial, valor_maximo)

        if valor_maximo == solucao_parcial:
            col_pos_inicio = col

    return valor_maximo, col_pos_inicio

def solve_with_pd():
    # O(N²)

    n = len(tabuleiro)
    ultima_linha = n-1
    valor_maximo = 0
    col_pos_inicio = 0

    for i in range(n):
        for j in range(n):
            if i == 0:
                continue

            # calc o max(max_diagonal_esq, max_cima, max_diagonal_dir)...
            # soma com o valor de [i][j]
            val_max = 0
            if j-1 == -1:
                # n tem diagonal esquerda
                val_cima = tabuleiro[i-1][j]
                val_diagonal_dir = tabuleiro[i-1][j+1]
                
                val_max = max(val_cima, val_diagonal_dir)
            
            elif j+1 == n:
                # n tem diagonal direita
                val_cima = tabuleiro[i-1][j]
                val_diagonal_esq = tabuleiro[i-1][j-1]

                val_max = max(val_cima, val_diagonal_esq)

            else:
                # to no meio...
                val_diagonal_esq = tabuleiro[i-1][j-1]
                val_cima = tabuleiro[i-1][j]
                val_diagonal_dir = tabuleiro[i-1][j+1]

                val_max = max(val_diagonal_esq, val_cima, val_diagonal_dir)

            tabuleiro[i][j] = val_max + tabuleiro[i][j]

    # Ate aq, tab[i][j] == melhor resposta saindo de [i][j]
    for j in range(n):
        val_da_celula = tabuleiro[ultima_linha][j]
        valor_maximo = max(valor_maximo, val_da_celula)

        if valor_maximo == val_da_celula:
            col_pos_inicio = j

    return valor_maximo, col_pos_inicio