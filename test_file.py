def unique_characters(str1, str2):
    unique_chars = []

    for char in str1:
        if char in str2 and str1.count(char) == 1 and str2.count(char) == 1 and char not in unique_chars:
            unique_chars.append(char)

    for char in str2:
        if char in str1 and str2.count(char) == 1 and str1.count(char) == 1 and char not in unique_chars:
            unique_chars.append(char)

    return unique_chars


string_1 = 'Helloy'
string_2 = 'Goodbye'
result = unique_characters(string_1, string_2)
print(result)


