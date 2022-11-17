class SearchAddressBrazil:

    def __init__(self, cep):
        cep = str(cep)
        self.is_valid(cep)
        self.__cep = cep

    def is_valid(self, cep):
        if len(cep) != 8:
            raise ValueError("O CEP Informado é inválido")



