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

range(10)  # повертає об'єкт , видача від 0 до 10(виключно)
#початоккінець крок
for index in value_str:
    #print(letter)
    print(index)
