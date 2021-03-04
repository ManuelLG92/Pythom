lista = [1,34,25.6,99,2,54,0,2,2,3]
lista.sort() #ordena la lista con el metodo sort de mayor a menor. ascendente
print(lista)
lista.sort(reverse=True) #ordena la lista alreves, mayor a menor. descendente
print(lista)
mayor = lista[0] #el valor mayor de una lista descendente
print(mayor)
lista.sort() 
mayor = lista[0] #el valor menor de una lista, ordeno ascendente y se busca el valor de p[0] 
print(mayor)

menor = min(lista) #obtener el valor menor de una lista
print(menor)
mayor = max(lista)#obtener el valor mayor de una lista
print(mayor)
longitud = len(lista)
print(longitud)

resultado= 2 in lista #saber si el valor esta en la lista
print(resultado)

indice = lista.index(2) #otener la posicion de un valor
print(indice)

repetido = lista.count(2) #contar cuantas veces esta repetido un valor en la lista
print(repetido)

