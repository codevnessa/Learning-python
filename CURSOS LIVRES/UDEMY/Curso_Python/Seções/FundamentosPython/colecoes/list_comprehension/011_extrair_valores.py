# Criando uma sequência com valores de um dicionário
valores = [v for k, v in {'a': 1, 'b': 2}.items()]

# Exibindo a sequência
print(valores)  # Resultado: [1, 2]

# 1. `[v for k, v in {'a': 1, 'b': 2}.items()]` extrai os valores do dicionário.
# 2. `items()` retorna chaves e valores.
# 3. `print(valores)` exibe a sequência.