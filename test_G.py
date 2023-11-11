import os


def names_of_directories(my_directory_path) -> dict:
    if not os.path.exists(my_directory_path) or not os.path.isdir(my_directory_path):
        return {"dir_path": my_directory_path, "file_names": [], "dir_names": []}

    items = os.listdir(my_directory_path)

    file_names = [i for i in items if os.path.isfile(os.path.join(my_directory_path, i))]
    dir_names = [i for i in items if os.path.isdir(os.path.join(my_directory_path, i))]

    return {"dir_path": my_directory_path, "file_names": file_names, "dir_names": dir_names}


def sort_directory_info(directory_info, alphabetically=True):
    sorted_info = {
        'file_names': sorted(directory_info['file_names'], reverse=not alphabetically),
        'dir_names': sorted(directory_info['dir_names'], reverse=not alphabetically)
    }
    return sorted_info


def updated_dictionary(directory_info, item_name):
    full_path = os.path.abspath(os.path.join(directory_info['dir_path'], item_name))

    if os.path.isfile(full_path):
        if item_name not in directory_info['file_names']:
            directory_info['file_names'].append(item_name)
    elif os.path.isdir(full_path):
        if item_name not in directory_info['dir_names']:
            directory_info['dir_names'].append(item_name)
    else:
        if '.' in item_name:
            with open(full_path, 'w'):
                pass
            directory_info['file_names'].append(item_name)
        else:
            new_dir_path = os.path.join(directory_info['dir_path'], item_name)
            os.makedirs(new_dir_path)
            directory_info['dir_names'].append(item_name)

    return directory_info


my_directory_path = '../lessons-3-10'


result = names_of_directories(my_directory_path)
print(result)


directory_info = names_of_directories(my_directory_path)
sorted_info_ascending = sort_directory_info(directory_info)
print("Alphabetically order:")
print(sorted_info_ascending)


new_dir = 'A'
new_file = 'text.3552.txt'
directory_info = names_of_directories(my_directory_path)
updated_info_file = updated_dictionary(directory_info, new_file)
print(updated_info_file)

updated_info_dir = updated_dictionary(updated_info_file, new_dir)
print(updated_info_dir)
