from random import choice
from time import sleep

def jokenpo():
	opcoes = ["PEDRA", "PAPEL", "TESOURA"]
	while True:
		print("")
		print("=" * 25)
		print("JOQUEMPO")
		print("=" * 25)
		print("[ 1 ] PEDRA")
		print("[ 2 ] PAPEL")
		print("[ 3 ] TESOURA")

		try:
			opcao = int(input("Qual a sua jogada: "))
			if opcao not in [1,2,3]:
				raise ValueError
		except (ValueError, TypeError):
			print("Opção invalida! Digite um número valido.")
			continue

		computador = choice(opcoes)
		jogador = opcoes[opcao - 1]

		print("JO")
		sleep(1)
		print("KEN")
		sleep(1)
		print("PÔ")

		print("-=" * 15)
		print(f"Voce escolheu: {jogador}")
		print(f"Computador escolheu: {computador}")
		print("=-" * 15)

		if computador == jogador:
			print("EMPATE")
		elif computador == "PEDRA" and jogador == "PAPEL":
			print("VOCE VENCEU")
		elif computador == "PAPEL" and jogador == "TESOURA":
			print("VOCE VENCEU")
		elif computador == "TESOURA" and jogador == "PEDRA":
			print("VOCE VENCEU")
		else:
			print("VOCE PERDEU")
		print("=-" * 15)
jokenpo()