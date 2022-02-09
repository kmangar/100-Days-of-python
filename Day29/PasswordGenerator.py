from random import choice, randint, shuffle
import pyperclip
import UI
from tkinter import *


class PasswordGen():

    def __init__(self):
        self.alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split() + "a b c d e f g h i j k l m n o p q r s t u v w x y z".upper().split()
        self.numbers = "0 1 2 3 4 5 6 7 8 9".split()
        self.characters = "` ~ ! @ # $ % ^ & * ( ) - _ = + | , . / < > ? ; : '  ".split()

        self.letter_list = [choice(self.alphabet) for _ in range(randint(8, 10))]

        self.char_list = [choice(self.characters) for _ in range(randint(2, 4))]

        self.num_list = [choice(self.numbers) for _char in range(randint(2, 4))]

        self.password_list = self.letter_list + self.char_list + self.num_list
        self.shuffle(self.password_list)

        self.password_entry = UI.password_entry


    def password_gen(self):
        password = ''.join(self.password_list)
        self.password_entry.delete(0, END)
        self.password_entry.insert(0, password)
        pyperclip.copy(password)


