import random
print("Welcome to the PyPassword Generator")
alpha = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
alphaUpper = "a b c d e f g h i j k l m n o p q r s t u v w x y z".upper().split()
numbers = "0 1 2 3 4 5 6 7 8 9".split()
characters = "` ~ ! @ # $ % ^ & * ( ) - _ = + | , . / < > ? ; : '  ".split()

letters = int(input("How many Letters do you want in your password?\n"))
chars = int(input("How many symbols do you want in your password?\n"))
num = int(input("How many numbers do you want in your password?\n"))
password = []
alphabet = alpha + alphaUpper
x = 0
while x < letters:
    password.append(random.choice(alphabet))
    x += 1
x = 0
while x < chars:
    password.append(random.choice(characters))
    x += 1
x = 0
while x < num:
    password.append(random.choice(numbers))
    x += 1

print(password)
random.shuffle(password)

password = ''.join(password)
print(password)
#print(f"{alpha} \n {alphaUpper} \n {numbers} \n {characters}")

