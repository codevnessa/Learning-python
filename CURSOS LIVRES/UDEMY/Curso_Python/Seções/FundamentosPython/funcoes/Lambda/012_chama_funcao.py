# Função lambda pode chamar outra função

# Função que converte uma string para maiúsculas
def maiusculas(texto):
    return texto.upper()

# Função lambda que usa a função maiusculas
transformar = lambda texto: maiusculas(texto)

# Usando a função lambda
resultado = transformar("olá, mundo!")
print(resultado)  # Resultado: OLÁ, MUNDO!

# 1. `maiusculas(texto)` é uma função que converte texto para maiúsculas.
# 2. `lambda texto:` cria uma função lambda que recebe um texto.
# 3. `maiusculas(texto)` chama a função `maiusculas` dentro da lambda.
# 4. `transformar("olá, mundo!")` chama a função lambda, passando o texto.
# 5. O resultado ("OLÁ, MUNDO!") é exibido.