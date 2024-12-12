i = int(input("Inicio: "))
f = int(input("Fnal: "))

quant = 0
for num in range(i, f+1):
	if num % 2 == 0:
		print(num)
		quant +=1

print(f"De {i} até {f} temos {quant} numeros pares")