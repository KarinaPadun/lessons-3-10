import argparse
import json

class Trader:
    def __init__(self, rate, uah_balance, usd_balance, delta):
        self.rate = rate
        self.uah_balance = uah_balance
        self.usd_balance = usd_balance
        self.delta = delta

    def get_rate(self):
        return self.rate

    def get_available_balance(self):
        return {"USD": round(self.usd_balance, 2), "UAH": round(self.uah_balance, 2)}

    def buy(self, amount):
        if self.uah_balance < amount * self.rate:
            print(f"Недостатньо коштів, потрібна сума UAH {amount * self.rate:.2f}, доступні {self.uah_balance:.2f}")
        else:
            self.uah_balance -= amount * self.rate
            self.usd_balance += amount

    def sell(self, amount):
        if self.usd_balance < amount:
            print(f"Недостатньо коштів, потрібна сума USD {amount:.2f}, доступні {self.usd_balance:.2f}")
        else:
            self.usd_balance -= amount
            self.uah_balance += amount / self.rate

    def buy_all(self):
        self.buy(self.uah_balance / self.rate)

    def sell_all(self):
        self.sell(self.usd_balance)

    def next_rate(self):
        import random
        self.rate = round(self.rate + random.uniform(-self.delta, self.delta), 2)

    def restart(self):
        with open("history.txt", "w") as f:
            f.truncate(0)
        self.rate = 36.00
        self.uah_balance = 10000.00
        self.usd_balance = 0.00

def main():
    parser = argparse.ArgumentParser(description="Клієнтська консоль для торговця валютою")
    parser.add_argument("command_type", type=str, choices=["RATE", "AVAILABLE", "BUY", "SELL", "NEXT", "RESTART"], help="Команда для виконання")

    # Початкові умови
    with open("config.json", "r") as f:
        config = json.load(f)
    initial_rate = config["rate"]
    initial_uah_balance = config["uah_balance"]
    initial_usd_balance = config["usd_balance"]
    initial_delta = config["delta"]

    trader = Trader(initial_rate, initial_uah_balance, initial_usd_balance, initial_delta)

    # Виконання команд
    commands = {
        "RATE": trader.get_rate,
        "AVAILABLE": trader.get_available_balance,
        "BUY": lambda amount: trader.buy(amount),
        "SELL": lambda amount: trader.sell(amount),
        "NEXT": trader.next_rate,
        "RESTART": trader.restart,
    }

    # Фіксація дій у файлі
    with open("history.txt", "a") as f:
        def log(command, result):
            f.write(f"{command}: {result}\n")

        try:
            result = commands[parser.parse_args().command_type](1)
        except KeyError as e:
            print(f"Невідома команда {parser.parse_args().command_type}")
        except ValueError as e:
            print(e)
        else:
            log(parser.parse_args().command_type, result)
            print(f"Команда {parser.parse_args().command_type}: {result}")


