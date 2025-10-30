class Driver:

    def __init__ (self,name, car_model):

        self.name = name
        self.car_model = car_model
        self.completed_rides = []
        self.available = True

    def __str__ (self):
        return f"Driver Name: {self.name}\nCar: {self.car_model}"

driver_1=Driver("Nothando Ndlovu","Bicycle")

print(driver_1)