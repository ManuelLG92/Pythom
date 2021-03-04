def crear (nombre="", apellido="", edad=18): #Valor pro default a paramtros
    return {
        'nombre' : nombre,
        'apellido' : apellido,
        'nombre_comp' : "{} {}".format(nombre,apellido),
        'edad' : edad
    }
codi= crear("Manuel","Leon")
print(codi["nombre"])
print(codi["apellido"])
print(codi["edad"])


def suma (*args): # se usa el * cuando no sabemos el numero de parametros, y lo convierte en una tupla
    total=0
    print(args)
    for numero in args:
        total+=numero
    return total
r = suma(2,5,10,50,60,18)
print(r)

def usuarios (**kwargs): #agrupa los param n un diccionarios
    print(kwargs)
usuarios(curso=True, python=False)

def combinacion (requerido, *args, **kwargs):
    print(requerido)
    print(args)
    print(kwargs)

combinacion("Valor Requrido",10,20,valor1=True, valor2=False)

def endfunction ():
    print("Aqui aprndemos a trminar una funcion")
    print("Una funcion terminara cuando se ejecute la ultima linea de la misma o en el return")
endfunction()


