class LastName:
    def __init__(self, filename):
        self.filename = filename
        self.last_names = self.read_last_names()

    def read_last_names(self):
        last_names = []

        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    data = line.strip().split('\t')
                    if len(data) > 1:
                        last_name = data[1]
                        last_names.append(last_name)
        except FileNotFoundError:
            print(f"Файл з прізвищами не знайдено.")

        return last_names

    def print_last_names(self):
        if self.last_names:
            print(self.last_names)
        else:
            print("Список порожній.")


# Перевірка, чи код викликається як скрипт, а не імпортується
if __name__ == '__main__':
    # Створення об'єкта класу LastName
    result = LastName('hom_1_2.py')
    # Виклик методу для виведення списку прізвищ
    result.print_last_names()
