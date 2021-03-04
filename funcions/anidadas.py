lista = ["track 2","track 3","track 4","track 5"]
def play (lista):
    def cancion():
        nonlocal lista
        lista=[1,2,3]
        for valor in lista:
            print(valor)
    cancion() #llamamos en la funcion madre a la la funcion anidada
    print(lista)

play(lista)