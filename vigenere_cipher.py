#John Carlo Ablay
#BSCPE 1-5
#Program 3: Vigenere Cipher

import pyfiglet
import emoji 
import string 

author_name = ("PROGRAMMED BY: JOHN CARLO ABLAY")
name = author_name.center(100)
print(name)

dict = {}
#PSEUDOCODE
#Make a dictionary of every letter with it corresponding base value.
#this variable won't be used in the program, this will just be my guide for the letter and its corresponding base value.
dict_made = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' : 6, 'H' : 7, 'I' : 8, 'J' : 9, 'K' : 10,
            'L' : 11, 'M' : 12, 'N' : 13, 'O' : 14, 'P' : 15, 'Q' : 16, 'R' : 17, 'S' : 18, 'T' : 19, 'U' : 20, 'V' : 21,  'W' : 22,
            'X' : 23, 'Y' : 24, 'Z' : 25}
#Make a variable with True value to ask the user if they want to try the program again 
moredata = "yes"
while moredata == "yes":

#Title of Program using pyfiglet 
    result = pyfiglet.figlet_format("VIGENERE CIPHER", font = "bubble" )
    print(result)
#Enumerate all the ASCII value and will be inserted inside the empty dictionary
for i, char in enumerate(string.ascii_uppercase):
    dict[i] = char
#Make a function named loop_key to get the list of key

#Make a function named cipher_txt to get the list of cipher text
#Make a function named add_bot to get the sum of the values of each character
#Make a function named mod_bot to decrypt the message inputted by the user
#Ask the user for their input
#Ask the user for their keyword
#Print the key
#Print the Ciphertext
#Make an empty variable for num_message and num_key
#Use for loop to get the number of base of each character of message in the dictionary
#Use for loop to get the number of base of each character of keyword in the dictionary
#Print the Message
#Print the Keyword
#Print the Sum
#Print the Mod 
#Print the Cipthertext
#Ask the user if they want to use the program again
#   if true
#       Run the program again
    moredata = str(input("Do you want to try again? (yes or no): "))

#   End the program with an exit message

print("\nThank you for using my program!")
print(emoji.emojize(":grinning_face_with_big_eyes:"))
