import os


def update_directory_info(directory_info, name):
    if os.path.isfile(name):
        directory_info['file_names'].append(name)
    elif os.path.isdir(name):
        directory_info['dir_names'].append(name)

    return directory_info

# Приклад використання
directory_info = {'file_names': ['file1.txt', 'file2.txt'], 'dir_names': ['dir1', 'dir2']}
updated_info = update_directory_info(directory_info, 'file3.txt')

print(updated_info)
