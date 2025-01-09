# Como criar uma função lambda que aceita vários valores nomeados

# Função lambda que exibe os valores nomeados
exibir_valores = lambda **kwargs: kwargs

# Usando a função lambda
resultado = exibir_valores(nome="João", idade=30)
print(resultado)  # Resultado: {'nome': 'João', 'idade': 30}

# 1. `lambda **kwargs:` cria uma função lambda que aceita valores nomeados.
# 2. `kwargs` é um dicionário que armazena os valores nomeados.
# 3. `exibir_valores(nome="João", idade=30)` chama a função lambda, passando dois valores nomeados.
# 4. O resultado é um dicionário com os valores passados.