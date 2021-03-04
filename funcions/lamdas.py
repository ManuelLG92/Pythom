#lambas = funciones anonimas
def centigrados (grados): #funcion normal
    return grados*1.8+32
func_variable = centigrados
print(func_variable(20))

mi_func = lambda grados=0: grados*1.8+32 # funcion lambda. grados=0. valor pro default, 
print(mi_func(32))                       #simpr devuelve un valor sin necesidad dl return

""""
sin_parametros = lambda : True

con_valores = lambda val, val1=10, val2=10 : val + val1 + val2

con_asterisco = lambda *args : args[0]

con_doble_asterisco = lambda **kwargs : args[0]

con_asteriscos = lambda *args , **kwargs : kwargs.get('key', False)
"""
