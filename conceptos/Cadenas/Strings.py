curso = "Curso de Python"
print(len(curso)) #nro de caracteres
print(curso[0])
subString = curso[1:16:2]
print(subString)

lenguajes = "Python; java; ruby; php; swift; JS; c#; c; c++"
separador = "; "
rs = lenguajes.split(separador) #split genera una lista con un stringh mediante separadores)
print(rs)

nString = "; ".join(rs) #.join crea una string apartir de una lista
print(nString)
texto = """
texto
con
saltos
de
linea
"""
r2 = texto.splitlines() #convierte un string a lista cuando hayan saltos de lineas
print(r2)

txt = "esto es una cadena"
r3 = txt.capitalize() #pone en mayuscula la primera letra
print(r3)
txt = "ESTO es una cadena"
r3 = txt.swapcase() #cambia mayusculas por minusculas y vice versa
print(r3)
txt = "ESTO es una cadena"
r3 = txt.upper() #todas las letras a mayusculas 
print(r3)
txt = "ESTO ESTO ESTO es una cadena"
r3 = txt.lower() #todas las letras a minusculas 
print(r3)
print(r3.islower()) #saber si esta en minusculas
print(r3.isupper())#saber si esta en mayusculas
r3 = txt.title() #Formato de titulo 
print(r3)
r3 = txt.replace("ESTO","this", 1) #Remplazar una plabra por otro, indicando las veces o todas
print(r3)
txt = "            esto es una cadena         "
r3 = txt.strip() #remove espacios en blanco al ppio o final
print(r3)

