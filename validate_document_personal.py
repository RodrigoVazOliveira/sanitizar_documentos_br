from validate_cnpj import ValidateCNPJ
from validate_cpf import ValidateCPF


class ValidateDocumentPersonal:

    def __init__(self, document, type_document = "cpf"):
        self.__document = document
        self.__type_document = type_document

    def validate(self):
        if self.__type_document.__eq__("cpf"):
            validate_cpf = ValidateCPF(self.__document)
            print(validate_cpf)
        elif self.__type_document.__eq__("cnpj"):
            validate_cnpj = ValidateCNPJ(self.__document)
            print(validate_cnpj)
        else:
            raise ValueError("Tipo de documento inválido!")