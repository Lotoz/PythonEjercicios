def anyoBisiesto(anyo):
    if anyo % 4 == 0 :
        if anyo % 100 == 0:
            if anyo % 400 == 0:
                print(f"El {anyo} es bisiesto.")
            else: 
              print(f"El {anyo} no es bisiesto.")  
        else:
            print(f"El {anyo} es bisiesto.")
    else:
        print(f"El {anyo} no es bisiesto.")
        
anyo = int(input("Introduce el anyo: "))
anyoBisiesto(anyo)