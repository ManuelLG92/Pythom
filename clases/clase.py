class Usuario:
    def __init__(self, nombre="", apel="",nick=""): #aqui crearemos todos los atributos
        self.nombre=nombre
        self.apel = apel
        self.nick = nick

    def saluda(self): #asis e crea un metodo, pr convencion se usa como atributo self
        print("Hola, soy un usuario "+self.nombre)
    def mostrar_datos (self):
        print(self.nick)
    def crear_nombre (self, nombre):
        self.nombre = nombre
    def mostrar_Nnombre (self):
        print(self.nombre)

manuel = Usuario("Manuel","Leon","Coco") #crear una instancia de una clase
manuel.saluda()
print(type(manuel)) #saber de qu clas es una instancia

class Circulo:
    pi = 3.14

    def __init__ (self, radio):
        self.radio = radio #Variables de instancia *1

c1 = Circulo(10)
c2= Circulo(20)
print(c1.radio)
print(c2.radio)
c1.radio = 100 # *1
print("\n")
print(c1.radio)
print(c2.radio)

#metodos staticos
class triangulo:
    @staticmethod
    def area(base,altura):
     return (base*altura)/2

print(triangulo.area(10,20) )

#metodos de clase
class cuadrado:
    pi=3.14

    @classmethod
    def areac(cls,radio): #por convncion se usa cls
     return cls.pi*radio**2
print(cuadrado.areac(10))