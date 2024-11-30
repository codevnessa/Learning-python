import random

# Define a função desenhar_forca que exibe o estado atual da forca com base no número de erros
def desenhar_forca(erros):
    estagios = [
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |     /|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |      |
           |     / \\
           -
        """
    ]
    return estagios[erros]

# Define a função escolher_palavra que seleciona uma palavra aleatória de uma lista
def escolher_palavra():
    palavras = ["PYTHON", "PROGRAMAR", "ALGORITMO", "DESENVOLVIMENTO"]
    return random.choice(palavras)

# Define a função exibir_palavra que mostra a palavra com as letras corretas reveladas
def exibir_palavra(palavra, letras_corretas):
    return ' '.join([letra if letra in letras_corretas else '_' for letra in palavra])

# Define a função jogo_da_forca que controla o fluxo do jogo
def jogo_da_forca():
    palavra_secreta = escolher_palavra()  # A palavra que o jogador vai adivinhar
    letras_corretas = set()  # Conjunto de acertos
    letras_erradas = set()  # Conjunto de erros
    max_erros = 6  # Máximo de erros permitidos

    print("Bem-vindo ao Jogo da Forca!")

    # Inicia o loop do jogo
    while len(letras_erradas) < max_erros and set(palavra_secreta) != letras_corretas:
        # Desenha o boneco da forca com base no número de erros
        print(desenhar_forca(len(letras_erradas)))
        # Exibe as letras corretas
        print(exibir_palavra(palavra_secreta, letras_corretas))
        # Exibe as letras que errou
        print(f"Letras erradas: {' '.join(letras_erradas)}")

         # Entrada do jogador
        while True:
            letra = input("Adivinhe uma letra: ").upper()
            if len(letra) == 1 and letra.isalpha():
                break
            else:
                print("Por favor, insira apenas uma letra.")

        # Verifica se a letra é repetida
        if letra in letras_corretas or letra in letras_erradas:
            print(f"Você já tentou a letra '{letra}'. Tente outra.")
            continue

        # Verifica se a letra está na palavra secreta
        if letra in palavra_secreta:
            letras_corretas.add(letra)  # Adiciona ao conjunto de acertos
        else:
            letras_erradas.add(letra)  # Adiciona ao conjunto de erros

    # Verifica o resultado do jogo
    if set(palavra_secreta) == letras_corretas:
        print(f"Parabéns! Você adivinhou a palavra: {palavra_secreta}")
    else:
        print(desenhar_forca(len(letras_erradas)))
        print(f"Você perdeu! A palavra era: {palavra_secreta}")

# Inicia o jogo
jogo_da_forca()