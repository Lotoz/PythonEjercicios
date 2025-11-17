def isPalindromo(texto):
    texto = texto.lower()
    textoReves = texto[::-1]
    if(texto == textoReves):
        print("Es un palindromo!")
    else:
        print("No es palindromo.")

def app():
    texto = input("Escribe una palabra a analizar de palindromo:")
    isPalindromo(texto)