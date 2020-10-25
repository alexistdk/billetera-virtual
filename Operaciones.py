import os
from DDBBoperacion import *
from Menu import *


class Operaciones:

    id_usuario_logueado = 0

    @classmethod
    def usuario_logueado(cls, id_usuario): cls.id_usuario_logueado = id_usuario

    @classmethod
    def id_usuario(cls): return cls.id_usuario_logueado

    @classmethod
    def pagar(cls): print("Pagar")

    @classmethod
    def transferir(cls): print("Transferir")

    @classmethod
    def ingresar_dinero(cls):
        os.system('clear')
        print("Ingresar dinero\n")
        cantidad = int(input("Cantidad a ingresar: "))
        pin = int(input("Ingrese el pin: "))
        if DDBBoperacion.confirma_pin(pin, cls.id_usuario):
            DDBBoperacion.ingresar_dinero(cls.id_usuario, cantidad)
            DDBBoperacion.registrar_ingreso(cls.id_usuario, cantidad)
        else:
            input("Pin incorrecto")

    @classmethod
    def mostrar_operaciones(cls): print("Mostrar operaciones")
