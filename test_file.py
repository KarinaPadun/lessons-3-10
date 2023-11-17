class DomainList:
    def __init__(self, file_name):
        self.file_name = file_name
        self.domain_list = self.load_domains()

    def load_domains(self):
        domain_list = []
        try:
            with open(self.file_name, 'r') as my_file:
                for line in my_file:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        domain_list.append(line.split('.')[-1])

        except FileNotFoundError:
            print(f"Файл '{self.file_name}' не знайдено")

        return domain_list

    def create_name_list(self):
        if self.domain_list:
            name_list = [name for name in self.domain_list]
            return name_list
        else:
            print("Список порожній.")
            return []

    def print_domains(self):
        if self.domain_list:
            print(self.domain_list)
        else:
            print("Список порожній.")


filename = 'hom_1_1.py'
domain_instance = DomainList(filename)
name_list = domain_instance.create_name_list()
print(name_list)