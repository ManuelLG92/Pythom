def m_msg (mensaje):
    mensaje = mensaje.title()

    def show ():    
        print(mensaje)

    return show

nw_func = m_msg("Hola manuel")
nw_func()

