import os
from os import system
from time import sleep
import csv

class personalInformation:

    def __init__(self, name:str, address:str, dni:str, primaryStudies:bool, secondaryStudies:bool, universityStudies:bool, ownHome:bool, healthInsurance:bool, works:bool):
        self.name = name.ljust(40)[0:40].rstrip()       
        self.address = address.ljust(40)[0:40].rstrip() 
        self.dni = dni.ljust(40)[0:40].rstrip()       
        self.primaryStudies = primaryStudies                          
        self.secondaryStudies = secondaryStudies                          
        self.universityStudies = universityStudies                          
        self.ownHome = ownHome                          
        self.healthInsurance = healthInsurance                         
        self.works = works                             

    def toFixedLengthBytes(self):
        bytes = []
        bytes += bytearray(self.name.ljust(40), "UTF-8")
        bytes += bytearray(self.address.ljust(40), "UTF-8")
        bytes += bytearray(self.dni.ljust(40), "UTF-8")
        bytes += self.primaryStudies.to_bytes(1, byteorder='big')
        bytes += self.secondaryStudies.to_bytes(1, byteorder='big')
        bytes += self.universityStudies.to_bytes(1, byteorder='big')
        bytes += self.ownHome.to_bytes(1, byteorder='big')
        bytes += self.healthInsurance.to_bytes(1, byteorder='big')
        bytes += self.works.to_bytes(1, byteorder='big')
        return bytes

    def toVariableLengthBytes(self):
        bytes = []
        bytes += len(self.name).to_bytes(1, byteorder='big') + bytearray(self.name, "UTF-8")
        bytes += len(self.address).to_bytes(1, byteorder='big') + bytearray(self.address, "UTF-8")
        bytes += len(self.dni).to_bytes(1, byteorder='big') + bytearray(self.dni, "UTF-8")
        byteSINO = 0
        if(self.primaryStudies): byteSINO += 32
        if(self.secondaryStudies): byteSINO += 16
        if(self.universityStudies): byteSINO += 8
        if(self.ownHome): byteSINO += 4
        if(self.healthInsurance):byteSINO += 2
        if(self.works): byteSINO += 1
        bytes += byteSINO.to_bytes(1, byteorder='big')
        return bytes
    

def writeBytes(filename, bytes):
    with open(filename,'wb') as file:
        for i in bytes:
            file.write(i.to_bytes(1, byteorder='big'))

def readBytes(filename):
    bytes = []
    
    with open(filename,'rb') as file:
        while True:
            b = file.read(1)
            if not b:
                break
            bytes.append(int.from_bytes(b, byteorder='big'))
    return bytes      

def readFile():
    with open('personas.csv', mode='r', newline='') as archivo_csv:  
        lector_csv = csv.DictReader(archivo_csv, delimiter=';')  
        informationPersons = []
        for row in lector_csv:
            informationPerson = personalInformation(row['Nombre'],
                row['Direccion'],
                row['dni'],
                row['EstudiosPrimarios'] == 'Si',
                row['EstudiosSecundarios'] == 'Si',
                row['EstudiosUniversitarios'] == 'Si',
                row['viviendaPropia'] == 'Si',
                row['obraSocial'] == 'Si',
                row['trabaja'] == 'Si'
            )
            informationPersons.append(informationPerson)
    return informationPersons


def savePersonsFixedLengthBytes(dataPersons):
    os.system("cls")
    print('Guardar datos en archivo de longitud fija:')

    if(len(dataPersons) == 0):
        print(' ** No hay personas cargadas **')
        sleep(1)
        input(' ** Enter para regresar al menu **')
    else:
        try:
            basePath = os.getcwd()
            filePathFijos   = rf'{basePath}\fijos.dat'

            bytes = []
            for p in map(personalInformation.toFixedLengthBytes, dataPersons) : bytes+=p
            writeBytes(filePathFijos, bytes)

            print(' ** Se guardaron los datos de forma correcta **')
            print('[dirPath]: ' + filePathFijos)
            sleep(1)
            input(' ** Enter para regresar al menu **')
        except: 
            print(' ** Error al escribir el archivo **')
            print('[dirPath]: ' + filePathFijos)
            sleep(1)
            input(' ** Enter para regresar al menu **')

def savePersonsVariableLengthBytes(dataPersons):
    os.system("cls")
    print('Guardar datos en archivo de longitud variable:')
    
    if(len(dataPersons) == 0):
        print(' ** No hay personas cargadas **')
        sleep(1)
        input(' ** Enter para regresar al menu **')
    else:
        try:
            basePath = os.getcwd()
            filePathVariables   = rf'{basePath}\variables.dat'

            bytes = []
            for p in map(personalInformation.toVariableLengthBytes, dataPersons) : bytes+=p
            writeBytes(filePathVariables, bytes)

            print(' ** Se guardaron los datos de forma correcta **')
            print('[dirPath]: ' + filePathVariables)
            sleep(1)
            input(' ** Enter para regresar al menu **')
        except: 
            print(' ** Error al escribir el archivo **')
            print('[dirPath]: ' + filePathVariables)
            sleep(1)
            input(' ** Enter para regresar al menu **')

