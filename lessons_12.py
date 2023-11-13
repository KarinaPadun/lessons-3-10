# json
# csv(reader, delimiter, writer writerows)
# DictReader DictWriter writerows, writeheader
# assert raise

###########JSON############

# import json
#
# filename = "utils/test.json"
#
#
# def read_json(file):
#     with open(file, 'r') as f:
#         data = json.load(f)
#     return data
#
#
# def write_json(file, data):
#     with open(file, 'w') as f:
#         json.dump(data, f)
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
# def some_def(request):
#     some_data = json.loads(request)
#     return some_data
#
#
# send_data = [1, 2, 3]
#
#
# def return_some_data(obj):
#     some_data = json.dumps(obj)
#     return some_data
#
# data = return_some_data(send_data)
# print(data, type(data))
# # print(read_json(filename))


########## CSV (comma separated values) ##########

# import csv
#
# filename = "utils/Workbook1.csv"
#
#
# def read_csv_file(name):
#     data = []
#     with open(name, 'r') as f:
#         reader = csv.reader(f, delimiter=";")
#         for row in reader:
#             data.append(row)
#     return data


# def write_csv_file(name, data):
#     with open(name, 'w') as f:
#         writer = csv.writer(f, delimiter=";")
#         # writer.writerow()
#         writer.writerows(data)
#
# data = read_csv_file(filename)
# header = data.pop(0)
# header.append("Sum")
#
# for row in data:
#     row.append(float(row[1]) * float(row[2]))
#
#
# data = [header] + data
# print(data)
#
# write_csv_file("utils/Workbook2.csv", data)


# def read_csv_file_dict(name):
#     data = []
#     with open(name, 'r') as f:
#
#         reader = csv.DictReader(f, delimiter=";")
#         for row in reader:
#             data.append(row)
#     return data
#
#
# def write_csv_file_dict(name, data):
#     with open(name, 'w') as f:
#         fieldnames = ["Price", "Month", "SoldItems", "Sum"]
#         # writer = csv.DictWriter(f, fieldnames=data[0].keys()) #delimiter=";",
#         writer = csv.DictWriter(f, fieldnames=fieldnames)
#         writer.writeheader()
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


# NumPy, Pandas


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