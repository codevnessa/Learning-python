from random import choice

nums = [0, 1, 2, 3, 4, 5]
adv = choice(nums)

while True:
	num = int(input('Adivinhe o número que estou pensando, de 0 a 5: '))

	if num == adv:
		print('PARABÉNS VOCÊ ACERTOU!')
		break
	else:
		print('VOCÊ ERROU! Tente novamente.')