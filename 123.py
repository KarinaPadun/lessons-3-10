import random
import json
from datetime import datetime
import argparse


class Trader:
    def __init__(self, config_path, history_path):
        self.config_path = config_path
        self.history_path = history_path
        self.history = []
        self.load_history()
        config = self.load_config()
        self.delta = config["delta"]
        if len(self.history) < 1:
            self.rate = config["rate"]
            self.uah_balance = config["uah_balance"]
            self.usd_balance = config["usd_balance"]

    def load_config(self):
        with open(self.config_path) as f:
            config = json.load(f)
        return config

    def load_history(self):
        try:
            with open(self.history_path, "r") as history_file:
                history_data = json.load(history_file)
                if isinstance(history_data, list) and len(history_data) > 0:
                    self.history = history_data
                    self.rate = history_data[-1].get("rate", 0)
                    self.uah_balance = history_data[-1].get("uah_balance", 0)
                    self.usd_balance = history_data[-1].get("usd_balance", 0)
                elif isinstance(history_data, dict):
                    self.history = history_data.get("history", [])
                    self.rate = history_data.get("rate", 0)
                    self.uah_balance = history_data.get("uah_balance", 0)
                    self.usd_balance = history_data.get("usd_balance", 0)

        except (FileNotFoundError, json.JSONDecodeError):
            self.history = []

    def save_to_history(self, action, currency_amount, uah_amount, rate, old_rate):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        transaction = {"timestamp": timestamp, "action": action, "usd_balance": currency_amount,
                       "uah_balance": uah_amount, "rate": rate, "old_rate": old_rate}
        self.history.append(transaction)

        with open(self.history_path, "w") as history_file:
            json.dump(self.history, history_file, indent=4)

    def get_rate(self):
        return round(self.rate, 2)

    def get_available_balance(self):
        return {"USD": round(self.usd_balance, 2), "UAH": round(self.uah_balance, 2)}

    def buy(self, amount):
        if amount.lower() == "all":
            self.buy_all()
        else:
            amount = float(amount)
            if self.uah_balance < amount * self.rate:
                print(f"UNAVAILABLE, REQUIRED BALANCE UAH {amount * self.rate:.2f}, AVAILABLE {self.uah_balance:.2f}")
                return
            self.uah_balance -= amount * self.rate
            self.usd_balance += amount
            self.save_to_history("BUY", self.usd_balance, self.uah_balance, self.rate, self.rate)

    def sell(self, amount):
        amount = float(amount)
        if self.usd_balance < amount:
            print(f"UNAVAILABLE, REQUIRED BALANCE USD {amount:.2f}, AVAILABLE {self.usd_balance:.2f}")
            return
        self.usd_balance -= amount
        self.uah_balance += amount / self.rate
        self.save_to_history("SELL", amount, amount / self.rate, self.rate, self.rate)

    def buy_all(self):
        if self.uah_balance == 0:
            print(f"UNAVAILABLE, REQUIRED BALANCE UAH {self.uah_balance:.2f}, AVAILABLE 0.00")
            return 0.0

        amount = self.uah_balance / self.rate
        self.uah_balance -= amount * self.rate
        self.usd_balance += amount
        self.save_to_history("BUY", amount, amount * self.rate, self.rate, self.rate)
        return amount

    def sell_all(self):
        amount = self.usd_balance
        if amount == 0:
            print("No USD to sell.")
            return
        self.usd_balance = 0
        uah_amount = amount * self.rate
        self.uah_balance += uah_amount
        self.save_to_history("SELL", self.usd_balance, self.uah_balance, self.rate, self.rate)
        return uah_amount

    def next_rate(self):
        old_rate = self.rate
        self.rate += random.uniform(-self.delta, self.delta)
        self.rate = round(self.rate, 2)

        self.save_to_history("RATE_CHANGE",self.usd_balance, self.uah_balance,  self.rate, old_rate)

    def get_history(self):
        return self.history

    def restart(self):
        with open(self.history_path, 'w') as history_file:
            history_file.write('[]')

        with open(self.config_path) as f:
            config = json.load(f)

        self.rate = config["rate"]
        self.uah_balance = config["uah_balance"]
        self.usd_balance = config["usd_balance"]
        self.load_history()


def main():
    parser = argparse.ArgumentParser(description="Currency Trader")
    parser.add_argument("--config", type=str, default="config.json", help="Path to configuration file")
    parser.add_argument("--history", type=str, default="history.json", help="Path to transaction history file")
    parser.add_argument("command", type=str, help="Command to execute", nargs="?")
    parser.add_argument("command_2", type=str, nargs="?", help="Second command")

    args = parser.parse_args()

    trader = Trader(args.config, args.history)

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
        bought_amount = trader.buy_all()
        if bought_amount > 0:
            print(f"Bought {bought_amount} USD. {trader.get_available_balance()}")
        else:
            print("No USD bought.")
    elif args.command == "SELL":
        if args.command_2 is not None:
            trader.sell(args.command_2)
            print(trader.get_available_balance())
        else:
            print("Invalid amount format for sell command")
    elif args.command == "SELL_ALL":
        uah_amount = trader.sell_all()
        if uah_amount is not None:
            print(trader.get_available_balance())
    elif args.command == "RESTART":
        trader.restart()
        trader.load_history()
    else:
        print("Unknown command")


if __name__ == "__main__":
    main()