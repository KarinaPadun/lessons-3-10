import json
import random
import argparse


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

    def buy_usd(self, amount):
        if amount > self.uah_balance:
            print("UNAVAILABLE, REQUIRED BALANCE UAH", amount, ", AVAILABLE", self.uah_balance)
            return
        self.uah_balance -= amount
        self.usd_balance += amount / self.rate

    def sell_usd(self, amount):
        if amount > self.usd_balance:
            print("UNAVAILABLE, REQUIRED BALANCE USD", amount, ", AVAILABLE", self.usd_balance)
            return
        self.usd_balance -= amount
        self.uah_balance += amount * self.rate

    def next_rate(self):
        self.rate = random.randint(self.rate - self.delta, self.rate + self.delta)

    def restart(self):
        self.rate = 36.00
        self.uah_balance = 10000.00
        self.usd_balance = 0.00


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", help="Command to execute")
    parser.add_argument("amount", type=int, help="Amount of USD to buy or sell")
    args = parser.parse_args()

    trader = Trader("config.json")

    if args.command == "RATE":
        print(trader.get_rate())
    elif args.command == "AVAILABLE":
        print(trader.get_available_balance())
    elif args.command == "BUY":
        trader.buy_usd(args.amount)
    elif args.command == "SELL":
        trader.sell_usd(args.amount)
    elif args.command == "NEXT":
        trader.next_rate()
    elif args.command == "RESTART":
        trader.restart()
    else:
        print("Unknown command")


if __name__ == "__main__":
    main()
