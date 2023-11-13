from datetime import datetime
from string import ascii_letters


def get_lines_from_file(filename):
    with open(filename, 'r') as input_file:
        lines_list = input_file.read().splitlines()
    return lines_list


###############################################################

domains_file = 'homework/domains.txt'


def get_domain_names_from_file(filename):
    data_from_file = get_lines_from_file(filename)
    dom_list = [value.replace('.', '') for value in data_from_file]

    return dom_list


domains_list = get_domain_names_from_file(domains_file)
print(domains_list)

# ###############################################################
#
# names_file = 'homework/names.txt'
#
#
# def get_last_names_from_file(filename):
#
#     data_from_file = get_lines_from_file(filename)
#
#     ln_list = [line.split('\t')[1] for line in data_from_file if line]
#     return ln_list
#
#
# last_names_list = get_last_names_from_file(names_file)
# print(last_names_list)
#
# # ###############################################################
#

# authors_file = 'homework/authors.txt'
#
#
# def get_date_dict_from_file(filename):
#
#     data_from_file = get_lines_from_file(filename)
#
#     # new_data = [{'date': line.split(' - ')[0]} for line in data_from_file if line and '-' in line]
#
#     new_data = []
#     for line in data_from_file:
#         if line and '-' in line:
#             new_data.append({'date': line.split(' - ')[0]})
#
#     return new_data
# #
# #
# date_list = get_date_dict_from_file(authors_file)
# print(date_list)

#
# # ###############################################################
import datetime

#
# def dateination(name=authors_file):
#     with open(name, "r") as my_file:
#         data = my_file.readlines()
#         my_list = []
#         for i in list(data):
#             x = i.split(" - ")
#             if "\n" not in x[0]:
#                 f = x[0].split()
#                 f[0] = f[0].replace("1st", "1").replace("th", "").replace("2nd", "2").replace("3rd", "3")
#
#                 date = "/".join(f)
#
#                 if date.split("/")[0].isdecimal():
#
#                     fdate = datetime.strptime(date, "%d/%B/%Y") #Y - 2022,  y - 22
#                     f2date = fdate.strftime("%d/%m/%Y")
#
#                 else:
#                     fdate = datetime.strptime(date, "%B/%Y") #.strftime("%m/%Y")
#                     f2date = fdate.strftime("%m/%Y")
#                 y = {"date_original": x[0], "date_modified": f2date, }
#                 my_list.append(y)
#
#         return my_list
#
# date_list = dateination()
# print(date_list)


def get_dates_authors(file_name: str) -> list:
    with open(file_name, 'r') as my_file:
        data = my_file.readlines()
        result =[]
        list_for_replace = ["st", "nd", "rd", "th"]
        for i in data:
            my_split = i.split("-")
            if len(my_split) < 2:
                continue
            splited_date = my_split[0].strip()
            day = splited_date.split(" ")[0]
            result_str = splited_date.split(" ")[1:]

            for n in list_for_replace:
                day = day.replace(n, "")
            #     .isdigit()

            result_str.insert(0, day)

            if len(result_str) < 3:
                continue
            result_str = " ".join(result_str)

            formated_date = datetime.datetime.strptime(result_str.strip(), "%d %B %Y").date().strftime("%d/%m/%Y")
            result.append({"date_original": splited_date, "date_modified": formated_date})
        return result


print(get_dates_authors('homework/authors.txt'))