# Explicação do conteúdo: Este código compara o uso do while e do for para realizar a mesma tarefa.
# O while é usado quando a condição de parada é desconhecida, enquanto o for é usado quando o número de iterações é conhecido.

# Exemplo de comparação entre while e for:
# Usando while
contador = 0  # Inicializa o contador com 0
print("Usando while:")
while contador < 3:  # Enquanto o contador for menor que 3
    print("Contador:", contador)  # Imprime o valor atual do contador
    contador += 1  # Incrementa o contador em 1

# Usando for
print("Usando for:")
for i in range(3):  # Para cada número no intervalo de 0 a 2
    print("Número:", i)  # Imprime o valor atual de i

# Explicação do código:
# 1. O while é usado para repetir um bloco de código enquanto a condição `contador < 3` for verdadeira.
# 2. O for é usado para iterar sobre uma sequência gerada por range(3).
# 3. Ambos os loops produzem o mesmo resultado, mas o for é mais conciso quando o número de iterações é conhecido.
# OBS: Escolha entre while e for com base na clareza e na necessidade do seu código.