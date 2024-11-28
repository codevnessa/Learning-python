texto = input("Digite uma palavra: ")
vogais = "aeiouAEIOU"
count = 0
for char in texto:
    if char in vogais:
        count += 1
print(f"O que foi digitado, contém {count} vogais.")