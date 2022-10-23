import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
quantity_passwords = int(input('Сколько паролей сгенерировать? '))
len_password = int(input('Сколько знаков должно быть в пароле? '))
digit_password = input('Включать ли цифры 0123456789? yes/no ')
uppercase_alphabet = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? yes/no ')
lowercase_alphabet = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? yes/no ')
other_symbols = input('Включать ли символы !#$%&*+-=?@^_ ? yes/no ')
ambiguous_symbols = input('Исключать ли неоднозначные символы il1Lo0O ? yes/no ')
chars = ''


if digit_password == 'yes' or digit_password == 'y':
    chars += digits
if uppercase_alphabet == 'yes' or uppercase_alphabet == 'y':
    chars += uppercase_letters
if lowercase_alphabet == 'yes' or lowercase_alphabet == 'y':
    chars += lowercase_letters
if other_symbols == 'yes' or other_symbols == 'y':
    chars += punctuation
if ambiguous_symbols == 'yes' or ambiguous_symbols == 'y':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')


def generate_password(chars):
    password = ''
    for _ in range(quantity_passwords):
        for _ in range(len_password):
            password += random.choice(chars)
        password += ' '
    return password


print(generate_password(chars))
