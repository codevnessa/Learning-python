lista = ["banana", "maçã", "laranja", "uva", "melancia"]

filtrar = list(
    filter(
       lambda palavra: len(palavra) >=6, lista
    )
)
print(filtrar)