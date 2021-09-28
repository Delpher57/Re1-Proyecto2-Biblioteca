from dataclasses import dataclass





@dataclass
class Libro:
    _id: int
    nombre: str
    autor: str
    fotografia: str


    def print_info_libro(self):
        return str(self._id) + " | " + self.nombre + " | Escrito por: " + self.autor

@dataclass
class Usuario:
    _id: int
    nombre: str
    usuario: str
    password: str

    def print_info_user(self):
        return str(self._id) + " | " + self.nombre + " | " + self.usuario + " | "  + self.password

@dataclass
class PrestamosXUsuario:
    _id: int
    usuario: int #Id del usuario que hizo el prestamo
    libro: int #Id del libro prestado
    fecha_prestamo: str   # fechas en formato "%d/%m/%Y"
    fecha_devolucion: str
    activo: bool #si es false es un prestamo del pasado y no se revisa

    def print_info_prestamo(self):
        return str(self._id) + " | " + self.fecha_prestamo + " | " + self.fecha_devolucion + " | " + str(self.activo) + " | User: " + str(self.usuario) + " | Libro: " + str(self.libro)