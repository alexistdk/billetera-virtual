from os import system
from DDBBoperacion import *
from Menu import *
from getpass import getpass


class Operaciones:

    id_usuario_logueado = 0

    @classmethod
    def usuario_logueado(cls, id_usuario): cls.id_usuario_logueado = id_usuario

    @classmethod
    def id_usuario(cls): return cls.id_usuario_logueado

    @classmethod
    def pagar(cls):
        system('clear')
        print("Pagar\n")
        cantidad = input("Importe: ")
        pin = getpass(prompt="Ingrese el pin: ")
        if DDBBoperacion.confirma_pin(pin, cls.id_usuario()):
            if DDBBoperacion.saldo_suficiente(cls.id_usuario(), cantidad):
                DDBBoperacion.pagar(cls.id_usuario(), cantidad)
            else:
                input("Saldo insuficiente")
        else:
            input("Pin incorrecto")

    @classmethod
    def transferir(cls): print("Transferir")

    @classmethod
    def ingresar_dinero(cls):
        system('clear')
        print("Ingresar dinero\n")
        cantidad = int(input("Importe: "))
        pin = getpass(prompt="Ingrese el pin: ")
        if DDBBoperacion.confirma_pin(pin, cls.id_usuario()):
            DDBBoperacion.ingresar_dinero(cls.id_usuario(), cantidad)
        else:
            input("Pin incorrecto")

    @classmethod
    def mostrar_operaciones(cls):
        system('clear')
        print("Operaciones realizadas\n")
        DDBBoperacion.listar_operaciones(cls.id_usuario())
