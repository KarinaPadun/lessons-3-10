import random
import json
from datetime import datetime
import argparse


class Trader:
    def __init__(self, config_path, history_path):
        with open(config_path) as f:
            config = json.load(f)
        self.delta = config["delta"]
        self.rate = 36.00
        self.uah_balance = 10000.00
        self.usd_balance = 0.00
        self.history_path = history_path
        self.history = []

    def save_to_history(self, action, amount):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        transaction = {"timestamp": timestamp, "action": action, "amount": amount}
        self.history.append(transaction)

    def get_rate(self):
        return round(self.rate, 2)

    def get_available_balance(self):
        return {"USD": round(self.usd_balance, 2), "UAH": round(self.uah_balance, 2)}

    def buy(self, amount):
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
        self.usd_balance = 0
        uah_amount = amount * self.rate
        self.uah_balance += uah_amount
        self.save_to_history("SELL", amount)
        return uah_amount

    def next_rate(self):
        new_rate = self.rate + random.uniform(-self.delta, self.delta)
        self.rate = round(new_rate, 2)

    def restart(self):
        self.rate = 36.00
        self.uah_balance = 10000.00
        self.usd_balance = 0.00
        self.history = []


def main():
    parser = argparse.ArgumentParser(description="Currency Trader")
    parser.add_argument("--config", type=str, default="config.json", help="Path to configuration file")
    parser.add_argument("--history", type=str, default="history.txt", help="Path to transaction history file")
    parser.add_argument("command", type=str, help="Command to execute", nargs="?")
    parser.add_argument("command_2", type=float, nargs="?", help="Second command")

    args = parser.parse_args()

    trader = Trader(args.config, args.history)

    if args.command == "RATE":
        print(trader.get_rate())
    elif args.command == "AVAILABLE":
        print(trader.get_available_balance())
    elif args.command == "NEXT":
        trader.next_rate()
        if args.command_2 is not None:
            if args.command_2 == "ALL":
                trader.buy_all()
            else:
                trader.buy(args.command_2)
    elif args.command == "RESTART":
        trader.restart()
        with open(args.history, "w") as history_file:
            history_file.write("")
    else:
        print("Unknown command")

if __name__ == "__main__":
    main()


