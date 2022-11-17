from validate_docbr import CPF


class ValidateCPF:
    def __init__(self, document):
        document = str(document)
        if self.is_valid(document):
            self.cpf = document
        else:
            raise ValueError('CPF inválido!')

    def is_valid(self, document):
        validator = CPF()
        if len(document) == 11:
            return validator.validate(document)
        raise ValueError("Quantidade de digitos inválidos!")

    def formated(self):
        validator = CPF()
        return validator.mask(self.cpf)

    def __str__(self):
        return self.formated()
