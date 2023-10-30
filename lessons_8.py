# розпаковка tuple та list
# змінна "_"
# поняття dict
# основні методи dict(update(), get(), pop(), keys(), values(), items())

# value_1 = 1
# value_2 = 2
#
# value_1, value_2 = value_2, value_1


# value_list = (1, 2, 3, 4, 6, 7, 8)

# value_1, value_2, value_3 = value_list[:3]

# value_1, value_2, value_3, _ = value_list

# _ когда ставят , значит данние больше не будут использовать, зустрічається у фор
# tmp - тимчасова змінна
#  *tmp -если не знаем какое количество прилетит , перекладає у лист

# print(_)
# print(value_1, value_2, value_3, tmp)
# print(value_list)
# print(*value_list) - лист без скобок, розпаковка

# request_list = ["", "", ""]


# if len(request_list) > 3:
#     value_1, value_2, value_3, *tmp = request_list
# else:
#     value_1, value_2, value_3 = request_list

# value_1, value_2, value_3, *tmp = value_list
# for _ in range(10):
#     print("hello")

########### dict словники  {} , швидше відпрацьовують
# немає індексу, є ключ- значення, ключ має бути унікальним

# value_list = [1, 2, 3, 4, 5]
# value_list[2]

# value_dict = dict()

# hash table for dict
#
# value_dict = {
#     "key": "value",
#     "key1": "value",
#     "key2": "value",
#     1: 3,
#     тип данних ключа - незмінна
#     # (1,2, [1,2]): 3, кортежі
#     (1, 2): 3, інти , стрінга
#     1.2: 3, дробі флоат
#     True: 3,
#     None: 3,
# }
# ключі не змінні на всю глибину

#
# address = {
#     "country": "Ukraine",
#     "city": "Kyiv",
# }
#
# person = {
#     "first_name": "Nick",
#     "last_name": "Kozlan",
#     "password": "111111",
#     "email": "email@gmail.com",
#     "address": address
# }
# print(person["first_name"]) - видает значение ключа first_name , Nick
# print(person["address"]["city"])
# print(person) - друкує в однаковому порядку, ключ- значення. Словник не ідексований, не зберігає порядок

# print(person["address"]["city"]) - видає Київ


# person_2 = {
#     "first_name": "Nick",
#     "last_name": "Kozlan",
#     "password": "111111",
#     "email": "email@gmail.com",
#     "address": address
# }
#
# our_group = [person, person_2] - лістом або талпл

# value_str = "1234"
# for value in enumerate(value_str): enumerate - видает индекс и символ
#     print(value)


# for key in person_2:   - видает ключи
#     print(key, person_2[key]) - видает ключ + значение
#
# for key in person_2.items():
#     print(key[0], key[1])
#
# for key, value in person_2.items():
#     print(key, value)

# .items() -схоже на enumerate дает кортеж , ключ значення

# print(person_2.keys()) - видает ключи , через дикт, но не листом
# print(person_2.values()) - видает  данние без ключей

# если есть сору - то скорее всего змінний тип данних

# person_3 = dict()
# person_3["first_name"] = "Bogdan"
# person_3["last_name"] = "Count"
# person_3["email"] = "Count@"
# # print(person_3)
# print(person_3.keys())

# .get ()допомагає витягти якісь данні зі словника при цьому перевіряє чи є там щось
# email_3 = person_3.get("email", False або None )  - ключ та дефолтне значення
# print(email_3)


# if "email" not in person_3:
#     print("Email is a nessesary field")

# email_3 = person_3["email"]


# email_3 = person_3.get('email', False)
