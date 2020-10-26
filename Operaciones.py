from os import system
from DDBBoperacion import *
from Menu import *
from getpass import getpass
from DDBBusuario import *


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
    def transferir(cls):
        system('clear')
        print('Transferir plata\n')
        cantidad = int(input("Importe: "))
        destinatario = input("Email o teléfono del destinatario: ")
        pin = int(input("Pin: "))
        if DDBBoperacion.confirma_pin(pin):
            DDBBoperacion.transferencia(cls.id_usuario(), cantidad, DDBBusuario.get_id_usuario(destinatario))
        else:
            input("Pin incorrecto")

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
