# Написати клас та реалізувати його методи: (основа – ДЗ № 10)
# 1. Ініціалізація класу з одним параметром – ім'я файлу.
# повертає імя файлів (без папок)
import os


class NameFile:
    def __init__(self, directory_path):
        self.directory_path = directory_path

    def names_of_files(self):
        if not os.path.exists(self.directory_path) or not os.path.isdir(self.directory_path):
            return {"file_names": []}

        items = os.listdir(self.directory_path)
        file_names = [i for i in items if os.path.isfile(os.path.join(self.directory_path, i))]

        return {"file_names": file_names}


directory_path = '../lessons-3-10'
result = NameFile(directory_path)
res = result.names_of_files()
print(res)

# 1.2 повертає імя файлів та папок


class NameFile:
    def __init__(self, directory_path):
        self.directory_path = directory_path

    def names_of_files(self):
        if not os.path.exists(self.directory_path) or not os.path.isdir(self.directory_path):
            return {"file_names": [], "dir_names": []}

        items = os.listdir(self.directory_path)
        file_names = [i for i in items if os.path.isfile(os.path.join(self.directory_path, i))]
        dir_names = [i for i in items if os.path.isdir(os.path.join(directory_path, i))]

        return {"file_names": file_names, "dir_names": dir_names}


directory_path = '../lessons-3-10'
result = NameFile(directory_path)
res = result.names_of_files()
print(res)

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

# 2. 2


class LastName:
    def __init__(self, filename):
        self.filename = filename
        self.last_names = self.read_last_names()

    def read_last_names(self):
        with open(self.filename, 'r') as file:
            return [line.strip().split('\t')[1] for line in file if len(line.strip().split('\t')) > 1]

    def print_last_names(self):
        if self.last_names:
            print(self.last_names)
        else:
            print("Список порожній.")


if __name__ == '__main__':
    result = LastName("hom_1_2.py")
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

# 4* (*здавати не обов'язково).
# Написати метод екземпляра класу, отримує у вигляді параметра ім'я файлу (authors.txt) та повертає список
# словників виду {"date_original": date_original, "date_modified": date_modified}
# у яких date_original - це дата з рядка (якщо є),
# а date_modified - ця ж дата, представлена у форматі "dd/mm/yyyy" (d-день, m-місяць, y-рік)
# Наприклад [{"date_original": "8th February 1828", "date_modified": 08/02/1828}, ...]


class DateMod:
    def __init__(self, filename):
        self.filename = filename
        self.date_list = self.process_authors_file()

    def process_authors_file(self):
        date_list = []

        month_mapping = {
            "January": "01", "February": "02", "March": "03", "April": "04", "May": "05",
            "June": "06", "July": "07", "August": "08", "September": "09", "October": "10",
            "November": "11", "December": "12"
        }

        with open(self.filename, 'r') as file:
            current_month = ""
            for line in file:
                line = line.strip()
                if not line:
                    continue
                if line.isalpha():
                    current_month = line
                elif current_month:
                    parts = line.split('-')
                    if len(parts) >= 2:
                        date_original = parts[0].strip()
                        date_modified = date_original.replace('st', '').replace('nd', '').replace('rd', '').replace(
                            'th', '')
                        month_number = month_mapping.get(current_month, "00")
                        date_modified = date_modified.replace(current_month, month_number)
                        date_list.append({"date_original": date_original, "date_modified": date_modified})

        return date_list

    def print_mod_dates(self):
        if self.date_list:
            print(self.date_list)
        else:
            print("Список порожній.")


if __name__ == '__main__':
    result = DateMod("hom_1_3.py")
    result.print_mod_dates()
