lista = [12,75,89,65,41,36,25]

print(
    list(
        filter(
            lambda x: x % 2 == 0,
           lista
        )
    )
)