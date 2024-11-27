try:
    n = int(input("Digite um número: "))
except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")
    exit()

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")