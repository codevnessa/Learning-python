from datetime import datetime

anoatual = datetime.now().year
maior = 0
menor = 0

for i in range(1,8):
	try:
		nasc= int(input(f"Digite o ano de nascimento da {i}ª pessoa: "))
		if nasc < 1900 or nasc > anoatual:
			print("Ano de nascimento invalido. Tente outra vez!")
			continue

		idade = anoatual - nasc

		if idade >= 18:
			maior += 1
		else:
			menor +=1

	except ValueError:
		print("Entrada inválida. Por favor, digite um número válido.")

print(f"O total de pessoas maiores de idade: {maior}")
print(f"O total de pessoas menores de idade: {menor}")