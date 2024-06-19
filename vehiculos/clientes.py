# continee la clase cliente que almecena la info de los clienes 

def crearCliente(name,lastname,licence):
    return{
        "nombre": name, 
        "apellido": lastname,
        "licencia": licence
    }
    
def mostrar_cliente(cliente):
    return (f"{cliente["nombre"]} {cliente["apellido"]}, {cliente["licencia"]}")



    
        