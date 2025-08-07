import random
import string

length = int(input("Enter password length: "))


characters = string.ascii_letters + string.digits


password_list = random.sample(characters, length)


random.shuffle(password_list)


password = ''.join(password_list)

print(f"Generated password: {password}")
