import requests


class SearchAddressBrazil:

    def __init__(self, cep):
        cep = str(cep)
        self.is_valid(cep)
        self.__cep = cep

    def is_valid(self, cep):
        if len(cep) != 8:
            raise ValueError("O CEP Informado é inválido")

    def formated(self):
        return "{}-{}".format(self.__cep[:5], self.__cep[5:])

    def get_address_by_via_cep(self):
        url_request = "https://viacep.com.br/ws/{}/json/".format(self.__cep)
        request_get = requests.get(url_request)
        address = request_get.json()

        return [
            address["bairro"],
            address["localidade"],
            address["uf"]
        ]

    def __str__(self):
        return self.formated()



