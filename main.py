from search_address_brazil import SearchAddressBrazil

cep = 65057869
search_address_brazil = SearchAddressBrazil(cep)
print(search_address_brazil)
response = search_address_brazil.get_address_by_via_cep()
print(response)
