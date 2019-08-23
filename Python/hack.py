#Opens a file. You can now look at each line in the file individually with a
#statement like "for line in f:

f = open("dictionary.txt").read()

print("Can your password survive a dictionary attack?")

#Take input from the keyboard, storing in the variable test_password

#NOTE - You will have to use .strip() to strip whitespace and newlines from the file and passwords

test_password = input("Type in a trial password: ")
#Write logic to see if the password is in the dictionary file below here:
test_password.strip()

if test_password in f:
    print("You've been hacked! Need a stronger password")

if test_password not in f:
    print("You win!")
