from argparse import ArgumentParser

args = ArgumentParser()

args.add_argument("RATE", type=str)
args.add_argument("AVAILABLE", type=str)
args.add_argument("BUY XXX", type=str)
args.add_argument("SELL XXX", type=str)
args.add_argument("BUY ALL", type=str)
args.add_argument("SELL ALL", type=str)
args.add_argument("NEXT", type=str)
args.add_argument("RESTART", type=str)


def buy(self, amount):
    if self.uah_balance < amount * self.rate:
        print(f"UNAVAILABLE, REQUIRED BALANCE UAH {amount * self.rate:.2f} , AVAILABLE {self.uah_balance: .2f}")
        return
    self.uah_balance -= amount * self.rate
    self.usd_balance += amount
    self.save_to_history("BUY", amount)


import random
import json
from datetime import datetime


class Trader:
    def __init__(self, config_path, history_path):
        with open(config_path) as f:
            config = json.load(f)
        self.delta = config["delta"]
        self.rate = 36.00
        self.uah_balance = 10000.00
        self.usd_balance = 0.00
        self.history_path = history_path

    def save_to_history(self, action, amount):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.history_path, 'a') as history_file:
            history_file.write(f"{timestamp} - {action} {amount} USD\n")

    def get_rate(self):
        return round(self.rate, 2)

    def get_available_balance(self):
        return {"USD": round(self.usd_balance, 2), "UAH": round(self.uah_balance, 2)}

    def buy(self, amount):
        if isinstance(amount, str):
            amount = self.uah_balance / self.rate
        if self.uah_balance < amount * self.rate:
            print(f"UNAVAILABLE, REQUIRED BALANCE UAH {amount * self.rate:.2f} , AVAILABLE {self.uah_balance:.2f}")
            return
        self.uah_balance -= amount * self.rate
        self.usd_balance += amount
        self.save_to_history("BUY", amount)

    def sell(self, amount):
        if self.usd_balance < amount:
            print(f"UNAVAILABLE, REQUIRED BALANCE USD {amount:.2f} , AVAILABLE {self.usd_balance:.2f}")
            return
        self.usd_balance -= amount
        self.uah_balance += amount / self.rate
        self.save_to_history("SELL", amount)

    def buy_all(self):
        amount = self.uah_balance / self.rate
        self.buy(amount)

    def sell_all(self):
        amount = self.usd_balance
        self.sell(amount)

    def next_rate(self):
        self.rate = round(self.rate + random.uniform(-self.delta, self.delta), 2)

    def restart(self):
        self.rate = 36.00
        self.uah_balance = 10000.00
        self.usd_balance = 0.00


def main():
    trader = Trader("config.json", "history.txt")

    print("Початкові умови:")
    print("Курс: {:.2f}".format(trader.rate))
    print("Гривневий рахунок: {:.2f} UAH".format(trader.uah_balance))
    print("Доларовий рахунок: {:.2f} USD".format(trader.usd_balance))
    print("Дельта: {:.2f}".format(trader.delta))

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
        elif command == "BUY ALL":
            trader.buy_all()
        elif command == "SELL ALL":
            trader.sell_all()
        elif command == "NEXT":
            trader.next_rate()
        elif command == "RESTART":
            trader.restart()
        else:
            print("Невідома команда")


if __name__ == "__main__":
    main()


    def sell_all(self):
        amount = self.usd_balance
        self.sell(amount)