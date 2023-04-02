class Package(object):
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
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        self._id = value
    
    @property
    def weight(self):
        return self._weight
    
    @weight.setter
    def weight(self, value):
        self._weight = value if value > 0 else 0
    
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        self._description = value  
    
    @property
    def cost_per_gram(self):
        return self._cost_per_gram
    
    @cost_per_gram.setter
    def cost_per_gram(self, value):
        self._cost_per_gram = value if value > 0 else 0
        
    def __str__(self):
        return f"Package {self.id} - {self.weight}g- {self.description} - ${self.cost_per_gram}/g"
    
    def equals(self, other):
        if isinstance(other, Package):
            return self.id == other.id and self.weight == other.weight and self.description == other.description and self.cost_per_gram == other.cost_per_gram
        return False

    