# ОПП - все является обьектом

# Клас
# Екземпляр класу     self
# Атрибут класу
# Атрибут екземпляру класса

# class Person: - назва верблюдом (камел кейс), функція - дієслово , змінні - іменники
#     name: str = "Jack"      # Атрибут класу - характеристка классу , за замовчанням
#     age: int = 18
#
#
# person_1 = Person()         # Екземпляр класу - копія яка відноситься до классу, буде мати всі властивості классу
# # print(person_1.age)
# person_1.gender = "female"           # Атрибут екземпляру класса
# # print(person_1.age)
#
# person_2 = Person()         # Екземпляр класу
# person_2.name = "Nick"
# person_2.gender = "male"        # Атрибут екземпляру класса
# print(person_2.gender)
# print(person_1.gender)

# class Person:
#     # def __new__(cls, *args, **kwargs): створює класс - краще не видозмінювати  , селф не існує на момент створення
#     #     pass
#    def __init__(self, name, age, gender):                 #один з двох методів ініціалізації(створення екземпляру)
#
# __init__ - створити , запустити якийсь метод.Відпоідає за створення екземплярів, краще видозмінювати
# та не переписувати

#         # self.first_name = name.split()[0] - додати лише перше (імя)
#         # self.last_name = name.split()[1] - додати лише друге (призвіще)
#         self.name = name - кладемо данні
#         self.age = age
#         self.gender = gender
#
#     def __str__(self):                       # магічний метод представлення в консоль(у вигляді строки)
#     self - сутність. екземпляр классу з яким ми зараз працюєм
#         return f"I'm {self.name}, I'm {self.age} years old" - витягуємо данні , лише видача
#
#     # def __repr__(self):                                       # магічний метод який презентує екземпляр класу
#     #     return self.name
#
#     def make_name_upper(self):
#         self.name = self.name.upper()
# NEW - створює класс - краще не видозмінювати
# init - ініціалізує
#
# person_1 = Person("Nick", 24, "male")         # Екземпляр класу
# person_2 = Person("Anna", 29, "female")         # Екземпляр класу
# print(person_1.name)
# print(person_2.name)
#
# person_1.make_name_upper()
#
# print(person_1.name)
# print(person_2.name)

# print(person_1.last_name)
# print(person_1.age)
# print(person_1.gender)
# print(person_1)
# print(person_2)
# persons_list = [person_1, person_2]
# print(persons_list)


# some_str = "hello"
# print(some_str, type(some_str))
# some_str.upper()

###### lambda ####### - анонімна функція в пайтоні, видати можна лише 1 раз, не можна викликати

# def get_rectangle_square(side_1, side_2):
#     result = side_1 * side_2
#     return result
#
# a = get_rectangle_square(2,4) - буде лежати результат функції
# a = (lambda side_1, side_2: side_1 * side_2)(2,4) - буде лежати результат функції
#
# print(get_rectangle_square(2,4))
#
# print((lambda side_1, side_2: side_1 * side_2)(2,4))

#################################### Наслідування ##########################################

# class ClassMaker
class Animal:  # класи пишуться в однині

    # def __init__(self, name):
    #     self.name = name
    #
    def feed_animals(self):
        return "mealAnimal"


class Zoo:
    def feed_animals(self):
        return "mealZoo"


class Tiger(Animal, Zoo):           # MRO-2 треба якийсь метод, шукаемо не тільки на 1 рівні , а заходимо вглиб,
    # копає весь класс вглиб
    # MRO-3 - більш ефективний, він буде шукати по шарах(рівнях), з 1 на 2 рівень економить память
    # технологія наслідування класів
    """hhhh"""
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Cat(Tiger, Zoo):
    """hhhh"""

tiger_1 = Tiger("Jack", "red")
# tiger_1 = Tiger("Jack")

print(tiger_1.name)
print(tiger_1.feed_animals())