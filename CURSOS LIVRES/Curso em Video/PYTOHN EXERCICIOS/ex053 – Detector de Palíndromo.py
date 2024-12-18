frase = str(input('Digite uma palavra ou frase: ')).upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

# Loop para inverter a string
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

# Verificação do palíndromo
if junto == inverso:
    print(f'"{frase}" é um palíndromo.')
else:
    print(f'"{frase}" não é um palíndromo.')