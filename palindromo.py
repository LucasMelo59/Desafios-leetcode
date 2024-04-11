inteiro = -121

numero_string = str(inteiro)
array_de_caracteres = list(numero_string)
quantidade_caracteres = len(array_de_caracteres) - 1
array_invertido = ""
for items in enumerate(array_de_caracteres):
    array_invertido += array_de_caracteres[(quantidade_caracteres)]
    quantidade_caracteres -= 1
if(numero_string == array_invertido):
    print(True)