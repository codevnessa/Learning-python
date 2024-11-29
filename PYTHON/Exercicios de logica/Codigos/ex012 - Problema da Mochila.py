# Define a função mochila que resolve o problema da mochila usando programação dinâmica
def mochila(capacidade, pesos, valores, n):
    # Inicializa uma matriz dp para armazenar os valores máximos para cada subproblema
    dp = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]

    # Loop para preencher a matriz dp
    for i in range(1, n + 1):
        for w in range(1, capacidade + 1):
            # Se o peso do item atual for menor ou igual à capacidade atual
            if pesos[i-1] <= w:
                # Escolhe o máximo entre incluir o item atual ou não
                dp[i][w] = max(valores[i-1] + dp[i-1][w-pesos[i-1]], dp[i-1][w])
            else:
                # Se o peso do item atual for maior que a capacidade atual, não inclui o item
                dp[i][w] = dp[i-1][w]

    # Retorna o valor máximo que pode ser colocado na mochila
    return dp[n][capacidade]

# Define os valores e pesos dos itens
valores = [60, 100, 120]
pesos = [10, 20, 30]

# Define a capacidade máxima da mochila
capacidade = 50

# Calcula o número de itens
n = len(valores)

# Calcula e exibe o valor máximo que pode ser colocado na mochila
print("O valor máximo que pode ser colocado na mochila é:", mochila(capacidade, pesos, valores, n))