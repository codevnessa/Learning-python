# Loop infinito para garantir que o usuário insira um número válido entre 1 e 150
while True:
    n = int(input("Digite um número entre 1 e 150: "))
    
    # Verifica se o número é maior que 150
    if n > 150:
        print("O número digitado ultrapassa os 150. Tente novamente.")
    
    # Verifica se o número é menor que 1
    elif n < 1:
        print("O número digitado é negativo, ou igual a 0. Tente novamente.")
    
    # Se o número estiver dentro do intervalo válido, sai do loop
    else:
        break

# Inicializa a variável soma com 0
soma = 0

# Lista para armazenar os números pares encontrados
numeros_pares = []

# Loop para encontrar e somar todos os números pares de 2 até n
for i in range(2, n+1, 2):
    soma += i  # Adiciona o número par à soma
    numeros_pares.append(i)  # Adiciona o número par à lista

# Verifica se o próprio número n é par
if n % 2 == 0:
    soma += n  # Se n for par, adiciona ele à soma
    numeros_pares.append(n)  # Adiciona n à lista de números pares

# Exibe os números pares encontrados e a soma total
print(f"Os números pares até {n} são: {numeros_pares}")
print(f"A soma dos números pares até {n} é {soma}")