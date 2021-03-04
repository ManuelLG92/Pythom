cursos = ["py","c","java","php"]
#Podemos recorrer la lista hacia adelante: cursos[2]. y hacia atras: cursos[-2]
curso = cursos[2]
#Creamos sublistas indicando la psicion de inicio o final de la lista madre
sub = cursos[2:4]
#hasta
sub = cursos[:4]
#desde
sub = cursos[:4]
#obtnr la lista actual
sub = cursos[:]
#lista con saltos[0(desde):4(hasta):2(saltos)]
sub = cursos[0:4:2]
#Asi visualizamos nuestra lista al inverso, de atras hcia adelante
sub = cursos[::-1]
print(sub)
"""
Estas son las formas en las cuales podemos crear una nueva lista (sublistas) a partir de otra.

[:] Todos los elementos.
[start:] Todos los elementos desde el índice establecido(start).
[:end] Todos los elementos desde el índice cero hasta el índice establecido(end).
[start:end] Todos los elementos de un rango de índices.
[start:end:step] Todos los elementos de un rango de índices con saltos.
De igual forma, este listado es aplicable a las tuplas y los strings.
"""