# Librerías de Python 📚📜

A continuacion mostrare un ejemplo de como instalar librerias de Python.

###Instalacion de libreria cryptography:

1- Descargar  fichero .whl :
        
    https://pypi.org/project/cryptography/#files

2- Desde la terminal, en mi caso windows, posicionarnos sobre la carpeta donde descargamos el archivo y usar el 
siguiente comando:

    pip install <nombre_fichero>.whl

luego presionar enter

3-Para verificar que la librería este instalada, accedemos a python. Seleccionamos import + nombre de libreria. Si da 
error es porque no esta instalada


En el siguiente ejemplo, vemos como las librerías  pynput  y datetime estan instaladas, mientras que criptography no

    C:\Users\Manu>python
    Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import pynput
    >>> import datetime
    >>> import cryptography
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    ModuleNotFoundError: No module named 'cryptography'
    >>>