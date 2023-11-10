# import for def
# __name__
# os (listdir, path.join, path.isfile, makedir, makedirs(exist_ok), remove)
# json

from utils.work_with_files import reading_text_file_readlines
import os

# data = reading_text_file_readlines("homework/lesson_4")
#
# print(data)

######### os ############## відповідає за всю роботу з файлом

# filedir = "homework"
# some_dir = ""
# filename = "lesson_4"
#
# files_list = os.listdir() видає ліст з назвами папок та файлів , якщо нічого не вказати ,
# видасть файли на одному рівні з яким працюємо. КРаще вказувати файл
# print(files_list)
# for file in files_list:
#     if os.path.isdir(file): - якщо це папка
#     # if os.path.isfile(file): - якщо це файл
#         print(file)
# #
# # data = reading_text_file_readlines("homework/lesson_4") - в залежності від системи різний слеш
# # data = reading_text_file_readlines(f"{filedir}/{some_dir}/{filename}") -
# data = reading_text_file_readlines(os.path.join(filedir, some_dir, filename)) - найкращий варіант
#
#
# print(data)


################################# JSON #########################################################
# import json
# #
# # some_json = '''
# #     {
# #         "key":"Val"
# #     }
# # '''
# some_json = '''
#     [
#         1,
#         2,
#         3
#     ]
# '''
#
# data = json.loads(some_json)
# json_data = json.dumps(data)
#
# def reading_json_readlines(file: str) -> list:
#     with open(file, 'r') as f:
#
#         data = json.load(f)
#     return data
#
#
# def writing_json_file(file: str, data: str) -> list:
#     with open(file, 'w') as f:
#         # data = f.readlines()
#         json.dump(data, f)
#     return data
#
#
# data = reading_json_readlines("utils/test.json")
# # writing_json_file("utils/test_1.json", [1, 2, 3])
#
# print(data, type(data))


# 8. Дано списки names та domains (створити самостійно). Написати функцію для генерування e-mail у форматі:
#     "ім'я . число від 100 до 999 @ стрінга з літер довжиною від 5 до 7 символів . домен"
# Прізвище та домен брати випадковим чином із заданих списків переданих у функцію у вигляді параметрів.
# Рядок і число генерувати випадковим чином.
#
# Приклад використання функції:
#
# names = ["king", "miller", "kean"]
# domains = ["net", "com", "ua"]
# e_mail = create_email(domains, names)
# print(e_mail)
#
# Відповідь: miller.249@sgdyyur.com
#
# import random
# from string import ascii_lowercase
#
#
# def list_for_rand_choice(some_list):
#     res = random.choice(some_list)
#     return res
#
#
# def create_rand_int(from_int, to_int):
#     res = random.randint(from_int, to_int)
#     return res
#
#
# def create_rand_str(ascii_lower, from_int, to_int):
#     res = "".join(random.choice(ascii_lower) for _ in range(random.randint(from_int, to_int)))
#     return res
#
#
# def create_email(domains, names):
#     # random.shuffle(names)
#     # name = names[0]
#
#     # name = random.choice(names)
#     name = list_for_rand_choice(names)
#
#     # some_num = random.randint(100, 999)
#     some_num = create_rand_int(100, 999)
#
#     some_str = create_rand_str(ascii_lowercase, 5, 7)
#     # some_str = "".join(random.choice(ascii_lowercase) for _ in range(random.randint(5, 7)))
#     # some_str = "".join("a" for _ in range(random.randint(5, 7)))
#
#     # domain = random.choice(domains)
#     domain = list_for_rand_choice(domains)
#
#     return f"{name}.{some_num}@{some_str}.{domain}"
#
#
# names = ["king", "miller", "kean"]
# domains = ["net", "com", "ua"]
# e_mail = create_email(domains, names)
# print(e_mail)

some_dict = [
    {
        "name": "Nick",
        "subject": "History",
    },
    {
        "name": "Nick2",
        "subject": "History2",
    }
]