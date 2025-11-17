def isPalindromo(texto1, texto2):
    textoReves = texto2[::-1]
    if(texto1 == textoReves):
        return "Es un palindromo"
    else:
        return "No es un palindromo"

def app():
    texto1 = input("Ingresa el primer texto: ")
    texto2 = input("Ingresa el segundo texto: ")
    print("Deseas que se tome en cuenta las mayusculas o minusculas?")
    respuesta = input()
    respuesta = respuesta.lower()
    match (respuesta):
        case "si":
            texto2 = texto2.lower()
            texto1 = texto1.lower()
            resultado = isPalindromo(texto1, texto2)
            print(resultado)
        case "no":
            resultado = isPalindromo(texto1, texto2)
            print(resultado)
        case _:
            print("Opcion no valida")