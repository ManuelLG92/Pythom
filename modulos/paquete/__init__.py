#para crear paquetes en py es necesatio crear una carpeta y detro un archivo llamada __init__.py
#asi python lo reconoce como un paquete
from .aves import pollo
print("Est es un mensaje del archivo init") #ste archivo de ejecuta cuando sea utilizado el paquete

mipollo = pollo() # tambien pòdemos excportart una