#CLI(command line interface)

# from argparse import ArgumentParser
#
# args = ArgumentParser()
#
#
# args.add_argument("name", type=str)
# args.add_argument("age", nargs="?" - не обовязковий , type=int, default=0)
# args.add_argument("--job", nargs="?", type=str, default='qa') - аргумент можуть викликати за іменем
#
# args = vars(args.parse_args())  - розперсити елементи
#
# print(args) - працює як звичайний словний
# print(args['name'])

# передавати в одному порядку

# принципи програмування
# наслідування
# інкапсуляція та полімозфізм

# декоратори  @property, @staticmethod

############# Наслідування #################
#
# class Transport: - батьківський класс на найвищому рівні
#
#     def __init__(self, color):
#         self.color = color
#
#     def __str__(self): - видает строку , на видачу клиентов
#         return "The transport is"
#
#     # def __repr__(self): - головниша , для розробныкив  (для дебагу)
#     #     return f"{self.color}"
#
#     def can_do(self):
#         return "I can move"
#
#
# class Radio():
#     pass
#
# class Car(Radio, Transport):
#
#     def __init__(self, model, color):
#         self.model = model
#         super().__init__(color) - щоб працювати з батьківським классом потрібна функція супер
#
#     def __str__(self):
#         return super().__str__() + f" a car the model is {self.model}"
#
#
#
# mercedes = Car("c-200", "white")
# # print(mercedes.model)
# # print(mercedes.color)
# print(mercedes)


########## інкапсуляція ############ - захищаемо обьект(капсула)
# два рівня захищенності: _ (перший рівень) , __ (після)

# class Transport:
#
#     def __init__(self, color):
#         self.color = color
#         # self.fuel = self._get_fuel()
#         self.fuel = self.__get_fuel()
#
#     def __str__(self):
#         return "The transport is"
#
#     def __get_fuel(self):
#         return "OIL"
#
#     def can_do(self):
#         return "I can move"
#
#
#
# mercedes = Transport("white")
# # print(mercedes.model)
# # print(mercedes.color)
# # print(mercedes.fuel)
# print(mercedes._Transport__get_fuel()) - достучатись до другого рівня захищенності
# # mercedes.get_fuel()


############ декоратори ############


# декоратори  @property, @staticmethod


# def can_do(): -не можна видозмінювати
#     return "I can move"


# class Transport:
#
#     def __init__(self, color):
#         self.color = color
#         # self.fuel = self._get_fuel()
#         # self.fuel = self.get_fuel()
#
#     @property - зробить з методу атрибут  ( пишемо НЕ через дієслово)
#     def fuel(self):
#         return "OIL"
#
#     def __str__(self):
#         return "The transport is"
#
#     @staticmethod - працює однаково не зважаючи на те що попадає сюди
#     НТМЛ- статичний, не важливо що будуть за данні, буде відбуватися те саме
#     def can_do():
#         return "I can move"
#
# mercedes = Transport("white")
# print(mercedes.fuel)
# # print(mercedes.fuel)




# модуль requests - треба встановлювати
# щоб встановити треба прописати в консолі pip install (імя бібліотеки)
# витягти інформацію з веб сторінок

import requests


response = requests.get('https://www.google.com') # get - взяти
print(response.status_code) # статус видає 200
print(response.content)


# API - 