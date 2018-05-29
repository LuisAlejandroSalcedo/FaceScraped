# importamos las librerias necesarias
import sys
import os
try:
    from urllib import urlopen
except ImportError:
    from urllib.request import urlopen
from datetime import datetime
from random import randint

# Metodo para crear el directorio que contendra las imagenes
def create_dir(prefix):
    dir_c = os.path.join(os.getcwd(), prefix, datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
    try:
        os.makedirs(dir_c)
    except OSError as e:
        if e.errno != 17:
            pass
        else:
            print("Problemas al crear la carpeta.")
            exit
    return dir_c

# Función para obtener las imagenes mediante la url
def getUrl(name):
    return "http://graph.facebook.com/picture?id=" + name + "&width=800"


def getProfile(photoUrl, saveUrl):
    print("Descargando " + photoUrl + ".")
    response = urlopen(photoUrl)
    if response.geturl() != "https://static.xx.fbcdn.net/rsrc.php/v3/yo/r/UlIqmHJn-SK.gif":
        open(saveUrl, "wb").write(response.read())
        return True
    return False

# La función getImges sera la encargada de descargar todas las imganes y descargarlas
# en nuestro ordenador.
def getImages(sizeDataset):
    id = randint(1, int(1e4)) # 1e4 = 10000. id = 1 a 10000.
    photoCount = 0 # Numero de imagenes. Incrementara constantemente.
    folder = create_dir("face_data") # Creamos la carpeta que contendra las imagenes
    while photoCount < sizeDataset: # EL bucle se detendra al alcanzar el numero de imagenes indicadas.
        if getProfile(getUrl(str(id)), folder + "/" + str(id) + ".jpg"): # Guardamos las imagenes con formato ".jpg"
            photoCount += 1 # incrementamos la variable "photoCount"
            id += 1 # Cambiamos la id de la imagen
        else:
            id += 10
    print("\nImagenes creadas en la carpeta face_data.")
    print("Tamaño del set de datos: " + str(photoCount))
    return

# Función principal.
def main():
    arguments = list(sys.argv[1:]) # El argumento, el cual sera el numero de imagenes que se descargaran
    if len(arguments) == 1 and arguments[0].isdigit() and int(arguments[0]) < int(1e7):
        getImages(int(arguments[0]))
    else: # Si el argumento esta vacio, se le avisara al usuario.
        print("\nArgumenton incorrecto.")
        print("Utiliza: python FaceScraped.py <numero de imagenes (entero < 10,000,000)>")
    return

if __name__ == "__main__":
    main()