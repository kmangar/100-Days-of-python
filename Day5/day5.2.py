# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

# defined a variable and assign it to the first value in the list and use the for loop to check for any
# value greater or equal to the assigned variable
highest_value = student_scores[0]

for x in student_scores:
    if x >= highest_value:
        highest_value = x
print(f"The highest score in the class is: {highest_value}")



