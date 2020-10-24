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
            db.commit()
        except Error:
            print("Error", Error)

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
            existe = cursor.callproc('ExisteTelefono', [telefono])
            return existe[0]
        except Error:
            print("Error", Error)

    @classmethod
    def tiene_pin(cls, email):
        try:
            db = cls.conexion()
            cursor = db.cursor()
            return cursor.callproc('ExistePin', [email])[0]
        except Error:
            print("Error", Error)

    @classmethod
    def agregar_pin(cls, email, pin):
        try:
            db = cls.conexion()
            cursor = db.cursor()
            return cursor.callproc('AgregarPin', [email, pin])[0]
        except Error:
            print("Error", Error)
