import tkinter as tk
from tkinter import ttk
from model.image import Imagen
from PIL import Image, ImageTk
from service.imageService import ImageService
from service.gameService import GameService

#########Datos de configuración (esto será parametrizable)############

longitud = 4
image_path = "src/resources/aves/hidden/incognito.png"  # Ruta a la imagen que deseas utilizar
usar_nombres_imagenes=True
imagenes = []
image_service = ImageService(100)
fondo_color = (255, 255, 255)  # Blanco
texto_color = (0, 0, 0)        # Negro

#######################################################################

### Imágenes (esto se va a borrar porque será configurable) ############
imagen_1 = Imagen(id=1, direccion_imagen="src/resources/aves/images/image_1.jpg", titulo="Ara macao", pareja=9)
imagen_2 = Imagen(id=2, direccion_imagen="src/resources/aves/images/image_2.jpg", titulo="Chlorochrysa nitidissima", pareja=10)
imagen_3 = Imagen(id=3, direccion_imagen="src/resources/aves/images/image_3.jpg", titulo="Semnornis ramphastinus", pareja=11)
imagen_4 = Imagen(id=4, direccion_imagen="src/resources/aves/images/image_4.jpg", titulo="Coeligena orina", pareja=12)
imagen_5 = Imagen(id=5, direccion_imagen="src/resources/aves/images/image_5.jpg", titulo="Doliornis remseni", pareja=13)
imagen_6 = Imagen(id=6, direccion_imagen="src/resources/aves/images/image_6.jpg", titulo="Crax alberti", pareja=14)
imagen_7 = Imagen(id=7, direccion_imagen="src/resources/aves/images/image_7.jpg", titulo="Capito hypoleucus", pareja=15)
imagen_8 = Imagen(id=8, direccion_imagen="src/resources/aves/images/image_8.jpg", titulo="Ortalis columbiana", pareja=16)

imagenes.extend([imagen_1, imagen_2, imagen_3, imagen_4, imagen_5, imagen_6, imagen_7, imagen_8])

if usar_nombres_imagenes:
    contador = (longitud * 2) + 1
    for imagen in imagenes:
        imagen_titulo = image_service.crear_imagen_nxn(imagen.titulo, fondo_color, texto_color)
        imagen_titulo.save(f"src/resources/aves/images/image_{contador}.jpg")
        contador += 1

    # Añadir las imágenes de nombres generadas al array imágenes
    imagenes.extend([
        Imagen(id=9, direccion_imagen="src/resources/aves/images/image_9.jpg", titulo="Ara macao", pareja=1),
        Imagen(id=10, direccion_imagen="src/resources/aves/images/image_10.jpg", titulo="Chlorochrysa nitidissima", pareja=2),
        Imagen(id=11, direccion_imagen="src/resources/aves/images/image_11.jpg", titulo="Semnornis ramphastinus", pareja=3),
        Imagen(id=12, direccion_imagen="src/resources/aves/images/image_12.jpg", titulo="Doliornis remseni", pareja=4),
        Imagen(id=13, direccion_imagen="src/resources/aves/images/image_13.jpg", titulo="Doliornis remseni", pareja=5),
        Imagen(id=14, direccion_imagen="src/resources/aves/images/image_14.jpg", titulo="Crax alberti", pareja=6),
        Imagen(id=15, direccion_imagen="src/resources/aves/images/image_15.jpg", titulo="Capito hypoleucus", pareja=7),
        Imagen(id=16, direccion_imagen="src/resources/aves/images/image_16.jpg", titulo="Ortalis columbiana", pareja=8)
    ])

######################################################################

matriz_imagenes = image_service.llenar_matriz_aleatoria(imagenes, longitud)

# Crear la ventana principal
root = tk.Tk()
root.title("Juego de Emparejados - Aves")

# Crear un contenedor para la tabla
frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)

# Crear la tabla de imágenes
buttons = []
for row in range(longitud):
    button_row = []
    for col in range(longitud):
        button = tk.Button(frame, borderwidth=1, relief="solid")
        button.grid(row=row, column=col, padx=10, pady=10)
        button_row.append(button)
    buttons.append(button_row)

# Crear el servicio de juego
game_service = GameService(matriz_imagenes, buttons)

# Asignar la imagen inicial (oculta) a todos los botones
photo = Image.open(image_path)
photo = photo.resize((100, 100))  # Ajusta el tamaño de la imagen según sea necesario
photo = ImageTk.PhotoImage(photo)

for row in range(longitud):
    for col in range(longitud):
        buttons[row][col].config(image=photo)
        buttons[row][col].config(command=lambda r=row, c=col: game_service.cambiar_imagen(r, c))

# Mantener una referencia de la imagen para evitar que sea recolectada por el garbage collector
root.photo = photo

# Ejecutar el bucle principal de la ventana
root.mainloop()