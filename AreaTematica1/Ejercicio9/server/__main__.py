import socket
BITSENBYTE=8
CANT_BIT_P_CARACTER=3
HOST = "192.168.1.55"
PORT = 5555
BUFSIZ = 1024
def decod(msg):
    if msg==int('000',2):
        letra="A"
    elif msg==int("001",2):
        letra="B"
    elif msg==int("010",2):
        letra="C"
    elif msg==int("011",2):
        letra="D"
    elif msg==int("100",2):
        letra="E"
    elif msg==int("101",2):
        letra="F"
    elif msg==int("110",2):
        letra="G"
    elif msg==int("111",2):
        letra="H"
    else:
        letra=""
    return letra
def decodificar(t,msg):
    #print(t)
    #print(type(msg))
    #print(msg[0])
    #print(msg[1])
    mensaje=""
    i=0
    cant=CANT_BIT_P_CARACTER
    byte=0
    while i<t:
        #print("i: "+str(i)+" t: "+str(t))
        bits=BITSENBYTE
        while bits>0 and i<t:
            byteaux=msg[byte]
            #print(byteaux)
            if bits<CANT_BIT_P_CARACTER: #cuando no tengo suficientes bits para representar la letra en el byte actual
                #print("bits menores a cant: "+str(bits))
                desplazamiento=bits
                #print("letra: "+str(byteaux)+" "+str(desplazamiento))
                letra=byteaux>>desplazamiento
                #print("letra: "+str(letra)+" "+str(desplazamiento))
                letra=letra<<desplazamiento
                #print("letra: "+str(letra)+" "+str(desplazamiento))
                letra2=byteaux-letra
                print("letra: "+str(letra2)+" "+str(desplazamiento)) #letra2 es la parte que guardo de la letra
                cant=CANT_BIT_P_CARACTER-desplazamiento
                aux=letra2
                #print("auxiliar: "+str(aux))
                bits=0
            else:
                if cant!=CANT_BIT_P_CARACTER:
                    desplazamiento=bits-cant
                    letra=byteaux>>desplazamiento                    
                    auxL=(aux<<cant)|letra  
                    print("letra aux: "+str(letra)+" "+str(desplazamiento)) 
                    l=decod(auxL)
                    bits=bits-cant
                    cant=CANT_BIT_P_CARACTER
                else:    
                    if bits==BITSENBYTE:
                        desplazamiento=bits-CANT_BIT_P_CARACTER
                        letra=byteaux>>desplazamiento
                        print("letra: "+str(letra))
                        l=decod(letra)
                        bits=bits-CANT_BIT_P_CARACTER
                    else:
                        desplazamiento=bits
                        #print("letra: "+str(byteaux)+" "+str(desplazamiento))
                        letra=byteaux>>desplazamiento
                        #print("letra: "+str(letra)+" "+str(desplazamiento))
                        letra=letra<<desplazamiento
                        print("letra: "+str(letra)+" "+str(desplazamiento))
                        letra2=byteaux-letra
                        bits=bits-CANT_BIT_P_CARACTER
                        letra2=letra2>>bits
                        print("letra: "+str(letra2))
                        l=decod(letra2)
                        
                print("la letra es "+l)



                mensaje=mensaje+l               
                i=i+1                
                letra<<desplazamiento
                byteaux=byteaux-letra
                
        byte=byte+1
    return mensaje
if __name__ == '__main__' :
    
    #implementar encendido del servidor y espera
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST,int(PORT)))
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    server_socket.listen(0)
    print("Servidor esperando por nuevas conexiones...")
    conn, addr = server_socket.accept()
    
    print("Cliente conectado desde: ", addr)
    data=""
    while True:
        data=conn.recv(BUFSIZ)
        tamaño=int(data)
        data=conn.recv(BUFSIZ)
        m=str(data)
        print("mensaje recibido: "+ m)
        mensaje=bytearray(data)
        m=decodificar(tamaño,mensaje)
        print("mensaje decodificado: "+ m)