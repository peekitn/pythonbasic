"""
def eh_quadrada(m):
    return len(m) > 0 and all(len(linha) == len(m) for linha in m)
"""
"""
def media_diagonal_principal(m):
    if not eh_quadrada(m):
        raise ValueError("A matriz precisa ser quadrada.")

    n = len(m)
    soma = 0
    for i in range(n):
        soma += m[i][i]
    return soma / n
"""
"""
def diagonal_secundaria_igual(m):
    if not eh_quadrada(m):
        raise ValueError("A matriz precisa ser quadrada.")

    n = len(m)
    primeiro = m[0][n-1]
    for i in range(1, n):
        if m[i][n-1-i] != primeiro:
            return False
    return True
"""
"""
def mostra_matriz_multiplicada_pela_diagonal(m):
    if not eh_quadrada(m):
        raise ValueError("A matriz precisa ser quadrada.")

    n = len(m)
    for i in range(n):
        fator = m[i][i]
        linha_resultado = []
        for j in range(n):
            linha_resultado.append(m[i][j] * fator)
        print(linha_resultado)
"""
"""
def eh_quadrado_magico(m):
    if not eh_quadrada(m):
        raise ValueError("A matriz precisa ser quadrada.")

    n = len(m)

    soma_alvo = sum(m[0])

    for i in range(n):
        if sum(m[i]) != soma_alvo:
            return False

    for j in range(n):
        soma_coluna = 0
        for i in range(n):
            soma_coluna += m[i][j]
        if soma_coluna != soma_alvo:
            return False

    soma_dp = 0
    for i in range(n):
        soma_dp += m[i][i]
    if soma_dp != soma_alvo:
        return False

    soma_ds = 0
    for i in range(n):
        soma_ds += m[i][n-1-i]
    if soma_ds != soma_alvo:
        return False

    return True
"""
"""
def diagonais_paralelas_com_zero(m):
    if not eh_quadrada(m):
        raise ValueError("A matriz precisa ser quadrada.")
    n = len(m)

    diagonais_acima = []
    diagonais_abaixo = []

    for k in range(1, n):
        tem_zero = False
        for i in range(n - k):
            if m[i][i + k] == 0:
                tem_zero = True
                break
        if tem_zero:
            diagonais_acima.append(k)

    for k in range(1, n):
        tem_zero = False
        for i in range(n - k):
            if m[i + k][i] == 0:
                tem_zero = True
                break
        if tem_zero:
            diagonais_abaixo.append(k)

    print("Diagonais acima da principal com 0 (deslocamentos):", diagonais_acima)
    print("Diagonais abaixo da principal com 0 (deslocamentos):", diagonais_abaixo)
"""
"""
m = [
    [8, 0, 7],
    [4, 5, 6],
    [3, 10, 2]
]

print(media_diagonal_principal(m))           
print(diagonal_secundaria_igual(m))          
mostra_matriz_multiplicada_pela_diagonal(m)  
print(eh_quadrado_magico(m))                 
diagonais_paralelas_com_zero(m)              
"""