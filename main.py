from package import Package
from standardPackage import StandardPackage
from address import Address
from person import Person
from delivery import Delivery
from overWeightPackage import OverweightPackage

# Crear dos paquetes
package1 = Package(1, 100, "Libro", 0.1)
package2 = StandardPackage(2, 200, "Libreta", 0.05, 20)
package3 = OverweightPackage(3, 200, "Libreta", 0.05, 55)

# Crear una dirección de origen y una de destino
sender_address = Address("Bonanza Vista Manzana 9 lote 21 Turbaco")
receiver_address = Address("Nuevo Bosque Lote 24 Cartagena")

# Crear una persona remitente y una destinataria
sender = Person("Michael", "555-1234")
receiver = Person("Andres", "555-5678")

# Crear un envío con los paquetes, las direcciones y las personas creadas anteriormente
shipment = Delivery([package1, package2, package3], sender, receiver, sender_address, receiver_address, "555-1212", "2023-03-22", "09:00")

print("\nInvolucrados:\n")
print(f"Remitente: {shipment.sender.sender} - Contacto: {shipment.sender.contact} - Dirección: {shipment.sender_address.sender_add}")
print(f"Receptor: {shipment.receive.receiver} - Contacto: {shipment.receive.contact} - Dirección: {shipment.receiver_address.sender_add}")
print("\nProductos:\n")
for item in shipment.items:
    print(item)
print(f"\nFecha de entrega: {shipment.date} - Hora de entrega: {shipment.time} - Contacto: {shipment.contact}")
