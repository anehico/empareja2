class Imagen:
    def __init__(self, id, direccion_imagen, titulo, pareja):
        """
        Inicializa una nueva instancia de la clase Imagen.

        :param id: Identificador único de la imagen.
        :param direccion_imagen: Ruta del archivo de la imagen (en archivos planos).
        :param titulo: Título de la imagen.
        """
        self.id = id
        self.direccion_imagen = direccion_imagen
        self.titulo = titulo
        self.pareja = pareja

    def mostrar_info(self):
        """
        Muestra la información de la imagen.
        """
        print(f"ID: {self.id}")
        print(f"Dirección de la imagen: {self.direccion_imagen}")
        print(f"Título: {self.titulo}")
        print(f"Pareja: {self.pareja}")

    def __repr__(self):
        """
        Representación en forma de cadena de la instancia de la clase Imagen.
        """
        return f"Imagen(id={self.id}, direccion_imagen='{self.direccion_imagen}', titulo='{self.titulo}', pareja='{self.pareja}')"