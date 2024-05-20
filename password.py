#Import random module
import random
#Import the shuffle method
from random import shuffle
#List of special characters
special_characters = ['!','@','#','$','%','^','&','*']
#List of the characters in the alphabet with upper and lowercase
alphabets = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'D', 'E', 'e', 
             'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 
             'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 
             'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 
             'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 
             'Z', 'z']
#List of numbers from 0 to 9
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#A while loop is added if the user wishes to run the program again
while True:
    #Function that takes in random special characters from the special characters list
    def random_special(i, j):
        return random.choices(j, k=i)

    #Function that takes in random letters from the alphabets list
    def random_alphabet(a, b):
        return random.choices(b, k=a)
    #Function that takes in random numbers from the numbers list
    def random_number(x, y):
        return random.choices(y, k=x)
    #Function to shuffle the list containing all the random characters 
    def shuffle_list(password_characters): 
        shuffle(password_characters)
        return password_characters

    #A while loop to validate input
    valid_input = False
    while not valid_input:
        try: 
            #The password must be between 10 and 20 characters long
            limit = int(input("How long do you want your password to be? (Min 10, Max 20): ")) 
            #Check to see if input is less than 10 characters or more than 20 characters
            if limit <= 20 and limit >= 10:
                #Accept the input if it's valid
                valid_input = True
            else:
                #Inform the user about the parameters for valid input
                print("Please enter a length in between 10 and 20. ")
        except ValueError:
            #Handle errors when the user inputs a non-integer such as a string
            print("Invalid input. Please enter a valid number.")
            

    #Set variables equal to 1
    special_chars = 1
    alphabet_chars = 1
    num_chars = 1
    #Determing the number of characters the password will have
    #Depends on the length of the password the user wants 
    #If length is 10, 11, or 12 -- have 2 special characters, 5 alphabets, 3 numbers
    if limit == 10: 
        special_chars = 2
        alphabet_chars = 5
        num_chars = 3
    elif limit == 11: 
        special_chars = 2
        alphabet_chars = 5
        num_chars = 3
    elif limit == 12: 
        special_chars = 2 
        alphabet_chars = 5
        num_chars = 3
    #If length is 13, 14, or 15 -- have 3 special characters, 6 alphabets, 4 numbers
    elif limit == 13: 
        special_chars = 3 
        alphabet_chars = 6
        num_chars = 4
    elif limit == 14: 
        special_chars = 3
        alphabet_chars = 6
        num_chars = 4
    elif limit == 15: 
        special_chars = 3
        alphabet_chars = 6 
        num_chars = 4
    #If length is 16, 17, or 18 -- have 4 special characters, 7 alphabets, 5 numbers
    elif limit == 16: 
        special_chars = 4 
        alphabet_chars = 7
        num_chars = 5
    elif limit == 17: 
        special_chars = 4
        alphabet_chars = 7
        num_chars = 5
    elif limit == 18: 
        special_chars = 4 
        alphabet_chars = 7
        num_chars = 5
    #If length is 19 or 20 -- have 5 special characters, 8 alphabets, 6 numbers
    elif limit == 19: 
        special_chars = 5
        alphabet_chars = 8
        num_chars = 6
    elif limit == 20: 
        special_chars = 5
        alphabet_chars = 8
        num_chars = 6

#Loop through the lists and taken in a random number of characters depending on the if, elif statements
    for _ in range(special_chars): 
        i = _ + 1
        #res_special is a list
        res_special = random_special(i, special_characters) 

    for q in range(alphabet_chars):
        a = q + 1
        #res_alpha is a list
        res_alpha = random_alphabet(a, alphabets) 

    for z in range(num_chars): 
        x = z + 1
        #res_num is a list
        res_num = random_number(x, numbers)

    #Add all the characters to one list
    pass_characters = res_alpha + res_special + res_num 

    #Shuffle the list
    password = shuffle_list(pass_characters)
    #Output the password 
    print(*password, sep = '')
    
    run_again_valid_input = False
    while not run_again_valid_input:
        try:
            #Ask the user if they wish to run the program again
            run_again = input("Do you want to run the program again? (yes/no): ").lower() #Input is always lowercase
            #Check to see if input is a yes or no
            if run_again == 'yes' or run_again == 'no': 
                #Accept the input is it's valid
                run_again_valid_input = True 
            else: 
                #Inform the user to enter a yes or no as input
                print("Please enter 'yes' or 'no'. ") 
        except ValueError: 
            #Handle errors when the user does not input a string
            ("Please enter 'yes' or 'no'. ")

    #If the user does not wish to continue then print a thank you message and quit the program
    if run_again == 'no': 
        print("Thank you for using. ")
        break  
