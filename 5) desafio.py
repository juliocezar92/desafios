string = "Exemplo"

# Converte a string para uma lista de caracteres
lista_caracteres = list(string)

# Obtém o tamanho da lista
tamanho_lista = len(lista_caracteres)

# Inverte os caracteres da lista
for i in range(tamanho_lista // 2):
    lista_caracteres[i], lista_caracteres[tamanho_lista - i - 1] = lista_caracteres[tamanho_lista - i - 1], lista_caracteres[i]

# Converte a lista de caracteres de volta para uma string
string_invertida = "".join(lista_caracteres)

# Imprime a string invertida
print(string_invertida)