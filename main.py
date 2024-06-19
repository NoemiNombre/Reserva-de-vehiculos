#importamos los modeulos de los otros archivos
from vehiculos.clientes import crearCliente,mostrar_cliente
from vehiculos.vehiculos import crearVehiculo,mostrarVehiculo,alquilarVehiculo,devolverVehiculo
from vehiculos.reservas import crearReserva, mostrarReserva, guardarReserva

# creo los clientes con su info
cliente1 = crearCliente("Juan Martin","Pazmiño","M34567TH")
cliente2 = crearCliente("Samia Noemi","Camacho","ME1234PO")

# crear info de vehiculos 
vehiculo1 = crearVehiculo("KL123","Audi",70)
vehiculo2 = crearVehiculo("KL789","Mclaren",100)
vehiculo3 = crearVehiculo("KL458","Aston Martin",80)
vehiculo4 = crearVehiculo("KL892","Ferrari",120)
vehiculo5 = crearVehiculo("KL024","Chery",66)

# crear reserva de los vehiculospara saber cual esta disponible o no 

fechaInicio = (2,12,2024)
fechaFin = (10,12,2024)

reserva1 = crearReserva(cliente1,vehiculo3,fechaInicio,fechaFin)
reserva2 = crearReserva(cliente2,vehiculo5,fechaInicio,fechaFin)

#alquilar vehiculo (hacer lo no disponible )

alquilarVehiculo(vehiculo3)
alquilarVehiculo(vehiculo5)

#mostrar reservas 
print(mostrarReserva(reserva1))

print(mostrarReserva(reserva2))

#guardar reservas en csv
reservas=[reserva1,reserva2]

guardarReserva(reservas,"reservas.csv")
  
#devolver los vehiculos 
devolverVehiculo(vehiculo3)
devolverVehiculo(vehiculo5)


