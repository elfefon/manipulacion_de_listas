
def append_manual(lista, elemento):
    """
    Agrega un elemento a la lista y la retorna
    """
    return lista + [elemento]

def insertar(lista, elemento, indice):
    """
    Inserta un elemento en el índice dado. Si el índice es mayor al largo, lo agrega al final.
    Devuelve la lista modificada.
    """
    lista_nueva = []
    insertado = False
    for i in range(len(lista) + 1):
        if i == indice:
            lista_nueva += [elemento]
            insertado = True
        if i < len(lista):
            lista_nueva += [lista[i]]
    if not insertado:
        lista_nueva += [elemento]
    return lista_nueva

def obtener_indice(lista, elemento):
    """
    Devuelve el indice de la primera ocurrencia del elemento.
    Si no existe, devuelve -1.
    """
    for i in range(len(lista)):
        if lista[i] == elemento: 
            return i
    return -1

def eliminar(lista):
    """
    Elimina el ultimo elemento de la lista y lo retorna.
    Si la lista esta vacia, retorna None.
    """
    if len(lista) == 0:
        return None
    ultimo = lista[len(lista) - 1]
    lista[:] = lista[:len(lista) - 1]
    return ultimo

def eliminar_primer_instancia(lista, elemento):
    """
    Elimina la primera instancia del elemento y lo retorna.
    Si no existe, devuelve None.
    """
    nueva_lista = []
    encontrado = False
    for i in range(len(lista)):
        if not encontrado and lista[i] == elemento:
            encontrado = True
            continue
        nueva_lista += [lista[i]]
    if encontrado:
        lista[:] = nueva_lista
        return elemento
    return None

def eliminar_todos(lista, elemento):
    """
    Elimina todas las apariciones del elemento y devuelve la lista modificada.
    """
    nueva_lista = []
    for i in range(len(lista)):
        if lista[i] != elemento:
            nueva_lista += [lista[i]]
    return nueva_lista

def vaciar_lista(lista):
    """
    Devuelve una lista vacía.
    """
    lista_vacia = lista
    lista_vacia = []
    return lista_vacia