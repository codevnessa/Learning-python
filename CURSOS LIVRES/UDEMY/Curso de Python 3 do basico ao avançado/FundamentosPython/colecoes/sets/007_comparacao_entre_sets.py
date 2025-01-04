# Compara conjuntos para verificar se um é subconjunto ou superconjunto de outro

# Definindo dois conjuntos
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}

# Verificando se A é subconjunto de B
subconjunto = A.issubset(B)

# Verificando se B é superconjunto de A
superconjunto = B.issuperset(A)

# Exibindo os resultados
print("A é subconjunto de B:", subconjunto)
print("B é superconjunto de A:", superconjunto)

"""
- A = {1, 2, 3} e B = {1, 2, 3, 4, 5}: Definindo dois conjuntos.
- subconjunto = A.issubset(B): Verifica se A é subconjunto de B.
- superconjunto = B.issuperset(A): Verifica se B é superconjunto de A.
- print(...): Exibe os resultados das comparações.
"""