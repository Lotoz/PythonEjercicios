texto = input("Introduce un texto: ")
letra = input("Introduce una letra: ")

contador = 0
#Para que no se lie entre mayusculas y minusculas
texto = texto.upper()
letra = letra.upper()

for buscado in texto:
    if buscado == letra:
        contador += 1

print(f"La letra '{letra}' aparece {contador} veces en el texto.")