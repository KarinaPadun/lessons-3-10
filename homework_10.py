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


def last_names(file_name):
    with open(file_name, 'r') as file:
        return [line.strip().split('\t')[1] for line in file if len(line.strip().split('\t')) > 1]


file_name = 'hom_1_2.py'
result = last_names(file_name)
print(result)


# 3. Написати функцію, яка отримує у вигляді параметра ім'я файлу (authors.txt) та повертає список
# словників виду {"date": date}
# у яких date - це дата з рядка (якщо є),
# Наприклад [{"date": "1st January 1919"}, {"date": "8th February 1828"}, ...]


def dates_from_file(filename):
    date_list = []

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip() # линия = линия в которой удаляем символи
            if any(month in line for month in ["January", "February", "March",
                                               "April", "May", "June",
                                               "July", "August", "September",
                                               "October", "November", "December"]):
                # тру если найдет месяц в линии из месяца в листе , в другом случае фолс
                date_parts = line.split('-') # дата пари равна линии разделенной по -
                if date_parts:
                    date_list.append({"date": date_parts[0].strip()}) # дата лист добавляем дату и нулевой по инлексу
                    # дату пари без символов

    return date_list


filename = 'hom_1_3.py'
result = dates_from_file(filename)
print(result)


def process_authors_file(filename):
    date_list = []
    month_mapping = {
        "January": "01", "February": "02", "March": "03", "April": "04", "May": "05",
        "June": "06", "July": "07", "August": "08", "September": "09", "October": "10",
        "November": "11", "December": "12"
    }

    with open(filename, 'r') as file:
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
                    date_modified = date_original.replace('st', '').replace('nd', '').replace('rd', '').replace('th', '')
                    date_list.append({"date_original": date_original, "date_modified": date_modified})

    return date_list

filename = 'hom_1_3.py'
result = process_authors_file(filename)
for item in result:
    print(item)



def process_authors_file(filename):
    date_list = []
    month_mapping = {
        "January": "01", "February": "02", "March": "03", "April": "04", "May": "05",
        "June": "06", "July": "07", "August": "08", "September": "09", "October": "10",
        "November": "11", "December": "12"
    }

    with open(filename, 'r') as file:
        current_month = "" # текущий месяц равен пустой строке
        for line in file: # линия в файле
            line = line.strip() # линия = линия в которой удаляем символи
            if not line: # если нет линии - продолжаем
                continue
            if line.isalpha(): # если линия содержит букви
                current_month = line # текущий месяц = линии
            elif current_month: # в другом случае
                parts = line.split('-') # часть равна линии котрая разделена по знаку -
                if len(parts) >= 2: # если длина части больше или равна 2
                    date_original = parts[0].strip() # оригинальная дата равна паре нулевого символа разделенного через стрип
                    date_modified = date_original.replace('st', '').replace('nd', '').replace('rd', '').replace('th', '')
                    # дата модификации равна дате оринигл где значение после дати равно пустоте
                    month_number = month_mapping.get(current_month, "00") #номер месяца равен месяцу которий отображает
                    # get() позволяет вернуть значение словаря по ключу, если оно существует, или другое, если указано (по-умолчанию возвращает None )
                    # ключ -значение с словаря с месяцами віше, если его нет , он равен 00
                    date_modified = date_modified.replace(current_month, month_number) # дата модификации возвращает месяц с строчки заменненний на число
                    date_list.append({"date_original": date_original, "date_modified": date_modified}) # потом добавляем все в дата лист

    return date_list

filename = 'hom_1_3.py'
result = process_authors_file(filename)
for item in result:
    print(item)


def process_authors_file(filename):
    date_list = []
    month_mapping = {
        "January": "01", "February": "02", "March": "03", "April": "04", "May": "05",
        "June": "06", "July": "07", "August": "08", "September": "09", "October": "10",
        "November": "11", "December": "12"
    }

    with open(filename, 'r') as file:
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
                    date_modified = date_original.replace('st', '').replace('nd', '').replace('rd', '').replace('th', '')
                    month_number = month_mapping.get(current_month, "00")
                    date_modified = date_modified.replace(current_month, month_number)
                    date_list.append({"date_original": date_original, "date_modified": date_modified})

    return date_list


filename = 'hom_1_3.py'
result = process_authors_file(filename)
for item in result:
    print(item)