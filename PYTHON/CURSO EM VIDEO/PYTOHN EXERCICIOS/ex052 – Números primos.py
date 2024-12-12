num = int(input("Digite um número: "))
total = 0

if num > 1:
    print(f"Divisores de {num}: ", end='')
    for i in range(1, num + 1):
        if num % i == 0:
            print("\033[31m", end='')
            print(f"{i}", end=' ')
            total += 1
        else:
            print("\033[33m", end='')
            print(f"{i}", end=' ')
    print("\033[0m")
else:
    print("Por favor, digite um número maior que 1.")
if total <= 2:
    print(f"Então o número {num} é um número primo, pois possui apenas {total} divisores.")
else:
    print(f"Então o número {num} não é um número primo, pois possui {total} divisores.")