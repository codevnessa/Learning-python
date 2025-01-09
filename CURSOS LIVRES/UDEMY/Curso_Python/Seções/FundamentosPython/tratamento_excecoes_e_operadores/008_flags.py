# Flags em Python
# Uma flag (em português, "bandeira") é uma variável que é usada para armazenar um estado ou condição lógica em um programa. Ela é frequentemente usada para controlar o fluxo de execução do código, como determinar se uma condição foi atendida ou não.

# Exemplo prático:
encontrado = False  # Flag inicializada como False

lista = [1, 2, 3, 4, 5]

# Procurando um número na lista
for numero in lista:
    if numero == 3:
        encontrado = True  # Flag é atualizada para True
        break

if encontrado:
    print("Número encontrado!")
else:
    print("Número não encontrado.")

# Explicação:
# A variável encontrado é uma flag que começa com o valor False.
# O programa percorre a lista e verifica se o número 3 está presente.
# Se o número for encontrado, a flag é atualizada para True.
# No final, o programa verifica o estado da flag para exibir a mensagem correspondente.