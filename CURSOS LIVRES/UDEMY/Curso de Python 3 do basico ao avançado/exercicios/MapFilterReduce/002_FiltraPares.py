lista = [12,75,89,65,41,36,25]
pares = list(
            filter(
                lambda x: x % 2 == 0,
            lista
            )
        )
print(pares)