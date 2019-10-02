import socket
import time
from datetime import datetime

HOST = 'headnode'
PORT = 5432
path = 'log/respuestas.txt'
respuestas = open(path,'a+')

time.sleep(2)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

message = 'Un mensajito muy lindo'
byt=message.encode()
print ('El mensaje a enviar es: ',byt.decode())
sock.sendall(byt)

# Esperando la respuesta
#amount_received = 0
#amount_expected = len(message)

data = sock.recv(1024)
decod = data.decode()
#amount_received += len(decod)
print ('La respuesta del Server es: ',decod)
escribir = 'La respuesta del Servidor es: ' + decod + ' \n'
dateTimeObj = datetime.now()
respuestas.write(str(dateTimeObj) + ' : ' + escribir)

print('Cerrando socket')
sock.close()
respuestas.close()