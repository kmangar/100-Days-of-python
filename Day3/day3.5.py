# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
truelove = (name1.lower()+name2.lower())
# print(truelove)
t = truelove.count('t')
r = truelove.count('r')
u = truelove.count('u')
e = truelove.count('e')

l = truelove.count('l')
o = truelove.count('o')
v = truelove.count('v')
e = truelove.count('e')

score = int(str(t+r+u+e) +str(l+o+v+e))

if  score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 < score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

