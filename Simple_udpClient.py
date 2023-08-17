from socket import *
from CriptografiaCesar import CriptografiaCesar

serverName = ""
serverPort = 12500
clientSocket = socket(AF_INET, SOCK_DGRAM)

print("UDP Client\n")

while 1:
    criptografia = CriptografiaCesar()

    message = input("Input message: ")
    mensagemCript = criptografia.criptografa(message)

    if message == "exit":
            break
    clientSocket.sendto(bytes(mensagemCript,"utf-8"), (serverName, serverPort))

clientSocket.close()