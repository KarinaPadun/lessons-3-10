# 3 stages of programming (створити програму яка працює, оптимізація , переклад частин на іншу мову, щоб працювало швидше)

# if statement not
# ternary operator
# while (True, flag, value)
# break, continue
# while else
# str methods

# value = "ffff"

# if (value == "+") or (value == "-"):
#     print("!!!!!")
# else:
#     print("????")



########### if statement not  ############

# if not value: - value is not True
#     print("ssss")

#value = 10

# if (value % 2) == 0 and (value % 5) == 0:
#     print(value)
# if not (value % 2) and not (value % 5) aбо if not (value % 2 and value % 5):


#logged = True
#
# if not logged: (сценарій що більше- на початок)
#     print("Please logged in")
# else:
#     print("Welcome")


############# ternary operator ############


# a = 2
# b = 330
#
# # print("A") if a > b else print("B")
#
# result = True if a > b else False
#
# print(result)

############# while (True, flag, value) ############ while - поки ,  loop- цикл, петля, бульбашка

#value = 1
# is_true = True


# while True:
#     value += 1 # те саме що value = value + 1 (синтаксичний цукор, спрощення  )
#     print(value)
#     if value > 10:
#         break

# while з Умовою
# while value < 10:
#     value += 1  # value = value + 1
#     if value % 2:
#         continue
#
#     print(value)

# while за прапором
# while is_true:
#     value += 1  # value = value + 1
#     print(value)
#
#     if value > 10:
#         is_true = False


############### break- прекратить , стоп , continue - продовжити
# condition_1 = True
# condition_2 = False
# condition_3 = False
#
# while condition_1:
#     print("1111")

# while value < 10:
#     value += 1  # value = value + 1
#     if value % 2:
#         continue - зупиняє цикл всередині циклу
#
#     print(value)