import os
from Operacion import *


class Menu:

    @staticmethod
    def menu_principal():
        os.system('clear')
        opcion1 = "1. Pagar"
        opcion2 = "2. Transferir dinero"
        opcion3 = "3. Ingresar dinero"
        opcion4 = "4. Mostrar operaciones"
        opciones = [opcion1, opcion2, opcion3, opcion4]
        for i in range(len(opciones)):
            print(opciones[i])

    @classmethod
    def elegir_opcion(cls):
        opcion = int(input("\nElija una opción: "))
        if opcion == 1:
            Operacion.pagar()
            cls.volver_al_menu()
        if opcion == 2:
            Operacion.transferir()
            cls.volver_al_menu()
        if opcion == 3:
            Operacion.ingresar_dinero()
            cls.volver_al_menu()
        if opcion == 4:
            Operacion.mostrar_operaciones()
            cls.volver_al_menu()
        else:
            input("Opción incorrecta. Presione cualquier tecla para ingresar una opción válida")
            os.system('clear')
            cls.menu_principal()
            cls.elegir_opcion()

    @classmethod
    def volver_al_menu(cls):
        input("Presione cualquier tecla para continuar...")
        os.system('clear')
        cls.menu_principal()
        cls.elegir_opcion()

