from socket import *
from CriptografiaCesar import CriptografiaCesar

serverName = ""
serverPort = 8888
clientSocket = socket(AF_INET, SOCK_DGRAM)

print("UDP Client\n")

while 1:
    criptografia = CriptografiaCesar()

    message = input("Input message: ")
    mensagemCript = criptografia.criptografa(message)

    if message == "exit":
            print(type(mensagemCript))
            break
    clientSocket.sendto(bytes(mensagemCript,"utf-8"), (serverName, serverPort))

clientSocket.close()
