# json
# csv(reader, delimiter, writer writerows)
# DictReader DictWriter writerows, writeheader
# assert raise

###########JSON############ - тип (формат) данних який допомогає взаємодіяти з фронтою ( від сервісу до сервісу)
# нагадує список словників


# import json
#
# filename = "utils/test.json" - числа будут интой , в конце нет запятой , двойние лапки
#
#
# def read_json(file):
#     with open(file, 'r') as f:
#         data = json.load(f) - вигрузить
#     return data
#
#
# def write_json(file, data):
#     with open(file, 'w') as f:
#         json.dump(data, f) - запакувати
#
#
# req = '''
#     [
#   {
#   "key": 1,
#   "key1": 2,
#   "key2": "value",
#   "key3": "value"
#   },
#   {
#   "key": "value",
#   "key1": "value",
#   "key2": "value",
#   "key3": "value"
#   }
# ]
# '''
#
#
# def some_def(request): - прилітає сира строка
#     some_data = json.loads(request) s - як стрінг
#     return some_data

# loads,dumps -для роботи с сиримі данними
#
# send_data = [1, 2, 3]
#
#
# def return_some_data(obj): - обектом може бути все що завгодно  (відправити на фронту)
#     some_data = json.dumps(obj)
#     return some_data
#
# data = return_some_data(send_data)
# print(data, type(data))
# # print(read_json(filename))


########## CSV (comma separated values) ########## - таблица (данние разделенние сепаратором -запятой или другой)

# import csv - пакет треба імпортувати
#
# filename = "utils/Workbook1.csv"
#
#
# def read_csv_file(name):
#     data = []
#     with open(name, 'r') as f:
#         reader = csv.reader(f, delimiter=";") щоб прочитати трбеа створити обєкт
#         delimiter- розділювальний символ
#         for row in reader:
#             data.append(row) - добавить строчки
#     return data прочитать по строчке ( видает лист в котором два листа)
#
#     ВИТЯГИВАЕТ ВСЕ ВСЕГДА СТРИНГОЙ!!


# def write_csv_file(name, data): - імя і те що записати
#     with open(name, 'w') as f:
#         writer = csv.writer(f, delimiter=";")
#         # writer.writerow() - декілька рядків
#         writer.writerows(data) -додае весь обект
#
# data = read_csv_file(filename)
# header = data.pop(0)
# header.append("Sum") - додаемо колонку сумма
#
# for row in data:    row- рядок (стала назва)
#     row.append(float(row[1]) * float(row[2])) - треба зробити інт,флоат щоб працювало
#
#ЕКСЕЛЬ - завжди ставить крапку з комою
# data = [header] + data
# print(data)
#
# write_csv_file("utils/Workbook2.csv", data) - записати новий файл в папку ютілс Воркбук2


# def read_csv_file_dict(name):
#     data = []
#     with open(name, 'r') as f:
#
#         reader = csv.DictReader(f, delimiter=";") - викликати дікт рідер  , отримаємо словники
#         for row in reader:
#             data.append(row)
#     return data
#
# НАБАГАТО ВАЖЧЕ ДЛЯ СИСТЕМИ
# def write_csv_file_dict(name, data):
#     with open(name, 'w') as f:
#         fieldnames = ["Price", "Month", "SoldItems", "Sum"] - послідовність
#         # writer = csv.DictWriter(f, fieldnames=data[0].keys()) #delimiter=";",
#         fieldnames - ПОСЛІДОВНІСТЬ
#         writer = csv.DictWriter(f, fieldnames=fieldnames)
#         writer.writeheader() - записує
#         writer.writerows(data)
#
#
# data = read_csv_file_dict(filename)
# print(data)
#
# for row in data:
#     row['Sum'] = float(row['Price']) * float(row['SoldItems'])
#
# print(data)
#
# write_csv_file_dict("utils/Workbook2.csv", data)


# NumPy, Pandas - бібліотеки Pandas -коли розрахунки (Дата аналітик)


########## assert raise


# def discount_price(price, discount):
#     res = price - discount
#     if res < 0:
#         raise Exception("Type some text for error raise raise")
#     return res
#
#
# result = discount_price(100, 999)
# print(result)
#
# assert result > 0, "Type some text for error"
#
# print("ok")

####################### ООП ###############

# class

# class Person:    # клас
#     name = None   # атрибут класу
#     age = 0
#
#
# person_1 = Person()      # екзампляр класу
#
# person_1.name = "Nick"
# # person_1.age = 24  # атрибут екзампляру класу
#
# print(person_1.name)
# print(person_1.age)