# Criando uma sequência com índices e valores
formatados = [f"{i}: {x}" for i, x in enumerate(['a', 'b', 'c'])]

# Exibindo a sequência
print(formatados)  # Resultado: ['0: a', '1: b', '2: c']

# 1. `[f"{i}: {x}" for i, x in enumerate(['a', 'b', 'c'])]` gera índices e valores.
# 2. `enumerate` adiciona índices.
# 3. `print(formatados)` exibe a sequência.