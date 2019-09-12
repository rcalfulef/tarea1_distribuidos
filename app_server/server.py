import socket
 
def Main():
    host = "0.0.0.0"  # Ip host
    port = 5000         # Puerto host
     
    mySocket = socket.socket()  # Instanciamos un socket
    mySocket.bind((host,port)) # La funcion bind recibe una tupla, que contiene el host y el puerto
     
    mySocket.listen(1)  # le pasamos 1 para que escuche hasta que se cierre la conexion
    conn, addr = mySocket.accept() # tenemos dos variables, una que tiene la conexion y la direccion del cliente
    print ("Connection from: " + str(addr))
    while True:
            data = conn.recv(1024).decode()
            if not data:
                    break
            print ("from connected  user: " + str(data))
             
            data = str(data).upper()
            print ("sending: " + str(data))
            conn.send(data.encode())
             
    conn.close()
     
if __name__ == '__main__':
    Main()