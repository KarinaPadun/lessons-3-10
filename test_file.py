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



import json

def load_config():
    with open('config.json', 'r') as file:
        return json.load(file)

# Приклад використання
config = load_config()
print("Початковий курс:", config["initial_conditions"]["rate"])
print("Баланс в гривнях:", config["initial_conditions"]["balance_uah"])
print("Баланс в доларах:", config["initial_conditions"]["balance_usd"])
print("Дельта:", config["delta"])


