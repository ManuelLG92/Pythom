def nombr (nombr : str) -> None: # (nombr : str) specifica l tipo de dato esperado pro puede ser 
    print("Manuel")    #otro  valor es solo para guiarnos,           
                        # (x : str/int/bool/flot) -> None/str/int/bool/flot. espcificamos el valor 
                        #esperado que devbuelva con el return, sino tenemos return es None


#comprenhension
lista = []
for num in range(0,101):
    lista.append(num)

 #esta linea de abajo hace el mismo trabnajo que las linas anteriores   
estructura = [x for x in range(0,101)]