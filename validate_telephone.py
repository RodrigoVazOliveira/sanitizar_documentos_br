import re


class ValidateTelephone:

    def __init__(self, telephone):
        if not self.is_valid(telephone):
            raise ValueError("Número incorreto!")
        self.number_telephone = telephone

    def is_valid(self, telephone):
        pattern = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        response = re.findall(pattern, telephone)
        if response:
            return True
        return False

    def formated(self):
        pattern = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        response = re.search(pattern, self.number_telephone)
        number_telephone_formated = "+{} ({}) {}-{}".format(
            response.group(1),
            response.group(2),
            response.group(3),
            response.group(4)
        )
        return number_telephone_formated

    def __str__(self):
        return self.formated()