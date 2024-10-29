class Car:
    wheels = 4

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_details(self):
        return f"{self.year} {self.make} {self.model} with {self.wheels}"


my_car = Car("Toyota", "Corolla", 2020)
print(my_car.display_details())