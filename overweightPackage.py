from package import Package

class OverweightPackage(Package):
    def __init__(self, id, weight, description, cost_per_gram, overweight_cost_per_gram):
        super().__init__(id, weight, description, cost_per_gram)
        self.overweight_cost_per_gram = overweight_cost_per_gram

    @property
    def overweight_cost_per_gram(self):
        return self._overweight_cost_per_gram

    @overweight_cost_per_gram.setter
    def overweight_cost_per_gram(self, overweight_cost_per_gram):
        self._overweight_cost_per_gram = overweight_cost_per_gram

    def calculate(self):
        if self.weight > 50:
            overweight_cost = (self.weight - 50) * self.overweight_cost_per_gram
            return super().calculate() + overweight_cost
        else:
            return super().calculate()
        
    def __str__(self):
        return f"OverweightPackage: {self.id} - {self.weight}g - {self.description} - ${self.cost_per_gram}/g + ${self.overweight_cost_per_gram} overweight_cost" 
        
    def equals(self, other):
        if isinstance(other, OverweightPackage):
            return super().equals(other) and self.overweight_cost_per_gram == other.overweight_cost_per_gram
        return False
