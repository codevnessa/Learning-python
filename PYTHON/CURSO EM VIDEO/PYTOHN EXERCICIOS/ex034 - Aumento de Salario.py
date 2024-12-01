salario = float(input('Qual o seu salário? R$'))
if salario <= 1250:
    print ('Seu salário teve um aumento de 15%, resultando em: R${:.2f}'.format(salario +(salario *15/100)))
if salario > 1250:
    print('Seu salario teve um aumento de cerca de 10%, resultando em: R${:.2f}'.format(salario +(salario *10/100)))