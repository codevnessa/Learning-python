#Realiza operações comuns entre conjuntos, como união, interseção e diferença

# Definindo dois conjuntos
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# União
uniao = A | B

# Interseção
intersecao = A & B

# Diferença
diferenca = A - B

diferenca_simetrica = A ^ B

# Exibindo os resultados
print("União:", uniao)
print("Interseção:", intersecao)
print("Diferença:", diferenca)
print("Diferença:", diferenca_simetrica)


"""
- A = {1, 2, 3, 4} e B = {3, 4, 5, 6}: Definindo dois conjuntos.
- uniao = A | B: Calcula a união dos conjuntos A e B.
- intersecao = A & B: Itens presentes em ambos.
- diferenca = A - B: Calcula a diferença entre A e B.
- diferenca_simetrica = A ^ B: Calcula o itens que nao estao em ambos.
- print(...): Exibe os resultados das operações.
"""