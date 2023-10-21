# порівняння list та tuple
# змінні не змінні типи даних різниця
# методи строк(split(), rsplit(), join())
# методи list(append(), pop(), sort(), copy())
# функція sorted()

# list = () - cписки , масиви
# tuple = () - кортеж, є незмінний , зустрічаються в бібліотеках та константах {} - tuple
# () - функції , мат дії

value_list = [1 , 1.1 , '&',None , True , [1]]
value_tuple = (1 , 1.1 , '&',None , True , [1])


value = 1
value = 5 #  переподв'язывается
#####################################################
value_list = ["hello"]
value_tuple = ("hello" , ) # typle  поставити перед якщо один обєкт


print(type(value_list ) )
print(type(value_tuple))


value_list = [
    1 ,
    1.1 ,
    '&',
    None ,
    True ,
]
   #]
value_tuple = (
    "hello" ,
)
#####################################################
base_list = [1, 2, 3]
new_list = [base_list.copy()] * 4 # copy() робить копію і не змінює лист
print(new_list)
#####################################################
base_list = [1, 2, 3]
my_new_list = base_list * 4 #працює з даними
print(my_new_list)
base_list[0] = 10
print(f"base_list {base_list}")
print(f"my_new_list {my_new_list}")

#####################################################
base_list = [1, 2, 3]
my_new_list = [base_list] * 4 #працює зі списком
print(my_new_list)
base_list[0] = 10
print(f"base_list {base_list}")
print(f"my_new_list {my_new_list}")

# в змінних value зберігається посилання
# листи можна доповнювати
#####################################################
base_list = [1, 2, 3]
base_list.append('hello') # працює з лістом Функция append() позволяет добавлять в список один новый элемент
print(base_list)

value = ("Hello")
value= value.lower() #  працює з копією
print(value)

#видаляє всі елементи clear()	Removes all the elements from the list

base_list.pop(1)
#видаляє останній обєкт якщо дужки пусті або індекс того що в дужках
deleted_val =base_list.pop(1)
print(deleted_val) #видає видаленний обєкт

websites = [
    "www.site1.com"
    "www.site2.com"
    "www.site3.com"
    "www.site4.com"
    "www.site5.com"
    "www.site6.com"
]

while len(websites) != 0 :
    deleted_val = websites.pop()
    print(deleted_val)

# while websites більш коротка умова



# методи строк split(), rsplit() , join()
#
value = ('c/desktop/doc/file/img.jpg')

# print(value.split('/', 2), type(value.split()))  #формує список
# print(value.rsplit('.', 1), type(value.rsplit()))  # ріже з кінця

val_list = value.rsplit(".", 1)
val_list[1] = 'png'
print(val_list)

# join обєднання
final_str = "\\".join(val_list)
print(final_str)


###########sort

base_list = [1, -4, 10, 2, 3]
print(base_list)
# base_list.sort() изменяет лист
base_list.sort(reverse = True) #в обратную
print(base_list)

# sorted() робить те саме, создает копию

base_list = ['amd', 'bmd','aamd', 'rrr', 'att'] # за алфавітом

print(sorted(base_list, reverse= False, key=len)) # за довжиною

# key=аbс - за модулем
# спочатку цифри , потім спецсимволи і букви

############### ASCII - міжнародний стандарт розмітки
print(ord('4')) # порядок - ord
# за кожним символом закріплений порядковий номер

print(chr(2)) #який символ за номером

#Len Python Возвращает количество символов в текстовой строке, включая пробелы.