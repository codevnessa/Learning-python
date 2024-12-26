# Solicita ao usuário que digite seu nome e armazena o valor na variável 'nome'
nome = input("Qual seu nome? ")

# Verifica o comprimento do nome usando a função len()
if len(nome) < 3:  # Se o nome tiver menos de 3 caracteres
    print("Seu nome é muito curto!")
elif len(nome) > 20:  # Se o nome tiver mais de 20 caracteres
    print("Seu nome é muito longo!")
else:  # Se o nome estiver entre 3 e 20 caracteres
    print(f"Olá, {nome}! Seu nome tem um comprimento adequado.")