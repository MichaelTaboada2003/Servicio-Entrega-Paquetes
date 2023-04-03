from package import Package

class StandardPackage(Package):
    def __init__(self, id, weight, description, cost_per_gram, delivery_fee):
        super().__init__(id, weight, description, cost_per_gram)
        self.delivery_fee = delivery_fee

    @property
    def delivery_fee(self):
        return self._delivery_fee
    
    @delivery_fee.setter
    def delivery_fee(self, value):
        if value < 0:
            self._delivery_fee = 0
        else:
            self._delivery_fee = value

    def calculate(self):
        return super().calculate() + self.delivery_fee
    
    def __str__(self):
        return f"StandardPackage: {self.id} - {self.weight}g - {self.description} - ${self.cost_per_gram}/g + ${self.delivery_fee} delivery fee"
    
    def equals(self, other):
        if isinstance(other, StandardPackage):
            return super().equals(other) and self.delivery_fee == other.delivery_fee
        return False
