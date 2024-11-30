print("=-" * 35)
print("BEM-VINDO AO SISTEMA DE CALCULO DE MENSALIDADE DA ACADEMIA ")
print("=-" * 35)

try:
    #ENTRADA DO USUÁRIO
    valor_base = float(input("Informe o valor base da mensalidade: R$ "))
    idade = int(input("Informe a idade do cliente: "))

    #CALCULA O VALOR MENSAL DA MENSALIDADE COM BASE NA IDADE
    if idade >= 0 and idade < 19:
        valor_mensal = valor_base * (100/100)
    elif idade >= 19 and idade < 29:
        valor_mensal = valor_base * (110/100)
    elif idade >= 29 and idade < 39:
        valor_mensal = valor_base * (120/100)
    elif idade >= 39 and idade < 49:
        valor_mensal = valor_base * (130/100)
    elif idade >= 49 and idade < 59:
        valor_mensal = valor_base * (140/100)
    else:
        valor_mensal = valor_base * (150/100)

    #EXIBE O RESULTADO
    print()
    print(f"O valor da mensalidade é de: R${valor_mensal:.2f}")
except ValueError as e:
    print(f"Erro: {e}")