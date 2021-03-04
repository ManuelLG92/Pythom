diccionario = {}
diccionario["Nombre"]="Codi" #Agregar una llave con su valr

print(diccionario)
diccionario["Nombre"]=90
print(diccionario["Nombre"])

dicc2 = {'a':1, 'b':2, 'c':3}
print(dicc2)
r= "z" in dicc2
print(r)
r=dicc2.get("j")
print(r)
r=dicc2.setdefault("j", "6")
print(r)
print(dicc2)

#res = dicc2.keys()
#tupla = tuple(dicc2)
#lista = list(dicc2)
print( dicc2.keys()) #obtine las llaves del diccionario
print( dicc2.values())#obtine el valor de las llaves del diccionario

print( dicc2.items()) #Muestra cada key con su valor

print(len(dicc2)) #imprime el numero de items del diccionario

del dicc2['a'] #del para eliminar una clave y su valor
print( dicc2.items()) #Muestra cada key con su valor
print(len(dicc2)) #imprime el numero de items del diccionario

#del para eliminar una clave y su valor
print(dicc2.pop('b'))
print( dicc2.items()) #Muestra cada key con su valor
print(len(dicc2)) #imprime el numero de items del diccionario
#dicc2 = {} asi dejamos vacio el diccionario
#dicc2.clear  asi dejamos vacio el diccionario