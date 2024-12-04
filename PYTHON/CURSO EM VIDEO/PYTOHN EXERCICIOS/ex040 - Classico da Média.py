nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
media = 7
res = (nota1 + nota2) / 2

if res > media:
	print(f"Tirando {nota1} e {nota2}, a média do aluno é de {res}.")
	print(f"Sendo a média igual a {media} pontos, o aluno está APROVADO!")
else:
	print(f"Tirando {nota1} e {nota2}, a média do aluno é de {res}.")
	print(f"Sendo a média igual a {media} pontos, o aluno está REPROVADO!")