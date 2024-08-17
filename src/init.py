import tkinter as tk
from tkinter import ttk

longitud=9

# Crear la ventana principal
root = tk.Tk()
root.title("Juego de Emparejados - Aves")

# Crear un contenedor para la tabla
frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)

# Crear la tabla de 8x8 usando un grid de labels
for row in range(longitud):
    for col in range(longitud):
        cell = ttk.Label(frame, text=f"({row+1}, {col+1})", borderwidth=1, relief="solid", width=10, anchor="center")
        cell.grid(row=row, column=col, padx=5, pady=5)

# Ejecutar el bucle principal de la ventana
root.mainloop()
