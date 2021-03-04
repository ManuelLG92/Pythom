class Animal:
    def comer (self):
        print("Comiendo")
    def dormir (self):
        print("Durmiendo")

class Perro(Animal): #herncia Perro(Animal). Clase perro hereda de l clase Animal

    def __init__ (self,nombre):
        self.nombre = nombre

    def ladrar(self):
        print("Ladrando")
    
mosha = Perro("Mosha")
mosha.dormir()
mosha.ladrar()
mosha.comer()

#Herencia Multiple class Perro(Animal, mamifero, mascota). las clases de las que hereda en los ()

print(mosha.__dict__) #metodo de la clase object para ver los atributos d eun instancia como un dccionario
    
