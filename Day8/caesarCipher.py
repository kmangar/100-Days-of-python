alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for x in plain_text:
        cipher_text += alphabet[alphabet.index(x) + shift_amount]
    print(f"The encoded text is {cipher_text}")
    # TODO-1-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift
    #  amount and print the encrypted text. e.g. plain_text = "hello" shift = 5 cipher_text = "mjqqt" print output:
    #  "The encoded text is mjqqt"

    # How do you get the index of an item in a list:
    # https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    # 🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛


# TODO-2: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for x in text:
        plain_text += alphabet[alphabet.index(x) - shift_amount]
# TODO-2-1: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift
#  amount and print the decrypted text. e.g. cipher_text = "mjqqt" shift = 5 plain_text = "hello" print output: "The
#  decoded text is hello"
    print(f"The decoded text is {plain_text}")

# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.
if direction == "endode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
