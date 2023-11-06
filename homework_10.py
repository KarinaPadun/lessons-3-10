# 1. Написати функцію, яка отримує як параметр ім'я файлу назви інтернет доменів (domains.txt)
# та повертає їх у вигляді списку рядків (назви повертати без крапки).

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

# 1.2


def domains_file(file: str) -> list:
    domain_list = []
    with open(file, 'r') as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith('#'):
                domain_list.append(line.split('.')[-1])
    return domain_list


filename = 'hom_1_1.py'
result = domains_file(filename)
print(result)

# 1.3


def domains_file(filename_1):
    domain_list = []

    with open(filename_1, 'r') as file:
        for line in file:
            domain = line.strip()
            domain = domain.strip('.')
            domain_list.append(domain)

    return domain_list


filename = 'hom_1_1.py'
result = domains_file(filename)
print(result)

# 2. Написати функцію, яка отримує як параметр ім'я файла (names.txt)
# і повертає список усіх прізвищ із нього.
# Кожен рядок файлу містить номер, прізвище, країну, кілька (таблиця взята з вікіпедії).
# Розділювач - символ табуляції "t"


def last_names_file(filename):
    last_names = []

    with open(filename, 'r') as file:
        for line in file:
            data = line.strip().split('\t')
            if len(data) > 1:
                last_name = data[1]
                last_names.append(last_name)

    return last_names


filename = 'hom_1_2.py'
result = last_names_file(filename)
print(result)

# 2.2

