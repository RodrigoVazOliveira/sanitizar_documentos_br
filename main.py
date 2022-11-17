from validate_document_personal import ValidateDocumentPersonal

cpf = "12354367996"
cnpj = "68130144000104"
validate_document_personal_cpf = ValidateDocumentPersonal(cpf)
validate_document_personal_cpf.validate()

validate_document_personal_cnpj = ValidateDocumentPersonal(cnpj, "cnpj")
validate_document_personal_cnpj.validate()