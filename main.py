#importamos los modeulos de los otros archivos
from vehiculos.clientes import crearCliente,mostrar_cliente
from vehiculos.vehiculos import crearVehiculo,mostrarVehiculo
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

