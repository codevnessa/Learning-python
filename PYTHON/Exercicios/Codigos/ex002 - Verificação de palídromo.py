 # Mensagem inicial informando ao usuário como sair do programa
print("Digite 'sair' a qualquer momento para encerrar o programa.\n")

# Loop infinito para permitir que o usuário insira palavras repetidamente
while True:
    # Solicita ao usuário que digite uma palavra
    palavra = input("Digite uma palavra: ")

    # Verifica se o usuário deseja sair do programa
    if palavra.lower() == 'sair':
        print("\nObrigada por utilizar nosso programa :)")
        print("Esperamos vê-lo novamente em breve!")
        break  # Sai do loop e encerra o programa

    # Verifica se a palavra é um palíndromo
    if palavra == palavra[::-1]:
        print(f"{palavra} é um palíndromo.\n")
    else:
        print(f"{palavra} não é um palíndromo.\n")