maior = None
menor = None

for i in range(1, 6):
    try:
        kilo = float(input(f"Peso da {i}ª pessoa: "))
        if maior is None or kilo > maior:
            maior = kilo
        if menor is None or kilo < menor:
            menor = kilo
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")

print(f"O maior dos pesos digitados foi de {maior}Kg")
print(f"E o menor dos pesos digitados foi de {menor}Kg")