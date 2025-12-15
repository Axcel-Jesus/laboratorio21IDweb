class libro:
    def __init__(self, titulo, autor, año, disponible):
        self.titulo = titulo
        self.autor = autor
        self.año=año
        self.disponible = disponible

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return f'El libro "{self.titulo}" ha sido prestado con exito.'
        else:
            return f'El libro "{self.titulo}" no está disponible para préstamo.'
    def devolver(self):
        self.disponible = True
        return f'El libro "{self.titulo}" ha sido devuelto con exito.'
class libroDigital(libro):
    def __init__(self, titulo, autor, año, disponible, formato, tamañoMB):
        super().__init__(titulo, autor, año, disponible)
        self.formato = formato
        self.tamañoMB = tamañoMB
        self.disponible = True
    def prestar(self):
        return f'Se descargo con exito.'
class biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        return f'El libro "{libro.titulo}" ha sido agregado a la biblioteca.'

    def listar_libros(self):
        if self.libros[0] == []:
            return "No hay libros en la biblioteca."
        listado = "Libros en la biblioteca:\n"
        for libro in self.libros:
            if(libro.disponible):
                estado = "Disponible"
            else:
                estado = "No disponible"
            listado += f'Título: {libro.titulo}, Autor: {libro.autor}, Año: {libro.año}, Estado: {estado}\n'
        return listado
try:
    biblioteca_mi = biblioteca()
    while True:
        accion = input("Seleccione una acción:\n1. Agregar libro\n2. Agregar libro digital\n3. Listar libros\n4. Prestar libro\n5. Devolver libro\n6. Buscar libros de un autor\n7. Salir\n")
        if accion == "1":
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            año = input("Ingrese el año del libro: ")
            nuevo_libro = libro(titulo, autor, año, True)
            print(biblioteca_mi.agregar_libro(nuevo_libro))
        elif accion == "2":
            titulo = input("Ingrese el título del libro digital: ")
            autor = input("Ingrese el autor del libro digital: ")
            año = input("Ingrese el año del libro digital: ")
            formato = input("Ingrese el formato del libro digital (e.g., PDF, EPUB): ")
            tamañoMB = float(input("Ingrese el tamaño en MB del libro digital: "))
            nuevo_libro_digital = libroDigital(titulo, autor, año, True, formato, tamañoMB)
            print(biblioteca_mi.agregar_libro(nuevo_libro_digital))
        elif accion == "3":
            print(biblioteca_mi.listar_libros())
        elif accion == "4":
            titulo_prestamo = input("Ingrese el título del libro a prestar: ")
            for libro in biblioteca_mi.libros:
                if libro.titulo == titulo_prestamo:
                    print(libro.prestar())
                    break
            else:
                print(f'El libro "{titulo_prestamo}" no se encuentra en la biblioteca.')
        elif accion == "5":
            titulo_devolucion = input("Ingrese el título del libro a devolver: ")
            for libro in biblioteca_mi.libros:
                if libro.titulo == titulo_devolucion:
                    print(libro.devolver())
                    break
            else:
                print(f'El libro "{titulo_devolucion}" no se encuentra en la biblioteca.')
        elif accion == "6":
            autor_busqueda = input("Ingrese el autor cuyos libros desea buscar: ")
            encontrados = []
            for libro in biblioteca_mi.libros:
                if libro.autor.lower() == autor_busqueda.lower():
                    encontrados.append(libro)
            if encontrados:
                print(f'Libros del autor "{autor_busqueda}":')
                for libro in encontrados:
                    estado = "Disponible" if libro.disponible else "No disponible"
                    print(f'Título: {libro.titulo}, Año: {libro.año}, Estado: {estado}')
            else:
                print(f'No se encontraron libros del autor "{autor_busqueda}".')
        elif accion == "7":
            print("Saliendo del programa.")
            break
        else:
            print("Acción no reconocida. Por favor intente de nuevo.")
except Exception as e:
    print(f"Ocurrió un error: {e}")