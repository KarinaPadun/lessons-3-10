#CLI(command line interface)

# from argparse import ArgumentParser
#
# args = ArgumentParser()
#
#
# args.add_argument("name", type=str)
# args.add_argument("age", nargs="?", type=int, default=0)
# args.add_argument("--job", nargs="?", type=str, default='qa')
#
# args = vars(args.parse_args())
#
# print(args)
# print(args['name'])



# наслідування
# інкапсуляція

# декоратори  @property, @staticmethod

############# Наслідування #################
#
# class Transport:
#
#     def __init__(self, color):
#         self.color = color
#
#     def __str__(self):
#         return "The transport is"
#
#     # def __repr__(self):
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
#         super().__init__(color)
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


########## інкапсуляція ############

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
# print(mercedes._Transport__get_fuel())
# # mercedes.get_fuel()


############ декоратори ############


# декоратори  @property, @staticmethod


# def can_do():
#     return "I can move"


# class Transport:
#
#     def __init__(self, color):
#         self.color = color
#         # self.fuel = self._get_fuel()
#         # self.fuel = self.get_fuel()
#
#     @property
#     def fuel(self):
#         return "OIL"
#
#     def __str__(self):
#         return "The transport is"
#
#     @staticmethod
#     def can_do():
#         return "I can move"
#
# mercedes = Transport("white")
# print(mercedes.fuel)
# # print(mercedes.fuel)




# модуль requests

import requests


response = requests.get('https://www.google.com')
print(response.status_code)
print(response.content)





# API