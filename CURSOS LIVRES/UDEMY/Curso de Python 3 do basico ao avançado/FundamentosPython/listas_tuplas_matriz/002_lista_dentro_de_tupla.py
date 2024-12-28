# Explicação do conteúdo: Podemos ter listas dentro de tuplas. Isso é útil quando queremos armazenar dados mutáveis (listas) dentro de uma estrutura imutável (tupla).
# Acessamos os elementos da lista dentro da tupla usando índices duplos: o primeiro para a tupla e o segundo para a lista.

# Exemplo de tupla com listas:
dados = (
    [10, 20, 30],  # Lista na posição 0 da tupla
    [40, 50, 60],  # Lista na posição 1 da tupla
    [70, 80, 90]   # Lista na posição 2 da tupla
)

# Acessando elementos:
print("Primeira lista:", dados[0])  # Acessa a primeira lista
print("Segundo elemento da segunda lista:", dados[1][1])  # Acessa 50

# Modificando a lista dentro da tupla:
dados[0].append(40)  # Adiciona 40 à primeira lista
print("Primeira lista após modificação:", dados[0])

# Explicação do código:
# 1. A tupla `dados` contém listas, onde cada lista pode ser modificada.
# 2. A tupla em si é imutável, mas as listas dentro dela podem ser alteradas.
# OBS: Isso é útil quando queremos garantir que a estrutura principal não seja alterada, mas os dados internos possam ser.