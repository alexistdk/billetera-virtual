import os
from getpass import getpass
from DDBBusuario import *
from Menu import *


class Usuario:

    @classmethod
    def iniciar_sesion(cls):
        os.system('clear')
        print("Iniciar sesión\n")
        email = input("Email: ")
        contrasenia = getpass(prompt="Contraseña: ")
        if DDBBusuario.loguear_usuario(email, contrasenia):
            if DDBBusuario.tiene_pin(email) is not None:
                os.system('clear')
                cls.agregar_pin(email)
                Menu.menu_principal()
                Menu.elegir_opcion()
            else:
                Menu.menu_principal()
                Menu.elegir_opcion()
        else:
            input("Usuario y/o contraseña incorrectos. Intente nuevamente.")
            cls.pantalla_principal()

    @classmethod
    def registrar_usuario(cls):
        os.system('clear')
        print("Registrar usuario\n")
        email = input("Email: ")
        password = getpass(prompt="Contraseña: ")
        password_reingresada = getpass(prompt="Reingrese la contraseña: ")
        telefono = input("Telefono: ")
        if password == password_reingresada:
            if not DDBBusuario.email_registrado(email) and not DDBBusuario.telefono_registrado(telefono):
                DDBBusuario.registrar_usuario(email, password, telefono)
            elif DDBBusuario.email_registrado(email) and not DDBBusuario.telefono_registrado(telefono):
                input("Email ya registrado. Por favor, inicie sesión")
            elif not DDBBusuario.email_registrado(email) and DDBBusuario.telefono_registrado(telefono):
                input("Telefono ya registrado. Por favor, inicie sesión")
            else:
                input("Email y teléfono ya registrado. Por favor, inicie sesión")
                cls.pantalla_principal()

    @classmethod
    def pantalla_principal(cls):
        os.system('clear')
        print("1. Iniciar sesión")
        print("2. Registrarse\n")
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            cls.iniciar_sesion()
        elif opcion == 2:
            cls.registrar_usuario()
        else:
            input("Opción inválida. Intente nuevamente.")
            cls.pantalla_principal()

    @classmethod
    def agregar_pin(cls, email):
        print("Solo se le pedirá el pin para confirmar las operaciones")
        pin = int(input("Pin: "))
        reingresa_pin = int(input("Reingresar pin: "))
        if pin is reingresa_pin:
            DDBBusuario.agregar_pin(email, pin)
        else:
            input("Los pin no coinciden. Intente nuevamente")
            cls.agregar_pin(email)
