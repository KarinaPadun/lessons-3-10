

class Car:
    def __init__(self, fuel, model, color):
        self.fuel = fuel
        self.model = model
        self.color = color

    def get_fuel(self):
        return f"This car uses {self.fuel}."

    def get_model(self):
        return f"This is a {self.model}."

    def get_color(self):
        return f"The car is {self.color}."


car = Car("Benz", "BMW", "red")


print(car.get_fuel())
print(car.get_model())
print(car.get_color())


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            return "Error: Deposit amount must be positive."
        else:
            self.balance += amount
            return f"Deposited {amount}. New balance: {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Error: Insufficient funds."
        self.balance -= amount
        return f"Withdrew {amount}. Remaining balance: {self.balance}"

    def __str__(self):
        return f"Bank account of {self.owner}: Balance = {self.balance}"


account = BankAccount("Alice", 100)

print(account.deposit(50))
print(account.withdraw(30))
print(account)


# Написать функцию, которая переворачивает строку.

def reverse_string(s: str) -> str:
    return s[::-1]


def count_vowels(s: str) -> int:
    list_1 = ['a', 'e', 'y', 'u', 'i', 'o']
    count = 0
    for char in s.lower():
        if char in list_1:
            count += 1
    return count


def find_min_max(arr: list[int]) -> tuple[int, int]:
    return (min(arr), max(arr))
