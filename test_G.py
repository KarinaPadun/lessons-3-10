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

def update_directory_info(directory_info, name):
    if os.path.isfile(name):
        directory_info['file_names'].append(name)
    elif os.path.isdir(name):
        directory_info['dir_names'].append(name)

    return directory_info

# Приклад використання
my_directory_path = '../lessons-3-10'
result = names_of_directories(my_directory_path)
print(result)

# Припустимо, у нас є словник, який ми хочемо оновити
directory_info = {'file_names': ['file1.txt'], 'dir_names': ['subdir1']}

# Додамо ім'я файлу до словника
updated_info = update_directory_info(directory_info, 'file2.txt')

# Додамо ім'я папки до словника
updated_info = update_directory_info(updated_info, 'subdir2')

print(updated_info)
