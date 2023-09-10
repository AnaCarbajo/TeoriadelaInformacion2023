from tkinter import Tk
from tkinter.filedialog import askopenfilename

def validar_archivo_wav(archivo):
    try:
        with open(archivo, 'rb') as file:
            cabecera = file.read(12)
            return b'RIFF' == cabecera[:4] and b'WAVE' == cabecera[8:12] #comprobamos que los primeros cuatro bits sean 'RIFF' Y los otros 4 bits 'WAV'
    except IOError:
        return False

def mostrar_cabecera_wav(archivo):
    with open(archivo, 'rb') as file:
        cabecera = file.read(44)

        #Extraemos información de la cabecera
        ChunkID = cabecera[:4].decode('ascii')
        ChunkSize = int.from_bytes(cabecera[4:8], byteorder='little')
        Format = cabecera[8:12].decode('ascii')
        Subchunk1ID = cabecera[12:16].decode('ascii')
        Subchunk1Size = int.from_bytes(cabecera[16:20], byteorder='little')
        AudioFormat = int.from_bytes(cabecera[20:22], byteorder='little')
        NumChannels = int.from_bytes(cabecera[22:24], byteorder='little')
        SampleRate = int.from_bytes(cabecera[24:28], byteorder='little')
        ByteRate = int.from_bytes(cabecera[28:32], byteorder='little')
        BlockAlign = int.from_bytes(cabecera[32:34], byteorder='little')
        BitsPerSample = int.from_bytes(cabecera[34:36], byteorder='little')
        Subchunk2ID = cabecera[36:40].decode('ascii')
        Subchunk2Size = int.from_bytes(cabecera[40:44], byteorder='little')

        print("Cabecera del archivo WAV:")
        print(f"-Identificador RIFF: {ChunkID}")
        print(f"-Tamanio del archivo: {ChunkSize} bytes")
        print(f"-Formato WAVE: {Format}")
        print(f"-Identificador del chunk fmt: {Subchunk1ID}")
        print(f"-Tamanio del chunk fmt: {Subchunk1Size} bytes")
        print(f"-Formato de audio (1 significa PCM sin compresion): {AudioFormat}")
        print(f"-Numero de canales(1 MONO, 2 STEREO): {NumChannels}")
        print(f"-Frecuencia de muestreo: {SampleRate} Hz")
        print(f"-Velocidad de bits (byte rate): {ByteRate } bytes/segundo")
        print(f"-Tamanio de bloque (block align): {BlockAlign} bytes")
        print(f"-Bits por muestra: {BitsPerSample}")
        print(f"-Identificador del chunk data: {Subchunk2ID}")
        print(f"-Tamanio del chunk data: {Subchunk2Size} bytes")

if __name__ == "__main__":
    print("Por favor ingrese un archivo para validar")
    Tk().withdraw()
    archivo = askopenfilename()
    if validar_archivo_wav(archivo):
        print("El archivo ingresado es un archivo WAV")
        mostrar_cabecera_wav(archivo)
    else:
        print("El archivo no es un archivo WAV valido.")