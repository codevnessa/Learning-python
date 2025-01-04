# Função lambda pode retornar outra função

criar_saudacao = lambda nome: lambda sobrenome: f"Olá, {nome} {sobrenome}!"

# Usando a função lambda
saudacao = criar_saudacao("João")
mensagem = saudacao("Silva")
print(mensagem)  # Resultado: Olá, João Silva!


# 1. `lambda nome:` cria uma função lambda que recebe um nome.
# 2. `lambda sobrenome:` cria outra função lambda que recebe um sobrenome.
# 3. `criar_saudacao("João")` retorna uma função lambda que espera um sobrenome.
# 4. `saudacao("Silva")` chama a segunda função lambda, passando "Silva" como sobrenome.
# 5. O resultado ("Olá, João Silva!") é exibido.