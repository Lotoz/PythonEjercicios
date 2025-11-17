#Recoje un texto e imprime cada letra en una línea distinta
texto = input("Introduce un texto: ")

#Hacemos un bucle para recorrer cada letra del texto
for letra in texto:
    print(letra)

#otra forma de hacelro es usando un indice
for i in range(len(texto)):
    print(texto[i])

#Otra forma es usando enumerate para obtener el indice y la letra
for indice, letra in enumerate(texto):
    print(f"Letra {indice}: {letra}")

#Otra forma es usando un while
i = 0
while i < len(texto):
    print(texto[i])
    i += 1

#Otra forma es usando join para unir cada letra con un salto de linea
print("\n".join(texto))
#Otra forma es usando map para aplicar print a cada letra
list(map(print, texto))

#Otra forma es usando unpacking para pasar cada letra como argumento a print
print(*texto, sep="\n")
