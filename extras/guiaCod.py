"""
Es de suma importancia que nosotros tengamos una forma estandarizada de codificación y siempre 
nos concentremos en codificar de la misma manera, recordemos que muy probablemente a nuestros 
proyectos les tengamos que dar mantenimiento o tengamos que incorporar más desarrolladores al 
mismo, en cualquier caso, codificar bajo un estándar nos permitirá crear proyectos de más alta 
calidad.

En Python existe los PEP's, Mejoras de propuestas de Python, de los cuales al momento de codificar
 nos interesa PEP8.

PEP8 Es una guía de codificación, la cual nos permite escribir código Python de una manera,
 mucho más legible y de forma consistente, a través de ciertas "reglas" y recomendaciones. 
 Por ejemplo, en la guía podemos encontrar:

utilizar espacios sobre tabs.
utilizar la nomenclatura de snake case para nombrar variables.
utilizar palabras en mayúsculas para las constantes.
Colocó "reglas" entre comillas ya que nosotros podemos crear un programa cien por 
ciento funcional sin habernos guiado de PEP8, simplemente siendo constantes al momento de codificar.

Si por algún motivo creemos que nuestra forma de codificar Python es errónea o queremos 
implementar al pie de la letra la guía, podemos validar nuestro código en la siguiente
página web: http://pep8online.com/, basta con copiar el código del cual tenemos duda y validar.
Si quieres crear una librería, te recomiendo validar todo tu código.
"""

"""
== O IS
En el vídeo de Operadores relacionales y lógicos mencianamos que es posible conocer si dos 
valores enteros son iguales mediante el uso de == y la palabra reservada is; Sin embargo, 
ahora que ya contamos con más conocimiento del que teníamos en ese vídeo es importante conocer
 cuando usaremos == y cuando usaremos is. Veamos.

Si ejecutamos la siguiente línea de código obtendremos como resultado True.

[1,2,3] == [1,2,3]
Eso de deben a que ambas listas son iguales. Ahora, ¿Qué pasa si reemplazamos == por is?

[1,2,3] is [1,2,3]
En este casa obtenemos False; Esto se debe a que con == compararemos que dos valores sean 
iguales y con is compareremos que dos objetos sean iguales, cosas completamente diferentes.

Veamos un par de ejemplos para que nos quede más en claro.

a = [1,2,3]
b = [1,2,3]
A la primera lista la llamaremos a y a la segunda b.

Si imprimimos el id de cada objeto, observaremos que son valores completamente diferentes, 
con lo cual concluimos que son dos objetos diferentes.

print(id(a))
print(id(b))
Si ejecutamos.

a = [1, 2, 3]
b = a

a is b 
Obtendremos cómo resultado True, debido a que a y b son el mismo objeto.

En conclusión == nos permite saber si dos objetos son iguales, mientras que is nos
 permite conocer si cuando los objetos son los mismos.
"""