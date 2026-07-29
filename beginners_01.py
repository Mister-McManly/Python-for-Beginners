import random

name = input("Please type your name here--> ")
greeting = random.randint(1, 6)
if greeting == 1:
    print("Hello there,", name + "!")
elif greeting == 2:
    print("Salutations,", name + "!")
elif greeting == 3:
    print("Whatsup,", name + "?")
elif greeting == 4:
    print("Greetings,", name + "!")
elif greeting == 5:
    print("Howdy,", name + "!")
else:
    print("Welcome,", name + "!")