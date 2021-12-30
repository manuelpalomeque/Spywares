# Librerías de Python 📚📜

A continuacion mostrare un ejemplo de como instalar librerias de Python.

### Instalación de librería cryptography:

1- Descargar  fichero .whl :
        
    https://pypi.org/project/cryptography/#files

2- Desde la terminal, en mi caso windows, posicionarnos sobre la carpeta donde descargamos el archivo y usar el 
siguiente comando:

    pip install <nombre_fichero>.whl

luego presionar enter:

    D:\Programacion\Librerias Python\cryptography>dir
     El volumen de la unidad D es Datos
     El número de serie del volumen es: 35D5-3X5D
    
     Directorio de D:\Programacion\Librerias Python\cryptography
    
    30/12/2021  01:54 p. m.    <DIR>          .
    30/12/2021  01:54 p. m.    <DIR>          ..
    30/12/2021  01:54 p. m.         2.188.060 cryptography-36.0.1-cp36-abi3-win_amd64.whl
                   1 archivos      2.188.060 bytes
                   2 dirs  1.696.085.364.736 bytes libres
    
    D:\Programacion\Librerias Python\cryptography>pip install cryptography-36.0.1-cp36-abi3-win_amd64.whl
    Defaulting to user installation because normal site-packages is not writeable
    Processing d:\programacion\librerias python\cryptography\cryptography-36.0.1-cp36-abi3-win_amd64.whl
    Collecting cffi>=1.12
      Downloading cffi-1.15.0-cp310-cp310-win_amd64.whl (180 kB)
         |████████████████████████████████| 180 kB 3.2 MB/s
    Collecting pycparser
      Downloading pycparser-2.21-py2.py3-none-any.whl (118 kB)
         |████████████████████████████████| 118 kB 6.8 MB/s
    Installing collected packages: pycparser, cffi, cryptography
    Successfully installed cffi-1.15.0 cryptography-36.0.1 pycparser-2.21
    
    
    D:\Programacion\Librerias Python\cryptography>


3-Para verificar que la librería este instalada, accedemos a python. Seleccionamos import + nombre de libreria. Si da 
error es porque no esta instalada


En el siguiente ejemplo, vemos como las librerías  pynput  y datetime estan instaladas, mientras que criptography no

    C:\Users\User1>python
    Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import pynput
    >>> import datetime
    >>> import cryptography
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    ModuleNotFoundError: No module named 'cryptography'
    >>>