#hola como vas 
class Address():
    def __init__(self, address):
        self.address = address 

    @property
    def sender_add(self):
        return self.address
    
    @sender_add.setter
    def sender_add(self, address):
        self.address = address
        
    @property
    def receive_add(self):
        return self.address
    
    @receive_add.setter
    def receive_add(self, address):
        self.address = address
