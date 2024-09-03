texto = input("Digite uma frase ou palavra para verificar a letra 'a': ")

contador = 0

texto = texto.lower()

for letra in texto:
    if letra == 'a':
        contador += 1

if contador > 0:
    print(f"A letra 'a' (ou 'A') aparece {contador} vez(es) na string.")
else:
    print("A letra 'a' (ou 'A') não aparece na string.")


#Usando o contador, podemos contar quantas letras 'a' temos na frase após ela ser convertida para letras minúsculas, contando assim
#todas as letras 'a', já que todas se tornam minúsculas.