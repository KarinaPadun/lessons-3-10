import argparse

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
            print(f"UNAVAILABLE, REQUIRED BALANCE UAH {amount * self.rate:.2f}, AVAILABLE {self.uah_balance:.2f}")
        else:
            self.uah_balance -= amount * self.rate
            self.usd_balance += amount

    def sell(self, amount):
        if self.usd_balance < amount:
            print(f"UNAVAILABLE, REQUIRED BALANCE USD {amount:.2f}, AVAILABLE {self.usd_balance:.2f}")
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
        self.rate = 36.00
        self.uah_balance = 10000.00
        self.usd_balance = 0.00

def main():
    parser = argparse.ArgumentParser(description="Currency Trader CLI")
    parser.add_argument("command", type=str, choices=["RATE", "AVAILABLE", "BUY", "SELL", "NEXT", "RESTART"], help="Command to execute")
    parser.add_argument("command_2", nargs="?", type=str, help="Second command (optional)")

    args = parser.parse_args()

    # Початкові умови
    initial_rate = 36.00
    initial_uah_balance = 10000.00
    initial_usd_balance = 0.00
    initial_delta = 0.5

    trader = Trader(initial_rate, initial_uah_balance, initial_usd_balance, initial_delta)

    # Виконання команд
    if args.command == "RATE":
        print(trader.get_rate())
    elif args.command == "AVAILABLE":
        print(trader.get_available_balance())
    elif args.command == "BUY":
        if args.command_2 == "ALL":
            trader.buy_all()
        elif args.command_2 is not None:
            try:
                amount = float(args.command_2)
            except ValueError:
                print("Invalid amount format")
            else:
                trader.buy(amount)
    elif args.command == "SELL":
        if args.command_2 == "ALL":
            trader.sell_all()
        elif args.command_2 is not None:
            try:
                amount = float(args.command_2)
            except ValueError:
                print("Invalid amount format")
            else:
                trader.sell(amount)
    elif args.command == "NEXT":
        trader.next_rate()
    elif args.command == "RESTART":
        trader.restart()
    else:
        print("Unknown command")

if __name__ == "__main__":
    main()
