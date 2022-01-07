
import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# len()-1 cuz the length is the total number of item on the list but if it counts from 0
# it should be len -1
random_picker = (random.randint(0, len(names)-1))
print(f"{names[random_picker]} is going to buy the meal today!")
