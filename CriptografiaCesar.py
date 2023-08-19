class CriptografiaCesar:
    def __init__(self):
        self.__alfabeto = ''
 
    def criptografa(self, mensagem, chave = 3):
        mensagemCriptografada = ''
        mensagem = mensagem.upper()

        for i in range(128):
            self.__alfabeto += chr(i)

        for letra in mensagem:
            if letra in self.__alfabeto:
                index = (self.__alfabeto.find(letra) + chave) % 128 
                mensagemCriptografada += self.__alfabeto[index]
            else:
                mensagemCriptografada += letra

        return mensagemCriptografada
    
    def descriptografa(self, mensagem,  chave = 3):
        mensagemDescriptografada = ''
        mensagem = mensagem.upper().decode('utf-8')

        for i in range(128):
            self.__alfabeto += chr(i)

        for letra in mensagem:
            if letra in self.__alfabeto:
                index = (self.__alfabeto.find(letra) - chave) % 128 
                mensagemDescriptografada += self.__alfabeto[index]
            else:
                mensagemDescriptografada += letra

        return mensagemDescriptografada.lower()
