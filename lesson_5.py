# debage
# for (range, enumerate)
# str methods (i)
# salpha ,rfind ,replase , startwith
##########################################

# debage - можна поставити точки, є своя консоль , показує як відпрацьовує код по строчкам чи повність
# step over - від точки до точки
# step into - буде чіпляти всі функції (вбудовані і не вбудовані) , які були викликані
# step into my code - лише по стрічках на які натиснемо


############## for (range, enumerate)################
value_str = 'Hello'
index = 0
# while index < len(value_str):
# print(value_str[index])
# index += 1

#["H", "e", "l"] (next) автоматично продовжує і закінчуємо
for letter in value_str:
    #print(letter)
    print(value_str.index(letter))
    #print(value_str.find(letter)) - те саме буде видавати

# там де можна використати while, скоріш за все і for
# там де можна використати for , 100% можна і while
# for не потребує умови , працює з індексованими об'єктами

#range(10)  # повертає об'єкт , видача від 0 до 10(виключно)
# range(5, 10)  # від 5 до 9 включно
# range(5, 10, 2)  # від 5 до 9 включно , кожний вдругий символ

#початок кінецькрок
for index in value_str:
    #print(letter)
    print(index)

for index in range(len(value_str)):
    print(index)

for index in range(len(value_str)):
    print(index, value_str[index]) # індекс , що лежить в цьому індексі

################## enumerate #############

for index, letter in enumerate(value_str):
    print(index, letter)


for value in enumerate(value_str):
    print(value) # кортеж
    # print(value [0], value[1]) #розкладає без дужок


for i in range(10): # k j виключення скороченних назв
    print(i)


#########################################################
value_str = 'hello1234'

for letter in value_str:
    if letter.isalpha(): # лише літера
         print(letter)

# value_str.startswith("h")  # якщо починається з якогось значення

# мalue_srt ="IMG.jpg"
# value_str.endswith(".jpg")   закінчується на значення

# value_srt ="103764_IMG.jpg"
# value_str.replace()   заменить

# будь який метод створює копію!!! не змінює основний
value_str = value_str.replace('hello','test')
print(value_str)

# метод - функція
# функція виконується до будь яких об'єктів , метод підв'язується під клас
#функція видозмінює обєкт , метод робить копію


value_str= 'Hello'
for letter in value_str:
    if letter.lower() in 'eyoiau':
        print(letter)


    if letter.lower() in 'eyoiau' and letter.isalpha() and not letter.isspace(): #  перевірити чи виключать ці умови
# перша умова має відсіяти найбільше варіантів
