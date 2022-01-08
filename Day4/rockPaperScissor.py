rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
import random

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors."))

lmap = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''', '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''', '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']
ai = random.randint(0, 2)


if user_input >= 3 or user_input < 0:
    print("You typed invalid number, you Loose")
else:
    print(lmap[user_input])
    print(f"computer chose: {lmap[ai]}")
    if user_input == 0 and ai == 1:
        print("You loose")
    elif user_input == 0 and ai == 2:
        print("You win")
    elif user_input == 1 and ai == 0:
        print("You win")
    elif user_input == 1 and ai == 2:
        print("You loose")
    elif user_input == 2 and ai == 0:
        print("You Loose")
    elif user_input == 2 and ai == 1:
        print("You win")
    else:
        print("It's a tie")
