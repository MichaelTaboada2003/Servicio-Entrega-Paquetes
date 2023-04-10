#We define the address class that will be used to request the address of the sender and the receiver
class Address():
    #the constructor of each of the package attributes is created
    def __init__(self, address: str = "address"):
        self.address = address 
      
    #the get and get are done to obtain the address for the sender 
    @property
    def sender_add(self) -> str:
        return self.address
    
    @sender_add.setter
    def sender_add(self, address) -> str:
        self.address = address
      
    #the get and get are done to obtain the address for the receiver       
    @property
    def receive_add(self) -> str:
        return self.address
    
    @receive_add.setter
    def receive_add(self, address) -> str:
        self.address = address
