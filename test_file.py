class DateMod:
    def __init__(self, filename):
        self.filename = filename
        self.date_list = self.process_authors_file()

    def process_authors_file(self):
        date_list = []

        month_mapping = {
            "January": "01", "February": "02", "March": "03", "April": "04", "May": "05",
            "June": "06", "July": "07", "August": "08", "September": "09", "October": "10",
            "November": "11", "December": "12"
        }

        with open(self.filename, 'r') as file:
            current_month = ""
            for line in file:
                line = line.strip()
                if not line:
                    continue
                if line.isalpha():
                    current_month = line
                elif current_month:
                    parts = line.split('-')
                    if len(parts) >= 2:
                        date_original = parts[0].strip()
                        date_modified = date_original.replace('st', '').replace('nd', '').replace('rd', '').replace(
                            'th', '')
                        month_number = month_mapping.get(current_month, "00")
                        date_modified = date_modified.replace(current_month, month_number)
                        date_list.append({"date_original": date_original, "date_modified": date_modified})

        return date_list

    def print_mod_dates(self):
        if self.date_list:
            print(self.date_list)
        else:
            print("Список порожній.")


if __name__ == '__main__':
    result = DateMod("hom_1_3.py")
    result.print_mod_dates()
