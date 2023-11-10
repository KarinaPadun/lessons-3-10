
import os

def names_of_directories(my_directory_path, alphabetically=True) -> dict:
    if not os.path.exists(my_directory_path) or not os.path.isdir(my_directory_path):
        return {"file_names": [], "dir_names": []}

    items = os.listdir(my_directory_path)

    if alphabetically:
        file_names = sorted([i for i in items if os.path.isfile(os.path.join(my_directory_path, i))])
        dir_names = sorted([i for i in items if os.path.isdir(os.path.join(my_directory_path, i))])
    else:
        file_names = [i for i in items if os.path.isfile(os.path.join(my_directory_path, i))]
        dir_names = [i for i in items if os.path.isdir(os.path.join(my_directory_path, i))]

    return {"file_names": file_names, "dir_names": dir_names}

my_directory_path = '../lessons-3-10'
result = names_of_directories(my_directory_path)
print(result)
