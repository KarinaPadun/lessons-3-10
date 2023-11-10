import os


def names_of_directories(my_directory_path) -> dict:
    if not os.path.exists(my_directory_path) or not os.path.isdir(my_directory_path):
        return {"file_names": [], "dir_names": []}

    items = os.listdir(my_directory_path)

    file_names = [i for i in items if os.path.isfile(os.path.join(my_directory_path, i))]
    dir_names = [i for i in items if os.path.isdir(os.path.join(my_directory_path, i))]

    return {"file_names": file_names, "dir_names": dir_names}


def update_directory_info(directory_info, name):
    full_path = os.path.abspath(name)

    if os.path.isfile(full_path):
        directory_info['file_names'].append(name)
    elif os.path.isdir(full_path):
        directory_info['dir_names'].append(name)

    return directory_info


# Приклад використання
my_directory_path = '../lessons-3-10'
directory_info = names_of_directories(my_directory_path)
print("До оновлення:")
print(directory_info)

# Приклад додавання файлу
updated_info_file = update_directory_info(directory_info, '../lessons-3-10/file3.txt')
print("\nПісля додавання файлу:")
print(updated_info_file)

# Приклад додавання папки
updated_info_dir = update_directory_info(directory_info, '../lessons-3-10/new_directory')
print("\nПісля додавання папки:")
print(updated_info_dir)


import os

def update_directory_info(directory_info, name):
    full_path = os.path.abspath(name)

    if os.path.isfile(full_path):
        directory_info['file_names'].append(name)
    elif os.path.isdir(full_path):
        directory_info['dir_names'].append(name)

    return directory_info

# Приклад використання
directory_info = {'file_names': ['.gitignore', 'homework_10.py', 'HOMEWORK_11.py',
'homework_11_a.py', 'homework_11_basic.py', 'homework_3.1.py', 'homework_3.py', 'homework_4.py', 'homework_5.py', 'homework_5_1.py', 'homework_6.py', 'homework_6_1.py', 'homework_7.py', 'homework_8.py', 'homework_9.py', 'hom_1_1.py', 'hom_1_2.py', 'hom_1_3.py', 'lessons_10.py', 'lessons_11.py', 'lessons_11_2.py', 'lessons_6.py', 'lessons_7.py', 'lessons_7_1.py', 'lessons_8.py', 'lessons_9.py', 'lessons_9_1.py', 'lesson_1.py', 'lesson_2.py',
'lesson_3.py', 'lesson_4.py', 'lesson_5.py', 'README.md', 'test_file.py', 'test_G.py'],
                  'dir_names': ['.git', 'utills', '__pycache__']}

# Оновлюємо інформацію про директорію додавши новий файл
updated_info_file = update_directory_info(directory_info, 'new_file.txt')
print("Оновлена інформація (додавши файл):", updated_info_file)

# Оновлюємо інформацію про директорію додавши нову папку
updated_info_dir = update_directory_info(updated_info_file, 'new_directory')
print("Оновлена інформація (додавши папку):", updated_info_dir)


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
        directory_info['file_names'].append(item_name)
    elif os.path.isdir(full_path):
        directory_info['dir_names'].append(item_name)

    return directory_info

# Приклад використання
my_directory_path = '../lessons-3-10'
directory_info = names_of_directories(my_directory_path)
print("До оновлення:")
print(directory_info)

# Оновлюємо інформацію про директорію додавши новий файл
updated_info_file = update_directory_info(directory_info, 'new_file.txt')
print("\nПісля додавання файлу:")
print(updated_info_file)

# Оновлюємо інформацію про директорію додавши нову папку
updated_info_dir = update_directory_info(updated_info_file, 'new_directory')
print("\nПісля додавання папки:")
print(updated_info_dir)
