palavra = input("Digite uma palavra: ")
vogais_encontradas = []
for letra in palavra:
    if letra.lower() in ['a', 'e', 'i', 'o', 'u']:
        vogais_encontradas.append(letra)
print("Vogais encontradas:", vogais_encontradas)
