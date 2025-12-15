import tkinter as tk
from tkinter import messagebox

# 1. Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi Primera App")
ventana.geometry("300x200") # Tamaño: Ancho x Alto

# 2. Definir qué hace el botón (La función lógica)
def mostrar_mensaje():
    etiqueta.config(text="¡Has pulsado el botón!")
    messagebox.showinfo("Alerta", "¡Hola desde Python!")

# 3. Crear los elementos (Widgets)
etiqueta = tk.Label(ventana, text="Presiona el botón de abajo", font=("Arial", 12))
etiqueta.pack(pady=20) # 'pack' coloca el elemento en la ventana

boton = tk.Button(ventana, text="Haz Clic Aquí", command=mostrar_mensaje)
boton.pack(pady=10)

# 4. Iniciar el bucle de ejecución
ventana.mainloop()