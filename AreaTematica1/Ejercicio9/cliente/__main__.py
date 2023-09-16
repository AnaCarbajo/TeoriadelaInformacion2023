import socket
CANTIDAD_DE_CARACTERES=3


HOST = "192.168.1.55" #45.175.103.153
PORT =  5555
BUFSIZ = 1024


def codificador(x):
    cadena=bytearray()
    i=0
    j=0
    byte=int('00000000',2)
    xbytes=(len(x)/3)+1
    #print(xbytes)
    while j<int(xbytes):
        cadena.append(byte)
        j=j+1
    #print(" la cadena inicial " + str(cadena))   
    #print(cadena[0]) 
    #print(cadena[1]) 
    bytecadena=0
    cant=CANTIDAD_DE_CARACTERES
    while i<len(x):
        bits=8
        while bits>0 and i<len(x):
            #print("cant: "+str(cant)+"  bits: "+ str(bits))
            if cant!=CANTIDAD_DE_CARACTERES:
                #print("Aux ejecutado")
                cadena[bytecadena]=cadena[bytecadena]|aux<<bits-cant
                bits=bits - cant
                cant=CANTIDAD_DE_CARACTERES
                i=i+1
            else:                 
                if x[i]=="A":
                    letra=int('000',2)
                elif x[i]=="B":
                    letra=int("001",2)
                elif x[i]=="C":
                    letra=int("010",2)
                elif x[i]=="D":
                    letra=int("011",2)
                elif x[i]=="E":
                    letra=int("100",2)
                elif x[i]=="F":
                    letra=int("101",2)
                elif x[i]=="G":
                    letra=int("110",2)
                elif x[i]=="H":
                    letra=int("111",2)
                #print("letra " +x[i]+"  "+ bin(letra))
                if bits<CANTIDAD_DE_CARACTERES:
                    byte=int('00000000',2)
                    if bits==1:
                        byte=(byte|letra>>2)<<2
                        #print("la letra "+x[i]+" no entra en el byte actual, se necesita 2 bits mas. Se guardara "+bin(letra-byte)+" en el sig byte")
                    elif bits==2:
                        byte=(byte|letra>>1)<<1
                        #print("la letra "+x[i]+" no entra en el byte actual, se necesita 1 bit mas. Se guardara "+bin(letra-byte)+" en el sig byte")
                    aux=letra-byte
                    cant=CANTIDAD_DE_CARACTERES-bits
                    cadena[bytecadena]=cadena[bytecadena]|letra>>cant
                    bits=bits-CANTIDAD_DE_CARACTERES
                else:
                    cadena[bytecadena]=cadena[bytecadena]|letra<<bits-cant
                    i=i+1            
                bits=bits - cant
        #print("byte numero: "+ str(bytecadena)+" byte: "+str(bin(cadena[bytecadena])))
        #print("la cadena " + str(cadena))
        bytecadena=bytecadena+1
    #print("ya termine de codificar")
    #print(cadena)
    return cadena
if __name__ == '__main__' :
    msg="0"
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = HOST
    port = PORT
    sock_addr = (host, int(port))
    client_sock.connect(sock_addr)
    data=""
    while (msg!="salir"):
        msg=input("hola, ingrese un mensaje, si desea finalizar la conexion escriba salir")
        if msg!='salir':
            print(msg[0])
            print(len(msg))
            codigo=codificador(msg)
            print("el mensaje a enviar es: "+str(len(msg)))  
            client_sock.send(bytes(str(len(msg)),'utf-8'))
            print("el mensaje a enviar es: "+str(codigo))  
            client_sock.send(codigo)
        else:
            client_sock.send(bytes(str("fin"),'utf-8'))
            print("conexion finalizada...")
            client_sock.close()
    
    