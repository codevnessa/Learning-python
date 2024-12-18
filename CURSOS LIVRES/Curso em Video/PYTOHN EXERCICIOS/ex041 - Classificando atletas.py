from datetime import date
nas = int(input("Ano de nascimento: "))
anoatual = date.today().year
idade = anoatual - nas

print(f"O atleta tem {idade} anos.")

if idade >= 0 and idade <=9 :
	print("Classificação: MIRIM")
elif idade <= 14:
	print("Classificação: INFATIL")
elif idade <= 19:
	print("Classificação: JÚNIOR")
elif idade <= 25:
	print("Classificação: SÊNIOR")
else:
	print("Classificação: VASTER")