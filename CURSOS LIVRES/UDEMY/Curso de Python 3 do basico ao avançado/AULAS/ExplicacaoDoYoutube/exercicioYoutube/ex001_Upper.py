nomes = ['Maria', 'Luiz', 'Vanessa', 'Rafael']

lower = [nome.lower() for nome in nomes]

upper = [nome[:-1] + nome[-1].upper() for nome in lower]

# Exibe as listas
print(nomes)  # Lista original
print(lower)  # Lista com nomes em minúsculas
print(upper)  # Lista com a última letra em maiúsculas