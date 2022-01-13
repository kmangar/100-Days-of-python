#Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
a = 0
temp = []
display = []
for x in chosen_word:
    display.append("_")
    temp += chosen_word[a]
    a += 1

# TODO-1: - Use a while loop to let the user guess again. The loop should only
# stop once the user has guessed all the letters in the chosen_word and
# 'display' has no more blanks ("_"). Then you can tell the user they've won.
print(temp)

# Check guessed letter

while "_" in display:
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
            print(display)

if display == temp:
    print("You win")
else:
    print("You Loose")
