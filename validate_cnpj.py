from validate_docbr import CNPJ


class ValidateCNPJ:

    def __init__(self, document):
        document = str(document)
        if self.is_valid(document):
            self.cnpj = document

    def is_valid(self, document):
        cnpj = CNPJ()
        if cnpj.validate(document):
            return True
        raise ValueError("CNPJ com quantidade digitos incorreto ou inválido!")

    def format(self):
        cnpj = CNPJ()
        return cnpj.mask(self.cnpj)

    def __str__(self):
        return self.format()