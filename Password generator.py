import random

chars = ["a", "b", "c", "d", "e"]
nums = [1,2,3,4,5,6,7,8,9,10]
syms = ["!", "@", "#", "$", "%"]
print("Welcome to password generator by Mehedi Hasan")
len_digit = int(input("How many digits do you want on your password? \n"))
len_char = int(input("How many characters do you wanna include? \n"))
len_num = int(input("How many numbers you want in your password? \n"))
len_sym = int(input("How many symbols you wanna use? \n"))

password = ""

# Easy password generator:
for char in range(1, len_char+1):
    rand_char = random.choice(chars)
    password = rand_char+password
# print(password)

for num in range(1, len_num+1):
    rand_num = str(random.choice(nums))
    password = rand_num+password
# print(password)

for sym in range(1, len_sym+1):
    rand_sym = str(random.choice(syms))
    password = rand_sym+password
# print(f"Password from easy password generator: {password}")



#Hard password generator:
password_list = []

for char in range(1, len_char+1):
    rand_char = random.choice(chars)
    password_list.append(rand_char)
# print(password_list)

for num in range(1, len_num+1):
    rand_num = random.choice(nums)
    password_list.append(rand_num)
# print(password_list)

for sym in range(1, len_sym+1):
    rand_sym = random.choice(syms)
    password_list.append(rand_sym)


# print(f"Easy Password: {password_list}")
random.shuffle(password_list)
# print(f"Hard Password: {password_list}")

final_password = ""
for item in password_list:
    final_password += str(item)
print(f"Here's the password. Just copy and use -->  {final_password}")