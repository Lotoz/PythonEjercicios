def app():
    cadena = input("Introduzca un texto: ")
    total = 0;
    cadena = cadena.lower()
    for vocal in cadena:
        a = vocal.count(a);
        e = vocal.count(e);
        i = vocal.count(i);
        o = vocal.count(o);
        u = vocal.count(u);

        total = a + e + i + o + u;

    print(f"Hay un total de vocales de {total}")

app()