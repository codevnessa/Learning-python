i = int(input("Inicio: "))
f = int(input("Fnal: "))
soma = 0
cont = 0

for num in range(i, f):
	if num % 3 == 0:
		soma += num
		cont += 1
print(f"A soma de todos os {cont} valores é de: {soma}")