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
