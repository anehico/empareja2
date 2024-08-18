from PIL import Image, ImageTk

class GameService:
    def __init__(self, matriz_imagenes, buttons):
        self.matriz_imagenes = matriz_imagenes
        self.buttons = buttons
        self.image_path_oculta = "src/resources/aves/hidden/incognito.png"
        self.photo_oculta = Image.open(self.image_path_oculta)
        self.photo_oculta = self.photo_oculta.resize((100, 100))
        self.photo_oculta = ImageTk.PhotoImage(self.photo_oculta)
        self.primer_boton = None
        self.segundo_boton = None

    def cambiar_imagen(self, row, col):
        # Obtener la imagen de la matriz
        imagen = self.matriz_imagenes[row][col].direccion_imagen
        nueva_imagen = Image.open(imagen)
        nueva_imagen = nueva_imagen.resize((100, 100))
        nueva_photo = ImageTk.PhotoImage(nueva_imagen)

        # Cambiar la imagen del botón seleccionado
        button = self.buttons[row][col]
        button.config(image=nueva_photo)
        button.image = nueva_photo  # Mantener una referencia a la imagen

        # Si es el primer botón que se presiona
        if not self.primer_boton:
            self.primer_boton = (row, col)
        elif not self.segundo_boton:
            self.segundo_boton = (row, col)
        else:
            # Si ya hay dos botones seleccionados, comparar si son pareja
            if not self.son_pareja(self.primer_boton, self.segundo_boton):
                # Si no son pareja, regresar las imágenes a la oculta
                self.ocultar_imagen(self.primer_boton)
                self.ocultar_imagen(self.segundo_boton)
            
            # Resetear para el próximo par
            self.primer_boton = (row, col)
            self.segundo_boton = None

    def son_pareja(self, boton1, boton2):
        # Verificar si los botones forman una pareja
        return self.matriz_imagenes[boton1[0]][boton1[1]].pareja == self.matriz_imagenes[boton2[0]][boton2[1]].id

    def ocultar_imagen(self, boton):
        row, col = boton
        button = self.buttons[row][col]
        button.config(image=self.photo_oculta)
        button.image = self.photo_oculta  # Mantener una referencia a la imagen ocult