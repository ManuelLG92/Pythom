#condicionales
color = "yellow"
if color=="verde":
    print("Go ahead")
elif color=="yellow":
    print("take care")
else: 
    print("Alto")

v = True
if v:
    print("verdadrs")
else:
    print("False")
#condicionales

#Ciclo while
numero = 54123452
contador=0
while numero>=1:
    contador+=1
    numero/=10
else:
    print("Cantidad de digitos es", contador)
#Ciclo while

#for
num = [1,2,3,4,5,6,7,8,9,10]
for numero in num:
    print(numero) 

valores = ((10,20),["Strings","String"], (True,False))
for valor, valor2 in valores:
    print(valor, valor2)

    #funcion range
for val in range(1,10):
    print(val+1)

for val2 in range(-10,11):
    print(val2)

for impar in range(1,101,3):
    print(impar)

lista = [1,2,3,4,5,6,7]
for vlista in range(len(lista)):
    print("Indice : ",vlista, ". Valor ",lista[vlista])
    #funcion range

    #funcion Enumerate
for indice, valor in enumerate(lista):
    print("Indice: ", indice, ". Valor: ", lista[indice])
    #funcion Enumerate
#for