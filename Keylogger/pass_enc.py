from cryptography.fernet import Fernet

def generar_clave():
    key = Fernet.generate_key()
    with open('clave.encriptacion', 'wb') as file:
        file.write(key)

