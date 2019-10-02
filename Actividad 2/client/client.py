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
    #print(data)
    
    #message = input("Ingrese un mensaje: ")
    
    if data == "--conexion--":
        print("conexion exitosa!")
        print("Ingrese 'salir' para cerrar programa:")
        
        mensajes = ['hola uWu','soy el cliente','y esta es una prueba','abandonare el servidor','salir']
        for message in mensajes:
            print("cliente envia: " + message+ "\n")
            if message != 'salir':
                mySocket.send(message.encode())
                data = recibir_input(mySocket,1024)
                print ('Respuesta headnode: \n' + data)
                    #message = input("Ingrese un mensaje: ")
                    #break
            if message == 'salir':
                mySocket.send("--quit--".encode())
                print("Desconectandose")
        print("El cliente ha enviado todos sus mensajes")

def recibir_input(mySocket,max_buffer_size):
    input_servidor = mySocket.recv(max_buffer_size)
    decoded_input = input_servidor.decode()
    resultado_guardar = guardar_en_archivo(decoded_input)
    if resultado_guardar == True:
        return decoded_input
 
def guardar_en_archivo(input_str):
    file = open("archivos/respuestas.txt","a")
    file.write(input_str + "\n")
    file.close()
    
    return True
 
if __name__ == '__main__':
    Main()
