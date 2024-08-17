from PIL import Image, ImageDraw, ImageFont, ImageTk
import textwrap
import random

class ImageService:
     def __init__(self, n):
        self.n = n

     def crear_imagen_nxn(self, texto, fondo_color, texto_color):
        """
        Crea una imagen nxn con un texto en el centro y un fondo de color.

        :param texto: El texto que se mostrará en la imagen.
        :param fondo_color: Color de fondo de la imagen (en formato RGB).
        :param texto_color: Color del texto (en formato RGB).
        :return: La imagen creada.
        """
       # Crear una nueva imagen en blanco
        imagen = Image.new("RGB", (self.n, self.n), fondo_color)

        # Crear un objeto para dibujar en la imagen
        dibujar = ImageDraw.Draw(imagen)

        # Cargar una fuente para el texto
        try:
            fuente = ImageFont.truetype("ariali.ttf", size=12)  # Puedes cambiar la fuente y tamaño
        except IOError:
            fuente = ImageFont.load_default()

        # Dividir el texto en líneas que se ajusten al ancho de la imagen
        max_ancho = self.n - 20  # Margen de 10 píxeles a cada lado
        lineas = []
        palabras = texto.split(' ')
        linea_actual = ''

        for palabra in palabras:
            prueba_linea = f'{linea_actual} {palabra}'.strip()
            bbox = dibujar.textbbox((0, 0), prueba_linea, font=fuente)
            ancho_linea = bbox[2] - bbox[0]

            if ancho_linea <= max_ancho:
                linea_actual = prueba_linea
            else:
                if linea_actual:
                    lineas.append(linea_actual)
                linea_actual = palabra

        if linea_actual:
            lineas.append(linea_actual)

        # Calcular el tamaño total del texto
        texto_ancho = max(dibujar.textbbox((0, 0), linea, font=fuente)[2] - dibujar.textbbox((0, 0), linea, font=fuente)[0] for linea in lineas)
        texto_alto = sum(dibujar.textbbox((0, 0), linea, font=fuente)[3] - dibujar.textbbox((0, 0), linea, font=fuente)[1] for linea in lineas)

        # Calcular la posición para centrar el texto
        x = (self.n - texto_ancho) / 2
        y = (self.n - texto_alto) / 2

        # Dibujar el texto en la imagen
        for linea in lineas:
            bbox = dibujar.textbbox((x, y), linea, font=fuente)
            _, _, _, alto_texto = bbox
            dibujar.text((x, y), linea, fill=texto_color, font=fuente)
            y += 10  # Mover hacia abajo para la siguiente línea

        return imagen
     
     def llenar_matriz_aleatoria(self, imagenes, longitud):
        """
        Llena una matriz de tamaño longitud x longitud con imágenes aleatorias del array imagenes.

        :param imagenes: Array de objetos de tipo Imagen.
        :param longitud: Tamaño de la matriz (NxN).
        :return: Matriz de imágenes.
        """
        # Asegúrate de que el array de imágenes tenga al menos el número de elementos necesario
        if len(imagenes) < longitud * longitud:
            raise ValueError("El array de imágenes no tiene suficientes elementos para llenar la matriz.")

        # Barajar el array de imágenes aleatoriamente
        imagenes_aleatorias = imagenes.copy()
        random.shuffle(imagenes_aleatorias)

        # Crear la matriz
        matriz = []
        for i in range(longitud):
            fila = imagenes_aleatorias[i*longitud:(i+1)*longitud]
            matriz.append(fila)

        return matriz