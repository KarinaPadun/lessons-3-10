class Date:
    def __init__(self, filename):
        self.filename = filename
        self.date_list = self.dates_from_file()

    def dates_from_file(self):
        date_list = []

        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    line = line.strip()
                    if any(month in line for month in ["January", "February", "March",
                                               "April", "May", "June",
                                               "July", "August", "September",
                                               "October", "November", "December"]):
                        date_parts = line.split('-')
                        if date_parts:
                            date_list.append({"date": date_parts[0].strip()})
        except FileNotFoundError:
            print(f"Файл не знайдено")

        return date_list

    def print_dates(self):
        if self.date_list:
            print(self.date_list)
        else:
            print("Список порожній.")


if __name__ == '__main__':
    result = Date("hom_1_3.py")
    result.print_dates()
