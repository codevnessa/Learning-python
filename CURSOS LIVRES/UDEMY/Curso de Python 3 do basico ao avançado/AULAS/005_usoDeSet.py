letras = set()
while True:
    letra = input('Digite: ').upper()
    letras.add(letra)

    if 'l'.upper() in letras:
        print('Parabens')
        break

    print(letras)
