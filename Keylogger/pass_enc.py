from cryptography.fernet import Fernet

def generar_clave():
    key = Fernet.generate_key()
    with open('clave.encriptacion', 'wb') as file:
        file.write(key)

def cargar_clave():
    return open('clave.encriptacion', 'rb').read()

generar_clave()

key = cargar_clave()

password = b'EjemploDeClave'

file = open('clave.encriptada', 'wb')
