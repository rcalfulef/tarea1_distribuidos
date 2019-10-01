import socket
import time
from threading import Thread, Timer
from random import choice
cant_datanodes = 3

def Main():
    host = "headnode"  # Ip host
    port = 5000
    mySocket = socket.socket()  # Instanciamos un socket
    
    sockets = sockets_datanodes(cant_datanodes) # Sockets para conectarse a los datanodes
    multicast(sockets) # se encarga de realizar multicast crear un archivo
    
    try:
        mySocket.bind((host,port)) # La funcion bind recibe una tupla, que contiene el host y el puerto 	
    except:
        print("no se ha podido crear el socket del servidor")
        exit(1)
	
    mySocket.listen(3)  # le pasamos 1 para que escuche hasta que se cierre la conexion
    print("servidor escuchando a clientes")
    
    while True:
        conn, addr = mySocket.accept() # tenemos dos variables, una que tiene la conexion y la direccion del cliente
        #print ("Conectado a : " + str(addr))		
        
        try:
            Thread(target= cliente_thread, args=(conn,addr,sockets)).start() # le asignamos un hilo a un cliente
        except:
            print("El thread no pudo iniciar")
    
    mySocket.close()

def cliente_thread(conn,addr,sockets,max_buffer_size=1024):
    cliente_activo = True
    
    while cliente_activo:
        input_cliente = recibir_input(conn,addr,max_buffer_size)
        
        if "--quit--" in input_cliente: # si el cliente envia salir
            print("Un cliente solicita salir")
            conn.close()
            print("Conexion "+ str(addr) + " cerrada")
            cliente_activo = False
        if "--conexion--" in input_cliente:
            print("nuevo cliente conectado: "+ str(addr))
            conn.send("--conexion--".encode())
        else: # si envia un mensaje
            print("mensaje del cliente "+ str(addr))
            aleatorio = choice(sockets)
            output_datanode = input_cliente + "--%--" + str(addr)  ## se le agrega la ip y puerto del cliente, para que el datanode sepa a que cliente pertenece el mensaje. 
            aleatorio.send(output_datanode.encode())
            respuesta = recibir_input_socket(aleatorio)
            mensaje_a_cliente = "MENSAJE:\n    "+input_cliente+"\nALMACENADO EN "+str(aleatorio.getpeername())+'\n'
            conn.send(mensaje_a_cliente.encode())
        
        
def recibir_input(conn,addr,max_buffer_size=1024):
    input_cliente = conn.recv(max_buffer_size)
    decoded_input = input_cliente.decode()
    resultado_guardar = guardar_en_archivo(decoded_input,addr)
    if resultado_guardar == True:
        return decoded_input

def recibir_input_socket(mySocket,max_buffer_size=1024):
    input_servidor = mySocket.recv(max_buffer_size)
    decoded_input = input_servidor.decode()
    #resultado_guardar = guardar_en_archivo(decoded_input)
    #if resultado_guardar == True:
    return decoded_input    

def guardar_en_archivo(input_str,addr):
    file  = open("log.txt","a")
    file.write(input_str + " " +str(addr) + "\n")
    file.close()
    
    return True

def escribir(nombreArchivo,aEscribir):
    var = open(nombreArchivo,"a")
    var.write(aEscribir)
    var.close()

def sockets_datanodes(cant_datanodes):
    """lista = []
    for i in range(cant_datanodes): # creamos los sockets para cada uno de los datanodes
        sock = socket.socket()
        dhost = str(input("ingrese ip del datanode "+ str(i) +" : "))
        dport = int(input("ingrese puerto del datanode "+ str(i) +" : "))
        sock.connect((dhost,dport))
        lista.append(sock)"""

    sock1 = socket.socket()
    sock1.connect(("datanode1",5001))
    sock2 = socket.socket()
    sock2.connect(("datanode2",5002))
    sock3 = socket.socket()
    sock3.connect(("datanode3",5003))
    
    lista = [sock1,sock2,sock3]


    return lista
	
def multicast(sockets):
    Timer(5.0,multicast,[sockets]).start()
    for socket in sockets:
        socket.send("--estado--".encode())
        respuesta = recibir_input_socket(socket)
        if "--vivo--" in respuesta:
            escribir("hearbeat_server.txt",time.ctime(time.time()) + " " + str(socket.getpeername())+"\n")
                     
if __name__ == '__main__':
    Main()
