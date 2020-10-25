from ConectarDDBB import *


class DDBBusuario(ConectarDDBB):

    @classmethod
    def loguear_usuario(cls, email_usuario, password):
        try:
            db = cls.conexion()
            cursor = db.cursor()
            cursor.execute('CALL LoguearUsuario(%s, %s)', [email_usuario, password])
            return cursor.fetchone()[0]
        except Error:
            print("Error", Error)

    @classmethod
    def registrar_usuario(cls, email, password, telefono):
        try:
            db = cls.conexion()
            cursor = db.cursor()
            cursor.execute('CALL RegistrarUsuario(%s, %s, %s)', [email, password, telefono])
            db.commit()
        except Error:
            print("Error", Error)

    @classmethod
    def tiene_pin(cls, email):
        try:
            db = cls.conexion()
            cursor = db.cursor()
            cursor.execute('CALL ExistePin(%s)', [email])
            return cursor.fetchone()[0]
        except Error:
            print("Error", Error)

    @classmethod
    def agregar_pin(cls, email, pin):
        try:
            db = cls.conexion()
            cursor = db.cursor()
            cursor.execute('CALL AgregarPin(%s, %s)', [email, pin])
            db.commit()
        except Error:
            print("Error", Error)

    @classmethod
    def existe_usuario(cls, email, telefono):
        try:
            db = cls.conexion()
            cursor = db.cursor()
            cursor.execute('CALL ExisteUsuario(%s, %s)', [email, telefono])
            return cursor.fetchone()[0]
        except Error:
            print("Error", Error)
