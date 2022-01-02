# try to get user input and if user does not input a number give them an error

try:
    # ask the user for input and convert it from string to int
    number = int(input("Which number do you want to check?"))
    # even number are have no remainder when divisable by 2
    # print wheather or not it is even or odd
    if number % 2 == 0:
        print("This is an even number.")
    else:
        print("This is an odd number.")
except(ValueError):
    # if the user input is not a number and can not be converted let the user know it is not a number
    print("Error: Not a Number")






