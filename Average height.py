# fruits = ["apple", "mango","orange" ]
# for fruit in fruits:
#     print(fruit+" Pie")
#     print(fruits)

# student_heights = 156 178 165 171 187
heightOfStudents = input("Input a list of student height").split()
# print(heightOfStudents)
for n in range(0 , len(heightOfStudents)):
    heightOfStudents[n] = int(heightOfStudents[n])
total_height = 0
for height in heightOfStudents:
    total_height += height
print(total_height)


number_of_students = 0
for student in heightOfStudents:
    number_of_students += 1
print(number_of_students)
# total_height = sum(heightOfStudents)
# numberOfStudents = len(heightOfStudents)
averageHeight = round(total_height / number_of_students)
print(averageHeight) 
