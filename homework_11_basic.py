# 1. Написати функцію, яка отримує один параметр - ім'я директорії та повертає словник виду
# {'filenames': [список файлів у папці], 'dirnames': [список усіх підпапок у папці]}.
# Підпапки враховувати лише першого рівня вкладення. Папка в папці в папці - таке не брати))

import os


def names_of_directories(my_directory_path) -> dict:
    if not os.path.exists(my_directory_path) or not os.path.isdir(my_directory_path):
        return {"file_names": [], "dir_names": []}

    items = os.listdir(my_directory_path)

    file_names = [i for i in items if os.path.isfile(os.path.join(my_directory_path, i))]
    dir_names = [i for i in items if os.path.isdir(os.path.join(my_directory_path, i))]

    return {"file_names": file_names, "dir_names": dir_names}


my_directory_path = '../lessons-3-10'
result = names_of_directories(my_directory_path)
print(result)


# 2 Написати функцію, яка отримує два параметри – словник, описаний у пункті 1
# і значення булю (True/False) - можна зробити за замовчуванням.
# Функція повертає той самий словник, але з відсортованими іменами файлів та папок у відповідних списках.
# Булеве значення True означає, що порядок сортування алфавітний, False – зворотний порядок.

def sort_directory_info(directory_info, alphabetically=True):
    sorted_info = {
        'file_names': sorted(directory_info['file_names'], reverse=not alphabetically),
        'dir_names': sorted(directory_info['dir_names'], reverse=not alphabetically)
    }
    return sorted_info


my_directory_path = '../lessons-3-10'
directory_info = names_of_directories(my_directory_path)


sorted_info_ascending = sort_directory_info(directory_info)
print("Alphabetically order:")
print(sorted_info_ascending)


sorted_info_descending = sort_directory_info(directory_info, alphabetically=False)
print("\nNo Alphabetically order:")
print(sorted_info_descending)

# 3 Написати функцію, яка отримує два параметри - словник, описаний у пункті 1 та рядок, який може бути
# або ім'ям файлу, або ім'ям папки. (У імені файлу має бути точка).
# Залежно від того, що функція отримала (ім'я файлу або ім'я папки) – записати його у відповідний список
# та повернути оновлений словник.


def names_of_directories(my_directory_path) -> dict:
    if not os.path.exists(my_directory_path) or not os.path.isdir(my_directory_path):
        return {"dir_path": my_directory_path, "file_names": [], "dir_names": []}

    items = os.listdir(my_directory_path)

    file_names = [i for i in items if os.path.isfile(os.path.join(my_directory_path, i))]
    dir_names = [i for i in items if os.path.isdir(os.path.join(my_directory_path, i))]

    return {"dir_path": my_directory_path, "file_names": file_names, "dir_names": dir_names}


def updated_dictionary(dir_info, item_name):
    full_path = os.path.abspath(os.path.join(dir_info['dir_path'], item_name))

    if os.path.isfile(full_path):
        if item_name not in dir_info['file_names']:
            dir_info['file_names'].append(item_name)
    elif os.path.isdir(full_path):
        if item_name not in dir_info['dir_names']:
            dir_info['dir_names'].append(item_name)
    else:
        if '.' in item_name:
            with open(full_path, 'w'):
                pass
            dir_info['file_names'].append(item_name)
        else:
            new_dir_path = os.path.join(dir_info['dir_path'], item_name)
            os.makedirs(new_dir_path)
            dir_info['dir_names'].append(item_name)

    return dir_info


new_dir = 'A'
new_file = 'text.3552.txt'


my_directory_path = '../lessons-3-10'
directory_info = names_of_directories(my_directory_path)

updated_info_file = updated_dictionary(directory_info, new_file)
print(updated_info_file)

updated_info_dir = updated_dictionary(updated_info_file, new_dir)
print(updated_info_dir)