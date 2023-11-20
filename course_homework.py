import argparse
import json
import random
from datetime import datetime

def load_config():
    with open('config.json', 'r') as file:
        return json.load(file)

def save_system_state(system_state):
    with open('system_state.json', 'w') as file:
        json.dump(system_state, file)

def load_system_state():
    if not os.path.exists('system_state.json'):
        return {
            'rate': 36.00,
            'balance_uah': 10000.00,
            'balance_usd': 0.00
        }

    with open('system_state.json', 'r') as file:
        return json.load(file)

# Додайте інші функції для обміну валют, отримання балансу і т.д.

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
        system_state = restart_system()
    else:
        print('Invalid action. Please enter a valid action.')

if __name__ == "__main__":
    main()
