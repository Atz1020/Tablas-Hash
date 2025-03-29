class Persona:
    nombre: str = ""
    telefono: str = ""
    direccion: str = ""

p = Persona()
p.nombre = "Arturo"
p.telefono = "5555555"
p.direccion = "Calle 31"

class TablaHash:
    def __init__(self, tamaño=10):
        self.size = tamaño
        self.tablaHash = [None] * self.size
        self.contador = 0

    def hashV(self, clave) -> int:
        return hash(clave) % self.size

    def agregar(self, clave: str, valor: str):
        if self.contador < self.size:
            hash_clave = self.hashV(clave)
            self.tablaHash[self.contador] = (clave, valor, hash_clave)
            print(f"\nContacto agregado:")
            print(f"   Nombre  : {clave}")
            print(f"   Teléfono: {valor}")
            print(f"   Hash    : {hash_clave}")
            print(f"   Índice  : {self.contador}")
            self.contador += 1
        else:
            print("No hay espacio en la tabla para agregar más contactos.")

    def buscar(self, clave: str):
        for i in range(self.size):
            lista = self.tablaHash[i]
            if lista and lista[0] == clave:
                clave, valor, hash_clave = lista
                print(f"\nContacto encontrado:")
                print(f"   Nombre  : {clave}")
                print(f"   Teléfono: {valor}")
                print(f"   Hash    : {hash_clave}")
                print(f"   Índice  : {i}")
                return
        print("\nContacto no encontrado.")

    def eliminar(self, clave: str):
        for i in range(self.size):
            lista = self.tablaHash[i]
            if lista and lista[0] == clave:
                self.tablaHash[i] = None
                print(f"\nContacto {clave} eliminado.")
                return
        print("\nContacto no encontrado.")

    def listar(self):
        print("\nLista de contactos:")
        for i in range(self.size):
            lista = self.tablaHash[i]
            if lista:
                clave, valor, hash_clave = lista
                print(f"   Índice {i} | Hash: {hash_clave} → {clave}: {valor}")
            else:
                print(f"   Índice {i}: Vacío")

tabla = TablaHash()

while True:
    opcion = input("\nSeleccione una opción: agregar, buscar, eliminar, listar, salir: ").lower()
    if opcion == 'salir':
        break
    elif opcion == 'agregar':
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el número de teléfono: ")
        tabla.agregar(nombre, telefono)
    elif opcion == 'buscar':
        nombre_buscar = input("Ingrese el nombre del contacto a buscar: ")
        tabla.buscar(nombre_buscar)
    elif opcion == 'eliminar':
        nombre_eliminar = input("Ingrese el nombre del contacto a eliminar: ")
        tabla.eliminar(nombre_eliminar)
    elif opcion == 'listar':
        tabla.listar()
    else:
        print("Opción no válida.")