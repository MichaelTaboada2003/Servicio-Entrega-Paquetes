from package import Package

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

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, items):
        self._items = []
        for package in items:
            if isinstance(package, Package):
                self._items.append(package)

    @property
    def sender(self):
        return self._sender

    @sender.setter
    def sender(self, sender):
        self._sender = sender

    @property
    def receive(self):
        return self._receive

    @receive.setter
    def receive(self, receive):
        self._receive = receive

    @property
    def sender_address(self):
        return self._sender_address

    @sender_address.setter
    def sender_address(self, sender_address):
        self._sender_address = sender_address

    @property
    def receiver_address(self):
        return self._receiver_address

    @receiver_address.setter
    def receiver_address(self, receiver_address):
        self._receiver_address = receiver_address

    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, contact):
        self._contact = contact

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, time):
        self._time = time


