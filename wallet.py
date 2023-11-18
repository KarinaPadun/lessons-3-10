# история системи сколько денег сколько куплено какой курс
# Стан системи (курс і доступний баланс кожної валюти) зчитується і зберігається
# у окремому файлі (формат файлу не розсуд розробника).
import argparse
import json
import random
import os


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

