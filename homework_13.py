# Написати клас та реалізувати його методи: (основа – ДЗ № 10)

# 1. Ініціалізація класу з одним параметром – ім'я файлу.

class FileName:
    def __init__(self, file_name):
        self.file_name = file_name


my_file = FileName("homework_13.py")
print(my_file.file_name)

# 2.1 Написати метод екземпляра класу, який створює атрибут екземпляра класу
# у вигляді списку рядків (назви повертати без крапки)


class DomainList:
    def __init__(self, file_name):
        self.file_name = file_name
        self.domain_list = self.load_domains()

    def load_domains(self):
        domain_list = []
        try:
            with open(self.file_name, 'r') as my_file:
                for line in my_file:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        domain_list.append(line.split('.')[-1])

        except FileNotFoundError:
            print(f"Файл '{self.file_name}' не знайдено")

        return domain_list

    def print_domains(self):
        if self.domain_list:
            print(self.domain_list)
        else:
            print("Список імен порожній.")


filename = 'hom_1_1.py'
domain_instance = DomainList(filename)
domain_instance.print_domains()

# 2.2


class DomainList:
    def __init__(self, file_name):
        self.file_name = file_name
        self.domain_list = self.load_domains()

    def load_domains(self):
        domain_list = []
        try:
            with open(self.file_name, 'r') as my_file:
                for line in my_file:
                    domain = line.strip()
                    domain = domain.strip('.')
                    domain_list.append(domain)

        except FileNotFoundError:
            print(f"Файл '{self.file_name}' не знайдено")

        return domain_list

    def print_domains(self):
        if self.domain_list:
            print(self.domain_list)
        else:
            print("Список порожній.")



filename = 'hom_1_1.py'
domain_instance = DomainList(filename)
domain_instance.print_domains()

# 2.3


class DomainList:
    def __init__(self, file_name):
        self.file_name = file_name
        self.domain_list = self.load_domains()

    def load_domains(self):
        domain_list = []
        try:
            with open(self.file_name, 'r') as my_file:
                for line in my_file:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        domain_list.append(line.split('.')[-1])

        except FileNotFoundError:
            print(f"Файл '{self.file_name}' не знайдено")

        return domain_list

    def create_name_list(self):
        if self.domain_list:
            name_list = [name for name in self.domain_list]
            return name_list
        else:
            print("Список порожній.")
            return []

    def print_domains(self):
        if self.domain_list:
            print(self.domain_list)
        else:
            print("Список порожній.")


filename = 'hom_1_1.py'
domain_instance = DomainList(filename)
name_list = domain_instance.create_name_list()
print(name_list)


# 2. Написати метод екземпляра класу, який повертає список усіх прізвищ із файлу.
# Кожен рядок файлу містить номер, прізвище, країну, кілька (таблиця взята з вікіпедії).
# Розділювач - символ табуляції "t"

class LastName:
    def __init__(self, filename):
        self.filename = filename
        self.last_names = self.read_last_names()

    def read_last_names(self):
        last_names = []

        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    data = line.strip().split('\t')
                    if len(data) > 1:
                        last_name = data[1]
                        last_names.append(last_name)
        except FileNotFoundError:
            print(f"Файл не знайдено")

        return last_names

    def print_last_names(self):
        if self.last_names:
            print(self.last_names)
        else:
            print("Список порожній.")


if __name__ == '__main__':
    result = LastName( "hom_1_2.py")
    result.print_last_names()


# 3. Написати метод екземпляра класу, який повертає список
# словників виду {"date": date} у яких date - це дата з рядка (якщо є),
# Наприклад [{"date": "1st January 1919"}, {"date": "8th February 1828"}, ...]

class Date:
    def __init__(self, filename):
        self.filename = filename
        self.date_list = self.dates_from_file()

    def dates_from_file(self):
        date_list = []

        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    line = line.strip()
                    if any(month in line for month in ["January", "February", "March",
                                               "April", "May", "June",
                                               "July", "August", "September",
                                               "October", "November", "December"]):
                        date_parts = line.split('-')
                        if date_parts:
                            date_list.append({"date": date_parts[0].strip()})
        except FileNotFoundError:
            print(f"Файл не знайдено")

        return date_list

    def print_dates(self):
        if self.date_list:
            print(self.date_list)
        else:
            print("Список порожній.")


if __name__ == '__main__':
    result = Date("hom_1_3.py")
    result.print_dates()

