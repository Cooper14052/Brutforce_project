NUM_CHARS = 3
FIRST_CHAR = 48
LAST_CHAR = 127

def generate_nchar_passwords(n, first_char_code, last_char_code):
    for i in range(first_char_code, last_char_code):
        yield chr(i)
        if n > 1:
            for j in generate_nchar_passwords(n - 1, first_char_code, last_char_code):
                yield chr(i) + j


with open('pwlist.txt', 'w') as file:
    for line in generate_nchar_passwords(NUM_CHARS, FIRST_CHAR, LAST_CHAR):
        file.write(line + '\n')
