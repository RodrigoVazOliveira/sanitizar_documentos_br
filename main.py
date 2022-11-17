from validate_cpf import ValidateCPF

cpf = "01234567890"
cpf_validate = ValidateCPF(cpf)
print(cpf_validate)

#print(cpf_validate.validate("012.345.678-90")) # True
#print(cpf_validate.validate("012.345.678-91"))  # False