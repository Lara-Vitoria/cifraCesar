from socket import *

serverPort = 12500
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("",serverPort))

print ("UDP server\n")

while 1:
    descriptografa = CriptografiaCesar()

    message, clientAddress = serverSocket.recvfrom(2048)

    mensagemCript = descriptografa.descriptografa(message)

    text = str(mensagemCript,"utf-8")
    print ("Received from Client: ", text)
