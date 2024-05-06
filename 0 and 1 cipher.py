def convert_string(input_string):
    output_string = ""
    for char in input_string:
        if char == 'o':
            output_string += '0'
        elif char == 'l':
            output_string += '1'
        else:
            output_string += char
    return output_string




input_string = """oloooollolloloooolloooololllolooooloooooollloollolloolololllooloolllollool
loolololllooloooloooooollooollolloooolollollloooloooooolloooloolloololoolo
ooooolloolloollollllolllololollollloolloolooooloooooolloooolollloloooooolo
loooloooloollollloollollooolloooloooloooooollollloollollooollooooloolooooo
olloooloolllolloolllloooolllloolollollloolloolloooloooooollloollollloollol
loolooollollllolloloooooloooooolllooololllloolollollloooloooooollollolollo
llooollololoollollllollolollolloooolollollolooloooooolloolloollloollollloo
loooloooooolllloooolllolloolloloooooloooooolllooooolloolloollollolollolooo
ollollooooloooooolllooooolloloolollollllolllloolooloooooollollllollooloooo
loooooollollololllolloolloolloolloolllooloooooolloolooolloooloollooollolll
loololloloooolloloolooloooooolllooololloolooollooollolloolllolllooloollolo
olollollllolllloloollollllolllloooolloooolooloooooolllolloolloooloollloolo
ooloooooolllooloollollllolloloooollolollolloolloollollllollooooloolooooool
loloooolloooloolllooolooloooooolllloololloloooollllooloolooolooooololoollo
loololloolloooloooooolllloolollollllolllololooloooooolllololollloollollool
olooloooooolllolooolloloooolloololooloooooollolollolloololollllooloolooooo
ooloooloolooolololllooloolloloolollooollooloooooololooooolllooloolloloolol
lollloollooollolloololoolooolooooololo
"""
converted_string = convert_string(input_string)
print(converted_string)
