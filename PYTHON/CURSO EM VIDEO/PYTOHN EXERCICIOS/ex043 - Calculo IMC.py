peso = float(input("Qual o seu peso? "))
alt = float(input("Qual a sua altura? "))
imc = peso / (alt * alt)
print(f"O seu IMC é de {imc:.1f}!")
if imc <= 18.5:
	print("Você está ABAIXO DO PESO")
elif imc <= 25:
	print("Você está no PESO IDEAL")
elif imc <= 30:
	print("Você está em SOBREPESO")
elif imc <= 40:
	print("Você está em OBESIDADE")
else:
	print("Você está em OBESIDADE MÓRBIDA")

