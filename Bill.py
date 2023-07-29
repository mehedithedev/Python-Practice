print('Welcome to pizza deliveris')
size = input('What siize do you want ? S, M, L')
add_peparoni = input("Do you want to add pepperoni? Y or N")
extra_cheese = input('Do you want extra cheese? Y or N')

bill = 0
if size=="S":
    bill= bill+15
elif size=="M":
    bill= bill+20
elif size=="L":
    bill= bill+25
else:
    print('Enter S, M or L in order to proceed further')



if add_peparoni == 'Y':
    if size == "S":
        bill += 2
    elif size == 'M':
        bill += 3
    elif size == "L":
        bill +=4
elif add_peparoni=="N":
    print("Okay we won't add pepperoni")

else:
    print('Choose between Y or N')




if extra_cheese == 'Y':
    if size == "S":
        bill += 2
    elif size == 'M':
        bill += 3
    elif size == "L":
        bill +=4
else:
    print('Choose between Y or N')




print(f"Your final bill is: ${bill }")