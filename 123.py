import random
import json
from datetime import datetime
import argparse


class Trader:
    def __init__(self, history_path, config_path):
        self.history_path = history_path
        self.config_path = config_path
        self.load_history()

    def load_config(self):
        try:
            with open(self.config_path, "r") as config_file:
                config_data = json.load(config_file)
                self.rate = float(config_data["rate"])
                self.uah_balance = float(config_data["uah_balance"][:-4])
                self.usd_balance = float(config_data["usd_balance"][:-4])
                self.delta = float(config_data["delta"])
        except FileNotFoundError:
            print(f"Config file '{self.config_path}' not found.")

    def load_history(self):
        try:
            with open(self.history_path, "r") as history_file:
                lines = history_file.readlines()
                if lines:
                    last_line = lines[-1].strip()
                    values = last_line.split()
                    if len(values) == 2:
                        uah, usd = map(float, values)
                        self.uah_balance = uah
                        self.usd_balance = usd
        except FileNotFoundError:
            print(f"History file '{self.history_path}' not found.")
            open(self.history_path, "w").close()

    def save_to_history(self, action, amount):
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        return timestamp

    def get_rate(self):
        return round(self.rate, 2)

    def get_available_balance(self):
        return {"USD": round(self.usd_balance, 2), "UAH": round(self.uah_balance, 2)}

    def buy(self, amount):
        if self.uah_balance < amount * self.rate:
            print(f"UNAVAILABLE, REQUIRED BALANCE UAH {amount * self.rate:.2f}, AVAILABLE {self.uah_balance:.2f}")
            return
        self.uah_balance -= amount * self.rate
        self.usd_balance += amount
        self.save_to_history("BUY", amount)

    def sell(self, amount):
        if self.usd_balance < amount:
            print(f"UNAVAILABLE, REQUIRED BALANCE USD {amount:.2f}, AVAILABLE {self.usd_balance:.2f}")
            return
        self.usd_balance -= amount
        self.uah_balance += amount / self.rate
        self.save_to_history("SELL", amount)

    def buy_all(self):
        if self.uah_balance == 0:
            print(f"UNAVAILABLE, REQUIRED BALANCE UAH {self.uah_balance:.2f}, AVAILABLE 0.00")
            return
        amount = self.uah_balance / self.rate
        self.buy(amount)

    def sell_all(self):
        amount = self.usd_balance
        if amount == 0:
            print("No USD to sell.")
            return
        self.usd_balance = 0
        uah_amount = amount * self.rate
        self.uah_balance += uah_amount
        self.save_to_history("SELL", amount)
        return uah_amount

    def next_rate(self):
        self.rate += random.uniform(-self.delta, self.delta)
        self.rate = round(self.rate, 2)

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

    trader = Trader(args.history, args.config)

    if args.command == "RATE":
        print(trader.get_rate())
    elif args.command == "AVAILABLE":
        print(trader.get_available_balance())
    elif args.command == "NEXT":
        trader.next_rate()
        print(trader.get_rate())
    elif args.command == "BUY":
        if args.command_2 is not None:
            trader.buy(args.command_2)
            print(trader.get_available_balance())
        else:
            print("Invalid amount format")
    elif args.command == "BUY_ALL":
        trader.buy_all()
        print(trader.get_available_balance())
    elif args.command == "SELL_ALL":
        uah_amount = trader.sell_all()
        if uah_amount is not None:
            print(trader.get_available_balance())
    elif args.command == "RESTART":
        trader.restart()
        with open(args.history, "w") as history_file:
            history_file.write("")
    else:
        print("Unknown command")

if __name__ == "__main__":
    main()
