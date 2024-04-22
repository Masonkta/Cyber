def convert_string(input_string):
    output_string = ""
    for char in input_string:
        if char == 'O':
            output_string += '0'
        elif char == 'l':
            output_string += '1'
        else:
            output_string += char
    return output_string

def binary_to_english(binary_string):
    binary_values = binary_string.split()
    ascii_string = ""
    for binary_value in binary_values:
        decimal_value = int(binary_value, 2)
        ascii_character = chr(decimal_value)
        ascii_string += ascii_character
    return ascii_string


input_string = """OlOlOOOl OOllOOlO OlOOOllO OlllOlOl OlOOlOlO OOllOOll
OlOlOOOl OllOOlll OlOllOlO OllOllOl OllOllOO OlllOlOl OlOllOlO OlOOOOll OlOOOOlO OllllOlO OllOOlOO OlOOlOOO OlOlOllO
OllOllOl OlOllOlO OllOlOOl OlOOOOlO OlllOllO OllOOOlO OllOlOOl OlOOOOlO OlOOOlll OlOlOllO OlOOOllO OlOOOOOl OOlOllll
OlOOlOOl OlOlOOll OlOOOOOl OlllOlOO OlOlOOOO OllOlOOl OlOOOOlO OlllOOll OllOOOll OllllOOl OlOOOOOl OlllOlOO OllOOOlO
OlOOOOOl OOllOOOO OlOOlOll OlOlOOOl OOllOOlO OlOOOllO OlllOlOl OlOOlOlO OOllOOll OlOlOOOl OllOOlll OlOllOlO OlOOOlll
OOlllOOl OOllOOll OllOOOlO OllOllOl OllllOOO OlllOllO OlOllOOl OlOlOlll OlOlOOOl OllOOlll OllOOlOO OlOOOlll OllOlOOO
OllOllOO OlOOlOOl OlOOOlll OlOllOlO OlllOOOO OllOOOlO OlOOOlll OlOlOlOl OllOOlll OllOOOlO OOllOOlO OlOllOlO OllOllOl
OlOOlOOl OlOOOlOl OlOllOlO OlOlOlOl OlOlOlOl OlOOOOll OlOOOOOl OlllOlOO OlOlOOOO OllOlOOl OlOOOOlO OllOlllO OlOllOlO
OlOllOOO OlOlOOOl OlOOlllO OlOOOOll OllOllOO OlOlOOlO OllOllll OlOllOOl OlOlOlll OOllOlOl OlllOOlO OlOOlOOl OlOOOlll
OOllOOOl OllOllOO OlOOlOOl OlOOOlll OllllOOO OllOlOOO OllOOlOO OlOOOlll OlOlOllO OllllOOl OlOOlOOl OlOlOOll OlOOOOlO
OlOOllOl OllOOOOl OlOlOlll OOllOlOl OlllOOlO OlOOlOOl OlOOlOOO OlOlOOlO OlllOllO OlOOlOOl OlOOOlll OOllOOOl OOllOlOl
OlOOlOOl OlOOOllO OlOllOlO OllOllOOOllOOOlO OllOllOl OOllOOOl OlllOllO OlOOllOO OOllOOOO OlOOlllO OllOlOOO OllOOOll
OOllOOlO OllOlOOO OlOOOOlO OllOOOll OlOOlOOO OlOOOOOl OOllOllO OlOOlOOl OlOOOlOl OlOOOOlO OllOlllO OllOOOOl OlOllOOO
OlOllOlO OllOllOO OllOOOlO OlOlOlll OlOlOllO OlllOlOO OllOOOlO OOllOOlO OOllOlOl OllOllOO OllOOlOl OlOlOOOl OOllllOl OOllllOl"""
converted_string = convert_string(input_string)
english_string = binary_to_english(converted_string)
print(english_string)
