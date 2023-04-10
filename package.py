#the definition of the father class Package
class Package(object):
  #the constructor of each of the package attributes is created
    def __init__(self, id: int = 0, weight: float = 0.0, description: str = "description", cost_per_gram: float = 0.0):
        self.id = id 
        self.weight = weight
        self.description = description
        self.cost_per_gram = cost_per_gram
      
        #make a condition for when the values are less than 0  
        if self.weight < 0:
            self.weight = 0
        if self.cost_per_gram < 0:
            self.cost_per_gram = 0
          
    #We define the function that will calculate the cost of the product
    def calculate(self):
        return self.weight * self.cost_per_gram
      
    #we define the get and set of each of the attributes that are private
    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, value) -> int:
        self._id = value
    
    @property
    def weight(self) -> float:
        return self._weight
    
    @weight.setter
    def weight(self, value) -> float:
        self._weight = value if value > 0 else 0
    
    @property
    def description(self) -> str:
        return self._description
    
    @description.setter
    def description(self, value) -> str:
        self._description = value  
    
    @property
    def cost_per_gram(self) -> float:
        return self._cost_per_gram
    
    @cost_per_gram.setter
    def cost_per_gram(self, value) -> float:
        self._cost_per_gram = value if value > 0 else 0

    #We define the function that will allow us to print each of the attributes
    def __str__(self):
        return f"Package: {self.id} - {self.weight}g- {self.description} - ${self.cost_per_gram}/g"

    #The equals function is created to make the comparison between two objects.
    def equals(self, other):
        if isinstance(other, Package):
            return self.id == other.id and self.weight == other.weight and self.description == other.description and self.cost_per_gram == other.cost_per_gram
        return False

    