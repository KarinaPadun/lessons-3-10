DEBUG = True
SOME_LIST = [1, 2, 3]


def reading_text_file_readlines(file: str) -> list: #readline - першу строку , readlines -весь файл построчно
    # в списке, read -весь файл
    with open(file, 'r') as f:
        data = f.readlines()
    return data


def writelines_text_file(file: str, data: list):
    with open(file, 'w') as my_file:
        my_file.writelines(data)


if __name__ == "__main__":
    data = reading_text_file_readlines("../homework/lesson_5.txt")
    print(data)