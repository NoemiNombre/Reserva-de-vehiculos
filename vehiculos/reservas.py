import pandas as pd 

#fun para crear la resrva
def crearReserva(cliente, vehiculo, fechaInicio, fechaFin):
    return {
        "cliente": cliente,
        "vehiculo": vehiculo,
        "fechaInicio": fechaInicio,
        "fechaFin": fechaFin
    }
        
# func de mostrar reserva   
def mostrarReserva(reserva):
    cliente = f"{reserva["cliente"]["nombre"]} {reserva["cliente"]["apellido"]}"
    vehiculo = f"{reserva["vehiculo"]["matricula"]} {reserva["vehiculo"]["modelo"]}"
    
    return (f"Su reserva de {reserva["cliente"]}, del vehiculo {reserva["vehiculo"]}. Con fecha de inicio: {reserva["fechaInicio"]} hasta {reserva["fechaFin"]}.")

#funcion para guardar los datos en un archico de csv
def guardarReserva(reservas, archivo):
    data = [{
        "Cliente": f"{reserva["cliente"]["nombre"]} {reserva["cliente"]["apellido"]}",
        "Vehiculo":f"{reserva["vehiculo"]["matricula"]} {reserva["vehiculo"]["modelo"]}",
        "Fecha Inicio":f"{reserva["fechaInicio"]}",
        "Fecha Fin":f"{reserva["fechaFin"]}"
    } for reserva in reservas]
    
    df = pd.DataFrame(data)
    df.to_csv(archivo, index=False)
  
    
 