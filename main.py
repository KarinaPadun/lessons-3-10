import sqlite3

db = sqlite3.connect('test.db')

# create cursor
c = db.cursor()

# создание таблицы
# c.execute("""CREATE TABLE articles (
#    title text,
#    full_text text,
#    views intenger,
#    author text
# ) """)

# добавление данных
# c.execute("INSERT INTO articles VALUES('facebook','facebooktest','3','admin2')")

# выборка данных, * - все
# rowid  -  уникальный номер
c.execute("SELECT rowid, * FROM articles WHERE rowid < 2 ORDER BY rowid DESC")
items = c.fetchall()
# print(c.fetchall()) СПИСОК
# print(c.fetchmany(2))  # только опеределенное количество записей . СПИСОК
# print(c.fetchone()[index]) только первую запись , кортеж
# <> - не равен, DESC - по спаданию

# удаление
# c.execute("DELETE FROM articles WHERE rowid = '1' ")

c.execute("UPDATE articles SET author= 'admin' WHERE")

for item in items:
    print(item[1] + "\n" + item[4])

db.commit()

db.close()
