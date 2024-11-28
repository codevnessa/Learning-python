# Solicita ao usuário que digite uma palavra
texto = input("Digite uma palavra: ")

# Define uma string contendo todas as vogais (minúsculas e maiúsculas)
vogais = "aeiouAEIOU"

# Inicializa um contador para contar o número de vogais
count = 0

# Loop para percorrer cada caractere na palavra digitada
for char in texto:
    # Verifica se o caractere atual é uma vogal
    if char in vogais:
        # Se for uma vogal, incrementa o contador
        count += 1

# Exibe o número total de vogais encontradas na palavra
print(f"O que foi digitado, contém {count} vogais.")