

class Car:
    def __init__(self, fuel, model, color):
        self.fuel = fuel
        self.model = model
        self.color = color

    def model(self):
        return f"This is {self.model()}"

    def fuel(self):
        return f"this is {self.fuel()}"

    def color(self):
        return f"Car is {self.color}"


car = Car("Benz", "BMW", "red")

print(car.color())