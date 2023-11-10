import os

def names_of_directories(directory_path) -> dict:
    if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
        return {"filenames": [], "dirnames": []} # якщо нічого не знайде файли  , то буде пустий словник повертатии


    items = os.listdir(directory_path)


    filenames = [item for item in items if os.path.isfile(os.path.join(directory_path, item))]
    dirnames = [item for item in items if os.path.isdir(os.path.join(directory_path, item))]

    return {"filenames": filenames, "dirnames": dirnames}



directory_path = '../lessons-3-10'
result = names_of_directories(directory_path)
print(result)


