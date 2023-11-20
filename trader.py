import json


def load_config():
    with open('config.json', 'r') as file:
        return json.load(file)


config = load_config()
print("Початковий курс:", config["initial_conditions"]["rate"])
print("Баланс в гривнях:", config["initial_conditions"]["balance_uah"])
print("Баланс в доларах:", config["initial_conditions"]["balance_usd"])
print("Дельта:", config["delta"])
