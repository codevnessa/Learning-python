lista = ["banana", "maçã", "laranja", "uva", "melancia"]

prefixo = list(
    map(
        lambda palavra: palavra + '-', lista
    )
)

print(prefixo)