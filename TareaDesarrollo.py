



class Package:
    def __init__(self, id, weight, description, cost_per_gram):
        self.id = id 
        self.weight = weight
        self.description = description
        self.cost_per_gram = cost_per_gram
        
        if self.weight < 0:
            self.weight = 0
        if self.cost_per_gram < 0:
            self.cost_per_gram = 0

    def calculate(self):
        return self.weight * self.cost_per_gram
    
    def get_id(self):
        return self.id
    
    def set_id(self, id):
        self.id = id
    
    def get_weight(self):
        return self.weight
    
    def set_weight(self, weight):
        self.weight = weight
    
    def get_description(self):
        return self.description
    
    def set_description(self, description):
        self.description = description  
    
    def get_cost_per_gram(self):
        return self.cost_per_gram
    
    def set_cost_per_gram(self, cost_per_gram):
        self.cost_per_gram = cost_per_gram
        
    def __str__(self):
        return f"Package {self.id} - {self.weight}g- {self.description} - ${self.cost_per_gram}/g"
    
    def equals(self, other):
        if isinstance(other, Package):
            return self.id == other.id and self.weight == other.weight and self.description == other.description and self.cost_per_gram == other.cost_per_gram
        return False

class StandardPackage(Package):
    def __init__(self, id, weight, description, cost_per_gram, delivery_fee):
        super().__init__(id, weight, description, cost_per_gram)
        self.delivery_fee = delivery_fee

    def calculate(self):
        return super().calculate() + self.delivery_fee
    
    def __str__(self):
        return f"StandardPackage {self.id} - {self.description} - {self.weight}g - ${self.cost_per_gram}/g + ${self.delivery_fee} delivery fee"
    
    def equals(self, other):
        if isinstance(other, StandardPackage):
            return super().equals(other) and self.delivery_fee == other.delivery_fee
        return False


class OverweightPackage(Package):
    def __init__(self, id, weight, description, cost_per_gram, overweight_cost_per_gram):
        super().__init__(id, weight, description, cost_per_gram)
        self.overweight_cost_per_gram = overweight_cost_per_gram

    def calculate(self):
        if self.weight > 50:
            overweight_cost = (self.weight - 50) * self.overweight_cost_per_gram
            return super().calculate() + overweight_cost
        else:
            return super().calculate()
        
    def __str__(self):
        return f"OverweightPackage with id {self.id}, weight {self.weight}, cost per gram {self.cost_per_gram}, description {self.description}, and overweight cost per gram {self.overweight_cost_per_gram}." 
        
    def equals(self, other):
        if isinstance(other, OverweightPackage):
            return super().equals(other) and self.overweight_cost_per_gram == other.overweight_cost_per_gram
        return False

class Address():
    def __init__(self, address):
        self.address = address 
        
    def get_sender_add(self):
        return self.address
    
    def set_sender_add(self, address):
        self.address = address
        
    def get_receive_add(self):
        return self.address
    
    def set_receive_add(self, address):
        self.address = address
    
class Person():
    def __init__(self, name, contact):
        self.name = name 
        self.contact = contact
        
    def get_sender(self):
        return self.name
    
    def set_sender(self, name):
        self.sender = name
        
    def get_receive(self):
        return self.name
    
    def set_receive(self, name):
        self.receive = name
        
    def get_contact(self):
        return self.contact
    
    def set_contact(self, contact):
        self.contact = contact
    
class Delivery:
    def __init__(self, item, sender, receive, sender_address, receiver_address, contact, date, time):
        self.items = []
        for package in item:
            if isinstance(package, Package):
                self.items.append(package)
        self.sender = sender
        self.receive = receive
        self.sender_address = sender_address
        self.receiver_address = receiver_address
        self.contact = contact
        self.date = date
        self.time = time

    def get_items(self):
        return self.items

    def set_items(self, items):
        self.items = []
        for package in items:
            if isinstance(package, Package):
                self.items.append(package)

    def get_sender(self):
        return self.sender

    def set_sender(self, sender):
        self.sender = sender

    def get_receive(self):
        return self.receive

    def set_receive(self, receive):
        self.receive = receive

    def get_sender_address(self):
        return self.sender_address

    def set_sender_address(self, sender_address):
        self.sender_address = sender_address

    def get_receiver_address(self):
        return self.receiver_address

    def set_receiver_address(self, receiver_address):
        self.receiver_address = receiver_address

    def get_contact(self):
        return self.contact

    def set_contact(self, contact):
        self.contact = contact

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = date

    def get_time(self):
        return self.time

    def set_time(self, time):
        self.time = time



# Crear dos paquetes
package1 = Package(1, 100, "Libro", 0.1)
package2 = StandardPackage(2, 200, "Libreta", 0.05, 20)

# Crear una dirección de origen y una de destino
sender_address = Address("Bonanza Vista Manzana 9 lote 21 Turbaco")
receiver_address = Address("Nuevo Bosque Lote 24 Cartagena")

# Crear una persona remitente y una destinataria
sender = Person("Michael", "555-1234")
receiver = Person("Andres", "555-5678")

# Crear un envío con los paquetes, las direcciones y las personas creadas anteriormente
shipment = Delivery([package1, package2], sender, receiver, sender_address, receiver_address, "555-1212", "2023-03-22", "09:00")

# Imprimir información sobre el envío
print("\nInvolucrados:\n")
print(f"Remitente: {shipment.get_sender().get_sender()} - Contacto: {shipment.get_sender().get_contact()} - Dirección: {shipment.get_sender_address().get_sender_add()}")
print(f"Receptor: {shipment.get_receive().get_receive()} - Contacto: {shipment.get_receive().get_contact()} - Dirección: {shipment.get_receiver_address().get_sender_add()}")
print("\nProductos:\n")
for item in shipment.get_items():
    print(item)
print(f"\nFecha de entrega: {shipment.get_date()} - Hora de entrega: {shipment.get_time()} - Contacto: {shipment.get_contact()}")


       







