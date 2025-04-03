import random
import string

def generate_password(length):
    pool = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.sample(pool, length))
    return password

user_input = int(input('Enter the password length (<= 94): '))
print(generate_password(user_input))
