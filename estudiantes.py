estudiantes = []


def agregar_estudiante(nombre):
    estudiantes.append(nombre)


def mostrar_estudiantes():
    print("Lista de estudiantes")

    if len(estudiantes) == 0:
        print("No hay estudiantes registrados")
    else:
        for estudiante in estudiantes:
            print("-", estudiante)


agregar_estudiante("James Reyes")
agregar_estudiante("Felipe Paez")

mostrar_estudiantes()