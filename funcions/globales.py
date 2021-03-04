animal = "Leon" #globales, fuera de las funciones

def m_animal():
    #animal = "Cat" en py dentro de una funcion si se declara una variable local sera diferente a la hlobal asi sean iguales 
    global animal #asi podremos modificar la variable global
    animal='Cat' # y aqui asignamos su valor
    print(animal)

m_animal()