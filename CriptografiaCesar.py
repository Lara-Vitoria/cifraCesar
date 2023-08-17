class CriptografiaCesar:
    def __init__(self):
        self.__alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
 
    def criptografa(self, mensagem, chave = 3):
        mensagemCriptografada = ''
        mensagem = mensagem.upper()

        for letra in mensagem:
            if letra in self.__alfabeto:
                index = (self.__alfabeto.find(letra) + chave) % 26 
                mensagemCriptografada += self.__alfabeto[index]
            else:
                mensagemCriptografada += letra

        return mensagemCriptografada