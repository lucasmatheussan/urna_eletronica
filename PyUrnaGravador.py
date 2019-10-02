def gravaEleitores(listaEleitores):
    gravar = open("eleitores.txt", "a+")
    gravar.write("\n"+listaEleitores)
    gravar.close()

def recuperaEleitores():
    gravar = open("eleitores.txt", "r+")
    lista = ""
    for k in gravar.readlines():
        lista = lista + k + '\n'
    gravar.close()
    return lista