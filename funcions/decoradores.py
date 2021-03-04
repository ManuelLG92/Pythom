# minimo 3 funcions. ejem: a,b,c. a(b)->c

def decorador(funcion): #la Funcion a recib cmo parametro la funcion b, y genera la funcion C
    
     def nueva_f(*args,**kwargs): """funcion c"""
      print("Mnsaje antes de la funcion")
      rsult = funcion(*args,**kwargs)
      print("Mnsaje despues de la funcion")
      return rsult
    return nueva_f

@decorador
def funcion_a_decorar (): #Funcion a decorar. funcion b
    print("Esta es la funcion B")

funcion_a_decorar()

@decorador
def suma (a,b):
    return a+b

rees = suma(10,20)
print(rees)
