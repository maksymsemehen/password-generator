import random
import string

def generate_password(length):
    pool = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.sample(pool, length))
    return password

user_input = int(input('Enter the password length (<= 94): '))
result = generate_password(user_input)

with open('history.txt', 'a', encoding="utf-8") as file:
    file.write(result + '\n')
