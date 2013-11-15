class Car(object):
	condition = "new"
	def __init__(self, model, color, mpg):
		self.model = model
		self.color = color
		self.mpg = mpg
        
    def displayCar(self):
        return "This is a %s %s with %s MPG." % (self.color, self.model, self.mpg)
     
    def driveCar(self):
        self.condition = "used"


class ElectricCar(Car):
    def __init__(self, model, color, mpg, typeOfBattery):
        self.model = model
        self.color = color
        self.mpg = mpg
        self.typeOfBattery = typeOfBattery
        
    def driveCar(self):
        self.condition = "like new"
        
myCar = ElectricCar("Nissan", "silver", 99, "molten salt")
print myCar.driveCar()
