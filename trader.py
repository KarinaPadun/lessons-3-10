import argparse
import json
import random
import os

os.chdir(r'C:\Users\Acer 5\PycharmProjects\lessons-3-10')

# Завантаження конфігурації з файлу
def load_config():
    with open('config.json', 'r') as file:
        return json.load(file)

# Отримання поточного курсу
def get_current_rate(config):
    return round(config['rate'] + random.uniform(-config['delta'], config['delta']), 2)

# Збереження стану системи у файл
def save_system_state(system_state):
    with open('system_state.txt', 'w') as file:
        file.write(json.dumps(system_state))

# Завантаження стану системи з файлу
def load_system_state():
    if os.path.exists('system_state.txt'):
        with open('system_state.txt', 'r') as file:
            return json.load(file)
    else:
        return {
            'rate': 36.00,
            'balance_uah': 10000.00,
            'balance_usd': 0.00
        }

# Покупка доларів
def buy_dollars(amount, config, system_state):
    required_amount = amount / get_current_rate(config)
    if system_state['balance_uah'] >= required_amount:
        system_state['balance_uah'] -= required_amount
        system_state['balance_usd'] += amount
        return True
    else:
        print(f'UNAVAILABLE, REQUIRED BALANCE UAH {required_amount:.2f}, AVAILABLE {system_state["balance_uah"]:.2f}')
        return False

# Продаж доларів
def sell_dollars(amount, config, system_state):
    required_amount = amount * get_current_rate(config)
    if system_state['balance_usd'] >= amount:
        system_state['balance_uah'] += required_amount
        system_state['balance_usd'] -= amount
        return True
    else:
        print(f'UNAVAILABLE, REQUIRED BALANCE USD {amount:.2f}, AVAILABLE {system_state["balance_usd"]:.2f}')
        return False

# Виведення залишків за рахунками
def print_available_balance(system_state):
    print(f'USD {system_state["balance_usd"]:.2f} UAH {system_state["balance_uah"]:.2f}')

# Отримання наступного курсу
def get_next_rate(config):
    config['rate'] = get_current_rate(config)
    return config['rate']

# Головна функція
def main():
    parser = argparse.ArgumentParser(description="Currency Trader CLI")

    parser.add_argument("action", choices=['RATE', 'AVAILABLE', 'BUY', 'SELL', 'BUY_ALL', 'SELL_ALL', 'NEXT', 'RESTART'], help="Action to perform")
    parser.add_argument("amount", nargs='?', type=float, default=None, help="Amount for BUY/SELL actions")

    args = parser.parse_args()

    config = load_config()
    system_state = load_system_state()

    if args.action == 'RATE':
        print(get_current_rate(config))
    elif args.action == 'AVAILABLE':
        print_available_balance(system_state)
    elif args.action == 'BUY':
        if args.amount is not None:
            buy_dollars(args.amount, config, system_state)
            save_system_state(system_state)
        else:
            print('Invalid command. Usage: BUY XXX')
    elif args.action == 'SELL':
        if args.amount is not None:
            sell_dollars(args.amount, config, system_state)
            save_system_state(system_state)
        else:
            print('Invalid command. Usage: SELL XXX')
    elif args.action == 'BUY_ALL':
        amount = system_state['balance_uah'] * get_current_rate(config)
        buy_dollars(amount, config, system_state)
        save_system_state(system_state)
    elif args.action == 'SELL_ALL':
        amount = system_state['balance_usd']
        sell_dollars(amount, config, system_state)
        save_system_state(system_state)
    elif args.action == 'NEXT':
        get_next_rate(config)
        save_system_state(system_state)
    elif args.action == 'RESTART':
        system_state = {
            'rate': 36.00,
            'balance_uah': 10000.00,
            'balance_usd': 0.00
        }
        save_system_state(system_state)
    else:
        print('Invalid action. Please enter a valid action.')

if __name__ == "__main__":
    main()
