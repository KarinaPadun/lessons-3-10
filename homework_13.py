# Написати клас та реалізувати його методи: (основа – ДЗ № 10)

# 1. Ініціалізація класу з одним параметром – ім'я файлу.
class FileName:
    def domains_file(file: str) -> list:
        domain_list = []
        try:
            with open(file, 'r') as my_file:
                for line in my_file:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        domain_list.append(line.split('.')[-1])

        except FileNotFoundError:
            print(f"Файл '{file}' не знайдено")

        return domain_list

    filename = 'hom_1_1.py'
    result = domains_file(filename)
    print(result)


# 2. Написати метод екземпляра класу, який створює атрибут екземпляра класу
# у вигляді списку рядків (назви повертати без крапки)

# 2. Написати метод екземпляра класу, який повертає список усіх прізвищ із файлу.
# Кожен рядок файлу містить номер, прізвище, країну, кілька (таблиця взята з вікіпедії).
# Розділювач - символ табуляції "t"

# 3. Написати метод екземпляра класу, який повертає список
# словників виду {"date": date} у яких date - це дата з рядка (якщо є),
# Наприклад [{"date": "1st January 1919"}, {"date": "8th February 1828"}, ...]
