# Vigenere-Cipher
Programmed by: John Carlo Ablay

CMPE 103 OBJECT-ORIENTED PROGRAMMING
LAB EXERCISE No 1 – PYTHON STRINGS
PROBLEM 3 - The Vigenère Cipher  
The Vigenère Cipher works as follows:

Your key is a keyword, which you then translate into corresponding letter values 0 – 25. Then, to encrypt, write your message on one row (letters 0 – 25), and repeatedly write the keyword below it, adding each column, taking the result mod 26. These resultant numbers are the ciphertext. Here is a small example:
Message: LETSGOTOTHESHOW 11  4 19 18  6 14 19 14   19    7   4    18    7   14     22
Key: TICKET                                    19 8   2 10 4  19 19   8    2   10   4   19   19    8       2
Add: 30 12 21 28 10 33 38 22 21 17 8 37 26 22 24
Mod: 4 12 21 2 10 7 12 22 21 17 8 11 0 22 24
Ciphertext: E M V C K H M W V R I L A W Y

Write a program that asks the user for the plaintext (all uppercase letters, no spaces) and the keyword (all uppercase letters) and produce the ciphertext using the Vigenère cipher. Give the output of your program for the following message and key:

Message: THISISTHELASTTASKHOORDAY
Key: KNIGHTS
 

#PSEUDOCODE
#Make a dictionary of every letter with it corresponding base value.
#Make a variable with True value to ask the user if they want to try the program again 
#Title of Program using pyfiglet
#Enumerate all the ASCII value and will be inserted inside the empty dictionary
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
#   End the program with an exit message
