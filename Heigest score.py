list_of_score= [45,55,96,69,24,87,98,48,81]
highest_score = 0
for score in list_of_score:
    if score > highest_score:
        highest_score = score
print(f"The highest score is : {highest_score}")