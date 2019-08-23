# Creates the dictionary to store responses.

import json

def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)

users = {}
def main():
    # Example
    # './' represents the current directory so the directory save-file.py is in
    # 'test' is my file name


    # Below, write code that will pose the survey questions from the student prompt
    #to a user. Your program should save user input as a dictionary.


    for i in range(4):

            greet()
            q1()
            q2()
            q3()
            q4()
            writeToJSONFile('./','file-name',users)
            print(users)


def greet():
    print("Hello! Are you ready to take a survey?")
    answer = input("Type your name ")
    print(answer , "Nice to meet you")
    users["name"] = answer

def q1():
    answer = int(input("What is your age?"))
    print("Next question")
    users["age?"] = answer

def q2():
    answer = int(input("How many people live in your home more than 50% of the time?"))
    print("Next question")
    users["How many people live in your home more than 50% of the time?"] = answer

def q3():
    answer = int(input("How many hours per week do you spend on the phone?"))
    users["How many hours per week do you spend on the phone?"] = answer

def q4():
    answer = input("What is your favorite color?")
    users["favorite color?"] = answer

if __name__ =="__main__":
    main()



# Print the context of the dictionary.
#print(answers)
