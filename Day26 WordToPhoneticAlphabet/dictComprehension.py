sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

words = sentence.split()

# list_name = {new_key:new_value for (key, value) in dictionary.items() if condition}
result = {word:len(word) for word in words}

print(result)

