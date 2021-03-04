def tabla_m (nro, maximo=10):
    for posicion in range(1,maximo+1):
        yield nro, posicion, nro * posicion #yield retorna un valor sin terminar la funcion

for num,pos,resultad in tabla_m(9,20):
    print(num," X ", pos , " = ", resultad)