from tkinter import Tk
from tkinter.filedialog import askopenfilename

def validar_archivo_bmp(archivo):
    try:
        with open(archivo, 'rb') as file:
            Signaturecabecera = file.read(2)
            return b'BM' == Signaturecabecera
    except IOError:
        return False

def mostrar_cabecera_bmp(archivo):
    with open(archivo, 'rb') as file:
        cabecera = file.read(14)

        # Extraemos información de la cabecera
        Signature = cabecera[:2].decode('ascii')
        FileSize = int.from_bytes(cabecera[2:6], byteorder='little')
        DataOffset = int.from_bytes(cabecera[10:14], byteorder='little')
        

        print("Cabecera del archivo BMP:")
        print(f"-Identificador BMP: {Signature}")
        print(f"-Tamanio del fichero: {FileSize} bytes")
        print(f"-Posicion relativa del comienzo de los datos de imagen: {DataOffset}")
        

if __name__ == "__main__":
    print("Por favor ingrese un archivo para validar")
    Tk().withdraw()
    archivo = askopenfilename()
    if validar_archivo_bmp(archivo):
        print("El archivo ingresado es un archivo BMP")
        mostrar_cabecera_bmp(archivo)
    else:
        print("El archivo no es un archivo BMP valido.")