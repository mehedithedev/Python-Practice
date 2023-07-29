import random

chars = ["a", "b", "c", "d", "e"]
nums = [1,2,3,4,5,6,7,8,9,10]
syms = ["!", "@", "#", "$", "%"]
print("Welcome to password generator by Mehedi Hasan")
len_digit = int(input("How many digits do you want on your password? \n"))
len_char = int(input("How many characters do you wanna include? \n"))
len_num = int(input("How many numbers you want in your password? \n"))
len_sym = int(input("How many symbols you wanna use? \n"))

password = []

for char in range(1, len_char):
    randomCharacter = random.choice(chars)
    password.append(randomCharacter)
print(password)

for num in range(1, len_num+1):
    randomNumber = random.choice(nums)
    password.append(randomNumber)
print(password)
