nome = input("Qual o seu nome? ")

if nome.strip() == "":
    print("Desculpe, mas voce deixou o campo vazio!")
else:
    nome = nome.strip()

    print(f"Seu nome tem {len(nome)} letras")

    print(f"A primeira letra do seu nome é: {nome[0]}")

    print(f"A ultima letra do seu nome é: {nome[-1]}")
    
    nomeinvertido = nome[::-1]
    print(f"Seu nome invertido é: {nomeinvertido}")

    if " " in nome:
        print("Seu nome contém espaços.")
    else:
        print("Seu nome não contém espaços.")