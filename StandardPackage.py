from package import Package

#We define the StandardPackage class that will inherit the attributes of the father Package class
class StandardPackage(Package):
    def __init__(self, id: int = 0, weight: float = 0.0, description: str = "description", cost_per_gram: float = 0.0, delivery_fee: float = 0.0):
        #with the super() function we can inherit the attributes of the package class
        super().__init__(id, weight, description, cost_per_gram)
        self.delivery_fee = delivery_fee
    #This function is created to be able to modify the rate attribute
    @property
    def delivery_fee(self) -> float:
        return self._delivery_fee
    
    @delivery_fee.setter
    def delivery_fee(self, value) -> float:
        if value < 0:
            self._delivery_fee = 0
        else:
            self._delivery_fee = value
          
    #The function calculate that calculates the cost of the product plus a fee is inherited from the Package class
    def calculate(self):
        return super().calculate() + self.delivery_fee

    #We define the function that will allow us to print each of the attributes
    def __str__(self):
        return f"StandardPackage: {self.id} - {self.weight}g - {self.description} - ${self.cost_per_gram}/g + ${self.delivery_fee} delivery fee"
    #The equals function is created to make the comparison between two objects
    def equals(self, other):
        if isinstance(other, StandardPackage):
            return super().equals(other) and self.delivery_fee == other.delivery_fee
        return False
