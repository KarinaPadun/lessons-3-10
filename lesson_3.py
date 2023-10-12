# Bool , None types
# Logic operator
# зведення типів
# Duck typing
# If statement ( programing golf . Тернарний оператор)
# Input ()
# working with errors

######### None types #########

value_none = None

value_int = 123

print(value_int)

value_id = id(value_int)

value_print = print(value_int)

print(value_print, type(value_print))

#print(value_id, type(value_id))

########## Bool##########

value_bool_1 = True
value_bool_2 =  False

result = 1 > 2 # > , < , == , != (не дорівнює), >= <=

result_str =  "lo" in "hello" # містить - in

print(result_str)


########### Type ##############

value_int = 2
value_str = "2.3"

# f " {} {}"

result = value_int + float(value_str)

print(result)


################# If statement  ####################

# if (якщо) умова
# зроби це

weather = "hot"
if weather == "cold":
    print("It's cold")
else:
    print("It's not cold")


value_int = 20
# and or

#if value_int > 0 and value_int < 10:
#if 0 < value_int < 10: #спрощенний запис
   # print(f"{value_int} is bigger then 10")
#elif value_int > 0: #else if
    #print(f"{value_int} is bigger then 0")
#else:
 #   print(f"{value_int} is less then 0")



############# input() ##################### завжди строка ! (10+10=1010)
# звіт данних

value_1 = int(input("Please type a number:"))
value_2 =  int(input("Please type another number: "))
# або звести в результаті!

result= int(value_1) + int(value_2)

print(result)