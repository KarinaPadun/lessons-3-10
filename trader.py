import random
import json
import os


def get_rate(state):
    return state["rate"]


def get_available_balance(state):
    return {"UAH": state["uah_balance"], "USD": state["usd_balance"]}


def buy_usd(state, amount):
    if amount > state["uah_balance"]:
        raise ValueError("UNAVAILABLE, REQUIRED BALANCE UAH {}".format(amount))

    state["uah_balance"] -= amount
    state["usd_balance"] += amount / state["rate"]


def sell_usd(state, amount):
    if amount > state["usd_balance"]:
        raise ValueError("UNAVAILABLE, REQUIRED BALANCE USD {}".format(amount))

    state["uah_balance"] += amount * state["rate"]
    state["usd_balance"] -= amount


def next_rate(state):
    state["rate"] += random.uniform(-state["delta"], state["delta"])


def restart(state):
    state["rate"] = 36
    state["uah_balance"] = 10000
    state["usd_balance"] = 0


def load_state(filename):
    if not os.path.isfile(filename):
        with open(filename, "w") as f:
            json.dump({
                "rate": 36,
                "uah_balance": 10000,
                "usd_balance": 0,
                "delta": 0.5
            }, f)

    with open(filename, "r") as f:
        state = json.load(f)

    if "delta" not in state:
        state["delta"] = 0.5

    return state



def save_state(state, filename):
    with open(filename, "w") as f:
        json.dump(state, f)


def main():
    state = load_state("state.json")

    while True:
        command = input("Введіть команду: ")
        if command == "RATE":
            print("Курс: {}".format(get_rate(state)))
        elif command == "AVAILABLE":
            print(get_available_balance(state))
        elif command.startswith("BUY"):
            amount = int(command[4:])
            buy_usd(state, amount)
        elif command.startswith("SELL"):
            amount = int(command[5:])
            sell_usd(state, amount)
        elif command == "NEXT":
            next_rate(state)
        elif command == "RESTART":
            restart(state)
        else:
            print("Невідома команда")


if __name__ == "__main__":
    main()
