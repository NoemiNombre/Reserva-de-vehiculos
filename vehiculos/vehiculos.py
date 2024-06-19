#  crear func vehiculo  
"""
contiene las siguientes funciones para almacenar 

"""
def crearVehiculo(matricula, model,price_x_day):
    return{
        "matricula": matricula,
        "modelo": model,
        "precioDia": price_x_day,
        "disponible": True
    }
    
def mostrarVehiculo(vehiculo):
    estado = "disponible" if vehiculo["disponible"] else "no disponible"
    return (f"Vehiculo: {vehiculo["matricula"]}, Modelo: {vehiculo["modelo"]} - {estado}, Precio: ${vehiculo["precioDia"]} por dia")

# marcar vehiculo como "No Dispionible" una vez que sea seleccionado
def alquilarVehiculo(vehiculo):
    vehiculo["disponible"] = False 
   
    
# marcar vehiculo como "Dispionible" una vez que sea seleccionado   
def devolverVehiculo(vehiculo):
    vehiculo["disponible"] = True
    
    
vehiculo1= crearVehiculo("AB123C", "Audi", 500)
print(mostrarVehiculo(vehiculo1))

alquilarVehiculo(vehiculo1)
print(mostrarVehiculo(vehiculo1))