class Persona:
    nombre:str = ""
    telefono:int = ""
    direccion:str = ""

p=Persona()
p.nombre = "Arturo"
p.telefono = "5555555"
p.direccion = "Calle 31"

class TablaHash:
    def __init__(self):
        self.size = 10
        self.tablaHash = [None] * self.size

    def hashV(self, nombre)-> int:
        return hash(nombre) % self.size

    def list(self, nombre):
        pos = self.tablaHash
tabla = TablaHash()
name = p.nombre
tabla.hashV(name)
