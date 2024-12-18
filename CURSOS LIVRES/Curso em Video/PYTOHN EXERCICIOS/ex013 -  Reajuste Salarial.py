s = float(input('Qual o seu salário:R$'))
r = s * 15 / 100
sr = s + r
print('Com o novo reajuste salarial de 15%, seu salario de R${:.2f} teve um aumento de R${:.2f}, com o total de R${:.2f}'.format(s,r ,sr))