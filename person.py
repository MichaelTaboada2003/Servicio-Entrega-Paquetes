#We define the person class that will help us to determine the information of the sender and the sender
class Person():
    def __init__(self, name: str = "name", contact: str = "contact"):
        self.name = name 
        self.contact = contact

    #the get and the set are done to get the name of the sender
    @property
    def sender(self) -> str:
        return self.name
    
    @sender.setter
    def sender(self, name) -> str:
        self.name = name

    #the get and the set are done to get the name of the receiver  
    @property
    def receiver(self) -> str:
        return self.name
    
    @receiver.setter
    def receiver(self, name) -> str:
        self.name = name

    #get and set are done for contact attribute  
    @property
    def contact(self) -> str:
        return self._contact
    
    @contact.setter
    def contact(self, contact) -> str:
        self._contact = contact
