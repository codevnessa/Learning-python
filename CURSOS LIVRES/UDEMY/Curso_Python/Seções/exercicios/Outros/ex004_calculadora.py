while True:
    num = input("Digite um número: ")
    print('[/][x][+][-]')
    operacao = input("Operador (/x+-): ")
    num2 = input("Digite outro número: ")

    numeros_validos = True

    try:
        numf = float(num)
        numf2 = float(num2)
    except ValueError:
        numeros_validos = False
        print("Um ou ambos os números digitados são inválidos.")

    operadores = '+-x/'

    if operacao not in operadores:
        print('Operador inválido.')
    elif not numeros_validos:
        continue  # Volta ao início do loop se os números não forem válidos
    else:
        if operacao == 'x':
            print(f'Resultado: {numf} {operacao} {numf2} = {(numf * numf2)}')
        elif operacao == '+':
            print(f'Resultado: {numf} {operacao} {numf2} = {(numf + numf2)}')
        elif operacao == '-':
            print(f'Resultado: {numf} {operacao} {numf2} = {(numf - numf2)}')
        elif operacao == '/':
            if numf2 == 0:
                print('Erro: Divisão por zero.')
            else:
                print(f'Resultado: {numf} {operacao} {numf2} = {(numf / numf2)}')

    sair = input("Digite 'sair' para encerrar: ").lower().startswith('s')

    if sair:
        print("ENCERRADO")
        break