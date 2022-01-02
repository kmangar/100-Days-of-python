import random

from art import logo, vs
from game_data import data


# make a function that returns a random instagram celebrity
def random_model():
    return random.choice(data)


# make a function that compares the two insta model and checks who has more follower and returns the one with the most
def higher_lower(model_a, model_b):
    if model_a['follower_count'] >= model_b['follower_count']:
        return 'a'
    else:
        return 'b'


# make a score and keep track of how many the user guess right
score = 0

# print the random model from the function and print their data
model1 = random_model()
model = model1

# print log
print(logo)

while True:
    print(f"Compare A: {model['name']}, a {model['description']}, from {model['country']}")

    # print vs
    print(vs)

    # print another random Instagram celebrity with their data cannot be the same as the last

    model2 = random_model()
    if model == model2:
        model2 = random_model()

    print(f"Compare B: {model2['name']}, a {model2['description']}, from {model2['country']}")

    # ask user for who has more follower between the two
    guess = input("Who has more followers? Type 'A' or 'B':").lower()

    winner = higher_lower(model, model2)

    # if the user guess was right continue and print random user from the
    # inst-gram data but not the one that was previously picked
    if winner >= guess:
        score += 1
        print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYou're right! Current score: {score}.")
        model = model2
    else:
        print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nSorry, that's wrong. Final score: {score}.\n\n\n\n\n\n\n\n\n\n\n")
        exit()
