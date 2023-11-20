import random
import json


class Trader:
    def __init__(self, config_path):
        with open(config_path) as f:
            config = json.load(f)
        self.delta = config["delta"]
        self.rate = 36.00
        self.uah_balance = 10000.00
        self.usd_balance = 0.00

    def get_rate(self):
        return self.rate

    def get_available_balance(self):
        return {"USD": self.usd_balance, "UAH": self.uah_balance}

    def buy(self, amount):
        if self.uah_balance < amount * self.rate:
            print("UNAVAILABLE, REQUIRED BALANCE UAH {} , AVAILABLE {}".format(amount * self.rate, self.uah_balance))
            return
        self.uah_balance -= amount * self.rate
        self.usd_balance += amount

    def sell(self, amount):
        if self.usd_balance < amount:
            print("UNAVAILABLE, REQUIRED BALANCE USD {} , AVAILABLE {}".format(amount, self.usd_balance))
            return
        self.usd_balance -= amount
        self.uah_balance += amount / self.rate

    def next_rate(self):
        self.rate = self.rate + random.uniform(-self.delta, self.delta)

    def restart(self):
        self.rate = 36.00
        self.uah_balance = 10000.00
        self.usd_balance = 0.00


def main():
    trader = Trader("config.json")

    while True:
        command = input("Введіть команду: ")
        if command == "RATE":
            print(trader.get_rate())
        elif command == "AVAILABLE":
            print(trader.get_available_balance())
        elif command.startswith("BUY"):
            amount = float(command[4:])
            trader.buy(amount)
        elif command.startswith("SELL"):
            amount = float(command[5:])
            trader.sell(amount)
        elif command == "NEXT":
            trader.next_rate()
        elif command == "RESTART":
            trader.restart()
        else:
            print("Невідома команда")


if __name__ == "__main__":
    main()