def loadPersonsFixedLengthBytes(dataPersons:list):
    os.system("cls")
    print('Cargar datos desde el archivo de longitud fija:')

    try:
        basePath = os.getcwd()
        filePathFijos = rf'{basePath}\fijos.dat'
        bytes = readBytes(filePathFijos)
    except: 
        print(' ** Error al leer el archivo **')
        print('[dirPath]: ' + filePathFijos)
        sleep(1)
        input(' ** Enter para regresar al menu **') 
        return []
    
    next = 0
    while next < len(bytes):
        try:
            pointer = next
            nChar = 40
            next = pointer + nChar
            name = ''.join(map(chr,bytes[pointer:next]))

            pointer = next
            next = pointer + nChar
            address = ''.join(map(chr,bytes[pointer:next]))

            pointer = next
            next = pointer + nChar
            dni = ''.join(map(chr,bytes[pointer:next]))

            pointer = next
            primaryStudies = bool(bytes[pointer])
            secondaryStudies = bool(bytes[pointer+1])
            universityStudies = bool(bytes[pointer+2])
            ownHome = bool(bytes[pointer+3])
            healthInsurance = bool(bytes[pointer+4])
            works = bool(bytes[pointer+5])
            next = pointer + 6

            dataPersons.append(personalInformation(name.strip(),address.strip(),dni.strip(),primaryStudies,secondaryStudies,universityStudies,ownHome,healthInsurance,works))
        except:
            print(' ** Error al leer el archivo **')
            print('[dirPath]: ' + filePathFijos)
            sleep(1)
            input(' ** Enter para regresar al menu **') 
            return []
    
    print(' ** Se cargaron los datos de forma correcta **')
    for persona in dataPersons:
        print(' Nombre y apellido: ' + persona.name + '  Direccion:' + persona.address + '  DNI:' + persona.dni)
 
    print('[dirPath]: ' + filePathFijos)
    sleep(1)
    input(' ** Enter para regresar al menu **')        
    return dataPersons

def loadPersonsVariableLengthBytes(dataPersons:list):
    os.system("cls")
    print('Cargar datos desde el archivo de longitud variable:')
    try:
        basePath = os.getcwd()
        filePathVariables   = rf'{basePath}\variables.dat'
        bytes = readBytes(filePathVariables)
    except: 
        print(' ** Error al leer el archivo **')
        print('[dirPath]: ' + filePathVariables)
        sleep(1)
        input(' ** Enter para regresar al menu **') 
        return []
    
    next = 0
    while next < len(bytes):
        try:
            pointer = next
            nChar = bytes[pointer]
            next = pointer + nChar + 1
            name = ''.join(map(chr,bytes[pointer+1:next]))

            pointer = next
            nChar = bytes[pointer]
            next = pointer + nChar + 1
            address = ''.join(map(chr,bytes[pointer+1:next]))

            pointer = next
            nChar = bytes[pointer]
            next = pointer + nChar + 1
            dni = ''.join(map(chr,bytes[pointer+1:next]))

            pointer = next
            nChar = bytes[pointer]
            next = pointer + 1

            primaryStudies = bool(nChar&3)
            secondaryStudies = bool(nChar&16)
            universityStudies  = bool(nChar&8)
            ownHome = bool(nChar&4)
            healthInsurance = bool(nChar&2)
            works  = bool(nChar&1)


            dataPersons.append(personalInformation(name,address,dni,primaryStudies,secondaryStudies,universityStudies,ownHome,healthInsurance,works))
        except:
            print(' ** Error al leer el archivo **')
            print('[dirPath]: ' + filePathVariables)
            sleep(1)
            input(' ** Enter para regresar al menu **') 
            return []
    
    print(' ** Se cargaron los datos de forma correcta **')
    print('[dirPath]: ' + filePathVariables)
    for persona in dataPersons:
        print(' Nombre y apellido: ' + persona.name + '  Direccion:' + persona.address + '  DNI:' + persona.dni)
    sleep(1)
    input(' ** Enter para regresar al menu **')       
    return dataPersons


def program():
    personas = readFile()
    while(True):
        os.system("cls")
        print(' Menu')
        print(' 0. Salir')
        print(' 1. Guardar datos en archivo de longitud fija')
        print(' 2. Guardar datos en archivo de longitud variable')
        print(' 3. Cargar datos desde el archivo de longitud fija')
        print(' 4. Cargar datos desde el archivo de longitud variable')
        
        option = input(" > ")
        try:
            option = int(option)
            if(option in range(0,8)):
                if  (option == 0): break
                elif(option == 1): savePersonsFixedLengthBytes(personas)
                elif(option == 2): savePersonsVariableLengthBytes(personas)
                elif(option == 3): personas = loadPersonsFixedLengthBytes(personas)
                elif(option == 4): personas = loadPersonsVariableLengthBytes(personas)
            else: 
                print(' ** Ingrese una opcion valida **')
                sleep(1)
        except:
            print(' ** Ingrese una opcion valida **')
            sleep(1)

program()

#Llegamos a la conclusion que el archivo de longitud fija utiliza mas espacio que el de longitud variable
