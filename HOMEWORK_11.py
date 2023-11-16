from test_G import names_of_directories, sort_directory_info, updated_dictionary

# Здесь вы можете использовать эти функции по мере необходимости
my_directory_path = '../lessons-3-10'

result = names_of_directories(my_directory_path)
print(result)

directory_info = names_of_directories(my_directory_path)
sorted_info_ascending = sort_directory_info(directory_info)
print("Alphabetically order:")
print(sorted_info_ascending)

new_dir = 'A'
new_file = 'text.3552.txt'
directory_info = names_of_directories(my_directory_path)
updated_info_file = updated_dictionary(directory_info, new_file)
print(updated_info_file)

updated_info_dir = updated_dictionary(updated_info_file, new_dir)
print(updated_info_dir)
