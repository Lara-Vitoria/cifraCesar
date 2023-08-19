from socket import *
from CriptografiaCesar import CriptografiaCesar

serverPort = 8888
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))

print ("UDP server\n")

while 1:
    descriptografa = CriptografiaCesar()

    message, clientAddress = serverSocket.recvfrom(2048)

    mensagemCript = descriptografa.descriptografa(message)

    print ("Received from Client: ", mensagemCript)

