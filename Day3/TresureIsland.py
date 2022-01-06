print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
name = input("Enter Your Name: ")
print(f"Welcome to Treasure Island {name}.")
print("Your mission is to find the treasure.")
#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
play = (input("ready to play?")).lower()

if play == 'yes' or play == 'y':
    Left_Right = (input("Start your journey, Left or Right? ")).lower()
    if Left_Right == 'right' or Left_Right == 'r':
        print(f"{name} you have lot to Learn!!")
    else:
        ocean = (input("your in the beach, swim or wait?")).lower()
        if ocean == 'swim' or ocean.count('s') > 0 :
            print(f"{name} got eaten by a shark, GAME OVER! :[")
        else:
            door = (input("You see doors, red, blue, green?")).lower()
            if door == 'blue' or door == 'b':
                print(f"congratulations {name}, you found the One Piece Treasure")
            else:
                print(f"{name} fell into a pit, GAME OVER!! :O")
else:
    print("Come Again")

