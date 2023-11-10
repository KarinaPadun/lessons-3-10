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



def sort_directory_names(directory_info, ascending=True):
    sorted_info = {
        'file_names': sorted(directory_info['file_names'], reverse=not ascending),
        'dir_names': sorted(directory_info['dir_names'], reverse=not ascending)
    }
    return sorted_info


directory_info = {
    'file_names': ["filenames": []",
    'dir_names': []
}

sorted_info_ascending = sort_directory_names(directory_info)
sorted_info_descending = sort_directory_names(directory_info, ascending=False)

def display_sorted_info(info, order):
    print(f"{order} order:")
    print(info)

display_sorted_info(sorted_info_ascending, "Ascending")
display_sorted_info(sorted_info_descending, "Descending")
