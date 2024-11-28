while True:
    n = int(input("Digite um número entre 1 e 150: "))
    if n > 150:
        print("O número digitado ultrapassa os 150. Tente novamente.")
    elif n < 1:
        print("O número digitado é negativo, ou igual a 0. Tente novamente.")
    else:
        break

soma = 0
numeros_pares = [] # Aqui é onde vai armazenar os números pares

for i in range(2, n+1, 2):
    soma += i
    numeros_pares.append(i) # Adiciona os numeros pares a lista

#Verifica se o proprio numero n é par
if n % 2 == 0:
    soma += n
    numeros_pares.append(i)

print(f"Os números pares até {n} são: {numeros_pares}")
print(f"A soma dos numeros pares até {n} é {soma}")

