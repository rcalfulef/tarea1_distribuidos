import socket
from datetime import datetime

HOST = 'headnode'
PORT = 5432
path = 'log/log.txt'
log = open(path,'a+')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))

print('Esperando cliente')
sock.listen(1)
conn, client_address = sock.accept()
ip_cliente, puerto_cliente = client_address

print('Cliente: ',client_address, ' se conecto')
data = conn.recv(1024)
decod = data.decode()
print('El mensaje del cliente fue: ',decod)

escribir = 'El cliente con ip: ' + str(ip_cliente) + ' envio el mensaje: ' + decod + ' \n'
dateTimeObj = datetime.now()
log.write(str(dateTimeObj) + ' : ' + escribir)


message = 'Hola, su mensaje fue recibido'
byt=message.encode()
conn.sendall(byt)
print('Cerrando Conexion')
conn.close()
print('Cerrando socket')
sock.close()
log.close()