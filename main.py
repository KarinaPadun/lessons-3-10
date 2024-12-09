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
c.execute("SELECT title FROM articles")
# print(c.fetchall()) СПИСОК
# print(c.fetchmany(2))  # только опеределенное количество записей . СПИСОК
# print(c.fetchone()[index]) только первую запись , кортеж

db.commit()

db.close()
