vogais = ('a', 'e', 'i', 'o', 'u')
frase = 'O código é como um quebra-cabeça: cada peça faz sentido quando você olha o todo'

# Convertendo a frase para minúsculas e removendo espaços
frase = frase.lower().replace(' ', '')
contadorLetras = len(frase)  # Total de letras sem espaços
contagem = {vogal: 0 for vogal in vogais}  # Inicializa o dicionário com contagem zero para cada vogal

# Iteração para contar as vogais
for letra in frase:
    if letra in vogais:
        contagem[letra] += 1

# Resultados finais
print("\n--- Resultados Finais ---")
print("Contagem total de letras (sem espaços):", contadorLetras)
print("Vogais:", vogais)
print("Contagem final das vogais:")
for vogal, quantidade in contagem.items():
    print(f"{vogal.upper()}: {quantidade}")