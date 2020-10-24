from ConectarDDBB import *


class DDBBusuario(ConectarDDBB):

    @classmethod
    def loguear_usuario(cls, email_usuario, password):
        try:
            db = cls.conexion()
            cursor = db.cursor()
            existe_usuario = cursor.callproc('LoguearUsuario', [email_usuario, password])
            return existe_usuario[0]
        except Error:
            print("Error", Error)

    @classmethod
    def registrar_usuario(cls, email, password, telefono):
        try:
            db = cls.conexion()
            cursor = db.cursor()
            cursor.callproc('RegistrarUsuario', [email, password, telefono])
        except Error:
            print("Error", Error)
        finally:
            db.commit()

    @classmethod
    def email_registrado(cls, email):
        try:
            db = cls.conexion()
            cursor = db.cursor()
            existe_email = cursor.callproc('ExisteEmail', [email])
            return existe_email[0]
        except Error:
            print("Error", Error)

    @classmethod
    def telefono_registrado(cls, telefono):
        try:
            db = cls.conexion()
            cursor = db.cursor()
            existe_telefono = cursor.callproc('ExisteTelefono', [telefono])
            return existe_telefono[0]
        except Error:
            print("Error", Error)
