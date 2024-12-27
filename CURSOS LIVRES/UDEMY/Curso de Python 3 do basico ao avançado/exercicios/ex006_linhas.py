# Código 1: Imprime primeiro, depois incrementa
print("Código 1: Imprime primeiro, depois incrementa")
start1 = 0
end1 = 10
while start1 < end1:
    print(f"Valor de start1 antes do incremento: {start1}")
    start1 += 1
    print(f"Valor de start1 depois do incremento: {start1}")
print("Fim do Código 1\n")

# Explicação:
# - O valor de start é impresso antes de ser incrementado.
# - O loop imprime os valores de 0 a 9.
# - Quando start atinge 10, a condição start < end se torna falsa, e o loop termina.

print('-' * 20)

# Código 2: Incrementa primeiro, depois imprime
print("Código 2: Incrementa primeiro, depois imprime")
start2 = 0
end2 = 10
while start2 < end2:
    start2 += 1
    print(f"Valor de start2 depois do incremento: {start2}")
print("Fim do Código 2")

# Explicação:
# - O valor de start é incrementado antes de ser impresso.
# - O loop imprime os valores de 1 a 10.
# - Quando start atinge 10, ele é incrementado para 11, mas a condição start < end se torna falsa, e o loop termina.