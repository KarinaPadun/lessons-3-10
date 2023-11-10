# 1. Написати функцію, яка отримує один параметр - ім'я директорії та повертає словник виду
# {'filenames': [список файлів у папці], 'dirnames': [список усіх підпапок у папці]}.
# Підпапки враховувати лише першого рівня вкладення. Папка в папці в папці - таке не брати))

import os


def names_of_directories(my_directory_path) -> dict:
    if not os.path.exists(my_directory_path) or not os.path.isdir(my_directory_path):
        return {"filenames": [], "dirnames": []}

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

def sort_directory_info(directory_info, ascending=True):
    sorted_info = {
        'file_names': sorted(directory_info['file_names'], reverse=not ascending),
        'dir_names': sorted(directory_info['dir_names'], reverse=not ascending)
    }
    return sorted_info


my_directory_path = '../lessons-3-10'
directory_info = names_of_directories(my_directory_path)


sorted_info_ascending = sort_directory_info(directory_info)
print("Ascending order:")
print(sorted_info_ascending)


sorted_info_descending = sort_directory_info(directory_info, ascending=False)
print("\nDescending order:")
print(sorted_info_descending)
