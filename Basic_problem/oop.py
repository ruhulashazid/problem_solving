
class Car:
   
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
        self.speed = 0
    

    def accelerate(self, increment):
        self.speed += increment
    

    def brake(self, decrement):
        self.speed -= decrement

    def show_speed(self):
        print("Current speed:", self.speed)


my_car = Car("Toyota", "Corolla", "Red")


my_car.accelerate(20)
my_car.show_speed()

class ElectricCar(Car):
    def __init__(self, brand, model, color, battery_capacity):
      
        super().__init__(brand, model, color)
        self.battery_capacity = battery_capacity
    

    def show_battery_capacity(self):
        print("Battery Capacity:", self.battery_capacity)


my_electric_car = ElectricCar("Tesla", "Model S", "Blue", "100 kWh")


my_electric_car.show_battery_capacity()
my_electric_car.accelerate(30)
my_electric_car.show_speed()
