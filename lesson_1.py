
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


import os

def names_of_directories(my_directory_path) -> dict:
    if not os.path.exists(my_directory_path) or not os.path.isdir(my_directory_path):
        return {"dir_path": my_directory_path, "file_names": [], "dir_names": []}

    items = os.listdir(my_directory_path)

    file_names = [i for i in items if os.path.isfile(os.path.join(my_directory_path, i))]
    dir_names = [i for i in items if os.path.isdir(os.path.join(my_directory_path, i))]

    return {"dir_path": my_directory_path, "file_names": file_names, "dir_names": dir_names}

def update_directory_info(directory_info, item_name):
    full_path = os.path.abspath(os.path.join(directory_info['dir_path'], item_name))

    if os.path.isfile(full_path):
        if item_name not in directory_info['file_names']:
            directory_info['file_names'].append(item_name)
    elif os.path.isdir(full_path):
        if item_name not in directory_info['dir_names']:
            directory_info['dir_names'].append(item_name)
    else:
        # Если файл или папка не существует, создаем его
        if '.' in item_name:
            with open(full_path, 'w'):
                pass
            directory_info['file_names'].append(item_name)
        else:
            # Составляем полный путь для новой папки
            new_dir_path = os.path.join(directory_info['dir_path'], item_name)
            os.makedirs(new_dir_path)
            directory_info['dir_names'].append(item_name)

    return directory_info


new_dir = 'homework.a'
new_file = 'text.3552.txt'

# Приклад використання
my_directory_path = '../lessons-3-10'
directory_info = names_of_directories(my_directory_path)

updated_info_file = update_directory_info(directory_info, new_file)
print(updated_info_file)

updated_info_dir = update_directory_info(updated_info_file, new_dir)
print(updated_info_dir)
