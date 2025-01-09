# Criar uma função lambda que decide algo com base em uma condição:

# Lista de números de 0 a 10
num = [x for x in range(11)]

# Função lambda que verifica se um número é par
eh_par = lambda x: "Par" if x % 2 == 0 else "Ímpar"

# Iterando sobre a lista de números
for i in num:
    resultado = eh_par(i)  # Chama a função lambda para verificar se o número é par ou ímpar
    print(f"Numero: {i} -> {resultado}")

# 1. `lambda x:` cria uma função lambda que recebe um valor (x).
# 2. `"Par" if x % 2 == 0 else "Ímpar"` é uma condição:
#    - Se x for divisível por 2 (par), retorna "Par".
#    - Caso contrário, retorna "Ímpar".
# 3. `eh_par(i)` chama a função lambda, passando o número atual (i) como x.
# 4. O resultado ("Par" ou "Ímpar") é exibido para cada número na lista.