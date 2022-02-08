# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

#Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# import pandas for reading csv
import pandas
# student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:

# read the csv file and store in nato_alphabet
nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
# make a phonetic dictionary {"A": "Alfa", "B": "Bravo"} format
nato_alphabet_dict = {row.letter:row.code for (index, row) in nato_alphabet.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# ask the user to input a word and make that word capitalized and store it in variable word

def generate_phonetic():
    word = input("Enter A word: ").upper()
    try:
        # using the dictionary get the phonetic at the letter and stor it in a list
        output_list = [nato_alphabet_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        # print the list
        print(output_list)

generate_phonetic()



