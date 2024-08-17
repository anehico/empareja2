import tkinter as tk
from tkinter import ttk
from model.image import Imagen
from PIL import Image, ImageTk
from service.imageService import ImageService

#########Datos de configuración (esto será parametrizable)############


longitud = 4
image_path = "src/resources/aves/hidden/incognito.png"  # Ruta a la imagen que deseas utilizar
usar_nombres_imagenes=True
imagenes = []
image_service = ImageService(100)
fondo_color = (255, 255, 255)  # Blanco
texto_color = (0, 0, 0)        # Negro

#######################################################################

###imagenes (esto se va a borrar porque será configurable)############
imagen_1 = Imagen(    
    id=1,
    direccion_imagen="src/resources/aves/images/image_1.jpg",
    titulo="Ara macao",
    pareja=9
)

imagen_2 = Imagen(    
    id=2,
    direccion_imagen="src/resources/aves/images/image_2.jpg",
    titulo="Chlorochrysa nitidissima",
    pareja=10
)

imagen_3 = Imagen(    
    id=3,
    direccion_imagen="src/resources/aves/images/image_3.jpg",
    titulo="Semnornis ramphastinus",
    pareja=11
)

imagen_4 = Imagen(    
    id=4,
    direccion_imagen="src/resources/aves/images/image_4.jpg",
    titulo="Coeligena orina",
    pareja=12
)
imagen_5 = Imagen(    
    id=5,
    direccion_imagen="src/resources/aves/images/image_5.jpg",
    titulo="Doliornis remseni",
    pareja=13
)
imagen_6 = Imagen(    
    id=6,
    direccion_imagen="src/resources/aves/images/image_6.jpg",
    titulo="Crax alberti",
    pareja=14
)
imagen_7 = Imagen(    
    id=7,
    direccion_imagen="src/resources/aves/images/image_7.jpg",
    titulo="Capito hypoleucus",
    pareja=15
)
imagen_8 = Imagen(    
    id=8,
    direccion_imagen="src/resources/aves/images/image_8.jpg",
    titulo="Ortalis columbiana",
    pareja=16
)

imagenes.append(imagen_1)
imagenes.append(imagen_2)
imagenes.append(imagen_3)
imagenes.append(imagen_4)
imagenes.append(imagen_5)
imagenes.append(imagen_6)
imagenes.append(imagen_7)
imagenes.append(imagen_8)


if(usar_nombres_imagenes):
    contador=(longitud*2)+1
    for imagen in imagenes:
        imagen_titulo=image_service.crear_imagen_nxn(imagen.titulo, fondo_color, texto_color)
        imagen_titulo.save(f"src/resources/aves/images/image_{contador}.jpg")
        contador=contador+1
    imagen_9 = Imagen(    
    id=9,
    direccion_imagen="src/resources/aves/images/image_9.jpg",
    titulo="Coeligena orina",
    pareja=1
    )
    imagen_10 = Imagen(    
    id=10,
    direccion_imagen="src/resources/aves/images/image_10.jpg",
    titulo="Coeligena orina",
    pareja=2
    )
    imagen_11 = Imagen(    
    id=11,
    direccion_imagen="src/resources/aves/images/image_11.jpg",
    titulo="Coeligena orina",
    pareja=3
    )
    imagen_12 = Imagen(    
    id=12,
    direccion_imagen="src/resources/aves/images/image_12.jpg",
    titulo="Coeligena orina",
    pareja=4
    )
    imagen_13 = Imagen(    
    id=13,
    direccion_imagen="src/resources/aves/images/image_13.jpg",
    titulo="Coeligena orina",
    pareja=5
    )
    imagen_14 = Imagen(    
    id=14,
    direccion_imagen="src/resources/aves/images/image_14.jpg",
    titulo="Coeligena orina",
    pareja=6
    )
    imagen_15 = Imagen(    
    id=15,
    direccion_imagen="src/resources/aves/images/image_15.jpg",
    titulo="Coeligena orina",
    pareja=7
    )
    imagen_16 = Imagen(    
    id=16,
    direccion_imagen="src/resources/aves/images/image_16.jpg",
    titulo="Coeligena orina",
    pareja=8
    )
    imagenes.append(imagen_9)
    imagenes.append(imagen_10)
    imagenes.append(imagen_11)
    imagenes.append(imagen_12)
    imagenes.append(imagen_13)
    imagenes.append(imagen_14)
    imagenes.append(imagen_15)
    imagenes.append(imagen_16)


######################################################################

matriz_imagenes = image_service.llenar_matriz_aleatoria(imagenes, longitud)

# Crear la ventana principal
root = tk.Tk()
root.title("Juego de Emparejados - Aves")

# Crear un contenedor para la tabla
frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)

# Cargar la imagen y redimensionarla
image = Image.open(image_path)
image = image.resize((100, 100))  # Ajusta el tamaño de la imagen según sea necesario
photo = ImageTk.PhotoImage(image)

# Crear la tabla de imágenes
buttons = []
for row in range(longitud):
    button_row = []
    for col in range(longitud):
         button = tk.Button(frame, image=photo, borderwidth=1, relief="solid")
         button.grid(row=row, column=col, padx=10, pady=10)
         button.config(command=lambda r=row, c=col: cambiar_imagen(r, c))
         button_row.append(button)
    buttons.append(button_row)

# Mantener una referencia de la imagen para evitar que sea recolectada por el garbage collector
root.photo = photo

def cambiar_imagen(row, col):
    """
    Cambia la imagen del botón en la posición especificada en la matriz.

    :param row: Fila del botón.
    :param col: Columna del botón.
    """
    imagen = matriz_imagenes[row][col].direccion_imagen
    nueva_imagen = Image.open(imagen)
    nueva_imagen = nueva_imagen.resize((100, 100))  # Ajustar tamaño si es necesario
    nueva_photo = ImageTk.PhotoImage(nueva_imagen)

    # Actualizar la imagen del botón
    buttons[row][col].config(image=nueva_photo)
    buttons[row][col].image = nueva_photo  # Mantener una referencia a la imagen
    
# Ejecutar el bucle principal de la ventana
root.mainloop()
