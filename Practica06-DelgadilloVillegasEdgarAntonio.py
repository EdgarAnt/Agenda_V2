#Agenda V2
#Delgadillo Villegas Edgar Antonio
import os
archivo = open("AgendaV2.txt", 'w')
archivo.write("Agenda\n")
archivo.close()


class Estudiante:
    nom2 = " "
    tel2 = " "
    carrera = " "
    codigo = " "


    def __init__(self):
        self.nom2 = "Sin_nombre"
        self.carrera = "Sin_carrera"
        self.codigo = 0
        self.tel2 = 0


    def set_code(self, cod):
        self.codigo = cod
    def set_nom(self, nom):
        self.nombre = nom
    def set_tel(self, tel):
        self.tel2 = tel
    def set_car(self, car):
        self.carrera = car

    def get_car(self):
        return self.carrera
    def get_car(self):
        return self.tel2
    def get_nom(self):
        return self.nom2
    def get_code(self):
        return self.codigo

    def insertar(self, nom, cod, car, tel):
        print("\t Datos del estudiante:")
        archivo = open("AgendaV2.txt", "a")
        self.nom2 = nom
        self.carrera = car
        self.tel2 = tel
        self.codigo = cod
        data = self.nom2 + "\t" + self.codigo + "\t" + self.carrera + "\t" + self.tel2 + "\n"
        archivo.write(data)
        archivo.close()

    def mod(self, cod):

        print("\tQue dato desea eliminar del estudiante? ")
        print("\t1) Nombre")
        print("\t2) Codigo")
        print("\t3) Carrera")
        print("\t4) Telefono")
        print("\t5) Todo")
        resp = input("\tRespuesta: ")
        resp = int(resp)
        return resp

    def buscarNom(self, nom):
        archivo = open("AgendaV2.txt","r")
        data = archivo.readlines()
        for i in data:
            if nom in i:
                print(i)
                break
        else:
            print(" Dato inexistente ")
        archivo.close()

    def buscarCode(self, cod):
        archivo = open("AgendaV2.txt", "r")
        data = archivo.readlines()
        for i in data:
            if cod in i:
                print(i)
                break
        else:
            print("Estudiante no encontrado")
        archivo.close()

    def eliminar(self, nom):
        archivo = open("AgendaV2.txt", "r")
        data = archivo.readlines()
        archivo.close()

        archivo = open("AgendaV2.txt", "w")
        for i in data:
            if nom in i:
                nom = ""
            else:
                print("\tEl dato no esta")
                archivo.write(i)
        archivo.close()

    def mostrar(self):
        archivo = open("AgendaV2.txt", "r")
        read = archivo.read()
        if read == "":
            print("\tArchivo vacio")
        else:
            print(read)
        archivo.close()

while True:
    os.system("cls")
    estudiante = Estudiante()

    print("-----------------------------")
    print("      Agenda de estudiantes")
    print("-----------------------------\n")
    print("\t\t1) Agregar ")
    print("\t\t2) Mostrar ")
    print("\t\t3) Buscar (nombre)")
    print("\t\t4) Buscar estudiante (codigo)")
    print("\t\t5) Eliminar ")
    print("\t\t6) Modificar ")
    print("\t\t7) Salir")
    opc = input("\n\t\tOpcion: ")
    opc = int(opc)

    if opc == 1:
        print("\tIntroducir alumno: ")
        nom = input("\tNombre: ")
        cod = input("\tCodigo: ")
        car = input("\tCarrera: ")
        tel = input("\tTelefono: ")
        estudiante.insertar(nom, cod, car, tel)
    elif opc == 2:
        print("----------------------------")
        print("            mostrar:        ")
        print("-----------------------------")
        print("\tEstudiantes registrados: ")
        estudiante.mostrar()

    elif opc == 3:
        print("----------------------------")
        print("         Buscar nombre:       ")
        print("-----------------------------")
        nom = input("\tIngresar nombre: ")
        estudiante.buscarNom(nom)
    elif opc == 4:
        print("----------------------------")
        print("            Buscar codigo:        ")
        print("-----------------------------")
        cod = input("\tIngresar codigo: ")
        estudiante.buscarNom(cod)
    elif opc == 5:
        print("----------------------------")
        print("            Eliminar:        ")
        print("-----------------------------")
        nom = input("\tIngresar nombre: ")
        estudiante.eliminar(nom)
    elif opc == 6:
        print("----------------------------")
        print("    Modificar estudiante:    ")
        print("-----------------------------")
        cod = input("\tIngresar codigo: ")
        if estudiante.buscarCode(cod):
            opc = estudiante.mod(cod)
            if opc == 1:
                nom = input("\tEscribe el nuevo nombre: ")
                estudiante.set_nom(nom)
            elif opc == 2:
                cod = input("\tEscribe el nuevo codigo: ")
                estudiante.set_code(cod)
            elif opc == 3:
                car = input("\tEscribe el nuevo carrera: ")
                estudiante.set_car(car)
            elif opc == 4:
                tel = input("\tEscribe el nuevo telefono: ")
                estudiante.set_tel(tel)
            elif opc == 5:
                nom = input("\tEscribe el nuevo nombre: ")
                cod = input("\tEscribe el nuevo codigo: ")
                car = input("\tEscribe la nueva carrera: ")
                tel = input("\tEscribe el nuevo telefono: ")
                estudiante.set_nom(nom)
                estudiante.set_code(cod)
                estudiante.set_car(car)
                estudiante.set_tel(tel)
            else:
                print("\tEsa opcion es invalida")
    elif opc == 7:
        print("\tHasta luego :D")
        quit()
    else:
        print("\t\tOpcion invalida")