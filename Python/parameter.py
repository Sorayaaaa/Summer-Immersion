# --- Define your functions below! ---

# The chatbot introduces itself and gives the user instructions.

def intro():
    print("Hi, my name is ChatBot. Let's talk!")
    print("Type something and hit enter.")
    print("Type 'poem' if you want to hear a poem")


# Choose a response based on the user's input.

def process_input(response):
    if (response == is_valid_input):
        return True
    elif (response == "poem"):
        say_poem()
    else:
        say_default()

# Display a greeting message to the user.

def say_greeting():
  print("Hey there!")

# Default

def say_default():
  print("Cool!")
  return False

#Display poem to user.

def say_poem():
    print("I contimplate if I should stay")
    print("Away..")
    print("'From whom?' you may say.")
    print("Well...")
    print("I replay")
    print("Everyday in May")
    print("To my dismay")
    print("A month that will go down in infamy")
    reply= input("Did you enjoy my poem? ")
    if (reply == "yes"):
        print("thank you")
        return True
# Display a default message to the user.

def is_valid_input(greet):
    greeting:["hi", "hello", "hey"]
    if greet in greeting:
        say_greeting()

# --- Put your main program below! ---

def main():
  intro()
  while True:
    answer = input("What will you say? ")
    process_input(answer)
    is_valid_input(answer)



# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
