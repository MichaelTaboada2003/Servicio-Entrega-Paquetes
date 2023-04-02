class Person():
    def __init__(self, name, contact):
        self.name = name 
        self.contact = contact
        
    @property
    def sender(self):
        return self.name
    
    @sender.setter
    def sender(self, name):
        self.name = name
        
    @property
    def receiver(self):
        return self.name
    
    @receiver.setter
    def receiver(self, name):
        self.name = name
        
    @property
    def contact(self):
        return self._contact
    
    @contact.setter
    def contact(self, contact):
        self._contact = contact
