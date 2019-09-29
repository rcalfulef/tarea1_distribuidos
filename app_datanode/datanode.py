import socket

def Main():
    host = "0.0.0.0"  # Ip host
    port =  int(input("ingrese puerto a utilizar: "))
    mySocket = socket.socket()  # Instanciamos un socket
    
    try:
        mySocket.bind((host,port)) # La funcion bind recibe una tupla, que contiene el host y el puerto 
		
    except:
        print("no se ha podido crear el socket")
        exit(1)
        
    mySocket.listen(1)  # solo soportara una conexion
    print("Esperando que se conecte el Headnode\n")
    
    while True:
        conn, addr = mySocket.accept() # tenemos dos variables, una que tiene la conexion y la direccion del cliente
        print ("Headnode conectado en: " + str(addr))
        
        try:
            datanode(conn,addr)
        except:
            print("Datanode con problemas")		        

    
    mySocket.close()

def datanode(conn,addr,max_buffer_size=1024):
    datanode_activo = True
    
    while datanode_activo:
        input_headnode = recibir_input(conn,addr,max_buffer_size)
        
        if "--salir--" in input_headnode:
            print("se solicita apagar datanode")
            conn.close()
            print("Conexion "+ str(addr) + " cerrada")
            datanode_activo = False
        if "--estado--" in input_headnode:
            print("datanode corriendo")
            conn.send("--vivo--".encode())
        else:
            print("mensaje desde el headnode recibido")
            guardar_en_data(input_headnode,addr)
            conn.send("Guardado correctamente en data".encode())



    
def recibir_input(conn,addr,max_buffer_size):
    input_cliente = conn.recv(max_buffer_size)
    decoded_input = input_cliente.decode()
    resultado_guardar = guardar_en_log(decoded_input,addr)
    if resultado_guardar == True:
        return decoded_input
    
def guardar_en_log(input_str,addr):
    file  = open("log.txt","a")
    file.write(input_str + " " +str(addr) + "\n")
    file.close()
    return True

def guardar_en_data(input_str,addr):
    file  = open("data.txt","a")
    file.write("MENSAJE:\n    "+input_str + "\nDE CLIENTE" +str(addr) + "\n\n")
    file.close()
    return True


if __name__ == '__main__':
    Main()