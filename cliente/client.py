import socket
 
def Main():
    host = 'headnode'
    port = 5000
    
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        mySocket.connect((host,port))
    except:
        print("no se ha podido realizar la conexion")
        exit(1)
    mySocket.send("--conexion--".encode())
    data = recibir_input(mySocket,1024)
    print(data)
    print("Ingrese 'salir' para cerrar programa:")
    #message = input("Ingrese un mensaje: ")
    

    mensajes = ['hola','esto es una prueba','salir']
    for message in mensajes:

        while message != 'salir':
            mySocket.send(message.encode())
            data = recibir_input(mySocket,1024)
            if "--conexion--" in data:
                print("conexion exitosa!")
                message = input("Ingrese un mensaje: ")
            else:
                print ('Recibido desde el servidor: ' + data)
                message = input("Ingrese un mensaje: ")
    
    mySocket.send(b"--quit--")

def recibir_input(mySocket,max_buffer_size):
    input_servidor = mySocket.recv(max_buffer_size)
    decoded_input = input_servidor.decode()
    resultado_guardar = guardar_en_archivo(decoded_input)
    if resultado_guardar == True:
        return decoded_input
 
def guardar_en_archivo(input_str):
    file = open("respuestas.txt","a")
    file.write(input_str + "\n")
    file.close()
    
    return True
 
if __name__ == '__main__':
    Main()