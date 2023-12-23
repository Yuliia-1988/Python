import random

class Car:
    def __init__(self, model, color: str, economy: int, mileage: int = 0, fuel: int = 100):
        self.mileage = mileage
        self.fuel = fuel
        self.model = model
        self.color = color
        self.economy = economy

    def set_drive(self, distance):
        required_fuel = (distance / 100) * self.economy
        if required_fuel > self.fuel:
            raise Exception("Need more fuel to cover the distance. Please, fill more!")

        else:
            self.fuel -= required_fuel
            self.mileage += distance
            print(f"Mileage {distance} km. Fuel reserve: {self.fuel}.")

    def get_distance_left(self):
        return (self.fuel / self.economy) * 100

    def get_fuel_up(self, amount):
        self.fuel += amount
        print(f"Fuelled car. Fuel reserve: {self.fuel} litres.")

empty_car_list = []

models = ["Toyota", "Honda", "Ford", "Chevrolet", "Nissan", "BMW", "Porsche", "Lamborghini", "Ferrari", "Mclaren"]
color = ["black", "white", "red", "green", "yellow", "blue", "purple", "grey", "pink", "orange"]

model = random.choice(models)
color = random.choice(color)
economy = random.randint(10, 30)

for i in models:
    car = Car(model, color, economy)
    empty_car_list.append(car)

for car in empty_car_list:
    car.set_drive(200)
    car.get_fuel_up(20)
    car.set_drive(100)

max_fuel_car = max(empty_car_list, key=lambda x: x.fuel)

print(f"\nThe car with the largest remaining fuel: {max_fuel_car.color} {max_fuel_car.model}")
print(f"Fuel reserve: {max_fuel_car.fuel} litres.")
print(f"Mileage: {max_fuel_car.mileage} km.")
print(f"The remaining fuel allows you to drive more {max_fuel_car.get_distance_left()} km.")
