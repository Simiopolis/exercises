# Objective:
# Welcome to cipher day!
# write a program that can encrypt texts with an alphabetical caesar cipher.
# This cipher can ignore numbers, symbols, and whitespace.
# for extra credit, add a "decrypt" function to your program!
# Link:
# http://www.reddit.com/r/dailyprogrammer/comments/pkw2m/2112012_challenge_3_easy/

# Cipher, shifted leftwise by 3
cipher = 'defghijklmnopqrstuvwxyzabc'
ref = 'abcdefghijklmnopqrstuvwxyz'

plain_string = raw_input("Please insert a string to be encrypted: ")

encrypted_string = ''.join([cipher[ref.index(character)] for character in 
	list(plain_string) if character in cipher])

print "Encrypted string: " + encrypted_string
