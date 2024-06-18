# continee la clase cliente que almecena la info de los clienes 

def crearCliente(name,lastname,licence):
    return{
        "Name": name, 
        "Lastname": lastname,
        "Licence": licence
    }
    
def mostrar_cliente(cliente):
    return (f"{cliente["Name"]} {cliente["Lastname"]}, {cliente["Licence"]}")



    
        