import pandas as pd 

#fun para crear la resrva
def crearReserva(cliente, vehiculo, fechaInicio, fechaFin):
    return {
        "Cliente": cliente,
        "Vehiculo": vehiculo,
        "Fecha de Inicio": fechaInicio,
        "Fecha de Fin": fechaFin
    }
        
# func de mostrar reserva   
def mostrarReserva(reserva):
    
    
    return (f"Su reserva de {reserva["Cliente"]}, del vehiculo {reserva["Vehiculo"]}. Con fecha de inicio: {reserva["Fecha de Inicio"]} hasta {reserva["Fecha de Fin"]}.")

#funcion para guardar los datos en un archico de csv
def guardarReserva(reserva, archivo):
    
    return
    
