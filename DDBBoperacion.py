from ConectarDDBB import *
from datetime import date
from Operaciones import *


class DDBBoperacion(ConectarDDBB):

    @classmethod
    def ingresar_dinero(cls, id_usuario, cantidad):
        fecha = date.today()
        try:
            db = cls.conexion()
            cursor = db.cursor()
            cursor.execute('CALL IngresarDinero(%s, %s, %s)', [id_usuario, cantidad, fecha])
            db.commit()
        except Error:
            print("Error", Error)

    @classmethod
    def confirma_pin(cls, pin, id_usuario):
        try:
            db = cls.conexion()
            cursor = db.cursor()
            cursor.execute('CALL ConfirmaPin(%s, %s)', (pin, id_usuario))
            return cursor.fetchone()[0]
        except Error:
            print("Error", Error)

    @classmethod
    def saldo_suficiente(cls, id_usuario, cantidad):
        try:
            db = cls.conexion()
            cursor = db.cursor()
            cursor.execute('CALL SaldoSuficiente%s, %s)', [cantidad, id_usuario])
            return cursor.fetchone()[0]
        except Error:
            print("Error", Error)

    @classmethod
    def pagar(cls, id_usuario, cantidad):
        fecha = date.today()
        try:
            db = cls.conexion()
            cursor = db.cursor()
            cursor.execute('CALL PAGAR(%s, %s, %s)', [id_usuario, cantidad, fecha])
            db.commit()
        except Error:
            print("Error", Error)

    @classmethod
    def listar_operaciones(cls, id_usuario):
        try:
            db = cls.conexion()
            cursor = db.cursor()
            cursor.execute('CALL MostrarOperaciones(%s)', [id_usuario])
            operaciones = cursor.fetchall()
            for row in operaciones:
                print("Fecha: ", row[1])
                print("Tipo: ", row[2])
                print("Importe: ", row[3])
        except Error:
            print("Error", Error)

    @classmethod
    def transferencia(cls, id_usuario, cantidad, destinatario):
        fecha = date.today()
        try:
            db = cls.conexion()
            cursor = db.cursor()
            cursor.execute("CALL Transferir(%s, %s, %s, %s)", [id_usuario, cantidad, destinatario, fecha])
        except Error:
            print("Error", Error)
